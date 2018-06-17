class EquipmentHandler:
    def __init__(self):
        self.slots = {
            'mainhand': None,
            'offhand': None,
            'body': None,
            'legs': None,
            'shoes': None,
            'accessory': None
        }
    def equip(self, object, owner):
        target_slot = object.db.slot

        if self.slots[target_slot] is not None:
            self.unequip(target_slot, owner)
        self.slots[target_slot] = object
        object.location = None

    def unequip(self, slot, owner):
        if self.slots[slot] is not None:
            self.slots[target_slot].location = owner
        self.slots[target_slot] = None
