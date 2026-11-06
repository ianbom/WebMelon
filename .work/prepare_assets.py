from pathlib import Path
from PIL import Image, ImageDraw
import json
root=Path(__file__).resolve().parents[1]
# Rectangles remove poster headings, badges and claims, including attached labels.
selections={
'inthanon-signature': [('.work/pdf-7-189.jpeg',(0,620,1024,1215))],
'dalmation': [('Product/Dalmation/3.png',(0,870,941,1290)),('Product/Dalmation/2.png',(460,790,930,1460))],
'hamiqua': [('Product/Hamiqua/3.png',(0,1000,941,1600)),('Product/Hamiqua/2.png',(215,1125,930,1455))],
'rock-melon': [('Product/Rock Melon/4.png',(0,1080,941,1580)),('Product/Rock Melon/6.png',(510,800,930,1460))],
'sweet-hamy': [('Product/Sweet Hamy/4.png',(0,1000,941,1610)),('Product/Sweet Hamy/3.png',(505,900,930,1490))],
'sweet-lavender': [('Product/Sweet Lavender/5.png',(480,930,941,1510)),('Product/Sweet Lavender/6.png',(0,1090,941,1600))]
}
rows=[]
for slug,items in selections.items():
    folder=root/'assets/images/products'/slug; folder.mkdir(parents=True,exist_ok=True)
    for i,(source,box) in enumerate(items):
        image=Image.open(root/source).convert('RGB').crop(box)
        name='utama' if i==0 else 'detail-1'
        for width in sorted({min(480,image.width),min(800,image.width)}):
            height=round(image.height*width/image.width)
            target=folder/f'{name}-{width}.webp'
            image.resize((width,height),Image.Resampling.LANCZOS).save(target,'WEBP',quality=86,method=6)
            rows.append({'slug':slug,'source':source,'box':box,'path':target.relative_to(root).as_posix(),'width':width,'height':height,'bytes':target.stat().st_size})
# The hero uses an existing clean Inthanon fruit crop; no invented landscape.
hero=root/'assets/images/hero'; hero.mkdir(parents=True,exist_ok=True)
image=Image.open(root/'.work/pdf-7-189.jpeg').convert('RGB').crop((0,620,1024,1215))
for width in (640,1024):
    image.resize((width,round(image.height*width/image.width)),Image.Resampling.LANCZOS).save(hero/f'melon-{width}.webp','WEBP',quality=88,method=6)
brand=root/'assets/images/brand'; brand.mkdir(parents=True,exist_ok=True)
Image.open(root/'.work/pdf-1-6.jpeg').convert('RGB').thumbnail((600,400)) if False else None
logo=Image.open(root/'.work/pdf-1-6.jpeg').convert('RGB'); logo.thumbnail((600,400)); logo.save(brand/'logo.webp','WEBP',quality=90)
(root/'.work/assets.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
# Show actual complete crops, not CSS-masked posters.
large=[r for r in rows if r['width']==max(x['width'] for x in rows if x['slug']==r['slug'] and ('utama' in x['path'])==('utama' in r['path']))]
sheet=Image.new('RGB',(1200,((len(large)+2)//3)*320),'#eff5e4'); draw=ImageDraw.Draw(sheet)
for i,r in enumerate(large):
    image=Image.open(root/r['path']); image.thumbnail((390,280)); x=(i%3)*400; y=(i//3)*320
    draw.text((x+8,y+5),r['slug']+(' utama' if 'utama' in r['path'] else ' detail'),fill='black'); sheet.paste(image,(x,y+30))
sheet.save(root/'.work/crops.jpg')
print(f'{len(rows)} product derivatives; max {max(r["bytes"] for r in rows)} bytes; no upscale.')
