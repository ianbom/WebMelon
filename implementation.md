# Rencana Implementasi Website Green House Indonesia & GHI MELON

**Perusahaan:** PT GHI Makmur Indonesia  
**Tujuan:** Website company profile sekaligus katalog produk melon.  
**Teknologi:** HTML5 semantik, CSS native, JavaScript vanilla.  
**Referensi desain:** https://solune.framer.website/  
**Status:** Implementasi lokal tersedia: beranda, katalog, tentang kami, kontak, dan enam detail produk (sepuluh HTML), menggunakan HTML/CSS/JavaScript native. Riwayat implementasi awal tercatat pada bagian 14; perluasan tiga halaman pada bagian 15. Belum dipublikasikan/deploy.

## 1. Konteks dan Ruang Lingkup

Website memperkenalkan PT GHI Makmur Indonesia, kegiatan greenhouse dan agribisnis terintegrasi, enam varietas GHI MELON, serta peluang kerja sama. Pengunjung dapat memahami perusahaan, mengenali produk, lalu menghubungi perusahaan melalui telepon atau WhatsApp.

Prioritas:
1. Tampilan sangat dekat dengan karakter visual Solune, bukan template katalog generik.
2. Materi perusahaan dan foto menggunakan sumber milik pengguna, bukan konten atau foto Solune.
3. Informasi produk akurat; keterbatasan data tidak diisi dengan klaim rekaan.
4. Header, konten utama, dan footer terpisah secara semantik dan visual.
5. Website ringan, responsif, mudah diperbarui, dan tetap berguna tanpa JavaScript.

Cakupan terbaru atas permintaan pengguna: **satu beranda, tiga halaman mandiri (katalog produk, tentang kami, kontak), dan enam detail produk**. Bagian produk/profil/kontak pada beranda tetap tersedia; navigasi umum menuju halaman mandiri.

Tidak termasuk: transaksi online, keranjang, checkout, pembayaran, akun, stok real-time, dashboard admin, database, CMS, newsletter, blog, backend formulir, atau deployment otomatis. Penyusunan dokumen dilanjutkan menjadi implementasi website atas permintaan pengguna. Deployment tetap di luar cakupan.

## 2. Sumber dan Hasil Pemeriksaan

### 2.1 Kondisi awal

- Belum ada website atau kode aplikasi di direktori proyek.
- `company_profile.pdf`: **13 halaman**, seluruh halaman telah dibaca.
- `Product/`: **26 gambar PNG**, seluruhnya telah diperiksa secara visual.
- Total ukuran 26 PNG: **62.932.157 bytes**, sekitar 60 MiB. Tidak ditemukan duplikat file identik berdasarkan SHA-256.
- Referensi Solune diperiksa pada desktop 1440px, ponsel 390px, serta halaman detail program.
- PDF menyebut **enam varietas**, sedangkan folder `Product/` hanya mencakup **lima varietas**. Inthanon Signature tetap masuk katalog menggunakan aset dari PDF.

### 2.2 Pemetaan seluruh halaman PDF

| Halaman | Materi sumber | Penggunaan di website |
|---|---|---|
| 1 | Identitas PT GHI Makmur Indonesia; agribisnis melon hidroponik dari hulu ke hilir | Hero, pengantar, positioning perusahaan |
| 2 | Profil; greenhouse, produksi, pascapanen, pemasaran; arsitektur merek | Tentang perusahaan dan cakupan bisnis |
| 3 | Visi, enam misi, nilai kualitas/integritas/inovasi/kemitraan | Tentang, nilai, rincian misi |
| 4 | Enam tahap bisnis terintegrasi | Bagian proses hulu ke hilir |
| 5 | Layanan pembangunan greenhouse dan empat tahapan proyek | Layanan dan CTA konsultasi |
| 6 | Proses produksi hidroponik; data kapasitas dan sertifikasi belum tersedia | Budidaya dan prinsip operasional |
| 7 | Inthanon Signature sebagai produk fokus; spesifikasi aktual perlu konfirmasi | Produk unggulan dan detail Inthanon |
| 8 | Daftar enam varietas | Katalog dan navigasi produk |
| 9 | Kerangka pengendalian mutu yang disarankan, merek, batasan klaim | Mutu dan aturan editorial |
| 10 | Kanal pemasaran dan distribusi | Kebutuhan pembeli dan peluang distribusi |
| 11 | Bentuk kerja sama potensial; prinsip jelas, terukur, adil | Kemitraan |
| 12 | Legalitas, alamat kantor, NIB, akta, pengesahan, KBLI | Identitas dan legalitas ringkas |
| 13 | Let's Grow Together; telepon, WhatsApp, alamat | Kontak dan footer |

### 2.3 Identitas perusahaan dan merek

| Nama | Peran menurut PDF h.2 dan h.9 | Penempatan |
|---|---|---|
| PT GHI Makmur Indonesia | Badan usaha | Tentang, legalitas, kontak, footer |
| Green House Indonesia | Identitas kegiatan greenhouse dan pertanian modern | Identitas navigasi dan layanan |
| GHI MELON | Identitas merek produk melon | Katalog dan halaman produk |

Gunakan logo resmi yang diekstrak dari PDF apabila hasilnya layak. Jika lockup terlalu panjang untuk navigasi, gunakan wordmark teks yang jelas; jangan merancang simbol baru lalu menyatakannya sebagai logo resmi.

### 2.4 Kontak terverifikasi dari sumber

| Data | Nilai | Implementasi |
|---|---|---|
| Telepon | 0813-9875-9898 | `tel:+6281398759898` |
| WhatsApp | 085284992841 | `https://wa.me/6285284992841` |
| Kantor | VIP Office, AD Premier Lantai 5 Suite 6, Jalan TB Simatupang No. 5, Ragunan, Pasar Minggu, Jakarta Selatan 12550 | Teks alamat berlabel **Alamat Kantor** |
| Email | Tidak tercantum | Jangan tampilkan email tebakan |
| Domain resmi | Tidak tercantum | Tetapkan saat domain sebenarnya tersedia |
| Media sosial | Tidak tercantum | Jangan menambahkan tautan generik |

Telepon dan WhatsApp menggunakan **nomor berbeda**. Alamat kantor bukan bukti lokasi kebun atau greenhouse. Tidak perlu embed peta agar halaman tetap ringan; tautan pencarian alamat dapat ditambahkan setelah tujuan diperiksa.

### 2.5 Legalitas untuk ringkasan perusahaan

Berdasarkan PDF h.12, bukan verifikasi independen terhadap registri pemerintah:

- NIB **1009260116962**, diterbitkan **10 September 2026**.
- Pengesahan **AHU-0072967.AH.01.01.TAHUN 2026**, ditetapkan **9 September 2026**.
- Akta pendirian **No. 106**, tanggal **8 September 2026**.
- Status modal **PMDN**; skala kegiatan pada NIB **Usaha Mikro**.
- Kedudukan **Jakarta Selatan, DKI Jakarta**.
- KBLI **01132 — Pertanian Buah Semusim**, **46312 — Perdagangan Besar Buah-buahan**, **41019 — Konstruksi Konvensional Gedung Lainnya**.

Footer cukup menampilkan badan usaha, alamat, dan NIB. Rincian lain dapat diletakkan dalam disclosure legalitas pada bagian Tentang. Tidak perlu mengekspos dokumen legal lengkap atau identitas notaris sebagai materi pemasaran. Unduhan PDF publik tidak diaktifkan tanpa persetujuan tersendiri.

