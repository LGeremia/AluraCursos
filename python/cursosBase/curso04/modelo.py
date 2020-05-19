class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    def give_like(self):
        self._likes += 1

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return "{} - {} - {}".format(self._name, self.year, self._likes)

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return "{} - {} - {} - {}".format(self._name, self.year, self._likes, self.duration)

class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return "{} - {} - {} - {}".format(self._name, self.year, self._likes, self.seasons)

class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self.program(item)

    @property
    def listagem(self):
        return self._programs

    def __len__(self):
        return len(self._programs)

senhor_dos_aneis_1 = Movie('Lord of the Rings - The Fellowship of the Ring', 2001, 208)
senhor_dos_aneis_2 = Movie('Lord of the Rings - Two Towers', 2002, 228)
senhor_dos_aneis_3 = Movie('Lord of the Rings - The Return of the King', 2003, 218)
o_ultimo_reino = Series('The Last Kingdom', 2015, 4)
vikings = Series('Vikings', 2012, 6)

o_ultimo_reino.give_like()
o_ultimo_reino.give_like()
vikings.give_like()
senhor_dos_aneis_1.give_like()
senhor_dos_aneis_1.give_like()
senhor_dos_aneis_2.give_like()
senhor_dos_aneis_3.give_like()
senhor_dos_aneis_3.give_like()
senhor_dos_aneis_3.give_like()

series_movies = [o_ultimo_reino, senhor_dos_aneis_1, senhor_dos_aneis_2, vikings, senhor_dos_aneis_3]

weekend_playlist = Playlist("Fim de Semana", series_movies)

print("A sua playlist tem o tamanho {} ".format(len(weekend_playlist)))

for program in weekend_playlist.listagem:
    print(program)
