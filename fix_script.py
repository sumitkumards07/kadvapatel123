import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Hero Section image safely
content = re.sub(
    r'(<img\s+class="[^"]*object-cover[^"]*")([^>]*src="https://lh3.googleusercontent.com/aida-public/[^"]*")([^>]*>)',
    r'\1 src="images/hero.jpg" alt="Kadva Patel Samaj Hero Image" \3',
    content, count=1
)

# Read the HTML from new_sections.py but without re-defining it, just rewrite the python code
with open('new_sections.py', 'r') as f:
    code = f.read()

# Extract just the HTML strings
rooms_html = re.search(r'rooms_html = """(.*?)"""', code, re.DOTALL).group(1)
modal_html = re.search(r'modal_html = """(.*?)"""', code, re.DOTALL).group(1)

# Safely replace the rooms section
pattern = re.compile(r'<section[^>]*id="rooms"[^>]*>.*?</section>', re.DOTALL)
content = pattern.sub(rooms_html, content)

# Inject the modal and script right before </body>
content = content.replace('</body>', modal_html + '\n</body>')

# Update Nav Links
content = content.replace('href="#rooms">Rooms</a>', 'href="#rooms">Rooms</a>\n<a class="text-on-surface-variant font-label-md text-label-md hover:text-secondary transition-colors duration-300" href="#about">About</a>\n<a class="text-on-surface-variant font-label-md text-label-md hover:text-secondary transition-colors duration-300" href="#location">Location</a>\n<a class="text-on-surface-variant font-label-md text-label-md hover:text-secondary transition-colors duration-300" href="#reviews">Reviews</a>')

with open('index.html', 'w') as f:
    f.write(content)

