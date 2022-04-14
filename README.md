### Environment

* Ubuntu 18.04

* python3.6 + pip + virtual environment


### Preparation

* install pip

        sudo apt-get update

        sudo apt-get install python3-pip

* install virtual environment for python3

        sudo apt-get install python3-venv

* create virtual environment

        python3 -m venv venv
        
        source venv/bin/activate
        
        pip install --upgrade pip

* check needed packages on your environment

        ./0_check_environment.sh
