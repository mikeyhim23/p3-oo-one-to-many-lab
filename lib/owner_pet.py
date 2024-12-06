class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f'Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.')

        if owner is not None and not isinstance(owner, Owner):
            raise Exception('The owner must be an instance of the Owner class.')

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        if not isinstance(self, Owner):
            raise Exception('The object must be an Owner instance.')
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('The object must be a Pet instance.')
        pet.owner = self

    def get_sorted_pets(self):
        if not isinstance(self, Owner):
            raise Exception('The object must be an Owner instance.')

        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets
    pass