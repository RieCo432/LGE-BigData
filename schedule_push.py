import time
import json
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from shared_stuff import ClassClass
import requests
from pytz import country_timezones

PRODUCTION = True

scheduler = BackgroundScheduler(timezone=country_timezones("lu")[0])

scheduler.start()


def push_scheduled_lesson(destination_class, lessons):
    fcm = {"address": "https://fcm.googleapis.com/fcm/send", "key": "AIzaSyD0KrIb6z4KSB6nghPtA-bG-rJI4MOMhwo"}
    stdParas = {"targetPackage": "com.colinries.lge"}

    postRequestHeaders = {"Content-Type": "application/json", "Authorization": "key=" + fcm["key"]}

    classNotificationDataRAW = {"data": {"lessons": lessons},
                                "restricted_package_name": stdParas["targetPackage"],
                                "to": "/topics/intraPush" + destination_class,
                                "time_to_live": 600,
                                "collapseKey": "intrapush_lesson",
                                "tag": "intrapush_lesson"}

    classNotificationData = json.dumps(classNotificationDataRAW)
    classNotificationResult = requests.post(fcm["address"], data=classNotificationData, headers=postRequestHeaders)
    print(classNotificationResult.text)
    print(classNotificationResult)


now = datetime(2017, 10, 1, datetime.now().hour, datetime.now().minute)

if PRODUCTION:

    now = datetime.now()

    notification_times = [datetime(now.year, now.month, now.day, 7, 50),
                          datetime(now.year, now.month, now.day, 8, 45),
                          datetime(now.year, now.month, now.day, 9, 50),
                          datetime(now.year, now.month, now.day, 10, 45),
                          datetime(now.year, now.month, now.day, 11, 40),
                          datetime(now.year, now.month, now.day, 12, 30),
                          datetime(now.year, now.month, now.day, 13, 25),
                          datetime(now.year, now.month, now.day, 14, 20),
                          datetime(now.year, now.month, now.day, 15, 15)]

else:
    minute_1_td = timedelta(0, 60)

    now1 = now + minute_1_td
    now2 = now1 + minute_1_td
    now3 = now2 + minute_1_td
    now4 = now3 + minute_1_td
    now5 = now4 + minute_1_td
    now6 = now5 + minute_1_td
    now7 = now6 + minute_1_td
    now8 = now7 + minute_1_td
    now9 = now8 + minute_1_td

    notification_times = [datetime(now1.year, now1.month, now1.day, now1.hour, now1.minute),
                          datetime(now2.year, now2.month, now2.day, now2.hour, now2.minute),
                          datetime(now3.year, now3.month, now3.day, now3.hour, now3.minute),
                          datetime(now4.year, now4.month, now4.day, now4.hour, now4.minute),
                          datetime(now5.year, now5.month, now5.day, now5.hour, now5.minute),
                          datetime(now6.year, now6.month, now6.day, now6.hour, now6.minute),
                          datetime(now7.year, now7.month, now7.day, now7.hour, now7.minute),
                          datetime(now8.year, now8.month, now8.day, now8.hour, now8.minute),
                          datetime(now9.year, now9.month, now9.day, now9.hour, now9.minute)]


# for class_name in ClassClass.class_list
if PRODUCTION:
    for class_name in ClassClass.class_list:
        with open("classes/timetable_" + class_name + ".json", "r") as fin:
            all_class_lessons = json.load(fin)

            all_class_lessons_today = filter(lambda today_lesson: today_lesson["day"] == now.weekday(), all_class_lessons)

            new_job = [0, 0, 0, 0, 0, 0, 0, 0, 0]

            for i in range(0, 9):
                all_class_lessons_time = filter(lambda lesson: lesson["time"] == i, all_class_lessons_today)
                if len(all_class_lessons_time) != 0:
                    new_job[i] = scheduler.add_job(push_scheduled_lesson, 'date', run_date=notification_times[i],
                                                   args=[class_name,
                                                         all_class_lessons_time])
                    print(all_class_lessons_time)
                    print(new_job[i])

else:

    class_name = "1B"
    with open("classes/timetable_" + class_name + ".json", "r") as fin:
        all_class_lessons = json.load(fin)

        all_class_lessons_today = filter(lambda today_lesson: today_lesson["day"] == 0, all_class_lessons)

        new_job = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(0, 9):
            all_class_lessons_time = filter(lambda lesson: lesson["time"] == i, all_class_lessons_today)
            if len(all_class_lessons_time) != 0:
                new_job[i] = scheduler.add_job(push_scheduled_lesson, 'date', run_date=notification_times[i],
                                               args=[class_name,
                                                     all_class_lessons_time])
                print(all_class_lessons_time)
                print(new_job[i])

while True:
    time.sleep(60)
