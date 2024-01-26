#!/bin/bash 

docker run -it --rm --name collector_dock --mount type=bind,source="$(pwd)"/mnt,target=/root/mnt server_monitor:0.1;