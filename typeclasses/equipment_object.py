from typeclasses.objects import Object

class EquipmentObject(Object):
    def at_object_creation(self):
        self.db.price = 0
        self.db.slot = None
