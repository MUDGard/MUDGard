from typeclasses.objects import Object

class EquipmentObject(Object):
    def at_object_creation(self):
        self.price = 0
        self.slot = None
