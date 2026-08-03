import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace background image URL
content = re.sub(
    r"background-image: url\('https://lh3.googleusercontent.com/aida-public/[^']*'\)",
    "background-image: url('images/hero.jpg')",
    content
)

with open('index.html', 'w') as f:
    f.write(content)
