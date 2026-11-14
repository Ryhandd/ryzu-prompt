# Knowledge base: cara menerapkan 17 area kompetensi
Dibaca on demand. Tiap area = aturan terapan, bukan definisi. Ragu fakta/versi → `[uncertain]`, cek dokumentasi resmi bila ada web.

## 1. Logika & pemecahan masalah
Sebelum kode non-trivial: input/output, constraint, edge case (kosong, besar, duplikat, negatif, concurrency) → pecah jadi langkah kecil → pseudocode bila algoritmanya tidak jelas → pilih struktur data → sebut kompleksitas waktu/ruang → uji dengan contoh kecil + edge. Algoritma: pilih yang sederhana dan benar dulu, optimasi bila ada bukti perlu.

## 2. OS, jaringan, database
OS (Windows/Linux/macOS): proses/thread, scheduling, memori virtual, file system, syscall, permission. Jaringan: OSI/TCP-IP, IP/subnet, DNS, HTTP/HTTPS/TLS, NAT, router vs switch; diagnosis berurutan L1→L7 (`ping`, `traceroute`, `dig`, `ss`, `curl -v`, `tcpdump`). Database: normalisasi dulu, indeks sesuai query, ACID/transaksi, pilih SQL vs NoSQL berdasar pola akses (relasional/konsistensi vs skala/skema fleksibel), baca `EXPLAIN`, cegah N+1, migrasi bertahap, backup + uji restore.

## 3. Pemrograman & version control
Bahasa mengikuti jalur (Python, JS/TS, C++, Java, Rust). Git: branch kecil, conventional commits, PR dengan deskripsi, jangan commit secret/artefak build, `.gitignore` benar, rebase vs merge dijelaskan 1 baris bila relevan. GitHub: issues, PR, Actions, branch protection, releases/tags.

## 4. Cloud, cybersecurity, AI & data
Cloud AWS/GCP/Azure (§11 SKILL.md). Security dasar: enkripsi (at-rest/in-transit), firewall/segmentasi, authn vs authz, MFA, least privilege, OWASP Top 10, patching, logging. AI/Data: statistik dasar, pipeline data, evaluasi model yang jujur (§11).

## 5. Soft skills
Adaptasi: cek dokumentasi resmi untuk versi terkini sebelum menyatakan fakta cepat-berubah. Komunikasi: diminta menjelaskan ke non-teknis → analogi sehari-hari, tanpa jargon, hasil dulu baru detail, 1 ide per paragraf.

## 6. Container, CI/CD, CLI
Docker multi-stage, non-root, healthcheck; Kubernetes (probes, limits, RBAC); CI/CD lint→test→build→scan→deploy, rollback jelas. CLI: berikan command siap salin, flag dijelaskan hanya bila tidak jelas, idempotent, ada dry-run bila destruktif.

## 7. UI/UX & aksesibilitas
Proses: user → tugas → alur → wireframe → visual. Heuristik Nielsen, hierarki visual, konsistensi, feedback, empty/loading/error state. Aksesibilitas target WCAG 2.2 AA: kontras, fokus, keyboard, label, alt, target sentuh, reduced-motion, screen reader. Detail visual ikut §4.

## 8. Agile & dokumentasi
Agile/Scrum: user story (`Sebagai … saya ingin … agar …`), acceptance criteria, Definition of Done, sprint planning/review/retro, backlog diprioritaskan nilai. Dokumentasi: README (apa, install, pakai, kontribusi), API docs (OpenAPI), CHANGELOG (Keep a Changelog), ADR untuk keputusan arsitektur, runbook ops. Tulis untuk anggota tim baru.

## 9. Regulasi, bisnis, debugging
Privasi: UU PDP (UU No. 27 Tahun 2022) dan GDPR: dasar hukum/persetujuan, minimisasi data, tujuan terbatas, hak subjek data, retensi, enkripsi, notifikasi insiden, DPA/vendor. Ini panduan teknis, bukan nasihat hukum. Bisnis: tiap fitur terhubung ke nilai (biaya, pendapatan, risiko, waktu); sebut trade-off dan ukuran sukses. Debugging sistematis: reproduksi → isolasi → hipotesis → verifikasi (log/bukti) → perbaiki akar masalah → tes regresi. Jangan menebak banyak perubahan sekaligus.

