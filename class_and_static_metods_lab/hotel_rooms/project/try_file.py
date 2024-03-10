from project.hotel import Hotel
from project.room import Room


room = Room(1, 3)
hotel = Hotel("Some Hotel")

hotel.add_room(room)
hotel.take_room(1, 3)
hotel.free_room(1)
print(hotel.guests, 0)
print(hotel.rooms[0].is_taken, False)
print(hotel.rooms[0].guests, 0)