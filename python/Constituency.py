class Constituency:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_details(self):
        return f"Constituency: {self.name}, Population: {self.population}"
