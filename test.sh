#!/bin/bash

# DISTRI=$(. /etc/os-release; echo $ID)
# echo $DISTRI

# CRON_JOBS="$(crontab -l)"
# CRONJOB="SHELL=/bin/bash\n*/5     *       *       *	*    	cd /var/users/gcartier/Server_monitoring/collector/ && python3 /var/users/gcartier/Server_monitoring/collector/collector_data.py"

# if [ "$CRON_JOBS" = "$(echo -e $CRONJOB)" ]; then
#     echo ">>> The collector cronjob is already installed";
# else
#     echo ">>> Cronjob installation"
#     # (sudo crontab -u $USER -l; echo -e "$CRONJOB" ) | sudo crontab -u $USER - 
# fi


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


if is_redhat_like; then 
    echo True;
else 
    echo False;
fi