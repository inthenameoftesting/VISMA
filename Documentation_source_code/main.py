'''
Author: Emilija Pupštaitė
2023-10-22
Summary: The program let's the user randomly generate band names and band member names.
The program also let's the user choose a band name from the list of adjectives and nouns, 
as well as, add their own custom name.
Program made for VISMA "Technical QA Intership Task"
'''
#PySimpleGUI and random packages needed for this program

import PySimpleGUI as sg #PySimpleGUI needs to be installed using the command: pip install pysimplegui
import random 
 

def rGen(file: str): #function takes files content, splits them and then outputs a random word.
    try: #tries the below code unless it hits error. 
        with open(file, "r") as file_content: #it opens the file in read mode and stores in the variable file_content
            words = file_content.read().split(',') #it reads the content, splits it based on where commas are and stores it in the variable "words"
            words = words[:-1] #removes last object from the list "words"
        if len(words) > -1: #it checks if the file contains elements
            output = random.choice(words) #selects a random element from "words" and stores it in the variable "output"
            return output #returns the value stored in "output"
        else: #if there is no elements in the file it prints the message below
            print("The file is empty!")
    except FileNotFoundError: #if there is no file by the specified name, it return the error below
        print("File not found:", file)

def updated_file(word: str,file): #
    try: #tries the below code unless it hits error. 
        with open(file, "r") as file_content: #it opens the file in read mode and stores in the variable file_content
            content = file_content.read() #it reads the content, splits it based on where commas are and stores it in the variable "words"
            list = content.split(",")
            l_words = len(list) -1 #checks the length of the list and removes one (so the counter is not included)
            list = list[:-1] #Remove the last element from the list
            '''
            Checks that the length of the input is between 0 and 16
            Checks that the input does not include a comma
            Checks that the input is not in the file already
            '''
            if 0 < len(word) <= 16 and "," not in word and word not in file_content.read(): 
                with open(file, "w") as w_file: #it opens the file in write mode and stores in the variable w_file
                    list.append(word) #adds the content of (word) to the end of the list
                    list.append(str(l_words)) #adds object counter to the end of the list
                    w_file.write(",".join(list)) #writes the list to the txt file
            else: #if the input does not pass the if statement e.g. more than 16 characters, includes a comma 
                    token = 1 
                    return token #returns the value to indicate that the input was invalid
    except FileNotFoundError: #if there is no file by the specified name, it return the error below
        print("File not found:", file)

sg.theme('Purple') #sets background color as purple

layout = [ #a code that governs the main windows layout and the keys that triggers events when buttons are pushed
    [sg.Text(text="Great Band Generator", font = ('Arial Bold', 20), size = 50,expand_x = True,
    justification = 'centre')],

    [sg.Text("Band Name:", pad=((160, 0), 0)), sg.Input(key= "BANDNAME", disabled = True), 
    sg.Button("Roll Again", button_color=('black','pink')),
      sg.Button("Choose", button_color=('black','pink'))],
    [sg.Text("Vocalist", pad=((100, 0), 0)), sg.Input(rGen("names.txt"), key="VOCAL", pad=((5, 0), 0), size = (25), disabled = True), sg.Button("Vocal Roll",button_color=('black', 'pink'), pad=((10, 0), 0)),
     sg.Text("Bass Guitar", pad=((80, 0), 0)), sg.Input(rGen("names.txt"), key="BASS", pad=((19, 0), 0), size = (25), disabled = True), sg.Button("Bass Roll",button_color=('black', 'pink'), pad=((10, 0), 0))],
    [sg.Text("Drummer", pad=((90, 0), 0)), sg.Input(rGen("names.txt"), key="DRUM", pad=((9, 0), 0), size = (25), disabled = True), sg.Button("Drum Roll",button_color=('black', 'pink'), pad=((10, 0), 0)),
     sg.Text("Electric Guitar", pad=((80, 0), 0)), sg.Input(rGen("names.txt"), key="ELEC", pad=((5, 0), 0), size = (25), disabled = True), sg.Button("Elec Roll",button_color=('black', 'pink'), pad=((10, 0), 0))],

    [sg.Exit(button_color=('black','pink')), sg.Button("Challanges", button_color=("black", "pink"))],
]


