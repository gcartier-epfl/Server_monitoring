# Server Monitoring

## TO DO   
- Réfléchir à l'affichage 
  - D'abord dans un terminal  
  - Ensuite, peut-être dans un navigateur  
- Réfléchir aux données à afficher en fonction des serveurs  

## Affichage dans un terminal  

### Librairies python disponibles pour l'affichage  
- textual  
- urwid (example : s-tui)  

### Données à afficher des Serveurs / Workstation
- OS
- Online  
- Charge :
  - CPU
  - GPU    
- Température  
- Network :  
  - up / Down
- Etat des disques  
  - Espace utilisé / Disponible  
  - Volume online
- Version :  
  - firmware  
  - CUDA  
  - Python  
  - ...     

  
## Fonctionnement du système   
- Exécuter des scripts sur les serveurs en tant que *daemon* / services :  
> voir  https://stackoverflow.com/questions/1603109/how-to-make-a-python-script-run-like-a-service-or-daemon-in-linux  

- Sur chaque serveur/machine :  
  - Avoir un script qui récupère les différentes informations importantes et les dump dans un fichier JSON  
  - Avoir un autre script qui sert de client REST pour envoyer le contenu du fichier au serveur  

- Scheduler de job : crontab  
  - https://crontab.guru/#*_*_*_*  
  - https://cronitor.io/guides/cron-jobs?utm_source=crontabguru&utm_campaign=cron_reference  

- Test sur la VM (wiki) dans `/var/Server_monitoring`  
- Edition de crontab avec `crontab -e`  

- Web server python : __uvicorn__
> Utilisé directement dans le script python 
> `host=0.0.0.0` et `port=8000` => Accepte toutes les connections. Voir pour utiliser les ip précises de chaque serveur pour `host`.  
  
- Running the server uvicorn as a service systemd : https://github.com/encode/uvicorn/issues/678
> Créer son propre service systemd `https://www.shubhamdipt.com/blog/how-to-create-a-systemd-service-in-linux/`

:arrow_right: Service systemd `server_monitor.service` up and running : Requêtes fonctionnent même en étant log out de la VM. :tada:

## Installation
- :warning: Utiliser le localuser comme user et owner du système me semble plus adapté.

- Création du venv

- Installation (utiliser un fichier ressource.txt)  
  - crontab (via python-crontab ?)
  - fastapi 
  - uvicorn  
  
- Ajout du cron-job  

- Copie du service dans systemd 
- Démarrage du service 
- check du status 
- Enable du service au boot  

### Procédure d'installation  
- __Pour la partie CENTRAL :__
  - Dans le Dockerfile : 
    - `git clone` dans le `/home` 
    - `mkdir Server_monitoring` dans le `/home` 
    - Création et activation du venv  
    - Installation des paquets python

## Docker  
:warning:  
- `docker run` créé un nouveau container à partir d'une image  
- `docker start` démarre un nouveau container précédemment stoppé
  
- Exécuter des commandes depuis le container sur l'hôte : https://stackoverflow.com/questions/32163955/how-to-run-shell-script-on-host-from-docker-container

## Visualisation des données  
- voir __Grafana__  
  - :arrow_right: Impliquera surement de mettre les données dans une base de données propre type MariaDB


## TO DO   
- Contrôle d'erreurs