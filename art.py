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

import csv

# Initializing our glyph dot dictionary
braille_values = {}
dot_braille_values = {}

# Reading our glyph_storage file and storing it as a dictionary
with open('glyph_storage.csv', newline='', encoding='utf-8') as csvfile:
   reader = csv.reader(csvfile)

   # For each column,
   for column in reader:
      # Unpack values from the two columns
      numbers, glyph = column
      # Store glyph as key and dots as value
      braille_values[glyph] = numbers
      # Opposite for dot_braille_values
      dot_braille_values[numbers] = glyph


def unglyph(glyph_string):
    number_list = []

    for glyph in glyph_string:
         # In case of it being a new line
         if glyph == '\n':
            number_list.append('\n')
         # Otherwise just match and append
         else:
            numbers = braille_values.get(glyph, 'undefined')
            if numbers == 'undefined':
               print(f"Glyph '{glyph}' caused an undefined value.")
            number_list.append(numbers)
         
    return number_list

def print_braille(number_list):
   printable = ""

   for number in number_list:
      if number == '\n':
         printable += '\n'
      else:
         glyph = dot_braille_values.get(number, '')
         printable += str(glyph)

   return printable
    
unglyphed_art = unglyph(input_art)
glyphed_art = print_braille(unglyphed_art)
print(glyphed_art)
print("braille_values:", braille_values)
print("dot_braille_values:", dot_braille_values)
print("unglyphed_art:", unglyphed_art)
print("glyphed_art:", glyphed_art)