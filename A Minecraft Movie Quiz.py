"""This. Is a minecraft movie quiz. It is a quiz. for the minecraft movie"""

#Import libraries needed for the program
import random
import os

#Set basic Variables that may be changed later on
total_correct = 0
cont = 0
answer = 0
question_Num = 0
percente_Correct = 0

#The questions
questions = {"Who was the main character of the Minecraft Movie": 2,
             "Which Line made the cinema's all over the world go wild": 1,
             "Who was the main antagonist of the movie": 2,
             "Which object let the Protaginists of the film enter the "
             "Minecraft world": 4,
             "Henry was known in the film for being...": 3,
             "What was Steve's Dog name": 2,
             "Which one of these is not a line in the film": 3,
             "What was the piglin Generals Name": 1,
             "Which of these Youtubers were not mentioned or appeared in "
             "the film": 2,
             "What was the main sideplot of the movie": 1}

#The answers
answers = ["1. John \n2. Steve \n3. Jeff \n4. Bowser",
            "1. CHICKEN JOCKEY! \n2. FLINT AND STEEL! \n3. I. AM STEVE!"
            "\n4. THE NETHER!", 
            "1. The Ender Dragon\n2. The Piglins \n3. Alex \n4. Herobrine", 
            "1. The Crystal of Power \n2. The teleportation Stone"
            "\n3. Totem Of Undying\n4. The orb of dominance",
            "1. A normal guy\n2. A Jerk \n3. A nerd \n4. An Idiot",
            "1. Derek\n2. Dennis \n3. Dan\n4. David", 
            "1. BIG OL RED ONES\n2. AS A CHILD I YEARNED FOR THE MINES"
            "\n3. TIME TO MINECRAFT! \n4. THEY WANT ME TO FIGHT THE CHICKEN?",
            "1. Chungus \n2. Porky\n3. Piglich\n4. Jeff",
            "1. MumboJumbo \n2. Dream\n3. Technoblade\n4. DanTDM",
            "1. Villager Marrying a real woman\n2. Villager Nitwit Getting a job"
            "\n3. Piglin Baby training for war"
            "\n4. Steve Making a cow farm",]

#Repeats the question program
for i in questions:
    os.system('cls')
    print(i)
    print(answers[question_Num])
    cont = 0
    while cont != 1:
        try:
            guess = 0
            while guess > 4 or guess < 1:
                guess = int(input("Which answer is correct? "))
                if guess > 4 or guess < 1:
                    print("Not a valid Number")
        except:
            print("Please type a valid answer")
            continue
        if guess == questions[i]:
            print("Correct! Good Job!!!")
            total_correct += 1
        else:
            print(f"Incorrect, The correct answer was number {answer}")
        cont = 1
        question_Num += 1
        input("Click enter to continue")

os.system('cls')
if total_correct > 8:
    message = "Amazing work!!!"
elif total_correct > 6:
    message = "Good Job!"
elif total_correct > 4:
    message = "You did ok!"
elif total_correct > 2:
    message = "Maybe try a bit harder next time."
elif total_correct > 0:
    message = "Oof, not so great"
elif total_correct == 0:
    message = "Have you even watched the movie?"
percent_Correct = total_correct * 10

print(f"{message} you got {percent_Correct}%")

    

