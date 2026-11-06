# SDD ledger — plan: C:\Users\Windows 11 Home\.claude\plans\baca-keseluruhan-company-profile-pdf-dan-recursive-kazoo.md

Spec: ../implementation.md
Ruling: Tidak membuat Git/worktree/commit; proyek bukan Git dan rencana melarang inisialisasi. Ledger lokal menggantikan skrip SDD berbasis Git; biaya: tidak ada riwayat commit otomatis.
Pre-flight: Task1 image names/dimensions consumed by Tasks2/3; markup must use actual crop dimensions, no upscale.
Pre-flight: Tasks2/3 data attributes consumed by Task4; menu/gallery remain static until handlers installed.
Pre-flight: Task5 runs stdlib tests from Task2/3; no framework or install needed.
Task1: complete. Audit 26 gambar, ekstraksi Inthanon/logo, 18 turunan WebP produk; crop penuh diperiksa ulang sesudah membuang teks Hamiqua. Source SHA256 sama menurut tests/check_site.py.
Ruling: Hero memakai close-up Inthanon bersih, bukan Hamiqua/2 — foto landscape fasilitas tidak tersedia dan inventaris lama keliru — biaya: detail terbatas resolusi sumber 1024px, perlu foto landscape asli untuk peningkatan.
Ruling: Body memakai Arial mengganti Satoshi; heading Libre Caslon Text Google Fonts dengan fallback Georgia — font lokal tidak tersedia — biaya: bentuk body tidak identik referensi; font heading online bergantung koneksi.
Task2: complete. index.html + CSS; uji kontrak RED karena 7 halaman hilang, GREEN setelah HTML/JS ada; screenshot hero390/1440, katalog dan kontak diperiksa.
Task3: complete. 6 detail HTML, 1 gambar Inthanon dan 2 foto lainnya; metadata/contact/path/anchor/case/source integrity PASS.
Task4: complete. JS native menu/gallery. Browser RED: enhancement tidak ada; GREEN setelah JS. Breakpoint focus RED (CSS menyembunyikan elemen sebelum change handler), GREEN dengan :focus-within/:focus guards.
Task5: complete (local implementation). Python check PASS; node --check PASS; Playwright 35 halaman/viewport PASS, keyboard Enter/Space/Escape/link/resize (nav dan toggle fokus) PASS, gallery PASS, no-JS 7 halaman PASS + 50 gambar decode, reduced motion PASS, subfolder direct/refresh/catalog 6 detail PASS. Tidak ada 404/pageerror selama suite. Accessibility tree dibaca. Lighthouse/CWV dan screen reader nyata belum diukur. Fresh whole-site reviewer diterima; tidak ada deployment.
Ruling: Pertahankan .work ledger/hash sebagai bukti lokal, tidak dihapus — tidak ada riwayat Git untuk pemulihan — biaya: folder internal harus dikecualikan saat publikasi.
Final: fixed card contrast — capture_contrast.js/check_contrast.py RED→GREEN; 34 persegi teks pada hero/kartu390/1440; heading hero min3.02, body5.77, card heading8.22, card body9.52. Overlay lebih gelap; gambar sumber tidak diubah.
Final: fixed Escape outside header and wordmark close — browser reproduction RED→GREEN; one listener moved to document, click delegation moved to header. Regraded Important: explicit keyboard/navigation contract, two-line correction.
Final: fixed targets below44px — browser_checks.js RED→GREEN, min-width navbar/breadcrumb; suite35/35.
Final: minor (deferred): tests/check_site.py:72–76 prints source integrity PASS with missing/empty/incomplete manifest. Current27-entry manifest checked and intact; affects future audit reliability, not website runtime.
Final: Ruling: disputed reviewer provenance/document references — do not claim independent provenance approval; retain local crop/source audit and record reviewer uncertainty — cost: independent image approval remains limited.
Final: Ruling: fractional breakpoint gap dismissed without reproduction; CSS exact767 matches JS. Old matchMedia.addEventListener absence leaves core navigation/photos visible, no legacy enhancement shim — cost: older browsers may receive static fallback only.
Final verification: final12 background recaptures, tests/check_site.py, node --check assets/js/main.js, tests/browser_checks.js (35/35 + no-JS7), tests/check_contrast.py (34/34 rectangles) all passed after fixes. Current browser left on working Dalmation detail; local preview8000 remains running.
