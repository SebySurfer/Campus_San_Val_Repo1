

total_clients = int(input("What are the total number of clients?: "))


#Creating Object

class Client:
    def __init__(self, name, social, number, sex, at_sex, rel, rel_s, prof, prof_s, no_prof1, no_prof2, q8, q8_s, q9,
                 q9_s, q10, q10_s, q11, q11_s, q12, q12_s, q13, q13_s, q14, q14_s, q15, q15_s, q16, q16_s, q17, q17_s, q18, q18_s,
                 q19, q19_s, q20, q21, q22, q23, q24, q25, q26):
        #Note: You dont need to create any getters in python, you get them directly by the name of the object

        #Preguntas Informativas
        self.name = name
        self.social = social
        self.number = number
        self.sex = sex
        self.at_sex = at_sex

        #Preguntas Fundamentales
        self.rel = rel  # 6
        self.rel_s = rel_s
        self.prof = prof
        self.prof_s = prof_s

        self.no_prof1 = no_prof1 #10
        self.no_prof2 = no_prof2 #11

        self.q8 = q8
        self.q8_s = q8_s
        self.q9 = q9
        self.q9_s = q9_s
        self.q10 = q10
        self.q10_s = q10_s
        self.q11 = q11
        self.q11_s = q11_s
        self.q12 = q12
        self.q12_s = q12_s
        self.q13 = q13
        self.q13_s = q13_s
        self.q14 = q14
        self.q14_s = q14_s
        self.q15 = q15
        self.q15_s = q15_s
        self.q16 = q16
        self.q16_s = q16_s
        self.q17 = q17
        self.q17_s = q17_s
        self.q18 = q18
        self.q18_s = q18_s
        self.q19 = q19
        self.q19_s = q19_s

        #Preguntas Especificas
        self.q20 = q20
        self.q21 = q21
        self.q22 = q22
        self.q23 = q23
        self.q24 = q24
        self.q25 = q25
        self.q26 = q26




#Main List

main_List = []

#For-Loop to create all objects and add them to the main list

#All Lists
gay_list = []

lesb_list = []

straight_ser_list = [[],[]]

straight_cas_list = [[],[]]

#For-Loop to add all the objects to every list


Preg_Fund = int(input("Give me the percentage the Preguntas_Fundamentales are going to take in the algorithm: "))
Preg_Esp = 100 - Preg_Fund

#


def alg_Straight(array):

    PF_pts = Preg_Fund/16
    PE_pts = Preg_Esp/7

    All_Scores = []


















