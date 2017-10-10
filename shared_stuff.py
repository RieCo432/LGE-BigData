# coding=utf-8
class ClassTeacher:
    def __init__(self):
        pass

    original_teacher_list = ["Almeida D.                    Dora", "ALVES F.                    Fernando",
                             "ANTONIO L.                     Luis", "ARAUJO M.                Melissa",
                             "BACKES G.       GIlles", "BAUSCH C.                      Claudine",
                             "BELHAOUCI K.                      Karim", "BERMES   P.                    PASCAL",
                             "BIEL M.                                  Martine", "BIMMERMANN L.            LUC",
                             "BLEY C.                             Claudine", "BOCK S.                     SARAH",
                             "BOGGIANI J.                            Jos.", "BOHLER   R.                   RITA",
                             "BOSA   R.                      ROLAND", "BOUR S.                                SVEN",
                             "BRECKLER C.                        Christine", "BRUCH E.                           Eric",
                             "BURTON C.                            Christiane", "CAMPAGNA   N.           NORBERT",
                             "CANCELLIERI F.                   Fabio", "COURSIMAULT C.",
                             "DEMMER C.                            Claus",
                             "DEMUTH D.                                      DAPHNÉ",
                             "DENTZER A.-M.                ANNE-MARIE",
                             "DIAS J.                                   Jean-Marc",
                             "ENGEL   P.                     PATRICK", "FIS       A.                Arnaud",
                             "FONSECA M.            Marina", "FOSSATI N.                                 Nicole",
                             "GAGGIOLI D.                            Diane",
                             "GIUSTO A.                                             Andrea",
                             "GLODT   R.                      ROMAIN", "GOERGEN   R.                      ROMAINE",
                             "HAMEN C.                 Christiane", "HEIDERSCHEID M.                        Maryse",
                             "HENGEN   T.                          Tom", "HERIN   V.                     VERA",
                             "HEYART     J.                               Jeff",
                             "HOFF V.                           Valérie", "HOFFMANN A.                Anne",
                             "HURT L.                           Liane", "HUTMACHER T.                         TOM",
                             "JANKOWSKI L.                                Lynn", "JUNIUS  G.                   GILLES",
                             "KARIER G.", "KIEFFER Jean-Pol", "KILL S.         Sven",
                             "KLEES G.                           Géraldine",
                             "LAMBERTY N.                                 Nicole",
                             "LANTZ J.-M.                                    JEAN-MARC", "Leonard C.",
                             "LOGELIN A.                Anne", "LÖHLE  A.                            Alexander",
                             "LUCARELLI C.            CARLA", "LUCIANI  D.                       DANIEL",
                             "LUTGEN N.                          NICO", "LUTZ  T.                          THIERRY",
                             "MAININI M.                Melvyn", "MAISCHAK A.                               Astrid",
                             "MAJERUS A.                          Anne", "MARNACH M.                 MICHELE",
                             "MAY M.                                             MARC",
                             "MEDERNACH  F.               FERNAND", "MENGOZZI J.             Jonathan", "MERSCH Gianni",
                             "MULLER G.                                     Goerges",
                             "NEIENS  M.                                     Marianne", "Neven J.            J0",
                             "NEY S.                                       Simone", "NURDIN J.          Jessica",
                             "OCHEM  S.               Stéphanie", "PACELLA P.                              Patrick",
                             "PANTALEONI C.                         CLAUDE",
                             "PARRASCH M.                               Marc", "POLLARD A.",
                             "QUARATO A.               Angela", "RABER  J.                         Julia",
                             "REIMEN  P.                                PIA", "RITZ M. Marie-Paule",
                             "ROY  M.                              Mireille", "SAVINI S.                      Sandrino",
                             "SCHAACK C.                    Christian",
                             "SCHAAF J.                                        JOCHEN",
                             "SCHANEN M.                                     Marc",
                             "SCHELLER  A.                             ANNE-MARIE",
                             "SCHMIT O.                            Oistein",
                             "SCHMITZ   C.                            CARLO",
                             "SCHMITZ Chr.                        Christian", "SCHMITZ La.              Laurent",
                             "SCHMOETTEN  J.-J.                         JEAN-JACQUES",
                             "SCHOMER G.                Gilles", "SCHRAM S.                  Sophie",
                             "SCHROEDER F.                         Fernand",
                             "SCHULTE Y.                            Yves", "SCHUMACHER  R.                     ROLAND",
                             "SCHUMMER   N.                      NADINE", "SIMOES  S.                   Stéphanie",
                             "SNEL L.                             Lynne", "SONNETTI S.                     Sarah",
                             "SONNTAG I.                                Iris", "STASIAK  P.                       Paul",
                             "TALBI  S.                           Sihem",
                             "THIEL   M.                                         MARC",
                             "THILL   S.                              SONJA", "THIMMESCH S.                     Sylvie",
                             "TIRPANDZIAN L.                          Laure", "TRENTIN R.                 Raoul",
                             "VIEN  G.                                              Gaëlle",
                             "WAGENER G.               GERARD", "Wagner A.    Alex",
                             "WEILER J.                 Jean-Joël", "WELTER C.                   Christian",
                             "WENANDY C.                   Claire",
                             "WEYER   H.                                   Henri", "WEYER L.                  Laure",
                             "WILLEMS J.                         Jessica"]

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

    class_list = ["1B latine", "1B", "1C1", "1C2 latine", "1C2", "1D", "1E(F)", "1(E)F", "1D(G)", "1(D)G latine",
                  "1(D)G",
                  "1G", "2A", "2B(C) latine", "2B(C)", "2(B)C", "2C latine", "2C", "2D(G)", "2(D)G",
                  "2D(F)",
                  "2(D)F", "2E latine", "2E", "2G", "3B(C) latine", "3B(C)", "3(B)C latine", "3(B)C", "3C latine",
                  "3C", "3D latine", "3D", "3D(G)", "3(D)G", "3E(F) latine", "3E(F)", "3(E)F latine", "3(E)F",
                  "3E(G) latine", "3E(G)", "3(E)G", "IV.1", "41", "IV.2", "42", "43", "44", "45", "V.1", "51", "52",
                  "53",
                  "54", "VI 1", "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", "76", "CLIJA+", "1ère,2e",
                  "2e",
                  "3ème", "DECHARGES", "DISPO", "Activités", "6e", "LHCE"]
