import pygame
import os


class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}

    def load_image(self, key, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image file not found: {path}")
        image = pygame.image.load(path).convert_alpha()
        self.images[key] = image
        # expose by key and by suffix (after first underscore) for convenience
        try:
            setattr(self, key, image)
        except Exception:
            pass
        if "_" in key:
            try:
                setattr(self, key.split("_", 1)[1], image)
            except Exception:
                pass

    def load_sound(self, key, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Sound file not found: {path}")
        sound = pygame.mixer.Sound(path)
        self.sounds[key] = sound
        try:
            setattr(self, key, sound)
        except Exception:
            pass
        if "_" in key:
            try:
                setattr(self, key.split("_", 1)[1], sound)
            except Exception:
                pass

    def get_image(self, key):
        return self.images.get(key)

    def get_sound(self, key):
        return self.sounds.get(key)

    def __getattr__(self, name):
        # allow attribute-style access for loaded assets
        if name in self.images:
            return self.images[name]
        if name in self.sounds:
            return self.sounds[name]

        # try matching suffixes like 'dr_ccar' -> 'ccar'
        for k, v in self.images.items():
            if k.endswith("_" + name):
                return v
            parts = k.split("_", 1)
            if len(parts) > 1 and parts[1] == name:
                return v

        for k, v in self.sounds.items():
            if k.endswith("_" + name):
                return v
            parts = k.split("_", 1)
            if len(parts) > 1 and parts[1] == name:
                return v

        raise AttributeError(f"'AssetManager' object has no attribute '{name}'")
