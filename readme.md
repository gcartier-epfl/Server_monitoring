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

  
## Focntionnement du système   
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


