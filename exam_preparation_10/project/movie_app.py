from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")

        new_user = User(username, age)
        if new_user not in self.users_collection:
            self.users_collection.append(new_user)
            return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))

        except StopIteration:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute_name, attribute in kwargs.items():
            if attribute_name == "title":
                movie.title = attribute

            elif attribute_name == "age_restriction":
                movie.age_restriction = attribute

            elif attribute_name == "year":
                movie.year = attribute

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie.owner.username == user.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        user = [u for u in self.users_collection if u.username == username][0]

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted([m for m in self.movies_collection], key=lambda x: (-x.year, x.title))
        if sorted_movies:
            return "\n".join(map(str, [m.details() for m in sorted_movies]))

    def __str__(self):
        users = f"All users: {', '.join(map(str, [u.username for u in self.users_collection]))}\n" if self.users_collection else "All users: No users.\n"
        movies = f"All movies: {', '.join(map(str, [m.title for m in self.movies_collection]))}" if self.movies_collection else "All movies: No movies."

        return users + movies
