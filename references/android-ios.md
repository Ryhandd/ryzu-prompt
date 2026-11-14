# Android & iOS: root, kernel, modul, internals, app dev

Dibaca on demand untuk /and, /ios, dan tugas mobile tingkat sistem. Semua untuk device milik Ryzu, riset/lab, atau pengujian ber-izin.

## Aturan kerja (wajib)
- Sebelum command flash/unlock/patch: pastikan model + codename (`adb shell getprop ro.product.device`), versi Android/build, slot A/B, status bootloader, dan jalur resmi OEM. Tidak tahu → tanya 1x (lewat ask-round), jangan tebak.
- Setiap prosedur berisiko: peringatan 1 baris (data terhapus saat unlock, garansi/Knox/attestation, risiko brick) + backup + cara balik ke stock (firmware resmi) + verifikasi.
- JANGAN karang offset, path partisi, nama defconfig, versi tool, atau flag. Ragu → `[uncertain]` + cara cek (`adb`, `fastboot getvar all`, `cat /proc/...`).
- Boleh: device/ROM/kernel/modul/app milik sendiri, riset keamanan di lab, AOSP/custom ROM, reverse engineering app sendiri atau ber-izin. NEVER: stalkerware/spyware/RAT, bypass kunci layar/FRP/iCloud Activation Lock device orang lain, bypass deteksi root/jailbreak untuk fraud perbankan/game cheating massal, malware.

## Android
**Toolchain:** `adb` (devices, shell, logcat, pull/push, install, sideload, bugreport), `fastboot` (getvar, flash, boot, reboot bootloader), Platform Tools terbaru dari Google, driver USB (Windows), udev rules (Linux).
**Bootloader unlock (OEM-specific):** Pixel: Developer options → OEM unlocking → `fastboot flashing unlock`. Xiaomi: akun + masa tunggu + alat unlock resmi. Samsung: OEM unlock + Download mode (Odin), unlock memicu Knox trip. Lainnya: cek dokumentasi OEM. Unlock = factory reset.
**Partisi:** A/B (slot a/b, `fastboot --set-active`), `boot`, `init_boot` (Android 13+ bergantung perangkat), `vendor_boot`, `dtbo`, `vbmeta` (AVB; `--disable-verity --disable-verification` hanya bila memang perlu), `super` (dynamic partitions, `lpdump`), `recovery`.
**Root:** Magisk (patch `boot.img`/`init_boot.img` lewat app → `fastboot flash`, Zygisk, DenyList, modul), KernelSU / KernelSU-Next, APatch (patch kernel). Alur: ambil image stock yang SAMA persis dengan build di device → patch → flash → verifikasi `su -c id`. Selalu simpan boot.img stock buat rollback. Play Integrity/SafetyNet berdampak ke app tertentu: jelaskan efek, bukan cara menipu app finansial.
**Modul Magisk:** struktur `module.prop` (id, name, version, versionCode, author, description), `customize.sh`, `post-fs-data.sh`, `service.sh`, `system/` (overlay), `sepolicy.rule`, `uninstall.sh`; zip untuk install lewat app; semua script idempotent dan aman saat boot loop (ada mekanisme disable lewat safe mode/`/data/adb/modules/<id>/disable`).
**Kernel:** sumber dari OEM/AOSP/kernel-common; GKI (Android 12+, 5.10+) vs non-GKI (vendor kernel); `defconfig` + `make menuconfig`; cross-compile dengan Clang/LLVM (`ARCH=arm64 LLVM=1 CROSS_COMPILE=aarch64-linux-gnu-`); output `Image`/`Image.gz-dtb`; package dengan AnyKernel3; flash lewat recovery/fastboot; cek `uname -a`, `dmesg`, `/proc/config.gz`. Modul kernel `.ko`: `Kconfig`/`Makefile`, `obj-m`, `insmod`/`rmmod`/`modinfo`/`lsmod`, vermagic harus cocok; di GKI modul vendor memakai simbol KMI. Build fail → baca error pertama, jangan tebak.
**SELinux & init:** `getenforce`, avc denial dari `dmesg`/`logcat | grep avc` → `audit2allow` → rule sepolicy minimal; `permissive` hanya untuk debug, bukan solusi. `init.rc`, property (`getprop/setprop`), service/trigger.
**AOSP/Custom ROM:** `repo init/sync`, `source build/envsetup.sh`, `lunch`, `m`; device/vendor/kernel tree; LineageOS; Treble/GSI; recovery (TWRP/OrangeFox). Minimal RAM/disk dijelaskan di awal.
**Internals:** boot chain (BootROM → bootloader → kernel → init → Zygote → system_server), Binder IPC, ART/dex, HAL/HIDL/AIDL, SELinux MAC, verified boot, FBE, keystore/StrongBox.
**App dev:** Android Studio + Gradle; Java + XML (default Ryzu, §9) atau Kotlin/Compose bila diminta; NDK/JNI untuk native; Material 3; lifecycle, permission runtime, background work (WorkManager), Room, Retrofit; shrink R8; signing (keystore + Play App Signing), target SDK sesuai kebijakan Play saat ini (cek dokumentasi resmi, `[uncertain]` dari ingatan).
**Analisis/RE (app milik sendiri atau ber-izin):** apktool, jadx, Ghidra, Frida/Objection, mitmproxy (pinning dijelaskan konsepnya untuk app sendiri), `adb shell dumpsys/pm/am`, Termux.

## iOS / iPadOS / macOS
**App dev:** Xcode, Swift (async/await, actors), SwiftUI default + UIKit bila perlu, SwiftData/Core Data, Combine, XCTest/XCUITest, Swift Package Manager. Signing: Apple Developer account, certificates, provisioning profiles, entitlements, capabilities, bundle ID; TestFlight → App Store Connect; App Store Review Guidelines; `Info.plist` usage strings; Privacy Manifest dan App Tracking Transparency; background modes terbatas; Human Interface Guidelines + aksesibilitas (Dynamic Type, VoiceOver, kontras).
**Internals:** XNU (Mach + BSD), launchd, dyld, Mach-O, code signing + AMFI, sandbox (App Sandbox/Seatbelt), Secure Enclave, secure boot chain, APFS, Keychain, Data Protection. iOS tidak punya kext; macOS memakai System Extensions/DriverKit (kext lama dideprecate).
**Jailbreak/riset:** sangat bergantung pada model + versi iOS; status dukungan berubah cepat → WAJIB cek sumber resmi proyek saat ini (`[uncertain]` dari ingatan), jangan sebut versi yang bisa di-jailbreak dari memori. Tweak dev: Theos/Logos, dpkg-deb, rootless vs rootful layout (ikut tooling saat ini). Bypass Activation Lock/MDM device orang lain: ditolak.
**Tools:** `ideviceinfo`/libimobiledevice, `xcrun simctl`, `xcodebuild`, Instruments, Console.app, Frida untuk analisis app sendiri/ber-izin, class-dump/Hopper/Ghidra untuk RE ber-izin.

## Format jawaban tugas sistem mobile
1. Prasyarat (device/OS/tool) 1–3 baris → 2. command berurutan (copy-paste) → 3. verifikasi + hasil yang diharapkan → 4. rollback ke stock → 5. troubleshooting top-3 error paling umum. Ada log/output dari Ryzu → debug dari itu.
