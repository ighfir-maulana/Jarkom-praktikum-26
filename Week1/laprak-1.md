# 🌐 Laporan Praktikum Jaringan Komputer Modul 1 & 2
### Running Modul dan Pengenalan Tools

Nama    : Ighfir Maulana
NIM     : 103072400029
Kelas   : IF-04-04

---

## 📋 Daftar Isi
- [Prasyarat & Instalasi](#-prasyarat--instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
  - [Modul 1: Running Modul (Regulasi & Persiapan)](#modul-1-running-modul-regulasi--persiapan)
  - [Modul 2: Pengenalan Tools (Analisis HTTP)](#modul-2-pengenalan-tools-analisis-http)
- [Fitur Utama](#-fitur-utama)
- [Kontribusi](#-kontribusi)

---

## ⚙️ Prasyarat & Instalasi
Sebelum memulai praktikum, pastikan perangkatmu sudah terinstal beberapa perangkat lunak berikut:

1.  **Wireshark**: Alat analisis protokol jaringan (Packet Sniffer).
2.  **Npcap / WinPcap**: Driver yang dibutuhkan agar Wireshark dapat menangkap paket secara real-time.
3.  **Python 3.x**: Dibutuhkan untuk pengembangan skrip jaringan pada modul-modul mendatang.

**Langkah Instalasi:**
* Unduh installer melalui situs resmi [wireshark.org](https://www.wireshark.org/).
* Jalankan proses instalasi dan pastikan opsi **Install Npcap** sudah tercentang.
* Verifikasi instalasi dengan menjalankan aplikasi Wireshark atau melalui terminal dengan perintah `wireshark --version`.

---

## 🚀 Cara Penggunaan

### Modul 1: Running Modul (Regulasi & Persiapan)
Fokus pada tahap ini adalah memastikan kesiapan teknis dan administratif sesuai aturan Laboratorium Informatika:
1.  **Sinkronisasi Aturan**: Memahami kebijakan kehadiran (min. 75%), sistem penilaian, dan larangan penggunaan AI yang tidak sah.
2.  **Uji Coba Software**:
    * Buka Wireshark.
    * Klik `File` -> `Open`.
    * Pilih file contoh `soal1.pcap`.
    * Pastikan daftar paket muncul dengan benar di jendela utama.

### Modul 2: Pengenalan Tools (Analisis HTTP)
Langkah-langkah menangkap lalu lintas data (capture) secara langsung:
1.  Buka Wireshark dan pilih **Interface** yang sedang aktif (misalnya Wi-Fi).
2.  Klik tombol **Start** (ikon sirip hiu biru).
3.  Buka browser dan akses halaman: `http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html`.
4.  Kembali ke Wireshark dan klik **Stop**.
5.  Gunakan kolom filter dan ketik `http` untuk menyaring pesan HTTP GET dan HTTP OK.

> **Catatan:** Amati perbedaan struktur data pada *Packet-listing*, *Packet-header*, dan *Packet-contents*.

---

## ✨ Fitur Utama
* **Audit Kesiapan Sistem**: Memastikan lingkungan kerja siap untuk skenario jaringan yang lebih kompleks.
* **Real-time Packet Capturing**: Mengamati aliran data mentah yang melewati kartu jaringan (NIC).
* **Deep Packet Inspection (DPI)**: Analisis mendalam pada berbagai lapisan protokol (Ethernet, IP, TCP, dan HTTP).
* **Visualisasi Hierarki Protokol**: Menampilkan struktur header paket secara terperinci untuk memudahkan identifikasi masalah jaringan.

---

## 🤝 Kontribusi
Laporan ini disusun sebagai bagian dari tugas praktikum S1 Informatika Telkom University. Jika Anda ingin memberikan saran atau perbaikan pada dokumentasi ini, silakan ikuti langkah berikut:
1.  Lakukan **Fork** pada repositori ini.
2.  Buat branch baru untuk fitur atau perbaikan Anda.
3.  Kirimkan **Pull Request** dengan penjelasan mengenai perubahan yang dilakukan.

---
**Informatics Lab - Telkom University** *Semester Genap 2025/2026*