class Project:
    def __init__(self, name, description, github_url, technologies, website=None, icon=None, challenges=""):
        self.name = name
        self.description = description
        self.github_url = github_url
        self.technologies = technologies
        self.website = website
        self.icon = icon
        self.challenges = challenges
        

PROJECTS = [
    Project(
        name = "Glyph",
        description = "The very device you are holding right now! A custom NFC Card but with an E-ink Display, built with a Seeed Studio XIAO nRF52840 and the Seeed Studio E-ink Display. The device is built to be a business card, but with a lot of customizations and features",
        github_url = "https://github.com/ItsAkshatSh/Glyph",
        technologies = ["Circuit Python","Python","E-ink Display"],
        challenges = "The biggest challenge for me was to get the footprints for the E-ink Display breakout board, but after bunch of research, I got it right!",
        icon = "glyph.bmp"
    ),
    Project(
        name = "Neko",
        description = "An Apple inspired Dynamic Island app but for cat owners! While also helping cat owners keep track of their cat's activities, health and documents. Built for HackTheKitty 2026",
        github_url = "https://github.com/ItsAkshatSh/Neko",
        technologies = ["Flutter","Firebase","Dart","Riverpod","Lottie"],
        challenges = "Since this was for a hackathon, we had to build the app in 2 weeks. So me and my teammate had to work on the app after school leading to late nights, but overall we are proud of what we built!",
        icon = "neko.bmp"
    ),
    Project(
        name = "The Deck!",
        description = "My take on the streamdeck, but with a 2.8' inch touchscreen, running on a Seeed Studio XIAO RP2040 and Three Cherry MX switches",
        github_url = "https://github.com/ItsAkshatSh/thedeck",
        technologies = ["Circuit Python","Python","WinDSK"],
        challenges = "Building a functional music bridge between the MCU and the PC was a challenge, but after a lot of trial and error, it worked!",
        icon = "the_deck.bmp"
    ),
    Project(
        name = "Bat Hunt",
        description = "A 2D game built in Godot, inspired by the classic game 'Duck Hunt', the player is supposed to flying bats with a shotgun and the game is built for the Ember Game Jam 2026",
        github_url = "https://github.com/ItsAkshatSh/BatHunt",
        technologies = ["Godot","GDScript"],
        challenges = "The biggest challenge was to make the bats fly in a realistic but challenging way, but after multiple versions, I found the best way to make the bats fly around",
        icon = "bat_hunt.bmp"
    )
    
]
