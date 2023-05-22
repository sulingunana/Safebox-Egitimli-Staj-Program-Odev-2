import json

class MovieSelector:
    def __init__(self, movie_list, file_name):
        self.movie_list = movie_list
        self.file_name = file_name

    def select_movie(self, number):
        selected_movie = self.movie_list[int(number) - 1]
        return selected_movie

    def save(self, movie_name):
        data = {"selected_movie": movie_name}
        with open(self.file_name, "w") as file:
            json.dump(data, file)

# Film listesi ve dosya adı
movie_list = ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]
file_name = "movies.json"

# MovieSelector sınıfından bir örnek oluşturma
movie_selector = MovieSelector(movie_list, file_name)

# Kullanıcıdan bir film seçmesini isteme
selected_movie = movie_selector.select_movie(input("Select a movie 1-5: "))

# Seçilen filmi ekrana yazdırma
print("Selected movie:", selected_movie)

# Seçilen filmi JSON dosyasına kaydetme
movie_selector.save(selected_movie)

# Bilgilendirme mesajı yazdırma
print("Movie saved to JSON file.")
