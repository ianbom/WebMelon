"""Run: python -I tests/check_product_photos.py — photo coverage and gallery contract."""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = {
    'dalmation': ('Dalmation', [1, 2, 3, 4, 5], 'detail-1-470.webp'),
    'rock-melon': ('Rock Melon', [1, 2, 3, 4, 5, 6], 'detail-1-420.webp'),
    'sweet-hamy': ('Sweet Hamy', [3, 1, 2, 4], 'detail-1-425.webp'),
    'sweet-lavender': ('Sweet Lavender', [5, 1, 2, 3, 4, 6], 'detail-1-800.webp'),
}


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.frames, self.buttons, self.cards, self.images, self.ids = [], [], [], [], []
        self.frame = self.card = None
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'figure' and 'data-gallery-image' in attrs:
            self.frame = attrs
        if tag == 'button' and 'data-gallery-thumb' in attrs:
            self.buttons.append(attrs)
        if tag == 'a' and set(attrs.get('class', '').split()) & {'product-card', 'related-card'}:
            self.card = attrs['href']
        if tag == 'img':
            self.images.append(attrs)
            if self.frame is not None:
                self.frames.append((self.frame['id'], attrs))
            if self.card is not None:
                self.cards.append((self.card, attrs))

    def handle_endtag(self, tag):
        if tag == 'figure':
            self.frame = None
        if tag == 'a':
            self.card = None


def check():
    paths = [ROOT / 'index.html', ROOT / 'katalog.html', *sorted((ROOT / 'produk').glob('*.html'))]
    total = 0
    for path in paths:
        page = Page(path)
        assert len(page.ids) == len(set(page.ids)), f'{path.name}: duplicate IDs'
        for image in page.images:
            assert image.get('alt'), f'{path.name}: missing alt'
            refs = [image['src']] + [item.strip().split()[0] for item in image.get('srcset', '').split(',') if item.strip()]
            for ref in refs:
                assert (path.parent / ref).is_file(), f'{path.name}: missing {ref}'
        for href, image in page.cards:
            slug = Path(href).stem
            if slug in PRODUCTS:
                cover = PRODUCTS[slug][1][0]
                assert image['src'].endswith(f'/{slug}/foto-baru-{cover}-800.webp'), f'{path.name}: stale cover {slug}'
        if path.parent.name != 'produk':
            continue
        total += len(page.frames)
        if path.stem not in PRODUCTS:
            assert len(page.frames) == (1 if path.stem == 'inthanon-signature' else 2)
            assert page.frames[0][0] == 'foto-utama'
            continue
        name, order, old_detail = PRODUCTS[path.stem]
        sources = {int(p.stem) for p in (ROOT / 'Melon' / name).glob('*.png')}
        assert sources == set(order), f'{name}: source coverage changed'
        ids = [frame_id for frame_id, _ in page.frames]
        assert ids == [f'foto-baru-{n}' for n in order] + ['foto-utama', 'foto-detail'], f'{name}: wrong gallery order/coverage'
        assert [b['data-image'] for b in page.buttons] == ids, f'{name}: thumbnail pairing'
        assert all(b['aria-controls'] == b['data-image'] for b in page.buttons)
        assert [b['aria-pressed'] for b in page.buttons] == ['true'] + ['false'] * (len(ids) - 1)
        assert len({b['aria-label'] for b in page.buttons}) == len(ids), f'{name}: duplicate labels'
        for (_, image), n in zip(page.frames, order):
            assert image['src'].endswith(f'/{path.stem}/foto-baru-{n}-800.webp')
            assert f'foto-baru-{n}-480.webp 480w' in image['srcset']
        old_main = 'utama-461.webp' if path.stem == 'sweet-lavender' else 'utama-800.webp'
        assert page.frames[-2][1]['src'].endswith('/' + old_main)
        assert page.frames[-1][1]['src'].endswith('/' + old_detail)
        assert page.frames[0][1].get('fetchpriority') == 'high'
        assert all(img.get('loading') == 'lazy' and 'fetchpriority' not in img for _, img in page.frames[1:])
        print(f'PASS: {name}: {len(order)} new + 2 existing photos')
    assert total == 32, f'Expected 32 photos, got {total}'
    print('PASS: 32 gallery photos, covers, local assets and thumbnail pairing.')


if __name__ == '__main__':
    check()
