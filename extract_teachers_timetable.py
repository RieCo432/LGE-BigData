import json

with open("lessons_list.json", "r") as fin:
	lessons_list = json.load(fin)
	
original_teacher_list = ["Almeida D.                    Dora","ALVES F.                    Fernando","ANTONIO L.                     Luis","ARAUJO M.                Melissa","BACKES G.       GIlles","BAUSCH C.                      Claudine","BELHAOUCI K.                      Karim","BERMES   P.                    PASCAL","BIEL M.                                  Martine","BIMMERMANN L.            LUC","BLEY C.                             Claudine","BOCK S.                     SARAH","BOGGIANI J.                            Jos.","BOHLER   R.                   RITA","BOSA   R.                      ROLAND","BOUR S.                                SVEN","BRECKLER C.                        Christine","BRUCH E.                           Eric","BURTON C.                            Christiane","CAMPAGNA   N.           NORBERT","CANCELLIERI F.                   Fabio","COURSIMAULT C.","DEMMER C.                            Claus","DEMUTH D.                                      DAPHNÉ","DENTZER A.-M.                ANNE-MARIE","DIAS J.                                   Jean-Marc","ENGEL   P.                     PATRICK","FIS       A.                Arnaud","FONSECA M.            Marina","FOSSATI N.                                 Nicole","GAGGIOLI D.                            Diane","GIUSTO A.                                             Andrea","GLODT   R.                      ROMAIN","GOERGEN   R.                      ROMAINE","HAMEN C.                 Christiane","HEIDERSCHEID M.                        Maryse","HENGEN   T.                          Tom","HERIN   V.                     VERA","HEYART     J.                               Jeff","HOFF V.                           Valérie","HOFFMANN A.                Anne","HURT L.                           Liane","HUTMACHER T.                         TOM","JANKOWSKI L.                                Lynn","JUNIUS  G.                   GILLES","KARIER G.","KIEFFER Jean-Pol","KILL S.         Sven","KLEES G.                           Géraldine","LAMBERTY N.                                 Nicole","LANTZ J.-M.                                    JEAN-MARC","Leonard C.","LOGELIN A.                Anne","LÖHLE  A.                            Alexander","LUCARELLI C.            CARLA","LUCIANI  D.                       DANIEL","LUTGEN N.                          NICO","LUTZ  T.                          THIERRY","MAININI M.                Melvyn","MAISCHAK A.                               Astrid","MAJERUS A.                          Anne","MARNACH M.                 MICHELE","MAY M.                                             MARC","MEDERNACH  F.               FERNAND","MENGOZZI J.             Jonathan","MERSCH Gianni","MULLER G.                                     Goerges","NEIENS  M.                                     Marianne","Neven J.            J0","NEY S.                                       Simone","NURDIN J.          Jessica","OCHEM  S.               Stéphanie","PACELLA P.                              Patrick","PANTALEONI C.                         CLAUDE","PARRASCH M.                               Marc","POLLARD A.","QUARATO A.               Angela","RABER  J.                         Julia","REIMEN  P.                                PIA","RITZ M. Marie-Paule","ROY  M.                              Mireille","SAVINI S.                      Sandrino","SCHAACK C.                    Christian","SCHAAF J.                                        JOCHEN","SCHANEN M.                                     Marc","SCHELLER  A.                             ANNE-MARIE","SCHMIT O.                            Oistein","SCHMITZ   C.                            CARLO","SCHMITZ Chr.                        Christian","SCHMITZ La.              Laurent","SCHMOETTEN  J.-J.                         JEAN-JACQUES","SCHOMER G.                Gilles","SCHRAM S.                  Sophie","SCHROEDER F.                         Fernand","SCHULTE Y.                            Yves","SCHUMACHER  R.                     ROLAND","SCHUMMER   N.                      NADINE","SIMOES  S.                   Stéphanie","SNEL L.                             Lynne","SONNETTI S.                     Sarah","SONNTAG I.                                Iris","STASIAK  P.                       Paul","TALBI  S.                           Sihem","THIEL   M.                                         MARC","THILL   S.                              SONJA","THIMMESCH S.                     Sylvie","TIRPANDZIAN L.                          Laure","TRENTIN R.                 Raoul","VIEN  G.                                              Gaëlle","WAGENER G.               GERARD","Wagner A.    Alex","WEILER J.                 Jean-Joël","WELTER C.                   Christian","WENANDY C.                   Claire","WEYER   H.                                   Henri","WEYER L.                  Laure","WILLEMS J.                         Jessica"]

def modify_teacher_list(teachers):
	new_teacher_list = []
	for teacher in teachers:
		new_teacher = teacher.split()
		for i in range(1, len(new_teacher)):
			new_teacher[i].lower()
		new_teacher_list.append(new_teacher)
		
	return new_teacher_list
	



teachers = modify_teacher_list(original_teacher_list)

for teacher in teachers:

	try:
		current_teacher = teacher[0] + " " + teacher[2]
	except IndexError:
		current_teacher = teacher[0] + " " + teacher[1]

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
					#print("KeyError, no room key")
					pass
				
				new_teacher_timetable.append(new_lesson)
				
		except KeyError:
			#print("KeyError, no teacher Key")
			pass
		
	new_teacher_timetable.sort(key = lambda d: d["day"])

	with open("teachers/timetable_"+current_teacher+".json", "w") as fout:
		json.dump(new_teacher_timetable, fout)