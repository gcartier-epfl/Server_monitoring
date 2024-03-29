#!/bin/bash  

USER="gcartier" 
GROUP="gcartier" 
WORKSPACE="/var/users/gcartier/Server_monitoring" 
COLLECTOR_PATH=$WORKSPACE/collector/
VENV_NAME=".env"


function is_debian_like {
    DISTRI=$(. /etc/os-release; echo $ID)
    DISTRI=${DISTRI,,} # TO LOWER CASE
    echo $DISTRI
    if [[ "$DISTRI" =~ ^(debian|ubuntu|mint)$ ]]; then 
        return 0; # 0 = true
    else 
        return 1;
    fi
}

function is_redhat_like {
    DISTRI=$(. /etc/os-release; echo $ID)
    DISTRI=${DISTRI,,} # TO LOWER CASE
    if [[ "$DISTRI" =~ ^(redhat|rhel|fedora|centos)$ ]]; then 
        return 0;
    else 
        return 1;
    fi
}

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
CRON_JOBS="$(crontab -l)"
CRONJOB="SHELL=/bin/bash\n*/5     *       *       *	*    	cd /var/users/gcartier/Server_monitoring/collector/ && python3 /var/users/gcartier/Server_monitoring/collector/collector_data.py"

if [ "$CRON_JOBS" = "$(echo -e "$CRONJOB")" ]; then
    echo ">>> The collector cronjob is already installed";
else
    (sudo crontab -u $USER -l; echo -e "$CRONJOB" ) | sudo crontab -u $USER - 
fi

# Désactivation du firewall pour le port utilisé sur les distribution de type red Hat
if is_redhat_like; then 
    sudo firewall-cmd --add-port=8000/tcp
    sudo firewall-cmd --add-port=8000/udp
fi 


# Install the systemd service
if [ ! -f /etc/systemd/system/server_monitor.service ]; then 
    sudo cp server_monitor.service /etc/systemd/system 
    sudo systemctl daemon-reload 
    sudo systemctl start server_monitor.service 
    sudo systemctl status server_monitor.service 
    sudo systemctl enable server_monitor.service
fi
