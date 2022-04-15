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
        
        source venv/bin/activate # activate virtual environment
        
        pip install --upgrade pip
        
        deactivate # deactivate virtual environment

* check your environment for needed packages

        ./0_check_environment.sh

* visualize data

        source venv/bin/activate # activate virtual environment
        
        python3 ./visualize_data.py
        
        deactivate # deactivate virtual environment
        
* see output result in output/*