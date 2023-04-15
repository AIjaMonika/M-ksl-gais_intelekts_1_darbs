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

class TREE:
    def gajiena_parbaude (gajiena_tips,generetas_virsotnes,pasreizeja_virsotne, sp, j):        
        if int(pasreizeja_virsotne[1])>0:
            id_new='A'+str(j)
            j+=1

            mainita_virkne=pasreizeja_virsotne[1]
            
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
        return j
    
    def genere_koku(generetas_virsotnes, sp, j):
        #kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
       
        while len(generetas_virsotnes):
            #par pašreiz apskatāmo virsotni kļūst pirmā virsotne saģenerēto virsotņu sarakstā
            pasreizeja_virsotne=generetas_virsotnes[0]
            if(int(pasreizeja_virsotne[1])>3):
                #tiek pārbaudīts gājiens, kad spēlētājs paņem sev vieninieku
                j = TREE.gajiena_parbaude('1',generetas_virsotnes,pasreizeja_virsotne, sp, j)
                #tiek pārbaudīts gājiens, kad spēlētājs paņem sev divnieku
                j = TREE.gajiena_parbaude('2',generetas_virsotnes,pasreizeja_virsotne, sp, j)
                #tiek pārbaudīts gājiens, kad spēlētājs sadala divnieku
                j = TREE.gajiena_parbaude('3',generetas_virsotnes,pasreizeja_virsotne, sp, j)
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

        return sp #Atgriež izveidotu spēlēs koku
    
    def printe_koku(sp):
        #ciklam beidzoties, tiek izvadīta spēles koka virsotņu kopa ar min max vērtējumiem
        for x in sp.virsotnu_kopa:
            print(x.id,x.virkne,x.p1,x.p2,x.limenis)
