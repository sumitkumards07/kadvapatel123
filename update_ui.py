import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Make the logo bigger on mobile
content = content.replace('alt="Kadva Patel Samaj Logo" class="h-10 w-auto"', 'alt="Kadva Patel Samaj Logo" class="h-16 md:h-10 w-auto"')

# 2. Remove View Gallery and change to Contact Us
content = content.replace('href="#gallery">View Gallery</a>', 'href="#contact">Contact Us</a>')

# Also update the nav link "Gallery" to "Contact" if it points to #gallery
content = content.replace('href="#gallery">Gallery</a>', 'href="#contact">Contact</a>')

# 3. Add more sections (About Us, Why Choose Us)
# We will insert them right before the "Our Location" map section
about_us_html = """
<!-- About Us Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto" id="about">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <div>
            <h3 class="font-headline-md text-headline-md text-primary mb-6">About Kadva Patel Samaj</h3>
            <p class="text-on-surface-variant font-body-lg mb-4">Established with a vision to provide a comfortable and welcoming home away from home, Kadva Patel Samaj in Dwarka has been serving community members and pilgrims with dedication for decades.</p>
            <p class="text-on-surface-variant font-body-md mb-6">Our facility is designed to offer a peaceful environment for families, groups, and individuals visiting the holy city. We pride ourselves on maintaining clean, well-equipped accommodations while preserving our rich cultural heritage.</p>
            <div class="flex gap-4">
                <div class="p-4 bg-primary/5 rounded-xl border border-primary/10">
                    <span class="material-symbols-outlined text-secondary text-3xl mb-2 block">history_edu</span>
                    <h5 class="font-bold text-primary">Rich Heritage</h5>
                    <p class="text-sm text-on-surface-variant">Decades of community service</p>
                </div>
                <div class="p-4 bg-primary/5 rounded-xl border border-primary/10">
                    <span class="material-symbols-outlined text-secondary text-3xl mb-2 block">family_home</span>
                    <h5 class="font-bold text-primary">Family Friendly</h5>
                    <p class="text-sm text-on-surface-variant">Safe & secure environment</p>
                </div>
            </div>
        </div>
        <div class="relative">
            <div class="absolute -top-6 -left-6 w-32 h-32 bg-secondary/10 rounded-full blur-2xl -z-10"></div>
            <div class="absolute -bottom-6 -right-6 w-40 h-40 bg-primary/10 rounded-full blur-3xl -z-10"></div>
            <img class="rounded-2xl luxury-shadow w-full aspect-video object-cover" src="images/hero.jpg" alt="About Kadva Patel Samaj" />
        </div>
    </div>
</section>

<!-- Why Choose Us Section -->
<section class="py-section-gap bg-primary/5 px-margin-mobile md:px-margin-desktop" id="why-choose-us">
    <div class="max-w-container-max mx-auto">
        <div class="text-center mb-16">
            <h3 class="font-headline-md text-headline-md text-primary mb-4">Why Choose Us</h3>
            <div class="h-1 w-24 bg-secondary mx-auto rounded-full"></div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-2xl luxury-shadow hover:-translate-y-2 transition-transform duration-300">
                <div class="w-14 h-14 bg-secondary/10 rounded-xl flex items-center justify-center mb-6 text-secondary">
                    <span class="material-symbols-outlined text-3xl">location_on</span>
                </div>
                <h4 class="font-headline-sm text-headline-sm text-primary mb-3">Prime Location</h4>
                <p class="text-on-surface-variant font-body-md">Strategically located close to major temples and transit points, making your pilgrimage convenient and hassle-free.</p>
            </div>
            <div class="bg-white p-8 rounded-2xl luxury-shadow hover:-translate-y-2 transition-transform duration-300">
                <div class="w-14 h-14 bg-secondary/10 rounded-xl flex items-center justify-center mb-6 text-secondary">
                    <span class="material-symbols-outlined text-3xl">cleaning_services</span>
                </div>
                <h4 class="font-headline-sm text-headline-sm text-primary mb-3">Hygienic & Clean</h4>
                <p class="text-on-surface-variant font-body-md">We maintain the highest standards of cleanliness in all our rooms, common areas, and dining facilities.</p>
            </div>
            <div class="bg-white p-8 rounded-2xl luxury-shadow hover:-translate-y-2 transition-transform duration-300">
                <div class="w-14 h-14 bg-secondary/10 rounded-xl flex items-center justify-center mb-6 text-secondary">
                    <span class="material-symbols-outlined text-3xl">volunteer_activism</span>
                </div>
                <h4 class="font-headline-sm text-headline-sm text-primary mb-3">Community First</h4>
                <p class="text-on-surface-variant font-body-md">Operated with a service-oriented mindset, focusing on guest comfort and satisfaction above all else.</p>
            </div>
        </div>
    </div>
</section>

"""

map_section_target = '<!-- Map Section -->'

if map_section_target in content:
    content = content.replace(map_section_target, about_us_html + map_section_target)
else:
    print("Map section not found, couldn't insert new sections.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("UI updated successfully.")
