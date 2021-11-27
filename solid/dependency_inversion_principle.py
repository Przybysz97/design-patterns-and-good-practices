class Computer:
    def get_reviews(self):
        pass

    def get_specs(self):
        pass


class Software:
    def get_reviews(self):
        pass

    def get_requirements(self):
        pass


class Favourites:
    def __init__(self):
        self._favourites = []

    def add_computer(self, computer: Computer):
        self._favourites.append(computer)

    def add_software(self, software: Software):
        self._favourites.append(software)
