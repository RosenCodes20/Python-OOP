class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if result is None:
                    self.guests += people

    def free_room(self, room_number):
        for rooms in self.rooms:
            if rooms.number == room_number:
                people = rooms.guests
                result = rooms.free_room()
                if result is None:
                    self.guests -= people

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"


