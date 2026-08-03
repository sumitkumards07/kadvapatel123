import re

with open('index.html', 'r') as f:
    content = f.read()

# Generate new rooms HTML
rooms_html = """
<section class="py-section-gap px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto" id="rooms">
<div class="text-center mb-16">
<h3 class="font-headline-md text-headline-md text-primary mb-4">Our Rooms & Categories</h3>
<div class="h-1 w-24 bg-secondary mx-auto rounded-full"></div>
<p class="text-on-surface-variant font-body-md text-body-md mt-6">Choose the perfect room for your stay.</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">
<!-- AC Room 2 Bed -->
<div class="group luxury-shadow bg-surface-container-lowest rounded-xl overflow-hidden transition-transform duration-500 hover:-translate-y-2 flex flex-col">
<div class="h-64 overflow-hidden relative">
<img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" src="images/S.jpg" alt="AC Room 2 Bed"/>
</div>
<div class="p-6 flex flex-col flex-grow">
<div class="flex justify-between items-start mb-4">
<div><h4 class="font-headline-sm text-headline-sm text-primary mb-1">AC Room 2 Bed</h4></div>
<div class="text-right">
<p class="text-secondary font-bold text-headline-sm">₹1,650</p>
<p class="text-label-sm font-label-sm text-on-surface-variant">/ night</p>
</div>
</div>
<div class="flex flex-wrap gap-2 mb-6">
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">bed</span> 2 Beds</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">ac_unit</span> AC</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">wifi</span> WiFi</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">tv</span> TV</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">water_drop</span> Hot Water</span>
</div>
<button onclick="openBookingModal('AC Room 2 Bed', '₹1,650')" class="mt-auto w-full py-4 bg-primary text-on-primary rounded-lg font-label-md text-label-md hover:bg-secondary transition-all active:scale-[0.98]">Book Now</button>
</div>
</div>

<!-- Best Room -->
<div class="group luxury-shadow bg-surface-container-lowest rounded-xl overflow-hidden transition-transform duration-500 hover:-translate-y-2 flex flex-col border-2 border-secondary relative">
<div class="absolute top-4 right-4 z-10 bg-secondary text-white px-3 py-1 rounded-full text-label-sm font-bold shadow-md">TOP CHOICE</div>
<div class="h-64 overflow-hidden relative">
<img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" src="images/s1.jpg" alt="Best Room"/>
</div>
<div class="p-6 flex flex-col flex-grow">
<div class="flex justify-between items-start mb-4">
<div><h4 class="font-headline-sm text-headline-sm text-primary mb-1">Best Room</h4></div>
<div class="text-right">
<p class="text-secondary font-bold text-headline-sm">₹2,445</p>
<p class="text-label-sm font-label-sm text-on-surface-variant">/ night</p>
</div>
</div>
<div class="flex flex-wrap gap-2 mb-6">
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">bed</span> Comfort Bed</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">ac_unit</span> AC</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">wifi</span> WiFi</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">tv</span> TV</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">water_drop</span> Hot Water</span>
</div>
<button onclick="openBookingModal('Best Room', '₹2,445')" class="mt-auto w-full py-4 bg-secondary text-on-secondary rounded-lg font-label-md text-label-md hover:bg-secondary/90 transition-all active:scale-[0.98]">Book Now</button>
</div>
</div>

<!-- AC Room 4 Bed -->
<div class="group luxury-shadow bg-surface-container-lowest rounded-xl overflow-hidden transition-transform duration-500 hover:-translate-y-2 flex flex-col">
<div class="h-64 overflow-hidden relative">
<img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" src="images/d3.jpg" alt="AC Room 4 Bed"/>
</div>
<div class="p-6 flex flex-col flex-grow">
<div class="flex justify-between items-start mb-4">
<div><h4 class="font-headline-sm text-headline-sm text-primary mb-1">AC Room 4 Bed</h4></div>
<div class="text-right">
<p class="text-secondary font-bold text-headline-sm">₹2,500</p>
<p class="text-label-sm font-label-sm text-on-surface-variant">/ night</p>
</div>
</div>
<div class="flex flex-wrap gap-2 mb-6">
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">bed</span> 4 Beds</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">ac_unit</span> AC</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">wifi</span> WiFi</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">tv</span> TV</span>
<span class="bg-surface-container-high px-2 py-1 rounded text-primary text-label-sm flex items-center gap-1"><span class="material-symbols-outlined text-sm">water_drop</span> Hot Water</span>
</div>
<button onclick="openBookingModal('AC Room 4 Bed', '₹2,500')" class="mt-auto w-full py-4 bg-primary text-on-primary rounded-lg font-label-md text-label-md hover:bg-secondary transition-all active:scale-[0.98]">Book Now</button>
</div>
</div>
</div>
</section>

<!-- About Us & Why Choose Us Sections -->
<section class="py-section-gap bg-surface px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto" id="about">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div>
            <h3 class="font-headline-md text-headline-md text-primary mb-4">About Kadva Patel Samaj</h3>
            <div class="h-1 w-24 bg-secondary rounded-full mb-6"></div>
            <p class="text-on-surface-variant font-body-md mb-4 leading-relaxed">
                Kadva Patel Samaj is dedicated to providing a premium, culturally-rooted hospitality experience. We blend modern luxury with traditional values to offer an exceptional stay for all our guests.
            </p>
            <p class="text-on-surface-variant font-body-md leading-relaxed mb-6">
                Our facilities are designed to host families, business travelers, and community events with the utmost care, ensuring every moment spent with us is comfortable, secure, and memorable.
            </p>
            <a href="#rooms" class="inline-block py-3 px-8 bg-secondary text-white rounded-lg font-label-md hover:bg-secondary/90 transition-all">Explore Rooms</a>
        </div>
        <div class="grid grid-cols-2 gap-4">
            <div class="bg-surface-container-lowest p-6 rounded-xl luxury-shadow flex flex-col items-center text-center">
                <span class="material-symbols-outlined text-4xl text-secondary mb-3">verified</span>
                <h4 class="font-headline-sm text-lg text-primary mb-2">Premium Comfort</h4>
                <p class="text-on-surface-variant text-sm">Luxurious beds and top-tier amenities.</p>
            </div>
            <div class="bg-surface-container-lowest p-6 rounded-xl luxury-shadow flex flex-col items-center text-center">
                <span class="material-symbols-outlined text-4xl text-secondary mb-3">location_on</span>
                <h4 class="font-headline-sm text-lg text-primary mb-2">Prime Location</h4>
                <p class="text-on-surface-variant text-sm">Conveniently situated in the heart of the city.</p>
            </div>
            <div class="bg-surface-container-lowest p-6 rounded-xl luxury-shadow flex flex-col items-center text-center">
                <span class="material-symbols-outlined text-4xl text-secondary mb-3">security</span>
                <h4 class="font-headline-sm text-lg text-primary mb-2">Safe & Secure</h4>
                <p class="text-on-surface-variant text-sm">24/7 security and assistance.</p>
            </div>
            <div class="bg-surface-container-lowest p-6 rounded-xl luxury-shadow flex flex-col items-center text-center">
                <span class="material-symbols-outlined text-4xl text-secondary mb-3">restaurant</span>
                <h4 class="font-headline-sm text-lg text-primary mb-2">Great Food</h4>
                <p class="text-on-surface-variant text-sm">Delicious local cuisine available.</p>
            </div>
        </div>
    </div>
</section>

<!-- Reviews Section -->
<section class="py-section-gap bg-surface-container-low px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto" id="reviews">
    <div class="text-center mb-16">
        <h3 class="font-headline-md text-headline-md text-primary mb-4">Guest Reviews</h3>
        <div class="h-1 w-24 bg-secondary mx-auto rounded-full"></div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-surface-container-lowest p-8 rounded-xl luxury-shadow relative">
            <span class="material-symbols-outlined text-secondary opacity-20 absolute top-4 right-4 text-6xl">format_quote</span>
            <div class="flex text-secondary mb-4">
                <span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span>
            </div>
            <p class="text-on-surface-variant font-body-md mb-6 relative z-10">"Exceptional stay! The rooms were incredibly clean and the staff was so welcoming. A perfect blend of modern comfort and traditional hospitality."</p>
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold">R</div>
                <div><h5 class="font-bold text-primary text-sm">Rahul Patel</h5><p class="text-xs text-on-surface-variant">Business Traveler</p></div>
            </div>
        </div>
        <div class="bg-surface-container-lowest p-8 rounded-xl luxury-shadow relative">
            <span class="material-symbols-outlined text-secondary opacity-20 absolute top-4 right-4 text-6xl">format_quote</span>
            <div class="flex text-secondary mb-4">
                <span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span>
            </div>
            <p class="text-on-surface-variant font-body-md mb-6 relative z-10">"We booked the Best Room for our family trip and it exceeded expectations. The location is perfect and the amenities are top-notch."</p>
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold">A</div>
                <div><h5 class="font-bold text-primary text-sm">Amit Shah</h5><p class="text-xs text-on-surface-variant">Family Vacation</p></div>
            </div>
        </div>
        <div class="bg-surface-container-lowest p-8 rounded-xl luxury-shadow relative">
            <span class="material-symbols-outlined text-secondary opacity-20 absolute top-4 right-4 text-6xl">format_quote</span>
            <div class="flex text-secondary mb-4">
                <span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star</span><span class="material-symbols-outlined text-sm">star_half</span>
            </div>
            <p class="text-on-surface-variant font-body-md mb-6 relative z-10">"Great value for money. The AC 4 Bed room was spacious enough for our whole group. Very secure and peaceful environment."</p>
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold">N</div>
                <div><h5 class="font-bold text-primary text-sm">Neha Desai</h5><p class="text-xs text-on-surface-variant">Group Tour</p></div>
            </div>
        </div>
    </div>
</section>

<!-- Map Section -->
<section class="py-section-gap bg-surface px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto" id="location">
    <div class="text-center mb-16">
        <h3 class="font-headline-md text-headline-md text-primary mb-4">Our Location</h3>
        <div class="h-1 w-24 bg-secondary mx-auto rounded-full"></div>
    </div>
    <div class="rounded-xl overflow-hidden luxury-shadow h-96 w-full">
        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14766.195325852932!2d68.9669527!3d22.2950669!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39569ceeb0f2c417%3A0xc02e4d0d3885d518!2sKadva%20Patel%20Samaj!5e0!3m2!1sen!2sin!4v1705662369680!5m2!1sen!2sin" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
</section>

"""

