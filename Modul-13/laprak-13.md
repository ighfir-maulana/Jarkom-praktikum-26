# Modul 13 Protokol Ethernet dan Address Resolution Protocol (ARP)
### Investigasi Struktur Frame Data Link Layer dan Analisis Mekanisme Resolusi Alamat Fisik

Nama    : Ighfir Maulana  
NIM     : 103072400029  
Kelas   : IF-04-04

---

## 📋 Daftar Isi
- [Eksperimen 1: Analisis Frame Ethernet](#-eksperimen-1-analisis-frame-ethernet)
- [Eksperimen 2: Mengamati Aksi Protokol ARP](#-eksperimen-2-mengamati-aksi-protokol-arp)
- [Pertanyaan dan Analisis Mendalam](#-pertanyaan-dan-analisis-mendalam)
- [Kesimpulan](#-kesimpulan)

---

## Eksperimen 1: Analisis Frame Ethernet
1. Pertama, pastikan cache browser kosong. Untuk melakukan hal ini pada Mozilla Firefox V3, pilih Tools -> Clear Recent History dan centang kotak untuk Cache. Untuk Microsoft Edge adalah dengan menekan tombol pintasan Ctrl + Shift + Delete secara bersamaan.
2. Mulai sniffer paket Wireshark.
3. Masukkan URL berikut ke dalam browser http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html Browser akan menampilkan *Bill of Rights AS* yang agak panjang.
4. Hentikan penangkapan paket Wireshark.
5. Temukan nomor paket (kolom paling kiri
pada window Wireshark bagian atas) dari pesan HTTP GET yang dikirim dari komputer Anda
ke gaia.cs.umass.edu
6. Temukan awal dari pesan HTTP yang dikirim ke komputer Anda oleh `gaia.cs.umass.edu`.
![tampila GET](../Assets/Modul13-1.png)

Berdasarkan praktik paket HTTP GET yang dipilih, struktur frame Ethernet II yang terisolasi memiliki karakteristik sebagai berikut.
- Destination MAC Address: `TendaTechnol_1f:62:80 (d8:32:14:1f:62:80)` (Alamat fisik perangkat next-hop yang menjembatani laptop menuju internet).
- Source MAC Address: Intel_2b:6e:b6 (44:af:28:2b:6e:b6) (Alamat fisik kartu jaringan / NIC laptop praktikan).
- Type Field: 0x0800 (Menandakan bahwa payload di dalam frame Ethernet ini mengangkut paket protokol IPv4).

![analisis frame Ethernet II](../Assets/Modul13-2.png)

**Mengapa Alamat MAC Tujuan pada Frame Ethernet HTTP GET bukan milik Server gaia.cs.umass.edu?**

Frame Ethernet beroperasi pada Data Link Layer (Layer 2), yang bertanggung jawab untuk pengiriman hop-ke-hop dalam satu jaringan lokal (LAN) yang sama. Karena server gaia.cs.umass.edu berada di luar jaringan lokal praktikan, komputer klien tidak bisa langsung mengirimkan frame fisik ke server tersebut. Oleh karena itu, Alamat MAC tujuan diarahkan ke Default Gateway (Router Lokal), sedangkan alamat IP server tujuan tetap dijaga di dalam header IP (Layer 3).

## Eksperimen 2: Mengamati Aksi Protokol ARP
Saya melakukan praktikum ini menggunakan OS Windows 10.
1. Buka Command Prompt/PowerShell dengan hak akses Administrator.
2. Mengecek isi tabel cache awal dengan `arp -a`.
3. Mengosongkan seluruh tabel cache ARP dengan `arp -d *`.

![cache ARP kosong](../Assets/Modul13-3.png)

4. Pastikan cache browser kosong. Untuk melakukan hal ini pada Mozilla Firefox V3, pilih Tools -> Clear Recent History dan centang kotak untuk Cache. Untuk Microsoft Edge adalah dengan menekan tombol pintasan Ctrl + Shift + Delete secara bersamaan.

![clear cache browser](../Assets/Modul13-4.png)

5. Mulai sniffer paket Wireshark.
6. Masukkan URL berikut ke dalam browser http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html Browser akan menampilkan *Bill of Rights AS* yang agak panjang.
7. Hentikan penangkapan paket Wireshark.

![ARP](../Assets/Modul13-5.png)