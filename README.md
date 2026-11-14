# ryzu-prompt

Personal operating system buat AI. Dipasang sekali, jalan otomatis di semua prompt tanpa perlu manggil `/ryzu-prompt`. Fokusnya hasil maksimal dengan token minimal: gaya Ryzu, scope disiplin, dan semua file dikirim dalam satu zip berisi file yang berubah aja.

## Isi repo

```
ryzu-prompt/
├── SKILL.md                      # instruksi utama skill
├── README.md
├── references/
│   ├── humanizer.md              # pola tulisan AI + cara bersihin (ID/EN)
│   ├── android-ios.md            # root, kernel, modul, internals, app dev Android/iOS
│   └── knowledge.md              # 17 area kompetensi terapan (OS, jaringan, DB, API, QA, DR, dll)
└── ui-ux/
    ├── scripts/search.py         # design-intelligence search (Python 3 stdlib only)
    ├── data/                     # styles, colors, typography, landing, ux, charts, icons, gsap, dll
    │   └── stacks/               # react, nextjs, vue, svelte, astro, html-tailwind, shadcn,
    │                             # react-native, flutter, swiftui, jetpack-compose, threejs
    └── references/
        ├── quick-reference.md    # aturan UX lengkap (dibaca on demand)
        └── pro-rules.md          # mobile/native polish + checklist
```

## Install

Claude Code:

```bash
git clone https://github.com/Ryhandd/ryzu-prompt.git ~/.claude/skills/ryzu-prompt
```

Tool lain: taruh folder ini di lokasi skills tool tersebut.

Skill auto-trigger bergantung pada `description` di `SKILL.md`. Biar lebih pasti, tambah 1 baris di preferences Claude (atau `CLAUDE.md` di Claude Code): `Selalu terapkan skill ryzu-prompt di setiap pesan.`

## Cara kerja

| Bagian SKILL.md | Isi |
|---|---|
| §0 Profil | Bahasa gw/lu, hobi, stack, selera UI, memori preferensi (`RYZU-MEMORY.md` bila ada). Chat biasa dijawab langsung tanpa zip. |
| §1 Token & scope | Kerjain yang diminta aja. Tanpa pembuka, rekap, atau tawaran lanjutan. Max 1 pertanyaan, selebihnya pakai default. Edit surgical. |
| §2 Delivery | Satu `.zip` berisi hanya file yang berubah, path relatif project. Nama `<project>-update-<desc>.zip`. Pesan akhir: link + max 3 baris. |
| §1b Ask-first | Saat bilang "buatkan/bikin ...": 1 ronde 2-4 pertanyaan pilihan (opsi rekomendasi di depan), pertanyaan terakhir selalu "Mau diposting ke GitHub?". Dilewati kalau request sudah spesifik, tugas kecil/edit, atau ketik "langsung/gas". |
| §2b GitHub | Jawab Ya → zip tambah README + .gitignore, dan pesan akhir berisi semua command (init, commit, remote, push, `gh`, auth, update, tag). |
| §3 Mode | Dipilih diam-diam sesuai tugas, bisa digabung. |
| §14 Shortcut | Command opsional dengan default tersembunyi, jadi prompt bisa pendek. |
| §15 Konflik | Instruksi Ryzu di pesan sekarang menang atas skill; permintaan yang melanggar keamanan/hukum ditolak 1 baris + alternatif sah. |

## Mode

