# Modul 14 Protokol Jaringan Nirkabel IEEE 802.11 (Wi-Fi)
### Investigasi Mekanisme Transmisi Nirkabel, Beaconing, dan Manajemen Asosiasi Paket

Nama    : Ighfir Maulana  
NIM     : 103072400029  
Kelas   : IF-04-04

---

## 📋 Daftar Isi
- [1. Topologi & Skenario Aktivitas Jejak](#1-topologi--skenario-aktivitas-jejak)
- [2. Analisis Eksperimen 1: Beacon Frames](#2-analisis-eksperimen-1-beacon-frames)
- [3. Analisis Eksperimen 2: Data Transfer](#3-analisis-eksperimen-2-data-transfer)
- [4. Analisis Eksperimen 3: Association dan Disassociation](#4-analisis-eksperimen-3-association-dan-disassociation)

---

## 1. Topologi & Skenario Aktivitas Jejak

Berkas jejak diambil pada Saluran 6 (*Channel 6*) di lingkungan jaringan rumah yang terdiri dari perangkat Linksys 802.11g AP/Router, 2 PC kabel, dan satu PC nirkabel (*wireless host*). Alur aktivitas jaringan yang terekam adalah sebagai berikut.
* **Awal**: Host nirkabel telah terasosiasi secara aktif dengan AP bertajuk `30 Munroe St`.
![Awal](../Assets/Modul14-1.png)
* **t = 24.82 detik**: Host melakukan HTTP GET request ke `gaia.cs.umass.edu` (`128.119.245.12`) untuk mengunduh naskah `alice.txt`.
![detik 24.82](../Assets/Modul14-2.png)
* **t = 32.82 detik**: Host melakukan HTTP GET request ke `www.cs.umass.edu` (`128.119.240.19`).
![detik 32.82](../Assets/Modul14-3.png)
* **t = 49.58 detik**: Host melakukan disasosiasi secara sengaja dari AP `30 Munroe St` dan mencoba berasosiasi ke jaringan terkunci `linksys_ses_24086` (gagal terhubung).
![detik 49.58](../Assets/Modul14-4.png)
* **t = 63.00 detik**: Host membatalkan proses pencarian pada AP kedua, lalu berasosiasi kembali secara resmi dengan AP `30 Munroe St`.
![detik 63.00](../Assets/Modul14-5.png)

## 2. Analisis Eksperimen 1: Beacon Frames

*Beacon Frames* dikirimkan secara berkala oleh *Access Point* (AP) untuk mengumumkan parameter keberadaan dan karakteristik teknis jaringan ke lingkungan sekitar.

![Beacon Frames](../Assets/Modul14-6.png)

Berdasarkan analisis sub-bidang `IEEE 802.11 Wireless LAN` pada jendela tengah Wireshark untuk frame Beacon:
- Type / Subtype: `Type: Management frame (0)` dan `Subtype: Beacon frame (8)`. Kombinasi bit biner ini menstandarkan bahwa paket ini untuk kebutuhan manajemen administratif nirkabel.
![Type / Subtype](../Assets/Modul14-7.png)

- SSID Parameter: Menampilkan teks string identitas jaringan (misal: 30 Munroe St).
- Supported Rates: Mengiklankan kapasitas kecepatan transmisi data maksimum yang didukung oleh interface fisik AP.
![Supported Rates](../Assets/Modul14-8.png)

## 3. Analisis Eksperimen 2: Data Transfer
Analisis transfer data nirkabel diamati pada jendela waktu pengunduhan berkas teks `alice.txt` pada saat komponen enkapsulasi layer atas mulai ditransmisikan.

![ARP](../Assets/Modul14-9.png)

Berbeda dengan frame Ethernet kabel standar yang hanya memiliki 2 alamat fisik (*Source* dan *Destination*), frame data 802.11 mengimplementasikan skema 4 alamat fisik di dalam komponen headernya guna menjembatani media nirkabel dan kabel melalui *Distribution System* (DS):
1. Address 1 (*Receiver Address*). Alamat fisik interface nirkabel penerima langsung (biasanya MAC Address dari AP).
2. Address 2 (*Transmitter Address*). Alamat fisik stasiun nirkabel pengirim langsung (MAC Address host klien).
3. Address 3 (*Destination Address*). Alamat fisik tujuan akhir paket data di jaringan kabel (MAC Address dari router / target server luar).
4. Address 4 (*Source Address*). Alamat fisik asal mula pembuat paket data asli di segmen kabel (jika frame datang dari arah luar).

## 4. Analisis Eksperimen 3: Association dan Disassociation
Sesuai kronologi lini masa, proses pemutusan sambungan secara paksa (*Disassociation*) dan pendaftaran kembali (*Association*) terekam secara jelas pada rentang waktu kritis antara `t = 49.58 s` hingga `t = 63.00 s`.

**Mekanisme Detail Pertukaran Pesan Manajemen Jaringan**
1. *Disassociation*. *Disassociation* dikirim oleh host untuk memutuskan ikatan sesi logis yang aktif. Paket ini menggunakan klasifikasi **Type 0 (Management) dengan Subtype 12 (Disassociation)**.
![Disassociation](../Assets/Modul14-10.png)

2. *Association Request*. *Association request* dikirimkan oleh host menuju AP target (linksys_ses_24086 dan kemudian 30 Munroe St) untuk meminta izin pendaftaran parameter enkripsi dan alokasi resource jaringan lokal. *Association request* memiliki karakteristik bertipe **Type 0 (Management) dan Subtype 0 (Association Request)**.
![Association Request](../Assets/Modul14-11.png)

3. *Association Response*. *Association response* dikirimkan balik oleh perangkat AP menuju stasiun host klien sebagai keputusan penerimaan atau penolakan sesi kerja. *Association response* memiliki karakteristik bertipe **Type 0 (Management) dan Subtype 1 (Association Response)**. Di dalamnya memuat status Successful atau alasan kegagalan konektivitas (Status Code).
![Association Response](../Assets/Modul14-12.png)

## 🤝 Kontribusi
Laporan ini disusun sebagai bagian dari tugas praktikum S-1 Informatika Telkom University. Kalau kamu ingin memberikan saran atau perbaikan pada dokumentasi ini, silakan ikuti langkah berikut:
1.  Lakukan **Fork** pada repositori ini.
2.  Buat branch baru untuk fitur atau perbaikan Anda.
3.  Kirimkan **Pull Request** dengan penjelasan mengenai perubahan yang dilakukan.

---
**Informatics Lab - Telkom University**
*Copyright © 2026 - UKM Coder*