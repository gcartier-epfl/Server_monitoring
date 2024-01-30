#!/bin/bash

# DISTRI=$(. /etc/os-release; echo $ID)
# echo $DISTRI

CRON_JOBS="$(crontab -l)"
CRONJOB="SHELL=/bin/bash\n*/5     *       *       *	*    	cd /var/users/gcartier/Server_monitoring/collector/ && python3 /var/users/gcartier/Server_monitoring/collector/collector_data.py"

if [ "$CRON_JOBS" = "$(echo -e $CRONJOB)" ]; then
    echo ">>> The collector cronjob is already installed";
else
    echo ">>> Cronjob installation"
    # (sudo crontab -u $USER -l; echo -e "$CRONJOB" ) | sudo crontab -u $USER - 
fi