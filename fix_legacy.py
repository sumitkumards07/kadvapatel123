import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove the Gallery section which is lines 251 to 326 (this corresponds to "A Legacy of Quality")
# Let's use a regex to remove the <section ... id="gallery">...</section>
content = re.sub(
    r'<section[^>]*id="gallery"[^>]*>.*?</section>',
    '',
    content,
    flags=re.DOTALL
)

# Remove the "Our Legacy Timeline" section which is inside the "About Us" section or another area.
# Wait, let's just find the section tag containing "Our Legacy Timeline".
# In index.html, "Our Legacy Timeline" was at line 383, which is likely in a section id="legacy" or similar.
content = re.sub(
    r'<section[^>]*id="history"[^>]*>.*?</section>',
    '',
    content,
    flags=re.DOTALL
)

with open('index.html', 'w') as f:
    f.write(content)
