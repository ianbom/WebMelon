from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import fitz, hashlib, json
root=Path(__file__).resolve().parents[1]
files=sorted((root/'Product').glob('*/*.png'))
manifest={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files+[root/'company_profile.pdf']}
(root/'.work/source_hashes.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
for folder in sorted((root/'Product').iterdir()):
    images=sorted(folder.glob('*.png'))
    sheet=Image.new('RGB',(310*len(images),600),'#eeeeee')
    d=ImageDraw.Draw(sheet)
    for i,p in enumerate(images):
        image=Image.open(p).convert('RGB'); image.thumbnail((300,550))
        sheet.paste(image,(i*310,35)); d.text((i*310+10,10),p.relative_to(root).as_posix(),fill='black')
    sheet.save(root/'.work'/f'{folder.name}.jpg')
doc=fitz.open(root/'company_profile.pdf')
for page_no in (0,6,12):
    page=doc[page_no]
    for item in page.get_images(full=True):
        xref=item[0]; data=doc.extract_image(xref)
        if data['width']>500:
            (root/'.work'/f'pdf-{page_no+1}-{xref}.{data["ext"]}').write_bytes(data['image'])
            print(page_no+1,xref,data['width'],data['height'])
print('Contact sheets: 26 images; source hashes recorded.')
