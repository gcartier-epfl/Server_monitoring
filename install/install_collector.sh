#!/bin/bash  

USER="gcartier" 
GROUP="gcartier" 
WORKSPACE="/var/users/gcartier/" 
COLLECTOR_PATH="/var/users/gcartier/collector/"
VENV_NAME=".env"

if [ ! -d "$(COLLECTOR_PATH)" ]; then
    sudo mkdir -p "$(COLLECTOR_PATH)";
    sudo chown "$(USER)":"$(GROUP)" -r "$(WORKSPACE)"
fi

cp ../collector/*.py "$(COLLECTOR_PATH)"
python3 -m pip install virtualenv 
virtualenv "$(WORKSPACE)"/"$(VENV_NAME)" 
source "$(WORKSPACE)"/"$(VENV_NAME)"/bin/activate