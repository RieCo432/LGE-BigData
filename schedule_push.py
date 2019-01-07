#!/usr/bin/python
#coding=utf-8

from __future__ import print_function

import time
import json
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from shared_stuff import ClassClass
import requests
from pytz import country_timezones
import os
from random import randint

PRODUCTION = True

if datetime(2019, 1, 7) <= datetime.now() < datetime(2019, 2, 16):
	vacation = False
elif datetime(2019, 2, 25) <= datetime.now() < datetime(2019, 4, 6):
	vacation = False
elif datetime(2019, 4, 23) <= datetime.now() < datetime(2019, 5, 25):
	vacation = False
elif datetime(2019, 6, 3) <= datetime.now() < datetime(2019, 7, 13):
	vacation = False
else:
	vacation = True

# print(vacation)

proj_dir = os.path.dirname(os.path.abspath(__file__))

log_file = open(proj_dir + "/output.log", "a")

print(str(datetime.now()) + " scheduler script started\n", file=log_file)

executors = {
        'default': {'type': 'threadpool', 'max_workers': 500}
    }


scheduler = BackgroundScheduler(timezone=country_timezones("lu")[0], deamon=True, executors=executors)

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
    with open(proj_dir + "/fcm_output.log", "a") as fcm_log:
        print(str(datetime.now()) + " " + destination_class + " " + str(classNotificationResult.text) + " " + str(lessons) + "\n", file=fcm_log)
        print(str(datetime.now()) + " " + destination_class + " " + str(classNotificationResult) + " " + str(lessons) + "\n", file=fcm_log)



if PRODUCTION:

    now = datetime.now()

    notification_times = [datetime(now.year, now.month, now.day, 7, 45, 0),
                          datetime(now.year, now.month, now.day, 8, 43, 0),
                          datetime(now.year, now.month, now.day, 9, 45, 0),
                          datetime(now.year, now.month, now.day, 10, 43, 0),
                          datetime(now.year, now.month, now.day, 11, 38, 0),
                          datetime(now.year, now.month, now.day, 12, 28, 0),
                          datetime(now.year, now.month, now.day, 13, 23, 0),
                          datetime(now.year, now.month, now.day, 14, 18, 0),
                          datetime(now.year, now.month, now.day, 15, 13, 0)]

else:
    now = datetime.now()


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

    notification_times = [datetime(now1.year, now1.month, now1.day, now1.hour, now1.minute, 0),
                          datetime(now2.year, now2.month, now2.day, now2.hour, now2.minute, 0),
                          datetime(now3.year, now3.month, now3.day, now3.hour, now3.minute, 0),
                          datetime(now4.year, now4.month, now4.day, now4.hour, now4.minute, 0),
                          datetime(now5.year, now5.month, now5.day, now5.hour, now5.minute, 0),
                          datetime(now6.year, now6.month, now6.day, now6.hour, now6.minute, 0),
                          datetime(now7.year, now7.month, now7.day, now7.hour, now7.minute, 0),
                          datetime(now8.year, now8.month, now8.day, now8.hour, now8.minute, 0),
                          datetime(now9.year, now9.month, now9.day, now9.hour, now9.minute, 0)]

if PRODUCTION and not vacation:
    new_job = []
    new_job_index = 0
    for class_name_original in ClassClass.class_list:
        class_name = class_name_original.replace("(", "-").replace(")", "-").replace(" ", "_")
        with open(proj_dir + "/classes/timetable_" + class_name + ".json", "r") as fin:
            all_class_lessons = json.load(fin)

            all_class_lessons_today = filter(lambda today_lesson: today_lesson["day"] == now.weekday(), all_class_lessons)

            new_job.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

            for i in range(0, 9):
                all_class_lessons_time = filter(lambda lesson: lesson["time"] == i, all_class_lessons_today)
                if len(all_class_lessons_time) != 0:
                    # split all push schedules into 5 groups and set them 3 seconds apart
                    run_date = datetime(notification_times[i].year,
                                        notification_times[i].month,
                                        notification_times[i].day,
                                        notification_times[i].hour,
                                        notification_times[i].minute,
                                        notification_times[i].second + (ClassClass.class_list.index(class_name_original)%5)*3)

                    new_job[new_job_index][i] = scheduler.add_job(push_scheduled_lesson, 'date', run_date=run_date,
                                               args=[class_name, all_class_lessons_time])

                    print(str(datetime.now()) + " " + class_name + " " + str(all_class_lessons_time) + "\n", file=log_file)
                    print(str(datetime.now()) + " " + class_name + " " + str(new_job[new_job_index][i]) + "\n", file=log_file)

            new_job_index = new_job_index + 1

    log_file.close()

    while True:
        time.sleep(10)
        #with open(proj_dir + "/loop_log.log", "a") as loop_log:
            #for job_array in new_job:
            #    for job in job_array:
        #    print(str(datetime.now()) + " " + str(scheduler.get_jobs()), file=loop_log)

elif not PRODUCTION:

    class_name = "1B-C-"
    with open(proj_dir + "/classes/timetable_" + class_name + ".json", "r") as fin:
        all_class_lessons = json.load(fin)

        all_class_lessons_today = filter(lambda today_lesson: today_lesson["day"] == 0, all_class_lessons)

        new_job = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(0, 9):
            all_class_lessons_time = filter(lambda lesson: lesson["time"] == i, all_class_lessons_today)
            if len(all_class_lessons_time) != 0:
                new_job[i] = scheduler.add_job(push_scheduled_lesson, 'date', run_date=notification_times[i],
                                               args=[class_name,
                                                     all_class_lessons_time])
                print(str(datetime.now()) + " " + str(all_class_lessons_time) + "\n", file=log_file)
                print(str(datetime.now()) + " " + str(new_job[i]) + "\n", file=log_file)
    
    log_file.close()

    while True:
        time.sleep(10)
        with open(proj_dir + "/loop_log.log", "a") as loop_log:
            for job in new_job:
                print(str(datetime.now()) + " " + str(job) + "\n", file=loop_log)


while True:
    time.sleep(10)
