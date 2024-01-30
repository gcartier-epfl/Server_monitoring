#!/bin/bash  

USER="gcartier" 
GROUP="gcartier" 
WORKSPACE="/var/users/gcartier/Server_monitoring" 
COLLECTOR_PATH=$WORKSPACE/collector/
VENV_NAME=".env"


if [ ! -d $COLLECTOR_PATH ]; then
    sudo mkdir -p $COLLECTOR_PATH;
    sudo chown -R $USER:$GROUP $WORKSPACE
fi

cp collector/*.py $COLLECTOR_PATH
python3 -m pip install virtualenv 
virtualenv $WORKSPACE/$VENV_NAME 
source $WORKSPACE/$VENV_NAME/bin/activate #FONCTIONNE POUR LE TEMPS D'EXECUTION DU SCRIPT

# Installation des paquets python  
python3 -m pip install -r requirements.txt

# Ajout du cronjob au crontab  
CRONJOB="SHELL=/bin/bash\n*/5     *       *       *	*    	cd /var/users/gcartier/Server_monitoring/collector/ && python3 /var/users/gcartier/Server_monitoring/collector/collector_data.py"
(crontab -u $USER -l; echo -e "$CRONJOB" ) | crontab -u $USER - 