# coding=latin1
import json
from shared_stuff import ClassClass

with open("lessons_list.json", "r") as fin:
    lessons_list = json.load(fin)

for class_name in ClassClass.class_list:

    new_class_timetable = []

    for lesson in lessons_list:
        if lesson["class"] == class_name:
            new_lesson = {
                "day": lesson["day"],
                "time": lesson["time"],
                "subject": lesson["subject"],
            }
            try:
                new_lesson["teacher"] = lesson["teacher"][0]
            except IndexError:
                new_lesson["teacher"] = "None"
            except KeyError:
                # print("KeyError")
                pass

            try:
                new_lesson["room"] = lesson["room"]
            except KeyError:
                # print("KeyError")
                pass

            new_class_timetable.append(new_lesson)

    new_class_timetable.sort(key=lambda d: d["day"])

    class_timetable_filename = class_name.replace("(", "-").replace(")", "-").replace(" ", "_")
    with open("classes/timetable_" + class_timetable_filename + ".json", "w") as fout:
        json.dump(new_class_timetable, fout)