#Random Hatsune Miku Cause Why Not
"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣾⡿⡍⠡⠐⡀⢂⠉⡙⢋⠓⠶⣦⣠⣶⠟⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡀⢀⣠⡶⠛⢋⠉⠄⠂⠄⡐⠠⠁⠌⡐⢀⣆⠐⡠⢈⡐⣀⠛⢷⣞⠛⣿⡛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠹⣷⡟⢡⠀⡡⠂⢌⠈⡁⠂⢄⣥⡌⠡⠐⢨⣿⡀⠰⡀⠐⠠⡈⢄⡘⢦⣽⣷⡀⢹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣥⣶⠙⣷⡄⠂⠄⣁⠂⠌⣠⡿⠋⢹⡇⠤⢁⢺⡟⠿⣦⡄⠩⢐⡀⠢⠐⡠⠙⣿⣇⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠃⡄⢸⣷⣽⣿⢠⡌⢠⣼⣾⠋⠀⠀⢺⣿⠀⠂⣼⠃⠀⠀⠙⣷⡆⢠⠁⡆⠁⡆⠘⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠡⢐⡀⢂⢻⡏⢉⠠⠐⢠⣿⠏⠀⠀⠀⢠⡟⠠⣈⡿⠀⠀⠀⠀⠈⢻⣇⠰⡀⠡⢠⠁⢺⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠄⣁⠢⠐⠂⢽⣷⠂⠄⡁⣿⠇⠀⠀⠀⠀⢸⣇⣥⠟⠁⠀⠀⠀⠀⠀⠀⢻⣧⠀⡅⠂⠌⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣤⣤⡤⠤⠴⠄⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠌⡐⢀⠂⢡⢈⡾⠁⠌⡐⣰⡏⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⣀⣠⣤⣤⣴⣿⡶⠠⠁⡌⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢃⠘⠄⠠⠃⠌⢠⣾⠁⢃⠰⢀⣿⠀⠀⣀⣀⣤⣤⣶⣆⠀⠀⠀⠀⠘⠟⠉⠁⠀⠀⠘⣿⡐⠡⢀⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⡈⢐⡈⠡⣈⠐⣿⣇⢈⠂⡐⢈⣷⡶⠟⠛⠉⠉⠀⠀⠁⠀⠀⠀⢀⣀⣠⣴⣶⠀⠀⠀⢹⡆⢁⢢⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠠⡐⠠⠠⢡⠀⣾⠇⠙⢷⣦⢈⠐⣿⠀⠀⠀⠀⠀⠀⢠⣤⡴⣶⢾⡻⣝⢧⡳⣽⡆⠀⠀⢸⣧⣂⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢃⠡⡀⠡⠁⠆⢸⣟⠀⠀⠀⠙⠿⣦⡹⣇⠀⠀⠀⠀⠀⠈⠳⣟⡼⣣⢟⡼⣣⢟⣶⡇⠀⢠⣟⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠇⠰⢀⠰⢁⠡⠊⣼⠇⠀⠀⠀⠀⠀⢨⡿⣿⡶⣤⣀⠀⠀⠀⠀⠘⠳⣯⣞⡵⣫⡾⠏⠀⣰⡟⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠡⠠⢁⠂⠔⡀⠢⢁⣿⠢⠀⠀⠀⠀⣰⡟⠡⢀⠐⠠⠙⠛⢶⣄⣀⡀⠀⠀⠉⠉⠉⢀⣀⣴⣋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡼⠃⠤⠑⡀⠆⣈⠐⡀⢃⢰⡿⠀⠀⣀⣴⠾⢁⠂⠡⢂⠘⠠⠡⠈⢄⣸⠿⠻⣟⡙⢻⡟⢻⣿⢹⡏⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠀⢃⠂⠡⢐⡈⠄⠂⠌⠄⣾⢃⣀⣤⠿⠟⡁⠂⠌⡁⠂⠌⣠⣱⣮⣾⡁⠀⠀⣸⢌⡉⣿⣼⢇⢺⣧⠀⢈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣏⡿⠈⠄⣈⠡⢂⠰⠈⠌⠂⢼⡿⢋⠉⠄⠒⠠⠐⡁⠂⢌⣤⠿⢋⣿⣿⣿⣿⣷⣴⢏⠢⣽⢇⡟⣌⢊⣿⠳⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⢸⡇⡘⠠⠄⠢⢁⢂⠡⢈⡁⣾⡃⢂⠘⠠⠑⡈⠡⣀⣷⠟⢁⣴⣿⣿⣿⣿⣿⣿⢋⠦⣹⢏⡾⡑⢦⡈⣿⠀⢻⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡇⣿⠃⠄⢡⠈⡑⡀⠢⢀⠃⣰⡿⣀⣦⡬⠶⠷⠾⠛⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣣⣬⣾⣭⡾⢣⣵⣦⣖⣹⡆⠀⢻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀
⠀⠀⠀⠸⢦⡟⠠⠉⠄⠒⢠⠐⡁⠂⣼⡿⠛⠉⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠁⠀⠀⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⢠⡾⠋⠙⠲⢦⣄
⠀⠀⠀⠀⢠⡟⡀⠣⠘⣀⠃⡄⡀⣿⣟⠀⠀⠀⠀⠀⠀⠀⠸⠿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣧⡟⠀⠀⠀⢀⡼⠃⡀⠃⠄⣠⡟
⠀⠀⠀⠀⣸⣇⡄⠅⠂⠄⢺⡏⠉⠉⠉⠉⠉⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠙⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠀⠀⣘⣿⣿⣿⣿⣿⣻⣋⣀⣀⣠⡤⠟⠁⡐⠀⠡⣰⠟⠀
⠀⠀⠀⠀⠉⠙⣿⠀⡉⠐⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⠛⠛⠛⠉⢽⣿⢿⡽⠞⠁⠁⡀⠠⢀⠠⠐⠠⢀⠁⣲⠏⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡔⠠⠁⢼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⡐⠠⢈⠐⠈⠟⠋⡀⠄⡈⠐⡀⠁⠄⡐⠠⠁⡀⢢⣏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣯⠀⢡⣾⣧⠤⠦⠴⠤⠤⠤⠶⠶⠶⠶⠶⠶⠖⠶⠲⠖⠶⠺⠒⢚⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡟⠒⠗⠶⠖⠾⢤⣴⣤⣴⣤⣤⣡⣄⣈⣄⠐⢀⠂⠐⡀⢉⠳⣦⡴
⠀⠀⠀⠀⠀⠀⠀⠻⣾⣼⠏⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠈⠉⠉⠙⠳⢦⣌⡀⠐⠠⢐⡾⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⠛⠻⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣷⣎⣰⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢛⡿⠓⠀⠈⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢛⡧⠀⠀⠀"""