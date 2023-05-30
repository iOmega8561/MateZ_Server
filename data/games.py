""" This module contains the hardcoded Games array """

from dataclasses import dataclass, field

DEFAULT_PLATFORMS = ["XBOX", "PlayStation", "PC", "Android", "iOS", "Switch"]
DEFAULT_MODES = []
DEFAULT_SKILLSET = []

@dataclass
class Game:
    """ Data class for the Game object """
    name: str
    imgname: str
    plat: [str] = field(default_factory = lambda: DEFAULT_PLATFORMS)
    modes: [str] = field(default_factory = lambda: DEFAULT_MODES)
    skills: [str] = field(default_factory = lambda: DEFAULT_SKILLSET)

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
        ["Bottom", "Top", "Middle", "Jungle", "Support"]
    ),

    "Counter Strike: GO": Game(
        "Counter Strike: GO",
        "csgo",
        ["PC", "XBOX"],
        ["Casual", "Competitive", "Wingman", "Deathmatch", "Custom", "War Games", "Danger Zone"],
        ["Leader", "Support", "Lurk", "AWPer"]
    ),

    "Rainbow Six Siege": Game(
        "Rainbow Six Siege",
        "r6s",
        ["PC", "PlayStation", "XBOX"],
        ["Unranked", "Ranked", "Tournament", "Custom"],
        ["Leader", "Fragger", "Support", "Flex", "Anchor", "Roamer"]
    ),

    "Fortnite": Game(
        "Fortnite",
        "fortnite",
        ["PC", "PlayStation", "XBOX", "Switch"],
        ["Save the World", "Battle Royale", "BR No builds"],
        []
    ),

    "War Thunder": Game(
        "War Thunder",
        "warthunder",
        ["PC", "PlayStation", "XBOX"],
        ["Arcade Battles", "Realistic Battles", "Simulator Battles", "Enduring Confrontation", "Event", "World War Mode"],
        []
    ),

    "Dota 2": Game(
        "Dota 2",
        "dota2",
        ["PC"],
        ["All Pick", "Turbo Mode", "Ranked All Pick", "Single Draft", "Random Draft", "All Random", "Captains Mode", "Captains Draft", "Least Played", "1v1 Solo Mid", "All Random Deathmatch", "Ability Draft", "Custom game", "Event"],
        ["Carry", "Midlaner", "Offlaner", "Roamer", "Hard Support"]
    ),

    "Fifa 23": Game(
        "Fifa 23",
        "fifa23",
        ["PC", "PlayStation", "XBOX", "Switch"],
        ["Tournament", "Frendlies", "Seasons", "Pro Club", "Ultimate Team"],
        []
    ),

    "COD: Warzone 2": Game(
        "COD: Warzone 2",
        "warzone",
        ["PC", "PlayStation", "XBOX"],
        ["Battle Royale", "Massive Resurgence", "Resurgence", "DMZ"],
        ["Airstriker", "Arms Dealer", "Eagle Eyes", "Fighter", "Gunner", "High-Roller", "Hustler", "Marauder", "Protector", "Reviver", "Savior", "Sharpshooter", "Sidekick", "Slayer", "Survivor", "Tank"]
    ),

    "Grand Theft Auto V": Game(
        "Grand Theft Auto V",
        "gtav",
        ["PC", "PlayStation", "XBOX"],
        ["Freemode", "Deathmatch", "Race", "Contend", "Hold", "Last Team Standing", "Raid", "Event Activities", "Any Activity"],
        []
    ),

    "World of Warcraft": Game(
        "World of Warcraft",
        "wow",
        ["PC"],
        ["Outdoor questing/leveling", "Mythic+", "Dragonflight Raiding", "Classic Raiding", "Dragonflight PvP", "Classic PvP", "Wrath Classic Dungeons", "Classic Era2", "Classic hardcore", "Other"],
        ["Tank", "Healer", "Damage dealer", "Support"]
    ),

    "Rust": Game(
        "Rust",
        "rust",
        ["PC"],
        ["Survival", "Softcore", "Hardcore"],
        []
    ),

    "Minecraft": Game(
        "Minecraft",
        "minecraft",
        ["PC", "PlayStation", "XBOX", "Switch", "Android", "iOS"],
        ["Vanilla Survival", "Vanilla Creative", "Modded Survival", "Modded Creative", "Adventure map", "Bedwars", "Block hunt", "Eggwars", "TNT tag", "Murder mystery", "Survival games", "Draw thing", "Build battle", "Any Mode"],
        []
    ),

    "Rocket League": Game(
        "Rocker League",
        "rleague",
        ["PC", "PlayStation", "XBOX", "Switch"],
        ["Casual", "Competitive", "Extra modes", "Custom game"]
    ),

    "Apex Legends": Game(
        "Apex Legends",
        "apex",
        ["PC", "PlayStation", "XBOX", "Switch", "Android", "iOS"],
        ["Battle Royale", "Ranked Leagues", "Mixtape", "Any Mode"],
        ["Assault", "Recon", "Support", "Skirmisher", "Controller"]
    ),

    "Valorant": Game(
        "Valorant",
        "valorant",
        ["PC"],
        ["Unrated", "Ranked", "Spike Rush", "Deathmatch", "Replication", "Escalation", "Custom Game"],
        ["Sentinel", "Duelist", "Controller", "Initiator"]
    ),

    "ARK: Survival Evolved": Game(
        "ARK: Survival Evolved",
        "arkse",
        ["PC", "PlayStation", "XBOX", "Switch", "Android", "iOS"],
        ["Official PVP", "Official PVE", "Small tribe PVP", "Unofficial PVP", "Unofficial PVE", "Non Dedicated Session"],
        []
    ),

    "Dead by Daylight": Game(
        "Dead by Daylight",
        "dbd",
        ["PC", "PlayStation", "XBOX", "Switch", "Android", "iOS"],
        ["Survivor", "Custom Game"]
    ),

    "Team Fortress 2": Game(
        "Team Fortress 2",
        "tf2",
        ["PC", "PlayStation", "XBOX"],
        ["Arena", "Capture The Flag", "Competitive", "Control Point", "Payload", "Arena", "King of the Hill", "Payload Race", "Medieval Mode", "Special Delivery", "Mann vs. Machine", "Robot Destruction", "Mannpower", "PASS Time", "Player Destruction"],
        ["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy"]
    )
}
