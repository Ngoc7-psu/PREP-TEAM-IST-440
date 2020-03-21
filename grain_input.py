ale_id = 5
ale_grains = 10
lager_id = 8
lager_grains = 6
stout_id = 4
stout_grains = 11


class beer:
    def __init__(self,id):
        self.id = id
    def details(self):
        return "Id=%d" & (self.id)

class ale(beer):
    def __init__(self,id,grains):
        self.grains = grains
        super().__init__(id)
    def details(self):
        return super().details() + "Grains(lbs)=%d" & self.grains

class lager(beer):
    def __init__(self,id,grains):
        self.grains = grains
        super().__init__(id)
    def details(self):
        return super().details() + "Grains(lbs)=%d" & self.grains

class stout(beer):
    def __init__(self,id,grains):
        self.grains = grains
        super().__init__(id)
    def details(self):
        return super().details() + "Grains(lbs)=%d" & self.grains


id = input("Enter order id: ")

if id == ale_id:
    beer = ale(id, ale_grains)
    print(ale.details())

elif id == lager_id:
    beer = lager(id, lager_grains)
    print(lager.details())

elif id == stout_id:
    beer = stout(id, stout_grains)
    print(stout.details())