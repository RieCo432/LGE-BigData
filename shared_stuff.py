# coding=utf-8
class ClassTeacher:
    def __init__(self):
        pass

    original_teacher_list = ["OPTIONS","_PROJET","ALMEIDA","ANTONIO","ARAUJO","ALVES","BACKES","BAUSCH","BELHAOUCI",
	"BERMES","BIEL","BIMMERMANN","BLEY","BOCK","BOHLER","BOSA","BOUR","BRECKLER","BRUCH","BURTON","CAMPAGNA",
	"CANCELLIERI","COURSIMAULT","DEMMER","DEMUTH","DENTZER","DIAS","ENGEL","FIS","FONSECA","FOSSATI","GAGGIOLI",
	"GIUSTO","GLODT","GOERGEN","HAMEN","HEIDERSCHEID","HENGEN","HERIN","HEYART","HOFF","HOFFMANN","HURT","HUTMACHER",
	"JANKOWSKI","JUNIUS","KARIER","KIEFFER","KILL","KLEES","LAMBERTY","LANTZ","LEONARD","LOGELIN","LÖHLE","LUCARELLI",
	"LUCIANI","LUTGEN","LUTZ","MAININI","MAISCHAK","MAJERUS","MARNACH","MAY","MEDERNACH","MENGOZZI","MERSCH","MULLER",
	"NEIENS","NEVEN","NEY","NURDIN","OCHEM","PACELLA","PANTALEONI","PARRASCH","POLLARD","QUARATO","RABER","REIMEN","RITZ",
	"ROY","SAVINI","SCHAACK","SCHAAF","SCHANEN","SCHELLER","SCHMIT","SCHMITZ","SCHMITZ","SCHMITZ","SCHMOETTEN","SCHOMER",
	"SCHRAM","SCHROEDER","SCHULTE","SCHUMACHER","SCHUMMER","SIMOES","SNEL","SONNETTI","SONNTAG","STASIAK","TALBI","THIEL",
	"THILL","THIMMESCH","TIRPANDZIAN","TRENTIN","VIEN","WAGENER","WAGNER","WEILER","WELTER","WENANDY","WEYER","WEYER",
	"WILLEMS","Z","Z","Z","Z","SALIO","WINANDY","MULLER","DONDELINGER"]

    @staticmethod
    def modify_teacher_list(teachers):
        new_teacher_list = []
        for teacher in teachers:
            new_teacher = teacher.split()
            for i in range(1, len(new_teacher)):
                new_teacher[i].lower()
            new_teacher_list.append(new_teacher)

        return new_teacher_list

class ClassClass:
    def __init__(self):
        pass

    class_list = ['CLIJA+', '1A', '1B(C)', '1B(C)', '1(B)C', '1C latine', '1C', '1D', '1E', '1(F)G', '1F(G)', '1G', '2B(C)', '2(B)C', 
	'2C latine', '2C', '2D', '2D(G)', '2(D)G', '2E', '2F(G)', '2(F)G', '3A(F) latine', '3A(F)', '3(A)F latine', '3(A)F', '3B(C) latine', 
	'3B(C)', '3(B)C latine', '3(B)C', '3C latine', '3C', '3D latine', '3D', '3E latine', '3E', '3G', 'IV.1', '41', '42', '43', '44', 'V.1', 
	'51', '52', '53', '54', '55', 'VI 1', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '76', '77', '5IB', '6IB', '6e', 'LHCE', 
	'Activités', 'DECHARGES', 'DISPO', '1ère,2e', '3ème', '2e']
