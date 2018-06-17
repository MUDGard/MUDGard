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

        if self.lhs is '':
            self.caller.msg("You must choose an object.")

        if self.rhs is '':
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
