import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import math
from functools import partial


#Klase, kas atbilst vienai virsotnei spēles kokā
class Virsotne:
    
    #Klases konstruktors, kas izveido virsotnes eksemplāru
    #Katrā virsotnes eksmeplārā glabājas virsotnes unikāls identifikators (id), skaitliskā virkne (virkne)
    #pirmā spēlētāja punkti (p1), otrā spēlētāja punkti(p2), un virsotnes atrašanās līmeņa numurs
    #Glabātie dati tiek padoti kā konstruktora argumenti
    def __init__(self, id, virkne, p1, p2, limenis):
        self.id=id
        self.virkne=virkne
        self.p1=p1
        self.p2=p2
        self.limenis=limenis
               
#Klase, kas atbilst spēles kokam        
class Speles_koks:
    
    #Klases konstruktors, kas izveido spēles koka eksemplāru
    #Spēles koka eksemplārs ietver sevī virsotņu kopu, kas tiek veidota kā Python saraksts un
    #loku kopu, kas tiek veidota kā Python vārdnīca (dictionary)
    #Gan virsotņu kopa, gan loku kopa sākotnējie ir tukšas
    #Virsotņu kopā glabāsies virsotnes viena aiz otras
    #Loku kopā glabāsies virsotnes unikāls identifikators kā vārdnīcas atslēga (key) un
    #ar konkrētu virsotni citu saistītu virsotņu unikālie identifikatori kā vērtības (values)
    def __init__(self):
        self.virsotnu_kopa=[]
        self.loku_kopa=dict()
    
    #Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)
        
    #Klases Speles_koks metode, kura papildina loku kopu, saņemot kā argumentus
    #virsotnes identifikatoru, no kuras loks iziet, un virsotnes identifikatoru, kurā loks ieiet
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id]=self.loku_kopa.get(sakumvirsotne_id,[])+[beiguvirsotne_id]

x1 = ''
j = 2
sp=Speles_koks()

def gajiena_parbaude (gajiena_tips,generetas_virsotnes,pasreizeja_virsotne):        
    if int(pasreizeja_virsotne[1])>0:
        global j
        id_new='A'+str(j)
        j+=1
        g = True
        mainita_virkne=pasreizeja_virsotne[1]
        #pozicija=mainita_virkne.find(skaitlis)
        
        if (gajiena_tips=='1'):
            mainita_virkne = str(int(mainita_virkne) -1)
        else:
            if (gajiena_tips=='2'):
                mainita_virkne = str(int(mainita_virkne) -2)
            else:
                mainita_virkne = str(int(mainita_virkne) -3) 

        limenis_new=pasreizeja_virsotne[4]+1
        if (int(mainita_virkne) < 4):
            if(limenis_new%2 == 0): 
                p1_new=-1 #atzīmē to, ka tā ir gala virsotne –> max uzvar
                p2_new=0
            else:
                p1_new=1 #atzīmē to, ka tā ir gala virsotne –> min uzvar
                p2_new=0

        else:
            p1_new=0 #atzīmē to, ka tā nav gala virsotne
            p2_new=0

        jauna_virsotne=Virsotne(id_new, mainita_virkne, p1_new, p2_new, limenis_new)
        parbaude=False
        i=0
        while (not parbaude) and (i<=len(sp.virsotnu_kopa)-1):
            if (sp.virsotnu_kopa[i].virkne==jauna_virsotne.virkne) and (sp.virsotnu_kopa[i].p1==jauna_virsotne.p1) and (sp.virsotnu_kopa[i].p2==jauna_virsotne.p2) and (sp.virsotnu_kopa[i].limenis==jauna_virsotne.limenis): #ja atrod kādu tādu pašu
                parbaude=True
            else:
                i+=1   
        if not parbaude:
                sp.pievienot_virsotni(jauna_virsotne)
                generetas_virsotnes.append([id_new, mainita_virkne, p1_new, p2_new, limenis_new])
                sp.pievienot_loku(pasreizeja_virsotne[0],id_new)
        else:
            j-=1
            sp.pievienot_loku(pasreizeja_virsotne[0],sp.virsotnu_kopa[i].id)

def sub(x):
    return x

def get_square_root(): 
    global x1
    x1 = username_entry.get() #monētu skaits 
    a=generate_tree()
    n = int(x1)
    rows=2*math.floor(math.sqrt(n/2)) #cik monētu vajadzētu ietilpināt vienā rindā
    load = Image.open("coin.png")
    r = math.floor(250/(rows+1)) #lai ietilpinātu visas monētas - cik lielām tām jābūt
    #monētām atvēl pusi laukuma augstumā = 600/2, visu laukumu platumā = 300 300*600

    F3 = Frame(mGui, bg="Blue", bd=2, relief=GROOVE)
    F3.grid(row=4, column=0)

    load = Image.open("coin.png")
    load = load.resize((r, r))
    heads = ImageTk.PhotoImage(load)
    sk = n
    for i in range(int(rows*2)):
        for j in range(int(rows)):
            if(sk > 0):
                z = Label(F3,image=heads)
                z.grid(column=j,row=i, sticky="news")
            sk-=1


    F3.create_window(window=F3)
    return x1

