#This allows me to import my Players database to my python file
import csv
from pymongo import MongoClient
#This allows me to import my QA sheet csv file into python
Titles = ['WWE Questions', 'WWE Answers']
Info = [['What is the Rocks Real Name ?','Dwayne The Rock Johnson'],
['Who is the founder of WWE ?','Vince McMahon'],
[' What does AEW stand for ?','All Elite Wrestling'],
['Who is the longest World Champion in History ?','Bruno Sanmartino'],
[' What does WWE stand for ?','World Wrestling Entertainment'],
['Bonus: How Many World titles has Randy Orton won ?','14'],
['Who is the Greatest Wrestler of All Time', 'John Cena']]
# This allows me to write to my csv file in python
with open ("QA sheet.csv", "w", newline='') as QA:
               writer = csv.writer(QA)                      
               writer.writerow(Titles)
               writer.writerows(Info)
# This defines my users input for my Game   
def  User_name(): 
        User_name = str(input('Player Name:'))
 # This saves the players information to my database               
def Save_players(db_Players, User_name, points):
                        dict_player = { 'name': User_name,
                                'total score': points }
                        db_Players.play.insert_one(dict_player)      
#This is the main function in which my python file execute the Quiz Bowl in python                         
def main():
        client = MongoClient()
        
        db_Players = client.Players

        print("Welcome to The WWE Quiz Bowl Game")
        print('>>>>')
        User_name = str(input('Player Name:'))
        while True:
                try:
                        if len(User_name) < 4:
                                raise ValueError
                except ValueError: 
                        print('NO Nicknames!')
                else: 
                        print('Continue with Quiz Bowl')
                break
        print('>>>>')
        WWE_Answers = input('Begin Game:\r')
        print('>>>>>')
        points = 0
        WWE_Answers = points
        WWE_Answers =input('Question1: What is the Rocks real name?')
        if WWE_Answers==("Dwayne The Rock Johnson"):
                                points=points+10
        else:
                  print("Nice Try")
        WWE_Answers=input('Question2: Who is the founder of WWE?')
        if   WWE_Answers==("Vince McMahon"):
                                points=points+10
        else:
                print("Nice Try")
        WWE_Answers=input('Question3: What does AEW stand for ?')
        if      WWE_Answers==("All Elite Wrestling"):
                                points=points+10
        else:
                         print("Nice Try")
        WWE_Answers=input('Question4: Who is the longest World Champion is History?')
        if WWE_Answers==("Bruno Sanmartino"):
                                points=points+15
        else:
                print("Nice Try")

        WWE_Answers=input('Question5: What does WWE stand for?')
        if WWE_Answers==("World Wrestling Entertainment"):
                                points=points+10
        else:
         print("Nice Try")
               
        WWE_Answers=input('Bonus: How Many World titles has Randy Orton won ?')
        if WWE_Answers== ('14'):
                         points=points+50
                         print('Hooray you got the Bonus')
        else:
                        print('Nice Try')         

        User_Results = (points)
                
        if (User_Results == 105):                                           
                        print("Great Job Your a Real Wrestling Fan ")
        else: 
                 print('Thank for Playing ')
        print('Your overall score is..', User_Results)
        Save_players(db_Players,User_name,points)
if __name__ == '__main__':
        main()

