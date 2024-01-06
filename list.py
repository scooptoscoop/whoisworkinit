import os
import glob

# Get a list of all files in the 'imgs' directory
files = glob.glob('imgs/*')

# Sort the list in ascending order
files.sort()

# Format the sorted list as a JavaScript array
js_array = "var imgs = ['" + "','".join(files) + "'];"

# Print the JavaScript array
print(js_array)