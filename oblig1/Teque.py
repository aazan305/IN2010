
import sys

class Teque:
    def __init__(self):
        self.liste=[]

    def push_front(self,x):
        self.liste.insert(0,x)
        

    def push_back(self,x):
        self.liste.append(x)
        
    def push_middle(self,x):
        middle=(len(self.liste) +1)//2
        self.liste.insert(middle,x)
        
    
    
    def get(self,i):
        val=self.liste[i]
        print(val)

class Main:
    teque=Teque()
    
    input_linje = sys.stdin.read().strip().split('\n')
    N = int(input_linje[0].strip())

    for linje in input_linje[1:]:
        deler = linje.strip().split()
        
        operasjon = deler[0]
        
        verdi = int(deler[1])
    
        if operasjon == "push_back":
            teque.push_back(verdi)
        
        if operasjon == "push_front":
            teque.push_front(verdi)
        
        if operasjon == "push_middle":
            teque.push_middle(verdi)
        elif operasjon =="get":
            teque.get(verdi)
    



        