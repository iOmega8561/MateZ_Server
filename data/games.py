""" This module contains the hardcoded Games array """

from dataclasses import dataclass, field

DEFAULT_PLATFORMS = ["XBOX", "PlayStation", "PC", "Android", "iOS", "Switch"]
DEFAULT_MODES = ["ranked", "unranked", "sandbox"]
DEFAULT_SKILLSET = []

@dataclass
class Game:
    """ Data class for the Game object """
    name: str
    imgname: str
    plat: [str] = field(default_factory=lambda: DEFAULT_PLATFORMS)
    modes: [str] = field(default_factory=lambda: DEFAULT_MODES)
    skills: [str] = field(default_factory=lambda: DEFAULT_SKILLSET)

    def repr_json(self):
        """ This method gets called to get the dict rapresentation of the object """

        return dict(
            name = self.name,
            imgname = self.imgname,
            plat = self.plat,
            modes = self.modes,
            skills = self.skills,
        )

GAMES = {
    "League of Legends": Game(
        "League of Legends",
        "lol",
        ["PC"],
        ["Draft pick", "Blind pick", "Ranked Solo/Duo", "Ranked Flex", "Tournament", "Custom"],
        ["Ranged", "Bruiser", "Tank", "Mage", "Assassin", "Flex"]
    ),

    "Counter Strike: GO": Game(
        "Counter Strike: GO",
        "csgo",
        ["PC", "XBOX"],
        ["Casual", "Competitive", "Wingman", "Deathmatch", "Custom", "War Games", "Danger Zone"],
        ["Leader", "Support", "Lurk", "AWPer", "Fluid Roles"]
    ),

    "Rainbow Six Siege": Game(
        "Rainbow Six Siege",
        "r6s",
        ["PC", "PlayStation", "XBOX"],
        ["Unranked", "Ranked", "Tournament", "Custom"],
        ["Leader", "Fragger", "Support", "Flex", "Anchor", "Roamer", "Fluid Roles"]
    ),
}
