class Randoms:
    adjectives = [
        "glitchy", "cozy", "chaotic", "minimal", "shiny",
        "sneaky", "sleepy", "hyper", "ancient", "digital",
        "rusty", "floating", "noisy", "invisible", "random",
        "squishy", "broken", "smooth", "spooky", "experimental"
    ]
    objects = [
        "button", "clock", "backpack", "key", "mirror",
        "door", "cube", "notebook", "remote", "coin",
        "robot", "lantern", "switch", "window", "card",
        "box", "map", "speaker", "battery", "lever"
    ]
    program_ideas = [
        "random name generator",
        "to-do list app",
        "clicker game",
        "digital pet",
        "password strength checker",
        "music loop player",
        "drawing app",
        "trivia game",
        "text adventure game",
        "mood-based timer",
        "maze generator",
        "notes app with tags",
        "typing speed test",
        "daily challenge generator",
        "calendar with reminders",
        "soundboard",
        "quiz maker",
        "simple chatbot",
        "pixel art editor",
        "story prompt generator"
    ]
    def project(self):
        import random
        print("Need inspiration? Here's a random project:")
        print(random.choice(self.adjectives), random.choice(self.objects), random.choice(self.program_ideas))


if __name__ == "__main__":
    randoms = Randoms()
    randoms.project()
