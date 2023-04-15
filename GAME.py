import random as rand
from TREE import *
import tkinter as tk

#tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()
#tiek izveidots tukšs ģenerēto virsotņu saraksts
generetas_virsotnes=[]

class game_state:

    def __init__(self, start:int, end:int, computerMinMax: int, player:str, turns, coins:int, vertex: int, csize: int, crows: int, text_message: str, root = False):
        self.start = start #sākuma skaitļa virsotnes minmax vērtiba
        self.end = end
        self.computerMinMax = computerMinMax #vai dators ir minimizētajs, vai maksimizētājs
        self.player = player #aktuālais spēlētājs
        self.turns =turns #pēdējais gājiens
        self.coins = coins #aktuālais monētu skaits
        self.vertex = vertex #aktuālā virsotne, kas atbilst monētu skaitam
        self.csize = csize #priekš GUI
        self.crows = crows # priekš GUI
        self.text_message = text_message # ziņojums, ko redz lietotājs
        self.root = root


def computer_turn(sp, tfield):
    MinMax_exists = False
    game_state.turns = game_state.coins
    #datora gājiens
    if(game_state.coins > 3):
        for y in (sp.loku_kopa[sp.virsotnu_kopa[game_state.vertex].id]):
            fix = y[1:]
            if(sp.virsotnu_kopa[int(fix)-1].p1 == game_state.player):    #atrod kuram no konkrētās virsotnes bērniem 
                game_state.vertex = int(fix)-1                                  #ir datoram atbilstošā MinMax algoritma vērtība       
                game_state.coins = int(sp.virsotnu_kopa[game_state.vertex].virkne)
                game_state.turns = game_state.turns - game_state.coins
                game_state.text_message = 'Computer game state coins:= ' + str(game_state.coins) +'\n'
                print('Computer game state coins:= ',game_state.coins)
                tfield.insert(tk.END, game_state.text_message)
                MinMax_exists = True
                game_state.player = game_state.player*(-1)
                return

        if(not MinMax_exists):      #ja visas virsotnes ved uz cilvēka uzvaru, tad izvēlas pēdējo apskatīto 
            game_state.vertex = int(fix)-1                                       
            game_state.coins = int(sp.virsotnu_kopa[game_state.vertex].virkne)
            game_state.turns = game_state.turns - game_state.coins
            game_state.text_message = 'Computer game state coins:= ' + str(game_state.coins) +'\n'
            print('Computer game state coins:= ',game_state.coins)
            tfield.insert(tk.END, game_state.text_message)
            game_state.player = game_state.player*(-1)
            get_winner(tfield)
            return
    else:
        get_winner(tfield)
    return


def human_turn(sp, tfield):
    if(game_state.coins > 3):
        game_state.coins = game_state.coins - game_state.turns
        for y in (sp.loku_kopa[sp.virsotnu_kopa[game_state.vertex].id]):
            fix = y[1:] #virsotnes kārtas numurs masīvā
            if(sp.virsotnu_kopa[int(fix)-1].virkne == str(game_state.coins)):  #atrod to kuram no virsotnes bērniem ir šāda vērtība
                game_state.vertex= int(fix)-1 #pamaina aktuālās virsotnes kārtas skaitli masīvā
                game_state.text_message = 'Human game state coins:= ' + str(game_state.coins) +'\n'
                tfield.insert(tk.END, game_state.text_message)
                print(game_state.text_message)
                game_state.player = game_state.player*(-1)
    else:
        get_winner(tfield)
    return
         
def get_winner(tfield):
    if(game_state.computerMinMax ==  game_state.player):
        game_state.text_message = 'Computer won!\n'
        tfield.insert(tk.END, game_state.text_message)
        print('Computer won!')
    else:
        game_state.text_message = 'Human won!\n'
        tfield.insert(tk.END, game_state.text_message)
        print('Human won!')
    return

def play_game(sp, tfield):
    if(game_state.player == game_state.computerMinMax):
        computer_turn(sp, tfield)
    elif(game_state.player == game_state.computerMinMax*(-1)):
        human_turn(sp, tfield)
        computer_turn(sp, tfield)
        




        


  