

total_clients = int(input("What are the total number of clients?: "))


#For Loop for creating an array for every client and assigning its values




#Main List of all array clients

main_List = []

#For-Loop to create all objects and add them to the main list

#All Lists
gay_list = []

lesb_list = []

straight_ser_list_m = []
straight_ser_list_f = []

straight_cas_list_m = []
straight_cas_list_f = []


#For-Loop to add all the objects to every list


Preg_Fund = int(input("Give me the percentage the Preguntas_Fundamentales are going to take in the algorithm: "))
Preg_Esp = 100 - Preg_Fund


def print_Res(client):
    print("")
    print("Client ", client[0], ", ", client[3],"4",client[4], ". WhatsApp: ", client[2])
    print("Results: ")



def alg_Straight(list_m, list_f):

    PF_pts = Preg_Fund/16
    PE_pts = Preg_Esp/7

    All_Scores = []

    match_score = 0.0

    value_m = 0
    value_f = 0

    top_5 = [0] * 5
    top_2 = [0] * 2



    #First iterate every client of every list
    for male in list_m:
        for female in list_f:
            for index in range(10, 40):

                #Valores Fundamentales
                if(index < 34):
                    value_m = male[index] * male[index+1]
                    value_f = female[index] * female[index+1]
                    #Checks if theres a match or not on that question/filter and adds points if there is
                    if(value_m < 0) and (value_f < 0):
                        match_score += PF_pts
                    elif(value_m == 0) and (value_f == 0):
                        match_score += PF_pts
                    elif(value_m > 0) and (value_f > 0):
                        match_score += PF_pts
                    index+= 1 #To skip the follow-up question

                #Valores Especificos
                elif(index >= 34):
                    if(male[index] == female[index]):
                        match_score += PF_pts

        All_Scores.append(match_score)

    #Using method from library to sort All_Scores from highest to lowest
    All_Scores.sort(reverse=True)

    #I need to find a way to identify the index of every girl when rearranging the dam All_scores
    #Solution: Every client will have the match rate at the end of their array, that way they are
    # arranged based on the value of their index.

    print_Res(male)















        #From index 9 (question 10) and onwards, its preg fund with values
































