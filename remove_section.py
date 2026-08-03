import sys

with open('index.html', 'r') as f:
    lines = f.readlines()

# Remove lines 345 to 388 (0-indexed 344 to 388)
# Let's verify the lines to be safe
start_line = 345
end_line = 388

new_lines = lines[:start_line-1] + lines[end_line:]

with open('index.html', 'w') as f:
    f.writelines(new_lines)
