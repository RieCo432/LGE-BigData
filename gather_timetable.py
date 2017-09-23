import requests
from lxml import html
from selenium import webdriver
import json
from extract_teachers_timetable import modify_teacher_list
from extract_teachers_timetable import original_teacher_list

driver = webdriver.PhantomJS()

class_list = ["1B latine","1B","1C1","1C2 latine","1C2","1D","1E(F)","1(E)F","1D(G)","1(D)G latine","1(D)G","1G","2A","2A","2A","2B(C) latine","2B(C)","2(B)C","2C latine","2C","2D(G)","2(D)G","2D(F)","2(D)F","2E latine","2E","2G","2G","3B(C) latine","3B(C)","3(B)C latine","3(B)C","3C latine","3C","3D latine","3D","3D(G)","3(D)G","3E(F) latine","3E(F)","3E(F) latine","3(E)F","3E(G) latine","3E(G)","3(E)G","IV.1","41","IV.2","42","43","44","45","V.1","51","52","53","54","VI 1","61","62","63","64","65","71","72","73","74","75","76","CLIJA+","1ère,2e","2e","3ème","DECHARGES","DISPO","Activités","6e","LHCE"]

teacher_list = modify_teacher_list(original_teacher_list)

lessons_list = []


for h in range(1, len(class_list)+1):
	driver.get("http://lge.lu/horaires/38/c/c"+str(h).zfill(5)+".htm")
	tree = html.fromstring(driver.page_source)

	for i in range(2, 17, 2): #cycle through times
		for j in range(2, 7): #cycle through days
		
			subject = tree.xpath("/html/body/center/table[1]/tbody/tr["+str(i)+"]/td["+str(j)+"]/table/tbody/tr/td[1]/font/b")
			teacher = tree.xpath("/html/body/center/table[1]/tbody/tr["+str(i)+"]/td["+str(j)+"]/table/tbody/tr/td[2]/font/b")
			room = tree.xpath("/html/body/center/table[1]/tbody/tr["+str(i)+"]/td["+str(j)+"]/table/tbody/tr/td[3]/font/b")
				
			for k in range(0, len(subject)):
			
				#if (subject[k] is not None) and (teacher[k] is not None) and (room[k] is not None):
					#print(subject[0].text, teacher[0].text, room[0].text)
					
					new_lesson = {
						"day": j - 2, #compensate for first column
						"time": int(i / 2) - 1, #compensate for empty rows
						"class": class_list[h - 1], #compensate for length=/=last index
					}
					
					try:
						new_lesson["subject"] = subject[k].text.strip()
					except IndexError:
						new_lesson["subject"] = "None"
						
					try:
						shorted_teacher = teacher[k].text.split()
						for teacher_name in teacher_list:
							if teacher_name[0] == shorted_teacher[0] and teacher_name[1] == shorted_teacher[1]:
								new_lesson["teacher"] = teacher_name
					except IndexError:
						new_lesson["teacher"] = "None"

					try:
						new_lesson["room"] = room[k].text.strip()
					except IndexError:
						new_lesson["room"] = "None"						
					
					lessons_list.append(new_lesson)
					
			if len(subject) == 0 and (int(i/2)-1 == 4 or int(i/2)-1 == 5):
					new_lunch_break = {
						"day": j - 2, #compensate for first column
						"time": int(i / 2) - 1, #compensate for empty rows
						"class": class_list[h - 1], #compensate for length =/= last index
						"subject": "SERVICE"
					}
					
					lessons_list.append(new_lunch_break)

with open("lessons_list.json", "w") as fout:
	json.dump(lessons_list, fout)