## 3. Inventaris Seluruh Gambar Produk

Path berikut relatif terhadap direktori proyek. Pilihan penggunaan merupakan rekomendasi desain, **bukan pernyataan semua gambar sudah siap dipublikasikan**. Foto dengan teks bermasalah harus lolos audit/crop atau mendapat versi koreksi.

| No. | Path sumber | Dimensi | Isi visual dan rekomendasi |
|---|---|---|---|
| 1 | `Product/Dalmation/1.png` | 941×1672 | Dua buah utuh di meja outdoor; poster bertulisan Brix. Kandidat galeri setelah audit. |
| 2 | `Product/Dalmation/2.png` | 941×1670 | Outdoor, dua buah utuh; badge 14 UP. Crop buah kanan untuk foto tambahan. |
| 3 | `Product/Dalmation/3.png` | 941×1672 | Outdoor, buah utuh, belahan dan irisan krem; badge 14 UP. Crop potongan buah untuk foto utama. |
| 4 | `Product/Dalmation/4.png` | 941×1672 | Studio putih, dua buah utuh dengan callout dan 14 Brix UP. |
| 5 | `Product/Dalmation/5.png` | 941×1672 | Studio putih, buah utuh, belahan, irisan dan callout; 14 Brix UP. |
| 6 | `Product/Hamiqua/1.png` | 1122×1402 | Buah lonjong di tatakan kayu, callout; satu-satunya rasio sekitar 4:5. |
| 7 | `Product/Hamiqua/2.png` | 941×1672 | Studio putih, buah utuh dan irisan oranye, callout. Crop irisan bawah untuk foto tambahan. |
| 8 | `Product/Hamiqua/3.png` | 941×1672 | Outdoor, buah utuh dan irisan; crop bawah untuk foto utama. |
| 9 | `Product/Hamiqua/4.png` | 941×1672 | Outdoor, buah utuh tanpa irisan. |
| 10 | `Product/Hamiqua/5.png` | 941×1672 | Editorial dekat jendela, buah utuh dan irisan, teks kanan. |
| 11 | `Product/Rock Melon/1.png` | 941×1672 | Dua buah di atas alas bambu/marmer; klaim 12°Bx UP. |
| 12 | `Product/Rock Melon/2.png` | 941×1672 | Studio, buah utuh, belahan dan irisan; klaim 12 UP. |
| 13 | `Product/Rock Melon/3.png` | 941×1672 | Studio putih, satu buah utuh; klaim 12 UP. |
| 14 | `Product/Rock Melon/4.png` | 941×1672 | Outdoor, buah utuh, belahan dan irisan; klaim 14 UP. Crop bawah untuk foto utama. |
| 15 | `Product/Rock Melon/5.png` | 941×1672 | Editorial dekat jendela, buah utuh dan potongan; klaim 12 UP. Tidak digunakan. |
| 16 | `Product/Rock Melon/6.png` | 941×1672 | Dua buah di meja outdoor; badge 14 UP berkonflik. |
| 17 | `Product/Sweet Hamy/1.png` | 941×1672 | Dua buah lonjong studio, callout; klaim 14–17°Bx perlu konfirmasi. |
| 18 | `Product/Sweet Hamy/2.png` | 941×1672 | Buah utuh, belahan, irisan/dadu studio; kandidat detail setelah audit. |
| 19 | `Product/Sweet Hamy/3.png` | 941×1672 | Dua buah lonjong di teras kebun; kandidat kartu melalui crop aman. |
| 20 | `Product/Sweet Hamy/4.png` | 941×1672 | Buah, belahan, irisan dan mint dekat jendela; kandidat detail editorial. |
| 21 | `Product/Sweet Lavender/1.png` | 941×1672 | Dua buah kuning emas studio; callout salah menyebut kulit hijau gelap. Jangan tampilkan teks keliru. |
| 22 | `Product/Sweet Lavender/2.png` | 941×1671 | Studio putih, buah kuning, belahan dan irisan; tag Sweet Lavender. |
| 23 | `Product/Sweet Lavender/3.png` | 941×1672 | Outdoor, buah utuh, belahan dan irisan; tag Sweet Net Lavender. Tidak digunakan. |
| 24 | `Product/Sweet Lavender/4.png` | 941×1672 | Satu buah kuning outdoor; tag Sweet Net Lavender. Tidak digunakan. |
| 25 | `Product/Sweet Lavender/5.png` | 941×1672 | Outdoor, dua buah kuning; tag Sweet Lavender. Crop buah kanan untuk foto utama. |
| 26 | `Product/Sweet Lavender/6.png` | 941×1672 | Editorial dekat jendela, buah utuh, belahan dan irisan; tag Sweet Lavender. Crop bawah untuk foto tambahan. |

Ringkasan: Dalmation **5**, Hamiqua **5**, Rock Melon **6**, Sweet Hamy **4**, Sweet Lavender **6**. Total **26**.

### Aset tambahan dalam PDF

- **Inthanon Signature:** poster 1024×1536 pada h.7; versi lain pada h.8. Ekstrak gambar tertanam, bukan screenshot seluruh halaman. Referensi pemeriksaan saat ini: xref 189 pada h.7 dan xref 491 pada h.8; temukan ulang jika PDF berubah.
- Poster Inthanon menampilkan buah bulat dengan tangkai T, tulisan GHI MELON PREMIUM dan Inthanon Signature. Tidak ada angka Brix. Teks promosi rasa/tekstur/nutrisi harus diaudit sebelum dipakai sebagai spesifikasi.
- **Logo perusahaan:** aset landscape h.1 sekitar 1200×800 dan h.13 sekitar 1109×740 merupakan lockup/logo dengan latar polos. Bukan foto greenhouse atau dokumentasi fasilitas.
- Tidak tersedia foto landscape fasilitas yang telah teridentifikasi sebagai dokumentasi perusahaan. Jangan mengganti kekurangan ini dengan foto stok yang seolah menunjukkan kebun milik perusahaan.

## 4. Aturan Konten dan Konflik Sumber

### 4.1 Hirarki penggunaan sumber

1. Identitas, kontak, ruang lingkup bisnis, dan daftar varietas mengikuti PDF.
2. Gambar `Product/` menjadi sumber visual serta catatan klaim materi promosi, bukan otomatis spesifikasi komersial tervalidasi.
3. Rasa, tekstur, ukuran, Brix, berat, masa simpan, ketersediaan dan harga hanya dicantumkan sebagai spesifikasi setelah pemilik mengonfirmasi data aktual yang relevan.
4. Materi usulan seperti headline dan label CTA ditandai sebagai copy rekomendasi, bukan kutipan resmi PDF.

### 4.2 Konflik yang harus dicatat

| Temuan | Keputusan rancangan |
|---|---|
| PDF berisi enam varietas; folder hanya lima | Tetap tampilkan Inthanon Signature dari PDF; jangan menggantinya dengan foto varietas lain. |
| Ejaan “Dalmation” | Pertahankan ejaan sumber; jangan otomatis menjadi “Dalmatian”. |
| Sweet Lavender versus tag Sweet Net Lavender | Nama katalog mengikuti PDF; catat variasi tag untuk konfirmasi pemilik. |
| Rock Melon 12 UP pada gambar 1/2/3/5, 14 UP pada 4/6 | Tahan angka Brix. Jangan membuat rentang 12–14 sebagai kompromi karena itu bukan spesifikasi yang diberikan sumber. |
| Dalmation 14 UP, Hamiqua 12–14, Sweet Hamy/Lavender 14–17 pada poster | Catat di dokumen internal; jangan otomatis mengubahnya menjadi spesifikasi publik sebelum konfirmasi aktual. |
| Sweet Lavender/1.png salah deskripsi kulit | Hindari versi penuh; gunakan crop buah yang aman atau minta koreksi. |
| Inventaris awal salah memetakan beberapa komposisi dan klaim gambar | Tabel bagian 3 telah dikoreksi berdasarkan audit contact sheet seluruh 26 gambar. Klaim typo Rock Melon/5 dari inventaris awal tidak digunakan karena belum terverifikasi. |

