from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
p=root/'implementation.md'; text=p.read_text(encoding='utf-8')
# Mark only implementation stages actually exercised; leave launch/data confirmations open.
start=text.index('### Tahap 2 —'); end=text.index('### Tahap 6 —')
text=text[:start]+text[start:end].replace('- [ ]','- [x]')+text[end:]
text=text.replace('Pada tahap implementasi nanti, jalankan server statis dari direktori website, misalnya `python -m http.server 8000` jika Python tersedia. Buka `http://localhost:8000/`; jangan hanya menguji `file://`.','Preview lokal: `python -I -m http.server 8000 --bind 127.0.0.1`, buka `http://127.0.0.1:8000/`. Server pengembangan hanya loopback; jangan deploy seluruh direktori sumber.')
rows=json.loads((root/'.work/assets.json').read_text())
table='\n'.join(f'| `{r["path"]}` | '+('PDF h.7 xref189' if r['slug']=='inthanon-signature' else '`'+r['source']+'`')+f' | `{tuple(r["box"])}` | {r["width"]}×{r["height"]} | {r["bytes"]:,} |' for r in rows)
append='''
## 14. Hasil Implementasi Lokal — 6 November 2026

### 14.1 Berkas dan keputusan implementasi

- Tersedia `index.html`, enam `produk/*.html`, `assets/css/styles.css`, `assets/js/main.js`.
- HTML lengkap; header/main/footer terpisah secara semantik. Tidak ada runtime fetch, framework, backend, atau instalasi dependency aplikasi.
- Body Arial menggantikan Satoshi. Heading Libre Caslon Text melalui Google Fonts, `display=swap`, fallback Georgia. Saat offline seluruh isi tetap tersedia dengan fallback; font online menghubungi Google.
- Wordmark navbar berbentuk teks, bukan logo baru yang diklaim resmi. Logo diekstrak menjadi `assets/images/brand/logo.webp`, tidak dipaksakan ke kapsul navbar.
- Hero close-up Inthanon dari PDF, bukan foto kebun atau greenhouse. Berkas 640×372 dan1024×595; tidak dibuat upscale. Keterbatasan detail mengikuti resolusi sumber. Foto landscape asli menjadi peningkatan berikutnya.
- Inthanon satu foto; lima varietas lain masing-masing dua foto berbeda. Seluruh teks poster/tag/badge dibuang dari crop fisik terpilih; sumber master tidak diedit.
- Inventaris awal dikoreksi setelah audit ulang seluruh26 gambar. Nama Sweet Lavender mengikuti PDF; gambar bertag Sweet Net Lavender tidak dipakai. Brix/nutrisi/rasa/berat/harga/stok/sertifikasi tidak dicantumkan.
- Header/footer sengaja duplikat pada tujuh HTML untuk ketahanan tanpa JavaScript; perubahan bersama perlu disinkronkan manual.
- `.work/` menyimpan script authoring, hash sumber dan bukti audit lokal; bukan kebutuhan runtime atau file publik.

### 14.2 Pemetaan turunan final

Kotak crop menggunakan koordinat sumber `(left, top, right, bottom)`. Semua resize turun atau sama dengan crop, tidak meng-upscale.

| Turunan | Sumber | Crop | Dimensi | Bytes |
|---|---|---|---|---|
'''+table+'''

Hero memakai crop Inthanon yang sama, bukan foto galeri kedua. Logo PDF h.1 xref6 diturunkan ke maksimum600×400.

### 14.3 Hasil verifikasi yang benar-benar dijalankan

| Pemeriksaan | Hasil |
|---|---|
| `python -I tests/check_site.py` | PASS:7 halaman; metadata unik; lang/H1/landmark; kontak dan pesan produk; enam URL; href/src/srcset/fragment; kapitalisasi path; SHA256 PDF+26 PNG tidak berubah. |
| `node --check assets/js/main.js` | PASS, exit0. |
| `tests/browser_checks.js` via Playwright MCP | PASS35 kombinasi halaman/viewport360/390/768/1024/1440, tanpa overflow. |
| Menu keyboard | PASS Enter/Space, Escape mengembalikan fokus, link katalog, resize breakpoint tidak kehilangan fokus. |
| Galeri | PASS pilihan foto/aria-pressed/hidden, reload mengembalikan foto utama. |
| JavaScript disabled | PASS navigasi dan seluruh foto statis pada7 halaman di390px. |
| Reduced motion | PASS computed `scroll-behavior:auto`. |
| Subfolder `/Melon/` | PASS6 detail direct/refresh/kembali katalog, tanpa404. |
| Console/network selama suite | Tidak ada pageerror atau responsHTTP≥400. |
| Visual | Hero390/1440, katalog desktop/mobile, detail mobile, CTA/footer ditinjau melalui screenshot; susunan kapsul/serif/panel2+3 mengikuti referensi, bukan salinan gambar Solune. |
| Accessibility tree | Landmark, heading, label menu/thumbnail/status diperiksa pada detail. Screen reader nyata belum diuji. |
| Lighthouse/Core Web Vitals | Belum diukur; Lighthouse tidak tersedia dalam tooling global. Tidak mengklaim target skor/LCP/CLS/INP tercapai. |

Menjalankan browser suite memerlukan Playwright MCP yang tersedia di lingkungan pengembangan. Script berisi fungsi `async(page)` untuk `browser_run_code_unsafe({filename:'tests/browser_checks.js'})`; tidak memerlukan framework proyek.

### 14.4 Batas peluncuran

Belum ada deployment, domain/canonical/sitemap produksi, verifikasi registri legal independen, atau pengiriman pesan WhatsApp. Hanya tautan native yang disiapkan. Konfirmasi komersial dan izin publikasi tetap mengikuti bagian13.

Saat deployment disetujui, unggah **hanya** `index.html`, `produk/*.html`, dan `assets/` yang diperlukan. Jangan unggah `Product/`, PDF, `.work/`, `tests/`, screenshot, atau dokumen internal. Server Python ini adalah preview, bukan server produksi.
'''
text+=append
p.write_text(text,encoding='utf-8')
print('Updated implementation status, source inventory and 18 asset mappings; launch confirmations remain open.')
