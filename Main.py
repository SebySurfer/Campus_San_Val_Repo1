

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

def print_Partner(partner):
    print("Partner: ", partner[0], " Social: ", partner[2], " Match Rate: ", partner[41], "% ")


# I need to find a way to identify the index of every girl when rearranging the dam All_scores
        # Solution: Every client will have the match rate at the end of their array, that way they are
        # arranged based on the value of their index.

def alg_Straight(list_m, list_f):

    PF_pts = Preg_Fund/16
    PE_pts = Preg_Esp/7

    match_score = 0.0

    value_m = 0
    value_f = 0

    #First iterate every client of every list
    for male in list_m:
        for female in list_f:
            #index from 10 to 40
            for index in range(10, 41):
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

                    #Reset values to use them again
                    value_m = 0
                    value_f = 0

                #Valores Especificos
                elif(index >= 34):
                    if(male[index] == female[index]):
                        match_score += PE_pts

            # Index 41 = added space for match rate
            female[41] = match_score

            #Adding for each female their match score towards the list.

        index_to_sort = 41
        # RESOLVE ISSUE: how is it possible to organize an array of lists, from highest to lowest, based on a specific index that is the same for every other list ?
        All_Scores = sorted(list_f, key=lambda x: x[index_to_sort], reverse=True)

        print_Res(male)
        #First printing the top 3 scores, considering their careers
        # index 7 is your career
        # index 8 and 9 are the eliminated careers

        count3 = 0
        count2 = 0

        print("Best matches:")
        for c in All_Scores:
            for index in range(len(All_Scores)):
                if(count3 < 4) and (index < len(All_Scores)):
                    if(male[7] != c[8]) or (male[7] != c[9]):
                        print_Partner(c)
                        count3+= 1

        print("Matches that you made, but you excluded them for career type")
        for c in All_Scores:
            for index in range(len(All_Scores)):
                if (count2 < 2) and (index < len(All_Scores)):
                    if (male[7] == c[8]) or (male[7] == c[9]):
                        count2 += 1

        #Resets
        female[41] = 0
        All_Scores = []















