Konfirmasi Brix tidak otomatis memerlukan uji laboratorium untuk setiap nilai; gunakan konfirmasi pemilik dan bukti pengukuran yang sesuai. Klaim nutrisi, sertifikasi, organik atau bebas residu memerlukan dasar bukti sesuai jenis klaim, mengikuti batasan PDF h.9.

**Menghapus klaim dari HTML tidak cukup jika klaim masih terbaca pada gambar.** Crop boleh membuang area teks/badge tanpa merusak buah. Jika tidak memungkinkan, tahan gambar bermasalah sampai tersedia revisi. Jangan memalsukan label, mengganti varietas, atau memakai retouch generatif untuk mengarang aset.

Tidak wajib memublikasikan seluruh 26 poster. Seluruhnya sudah ditinjau; hanya foto yang layak dan relevan yang digunakan.

### 4.3 Bahasa yang tidak boleh diubah menjadi pencapaian

PDF memuat tujuan pengembangan, kerangka mutu yang disarankan, kanal pemasaran, serta bentuk kerja sama potensial. Pertahankan makna tersebut.

- “Menargetkan pengembangan” bukan “telah menjadi produsen terbesar”.
- Kanal retail/horeca bukan bukti daftar klien aktif.
- Kerangka pengendalian mutu bukan sertifikasi resmi.
- Jangan membuat statistik kapasitas panen, jumlah mitra, rating, ulasan pelanggan, logo klien, atau status terlaris.
- Slogan “NATURALLY GROWN” tidak disamakan dengan sertifikasi organik. Audit konteks klaim, bukan membuat kesimpulan hukum yang tidak dibuktikan.

## 5. Arah Desain: Adaptasi Solune

### 5.1 Ciri referensi yang dipertahankan

- Navbar putih mengambang berbentuk kapsul dengan CTA hijau gelap dan ikon panah bundar.
- Hero foto besar mendekati tinggi viewport, inset tipis, sudut membulat, overlay gelap, judul serif putih.
- Judul editorial berukuran besar; body sans-serif sederhana.
- Section putih dan hijau pucat bergantian dengan ruang kosong lega.
- Label kecil berbentuk kapsul, kartu radius lembut, border tipis, minim bayangan berat.
- Komposisi lima kartu program Solune: dua kartu horizontal di atas, tiga kartu vertikal di bawah.
- Footer lapang dengan identitas, navigasi, dan kontak.

Yang tidak dipindahkan: logo/nama Solune, foto yoga atau gunung, copy wellness, harga kelas, jadwal, instruktur, testimoni, newsletter, badge Framer, kode internal template, dan panjang halaman yang tidak relevan.

### 5.2 Token desain

| Token | Nilai rancangan |
|---|---|
| Teks dan hijau utama | `#121C03` |
| Latar putih | `#FFFFFF` |
| Panel hijau pucat | `#F4FAE8` |
| Panel hijau alternatif | `#EFF5E4` |
| Border/aksen lembut | `#E6EDD5` |
| Heading | Libre Caslon Text, fallback Georgia/serif |
| Body | Satoshi, fallback Arial/sans-serif |
| H1 desktop / ponsel | Sekitar 72px / 36px |
| H2 desktop / ponsel | Sekitar 48px / 26px |
| Body | 16–18px; line-height sekitar 1.5–1.65 |
| Konten desktop | Maksimum 1120px dalam wrapper 1200px dengan padding 40px |
| Navbar desktop | Maksimum 920px, tinggi sekitar 64px, offset atas 20px |
| Navbar ponsel | Tinggi minimum sekitar 54px; tinggi bertambah ketika menu dibuka |
| Radius hero/kartu | Sekitar 20px |
| Radius tombol/label | Kapsul |
| Padding section desktop | Sekitar 100px vertikal |
| Heading ke isi section | Sekitar 60px desktop |
| Gutter ponsel | Minimum 16px |
| Padding section ponsel | Sekitar 56–64px vertikal |

Ukuran merupakan acuan komposisi, bukan alasan memotong teks demi tinggi tetap. Gunakan CSS custom properties, `clamp()`, Grid, dan Flexbox. Font hanya dimuat jika tersedia dengan lisensi sesuai; bila Satoshi diganti, catat substitusinya. Jangan mengambil file font tanpa izin dari hosting referensi.

### 5.3 Responsif

Breakpoint rekomendasi implementasi, bukan klaim breakpoint internal Solune:

- **Di bawah 768px:** satu kolom, menu disclosure, hero portrait-friendly, kartu tanpa pemaksaan orientasi horizontal.
- **768–1023px:** dua kolom jika ruang cukup; seluruh teks dan gambar tetap terbaca.
- **Mulai 1024px:** komposisi desktop dan grid dua-plus-tiga.

Pada desktop 1440px, dua kartu atas sekitar 555px; tiga kartu bawah sekitar 367px, gap sekitar 10px. Ukuran mengecil mengikuti container. Pertahankan rasio gambar secara proporsional, bukan menyalin ukuran tetap di seluruh layar.

## 6. Struktur Beranda dan Pemetaan Konten

Urutan section berikut merupakan rekomendasi desain, bukan transkripsi urutan PDF.

| Bagian / ID | Isi | Rancangan visual dan sumber |
|---|---|---|
| Header | Identitas, Tentang, Produk, Layanan, Kemitraan, Hubungi Kami | Navbar mengambang seperti Solune; logo/wordmark lokal. |
| Hero / `#beranda` | Positioning perusahaan, CTA Jelajahi Produk | Foto lokal besar, overlay gelap, heading serif putih. PDF h.1–2. |
| Tentang / `#tentang` | Profil, tiga identitas merek, visi, nilai | Panel hijau pucat; narasi editorial, empat nilai dalam kartu ringkas. PDF h.2–3. |
| Produk / `#produk` | Inthanon Signature, lalu lima varietas lainnya | Blok signature terpisah, diikuti komposisi kartu dua-plus-tiga. PDF h.7–8. |
| Layanan / `#layanan` | Greenhouse, produksi, pascapanen, pemasaran | Kartu ringkas; detail layanan greenhouse dalam disclosure. PDF h.2 dan h.5. |
| Proses / `#proses` | Enam tahap hulu ke hilir | Daftar bernomor 01–06, bukan statistik bisnis. PDF h.4. |
| Budidaya dan Mutu / `#mutu` | Prinsip kerja, tahapan produksi, arah pengendalian mutu | Panel hijau-putih dengan poin singkat; tidak mengesankan sertifikasi. PDF h.6 dan h.9. |
| Galeri / `#galeri` | Pilihan foto produk yang lolos audit | Komposisi editorial membulat; jangan dilabeli dokumentasi kebun. |
| Kemitraan / `#kemitraan` | Kanal pembeli dan kerja sama potensial | Teks pengantar, daftar opsi, prinsip jelas/terukur/adil, CTA diskusi. PDF h.10–11. |
| Kontak / `#kontak` | Let's Grow Together, alamat kantor, telepon, WhatsApp | CTA besar seperti penutup Solune; kanal kontak native. PDF h.13. |
| Footer | Badan usaha, merek, navigasi ringkas, alamat, NIB | Lapang, sederhana; bukan salinan legal/footer Solune. PDF h.9, h.12–13. |

