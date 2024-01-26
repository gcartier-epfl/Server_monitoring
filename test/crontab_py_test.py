from crontab import CronTab 

with CronTab( user = 'gael' ) as cron : 
    job = cron.new( command = "echo $(date) >> /home/gael/test.txt" )
    job.minute.every(1)

print( "cronjob added" )
