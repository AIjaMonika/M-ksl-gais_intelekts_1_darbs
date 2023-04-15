from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import math

from TREE import *
from GAME import *

mGui = tk.Tk()

mGui.geometry("300x600")
mGui.title('Game with coins')
mGui.resizable(0, 0)
mGui.configure(background="white")

FMas = Frame(mGui, bg="white")
FMas.columnconfigure(0, weight=1)

gameWindow_objects = [FMas]
coins = tk.IntVar(mGui, value = 5)
ChkBox1 = tk.IntVar(mGui, value = 0)
ChkBox2 = tk.IntVar(mGui, value = 1)

#tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()
#tiek izveidots tukšs ģenerēto virsotņu saraksts
generetas_virsotnes=[]

def first_window():
    F1 = Frame(FMas, bd=2, width = 10)
    F1.grid(row=0, column=0)

    L1 = Label(F1, text="Cik monētu būs spēles sākumā?",font=("Arial", 10))
    L1.grid(row=0, column=0, pady=5)

    username_entry = Entry(F1,width=15, textvariable = coins)
    username_entry.grid(column=1, row=0, padx=2)

    F2 = Frame(FMas, bd=2)
    F2.grid(row=1, column=0)

    L2 = Label(F2, text="Kurš sāks spēli?",font=("Arial", 10))
    L2.grid(row=0, column=0, pady=5)

    
    CB1 = Checkbutton(F2, text="Dators",font=("Arial", 10), variable=ChkBox1)
    CB1.grid(row=0,column=1,padx=2)

    
    CB2 = Checkbutton(F2, text="Es", font=("Arial", 10),variable=ChkBox2)
    CB2.grid(row=0,column=2,padx=2)

    START_btn = Button(F2, text="START", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue", command = lambda: startGame())
    START_btn.grid(column=3, row=0, sticky=tk.E, padx=10, pady=5)
    
    menuWindow_objects = [FMas]
    pack_all(menuWindow_objects)

def pack_all(guiObjectList):
    for object in guiObjectList:
        object.pack()
        
def startGame():
    global sp
    global generetas_virsotnes
    sp = Speles_koks()
    generetas_virsotnes=[]

    computer = ChkBox1.get()
    #es = ChkBox2.get()
    game_state.coins = coins.get()
    print(game_state.coins)
    calculate_r_rows()
    
    #tiek izveidota sākumvirsotne spēles kokā
    sp.pievienot_virsotni(Virsotne('A1', str(game_state.coins), 0, 0, 1))
    #tiek pievienota pirmā virsotne ģenerēto virsotņu sarakstam
    generetas_virsotnes.append(['A1', str(game_state.coins), 0, 0, 1])
    #mainīgais, kurš skaita virsotnes
    j = 2
    sp = TREE.genere_koku(generetas_virsotnes, sp, j)
    TREE.printe_koku(sp)

    #mainīgo inicializācija ar virsotnes vērtībām
    game_state.vertex = 0 #skaitītājs sp.virsotnu_kopa
    game_state.coins = int(sp.virsotnu_kopa[0].virkne) #monētu skaits
    game_state.start = sp.virsotnu_kopa[0].p1 #piešķir 1 /-1 

    if(computer): #dators sāk
        game_state.computerMinMax = game_state.start #ja dators sāk, tad datora min max nemainās, ja cilvēks sāk, mainās uz pretējo
        game_state.player = game_state.computerMinMax
    else: #cilvēks sāk
        game_state.computerMinMax = game_state.start*(-1)
        game_state.player = game_state.computerMinMax*(-1)
    
    gameWindow()

def pack_forget_all(guiObjectList, topLevel = None):
    for object in guiObjectList:
        object.grid_forget()
    if topLevel != None:
        topLevel.destroy()

def newGame(tfield):
    tfield.delete("1.0","end")
    pack_forget_all(gameWindow_objects)
    first_window()

def gameWindow():
    pack_forget_all(gameWindow_objects)
    F1 = Frame(FMas, bd=2, relief=GROOVE)
    F1.grid(row=0,column=0, sticky =(N,W))

    F2 = Frame(FMas, bd=2, relief=GROOVE)
    F2.grid(row=1, column=0,columnspan = 4, sticky=(N,W))

    L2 = Label(F2, text="Cik monētas ņemsi?",font=("Arial", 10))
    L2.grid(row=0, column=0, pady=5, padx = 5, sticky=(N,W))

    button1 = Button(F2, text="1", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",  command = lambda: load_coins(1, tfield))
    button1.grid(column=1, row=0, sticky=tk.E, padx=7, pady=5)

    button2 = Button(F2, text="2", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",  command = lambda: load_coins(2, tfield))
    button2.grid(column=2, row=0, sticky=tk.E, padx=7, pady=5)

    button3 = Button(F2, text="3", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",  command = lambda: load_coins(3,tfield))
    button3.grid(column=3, row=0, sticky=tk.E, padx=7, pady=5)

    RESET_btn = Button(F2, text="RESET", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",  command = lambda: newGame(tfield))
    RESET_btn.grid(column=4, row=0, sticky=tk.E, padx=3, pady=5)

    FCoin = Frame(FMas, bg="white")
    FCoin.grid(row=2,column=0, sticky =(N,W))
    
    game_state.text_message=' '
    tfield = Text(FCoin, width=52, height=5)
    tfield.grid(column=0, row=0, columnspan = 4, padx=5, pady=5)
    if(game_state.player == game_state.computerMinMax):
        play_game(sp, tfield)
    

    load = Image.open("coin.png")
    load = load.resize((game_state.csize, game_state.csize))

    heads = ImageTk.PhotoImage(load)
    sk = game_state.coins
    for i in range(1,(int(game_state.crows*2)+2)):
        for j in range(int(game_state.crows)):
            if(sk > 0):
                z = Label(FCoin,image=heads)
                z.grid(column=j,row=i, sticky="news")
            sk-=1
    
    get_square_root() 
    #FCoin.create_window(window=FCoin)

def get_square_root():  
    

    F3 = Frame(mGui, bg="Blue", bd=2, relief=GROOVE)
    F3.grid(row=4, column=0)

    F3.create_window(window=F3)

def load_coins(x, tfield):
    tfield.delete("1.0","end")
    game_state.turns = x
    play_game(sp, tfield)
    

def calculate_r_rows():
    game_state.crows=2*math.floor(math.sqrt(game_state.coins/2)) #cik monētu vajadzētu ietilpināt vienā rindā
    game_state.csize = math.floor(250/(game_state.crows+1)) #lai ietilpinātu visas monētas - cik lielām tām jābūt
    #monētām atvēl pusi laukuma augstumā = 600/2, visu laukumu platumā = 300 300*600