## 10. API, system design, arsitektur
API: REST (resource, status code benar, idempotency, pagination, versioning, error format konsisten, rate limit, auth), GraphQL (kapan cocok: klien beragam/overfetching; waspada N+1, depth limit). System design: tanya kebutuhan fungsional/non-fungsional → estimasi beban → komponen (LB, cache, DB, queue, CDN) → bottleneck → skala (replika, shard, cache) → trade-off (CAP/konsistensi) → failure modes. Microservices vs monolith: default modular monolith; pecah ke microservices hanya bila ada alasan nyata (tim/skala/deploy independen) dan sanggup menanggung kompleksitas operasional.

## 11. QA & observability
Piramida tes: banyak unit, secukupnya integration, sedikit e2e; test deterministic, cepat, bukan sekadar mengejar coverage; regression test untuk tiap bug. Observability: log terstruktur, metrik (RED/USE), trace (OpenTelemetry), SLI/SLO, alert yang actionable, dashboard.

## 12. Era AI & otomasi
Prompt engineering (§5). Integrasi LLM: streaming, timeout/retry, batas token + biaya, eval set, guardrails, secret di server bukan klien, jangan kirim data sensitif tanpa izin. Otomasi: skrip (bash/Python/cron) dulu; n8n/Make/Zapier bila alur berbasis SaaS; idempotent + log + notifikasi gagal.

## 13. FinOps & Green IT
FinOps: tagging + budget/alert, right-sizing, autoscaling, savings plans/reserved/spot untuk beban sesuai, storage tiering/lifecycle, matikan resource idle, hitung unit cost. Green IT: kode efisien, cache, right-size, pilih region lebih bersih bila bisa, jadwalkan batch off-peak, kompres aset.

## 14. Disaster recovery & incident response
DR: tentukan RPO/RTO, backup 3-2-1, uji restore berkala, multi-AZ/region sesuai kebutuhan, runbook failover. Incident response (alur NIST): persiapan → deteksi & analisis → containment/eradication/recovery → pasca-insiden. Komunikasi krisis: status jelas, jam update teratur. Post-mortem blameless: timeline, dampak, akar masalah, yang berjalan baik, action item ber-owner + tenggat.

## 15. Tata kelola & sistem warisan
Legacy: pahami dulu (characterization tests), migrasi bertahap (strangler fig), tidak big-bang, jaga operasional, rollback tiap tahap. Framework: ITIL 4 (incident/change/problem management), ISO/IEC 27001 (ISMS, risk assessment, kontrol Annex A), NIST CSF sebagai peta fungsi. Jelaskan ringkas dan terapkan ke checklist nyata, bukan teori.

## 16. Teknologi batas
Edge/IoT: sensor → MCU/SBC (ESP32, Raspberry Pi) → MQTT/CoAP → edge processing → cloud; OTA update, power, keamanan perangkat. Web3: Solidity, smart contract (uji dengan Foundry/Hardhat; waspada reentrancy, access control, integer, oracle), use case non-kripto (provenance, audit trail); bukan nasihat finansial. Kuantum: konsep qubit/superposisi/entanglement, Shor/Grover berdampak ke kripto publik-key; migrasi ke post-quantum (standar NIST: ML-KEM, ML-DSA) dibahas sebagai perencanaan.

## 17. Leadership teknis & open source
Technical debt: catat di debt register (dampak, biaya bayar, risiko), ambil jalan pintas hanya dengan keputusan sadar + tenggat bayar, refactor saat sentuh area itu atau bila debt memperlambat tim/risiko tinggi. Open source: pahami lisensi (MIT, Apache-2.0, BSD permisif; GPL/AGPL copyleft), kompatibilitas lisensi, audit dependensi (`npm audit`, `cargo audit`, `pip-audit`, Dependabot), SBOM, pin versi, kontribusi lewat issue → fork → PR sesuai CONTRIBUTING.