| Mode | Cakupan | Default utama |
|---|---|---|
| Web/UI/UX (§4) | Website, landing page, dashboard, komponen | Design system dari `search.py`, dials variance 7 / motion 6 / density 4, checklist aksesibilitas + performa, HTML + Tailwind (static) atau Next.js + Tailwind + shadcn (app) |
| Docs & akademik (§6) | Laporan, makalah, jurnal, riset, proposal, skripsi | `.docx` format kampus (A4, Times New Roman 12, spasi 1,5, margin 4/3/3/3), sitasi IEEE (teknik) atau APA 7, skripsi per bab, wajib humanize |
| 3D / OpenGL (§7) | Renderer, kamera, shader, model viewer | C++17 + CMake + GLFW + GLAD + GLM, GL 3.3 core; varian Rust (glfw/glutin + gl/glow) dan Java (LWJGL + JOML) |
| Cisco Packet Tracer (§8) | Topologi, VLAN, routing, NAT, ACL, soal praktikum | Tabel topologi + addressing + config per device siap paste + verifikasi (`.pkt` tidak bisa dibuat, jadi build manual) |
| Rust / Java / XML (§9) | Software, desktop, Android | Rust: fmt + clippy bersih, tanpa `unwrap` sembarangan. Java: LTS 17/21, Maven, JavaFX/FXML. XML: well-formed, Android XML pakai resource |
| Linux / Networking / Security (§10) | Debian, Kali, admin, hardening, script | Debian default, command + verifikasi + rollback, bash `set -euo pipefail`, pentest hanya lab/CTF/target ber-izin |
| AI / ML (§11) | Model, training, MLOps, LLM app | PyTorch, baseline dulu, seed + config, metrik tepat, serve via FastAPI + Docker |
| Security ops (§11) | SIEM, deteksi, vuln assessment, kripto, laporan pentest | SPL/KQL/Sigma, CVSS, MITRE ATT&CK, primitif kripto standar |
| Data science / analyst (§11) | SQL, Python, R, Tableau, Power BI | SQL dulu (PostgreSQL), insight format `temuan → angka → aksi` |
| Cloud (§11) | AWS/Azure, Terraform, Docker, Kubernetes | AWS + Terraform, least-privilege, `plan`/dry-run dulu |
| Full stack (§11) | Web/mobile app, API | TypeScript strict, React/Next.js, Node, FastAPI, PostgreSQL, conventional commits |
| DevOps (§11) | CI/CD, container, server | GitHub Actions: lint → test → build → scan → deploy, Docker multi-stage non-root |
| Android & iOS (§12) | Root, bootloader, kernel, modul Magisk/KernelSU, SELinux, AOSP; Swift/Xcode/signing, internals iOS, app dev | Konfirmasi model/OS dulu, backup + peringatan risiko + rollback ke stock, tanpa karang offset/flag; pentest/RE hanya device milik sendiri atau ber-izin |
| Knowledge base (§13) | 17 area: logika, OS/jaringan/DB, Git, cloud/security/AI, UI/UX + a11y, Agile + dokumentasi, UU PDP/GDPR, API + system design, QA + observability, FinOps, DR/IR, legacy + ISO 27001/ITIL, IoT/Web3/kuantum, technical debt + open source | Aturan terapan, bukan teori |
| Prompt engineer (§5) | Prompt buat tool AI lain | 1 blok siap paste + baris `🎯 Target`, XML tags untuk Claude, scope lock untuk tool agentic |
| Mobile, Game, Design (§3) | RN/Expo, Flutter, SwiftUI, Compose; Unity/Godot/Phaser; brand dan layout | Standar di SKILL.md §3 |

Aksi destruktif atau berdampak ke production (apply/destroy, drop, delete, force push, rotate key) selalu stop-and-ask, dry-run dulu.

## Shortcut

Command opsional, teks setelahnya = topik. Tanpa command, skill tetap jalan. "langsung" atau "gas" melewati ronde pertanyaan.

| Command | Fungsi |
|---|---|
| `/web <produk> <vibe>` | Website / landing page |
| `/lap <topik>` | Laporan praktikum / proyek |
| `/skripsi <judul> bab N` | 1 bab skripsi / proposal |
| `/jurnal <topik>` | Artikel ilmiah (IMRaD, abstrak ID+EN) |
| `/riset <topik>` | Literature review dengan sumber nyata |
| `/hum` + teks/file | Humanize (file: hanya prosa yang diubah) |
| `/gl <fitur>` | OpenGL |
| `/pt <topik/soal>` | Packet Tracer |
| `/rs` `/jv` `/xml` | Rust / Java / XML |
| `/and` `/ios` | Android / iOS sistem + app |
| `/gh` | Command push ke GitHub |
| `/lx` `/kali` | Linux / Kali |
| `/ml` `/ds` `/sec` | AI-ML / Data / Security |
| `/cloud` `/full` `/devops` | Cloud / Full stack / DevOps |
| `/prompt <tool> <tujuan>` | Tulis prompt |

## Aturan integritas penting

- Sumber, DOI, kutipan, data, hasil uji, dan angka benchmark tidak pernah dikarang. Klaim tanpa sumber terverifikasi ditandai `[SUMBER: ...]`; hasil cuma dari data/output milik Ryzu.
- Versi, API, flag, dan crate yang nggak yakin ditandai `[uncertain]`, bukan ditebak.
- Humanize memakai `references/humanizer.md` (basis humanizer v4 + stop-slop, ditambah tell khas tulisan ilmiah Indonesia). Tujuannya kualitas tulisan, bukan janji lolos detektor.
- Pentest, Kali, root, kernel, dan jailbreak hanya untuk device/lab sendiri, CTF, atau target yang jelas ber-izin. Malware, stalkerware, bypass kunci/FRP/Activation Lock device orang lain, serangan tanpa izin, dan pencurian kredensial ditolak.
- Hemat limit tapi kerja keras: mikir dalam, output ringkas, verifikasi dengan menjalankan, tidak baca/ulang hal yang sudah ada.

## Search design manual

Butuh Python 3, dijalankan dari folder skill:

```bash
# design system
python ui-ux/scripts/search.py "saas dashboard dark" --design-system -p "NamaProject"

# satu domain
python ui-ux/scripts/search.py "contrast focus" --domain ux

# satu stack
python ui-ux/scripts/search.py "image optimization" --stack nextjs
```

Domain: `ux, style, color, typography, landing, chart, react, web, icons, google-fonts, gsap, product`.
Dial opsional: `--variance 1-10 --motion 1-10 --density 1-10`.
Simpan hasil: `--persist --output-dir <folder>` (`--force` buat menimpa).

## Update repo

```bash
git add .
git commit -m "update: <deskripsi singkat>"
git push
```
