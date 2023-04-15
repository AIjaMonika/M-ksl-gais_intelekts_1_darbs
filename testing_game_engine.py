from GAME import *
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


#Funkcija, kas atbilstoši veiktajam gājienam iegūst jaunu spēles koka virsotni un
#papildina speles koka virsotņu kopu un loku kopu
#Funkcija kā argumentus saņem veiktā gājiena tipu, sarakstu ar jau iepriekš saģenerētajām virsotnēm, kuras apskata 
#vienu pēc otras, un pašreiz apskatāmo virsotni
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
     
#tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()
#tiek izveidots tukšs ģenerēto virsotņu saraksts
generetas_virsotnes=[]
#tiek izveidota sākumvirsotne spēles kokā
sp.pievienot_virsotni(Virsotne('A1', '7', 0, 0, 1))
#tiek pievienota pirmā virsotne ģenerēto virsotņu sarakstam
generetas_virsotnes.append(['A1', '7', 0, 0, 1])
#mainīgais, kurš skaita virsotnes
j=2

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


#ciklam beidzoties, tiek izvadīta spēles koka loku kopa
'''Printē loku kopu
for x, y in sp.loku_kopa.items():
    print(x, y)  
print(len(sp.virsotnu_kopa))
'''

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

#mainīgo inicializācija ar virsotnes vērtībām
game_state.vertex = 0 #skaitītājs sp.virsotnu_kopa
game_state.coins = int(sp.virsotnu_kopa[0].virkne) #monētu skaits
game_state.start = sp.virsotnu_kopa[0].p1 #piešķir 1 /-1 


def computer_turn():
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
                print('Computer game state coins:= ',game_state.coins)
                MinMax_exists = True
                game_state.player = game_state.player*(-1)
                return

        if(not MinMax_exists):      #ja visas virsotnes ved uz cilvēka uzvaru, tad izvēlas pēdējo apskatīto 
            game_state.vertex = int(fix)-1                                       
            game_state.coins = int(sp.virsotnu_kopa[game_state.vertex].virkne)
            game_state.turns = game_state.turns - game_state.coins
            print('Computer game state coins:= ',game_state.coins)
            game_state.player = game_state.player*(-1)
            get_winner()
            return
    else:
        get_winner()
    return


def human_turn():
    if(game_state.coins > 3):
        game_state.coins = game_state.coins - game_state.turns
        for y in (sp.loku_kopa[sp.virsotnu_kopa[game_state.vertex].id]):
            fix = y[1:] #virsotnes kārtas numurs masīvā
            if(sp.virsotnu_kopa[int(fix)-1].virkne == str(game_state.coins)):  #atrod to kuram no virsotnes bērniem ir šāda vērtība
                game_state.vertex= int(fix)-1 #pamaina aktuālās virsotnes kārtas skaitli masīvā
                print('Human game state coins:= ', game_state.coins)
                game_state.player = game_state.player*(-1)
    else:
        get_winner()
    return
         
def get_winner():
    if(game_state.computerMinMax ==  game_state.player):
        print('Computer won!')
    else:
        print('Human won!')
    return

def play_game():
    if(game_state.player == game_state.computerMinMax):
        computer_turn()
    elif(game_state.player == game_state.computerMinMax*(-1)):
        human_turn()
        computer_turn()


        
                                               
#cilvēka gājiens   
gajiens = int(input('Kam būs pirmais gājiens? -1= cilvēkam, 1=datoram'))  
game_state.computerMinMax = game_state.start*gajiens #ja dators sāk, tad datora min max nemainās, ja cilvēks sāk, mainās uz pretējo

if (gajiens == 1):
    game_state.player = game_state.computerMinMax
else:
    game_state.player = game_state.computerMinMax*-1

while(game_state.coins > 3):
    if (game_state.computerMinMax == game_state.player):
        play_game()
    else:
        game_state.turns = int(input('Ievadiet gājienu: '))
        play_game()










    