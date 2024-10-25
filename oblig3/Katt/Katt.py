import sys  

def les_fil(filnavn):
    
    #Leser inn et filnavn og bygger et tre basert på innholdet i filen.
    #Returnerer roten av treet og treet som en ordbok.
    
    tree = {}  
    with open(filnavn, 'r') as fil:
        linjer = fil.readlines()  
        forsteNode = int(linjer[0].strip())  # Første linje inneholder roten
        for linje in linjer[1:]:
            noder = list(map(int, linje.strip().split()))  # Splitt linjen i noder
            if noder[0] == -1:  # 
                break
            foreldre = noder[0]  # Første nummer er foreldrenoden
            for barn in noder[1:]:
                if barn == -1: 
                    break
                tree[barn] = foreldre  # Legger til barn og deres foreldre i ordboken
    return forsteNode, tree 
def finn_vei_til_rot(tree, forsteNode):
    
    veien = []  #
    current = forsteNode
    while current in tree:  # Fortsett til man når roten
        veien.append(current)  
        current = tree[current]  # Gå til foreldre-noden
    veien.append(current)  # Legg til roten til slutt
    return veien

def main():
    
   
    filnavn = sys.argv[1]
    forsteNode, tree = les_fil(filnavn)  

    veien = finn_vei_til_rot(tree, forsteNode)  # Finner veien fra første node til roten
    for node in veien:  # Skriver ut hver node i veien
        print(node, end=" ")

if __name__ == '__main__':
    main()
