from crontab import CronTab

cron = CronTab(user='username')
job = cron.new(command='myjob.sh >> /var/log/myjob.log 2>&1')
job.minute.every(1)

cron.write()