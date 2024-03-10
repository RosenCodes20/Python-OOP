def start_playing(self):
    return self.play()


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))