### 6.1 Copy awal yang direkomendasikan

Copy berikut usulan editorial berbasis sumber, bukan kutipan baru yang dianggap sudah disetujui perusahaan:

- Label hero: **Green House Indonesia · GHI MELON**.
- H1: **Melon hidroponik, terintegrasi dari hulu ke hilir.**
- Pengantar: **PT GHI Makmur Indonesia mengembangkan agribisnis melon melalui greenhouse, budidaya hidroponik, penanganan pascapanen, dan pemasaran yang terintegrasi.**
- CTA utama: **Jelajahi Produk** menuju `#produk`.
- CTA navbar/kontak: **Hubungi Kami** menuju `#kontak`.
- Judul katalog: **Kenali pilihan melon GHI MELON.**
- Judul kerja sama: **Tumbuh bersama melalui kemitraan yang jelas.**
- CTA kemitraan: **Diskusikan Kemitraan** melalui WhatsApp.

Visi dapat memakai rumusan PDF h.3. Enam misi tetap terakomodasi melalui `<details>` agar halaman tidak dipenuhi teks panjang. Empat nilai: Kualitas, Integritas, Inovasi, Kemitraan.

### 6.2 Hero dan batasan aset

Pilihan implementasi: close-up bersih Inthanon Signature dari gambar tertanam PDF h.7, crop `(0,620,1024,1215)`. Hamiqua/2 ternyata poster studio, bukan landscape seperti inventaris awal. Preview hero diperiksa pada desktop 1440px dan ponsel 390px. Hero memakai close-up editorial, bukan dokumentasi kebun; keterbatasan resolusi sumber tetap berlaku.

Sumber portrait hanya 941px lebar; crop landscape mengurangi detail lebih jauh. Jangan memperbesar lalu mengklaim hasil setajam foto landscape 2K. Jika crop tidak layak, gunakan foto portrait lokal di atas panel hijau dengan navbar, tipografi, CTA, dan radius khas Solune. Catat kompromi; foto landscape asli dari pemilik menjadi peningkatan berikutnya. Jangan memakai logo PDF sebagai foto greenhouse.

## 7. Katalog dan Halaman Detail Produk

### 7.1 Pemetaan enam varietas

| Produk | URL | Visual awal | Posisi beranda |
|---|---|---|---|
| Inthanon Signature | `produk/inthanon-signature.html` | Ekstraksi gambar PDF h.7 | Blok unggulan sebelum grid |
| Dalmation | `produk/dalmation.html` | Crop `Product/Dalmation/3.png` | Kartu horizontal pertama |
| Hamiqua | `produk/hamiqua.html` | Crop `Product/Hamiqua/3.png` | Kartu horizontal kedua |
| Rock Melon | `produk/rock-melon.html` | Crop aman `Product/Rock Melon/4.png` | Kartu vertikal pertama |
| Sweet Hamy | `produk/sweet-hamy.html` | Crop aman `Product/Sweet Hamy/4.png` | Kartu vertikal kedua |
| Sweet Lavender | `produk/sweet-lavender.html` | Crop aman `Product/Sweet Lavender/5.png` | Kartu vertikal ketiga |

Semua pilihan gambar tunduk pada aturan audit klaim di bagian 4. Inthanon disebut unggulan karena PDF h.7 menyatakannya sebagai produk fokus; lima kartu lain tidak diberi badge populer/terlaris tanpa bukti.

### 7.2 Isi kartu

- Foto buah, nama varietas, identitas GHI MELON.
- Kalimat singkat yang hanya memakai informasi terkonfirmasi.
- Link **Lihat Produk** dengan tujuan halaman detail nyata.
- Tidak ada harga, stok, rating, Brix, berat atau masa simpan rekaan.
- Tidak perlu pencarian, filter, sorting atau pagination untuk enam varietas.

### 7.3 Anatomi halaman detail

1. Header konsisten dengan beranda.
2. Breadcrumb: Beranda, Produk, nama varietas.
3. Satu H1 nama varietas; label GHI MELON.
4. Foto utama dan thumbnail gambar tambahan yang lolos audit.
5. Deskripsi singkat berbasis sumber; jangan memaksakan uraian panjang jika spesifikasi belum tersedia.
6. Atribut terkonfirmasi bila ada. Jangan menampilkan tabel kosong atau placeholder publik untuk menutup kekurangan data.
7. CTA **Tanyakan Produk**, dengan pesan WhatsApp sesuai nama varietas.
8. Dua atau tiga tautan varietas terkait; pemilihannya eksplisit, tidak memerlukan mesin rekomendasi.
9. Footer konsisten.

Desktop menggunakan dua kolom foto dan informasi; ponsel satu kolom. Poster penuh memakai `object-fit: contain` agar tulisan tidak terpotong. Foto kartu boleh memakai crop editorial yang aman.

Inthanon dapat memakai satu gambar; jangan menggandakan gambar h.7 dan h.8 yang hampir sama seolah dua foto produk berbeda. Jangan mengambil foto varietas lain untuk mengisi galeri Inthanon.

## 8. Header, Main, Footer dan Interaksi

### 8.1 Pembagian layout

Semua halaman mempunyai landmark `<header>`, `<main id="konten-utama">`, dan `<footer>` yang terpisah. Header/footer bukan bagian dari carousel atau konten produk.

Untuk sepuluh HTML, gunakan markup header/footer langsung pada tiap halaman dengan class dan susunan konsisten. CSS dan JavaScript digunakan bersama. Ini sengaja menghindari build system atau runtime fetch hanya untuk memuat navigasi/footer. Bila jumlah halaman atau frekuensi pembaruan meningkat besar, pertimbangkan template build-time pada tugas terpisah.

### 8.2 Navigasi

- Skip link **Lewati ke konten utama**.
- Tentang/Produk/Hubungi Kami menuju `tentang.html`/`katalog.html`/`kontak.html`; dari detail memakai prefix `../`. Footer mengikuti tujuan yang sama. Breadcrumb Produk dan Kembali ke katalog menuju `../katalog.html`.
- Layanan/Kemitraan tetap anchor beranda: `#layanan`/`#kemitraan` di beranda, `index.html#layanan`/`index.html#kemitraan` pada root lain, prefix `../` dari detail. Seluruh ID section beranda lama dipertahankan.
- `aria-current="page"` navbar hanya pada halaman mandiri yang sedang dibuka, bukan katalog saat membuka detail. Pembuka halaman memiliki breadcrumb, H1, serta pengantar pada panel hijau pucat.
- Navbar fixed dengan offset atas; section memiliki `scroll-margin-top` agar judul tidak tertutup.
- Menu seluler memakai tombol dengan nama aksesibel, `aria-controls`, dan `aria-expanded`.
- Menu merupakan disclosure nonmodal; tidak perlu focus trap.
- Escape menutup menu dan mengembalikan fokus ke tombol. Memilih link menutup menu.
- Tanpa JavaScript, tautan navigasi tetap terlihat dan bisa dipakai. Tombol toggle baru diaktifkan ketika perilakunya tersedia.

### 8.3 Galeri

