"""Run: python -I tests/check_site.py — stdlib-only site contract."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, parse_qs
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = {'inthanon-signature': 'Inthanon Signature', 'dalmation': 'Dalmation', 'hamiqua': 'Hamiqua', 'rock-melon': 'Rock Melon', 'sweet-hamy': 'Sweet Hamy', 'sweet-lavender': 'Sweet Lavender'}

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.nodes, self.text = path, [], []
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))
    def handle_data(self, text):
        self.text.append(text)

def check():
    paths = [ROOT/'index.html'] + [ROOT/f'produk/{slug}.html' for slug in PRODUCTS]
    assert all(p.is_file() for p in paths), 'Missing website pages: ' + ', '.join(p.name for p in paths if not p.is_file())
    pages = {p: Page(p) for p in paths}
    titles, descriptions = set(), set()
    for path, page in pages.items():
        tags = [t for t, _ in page.nodes]
        assert tags.count('h1') == 1, f'{path.name}: one H1'
        assert all(tags.count(t) == 1 for t in ('header', 'main', 'footer')), f'{path.name}: landmarks'
        assert next(a for t,a in page.nodes if t=='html')['lang']=='id'
        ids = [a['id'] for _, a in page.nodes if 'id' in a]
        assert len(ids)==len(set(ids)), f'{path.name}: duplicate IDs'
        title = path.read_text(encoding='utf-8').split('<title>')[1].split('</title>')[0]
        description = next(a['content'] for t,a in page.nodes if t=='meta' and a.get('name')=='description')
        assert title not in titles and description not in descriptions, 'Metadata must be unique'
        titles.add(title); descriptions.add(description)
        links = [a['href'] for t,a in page.nodes if t=='a']
        assert 'tel:+6281398759898' in links
        wa = [urlsplit(x) for x in links if x.startswith('https://wa.me/')]
        assert wa and all(x.path=='/6285284992841' for x in wa)
        if path.parent.name=='produk':
            name = PRODUCTS[path.stem]
            expected = f'Halo GHI MELON, saya ingin menanyakan produk {name}.'
            assert any(parse_qs(x.query).get('text')==[expected] for x in wa), f'{path.name}: inquiry message'
            assert '../index.html#produk' in links
        assert all('defer' in a for t,a in page.nodes if t=='script' and 'src' in a)
        for tag, attrs in page.nodes:
            if tag=='img':
                assert all(k in attrs for k in ('alt','width','height')), f'{path.name}: image metadata'
                assert int(attrs['width'])>0 and int(attrs['height'])>0
            refs = [attrs[k] for k in ('href','src') if k in attrs]
            refs += [part.strip().split()[0] for part in attrs.get('srcset','').split(',') if part.strip()]
            for ref in refs:
                assert ref and ref!='#', f'{path.name}: empty link'
                u = urlsplit(ref)
                if u.scheme or u.netloc: continue
                assert not u.path.startswith('/'), f'{path.name}: root-relative path'
                target = (path.parent/unquote(u.path)).resolve() if u.path else path
                assert target.is_relative_to(ROOT) and target.is_file(), f'{path.name}: missing {ref}'
                assert target.suffix.lower()!='.pdf' and 'Product' not in target.parts, 'Source masters must not be public references'
                # Compare real spelling even on Windows case-insensitive filesystems.
                rel = target.relative_to(ROOT); current = ROOT
                for part in rel.parts:
                    assert part in {p.name for p in current.iterdir()}, f'Wrong case: {ref}'
                    current /= part
                if u.fragment:
                    assert target in pages and unquote(u.fragment) in {a.get('id') for _,a in pages[target].nodes}, f'{path.name}: missing anchor {ref}'
    home=pages[ROOT/'index.html']
    ids={a.get('id') for _,a in home.nodes}
    assert {'beranda','tentang','produk','layanan','proses','mutu','galeri','kemitraan','kontak','konten-utama'}<=ids
    hrefs={a.get('href') for t,a in home.nodes if t=='a'}
    assert all(f'produk/{slug}.html' in hrefs for slug in PRODUCTS)
    hashes=ROOT/'.work/source_hashes.json'
    if hashes.exists():
        for source,digest in json.loads(hashes.read_text()).items():
            assert hashlib.sha256((ROOT/source).read_bytes()).hexdigest()==digest, f'Source changed: {source}'
    print('PASS: 7 pages; metadata, landmarks, six varieties, links/assets/anchors, contacts and source integrity.')

if __name__=='__main__': check()
