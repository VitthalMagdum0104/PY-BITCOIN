from apscheduler.schedulers.background import BackgroundScheduler
from bitcoin import send_whatsapp, client, message
import time

scheduler = BackgroundScheduler(timezone="Asia/kolkata")

scheduler.start()

job = scheduler.add_job(send_whatsapp, "cron", [
                        client, message], hour="17", minute="07")

while True:
    time.sleep(1)