JavaScript hanya meningkatkan galeri statis menjadi gambar utama dengan pilihan thumbnail. Tombol thumbnail mempunyai label dan indikator aktif; pergantian gambar memperbarui alt serta ukuran intrinsik yang sesuai.

Tanpa JavaScript, gambar tetap tampil sebagai daftar/grid yang bisa dijangkau. Tidak perlu lightbox, autoplay, library slider, atau drag gesture khusus.

### 8.4 Kontak

- Telepon memakai `tel:+6281398759898`.
- WhatsApp memakai nomor `6285284992841`.
- Pesan produk: **Halo GHI MELON, saya ingin menanyakan produk [Nama Varietas].**
- Pesan kemitraan: **Halo Green House Indonesia, saya ingin berdiskusi mengenai peluang kemitraan.**
- Encode teks query menggunakan `encodeURIComponent` saat menyusun tautan; URL akhir tetap tersedia dalam HTML agar kontak tidak bergantung pada JavaScript.
- Tidak tampilkan pemberitahuan “pesan terkirim” atau “pesanan berhasil” hanya karena WhatsApp dibuka.
- Tidak membuat formulir kontak tanpa endpoint pengiriman yang nyata.

### 8.5 Gerakan

Hover/focus cukup transisi ringan sekitar 150–250ms. Animasi muncul saat scroll tidak wajib. Konten terlihat secara default; jangan memulai dengan seluruh section transparan sampai JavaScript berjalan. Hormati `prefers-reduced-motion` dan nonaktifkan smooth scrolling/animasi yang tidak perlu.

## 9. Struktur File yang Direncanakan

```text
Melon/
├── implementation.md
├── index.html
├── katalog.html
├── tentang.html
├── kontak.html
├── produk/
│   ├── inthanon-signature.html
│   ├── dalmation.html
│   ├── hamiqua.html
│   ├── rock-melon.html
│   ├── sweet-hamy.html
│   └── sweet-lavender.html
├── assets/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   ├── fonts/                 # Jika font berlisensi tersedia
│   └── images/
│       ├── brand/
│       ├── hero/
│       └── products/
│           ├── inthanon-signature/
│           ├── dalmation/
│           ├── hamiqua/
│           ├── rock-melon/
│           ├── sweet-hamy/
│           └── sweet-lavender/
├── company_profile.pdf        # Sumber asli, tidak diubah
└── Product/                   # Sumber asli, tidak diubah
```

Tanggung jawab:

- `index.html`: company profile dan bagian katalog lengkap dengan konten inti dalam HTML.
- `katalog.html`: pembuka editorial, Inthanon unggulan, lima kartu varietas, CTA kontak.
- `tentang.html`: profil, pembedaan tiga identitas, nilai, visi/misi, legalitas, foto editorial melon, CTA katalog/kemitraan.
- `kontak.html`: telepon, WhatsApp, alamat kantor, jalur percakapan produk dan kemitraan; tanpa form atau peta rekaan.
- `produk/*.html`: detail statis, bisa dibuka langsung dan diindeks.
- `styles.css`: token, tipografi, header/footer, layout section, kartu, galeri, breakpoint, reduced motion.
- `main.js`: disclosure navigasi dan peningkatan galeri; dimuat dengan `defer`.
- `assets/images/`: salinan turunan teroptimasi, bukan pengganti master.

Gunakan nama file turunan lowercase dengan tanda hubung. Referensi aset dari seluruh halaman root memakai `assets/...`; dari halaman produk memakai `../assets/...`. Hindari path absolut `/assets/...` agar situs tetap berjalan pada hosting subfolder. Tidak perlu JSON katalog dan renderer client-side untuk enam halaman statis.

Saat hosting dipersiapkan, publikasikan hanya file website yang diperlukan. Folder master `Product/`, PDF asli, dokumen internal dan cache pemeriksaan tidak otomatis ikut dipublikasikan.

## 10. Aset, Performa, Aksesibilitas dan SEO

### 10.1 Pengolahan gambar

- Ekstrak logo dan Inthanon dari PDF saat implementasi, tanpa mengubah sumber.
- Simpan catatan pemetaan sumber ke file turunan pada tabel aset dalam dokumen ini ketika pilihan final sudah dikunci.
- Audit teks tertanam sebelum mengekspor crop.
- Buat turunan WebP dan JPEG/PNG fallback bila diperlukan; jangan memuat master PNG 60 MiB ke halaman.
- Ukuran turunan mengikuti dimensi sumber dan tampilan; jangan meng-upscale hanya untuk memenuhi angka 1600px.
- Contoh lebar turunan: thumbnail sekitar 240px, kartu 480/800px, gambar besar sampai lebar asli yang layak. Hero memakai resolusi terbaik yang benar-benar tersedia.
- Gunakan `srcset`, `sizes`, `width`, dan `height`; `aspect-ratio` menstabilkan area sebelum gambar termuat.
- Hero tidak lazy-loaded; prioritaskan hanya gambar LCP. Gambar di bawah fold memakai lazy loading dan decoding async.
- Target ukuran awal: kartu sekitar 80–180KB dan hero sekitar 300KB bila kualitas memungkinkan; ini anggaran optimasi, bukan alasan merusak detail produk.

### 10.2 Aksesibilitas

- `lang="id"`, satu H1 per halaman, heading berurutan, struktur landmark jelas.
- Kontras teks normal minimal 4.5:1; teks besar minimal 3:1.
- Target sentuh minimum 44×44px, termasuk tombol menu dan thumbnail.
- Fokus keyboard terlihat; jangan mengandalkan hover atau warna saja.
- Alt menjelaskan objek/foto, bukan memasukkan klaim nutrisi atau Brix yang belum dikonfirmasi.
- Informasi penting tidak hanya berada dalam teks gambar; salin sebagai HTML hanya setelah fakta terverifikasi.
- Gambar dekoratif memakai alt kosong; ikon panah dekoratif tidak dibaca berulang oleh screen reader.
- Jangan menambahkan atribut ARIA untuk menggantikan elemen HTML native yang sudah sesuai.

### 10.3 SEO dasar

- Judul dan meta description unik untuk beranda dan enam produk.
- Isi utama tersedia dalam HTML tanpa menunggu rendering JavaScript.
- Nama produk, breadcrumb, tautan internal dan alt bermakna.
- Canonical, sitemap dan robots produksi menunggu domain serta struktur hosting sebenarnya; jangan memakai domain tebakan.
- Structured data hanya fakta yang benar. Jangan mengarang `Offer`, harga, stok, `aggregateRating`, sertifikasi atau ulasan demi rich result.
- Tidak perlu menambah artikel/blog tipis hanya untuk mengejar SEO.

## 11. Tahapan Implementasi Website

Implementasi lokal telah dikerjakan atas permintaan pengguna. Checklist berikut menandai hasil implementasi; konfirmasi data dan peluncuran tetap terpisah.

### Tahap 1 — Kunci konten dan aset

**Hasil lokal:** nama, copy, dan crop ditetapkan. Spesifikasi/Brix dan variasi nama tag belum dikonfirmasi; klaim tersebut tidak dipublikasikan. Checklist awal berikut tetap menunjukkan pekerjaan konfirmasi yang terpisah dari hasil lokal.

**Berkas terkait:** `company_profile.pdf`, `Product/`, tabel sumber dalam `implementation.md`.

