#!/bin/bash  

docker create -i --name collector_dock --mount type=bind,source="$(pwd)"/mnt,target=/root/mnt server_monitor:0.1;

