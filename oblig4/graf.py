import sys
import networkx as nx
from collections import deque,Counter

def les_filmer(film_file):
    filmer = {}
    with open(film_file, 'r', encoding='utf-8') as f:  # Spesifiser encoding som UTF-8
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 3:
                film_id = fields[0]
                film_title = fields[1]
                film_rating = float(fields[2])
                filmer[film_id] = {'title': film_title, 'rating': film_rating}
    return filmer

def les_skuespillere(actor_file, filmer):
    skuespillere = {}
    with open(actor_file, 'r', encoding='utf-8') as f:  # Spesifiser encoding som UTF-8
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 2:
                actor_id = fields[0]
                actor_name = fields[1]
                film_ids = [film_id for film_id in fields[2:] if film_id in filmer]
                skuespillere[actor_id] = {'name': actor_name, 'films': film_ids}
    return skuespillere

def bygg_graf(skuespillere): # bygger grafen med å bruke networkx library
    G = nx.Graph()
    for actor, data in skuespillere.items():
        for film in data['films']:
            for co_actor, co_data in skuespillere.items():
                if actor != co_actor and film in co_data['films']:
                    if G.has_edge(actor, co_actor):
                        G[actor][co_actor]['films'].append(film)
                    else:
                        G.add_edge(actor, co_actor, films=[film])
    return G

def finne_korteste_vei(G, start, slutt): # bruker BFS algortimen for å finne korteste vei mellom to skuespiller
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                if neighbor == slutt:
                    film = G[node][neighbor]['films'][0]
                    return path + [neighbor], film
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, None

def formater_sti(sti, filmer, skuespillere, G, total_vekt=None):  # metode for å få svar som innleveringsoppgaven
    if not sti:
        return "Ingen sti funnet."

    formatert_sti = skuespillere[sti[0]]['name']
    for i in range(len(sti) - 1):
        actor1 = sti[i]
        actor2 = sti[i + 1]
        film = G[actor1][actor2]['films'][0]
        film_title = filmer[film]['title']
        film_rating = filmer[film]['rating']
        formatert_sti += f"\n===[ {film_title} ({film_rating}) ] ===> {skuespillere[actor2]['name']}"
    if total_vekt is not None :
        formatert_sti += f"\nTotal weight: {total_vekt:.1f}"
    return formatert_sti

def finne_chilleste_vei(G,start,slutt): # bruke networkx for å finne chilleste vei som bruke dijkstra algoritmen
    try:
        sti=nx.dijkstra_path(G,start,slutt,weight='vekt')
        total_vekt= nx.dijkstra_path_length(G,start,slutt,weight='vekt')
        return sti,total_vekt
    except nx.NetworkXNoPath:
        return None, None

def tell_komponenter(G):
    # Finn alle komponentene i grafen
    komponenter = list(nx.connected_components(G))

    # Beregn størrelsen på hver komponent
    komponent_storrelser = [len(komponent) for komponent in komponenter]

    # Tell hvor mange komponenter det er av hver størrelse
    teller = Counter(komponent_storrelser)

    # Skriv ut resultatet
    print("\nOppgave 4\n")
    for storrelse, antall in sorted(teller.items(), reverse=True):
        print(f"Det finnes {antall} komponenter av størrelse : {storrelse}")   



def main(actor_file, film_file):
    filmer = les_filmer(film_file)
    skuespillere = les_skuespillere(actor_file, filmer)
    G = bygg_graf(skuespillere)

    # Skriv ut antall noder og kanter
    print("\nOppgave 1\n")
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")

    # Definer par av skuespillere for å finne stien mellom
    par = [
        ('nm0000313','nm0000375','Jeff Bridges','Robert Downey Jr.'),
        ('nm0038355','nm1107001','Anthony Mackie','Tadanobu Asano'),
        ('nm0000313','nm1107001','Jeff Bridges','Tadanobu Asano')
    ]

    # Skriv ut korteste vei
    print("\nOppgave 2\n")
    for actor1, actor2, name1, name2 in par:
        print(f"Sti fra {name1} til {name2}:")
        sti, film = finne_korteste_vei(G, actor1, actor2)
        resultat = formater_sti(sti, filmer, skuespillere, G)
        print(resultat)
    # Skriv chilleste vei 
    
    print("\nOppgave 3\n")
    for actor1, actor2, name1, name2 in par:
        print(f"Chilleste vei fra {name1} til {name2}:")
        sti, total_vekt = finne_chilleste_vei(G, actor1, actor2)
        resultat2 = formater_sti(sti, filmer, skuespillere, G,total_vekt)
        print(resultat2)

    tell_komponenter(G)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Feil: for lite filer")
        sys.exit(1)

    actor_file = sys.argv[1]
    film_file = sys.argv[2]

    main(actor_file, film_file)