- [x] Tetapkan nama tampilan tiga identitas merek dan enam varietas sesuai sumber.
- [ ] Konfirmasi Sweet Lavender versus Sweet Net Lavender serta spesifikasi yang ingin ditampilkan.
- [ ] Selesaikan konflik Brix Rock Melon; jika belum selesai, angka tidak dipublikasikan.
- [x] Pilih gambar yang lolos audit dan crop aman untuk masing-masing penempatan.
- [x] Tetapkan copy beranda, layanan, produk, kemitraan, kontak dan legalitas ringkas.

**Selesai bila:** matriks konten memiliki sumber; setiap produk punya aset benar; tidak ada klaim yang bertentangan tetap terlihat pada aset terpilih.

### Tahap 2 — Siapkan turunan visual

**Berkas keluaran:** `assets/images/brand/`, `hero/`, `products/`, font berlisensi bila dipakai.

- [x] Ekstrak logo resmi dan Inthanon dari PDF.
- [x] Ekspor turunan foto sesuai kartu/detail/thumbnail tanpa mengubah master.
- [x] Buat preview hero 1440px dan 390px; gunakan fallback komposisi portrait bila crop landscape tidak layak.
- [x] Periksa warna buah, identitas varietas, keterbacaan, dan ukuran file.

**Selesai bila:** aset punya sumber tercatat, tidak terdistorsi, tidak memuat teks keliru, dan tidak memakai upscale yang menyesatkan.

### Tahap 3 — Bangun beranda dan layout

**Berkas:** `index.html`, `assets/css/styles.css`.

- [x] Buat header, skip link, main, footer serta anchor section.
- [x] Isi profil, visi/nilai/misi, signature, lima kartu, layanan, proses, mutu, galeri, kemitraan dan kontak.
- [x] Terapkan token Solune, navbar kapsul, hero, tipografi serif, CTA panah, panel bergantian, dan grid dua-plus-tiga.
- [x] Susun responsif mobile-first; semua navigasi dan konten inti berfungsi tanpa JavaScript.

**Selesai bila:** keenam varietas terlihat, section tidak menjadi salinan PDF mentah, dan tampilan 390/1440px mengikuti komposisi referensi dengan aset lokal.

### Tahap 4 — Bangun enam detail produk

**Berkas:** enam `produk/*.html`, stylesheet bersama.

- [x] Terapkan pola breadcrumb, galeri, informasi, CTA WhatsApp dan produk terkait.
- [x] Gunakan header/footer konsisten serta path `../` yang benar.
- [x] Tampilkan hanya atribut terkonfirmasi; jangan menambah detail fiktif untuk memperpanjang halaman.
- [x] Pastikan Inthanon memakai foto PDF sendiri, bukan foto produk lain.

**Selesai bila:** semua URL bisa dibuka langsung, di-refresh, dan kembali ke katalog tanpa link/aset rusak.

### Tahap 5 — Tambahkan interaksi minimum

**Berkas:** `assets/js/main.js`, markup menu/galeri yang relevan.

- [x] Implementasikan menu disclosure dan perilaku keyboard/Escape.
- [x] Implementasikan pilihan thumbnail secara progresif; jangan memerlukan JavaScript untuk membaca foto/konten dasar.
- [x] Gunakan CTA native dengan pesan WhatsApp ter-encode.
- [x] Tinggalkan satu pemeriksaan runnable kecil untuk logika nontrivial, misalnya validasi tujuan WhatsApp dan kontrak toggle menu, tanpa menambah framework pengujian hanya untuk ini.

**Selesai bila:** interaksi keyboard, mode JavaScript mati, dan reduced motion berfungsi tanpa error console.

### Tahap 6 — Verifikasi sebelum peluncuran

- [ ] Jalankan pemeriksaan pada bagian 12.
- [ ] Bandingkan screenshot tiap bagian dengan Solune pada viewport setara.
- [ ] Finalisasi domain, metadata, izin publikasi aset dan informasi kontak.
- [ ] Pilih hosting statis dan HTTPS setelah ada persetujuan deployment.

**Selesai bila:** kriteria penerimaan terpenuhi dan pemilik menyetujui konten serta aset publik. Penyusunan dokumen ini tidak melakukan deployment.

## 12. Kriteria Penerimaan dan Cara Verifikasi

### 12.1 Pemeriksaan konten

- [ ] Perusahaan disebut PT GHI Makmur Indonesia; peran Green House Indonesia dan GHI MELON tidak tertukar.
- [ ] Katalog memuat keenam varietas, termasuk Inthanon Signature.
- [ ] Semua foto benar varietasnya; gambar cacat teks tidak dipublikasikan tanpa perbaikan/crop aman.
- [ ] Tidak ada spesifikasi rekaan, angka Brix kompromi, rating, testimoni, logo klien, atau klaim sertifikasi tanpa dasar.
- [ ] Kanal distribusi dan kerja sama potensial tidak ditulis sebagai pencapaian atau pelanggan aktif.
- [ ] Nomor telepon/WhatsApp sesuai sumber; tidak ada email/domain/sosial tebakan.
- [ ] Tidak ada placeholder publik, tombol tanpa tujuan, atau formulir pengiriman palsu.

### 12.2 Uji melalui HTTP lokal

Preview lokal: `python -I -m http.server 8000 --bind 127.0.0.1`, buka `http://127.0.0.1:8000/`. Server pengembangan hanya loopback; jangan deploy seluruh direktori sumber.

- [ ] Beranda dan enam `produk/*.html` memberi respons berhasil.
- [ ] Buka langsung dan refresh setiap URL detail.
- [ ] Semua link kartu, breadcrumb, anchor, navigasi/footer dan aset berfungsi.
- [ ] Tidak ada request 404, error JavaScript, atau mismatch kapitalisasi path.
- [ ] Tautan telepon memiliki nomor benar; tautan WhatsApp memiliki tujuan dan pesan sesuai produk. Tidak perlu mengirim pesan untuk menguji URL.
- [ ] Pengujian juga mempertimbangkan hosting subfolder dan sistem file case-sensitive.

### 12.3 Uji visual dan responsif

Viewport: **360, 390, 768, 1024, 1440px**.

- [ ] Tidak ada scroll horizontal halaman.
- [ ] Navbar tidak menutupi heading, konten, atau target anchor.
- [ ] Hero mempertahankan buah dan kontras; tidak ada poster portrait terdistorsi.
- [ ] Grid desktop membentuk dua kartu horizontal dan tiga vertikal, ditambah blok signature; ponsel satu kolom.
- [ ] Footer dan CTA tetap terbaca; tidak ada teks terpotong karena tinggi tetap.
- [ ] Bandingkan navbar, hero, katalog, panel hijau-putih, CTA, dan footer terhadap Solune: warna, font, komposisi, radius, dan spacing.

Screenshot referensi panjang dapat menampilkan bagian kosong akibat animasi scroll. Lakukan perbandingan per section setelah section terlihat; jangan menyalin kekosongan tersebut sebagai desain.

### 12.4 Uji aksesibilitas dan ketahanan

- [ ] Seluruh navigasi dan tombol berfungsi melalui Tab/Enter/Space sesuai elemen native.
- [ ] Escape menutup menu dan mengembalikan fokus.
- [ ] Fokus terlihat; thumbnail memiliki nama dan status aktif.
- [ ] Nonaktifkan JavaScript: profil, enam produk, detail, foto, navigasi, footer dan kontak tetap tersedia.
- [ ] Aktifkan reduced motion: tidak ada animasi wajib atau smooth scrolling yang mengganggu.
- [ ] Uji heading/landmark/nama tombol dengan accessibility tree dan screen reader bila tersedia.
- [ ] Periksa kontras dan ukuran target sentuh.

### 12.5 Performa dan metadata