window = sg.Window("Great Bands", layout)#draw window
while True:#monitors waiting for a button input and executes relevant function
    event, values = window.read()
    print (event, values) # debugging purpose
    
    
    if event in (sg.WINDOW_CLOSED, "Exit"): #closes the window when Exit or [x] is pressed on
        break
    elif event == "Roll Again": #pulls a random value from adjective and noun and displays them in the BANDNAME input field. Code is mirrored same for the 4 below.
        bandnames = rGen("adjective.txt") + " " + rGen("nouns.txt")
        window["BANDNAME"].update(bandnames)
    elif event == "Vocal Roll":
        vocal = rGen("names.txt") 
        window["VOCAL"].update(vocal)
    elif event == "Bass Roll":
        bass = rGen("names.txt") 
        window["BASS"].update(bass)
    elif event == "Drum Roll":
        drum = rGen("names.txt")
        window["DRUM"].update(drum)
    elif event == "Elec Roll":
        elec = rGen("names.txt")
        window["ELEC"].update(elec)
    
    
    elif event == "Choose": 
        '''
        when the Choose button is pressed a new window is displayed to form your own band name. 
        Below is the code that tells the program to read from certain databases

        '''
        with open("adjective.txt", "r") as file_content:
            adjectives = file_content.read().split(",")
            adjectives = adjectives[:-1]
        with open("nouns.txt", "r") as file_content:
            nouns = file_content.read().split(",")
            nouns = nouns[:-1]
        t_layout = [ #the layout for the second window
            [sg.Text('Adjective:', pad=((3, 0), 0)), sg.OptionMenu(adjectives, key="adjective", size=(20, 1)),
            sg.Text('Noun:', pad=((3, 0), 0)), sg.OptionMenu(nouns, key="nouns", size=(20, 1))],
            [sg.Text("Your name:"),sg.Text("Adjective"), sg.Input(key="c_adjective", pad=((5, 0), 0), size = (16)),
             sg.Text("+"), sg.Input(key="c_nouns", pad=((5, 0), 0), size = (16)), sg.Text("Noun")],
            [sg.Button("Confirm", button_color=("black", "pink")), sg.Text("Words must be under 16 characters with no commas", text_color=("black"))]
        ]


        second_window = sg.Window("Form your own band name", t_layout) #draws a second window 
        
        
        while True: #monitors waiting for a button input and executes relevant function
            event, values = second_window.read()
            if event in (sg.WINDOW_CLOSED, 'Cancel'): #closes the window when Cancel or [x] is pressed on
                break
            elif event == "Confirm" and (values["adjective"] and values["nouns"]): #makes sure that there are values in both adjective and nouns, and that the confirm button has been pushed
                t_adjective = values["adjective"]
                t_noun = values["nouns"]
                t_bandnames = t_adjective + " " + t_noun
                window["BANDNAME"].update(t_bandnames)
                break
            elif event == "Confirm" and (values["c_adjective"] and values["c_nouns"]):
                adjective_token = updated_file(values["c_adjective"], "adjective.txt")
                noun_token = updated_file(values["c_nouns"], "nouns.txt")
                if adjective_token == None and noun_token == None: #both are correct
                    t_adjective = values["c_adjective"]
                    t_noun = values["c_nouns"]
                    t_bandnames = t_adjective + " " + t_noun
                    window["BANDNAME"].update(t_bandnames)
                    break
                elif noun_token == None and adjective_token > 0: #noun is correct, adjective is incorrect
                    sg.popup("Adjective is invalid \nWords must be under 16 characters with no commas")
                elif adjective_token == None and noun_token >0: #adjective is correct, noun is not correct
                    sg.popup("Noun is invalid \nWords must be under 16 characters with no commas")
                else:
                    sg.popup("Input is invalid \nWords must be under 16 characters with no commas")
            elif event == "Confirm":
                break  
        second_window.close() #closes the second window after 


    elif event == "Challanges": #sets a layout for challanges window
        challange_layout = [
            [sg.Text(text="Up for a challange?", font = ('Arial Bold', 20), size = (50,1), expand_x = True,
            justification = 'centre')],
            [sg.Button("Click here!", button_color=("black", "pink"), font = ('Arial Bold', 20)),
             sg.StatusBar("", size=(50,2), key='-STATUS-', font=("Arial Bold", 15))],
            [sg.Button("OK", button_color=("black", "pink"))]
        ]


        challange_window = sg.Window("Spicy Challanges", challange_layout) #draws a challange(third) window
        while True: #monitors waiting for a button input and executes relevant function
            event, values = challange_window.read()
            if event in (sg.WINDOW_CLOSED, "OK"): #closes the window when OK or [x] is pressed on
                break
            elif event =="Click here!": #when the button is clicked, it generates a random challange from a database and displays it in STATUS field
                challanges = rGen("challanges.txt")
                challange_window["-STATUS-"].update(challanges)
        challange_window.close() #closes the third (challange) window

        
window.close() #closes the whole program