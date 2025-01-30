import csv

# Initializing our glyph dot dictionary
braille_values = {}

# Reading our glyph_storage file and storing it as a dictionary
with open('glyph_storage.csv', newline='', encoding='utf-8') as csvfile:
   reader = csv.reader(csvfile)

   # For each column,
   for column in reader:
      # Unpack values from the two columns
      letters, glyph = column
      # Assign letter as key and glyph as value
      braille_values[letters] = glyph

print(braille_values)