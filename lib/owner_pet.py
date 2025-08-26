# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return all pets belonging to this owner"""
        return self._pets

    def add_pet(self, pet):
        """Add a pet, but only if it’s a Pet instance"""
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self
        else:
            raise TypeError("Only Pet instances can be added")

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []   # class variable to store all Pet instances

    def __init__(self, name, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = None  # gets set when added to an Owner

        Pet.all.append(self)
