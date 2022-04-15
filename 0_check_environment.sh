#!/bin/bash

CURRENT_DIR=$(dirname $0)

MINIMUM_PYTHON3_VERSION=3.6

TRUE=1
FALSE=0

VENV_PATH=$CURRENT_DIR/venv

NEEDED_PACKAGES=(
    numpy
    pandas
    matplotlib
)

RECORD_FILE_IF_CHECK_ENVIRONMENT_PASS=$CURRENT_DIR/check_environment_ok.tmp

############################
#
#         echo
#
############################
BACKGROUND_WHITE='\e[0;30;47m'
BACKGROUND_RESET='\e[0m'

echo_highlight(){
    local str=$1
    echo -e "${BACKGROUND_WHITE}$1${BACKGROUND_RESET}";
}

############################
#
#        spinner
#
############################
spin(){
    spinner="/|\\-/|\\-"
    while :
    do
      for i in `seq 0 7`
      do
        echo -n "${spinner:$i:1}"
        echo -en "\010"
        sleep .2
      done
    done
}

pause_spin(){
    kill -s SIGSTOP $spin_pid
}

resume_spin(){
    kill -s SIGCONT $spin_pid
}

spin &
spin_pid=$!

############################
#
#      check python
#
############################
get_python_version(){
    local python_version=$(python3 -V | awk '{print $2}')
    echo $python_version
}

get_python_main_version(){
    local python_version=$1
    echo ${python_version%.*}
}

get_python_venv_command_name(){
    local python_main_version=$1
    echo "python"$python_main_version"-venv"
}

is_current_python_version_valid(){
    local python_version=$1
    
    if [ $python_version = $MINIMUM_PYTHON3_VERSION ]; then
        return $TRUE
    fi
    
    if [ $python_version = $(echo -e "$python_version\n$MINIMUM_PYTHON3_VERSION" | sort -V | head -n1) ]; then
        return $FALSE
    else
        return $TRUE
    fi
}

############################
#
# check virtual environment
#
############################
is_venv_installed(){
    local venv_command_name=$1
    local is_installed=$(dpkg -l | grep $venv_command_name)

    if [ -z "$is_installed" ]; then
        return $FALSE
    else
        return $TRUE
    fi
}

is_venv_package_installed(){
    local ret=$TRUE
    
    pip_installed_packages=$(pip list --format=columns)
    
    pause_spin
    
    for package in "${NEEDED_PACKAGES[@]}"; do
        check_package=$(echo $pip_installed_packages | grep -i $package)

        if [ -z "$check_package" ]; then
            echo "need to install package '$package' in venv"
            while true; do
                
                
                echo -ne "Do you want to install ${BACKGROUND_WHITE}$package${BACKGROUND_RESET} "
                echo -ne "automatically by pip at virtual environment?"
                read -p " [Y/N] " reply
                
                case $reply in
                    [Yy]* )
                        echo_highlight "pip install $package";
                        pip install $package;
                        exit_stat=$?
                        if [ $exit_stat -ne 0 ]; then
                            echo_highlight "ERROR: pip install $package failed, please fix it"
                            ret=$FALSE
                        fi
                        break;;
                    [Nn]* )
                        ret=$FALSE;
                        break;;
                esac
            done
        fi
    done
    
    resume_spin
    
    return $ret
}

###########################
#
#         main
#
###########################
trap 'echo "script terminated"; exit' SIGINT SIGTERM
trap 'kill -s SIGTERM 0' EXIT

python_version=$(get_python_version)
python_main_version=$(get_python_main_version $python_version)
python_venv_command=$(get_python_venv_command_name $python_main_version)
echo "current python version is $python_version"
echo "current python main version is $python_main_version"
echo "expected python venv package is $python_venv_command"

is_current_python_version_valid $python_version
is_version_valid=$?
if [ $is_version_valid -eq $FALSE ]; then
    echo_highlight "ERROR: please make sure python version is bigger than $MINIMUM_PYTHON3_VERSION, exiting..."
    exit 1
fi

is_venv_installed $python_venv_command
is_installed=$?
if [ $is_installed -eq $FALSE ]; then
    echo_highlight "ERROR: need to install $python_venv_command, exiting..."
    exit 1
fi

if [ ! -d "$VENV_PATH" ]; then
    echo_highlight "ERROR: there is no $python_venv_command folder($VENV_PATH) for this app"
    echo_highlight "please generate venv like: $ python3 -m venv venv"
    echo "exiting..."
    exit 1    
fi

source $VENV_PATH/bin/activate
ret=$?
if [ $ret -ne 0 ]; then
    echo_highlight "ERROR: activate venv failed, please check venv environment, exiting..."
    exit 1
fi

is_venv_package_installed
is_package_installed=$?
deactivate # deactivate venv

if [ $is_package_installed -eq $FALSE ]; then
    echo_highlight "ERROR: need to install lacked package, exiting..."
    exit 1
fi

echo "simple environment checks done"
touch $RECORD_FILE_IF_CHECK_ENVIRONMENT_PASS
