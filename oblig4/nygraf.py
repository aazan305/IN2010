from collections import deque, defaultdict, Counter
import heapq
import sys


def les_filmer(film_file):
    filmer = {}
    with open(film_file, 'r', encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Ensure at least 4 fields for movie ID, title, rating, and number of ratings
                movie_id = fields[0]
                movie_title = fields[1]
                movie_rating = float(fields[2])
                num_ratings = fields[3]  # This can be stored if needed
                filmer[movie_id] = {'title': movie_title, 'rating': movie_rating, 'num_ratings': num_ratings}
    return filmer


def les_skuespillere(actor_file, filmer):
    skuespillere = {}
    with open(actor_file, 'r', encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 2:
                actor_id = fields[0]
                actor_name = fields[1]
                film_ids = fields[2:]
                skuespillere[actor_id] = {'name': actor_name, 'films': film_ids}
    return skuespillere


def bygg_graf(skuespillere):
    G = defaultdict(dict)
    for actor, data in skuespillere.items():
        for film in data['films']:
            for co_actor, co_data in skuespillere.items():
                if actor != co_actor and film in co_data['films']:
                    if co_actor not in G[actor]:
                        G[actor][co_actor] = {'films': [film]}
                    else:
                        G[actor][co_actor]['films'].append(film)
    return G


def finne_korteste_vei(G, start, slutt):
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        for neighbor in G[node]:
            if neighbor not in visited:
                if neighbor == slutt:
                    film = G[node][neighbor]['films'][0]
                    return path + [neighbor], film
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, None


def formater_sti(sti, filmer, skuespillere, G, total_vekt=None):
    if not sti:
        return "Ingen sti funnet."

    formatert_sti = skuespillere[sti[0]]['name']
    unique_movies = set()  # Use a set to avoid duplicates
    for i in range(len(sti) - 1):
        actor1 = sti[i]
        actor2 = sti[i + 1]
        film = G[actor1][actor2]['films'][0]
        film_title = filmer[film]['title']
        film_rating = filmer[film]['rating']
        unique_movies.add((film, film_title, film_rating))  # Store unique films
        formatert_sti += f"\n===[ {film_title} ({film_rating}) ] ===> {skuespillere[actor2]['name']}"
    
    total_weight = sum(-rating for _, _, rating in unique_movies)  # Calculate total weight
    if total_weight is not None:
        formatert_sti += f"\nTotal weight: {total_weight:.1f}"
    
    return formatert_sti


def finne_chilleste_vei(G, start, slutt, filmer):
    heap = [(0, start, [start], set())]  # Include a set to track used films
    visited = set()

    while heap:
        current_weight, node, path, used_films = heapq.heappop(heap)

        if node == slutt:
            return path, -current_weight  # Return positive weight

        if node in visited:
            continue
        visited.add(node)

        for neighbor, data in G[node].items():
            if neighbor not in visited:
                film = data['films'][0]
                film_weight = -filmer[film]['rating']  # Negative to prioritize higher ratings
                if film not in used_films:
                    heapq.heappush(heap, (current_weight + film_weight, neighbor, path + [neighbor], used_films | {film}))

    return None, None


def tell_komponenter(G):
    visited = set()
    komponent_storrelser = []

    def dfs(node):
        stack = [node]
        size = 0
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                size += 1
                stack.extend(neigh for neigh in G[current] if neigh not in visited)
        return size

    for node in G:
        if node not in visited:
            komponent_storrelser.append(dfs(node))

    teller = Counter(komponent_storrelser)
    print("\nOppgave 4\n")
    for storrelse, antall in sorted(teller.items(), reverse=True):
        print(f"Det finnes {antall} komponenter av størrelse: {storrelse}")


def main(actor_file, film_file):
    filmer = les_filmer(film_file)
    skuespillere = les_skuespillere(actor_file, filmer)
    G = bygg_graf(skuespillere)

    print("\nOppgave 1\n")
    print(f"Nodes: {len(G)}")
    print(f"Edges: {sum(len(neigh) for neigh in G.values()) // 2}")

    par = [
        ('nm0000313', 'nm0000375', 'Jeff Bridges', 'Robert Downey Jr.'),
        ('nm0038355', 'nm1107001', 'Anthony Mackie', 'Tadanobu Asano'),
        ('nm0000313', 'nm1107001', 'Jeff Bridges', 'Tadanobu Asano')
    ]

    print("\nOppgave 3\n")
    for actor1, actor2, name1, name2 in par:
        print(f"Chilleste vei fra {name1} til {name2}:")
        sti, total_vekt = finne_chilleste_vei(G, actor1, actor2, filmer)
        resultat2 = formater_sti(sti, filmer, skuespillere, G, total_vekt)
        print(resultat2)

    tell_komponenter(G)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Feil: for lite filer")
        sys.exit(1)

    actor_file = sys.argv[1]
    film_file = sys.argv[2]

    main(actor_file, film_file)
