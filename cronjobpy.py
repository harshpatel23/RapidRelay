from crontab import CronTab

cron = CronTab(user='tanay')
job = cron.new(command='/home/tanay/Projects/BugBox/upload_data.py >> /var/log/myjob.log 2>&1')
job.minute.every(1)

cron.write()
