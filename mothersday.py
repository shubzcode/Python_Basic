import pyfiglet
import random

# Define list of available fonts
fonts = ["standard", "banner3", "digital", "slant", "smscript"]

# Define List of available colors
colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]

# Select random font and color
selected_font = random.choice(fonts)
selected_color = random.choice(colors)

# Generate the Mother's Day message
message = pyfiglet.figlet_format("Happy Mother's Day!", font=selected_font)

# Print the message in the selected color
print(f"\033[1; {colors.index(selected_color) + 31}m{message}\033[0m")