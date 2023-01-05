import sys
sys.path.insert(0,'./selection/')
from selection_math import analyze_math
sys.path.insert(1,'./main/')
from write_infos import informations
from selection_turkish import analyze_tr
from selection_social import analyze_social 
from selection_science import analyze_science
from selection_general import analyze_general


lessons = ['Turkish','Math','Social','Science','General']

class check():
    def check():
        print("Hi! Welcome to the Program!")
        
    
class select_lessons():
    def select():
        informations.create_table()
        for i in range(len(lessons)):
            print(f"Please enter: {i+1} for see Analyze Techniques: {lessons[i]}")
        selection = int(input("ENTER THE SELECTED NUM: "))

        if selection == 1:
            analyze_tr.select()
        if selection == 2:
            analyze_math.select()
        if selection == 3:
            analyze_social.select()
        if selection == 4:
            analyze_science.select()
        if selection == 5:
            analyze_general.select()
