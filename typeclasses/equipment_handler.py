class EquipmentHandler:
    def __init__(self, owner):
        self.slots = {
            'mainhand': None,
            'offhand': None,
            'body': None,
            'legs': None,
            'shoes': None,
            'accessory': None
        }
        self.owner = owner
    def equip(self, object):
        target_slot = object.db.slot

        if self.slots[target_slot] is not None:
            self.slots[target_slot].location = self.owner

        self.slots[target_slot] = object
        object.location = None
