from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld

movie_world = MovieWorld("Test")
for _ in range(16):
    movie_world.add_dvd(DVD("A", 1, 1254, "February", 10))
print(len(movie_world.dvds), 15)
