# Laporan Praktikum Pengolahan Citra Digital (Computer Vision)

Repositori ini berisi kode sumber dan dokumentasi untuk **Tugas 1** dan **Tugas 2** sebagai bagian dari laporan praktikum Pengolahan Citra Digital. Proyek ini menggunakan Python dan pustaka OpenCV untuk manipulasi citra dan deteksi objek secara *real-time*.

## Daftar Isi
1. [Prasyarat](#prasyarat)
2. [Tugas 1: GUI Filter Citra](#tugas-1-gui-filter-citra)
3. [Tugas 2: Deteksi Multi-Warna](#tugas-2-deteksi-multi-warna)
4. [Cara Menjalankan Program](#cara-menjalankan-program)

---

## Prasyarat

Sebelum menjalankan program, pastikan pustaka berikut telah terinstal di lingkungan Python Anda:

* Python 3.x
* OpenCV (`cv2`)
* NumPy

Instalasi dependensi dapat dilakukan dengan perintah:

Tugas 1: GUI Filter Citra
File: Tugas1.py

Deskripsi
Program ini merupakan aplikasi pengolahan citra real-time yang menyediakan antarmuka grafis (GUI) sederhana berupa tombol di layar untuk mengganti mode filter citra. Pengguna dapat berinteraksi menggunakan klik mouse pada tombol visual atau menggunakan tombol keyboard.

Fitur Utama
Program ini memiliki 4 mode filter yang dapat dipilih:

Normal ('0'): Menampilkan video asli dari webcam tanpa filter.

Avg Blur ('1'): Menggunakan Average Blurring dengan kernel ukuran 9x9 untuk menghaluskan citra.

Gaussian ('2'): Mengimplementasikan Gaussian Blur menggunakan kernel 15x15 yang dikalkulasi secara manual (perkalian matriks kernel 1D).

Sharpen ('3'): Mempertajam citra menggunakan kernel konvolusi kustom [[0, -1, 0], [-1, 5, -1], [0, -1, 0]].

Cara Kerja
Interaksi Mouse: Program mendeteksi klik kiri mouse. Jika koordinat klik berada di dalam area kotak tombol yang digambar, mode filter akan berubah.

Indikator Visual: Tombol mode yang aktif akan berubah warna menjadi hijau, sementara yang tidak aktif berwarna abu-abu. Teks status mode aktif juga ditampilkan di pojok kiri atas.


Tugas 2: Deteksi Multi-Warna
File: Tugas2.py

Deskripsi
Program ini bertujuan untuk mendeteksi dan melacak objek berdasarkan warna tertentu menggunakan ruang warna HSV (Hue, Saturation, Value). Program akan menggambar Bounding Box (kotak pembatas) di sekitar objek yang terdeteksi.

Fitur Utama
Program dikonfigurasi untuk mendeteksi 4 warna sekaligus:

🔴 Merah (Menangani wrap-around hue pada rentang 0-10 dan 170-180).

🟢 Hijau

🔵 Biru

🟡 Kuning

Cara Kerja
Konversi Warna: Mengubah frame video dari BGR ke HSV.

Masking: Membuat mask biner berdasarkan rentang warna lower dan upper yang telah ditentukan dalam konfigurasi colors_config.

Morphological Operations: Menggunakan operasi Opening dan Closing dengan kernel 5x5 untuk menghilangkan noise (bintik-bintik kecil) pada hasil deteksi.

Kontur & Bounding Box:

Mencari kontur dari area yang terdeteksi.

Hanya mengambil kontur terbesar dengan luas area > 500 piksel untuk menghindari deteksi palsu.

Menggambar persegi panjang (rectangle) dan label nama warna pada frame output.
