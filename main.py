import helper
import schedule
import time
import threading

from schedule import repeat, every

@repeat(every(5).seconds)
def task():
    print("Doing something...", helper.get_time())

def start_thread():
    job_thread = threading.Thread(target=task)
    job_thread.start()
    

    
    

#schedule.every(5).seconds.do(task).tag('my_tag')
#schedule.every(10).seconds.until('19:00').do(task)')
#schedule.every(10).seconds.until(datetime(2027,1,1)).do(task)')

schedule.every().monday.at('10:30').do(task)

my_tag = schedule.get_jobs('my_tag')
job = schedule.every().hour.at(':30').do(task)
print(my_tag)
#schedule.cancel_job(job)

print(schedule.get_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)
