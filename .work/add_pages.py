"""One-off authoring helper; run from project root with python -I .work/add_pages.py."""
from pathlib import Path
from urllib.parse import quote
import re

root = Path(__file__).resolve().parents[1]
home = (root/'index.html').read_text(encoding='utf-8')

def section(name):
    return next(line for line in home.splitlines() if f'id="{name}"' in line and line.startswith('<section'))

def button(label, href, light=False):
    return f'<a class="button{" light" if light else ""}" href="{href}">{label}<span class="arrow" aria-hidden="true">↗</span></a>'

partnership = 'https://wa.me/6285284992841?text=' + quote('Halo Green House Indonesia, saya ingin berdiskusi mengenai peluang kemitraan.', safe='')

def intro(label, title, text):
    return f'''<section class="page-intro"><div class="container">
<nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Beranda</a><span aria-hidden="true">/</span><span aria-current="page">{label}</span></nav>
<span class="pill">Green House Indonesia</span><h1>{title}</h1><p>{text}</p>
</div></section>'''

def cta(title, label, href):
    return f'<div class="product-cta"><div class="container product-cta-inner"><h2>{title}</h2>{button(label, href)}</div></div>'

# Reuse authored HTML directly, never regenerate or alter audited photos.
products = section('produk').replace('id="produk"', 'id="pilihan-produk"')
about = section('tentang').replace('section pale', 'section').replace('id="tentang"', 'id="profil"')
values_start = about.index('<div class="values">')
about = about[:values_start] + '''<div class="brand-roles"><div><h3>PT GHI Makmur Indonesia</h3><p>Badan usaha yang mengembangkan agribisnis melon terintegrasi.</p></div><div><h3>Green House Indonesia</h3><p>Identitas kegiatan greenhouse dan pertanian modern.</p></div><div><h3>GHI MELON</h3><p>Merek produk melon, dengan Inthanon Signature sebagai produk fokus.</p></div></div>''' + about[values_start:]
photo = re.search(r'<img class="signature-image"[^>]+>', products).group().replace('signature-image', 'quality-image')
editorial = f'''<section class="section pale"><div class="container quality-layout">{photo}<div><span class="pill">Dari hulu ke hilir</span><h2>Budidaya dan pasar,<br>dalam satu arah.</h2><p>Greenhouse, budidaya hidroponik, penanganan pascapanen, dan pemasaran menjadi bagian dari pengembangan agribisnis kami.</p><p class="about-copy">Kenali pilihan varietas yang diperkenalkan melalui merek GHI MELON.</p><a class="text-link" href="katalog.html">Jelajahi katalog <span aria-hidden="true">↗</span></a></div></div></section>'''
contact = section('kontak').replace('id="kontak"', 'id="hubungi"').replace("Let's grow<br>together.", 'Produk, greenhouse,<br>atau kemitraan?')
contact += f'''<section class="section pale"><div class="container partner-layout"><div><span class="pill">Langkah berikutnya</span><h2>Mulai dari kebutuhan Anda.</h2><p>Pilih produk untuk percakapan yang lebih spesifik, atau diskusikan peluang kerja sama dengan tim kami.</p>{button('Diskusikan Kemitraan', partnership)}</div><ul class="partner-options"><li><div><h3>Ingin mengenal produk?</h3><p>Jelajahi enam varietas GHI MELON. Tautan di setiap detail produk menyiapkan pesan sesuai varietas yang dipilih.</p><a class="text-link" href="katalog.html">Lihat katalog produk <span aria-hidden="true">↗</span></a></div></li><li><div><h3>Menjajaki kerja sama?</h3><p>Sampaikan kebutuhan greenhouse, budidaya, pembelian, atau distribusi. Cakupan dan ketentuan kerja sama dibahas berdasarkan kebutuhan serta kesepakatan.</p></div></li></ul></div></section>'''

pages = {
 'katalog.html': ('Katalog Produk | GHI MELON', 'Jelajahi enam varietas GHI MELON, dari Inthanon Signature hingga Sweet Lavender. Lihat foto dan detail untuk membahas kebutuhan produk.', intro('Katalog Produk', 'Katalog Produk', 'Enam varietas GHI MELON. Kenali pilihan kami, lihat detail buah, lalu bicarakan kebutuhan Anda.') + products + cta('Sudah menemukan pilihan Anda?', 'Bicarakan Kebutuhan Anda', 'kontak.html')),
 'tentang.html': ('Tentang Kami | PT GHI Makmur Indonesia', 'Kenali PT GHI Makmur Indonesia, Green House Indonesia, dan GHI MELON: profil, nilai, visi, serta arah pengembangan agribisnis melon.', intro('Tentang Kami', 'Tentang Kami', 'Mengenal perusahaan di balik Green House Indonesia dan GHI MELON, dari arah pengembangan hingga nilai yang kami pegang.') + about + editorial + cta('Tumbuh bersama melalui kemitraan.', 'Diskusikan Kemitraan', partnership)),
 'kontak.html': ('Kontak | Green House Indonesia & GHI MELON', 'Hubungi Green House Indonesia dan GHI MELON melalui telepon atau WhatsApp. Informasi alamat kantor dan percakapan produk maupun kemitraan.', intro('Kontak', 'Mari Mulai Percakapan', 'Untuk kebutuhan produk melon, greenhouse, atau peluang kemitraan. Hubungi kami melalui saluran berikut.') + contact),
}
header = home[home.index('<header'):home.index('<main')]
footer = home[home.index('<footer'):]
head = home[:home.index('<header')]
for name, (title, description, content) in pages.items():
    page_head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head)
    page_head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{description}">', page_head)
    page_header = header.replace('href="#beranda"', 'href="index.html"')
    page_header = page_header.replace('href="#layanan"', 'href="index.html#layanan"').replace('href="#kemitraan"', 'href="index.html#kemitraan"')
    page_footer = footer.replace('href="#layanan"', 'href="index.html#layanan"').replace('href="#kemitraan"', 'href="index.html#kemitraan"')
    (root/name).write_text(page_head + page_header + '<main id="konten-utama" tabindex="-1">\n' + content + '\n</main>' + page_footer, encoding='utf-8')

for path in [root/'index.html', *root.glob('produk/*.html'), *[root/name for name in pages]]:
    text = path.read_text(encoding='utf-8')
    prefix = '../' if path.parent.name == 'produk' else ''
    for anchor, destination in [('tentang', 'tentang.html'), ('produk', 'katalog.html'), ('kontak', 'kontak.html')]:
        for old in [f'#{anchor}', f'index.html#{anchor}', f'../index.html#{anchor}']:
            text = text.replace(f'href="{old}"', f'href="{prefix}{destination}"')
    text = text.replace('href="../index.html#beranda"', 'href="../index.html"')
    text = text.replace('<div class="footer-links"><a href="tel:', f'<div class="footer-links"><a href="{prefix}kontak.html">Halaman kontak</a><a href="tel:')
    if path.name in pages:
        before, after = text.split('</header>', 1)
        before = before.replace(f'href="{path.name}"', f'href="{path.name}" aria-current="page"')
        text = before + '</header>' + after
    path.write_text(text, encoding='utf-8')
print('Created three pages; synchronized ten HTML navigation shells.')
