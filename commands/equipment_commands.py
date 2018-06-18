from evennia.commands.default.muxcommand import MuxCommand
from evennia import utils

slots = ['accessory', 'shoes', 'legs', 'body', 'offhand', 'mainhand']

class CmdSlot(MuxCommand):
    """
    Set the slot of an equipment object.

    Usage:
        @slot [object] = [slot]

    Use this to set the slot of the object to one of the equipment slots.
    """

    key = "@slot"

    def func(self):
        if not self.caller.locks.check_lockstring(self.caller, "dummy:perm(Builder)"):
            self.caller.msg("You must be a Builder or higher to do this!")
            return

        if self.lhs == '':
            self.caller.msg("You must choose an object.")

        if self.rhs == '':
            self.caller.msg("You must choose a slot.")

        target = self.caller.search(self.lhs)

        if target is None:
            self.caller.msg("Cannot find %s" % self.lhs)
            return

        if self.rhs not in slots:
            self.caller.msg("Invalid slot %s" % self.rhs)
            return

        self.caller.msg("Slot set.")
        target.db.slot = self.rhs

class CmdEquip(MuxCommand):
    """
    Equip an item.

    Usage:
        equip [item]

    Use this to equip an item to an appropriate slot.
    """

    key = "equip"

    def func(self):
        if self.lhs == '':
            self.caller.msg("You must choose an item!")
            return

        target_item = self.caller.search(self.lhs)
        if target_item is None:
            self.caller.msg("You do not see a %s" % self.lhs)

        self.caller.location.msg_contents("%s equips a %s" %
            (self.caller, target_item))
        self.caller.db.equipment.equip(target_item, self.caller)

class CmdUnequip(MuxCommand):
    """
    Unequips an item from a specific slot.

    Usage:
        unequip [slot]

    This removes the object from the slot and puts it into your inventory.
    """

    key = "unequip"

    def func(self):
        if self.lhs == '':
            self.caller.msg("You must choose a slot.")
            return

        if self.lhs not in slots:
            self.caller.msg("That is not a valid slot!")
            return

        item = self.caller.equipment.slots[self.lhs]
        self.caller.location.msg_contents("%s unequips %s" % (self.caller, item))
        self.caller.db.equipment.unequip(self.lhs, self)
