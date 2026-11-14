# ryzu-prompt

Personal operating system buat AI (always-on: otomatis jalan di semua prompt, tanpa perlu `/ryzu-prompt`): website modern/premium, laporan/karya ilmiah/skripsi (humanized), OpenGL 3D, Cisco Packet Tracer, Rust/Java/XML, Linux (Kali/Debian), AI/ML, data science, cloud, DevOps, full stack, cybersecurity (defensif/authorized), design, dan nulis prompt buat tool AI lain. Hemat token, scope disiplin, hasil dikirim sebagai zip file yang berubah aja.

## Isi

```
ryzu-prompt/
├── SKILL.md                      # instruksi utama skill
├── references/
│   └── humanizer.md              # pola tulisan AI + cara bersihin (ID/EN)
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

Untuk tool lain, taruh folder ini di lokasi skills tool tersebut.

## Pemakaian

Panggil dengan `/ryzu-prompt`, atau kata kunci seperti "buatin prompt" / "bikin website".

Shortcut: `/web` `/lap` `/skripsi` `/jurnal` `/riset` `/hum` `/gl` `/pt` `/rs` `/jv` `/xml` `/lx` `/kali` `/ml` `/ds` `/sec` `/cloud` `/full` `/devops` `/prompt` (detail di SKILL.md §11).

Search manual (butuh Python 3):

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
Simpan hasil: `--persist --output-dir <folder>` (`--force` buat timpa).

## Update

```bash
git add .
git commit -m "update: <deskripsi singkat>"
git push
```
