"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from typeclasses.equipment_handler import EquipmentHandler

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_object_creation(self):
        self.db.equipment = EquipmentHandler()
        self.db.silver_pieces = 0
        self.db.level = 1
        self.db.exp = 0
        self.db.class_stats = {}
        self.db.class_ = "None yet"

    def new_class(self, class_name):
        self.db.class_ = class_name
        self.db.class_stats[class_name] = [5, 5, 5]

    def current_stats(self):
        return self.db.class_stats[self.class_]

    def remaining_points(self):
            if sum(self.db.class_stats[self.db.class_]) < 45:
                return 45 - self.db.class_stats[self.db.class_]
            else:
                if type(self.current_stats()) == list:
                    self.db.class_stats[self.class_] = tuple(self.current_stats())
                return 0
