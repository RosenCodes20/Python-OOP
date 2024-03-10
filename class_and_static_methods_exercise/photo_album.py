from math import ceil


class PhotoAlbum:
    photos_per_page = 4
    dashes_count = 11
    symbol = "-"

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.photos_per_page))

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < self.photos_per_page:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self):
        dashes = [self.dashes_count * self.symbol]
        for page in self.photos:
            dashes.append(("[] " * len(page)).rstrip())
            dashes.append(self.dashes_count * self.symbol)

        return "\n".join(dashes)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

