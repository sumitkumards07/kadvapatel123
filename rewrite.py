import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Hero Section image
content = re.sub(
    r'<img\s+class="([^"]*object-cover[^"]*)"[^>]*src="https://lh3.googleusercontent.com/aida-public/[^"]*"[^>]*>',
    r'<img class="\1" src="images/hero.jpg" alt="Kadva Patel Samaj Hero Image"/>',
    content, count=1
)

with open('index.html', 'w') as f:
    f.write(content)
