import json

class Building:
    def __init__ (self, name, floors):
        self.name = name
        self.floors = floors

    def save(self, filename):     
        with open(filename, 'w') as text_file:
            json.dump(self.__dict__,text_file)
    
    def load(filename):
        with open(filename, 'r') as text_file:
            data = json.load(text_file)
            return building
        
building = Building('Empire State Building', 102)
building.save('text_file')

loaded_building = Building.load('text_file')
print(f"The {loaded_building.name} has {loaded_building.floors} floors.")