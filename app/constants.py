import random

run = True
FPS = 1/60

# PLAYERSCREEN_HEIGHT = 99
# PLAYERSCREEN_WIDTH = 99
WORLD_HEIGHT = 100
WORLD_WIDTH = 80

world_seed = random.randint(0, 9999999)

terrain_probability_dict: {float | int, str} = {-1: "e", 0.2 : "o", 0.5 : "M", 1 : "#"}

scale = 100.0  # Change this value to zoom in/out (lower values = more detail, higher = smoother)
octaves = 6  # Number of levels of detail
persistence = 0.5  # How much detail persists between octaves (values between 0 and 1)
lacunarity = 2.0  # Frequency of new details at each octave


print(101)