class human:
    def __init__(self, name, health, strenth, ):
        self.name = name
        self.health = health
        self.strenth = strenth
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def health(self):
        return self.health

    @health.setter
    def health(self, value):
        self.health = value

    @property
    def strenth(self):
        return self.strenth

    @strenth.setter
    def strength(self, value):
        self.strenth = value

