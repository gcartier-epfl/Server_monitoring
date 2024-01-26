FROM python:alpine3.19
WORKDIR /root/ 
ADD alpine_bashrc.txt ./
RUN mv alpine_bashrc.txt .bashrc && apk update && apk upgrade && apk add git && apk add --no-cache bash && apk add bash-completion && apk add bash-doc && apk add shadow && chsh -s /bin/bash root && bash
CMD bash