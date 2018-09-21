# coding=utf-8
import json
from shared_stuff import ClassTeacher

with open("lessons_list.json", "r") as fin:
    lessons_list = json.load(fin)


teachers = ClassTeacher.modify_teacher_list(ClassTeacher.original_teacher_list)

for teacher in teachers:

    try:
        current_teacher = teacher[0] #+ " " + teacher[2]
    except IndexError:
        current_teacher = "None" #teacher[0] + " " + teacher[1]

    new_teacher_timetable = []

    for lesson in lessons_list:

        try:

            if lesson["teacher"] == teacher:
                new_lesson = {
                    "day": lesson["day"],
                    "time": lesson["time"],
                    "subject": lesson["subject"],
                    "class": lesson["class"],
                }

                try:
                    new_lesson["room"] = lesson["room"]
                except KeyError:
                    # print("KeyError, no room key")
                    pass

                new_teacher_timetable.append(new_lesson)

        except KeyError:
            # print("KeyError, no teacher Key")
            pass

    new_teacher_timetable.sort(key=lambda d: d["day"])

    with open("teachers/timetable_" + current_teacher + ".json", "w") as fout:
        json.dump(new_teacher_timetable, fout)
