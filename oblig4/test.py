import sys

def les_filmer(film_file):
    filmer = {}
    print("Movies:")
    with open(film_file, 'r', encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 4:  # Handle movie file with an extra field for number of ratings
                movie_id = fields[0]
                movie_title = fields[1]
                movie_rating = fields[2]
                num_ratings = fields[3]
                filmer[movie_id] = {'title': movie_title, 'rating': movie_rating, 'num_ratings': num_ratings}
                print(f"Movie ID: {movie_id}, Title: {movie_title}, Rating: {movie_rating}, Ratings: {num_ratings}")
    return filmer

def les_skuespillere(actor_file, filmer):
    print("\nActors:")
    with open(actor_file, 'r', encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) >= 2:
                actor_id = fields[0]
                actor_name = fields[1]
                movie_ids = fields[2:]
                movie_list = [filmer[movie_id]['title'] if movie_id in filmer else f"Unknown movie ({movie_id})" for movie_id in movie_ids]
                print(f"Actor ID: {actor_id}, Name: {actor_name}, Movies: {', '.join(movie_list)}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <actors_file> <movies_file>")
        sys.exit(1)

    actor_file = sys.argv[1]
    film_file = sys.argv[2]
    
    # Read and print movies
    filmer = les_filmer(film_file)
    
    # Read and print actors, using the movie details read from the movie file
    les_skuespillere(actor_file, filmer)

if __name__ == "__main__":
    main()
