input_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⢶⢒⣚⣛⡛⠓⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣛⣲⠶⠤⣤⡤⠖⠋⠉⣀⡤⠖⠋⠉⠉⠉⠉⠙⠶⡀⠙⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⢽⡆⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣹⣿⣿⣿⣟⡾⠁⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠂⠙⠦⠼⠛⠋⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⢿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡟⠀⠀⢠⣄⡀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤⣀⣀⣀⠀⠀⠀⣀⣀⣠⠶⠛⠁⠀⡟⠀⠀⠀⠀⠀
⠀⠀⠀⣰⠿⠀⠀⣰⣾⠇⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⣼⢁⣤⣦⡀⠀⠀
⠀⠀⣰⠃⠀⠀⠐⠿⢿⣄⣀⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠶⠒⠒⠒⠲⠤⣄⣸⡿⠋⢛⣿⣷⠀⠀
⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠈⠙⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠴⠚⠉⠁⠀⠀
⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀
⣇⠀⠀⠀⠀⠀⠋⠉⠉⠉⠓⠦⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀
⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀
⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠋⠉
⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠧⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣋⣀⣀⡤
⠀⠀⠀⠀⠀⠀⠙⠒⠦⣄⣀⡀⠀⠀⠀⠀⢠⣿⡛⠒⠲⠦⠤⠤⠤⠤⠤⠶⠒⠒⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


"""
This is pretty much a braille conversion program?
Is it excessive...maybe
Anyways, here we are
"""
import csv

# Initializing our glyph dot dictionary
braille_values = {}

# Reading our glyph_storage file and storing it as a dictionary
with open('glyph_storage.csv', newline='', encoding='utf-8') as csvfile:
   reader = csv.reader(csvfile)

   # For each column,
   for column in reader:
      # Unpack values from the two columns
      numbers, glyph = column
      # Store glyph as key and dots as value
      braille_values[glyph] = numbers


def unglyph(glyph_string):
    number_list = []

    for glyph in glyph_string:
        numbers = braille_values.get(glyph, 'other')
        number_list.append(numbers)

    return number_list

new_dot = unglyph(input_art)
