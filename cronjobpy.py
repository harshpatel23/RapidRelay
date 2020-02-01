from crontab import CronTab

cron = CronTab(user='tanay')
job = cron.new(command='/home/tanay/Projects/BugBox/upload_data.py >> /home/tanay/Projects/BugBox/logs.txt 2>&1')
job.minute.every(5)

cron.write()
