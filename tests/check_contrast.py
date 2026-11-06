"""Check rendered text backgrounds captured by capture_contrast.js (Pillow already installed)."""
from pathlib import Path
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

def luminance(color):
    return sum(weight * (value / 3294.6 if value <= 10.31475 else ((value / 255 + .055) / 1.055) ** 2.4)
               for weight, value in zip((.2126, .7152, .0722), color))

failures = []
for sample in json.loads((ROOT / '.work/contrast.json').read_text()):
    image = Image.open(ROOT / sample['file']).convert('RGB')
    for rect in sample['rects']:
        foreground = rect['color'][:3]
        alpha = rect['color'][3] if len(rect['color']) > 3 else 1
        ratios = []
        for background in image.crop(rect['box']).getdata():
            text = [alpha * f + (1-alpha) * b for f, b in zip(foreground, background)]
            a, b = sorted((luminance(text), luminance(background)))
            ratios.append((b + .05) / (a + .05))
        ratio = min(ratios)
        print(f"{sample['file']} {rect['box']}: {ratio:.2f}:1 (minimum {rect['minimum']}:1)")
        if ratio < rect['minimum']:
            failures.append((sample['file'], rect['box'], round(ratio, 2)))
assert not failures, f'Contrast failed: {failures}'
print('PASS: conservative full text rectangles, hero/cards at 390 and 1440px.')