# Booking modal HTML
modal_html = """
<!-- Booking Modal -->
<div id="bookingModal" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 hidden opacity-0 transition-opacity duration-300">
  <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md flex flex-col overflow-hidden transform scale-95 transition-transform duration-300" id="bookingModalContent">
    <div class="bg-primary p-5 flex justify-between items-center text-white shrink-0">
      <h3 class="text-lg font-bold font-headline-sm">Enquire for <span id="modalRoomName" class="text-secondary">Room</span></h3>
      <button type="button" onclick="closeBookingModal()" class="text-white hover:text-gray-300 transition">
        <span class="material-symbols-outlined">close</span>
      </button>
    </div>
    <div class="overflow-y-auto p-6 bg-surface">
      <form id="bookingForm" onsubmit="sendToWhatsApp(event)" class="space-y-4">
        <input type="hidden" id="selectedRoom">
        <div>
          <label class="block text-sm font-semibold text-primary mb-1">Full Name</label>
          <input required type="text" id="custName" class="w-full border border-outline-variant rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-secondary transition-all bg-white" placeholder="John Doe">
        </div>
        <div>
          <label class="block text-sm font-semibold text-primary mb-1">Phone Number</label>
          <input required type="tel" id="custPhone" class="w-full border border-outline-variant rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-secondary transition-all bg-white" placeholder="+91 9876543210">
        </div>
        <div>
          <label class="block text-sm font-semibold text-primary mb-1">Number of Guests</label>
          <select required id="totalGuests" class="w-full border border-outline-variant rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-secondary transition-all bg-white cursor-pointer">
            <option value="1">1 Guest</option>
            <option value="2" selected>2 Guests</option>
            <option value="3">3 Guests</option>
            <option value="4">4 Guests</option>
            <option value="5+">5+ Guests</option>
          </select>
        </div>
        <button type="submit" class="w-full bg-[#25D366] hover:bg-[#128C7E] text-white font-bold py-4 px-4 rounded-xl shadow-md hover:-translate-y-0.5 transition-all flex justify-center items-center mt-6">
          <svg viewBox="0 0 24 24" class="w-6 h-6 mr-2 fill-current"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
          Send Enquiry via WhatsApp
        </button>
      </form>
    </div>
  </div>
</div>

<script>
function openBookingModal(roomName, price) {
    document.getElementById('modalRoomName').innerText = roomName;
    document.getElementById('selectedRoom').value = roomName;
    
    const modal = document.getElementById('bookingModal');
    const content = document.getElementById('bookingModalContent');
    
    modal.classList.remove('hidden');
    // Trigger reflow
    void modal.offsetWidth;
    modal.classList.remove('opacity-0');
    content.classList.remove('scale-95');
}

function closeBookingModal() {
    const modal = document.getElementById('bookingModal');
    const content = document.getElementById('bookingModalContent');
    
    modal.classList.add('opacity-0');
    content.classList.add('scale-95');
    
    setTimeout(() => {
        modal.classList.add('hidden');
    }, 300);
}

function sendToWhatsApp(event) {
    event.preventDefault();
    
    const room = document.getElementById('selectedRoom').value;
    const name = document.getElementById('custName').value;
    const phone = document.getElementById('custPhone').value;
    const guests = document.getElementById('totalGuests').value;
    
    const whatsappMobile = "917617265131"; // User's WhatsApp number
    const message = `*Booking Enquiry - Kadva Patel Samaj Dwarka*%0A%0A` +
                    `*Room:* ${room}%0A` +
                    `*Name:* ${name}%0A` +
                    `*Phone:* ${phone}%0A` +
                    `*Guests:* ${guests}%0A%0A` +
                    `I would like to inquire about room availability.`;
    
    const whatsappUrl = `https://wa.me/${whatsappMobile}?text=${message}`;
    window.open(whatsappUrl, '_blank');
    closeBookingModal();
    document.getElementById('bookingForm').reset();
}

// Close modal on click outside
document.getElementById('bookingModal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeBookingModal();
    }
});
</script>
"""

# Replace the old rooms section with the new rooms + extra sections
pattern = re.compile(r'<section.*?id="rooms".*?</section>', re.DOTALL)
new_content = pattern.sub(rooms_html, content)

# Inject the modal and script right before </body>
new_content = new_content.replace('</body>', modal_html + '\n</body>')

with open('index.html', 'w') as f:
    f.write(new_content)

