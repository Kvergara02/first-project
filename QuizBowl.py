from pymongo import MongoClient

client = MongoClient()

db_week4 = client.week4

stat = db_week4.stat

import csv
Titles=['WWE Questions', 'WWE Answers']
Info = [['What is the Rocks Real Name ?,Dwayne The Rock Johnson'],
['Who is the founder of WWE ?,Vince McMahon'],
[' What does AEW stand for ?,All Elite  Wrestling'],
['Who is the longest World Champion in History ?,Bruno SanMartino'],
[' What does WWE stand for ?,World Wrestling Entertainment'],
['Bonus: How Many World titles has Randy Orton won ?','14']]

with open ("QA sheet.csv", "w") as QA:
                write = csv.writer(QA , delimiter = ',')                      
                write.writerow(Titles)
                write.writerows(Info)
print("Welcome to The WWE Quiz Bowl Game")

def  User_name():
                
        User_name =input("Player Name:\r")                 
print(">>>")
def  WWE_Answers():
                WWE_Answers =input("Begin Game\r")
                print(">>>")
                points = 0
                WWE_Answers = points
                WWE_Answers =input('Question1: What is the Rocks real name?')
                if WWE_Answers==("Dwayne the Rock Johnson"):
                        points=+1
                else:
                 print("Nice Try")
                WWE_Answers=input('Question2: Who is the founder of WWE?')
                if   WWE_Answers==("Vince McMahon"):
                        points=+1
                else:
                        print("Nice Try")
                WWE_Answers=input('Question3: What does AEW stand for ?')
                if      WWE_Answers==("All Elite Wrestling"):
                        points=+1
                else:
                         print("Nice Try")
                WWE_Answers=input('Question4: Who is the longest World Champion is History?')
                if WWE_Answers==("Bruno SanMartino"):
                        points=+1
                else:
                        print("Nice Try")

                WWE_Answers=input('Question5: What does WWE stand for?')
                if WWE_Answers==("World Wrestling Entertainment"):
                        points=+1
                else:
                 print("Nice Try")
                WWE_Answers=input('Bonus: How Many World titles has Randy Orton won ?')
                if WWE_Answers== 14:
                         points=+1
                         print('Hooray you got the Bonus')
                else:
                        print('Nice Try')
                 
                        User_Results = (points)
                
                        if (User_Results == 6):
                                        print("Great Job Your a Real Wrestling Fan ")
                        if (User_Results == 2 or 1 ):
                                print("Try Again Next Time!")
                        else: 
                                print('Thank for Playing ')


User_name()
WWE_Answers()