def generate_tree():
    #tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku  
    global sp      
    #tiek izveidots tukšs ģenerēto virsotņu saraksts
    generetas_virsotnes=[]
    #tiek izveidota sākumvirsotne spēles kokā
    sp.pievienot_virsotni(Virsotne('A1', x1, 0, 0, 1))
    #tiek pievienota pirmā virsotne ģenerēto virsotņu sarakstam
    generetas_virsotnes.append(['A1', x1, 0, 0, 1])
    #mainīgais, kurš skaita virsotnes

    #kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
    while len(generetas_virsotnes):
        #par pašreiz apskatāmo virsotni kļūst pirmā virsotne saģenerēto virsotņu sarakstā
        pasreizeja_virsotne=generetas_virsotnes[0]
        if(int(pasreizeja_virsotne[1])>3):
            #tiek pārbaudīts gājiens, kad spēlētājs paņem sev vieninieku
            gajiena_parbaude('1',generetas_virsotnes,pasreizeja_virsotne)
            #tiek pārbaudīts gājiens, kad spēlētājs paņem sev divnieku
            gajiena_parbaude('2',generetas_virsotnes,pasreizeja_virsotne)
            #tiek pārbaudīts gājiens, kad spēlētājs sadala divnieku
            gajiena_parbaude('3',generetas_virsotnes,pasreizeja_virsotne)
            #kad visi gājieni no pašreiz apskatāmās virsotnes ir apskatīti, šo virsotni dzēš no ģenerēto virsotņu saraksta
        generetas_virsotnes.pop(0)


    #ciks piešķir kokam min max vērtējumus 1 vai -1
    for x in range(len(sp.virsotnu_kopa)-1, -1, -1):
        lim = sp.virsotnu_kopa[x].limenis
        if (sp.virsotnu_kopa[x].p1==0):
            if(lim%2 == 0): #minimizetaja limenji
                m = 1
                for y in (sp.loku_kopa[sp.virsotnu_kopa[x].id]):
                    fix = y[1:]
                    if(m>sp.virsotnu_kopa[int(fix)-1].p1): m = -1
            else:            #maxzimizetaja limeni
                m = -1
                for y in (sp.loku_kopa[sp.virsotnu_kopa[x].id]):
                    fix = y[1:]
                    if(m<sp.virsotnu_kopa[int(fix)-1].p1): m = 1
            
            sp.virsotnu_kopa[x].p1=m

    #ciklam beidzoties, tiek izvadīta spēles koka virsotņu kopa ar min max vērtējumiem
    for x in sp.virsotnu_kopa:
        print(x.id,x.virkne,x.p1,x.p2,x.limenis)

    return sp

mGui = Tk()

mGui.geometry("300x600")
mGui.title('Game with coins')
mGui.resizable(0, 0)
mGui.configure(background="white")

mGui.columnconfigure(0, weight=1)
mGui.rowconfigure(0, weight=1)

FMas = Frame(mGui, bg="white")
FMas.grid(sticky=(N,E,S,W))

FMas.columnconfigure(0, weight=1)


F1 = Frame(FMas, bd=2, relief=GROOVE)
F1.grid(row=0, column=0, sticky=(N,W))

L1 = Label(F1, text="Cik monētu būs spēles sākumā?",font=("Arial", 10))
L1.grid(row=0, column=0, pady=5, sticky=(N,W))

number = IntVar()
username_entry = Entry(F1,width=10)
username_entry.grid(column=1, row=0, padx=2)

login_button = Button(F1, text="ok", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",   command=get_square_root)
login_button.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)


F2 = Frame(FMas, bd=2, relief=GROOVE)
F2.grid(row=1, column=0, sticky=(N,W))

L2 = Label(F2, text="Kurš sāks spēli?",font=("Arial", 10))
L2.grid(row=0, column=0, pady=5, sticky=(N,W))

ChkBox1=IntVar()
CB2 = Checkbutton(F2, text="Dators",font=("Arial", 10), variable=ChkBox1)
CB2.grid(row=0,column=1,padx=2)

ChkBox2=IntVar()
CB2 = Checkbutton(F2, text="Es", font=("Arial", 10),variable=ChkBox2)
CB2.grid(row=0,column=2,padx=2)


F4 = Frame(FMas, bd=2, relief=GROOVE)
F4.grid(row=3, column=0, sticky=(N,W))

L2 = Label(F4, text="Cik monētas ņemsi?",font=("Arial", 10))
L2.grid(row=0, column=0, pady=5, sticky=(N,W))


login_button = Button(F4, text="1", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",  command = sub(1))
login_button.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

login_button = Button(F4, text="2", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",  command = sub(2))
login_button.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)

login_button = Button(F4, text="3", font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue",  command = sub(3))
login_button.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

F5 = Frame(FMas, bd=2, relief=GROOVE)
F5.grid(row=4,column=0, sticky =(N,W))

#Text Field for Result
tfield = Text(F5, width=52, height=5)
tfield.grid(column=0, row=2, columnspan = 4, padx=5, pady=5)

mGui.mainloop()
sys.exit()


