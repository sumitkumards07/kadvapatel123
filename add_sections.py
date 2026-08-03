import sys

new_sections_html = """
<!-- Features Section -->
<section class="py-section-gap px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto" id="features">
    <div class="text-center mb-16">
        <h3 class="font-headline-md text-headline-md text-primary mb-4">Our Features</h3>
        <div class="h-1 w-24 bg-secondary mx-auto rounded-full"></div>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
        <div class="text-center p-6 bg-white rounded-2xl luxury-shadow hover:-translate-y-1 transition-all">
            <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">wifi</span>
            <h5 class="font-bold text-primary mb-2">Free Wi-Fi</h5>
            <p class="text-sm text-on-surface-variant">High-speed internet in all areas</p>
        </div>
        <div class="text-center p-6 bg-white rounded-2xl luxury-shadow hover:-translate-y-1 transition-all">
            <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">local_parking</span>
            <h5 class="font-bold text-primary mb-2">Parking</h5>
            <p class="text-sm text-on-surface-variant">Secure parking space available</p>
        </div>
        <div class="text-center p-6 bg-white rounded-2xl luxury-shadow hover:-translate-y-1 transition-all">
            <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">restaurant</span>
            <h5 class="font-bold text-primary mb-2">Dining</h5>
            <p class="text-sm text-on-surface-variant">Pure veg dining facility</p>
        </div>
        <div class="text-center p-6 bg-white rounded-2xl luxury-shadow hover:-translate-y-1 transition-all">
            <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">ac_unit</span>
            <h5 class="font-bold text-primary mb-2">A/C Rooms</h5>
            <p class="text-sm text-on-surface-variant">Comfortable air-conditioned rooms</p>
        </div>
    </div>
</section>

<!-- Nearby Places Section -->
<section class="py-section-gap bg-primary/5 px-margin-mobile md:px-margin-desktop" id="nearby-places">
    <div class="max-w-container-max mx-auto">
        <div class="text-center mb-16">
            <h3 class="font-headline-md text-headline-md text-primary mb-4">Nearby Attractions</h3>
            <div class="h-1 w-24 bg-secondary mx-auto rounded-full"></div>
            <p class="text-on-surface-variant mt-4 max-w-2xl mx-auto">Explore the holy city of Dwarka. Our central location makes it easy to visit these sacred and historic places.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="bg-white rounded-2xl overflow-hidden luxury-shadow group">
                <div class="h-48 bg-primary/20 relative overflow-hidden">
                    <div class="absolute inset-0 flex items-center justify-center bg-primary/10 group-hover:bg-primary/20 transition-all">
                        <span class="material-symbols-outlined text-6xl text-primary/30">temple_hindu</span>
                    </div>
                </div>
                <div class="p-6 relative">
                    <div class="absolute -top-6 right-6 w-12 h-12 bg-secondary text-white rounded-full flex items-center justify-center luxury-shadow">
                        <span class="material-symbols-outlined">map</span>
                    </div>
                    <h4 class="font-bold text-lg text-primary mb-2">Dwarkadhish Temple</h4>
                    <p class="text-sm text-on-surface-variant mb-4">The main temple of Lord Krishna, a short drive from our location.</p>
                    <span class="inline-block bg-primary/10 text-primary text-xs px-3 py-1 rounded-full font-bold">2.5 km away</span>
                </div>
            </div>
            
            <div class="bg-white rounded-2xl overflow-hidden luxury-shadow group">
                <div class="h-48 bg-primary/20 relative overflow-hidden">
                    <div class="absolute inset-0 flex items-center justify-center bg-primary/10 group-hover:bg-primary/20 transition-all">
                        <span class="material-symbols-outlined text-6xl text-primary/30">water</span>
                    </div>
                </div>
                <div class="p-6 relative">
                    <div class="absolute -top-6 right-6 w-12 h-12 bg-secondary text-white rounded-full flex items-center justify-center luxury-shadow">
                        <span class="material-symbols-outlined">map</span>
                    </div>
                    <h4 class="font-bold text-lg text-primary mb-2">Gomti Ghat</h4>
                    <p class="text-sm text-on-surface-variant mb-4">Sacred bathing ghats situated on the banks of the Gomti river.</p>
                    <span class="inline-block bg-primary/10 text-primary text-xs px-3 py-1 rounded-full font-bold">2.8 km away</span>
                </div>
            </div>

            <div class="bg-white rounded-2xl overflow-hidden luxury-shadow group">
                <div class="h-48 bg-primary/20 relative overflow-hidden">
                    <div class="absolute inset-0 flex items-center justify-center bg-primary/10 group-hover:bg-primary/20 transition-all">
                        <span class="material-symbols-outlined text-6xl text-primary/30">landscape</span>
                    </div>
                </div>
                <div class="p-6 relative">
                    <div class="absolute -top-6 right-6 w-12 h-12 bg-secondary text-white rounded-full flex items-center justify-center luxury-shadow">
                        <span class="material-symbols-outlined">map</span>
                    </div>
                    <h4 class="font-bold text-lg text-primary mb-2">Rukmini Devi Temple</h4>
                    <p class="text-sm text-on-surface-variant mb-4">An architectural masterpiece dedicated to Lord Krishna's chief queen.</p>
                    <span class="inline-block bg-primary/10 text-primary text-xs px-3 py-1 rounded-full font-bold">4.0 km away</span>
                </div>
            </div>
        </div>
    </div>
</section>

"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<!-- Map Section -->'

if target in content:
    content = content.replace(target, new_sections_html + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("New sections added successfully.")
else:
    print("Map section not found.")