Target evaluasi, **bukan hasil pengukuran yang sudah tercapai**:

- Lighthouse mobile: Performance **≥90**, Accessibility **≥95**.
- LCP **≤2,5 detik**, CLS **≤0,1**, INP **≤200ms** pada kondisi evaluasi yang relevan.
- INP tidak dianggap lulus hanya karena skor Lighthouse; butuh interaksi nyata dan, setelah peluncuran, data lapangan bila tersedia.
- [ ] Hero tidak lazy-loaded; gambar bawah fold lazy-loaded.
- [ ] Gambar punya dimensi intrinsik dan turunan sesuai viewport.
- [ ] Tidak ada pemuatan seluruh 26 master PNG sebagai beban awal.
- [ ] Title/deskripsi unik, satu H1, alt bermakna, dan metadata memakai domain yang benar ketika tersedia.

## 13. Konfirmasi Sebelum Konten Publik Dikunci

Hal berikut tidak menghalangi penyusunan rancangan, tetapi harus diselesaikan sebelum konten terkait dipublikasikan:

1. Spesifikasi aktual tiap varietas, terutama konflik Brix Rock Melon.
2. Nama resmi Sweet Lavender versus Sweet Net Lavender pada tag.
3. Versi koreksi poster dengan typo, deskripsi salah, atau klaim yang belum didukung; alternatifnya crop aman dan pengecualian aset.
4. Crop hero yang layak atau tambahan foto landscape asli dari pemilik.
5. Versi logo untuk navbar serta hak penggunaan font/aset.
6. Persetujuan rincian legal yang ditampilkan, domain, hosting, dan izin terpisah jika PDF asli akan disediakan untuk diunduh.

**Hasil akhir yang dituju:** website bernuansa editorial-natural seperti Solune, dengan identitas Green House Indonesia dan katalog enam varietas GHI MELON; faktual, responsif, ringan, dan mengarahkan pertanyaan bisnis ke kontak perusahaan.

## 14. Riwayat Implementasi Awal — 6 November 2026

Bagian ini mencatat tahap awal tujuh HTML. Angka uji di bawah adalah riwayat, bukan hasil pengujian penambahan tiga halaman; cakupan terbaru ada pada bagian 15.

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
| `assets/images/products/inthanon-signature/utama-480.webp` | PDF h.7 xref189 | `(0, 620, 1024, 1215)` | 480×279 | 32,032 |
| `assets/images/products/inthanon-signature/utama-800.webp` | PDF h.7 xref189 | `(0, 620, 1024, 1215)` | 800×465 | 75,096 |
| `assets/images/products/dalmation/utama-480.webp` | `Product/Dalmation/3.png` | `(0, 870, 941, 1290)` | 480×214 | 21,068 |
| `assets/images/products/dalmation/utama-800.webp` | `Product/Dalmation/3.png` | `(0, 870, 941, 1290)` | 800×357 | 48,364 |
| `assets/images/products/dalmation/detail-1-470.webp` | `Product/Dalmation/2.png` | `(460, 790, 930, 1460)` | 470×670 | 46,384 |
| `assets/images/products/hamiqua/utama-480.webp` | `Product/Hamiqua/3.png` | `(0, 1000, 941, 1600)` | 480×306 | 50,562 |
| `assets/images/products/hamiqua/utama-800.webp` | `Product/Hamiqua/3.png` | `(0, 1000, 941, 1600)` | 800×510 | 116,566 |
| `assets/images/products/hamiqua/detail-1-480.webp` | `Product/Hamiqua/2.png` | `(215, 1125, 930, 1455)` | 480×222 | 25,038 |
| `assets/images/products/hamiqua/detail-1-715.webp` | `Product/Hamiqua/2.png` | `(215, 1125, 930, 1455)` | 715×330 | 49,536 |
| `assets/images/products/rock-melon/utama-480.webp` | `Product/Rock Melon/4.png` | `(0, 1080, 941, 1580)` | 480×255 | 40,788 |
| `assets/images/products/rock-melon/utama-800.webp` | `Product/Rock Melon/4.png` | `(0, 1080, 941, 1580)` | 800×425 | 97,614 |
| `assets/images/products/rock-melon/detail-1-420.webp` | `Product/Rock Melon/6.png` | `(510, 800, 930, 1460)` | 420×660 | 74,148 |
| `assets/images/products/sweet-hamy/utama-480.webp` | `Product/Sweet Hamy/4.png` | `(0, 1000, 941, 1610)` | 480×311 | 48,786 |
| `assets/images/products/sweet-hamy/utama-800.webp` | `Product/Sweet Hamy/4.png` | `(0, 1000, 941, 1610)` | 800×519 | 113,970 |
| `assets/images/products/sweet-hamy/detail-1-425.webp` | `Product/Sweet Hamy/3.png` | `(505, 900, 930, 1490)` | 425×590 | 102,696 |
| `assets/images/products/sweet-lavender/utama-461.webp` | `Product/Sweet Lavender/5.png` | `(480, 930, 941, 1510)` | 461×580 | 94,456 |
| `assets/images/products/sweet-lavender/detail-1-480.webp` | `Product/Sweet Lavender/6.png` | `(0, 1090, 941, 1600)` | 480×260 | 40,084 |
| `assets/images/products/sweet-lavender/detail-1-800.webp` | `Product/Sweet Lavender/6.png` | `(0, 1090, 941, 1600)` | 800×434 | 91,236 |

Hero memakai crop Inthanon yang sama, bukan foto galeri kedua. Logo PDF h.1 xref6 diturunkan ke maksimum600×400.

### 14.3 Hasil verifikasi yang benar-benar dijalankan

| Pemeriksaan | Hasil |
|---|---|
| `python -I tests/check_site.py` | PASS:7 halaman; metadata unik; lang/H1/landmark; kontak dan pesan produk; enam URL; href/src/srcset/fragment; kapitalisasi path; SHA256 PDF+26 PNG tidak berubah. |
| `node --check assets/js/main.js` | PASS, exit0. |
| `tests/browser_checks.js` via Playwright MCP | PASS35 kombinasi halaman/viewport360/390/768/1024/1440, tanpa overflow. |
| Menu keyboard | PASS Enter/Space; Escape dari dalam/luar header menutup dan mengembalikan fokus; link katalog/wordmark menutup; resize saat link maupun toggle fokus tidak kehilangan fokus. |
| Galeri | PASS pilihan foto/aria-pressed/hidden, reload mengembalikan foto utama. |
| JavaScript disabled | PASS navigasi dan seluruh foto statis pada7 halaman di390px; tambahan pemeriksaan decode berhasil untuk50 elemen gambar. |
| Reduced motion | PASS computed `scroll-behavior:auto`. |
| Subfolder `/Melon/` | PASS6 detail direct/refresh/kembali katalog, tanpa404. |
| Console/network selama suite | Tidak ada pageerror atau responsHTTP≥400. |
| Visual | Hero390/1440, katalog desktop/mobile, detail mobile, CTA/footer ditinjau melalui screenshot; susunan kapsul/serif/panel2+3 mengikuti referensi, bukan salinan gambar Solune. |
| Accessibility tree | Landmark, heading, label menu/thumbnail/status diperiksa pada detail. Screen reader nyata belum diuji. |
| Kontras hero/kartu | RED sebelum perbaikan; GREEN setelah overlay kartu diperkuat. Sampel seluruh persegi teks dengan teks disembunyikan pada390/1440px: hero H1 minimum3,02:1, body5,77:1; kartu H3 minimum8,22:1, teks kecil9,52:1. Bukan sertifikasi seluruh situs atau seluruh viewport. |
| Target interaktif | PASS35 kombinasi: elemen interaktif yang tampil minimal44×44px; skip link tersembunyi dikecualikan. Lebar link navbar/breadcrumb diperbaiki setelah regresi RED. |
| Review independen | Review diterima; Escape di luar header dan wordmark direproduksi lalu diperbaiki dengan regresi browser. Laporan provenance memiliki referensi keadaan dokumen berbeda; tidak dianggap audit eksternal final. Audit crop lokal tetap menjadi bukti utama. |
| Minor ditunda | `tests/check_site.py:72–76` dapat mengklaim source integrity ketika manifest hilang/kosong/tidak lengkap. Saat verifikasi ini manifest27 entri tersedia dan semuanya cocok. |
| Lighthouse/Core Web Vitals | Belum diukur; Lighthouse tidak tersedia dalam tooling global. Tidak mengklaim target skor/LCP/CLS/INP tercapai. |

