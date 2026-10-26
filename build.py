#!/usr/bin/env python3
"""Builds the Pro Choice Roofing site: every page shares one header, footer and set of sections.
Edit the content below, then run:  python3 build.py   (writes the .html files next to this script)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://prochoiceroofing.ie'
PHONE, TEL, EMAIL = '087 438 5708', 'tel:+353874385708', 'prochoiceroofers@gmail.com'

# ---------- icons ----------
def svg(body, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
I = {
    'arrow': svg('<path d="M5 12h14M13 6l6 6-6 6"/>', 'arr'),
    'arrowup': svg('<path d="M7 17L17 7M8 7h9v9"/>'),
    'phone': svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>'),
    'mail': svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>'),
    'pin': svg('<path d="M12 22s-8-6.6-8-12a8 8 0 0 1 16 0c0 5.4-8 12-8 12z"/><circle cx="12" cy="10" r="3"/>'),
    'check': svg('<path d="M20 6L9 17l-5-5"/>'),
    'chev': svg('<path d="M6 9l6 6 6-6"/>'),
    'x': svg('<path d="M18 6L6 18M6 6l12 12"/>'),
    'left': svg('<path d="M15 18l-6-6 6-6"/>'),
    'right': svg('<path d="M9 18l6-6-6-6"/>'),
    'bolt': svg('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
    'shield': svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>'),
    'quote': svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>'),
    'star': svg('<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>'),
    'clock': svg('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    'house': svg('<path d="M3 11l9-8 9 8"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>'),
    'wrench': svg('<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8z" transform="scale(.9) translate(1.3 1.3)"/>'),
    'layers': svg('<path d="M12 2l10 5-10 5L2 7z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>'),
    'drop': svg('<path d="M12 2.7l5.7 5.6a8 8 0 1 1-11.4 0z"/>'),
    'chimney': svg('<path d="M3 12l9-8 9 8"/><path d="M15 6.5V3h3v6"/><path d="M5 10.5V21h14V10.5"/>'),
    'gutter': svg('<path d="M3 6h18v3a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z"/><path d="M17 12v9M7 15v2M11 15v4"/>'),
    'storm': svg('<path d="M19 16.9A5 5 0 0 0 18 7h-1.3A8 8 0 1 0 4 15.3"/><path d="M13 11l-4 6h6l-4 6"/>'),
    'roof': svg('<path d="M2 12L12 3l10 9"/><path d="M6 8.5V5h3"/><path d="M5 12v9h14v-9"/>'),
    'hammer': svg('<path d="M15 12l-8.5 8.5a2.1 2.1 0 0 1-3-3L12 9"/><path d="M17.6 15L22 10.6M20.9 11.7l-4.6-4.6a3 3 0 0 0-2.1-.9h-1.8L10 4l1.8-1.8h3.5a6 6 0 0 1 4.2 1.8l2.6 2.6"/>'),
    'chat': svg('<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5z"/>'),
    'search': svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'),
    'broom': svg('<path d="M19.4 2.6l-7.8 7.8"/><path d="M11 9l4 4-3.5 8.5L3 13z"/><path d="M7 17l-2 2"/>'),
    'fb': svg('<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>'),
}
WA = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.5z"/></svg>'
HOUSE_SVG = '<svg class="house" viewBox="0 0 400 260" fill="none" stroke="#fff" stroke-width="22" stroke-linejoin="miter"><path d="M10 250L170 40l160 210"/><path d="M215 60l45-35 130 225"/><path d="M290 70V20h34v95"/></svg>'

# ---------- content ----------
SERVICES = [
    dict(slug='new-roof-installations', name='New Roof Installations', short='New Roof Installation', icon='roof',
         card='roof-6.jpg', img='roof-installation.jpg',
         summary='Complete new roof installations for homes, extensions and commercial properties. We install slate, tile and flat roofing systems using durable materials designed to provide reliable, long-term protection in the Irish climate.',
         h1='New roof installation contractors Dublin.',
         lead='Professionally installed roofing systems for new builds, extensions and replacement projects across North Dublin and the surrounding areas.',
         eyebrow='New roof installations', h2='New roof installation contractors Dublin.',
         body=['Pro Choice Roofing provides complete new roof installation services for residential and commercial properties throughout Dublin and the surrounding areas.',
               'Whether you are building a new property, adding an extension or replacing an ageing roof, our experienced team will assess your requirements and recommend a roofing system suited to your property, budget and the Irish climate.',
               'We manage every stage of the installation, including roof coverings, underlay, battens, ventilation, flashing and roofline components. Every detail is completed carefully to prevent leaks, improve energy efficiency and deliver lasting protection.',
               'From traditional slate and tiled roofs to modern flat roofing systems, we use durable, weather-resistant materials to produce a secure and professional finish.'],
         feats_title='Every stage of your new roof, handled', feats_eyebrow='What’s included',
         feats=[('roof', 'Slate & tiled roofs', 'Traditional slate and tiled roofs installed with durable, weather-resistant materials.'),
                ('layers', 'Underlay & battens', 'New underlay and battens laid properly beneath every roof covering.'),
                ('storm', 'Ventilation & flashing', 'Ventilation and flashing completed carefully to prevent leaks and condensation.'),
                ('gutter', 'Roofline components', 'Fascia, soffits and guttering finished to match for a complete, professional result.')],
         close=('New roofs', 'Built properly, built to last.', 'New builds, extensions and complete roof replacements, managed from first inspection to the final ridge tile. You get clear advice, a written quote and a roof designed for the Irish weather.'),
         ba=2),
    dict(slug='roof-repairs', name='Roof Repairs', short='Roof Repairs', icon='hammer',
         card='roof-5.jpg', img='roof-installation-2.jpg',
         summary='Professional repairs for leaking roofs, broken or missing tiles, damaged flashing, loose ridge tiles and general wear. We identify the source of the problem and complete the necessary work to prevent further damage.',
         h1='Roof repairs Dublin.', lead='Fast, reliable and professional roof repairs for homes and businesses across Dublin and the surrounding areas.',
         eyebrow='Roof repair specialists Dublin', h2='Fast, reliable & professional.',
         body=['Pro Choice Roofing provides dependable roof repair services for residential and commercial properties across Dublin and the surrounding areas. We repair leaking roofs, damaged flashing, broken or missing tiles, loose ridge tiles, storm damage and other common roofing problems.',
               'Our experienced team will inspect your roof, identify the source of the damage and recommend the most practical repair. Whether you have a small leak or significant weather damage, we work carefully to restore your roof, prevent further water ingress and protect your property.'],
         feats_title='The repairs we carry out every week', feats_eyebrow='Roof repair services',
         feats=[('drop', 'Leaking roofs', 'We find where the water is actually getting in and repair the source, not just the stain.'),
                ('roof', 'Broken or missing tiles', 'Slipped, cracked and missing tiles and slates replaced to match your roof.'),
                ('shield', 'Damaged flashing', 'Worn or lifted flashing repaired or replaced to seal joints against the weather.'),
                ('house', 'Loose ridge tiles', 'Ridge tiles re-bedded and secured so they stay put through the next storm.')],
         close=('Roof repairs', 'Repaired right, the first time.', 'From a single slipped tile to significant weather damage, we inspect properly, explain what we find and repair it to last. Every quote is clear and written before any work starts.'),
         ba=3),
    dict(slug='flat-roofing', name='Flat Roofing', short='Flat Roofing', icon='layers',
         card='roof-4.jpg', img='flat-roofing.jpg',
         summary='Flat roof installation, repair and replacement for extensions, garages and commercial properties. We provide durable, weather-resistant systems with effective drainage and a clean, professional finish.',
         h1='Flat roofing experts Dublin.', lead='Flat roof installation, repairs and replacement for homes, extensions, garages and commercial properties.',
         eyebrow='Flat roofing installation and repairs', h2='Flat roofing installation and repairs across Dublin.',
         body=['Pro Choice Roofing provides professional flat roofing services for homes, extensions, garages and commercial properties throughout Dublin. We install, repair and replace flat roofs using durable materials designed to provide long-term protection against leaks and weather damage.',
               'Whether you need a small leak repaired or a complete flat roof replacement, our team will inspect the existing roof and recommend the most suitable solution. We focus on correct drainage, reliable waterproofing and a clean finish to keep your property protected in every season.'],
         feats_title='From minor leaks to complete flat roof replacements', feats_eyebrow='Flat roofing services',
         feats=[('layers', 'New flat roof installations', 'Professionally installed flat roofing for extensions, garages, homes and commercial properties.'),
                ('roof', 'Flat roof replacements', 'Removal and replacement of worn or damaged flat roofs with a durable, watertight new system.'),
                ('drop', 'Flat roof leak repairs', 'Accurate identification and repair of leaks, damaged joints, cracks and other vulnerable areas.'),
                ('shield', 'Waterproofing and maintenance', 'Preventative maintenance and waterproofing work to extend the life of your existing flat roof.')],
         close=('Flat roofing', 'Reliable & built to last.', 'Pro Choice Roofing provides professional flat roof installation, repair and replacement services for homes and commercial properties. From extensions and garages to larger flat roof areas, we use durable, weather-resistant systems designed to prevent leaks, improve drainage and deliver reliable long-term protection in the Irish climate.'),
         ba=1),
    dict(slug='guttering-fascia-soffit', name='Guttering, Fascia & Soffit', short='Guttering, Fascia & Soffits', icon='gutter',
         card='roof-3.jpg', img='guttering.jpg',
         summary='Installation and repair of guttering, fascia, soffits and downpipes. Our roofline solutions direct rainwater safely away from your property while protecting the roof structure and improving its appearance.',
         h1='Guttering, fascia & soffit work Dublin.', lead='Comprehensive guttering, fascia and soffit installation, repair and replacement for homes and commercial properties.',
         eyebrow='Roofline services', h2='Comprehensive guttering, fascia & soffit services in Dublin.',
         body=['Pro Choice Roofing provides professional guttering, fascia and soffit installation, repair and replacement services for homes and commercial properties. We use durable, weather-resistant materials designed to protect your roofline and direct rainwater safely away from your property.',
               'Whether you need leaking gutters repaired, damaged roofline components replaced or a complete new system installed, our experienced team delivers a clean, reliable finish built to withstand the Irish weather.'],
         feats_title='Complete protection for your roofline', feats_eyebrow='Roofline services',
         feats=[('gutter', 'Guttering installation', 'Durable guttering systems professionally installed to collect rainwater and protect your property from water damage.'),
                ('wrench', 'Gutter repairs', 'Reliable repairs for leaking, cracked, blocked or sagging gutters before they cause more serious property damage.'),
                ('house', 'Fascia and soffits', 'Weather-resistant fascia and soffit installation that protects your roof structure and creates a clean, finished appearance.'),
                ('drop', 'Downpipes and drainage', 'Properly positioned downpipes that safely direct rainwater away from your walls, foundations and surrounding ground.')],
         close=('Guttering, fascia & soffit', 'Complete roofline protection.', 'From new guttering installations and repairs to fascia, soffit and downpipe replacements, our team provides complete roofline solutions for homes and commercial properties. We use durable, weather-resistant materials to prevent leaks, improve drainage and protect your roof structure from the Irish weather. Every installation is completed carefully for a clean, long-lasting finish.'),
         ba=None),
    dict(slug='chimney-repairs', name='Chimney Repairs', short='Chimney Repairs', icon='chimney',
         card='roof-2.jpg', img='chimney-repairs.jpg',
         summary='Chimney repointing, flashing repairs, capping, brickwork repairs and partial rebuilds. We resolve common chimney problems that can allow water to enter and damage the surrounding roof structure.',
         h1='Chimney repairs Dublin.', lead='Reliable chimney repairs that keep your home protected from damp, staining and costly structural damage.',
         eyebrow='Chimney repairs', h2='Reliable repairs that keep your home protected.',
         body=['A damaged chimney can allow water into your roof and lead to damp, staining and costly structural damage. Pro Choice Roofing provides professional chimney repairs throughout Dublin for homes of every size.',
               'We repair cracked chimney stacks, damaged pointing, loose chimney pots, worn lead flashing and leaks around the chimney base. Our team will inspect the problem, explain what is required and provide a clear quote before work begins.'],
         feats_title='Common chimney problems, properly fixed', feats_eyebrow='Chimney services',
         feats=[('hammer', 'Repointing', 'Damaged and crumbling pointing raked out and repointed to keep water out of the stack.'),
                ('shield', 'Lead flashing', 'Worn lead flashing replaced to seal the joint between chimney and roof.'),
                ('chimney', 'Pots & capping', 'Loose chimney pots re-secured and stacks capped to stop rain getting in.'),
                ('house', 'Brickwork & rebuilds', 'Cracked stacks and brickwork repaired, with partial rebuilds where needed.')],
         close=('Chimney repairs', 'Stop the leak at the stack.', 'Leaks around the chimney base are one of the most common causes of damp in Irish homes. We inspect the whole stack, explain what we find and fix it properly, with a clear quote before any work begins.'),
         ba=4),
    dict(slug='emergency-roof-repairs', name='Emergency Roof Repairs', short='Emergency Roof Repairs', icon='storm',
         card='roof-1.jpg', img='before-3.jpg',
         summary='Prompt assistance for roof leaks, storm damage, missing tiles and other urgent roofing problems. We assess the damage, secure the affected area and complete repairs to protect your property.',
         h1='Emergency roof repairs Dublin.', lead='Fast response. Reliable repairs. Urgent help when your home needs protecting, 24/7.',
         eyebrow='Emergency roofing', h2='Fast response. Reliable repairs.',
         body=['Roof damage can quickly lead to serious water damage inside your property. Pro Choice Roofing provides fast and dependable emergency roof repairs throughout Dublin when your home needs urgent protection.',
               'We repair storm-damaged roofs, active leaks, missing or broken tiles, damaged flashing, loose ridge tiles and other urgent roofing problems. Our team will identify the source of the damage and secure the affected area before completing the necessary repairs.',
               'If you notice water entering your property or visible damage following severe weather, contact Pro Choice Roofing as soon as possible. We’ll assess the problem, explain the repair required and work to make your roof safe and watertight again.'],
         feats_title='Fast help when your roof is damaged', feats_eyebrow='Emergency roof repair services',
         feats=[('drop', 'Active roof leaks', 'Fast identification and repair of active leaks to help prevent further water damage inside your property.'),
                ('storm', 'Storm damage repairs', 'Repairs for roofing damage caused by strong winds, heavy rain, fallen debris and severe weather.'),
                ('roof', 'Missing tiles and slates', 'Replacement of missing, loose or broken roof tiles and slates before more serious damage develops.'),
                ('shield', 'Emergency roof protection', 'Damaged areas secured and made watertight while the necessary permanent roofing repairs are completed.')],
         close=('Emergency roofing', 'Fast, reliable roof repairs.', 'Pro Choice Roofing provides prompt emergency roof repairs for leaks, storm damage, missing tiles and other urgent roofing problems. Our experienced team assesses the damage, secures the affected area and completes the necessary repairs to prevent further water entering your property and causing more extensive damage.'),
         ba=None),
]
BA = {
    1: ('before-1.jpg', 'after-1.jpg', 'Roofing Project 01', 'Flat roof & parapet gutter'),
    2: ('before-2.jpg', 'after-2.jpg', 'Roofing Project 02', 'Complete roof replacement'),
    3: ('before-3.jpg', 'after-3.jpg', 'Roofing Project 03', 'Broken tiles replaced'),
    4: ('before-4.jpg', 'after-4.jpg', 'Roofing Project 04', 'Chimney pot & capping'),
}
REVIEWS = [
    ('Nathan Power', 'Extension roof repair', 'I have no hesitation in recommending this company. They did a great job repairing the roof of my extension. The rain has been torrential over the past few days and nights, and the roof has stood the test. Great work. Great company.'),
    ('Elaine Cumiskey', 'Roof cleaning and tiles', 'Had James out to clean my roof, replace a few tiles and wash out my gutters. All I can say is it was an amazing job, and I would highly recommend this company. Thanks for your service, James.'),
    ('Stephanie Derbyshire', 'Roof and gutter repairs', 'Very helpful and professional service. James and the team cleaned and repaired our roof and gutters quickly and had everything clean and tidy when they left.'),
    ('Scott Mulready', 'Residential roofing', 'Had Jordan and his team at my house and they did a brilliant job on my roof. They arrived on time, were polite and I wouldn’t go anywhere else. Fully recommend them to anyone needing roofing work done.'),
]
AREAS = [('North Dublin', ['Swords', 'Malahide', 'Portmarnock', 'Skerries', 'Rush', 'Balbriggan']),
         ('Dublin City & West', ['Dublin City', 'Clontarf', 'Raheny', 'Artane', 'Blanchardstown', 'Castleknock']),
         ('Meath & Louth', ['Ashbourne', 'Ratoath', 'Dunboyne', 'Navan', 'Drogheda', 'Laytown'])]
STEPS = [('Inspect & Diagnose', 'We inspect your roof, identify the source of the problem and document any damage that needs attention.'),
         ('Explain & Quote', 'We explain our findings, recommend the right solution and provide a clear written quotation before work begins.'),
         ('Repair & Protect', 'Our team completes the roofing work professionally, checks the finished result and leaves your property clean and tidy.')]
SERVICE_OPTS = ['New Roof Installation', 'Roof Repairs', 'Flat Roofing', 'Chimney Repairs', 'Emergency Roofing', 'Guttering Fascia Soffit']

# ---------- building blocks ----------
def head(p, title, desc, path):
    canon = SITE + '/' + path
    return f'''<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#061630">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/img/after-2.jpg"><meta property="og:url" content="{canon}"><meta property="og:locale" content="en_IE">
<link rel="icon" href="{p}img/icon-192.png"><link rel="apple-touch-icon" href="{p}img/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css?v=1">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"RoofingContractor","name":"Pro Choice Roofing","url":"{SITE}/","telephone":"+353874385708","email":"{EMAIL}","image":"{SITE}/img/after-2.jpg","logo":"{SITE}/img/logo.png","address":{{"@type":"PostalAddress","streetAddress":"20 Mount Eustace Crescent","addressLocality":"Dublin 15","postalCode":"D15 RY6R","addressCountry":"IE"}},"openingHours":"Mo-Su 00:00-23:59","areaServed":["Dublin","Meath","Louth"],"aggregateRating":{{"@type":"AggregateRating","ratingValue":"5","reviewCount":"4"}}}}</script>'''

def header(p, active):
    def on(k): return ' class="on" aria-current="page"' if k == active else ''
    menu = ''.join(f'<a href="{p}{s["slug"]}/"><i>{I[s["icon"]]}</i>{s["name"]}</a>' for s in SERVICES)
    subs = ''.join(f'<a href="{p}{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)
    svc_on = ' class="on"' if active == 'services' else ''
    return f'''<header class="hdr"><div class="wrap">
<a class="brand" href="{p}" aria-label="Pro Choice Roofing home"><img src="{p}img/logo-white.png" alt="Pro Choice Roofing" width="763" height="393"></a>
<nav class="nav" aria-label="Main">
<a href="{p}"{on('home')}>Home</a>
<div class="dd"><a href="{p}services/"{svc_on}>Services {I['chev']}</a><div class="menu">{menu}</div></div>
<a href="{p}portfolio/"{on('portfolio')}>Portfolio</a>
<a href="{p}about/"{on('about')}>About</a>
<a href="{p}contact/"{on('contact')}>Contact</a>
</nav>
<a class="tel" href="{TEL}">{I['phone']}<span data-cfg="phone">{PHONE}</span></a>
<a class="btn btn-blue" href="#quote" data-quote>Request a quote</a>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
</div></header>
<nav class="mnav" aria-label="Mobile">
<a class="ml" href="{p}">Home <small>01</small></a>
<a class="ml" href="{p}services/">Services <small>02</small></a>
<div class="subs">{subs}</div>
<a class="ml" href="{p}portfolio/">Portfolio <small>03</small></a>
<a class="ml" href="{p}about/">About <small>04</small></a>
<a class="ml" href="{p}contact/">Contact <small>05</small></a>
<a class="btn btn-blue" href="#quote" data-quote>Request a free quote</a>
<a class="btn btn-ghost" href="{TEL}" style="margin-top:12px">{I['phone']} Call {PHONE}</a>
<div class="mfoot">20 Mount Eustace Crescent, Dublin 15 · Available 24/7</div>
</nav>'''

def select(name='service'):
    return f'<select name="{name}" required><option value="">Choose a service</option>' + ''.join(f'<option>{o}</option>' for o in SERVICE_OPTS) + '</select>'

def form(p, kind='quote', title='Request a free quote', sub='Free, no-obligation written quotation. We aim to respond to every enquiry within 24 hours.'):
    if kind == 'callback':
        fields = f'''<label class="f"><span>Name</span><input name="name" autocomplete="name" required></label>
<label class="f"><span>Phone</span><input name="phone" type="tel" autocomplete="tel" required></label>
<label class="f full"><span>Email</span><input name="email" type="email" autocomplete="email" required></label>'''
        btn = 'Request a callback'
    else:
        email = '<label class="f"><span>Email</span><input name="email" type="email" autocomplete="email" required></label>' if kind == 'full' else ''
        svc_cls = 'f' if kind == 'full' else 'f full'
        fields = f'''<label class="f"><span>Name</span><input name="name" autocomplete="name" required></label>
<label class="f"><span>Phone</span><input name="phone" type="tel" autocomplete="tel" required></label>
{email}<label class="{svc_cls}"><span>Service</span>{select()}</label>
<label class="f full"><span>Message</span><textarea name="message" placeholder="Tell us about the problem or project" required></textarea></label>'''
        btn = 'Get a quote'
    return f'''<form class="formcard" data-form novalidate>
<h3>{title}</h3><p class="sub">{sub}</p>
<div class="fmsg" role="status"></div>
<div class="fgrid">{fields}</div>
<input class="hp" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-blue" type="submit">{btn} {I['arrow']}</button>
<p class="fnote">Your details are kept private. See our <a href="{p}privacy-policy/">privacy policy</a>.</p>
</form>'''

def quote_drawer(p):
    f = form(p).replace('<form class="formcard"', '<form class="formcard" id="quote"').replace('<h3>', f'<button class="x" type="button" data-close aria-label="Close">{I["x"]}</button><h3>', 1)
    return f'<div class="qd" id="qd" role="dialog" aria-modal="true" aria-label="Request a quote"><div class="scrim" data-close></div>{f}</div>'

def footer(p):
    svc = ''.join(f'<li><a href="{p}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<footer class="ftr"><div class="wrap">
<div class="cols">
<div><img class="fl" src="{p}img/logo-white.png" alt="Pro Choice Roofing" width="763" height="393" loading="lazy">
<p>Pro Choice Roofing provides reliable roofing services throughout Dublin and the surrounding areas. Contact our team today for a free quote.</p>
<span class="h247">{I['clock'].replace('<svg', '<svg width="14" height="14"')} AVAILABLE 24/7</span></div>
<div><h4>Useful Links</h4><ul><li><a href="{p}">Home</a></li><li><a href="{p}about/">About Us</a></li><li><a href="{p}services/">Services</a></li><li><a href="{p}portfolio/">Our Portfolio</a></li><li><a href="{p}contact/">Contact Us</a></li></ul></div>
<div><h4>Services</h4><ul>{svc}</ul></div>
<div><h4>Contact Info</h4><ul class="ci">
<li>{I['pin']}<span>20 Mount Eustace Crescent<br>Dublin 15, D15 RY6R, Ireland</span></li>
<li>{I['phone']}<a href="{TEL}" data-cfg="phone">{PHONE}</a></li>
<li>{I['mail']}<a href="mailto:{EMAIL}" data-cfg="email">{EMAIL}</a></li>
<li>{I['clock']}<span>Open 24/7 for emergencies</span></li></ul></div>
</div>
<div class="base"><span>Copyright © <span data-cfg="year">2026</span> Pro Choice Roofing, All rights reserved.</span>
<nav><a href="{p}cookie-policy/">Cookie Policy</a><a href="{p}privacy-policy/">Privacy Policy</a></nav></div>
</div></footer>
<div class="fab"><a class="ph" href="{TEL}" aria-label="Call {PHONE}">{I['phone']}</a><a class="wa" href="https://wa.me/353874385708" data-href="whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp us">{WA}</a></div>'''

def scripts(p):
    return f'''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
<script src="{p}assets/site.js?v=1" defer></script>'''

def page(path, active, title, desc, body, intro=False):
    p = '../' * path.count('/')
    head_html = head(p, title, desc, path)
    if intro:
        head_html += '\n<script>try{if(!sessionStorage.getItem("pcr_intro")||/[?&]intro/.test(location.search))document.documentElement.classList.add("intro")}catch(e){document.documentElement.classList.add("intro")}</script>'
    loader = ''
    if intro:
        loader = f'''<div id="loader" aria-hidden="true"><div class="sky"></div><i class="glow"></i>
<i class="ring"></i><i class="ring r2"></i>
<div class="box"><div class="logo"><img class="off" src="{p}img/logo-white.png" alt=""><img class="on" src="{p}img/logo-white.png" alt=""></div><div class="lt">Roofing excellence, built to last</div></div>
<svg class="bolt"><defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter></defs></svg>
<div class="flash"></div></div>'''
    html = f'''{head_html}
</head>
<body>
{loader}
{header(p, active)}
<main>
{body(p)}
</main>
{footer(p)}
{quote_drawer(p)}
{scripts(p)}
</body>
</html>
'''
    out = os.path.join(ROOT, path, 'index.html') if path else os.path.join(ROOT, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', os.path.relpath(out, ROOT))

# ---------- sections ----------
def phero(p, crumb, h1, lead, img, extra=''):
    trail = ''.join(f'<span>/</span><a href="{p}{u}">{t}</a>' for t, u in crumb[:-1])
    return f'''<section class="phero" data-rain>
<img class="bg" src="{p}img/{img}" alt="" fetchpriority="high">
<div class="wrap">
<div class="crumb"><a href="{p}">Home</a>{trail}<span>/</span><b>{crumb[-1][0]}</b></div>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
{extra}
</div></section>'''

def marquee():
    items = ['New roof installations', 'Roof repairs', 'Flat roofing', 'Chimney repairs', 'Emergency call-outs 24/7', 'Guttering, fascia & soffits', 'Dublin, Meath & Louth', 'Free written quotes']
    s = ''.join(f'<span>{t}</span>' for t in items)
    return f'<div class="marquee" aria-hidden="true"><div class="track">{s}{s}</div></div>'

def feats():
    f = [('bolt', 'Fast Response', 'Urgent call-outs 24/7'), ('quote', 'Free Roof Quotes', 'Clear, written & fixed'),
         ('shield', 'Fully Insured', 'Roofing specialists'), ('star', '5-Star Rated', 'By Dublin homeowners')]
    cards = ''.join(f'<div class="feat"><i>{I[a]}</i><div><b>{b}</b><span>{c}</span></div></div>' for a, b, c in f)
    return f'<section class="sec tight soft"><div class="wrap"><div class="feats" data-reveal="group">{cards}</div></div></section>'

def services_grid(p, title='Expert roofing. Reliable protection. Built to last.', imgs='card', dark=False, head=True):
    cards = ''
    for i, s in enumerate(SERVICES, 1):
        cards += f'''<a class="scard" href="{p}{s['slug']}/"><img src="{p}img/{s[imgs]}" alt="{s['name']} by Pro Choice Roofing" loading="lazy">
<span class="num">0{i}</span><span class="go">{I['arrow']}</span>
<h3>{s['name']}</h3><p>{s['summary']}</p><span class="tlink">View service {I['arrow']}</span></a>'''
    hd = f'''<div class="sec-head"><div><span class="eyebrow">Our roofing services</span><h2 data-split>{title}</h2></div>
<a class="btn {'btn-ghost' if dark else 'btn-line'}" href="{p}services/">All services {I['arrow']}</a></div>''' if head else ''
    return f'<section class="sec{" dark" if dark else ""}" id="services"><div class="wrap">{hd}<div class="sgrid" data-reveal="group">{cards}</div></div></section>'

def compare(p, n):
    b, a, t, s = BA[n]
    return f'''<figure class="ba"><div class="compare"><img class="after" src="{p}img/{a}" alt="{s}: after, by Pro Choice Roofing" loading="lazy"><img class="before" src="{p}img/{b}" alt="{s}: before" loading="lazy">
<span class="tag l">Before</span><span class="tag r">After</span><span class="handle"></span>
<input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"></div>
<figcaption>{t}<span>{s}</span></figcaption></figure>'''

def before_after(p, grid=False, soft=False):
    items = ''.join(compare(p, n) for n in BA)
    inner = f'<div class="ba-grid" data-reveal="group">{items}</div>' if grid else f'<div class="ba-scroll">{items}</div>'
    return f'''<section class="sec{' soft' if soft else ''}" id="work"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Before &amp; After</span><h2 data-split>See the Pro Choice difference.</h2></div>
<p>Drag the slider across each project to see the difference our professional roofing work can make.</p></div>
{inner}</div></section>'''

def steps():
    s = ''.join(f'<div class="step"><div class="n">0{i}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(STEPS, 1))
    return f'''<section class="sec soft"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">How we work</span><h2 data-split>From roof inspection to completed work.</h2></div>
<div class="steps" data-reveal="group">{s}</div></div></section>'''

def reviews():
    r = ''.join(f'''<div class="review"><div class="stars" aria-label="5 stars">★★★★★</div><q>{t}</q>
<div class="who"><span class="av">{n[0]}</span><div><b>{n}</b><span>Google Review</span><br><span class="job">{j}</span></div></div></div>''' for n, j, t in REVIEWS)
    return f'''<section class="sec deep" data-rain><div class="wrap" style="position:relative;z-index:2">
<div class="sec-head"><div><span class="eyebrow">Customer reviews</span><h2 data-split>Trusted roofing. Recommended by homeowners.</h2></div>
<div><p>See what our customers say about the quality, reliability and professional service delivered by our roofing team.</p>
<div class="rhead"><span class="stars">★★★★★</span><b>5.0</b><span style="font-size:.85rem;color:rgba(255,255,255,.7)">Rated 5/5 · Excellent</span></div></div></div>
<div class="rgrid" data-reveal="group">{r}</div></div></section>'''

def areas():
    a = ''.join(f'<div class="area"><h3>{I["pin"]}{t}</h3><div class="chips">{"".join(f"<span>{x}</span>" for x in xs)}</div></div>' for t, xs in AREAS)
    return f'''<section class="sec"><div class="wrap">
<span class="eyebrow">Areas we serve</span><h2 data-split style="max-width:20ch">Professional roofing across Dublin and surrounding areas.</h2>
<p>Pro Choice Roofing provides new roof installations, roof repairs, flat roofing and guttering services throughout Dublin, Meath and Louth.</p>
<div class="areas" data-reveal="group">{a}</div>
<div class="callcard" data-reveal><div><h3>Not sure if we cover your area?</h3><p>Call our roofing team and we will be happy to help.</p></div>
<a class="btn btn-white" href="{TEL}">{I['phone']} Call {PHONE}</a></div>
</div></section>'''

def cta(p):
    return f'''<section class="cta">{HOUSE_SVG}<div class="wrap">
<div><span class="eyebrow">Contact Pro Choice Roofing</span><h2 data-split>Need a professional roofing quote?</h2>
<p>Contact our roofing team for a free written quotation. We aim to respond to every enquiry within 24 hours.</p></div>
<div class="btn-row"><a class="btn btn-white" href="{p}contact/">Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{TEL}">{I['phone']} {PHONE}</a></div>
</div></section>'''

def talk(p):
    return f'''<section class="sec"><div class="wrap"><div class="talk">
<div class="badge" data-reveal><img src="{p}img/badge.jpg" alt="Pro Choice Roofing: reliable, dependable, experienced" width="600" height="500" loading="lazy">
<div class="in"><span class="eyebrow">Prefer to talk?</span><h3>Speak directly with our roofing team.</h3>
<p>Get honest advice and a free quote for your roofing project. No call-out fees and no pushy sales.</p>
<a class="btn btn-blue" href="{TEL}">{I['phone']} Call {PHONE}</a></div></div>
<div data-reveal>{form(p, 'callback', 'Request a callback', 'Have a member of our team reach out to you to find out more.')}</div>
</div></div></section>'''

# ---------- pages ----------
def home(p):
    trust = ''.join(f'<li>{I["check"]}{t}</li>' for t in ['Free Roof Inspections & Fixed Quotes', 'Fully Insured Roofing Specialists', 'Quality Workmanship, Fully Guaranteed'])
    return f'''<section class="hero" data-rain>
<img class="bg" src="{p}img/roof-1.jpg" alt="" fetchpriority="high">
<div class="wrap">
<div>
<div class="gbadge"><span class="stars">★★★★★</span><b>5/5</b> Rated excellent by Dublin homeowners</div>
<span class="eyebrow">Dublin · Meath · Louth</span>
<h1>Reliable roofing &amp; roof repair contractors in <span class="blue">Dublin.</span></h1>
<p class="lead">New roofs, roof repairs, flat roofing, chimneys, guttering and 24/7 emergency call-outs. Quality materials, installed properly the first time, with a clear written quote before any work starts.</p>
<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{p}portfolio/">Our work</a></div>
<ul class="trust">{trust}</ul>
</div>
<div class="vwrap"><span class="frame"></span>
<div class="vcard"><video src="{p}img/hero.mp4" poster="{p}img/hero-poster.jpg" muted loop playsinline preload="metadata" aria-label="Pro Choice Roofing re-roofing a house"></video></div>
<span class="tag"><i></i>Recent work</span>
<div class="pill"><i>{I['bolt']}</i><div><b>24/7 call-outs</b><span>Emergency roof repairs</span></div></div>
</div>
</div>
<div class="scroll">Scroll</div>
</section>
{marquee()}
{feats()}
<section class="sec" id="about"><div class="wrap split">
<div>
<span class="eyebrow">About us</span>
<h2 data-split>Roofing excellence, built to last.</h2>
<p class="lead" style="color:var(--ink)">Pro Choice Roofing delivers dependable roofing services for homes and businesses, combining skilled workmanship, quality materials and results built to last.</p>
<p>We provide complete roofing solutions, including new roof installations, roof repairs, flat roofing, roof maintenance and storm damage repairs. From minor leaks to complete roof replacements, every project receives the same professional attention and high standard of workmanship.</p>
<p>Our experienced roofers carefully assess each property before recommending the most effective solution. We provide clear advice, transparent quotations and dependable service, ensuring every roof is completed safely, efficiently and with long-term protection in mind.</p>
<div class="callrow"><a class="btn btn-line" href="{p}about/">More about us {I['arrow']}</a>
<div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div>
</div>
<div class="collage">
<figure data-clip><img src="{p}img/roofer-dublin.jpg" alt="Pro Choice roofer at work in Dublin" loading="lazy"></figure>
<figure data-clip><img src="{p}img/roof-installation.jpg" alt="New tiled roof being installed" loading="lazy"></figure>
<figure data-clip><img src="{p}img/roof-installation-2.jpg" alt="Roofers fitting a new tile roof" loading="lazy"></figure>
<figure data-clip><img src="{p}img/roof-cleaning.jpg" alt="Roof cleaning in progress" loading="lazy"></figure>
</div>
</div></section>
<section class="sec dark weather" data-rain><div class="big" aria-hidden="true">IRISH WEATHER</div><div class="wrap split rev">
<div>
<span class="eyebrow">Built for Ireland</span>
<h2 data-split>Roofs built for Irish weather.</h2>
<p class="lead">Rain, wind and everything in between, a roof in Ireland has to work harder than most. That’s why we only fit quality materials, installed properly the first time, with clear advice and a transparent quote before any work starts.</p>
<p>Whether it’s a leak that needs fixing this week or a full replacement you’re planning ahead for, you’ll get straight answers and a roof that lasts.</p>
<div class="callrow"><a class="btn btn-blue" href="#quote" data-quote>Get a quote {I['arrow']}</a>
<div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div>
</div>
<div class="ph tall" data-clip><img src="{p}img/after-2.jpg" alt="Finished new roof by Pro Choice Roofing" loading="lazy"><span class="chip">{I['shield']}Quality workmanship, fully guaranteed</span></div>
</div></section>
{services_grid(p, imgs='card')}
{before_after(p, soft=True)}
<section class="sec"><div class="wrap split">
<div>
<span class="eyebrow">Contact us</span>
<h2 data-split>Every reliable roof begins with the right team.</h2>
<p>Whether you need a new roof installation, roof repairs, flat roofing, chimney repairs, emergency repairs, or new guttering, fascia and soffits, Pro Choice Roofing will protect your property with quality workmanship built to last.</p>
<ul class="ticks"><li>{I['mail']}<a href="mailto:{EMAIL}" data-cfg="email">{EMAIL}</a></li><li>{I['phone']}<a href="{TEL}" data-cfg="phone">{PHONE}</a></li><li>{I['pin']}20 Mount Eustace Crescent, Dublin 15</li></ul>
<a class="btn btn-line" href="{p}contact/">Get a quote {I['arrow']}</a>
</div>
<div class="ph" data-clip><img src="{p}img/roof-6.jpg" alt="Pro Choice roofers fitting a Velux window on a slate roof" loading="lazy"><span class="chip">{I['star']}5-star rated on Google</span></div>
</div></section>
{reviews()}
<section class="sec soft"><div class="wrap split">
<div>
<span class="eyebrow">About us</span>
<h2 data-split>Innovative &amp; experienced.</h2>
<p>Serving Dublin and the surrounding areas, the Pro Choice Roofing team brings extensive practical knowledge to every project. We use proven roofing techniques, dependable materials and careful inspections to deliver long-lasting protection for homes of every size.</p>
<p>Our core services include new roof installations, roof repairs, flat roofing, chimney repairs, guttering, fascias and soffits, and emergency roof repairs. From identifying difficult leaks to completing full roof replacements, our experienced team provides clear advice, professional workmanship and reliable results from start to finish.</p>
<a class="btn btn-line" href="{p}about/">Discover more {I['arrow']}</a>
</div>
<div data-reveal>{form(p, 'quote', 'Get a quote')}</div>
</div></section>
{areas()}
{steps()}
{cta(p)}'''

def services_page(p):
    details = ''
    for i, s in enumerate(SERVICES, 1):
        details += f'''<div class="sdetail"><div class="ph" data-clip><img src="{p}img/{s['card']}" alt="{s['name']} by Pro Choice Roofing" loading="lazy"></div>
<div><div class="bign">0{i}</div><h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem)">{s['name']}</h2><p>{s['summary']}</p>
<ul class="ticks">{''.join(f"<li>{I['check']}{f[1]}</li>" for f in s['feats'])}</ul>
<a class="btn btn-blue" href="{p}{s['slug']}/">View service {I['arrow']}</a></div></div>'''
    return f'''{phero(p, [('Services', 'services/')], 'Roofing services in Dublin.', 'New roof installations, roof repairs, flat roofing, guttering, fascia and soffits, chimney repairs and 24/7 emergency roof repairs, across Dublin, Meath and Louth.', 'roof-3.jpg', f'<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Request a quote {I["arrow"]}</a><a class="btn btn-ghost" href="{TEL}">{I["phone"]} {PHONE}</a></div>')}
{services_grid(p, title='What we offer.', imgs='card')}
<section class="sec deep"><div class="wrap">
<div class="center" style="margin-bottom:60px"><span class="eyebrow">In detail</span><h2 data-split>Expert roofing. Reliable protection.</h2></div>
{details}</div></section>
{reviews()}
{steps()}
{cta(p)}'''

def service_page(s):
    def body(p):
        feats_html = ''.join(f'<div class="card"><span class="ico">{I[a]}</span><h3>{b}</h3><p>{c}</p></div>' for a, b, c in s['feats'])
        paras = ''.join(f'<p>{x}</p>' for x in s['body'])
        ba = ''
        if s['ba']:
            ba = f'''<section class="sec soft"><div class="wrap split">
<div><span class="eyebrow">Before &amp; After</span><h2 data-split>See the Pro Choice difference.</h2><p>Drag the slider across the photo to see the difference our professional roofing work can make.</p>
<a class="btn btn-line" href="{p}portfolio/">See all our projects {I['arrow']}</a></div>
<div data-reveal>{compare(p, s['ba'])}</div></div></section>'''
        others = [o for o in SERVICES if o is not s]
        other_cards = ''.join(f'''<a class="scard" href="{p}{o['slug']}/" style="min-height:300px"><img src="{p}img/{o['card']}" alt="" loading="lazy"><span class="go">{I['arrow']}</span><h3>{o['name']}</h3><span class="tlink">View service {I['arrow']}</span></a>''' for o in others[:3])
        ce, ch, ct = s['close']
        return f'''{phero(p, [('Services', 'services/'), (s['name'], s['slug'] + '/')], s['h1'], s['lead'], s['card'], f'<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I["arrow"]}</a><a class="btn btn-ghost" href="{TEL}">{I["phone"]} Call {PHONE}</a></div>')}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">{s['eyebrow']}</span><h2 data-split>{s['h2']}</h2>{paras}
<div class="callrow"><a class="btn btn-blue" href="#quote" data-quote>Request a quote {I['arrow']}</a><div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div></div>
<div class="ph tall" data-clip><img src="{p}img/{s['img']}" alt="{s['name']} in Dublin by Pro Choice Roofing" loading="lazy"><span class="chip">{I[s['icon']]}{s['name']}</span></div>
</div></section>
<section class="sec soft"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">{s['feats_eyebrow']}</span><h2 data-split>{s['feats_title']}.</h2></div>
<div class="cards" data-reveal="group">{feats_html}</div></div></section>
{talk(p)}
{ba}
{reviews()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">{ce}</span><h2 data-split>{ch}</h2><p>{ct}</p>
<ul class="ticks"><li>{I['check']}Free roof inspections &amp; fixed quotes</li><li>{I['check']}Fully insured roofing specialists</li><li>{I['check']}Quality workmanship, fully guaranteed</li></ul></div>
<div data-reveal>{form(p, 'quote', 'Get a quote')}</div></div></section>
{steps()}
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">More services</span><h2 data-split>Other ways we can help.</h2></div><a class="btn btn-line" href="{p}services/">All services {I['arrow']}</a></div>
<div class="sgrid" data-reveal="group">{other_cards}</div></div></section>
{cta(p)}'''
    return body

def about_page(p):
    svc = ''.join(f'<div class="card"><span class="ico">{I[s["icon"]]}</span><h3><a href="{p}{s["slug"]}/">{s["name"]}</a></h3><p>{s["summary"]}</p><a class="tlink" href="{p}{s["slug"]}/" style="margin-top:16px">Learn more {I["arrow"]}</a></div>' for s in SERVICES)
    return f'''{phero(p, [('About', 'about/')], 'We deliver top quality roofing projects throughout Dublin.', 'Reliable, experienced roofers for homeowners and commercial clients across North Dublin and the surrounding areas.', 'roof-5.jpg')}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">About us</span><h2 data-split>Reliable &amp; experienced.</h2>
<p>Pro Choice Roofing provides professional roofing services for homeowners and commercial clients throughout North Dublin and the surrounding areas. Our experienced team handles projects of every size, from minor roof repairs and storm damage to complete new roof installations.</p>
<p>We take the time to assess each roof properly, explain the available options and recommend the most practical solution for the property. Our focus is always on dependable workmanship, durable materials and clear communication from the initial inspection through to completion.</p>
<p>We specialise in new roof installations, roof repairs, flat roofing, chimney repairs, emergency roofing and guttering, fascia and soffit work. Every project is approached carefully, with close attention paid to weatherproofing, drainage, ventilation and the details that protect a property over the long term.</p>
<p>Whether you have discovered a leak, need an ageing roof replaced or want professional advice before starting a project, Pro Choice Roofing is ready to help. Contact us to arrange an assessment and receive a free written quotation.</p>
<div class="btn-row" style="margin-top:26px"><a class="btn btn-blue" href="{p}portfolio/">Our projects {I['arrow']}</a><a class="btn btn-line" href="{p}contact/">Contact us</a></div></div>
<div class="ph tall" data-clip><img src="{p}img/roof-5.jpg" alt="Newly tiled roof by Pro Choice Roofing" loading="lazy"><span class="chip">{I['shield']}Fully insured roofing specialists</span></div>
</div></section>
{feats()}
<section class="sec"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Our services</span><h2 data-split>Complete roofing, start to finish.</h2></div>
<p>Pro Choice Roofing provides reliable roofing installations, repairs and maintenance across North Dublin and the surrounding areas.</p></div>
<div class="cards c3" data-reveal="group">{svc}</div></div></section>
{before_after(p, soft=True)}
{reviews()}
{steps()}
{cta(p)}'''

def portfolio_page(p):
    gal = ['after-2.jpg', 'roof-6.jpg', 'roofer-dublin.jpg', 'roof-5.jpg', 'roof-1.jpg', 'after-3.jpg', 'roof-2.jpg', 'roof-3.jpg', 'after-1.jpg', 'roof-4.jpg', 'roof-installation-2.jpg', 'after-4.jpg', 'chimney-repairs.jpg', 'flat-roofing.jpg', 'guttering.jpg', 'roof-cleaning.jpg', 'roof-installation.jpg']
    g = ''.join(f'<a href="{p}img/{x}"><img src="{p}img/{x}" alt="Roofing project by Pro Choice Roofing" loading="lazy"></a>' for x in gal)
    return f'''{phero(p, [('Portfolio', 'portfolio/')], 'Our portfolio.', 'Real roofs, real results. A look at recent roofing projects completed by the Pro Choice team across Dublin and the surrounding areas.', 'after-2.jpg')}
{before_after(p, grid=True)}
<section class="sec soft"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Gallery</span><h2 data-split>Recent jobs.</h2></div><p>Tap a photo to see it full size.</p></div>
<div class="gal">{g}</div></div></section>
<div class="lb" role="dialog" aria-label="Photo viewer"><button class="x" aria-label="Close">{I['x']}</button><button class="pv" aria-label="Previous">{I['left']}</button><img alt=""><button class="nx" aria-label="Next">{I['right']}</button></div>
{cta(p)}'''

def contact_page(p):
    return f'''{phero(p, [('Contact', 'contact/')], 'Contact info.', 'Urgent roof repair, new roof installation or a free quotation for planned work, Pro Choice Roofing is ready to help.', 'roof-6.jpg')}
<section class="sec" style="padding-top:0"><div class="wrap">
<div class="info" data-reveal="group">
<div class="ic"><span class="ico">{I['pin']}</span><div><h3>Our Address</h3><p>20 Mount Eustace Crescent<br>Dublin 15, D15 RY6R<br>Ireland</p></div></div>
<a href="{TEL}"><span class="ico">{I['phone']}</span><div><h3>Phone Number</h3><p data-cfg="phone">{PHONE}</p><p style="font-size:.85rem">Available 24/7</p></div></a>
<a href="mailto:{EMAIL}"><span class="ico">{I['mail']}</span><div><h3>Email Address</h3><p data-cfg="email" style="word-break:break-all">{EMAIL}</p></div></a>
</div>
<div class="split" style="margin-top:80px;align-items:start">
<div><span class="eyebrow">Get in touch</span><h2 data-split>Get in touch.</h2>
<p>Whether you need an urgent roof repair, a new roof installation or a free quotation for planned roofing work, Pro Choice Roofing is ready to help. Complete the form or call us on <a class="blue" href="{TEL}"><b>{PHONE}</b></a>. Tell us about the problem and our team will get back to you as soon as possible.</p>
<div class="map" style="margin-top:28px"><iframe title="Pro Choice Roofing location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=20%20Mount%20Eustace%20Crescent%2C%20Dublin%2015%2C%20D15%20RY6R&amp;z=14&amp;output=embed"></iframe></div></div>
<div data-reveal>{form(p, 'full', 'Send us a message', 'Free, no-obligation quotation. We aim to respond within 24 hours.')}</div>
</div></div></section>
{cta(p)}'''

COOKIES = [('pcr_intro', 'Session storage', 'Remembers that the opening animation has already played, so it only shows once per visit.', 'End of session')]
def cookie_page(p):
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in COOKIES)
    return f'''{phero(p, [('Cookie Policy', 'cookie-policy/')], 'Cookie policy.', 'How this website uses cookies and similar technologies.', 'roof-3.jpg')}
<section class="sec"><div class="wrap article">
<p>This page explains how we use cookies and similar technologies on our website. Cookies are small text files that are stored on your device when you visit a website. They help a site work properly and can help its owner understand how visitors use it. We are committed to respecting your privacy and being transparent about the data we collect. For more information on how we handle your personal data, please see our <a class="blue" href="{p}privacy-policy/">Privacy Policy</a>.</p>
<h2>Essential</h2>
<p>Essential storage enables basic functions and is necessary for the website to work properly. It does not identify you.</p>
<table><thead><tr><th>Name</th><th>Type</th><th>Description</th><th>Duration</th></tr></thead><tbody>{rows}</tbody></table>
<h2>Statistics &amp; marketing</h2>
<p>This website does not currently set any analytics, advertising or tracking cookies. If we add analytics in the future (for example Google Analytics), it will only load after you give consent, and this page will be updated to list each cookie, its purpose and how long it lasts.</p>
<h2>Third-party content</h2>
<p>Our contact page shows an embedded Google Map. Google may set its own cookies when the map loads. See <a class="blue" href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google’s privacy policy</a> for details. Fonts are served by Google Fonts.</p>
<h2>Managing cookies</h2>
<p>You can block or delete cookies and site data at any time in your browser settings. Blocking essential storage will not stop the site from working; the opening animation may simply play again.</p>
<h2>Contact</h2>
<p>Questions about this policy? Email <a class="blue" href="mailto:{EMAIL}">{EMAIL}</a> or call <a class="blue" href="{TEL}">{PHONE}</a>.</p>
</div></section>
{cta(p)}'''

def privacy_page(p):
    return f'''{phero(p, [('Privacy Policy', 'privacy-policy/')], 'Privacy policy.', 'How Pro Choice Roofing collects, uses and protects your personal information.', 'roof-4.jpg')}
<section class="sec"><div class="wrap article">
<p>Pro Choice Roofing (“we”, “us”) respects your privacy. This policy explains what personal information we collect through this website and how we use it, in line with the General Data Protection Regulation (GDPR) and Irish data protection law.</p>
<h2>Who we are</h2>
<p>Pro Choice Roofing, 20 Mount Eustace Crescent, Dublin 15, D15 RY6R, Ireland. Email <a class="blue" href="mailto:{EMAIL}">{EMAIL}</a>, phone <a class="blue" href="{TEL}">{PHONE}</a>.</p>
<h2>What we collect</h2>
<p>When you send a quote request, callback request or message, we collect the details you give us: your name, phone number, email address, the service you are interested in and your message. We do not collect any other personal information through this website.</p>
<h2>How we use it</h2>
<ul><li>To respond to your enquiry and arrange a roof inspection or quotation.</li><li>To carry out and follow up on work you have asked us to do.</li><li>To keep records required for accounting and legal purposes.</li></ul>
<p>Our legal basis is taking steps at your request before entering into a contract, and our legitimate interest in replying to enquiries. We never sell your information or use it for unrelated marketing.</p>
<h2>How long we keep it</h2>
<p>Enquiries that do not lead to work are deleted within 12 months. Records relating to completed work are kept for as long as required by law.</p>
<h2>Sharing</h2>
<p>We only share your information with service providers that help us run our business (such as our email provider), and only as needed. We do not transfer it outside the EEA except where appropriate safeguards are in place.</p>
<h2>Your rights</h2>
<p>You can ask to access, correct or delete your personal data, restrict or object to how we use it, or ask for a copy. Contact us using the details above. You also have the right to complain to the Data Protection Commission (dataprotection.ie).</p>
<h2>Cookies</h2>
<p>See our <a class="blue" href="{p}cookie-policy/">Cookie Policy</a>.</p>
</div></section>
{cta(p)}'''

if __name__ == '__main__':
    T = ' | Pro Choice Roofing'
    page('', 'home', 'Roof Repair And Replacement Experts In Dublin - Pro Choice Roofing',
         'Pro Choice Roofing: reliable roofing and roof repair contractors in Dublin. New roofs, roof repairs, flat roofing, chimneys, guttering and 24/7 emergency repairs. Free quotes.', home, intro=True)
    page('services/', 'services', 'Roofing Services Dublin' + T, 'New roof installations, roof repairs, flat roofing, guttering, fascia & soffits, chimney repairs and emergency roof repairs across Dublin.', services_page)
    for s in SERVICES:
        page(s['slug'] + '/', 'services', s['h1'].rstrip('.').replace(' Dublin', ' Dublin') + T, s['summary'], service_page(s))
    page('portfolio/', 'portfolio', 'Our Portfolio' + T, 'Before and after roofing projects and recent jobs by Pro Choice Roofing in Dublin.', portfolio_page)
    page('about/', 'about', 'About Us' + T, 'Pro Choice Roofing: reliable, experienced roofers for homes and businesses across North Dublin, Meath and Louth.', about_page)
    page('contact/', 'contact', 'Contact Us' + T, 'Contact Pro Choice Roofing for a free roofing quote. Call 087 438 5708 or email prochoiceroofers@gmail.com.', contact_page)
    page('cookie-policy/', '', 'Cookie Policy' + T, 'How the Pro Choice Roofing website uses cookies.', cookie_page)
    page('privacy-policy/', '', 'Privacy Policy' + T, 'How Pro Choice Roofing handles your personal information.', privacy_page)
