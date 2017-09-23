import json

with open("lessons_list.json", "r") as fin:
	lessons_list = json.load(fin)
	
class_list = ["1B latine","1B","1C1","1C2 latine","1C2","1D","1E(F)","1(E)F","1D(G)","1(D)G latine","1(D)G","1G","2A","2A","2A","2B(C) latine","2B(C)","2(B)C","2C latine","2C","2D(G)","2(D)G","2D(F)","2(D)F","2E latine","2E","2G","2G","3B(C) latine","3B(C)","3(B)C latine","3(B)C","3C latine","3C","3D latine","3D","3D(G)","3(D)G","3E(F) latine","3E(F)","3E(F) latine","3(E)F","3E(G) latine","3E(G)","3(E)G","IV.1","41","IV.2","42","43","44","45","V.1","51","52","53","54","VI 1","61","62","63","64","65","71","72","73","74","75","76","CLIJA+","1ère,2e","2e","3ème","DECHARGES","DISPO","Activités","6e","LHCE"]	

for class_name in class_list:

	new_class_timetable = []	
	
	for lesson in lessons_list:
		if lesson["class"] == class_name:
			new_lesson = {
				"day": lesson["day"],
				"time": lesson["time"],
				"subject": lesson["subject"],
			}
			try:
				new_lesson["teacher"] = lesson["teacher"][0] + " " + lesson["teacher"][2]
			except IndexError:
				new_lesson["teacher"] = lesson["teacher"][0] + " " + lesson["teacher"][1]
			except KeyError:
				#print("KeyError")
				pass
			
			try:
				new_lesson["room"] = lesson["room"]
			except KeyError:
				#print("KeyError")
				pass
				
			new_class_timetable.append(new_lesson)
		
	new_class_timetable.sort(key = lambda d: d["day"])

	with open("classes/timetable_"+class_name+".json", "w") as fout:
		json.dump(new_class_timetable, fout)