Menjalankan browser suite memerlukan Playwright MCP yang tersedia di lingkungan pengembangan. Script berisi fungsi `async(page)` untuk `browser_run_code_unsafe({filename:'tests/browser_checks.js'})`; tidak memerlukan framework proyek. Regresi kontras: jalankan `tests/capture_contrast.js` dengan tool yang sama, lalu `python -I tests/check_contrast.py` (Pillow yang telah tersedia). Capture menonaktifkan cache browser, menyimpan latar tanpa teks dan koordinat aktual di `.work/contrast.json`.

Pembangunan lokal selesai; checklist bagian12 tetap merupakan daftar penerimaan pra-peluncuran. Hasil yang benar-benar diuji dan batas cakupannya tercatat di tabel ini; Lighthouse/CWV, screen reader nyata, konfirmasi komersial, serta publikasi belum selesai.

### 14.4 Batas peluncuran

Belum ada deployment, domain/canonical/sitemap produksi, verifikasi registri legal independen, atau pengiriman pesan WhatsApp. Hanya tautan native yang disiapkan. Konfirmasi komersial dan izin publikasi tetap mengikuti bagian13.

Saat deployment disetujui, unggah **hanya** `index.html`, `katalog.html`, `tentang.html`, `kontak.html`, `produk/*.html`, dan `assets/` yang diperlukan. Jangan unggah `Product/`, PDF, `.work/`, `tests/`, screenshot, atau dokumen internal. Server Python ini adalah preview, bukan server produksi.

## 15. Perluasan Tiga Halaman — 6 November 2026

### 15.1 Cakupan terbaru

Tersedia sepuluh HTML: beranda, `katalog.html`, `tentang.html`, `kontak.html`, dan enam detail produk. Ketiga halaman baru menggunakan pembuka editorial hijau pucat, heading serif, navbar kapsul, komponen serta foto terverifikasi yang sama. Tidak ada dependency atau JavaScript aplikasi baru. Header/footer tetap langsung di HTML; pembaruan bersama harus disinkronkan manual.

Navigasi umum, hero Jelajahi Produk, footer, breadcrumb detail dan Kembali ke katalog sudah diarahkan ke halaman mandiri. Layanan/Kemitraan tetap menuju section beranda. Section lama dan galeri detail dipertahankan. Halaman kontak membedakan telepon/WhatsApp serta menyebut Alamat Kantor; tidak ada form, peta, harga, stok atau klaim komersial baru.

### 15.2 Hasil pengujian perluasan

| Pemeriksaan | Hasil aktual |
|---|---|
| Kontrak Python | RED: tiga halaman belum ada; GREEN:10 halaman, metadata/landmark, enam varietas, navigasi/current page, path/aset/fragment/case/kontak. Entri manifest sumber cocok. |
| JavaScript | `node --check assets/js/main.js` exit0; berkas aplikasi tidak berubah. |
| Browser responsive | PASS50 kombinasi sepuluh halaman ×360/390/768/1024/1440px; tidak ada overflow atau target tampil di bawah44×44px. |
| Tanpa JavaScript | PASS10 halaman; navigasi dan foto galeri tersedia;57 elemen gambar berhasil decode. |
| Navigasi | PASS beranda ke tiga halaman, reload, katalog ke enam detail, breadcrumb/return, nav detail ke Tentang/Kontak, Layanan/Kemitraan ke anchor beranda. |
| Menu/galeri | PASS Enter/Space/Escape, fokus luar header, wordmark, resize fokus, menu halaman aktif, thumbnail/reload dan reduced motion. |
| Fokus kontak aktif | RED: outline status aktif menimpa focus-visible; GREEN setelah selector status dibatasi `:not(:focus-visible)`. Regresi browser disertakan; screenshot fokus ditinjau. |
| Subfolder | PASS `/Melon/`: tiga halaman baru direct/reload, gambar, tautan katalog, Dalmation/detail/reload/breadcrumb return. |
| Visual/semantik | Enam screenshot halaman baru390/1440 ditinjau; pembuka/konten/CTA/footer dan alamat terbaca. Accessibility snapshot ketiga halaman dibaca; kedua disclosure Tentang dibuka dengan Enter. Kontras teks pengantar terhadap panel computed6,46:1. |
| Error selama suite | Tidak ada pageerror atau responsHTTP≥400. |
| Kontras | Overlay/kartu tidak berubah. Pemeriksaan34 persegi pada capture tahap awal tetap PASS; bukan pengukuran baru halaman mandiri atau sertifikasi WCAG. |

Satu run browser setelah penambahan pemeriksaan fokus sempat timeout: fokus yang ditinggalkan pengujian mempertahankan menu mobile terbuka ketika resize, lalu toggle justru menutupnya. Test mengakhiri pemeriksaan fokus sebelum skenario menu berikutnya; suite lengkap berikutnya PASS50. Bukan perubahan perilaku menu aplikasi.

Review akhir independen tidak menemukan defect runtime; dua celah pemeriksaan diperbaiki: tujuan diperiksa terpisah dalam header/footer/breadcrumb/return, serta geometri pembuka diperiksa pada seluruh viewport JS dan390/1440 tanpa JS. Mutation navbar salah dan padding pembuka nol menghasilkan RED; sumber aktual GREEN. Suite final Python10, sintaks Node, browser50/no-JS10/57decode PASS. Reviewer tidak menjalankan browser atau mengaudit ulang master; hasil runtime berasal dari pengujian lokal di atas. Minor ditunda: skenario subfolder masih pengujian inline, belum bagian suite tersimpan.

### 15.3 Preview dan batas

Preview lokal: `http://127.0.0.1:8000/katalog.html`, `http://127.0.0.1:8000/tentang.html`, `http://127.0.0.1:8000/kontak.html`; server parent8001 dipakai hanya untuk uji subfolder. Tidak ada deployment, Artifact, Git/commit, perubahan master PDF/Product, atau pengiriman WhatsApp.

Lighthouse/CWV, screen reader nyata, browser selain Chromium dan persetujuan komersial/publikasi belum diuji/diselesaikan. Manifest audit masih opsional dan tidak diuji kelengkapannya; output kini hanya menyatakan entri yang diperiksa, atau manifest tidak tersedia, bukan klaim integritas penuh tanpa bukti. `.work/` dipertahankan sebagai bukti lokal karena tidak ada riwayat Git; jangan ikut dipublikasikan. Helper authoring bukan build rutin dan tidak boleh dijalankan ulang sembarangan.
