import helper
import schedule
import time

from schedule import repeat, every

@repeat(every(5).seconds)
def task():
    print("Doing something...", helper.get_time())

#schedule.every(5).seconds.do(task)

job = schedule.every().hour.at(':30').do(task)

schedule.cancel_job(job)

print(schedule.get_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)
