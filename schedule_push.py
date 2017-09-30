import time
import json
from datetime import datetime, timedelta
from datetime import time
from apscheduler.schedulers.background import BackgroundScheduler
from shared_stuff import ClassClass
import requests
from pytz import timezone

scheduler = BackgroundScheduler()


def push_scheduled_lesson(destination_class, lesson):
    fcm = {"address": "https://fcm.googleapis.com/fcm/send", "key": "AIzaSyD0KrIb6z4KSB6nghPtA-bG-rJI4MOMhwo"}
    stdParas = {"targetPackage": "com.colinries.lge"}
    intraPushParas = {"ttl": 600, "collapseKey": "intrapush_lesson", "tag": "intrapush_lesson",
                      "to": "/topics/intrapush" + destination_class}
    postRequestHeaders = {"Content-Type": "application/json", "Authorization": "key=" + fcm["key"]}

    classNotificationPayload = {lesson}
    classNotificationDataRAW = {"notification": classNotificationPayload,
                                "restricted_package_name": stdParas["targetPackage"],
                                "to": "/topics/intraPush" + class_name,
                                "time_to_live": 600,
                                "collapseKey": "intrapush_lesson",
                                "tag": "intrapush_lesson"}
    classNotificationData = json.dumps(classNotificationDataRAW)
    classNotificationResult = requests.post(fcm["address"], data=classNotificationData, headers=postRequestHeaders)
    print(classNotificationResult.text)
    print(classNotificationResult)


now = datetime(2017, 9, 30, datetime.now().hour, datetime.now().minute)

# temporarily disabled for debugging purposes
# notification_times = [datetime(now.year, now.month, now.day, 7, 50),
#                      datetime(now.year, now.month, now.day, 8, 45),
#                      datetime(now.year, now.month, now.day, 9, 50),
#                      datetime(now.year, now.month, now.day, 10, 45),
#                      datetime(now.year, now.month, now.day, 11, 40),
#                      datetime(now.year, now.month, now.day, 12, 30),
#                      datetime(now.year, now.month, now.day, 13, 25),
#                      datetime(now.year, now.month, now.day, 14, 20),
#                      datetime(now.year, now.month, now.day, 15, 15)]

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

# notification_week_days = ["monday",
#              "tuesday",
#              "wednesday",
#              "thursday",
#              "friday"]

# for class_name in ClassClass.class_list
class_name = "1B"
with open("classes/timetable_" + class_name + ".json", "r") as fin:
    all_class_lessons = json.load(fin)

    # temporarily disabled for debbuging purposes
    # all_class_lessons_today = filter(lambda today_lesson: today_lesson["day"] == now.weekday(), all_class_lessons)

    all_class_lessons_today = filter(lambda today_lesson: today_lesson["day"] == 0, all_class_lessons)

    for i in range(0, 9):
        all_class_lessons_time = filter(lambda lesson: lesson["time"] == i, all_class_lessons_today)
        if len(all_class_lessons_time) != 0:
            new_job = scheduler.add_job(push_scheduled_lesson, 'date', run_date=notification_times[i], args=[class_name,
                                        all_class_lessons_time])
            print(all_class_lessons_time)
            print(new_job)



        # for lesson in all_class_lessons:
        #     if lesson["day"] == now.weekday():
        #         push_function_paras = {
        #             "subject": lesson["subject"],
        #             "teacher" : lesson["teacher"],
        #             "room" :
        #         }
        #         scheduler.add_job(push_intranet_notification(), 'date', run_date=notification_times[lesson["time"]],
        #                       args=[])
