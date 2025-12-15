# 📷 Laporan Praktikum Pengolahan Citra Digital (Computer Vision)

Repositori ini berisi **Tugas 1** dan **Tugas 2** pada mata kuliah **Pengolahan Citra Digital (Computer Vision)**.  
Seluruh program dikembangkan menggunakan **Python** dan pustaka **OpenCV**, dengan fokus pada pemrosesan citra dan video secara *real-time*.

---

## 📌 Daftar Isi
1. [Prasyarat](#-prasyarat)
2. [Struktur File](#-struktur-file)
3. [Tugas 1: GUI Filter Citra](#-tugas-1-gui-filter-citra)
4. [Tugas 2: Deteksi Multi-Warna](#-tugas-2-deteksi-multi-warna)
5. [Cara Menjalankan Program](#-cara-menjalankan-program)
6. [Catatan](#-catatan)

---

## 🔧 Prasyarat

Sebelum menjalankan program, pastikan lingkungan Python telah memenuhi kebutuhan berikut:

- Python **3.x**
- OpenCV (`cv2`)
- NumPy

Instalasi dependensi dapat dilakukan dengan perintah:

```bash
pip install opencv-python numpy

.
├── Tugas1.py   # Program GUI Filter Citra
├── Tugas2.py   # Program Deteksi Multi-Warna
└── README.md   # Dokumentasi proyek
```

** Tugas 1: GUI Filter Citra**

Nama File: Tugas1.py



Program ini merupakan aplikasi pengolahan citra real-time menggunakan webcam yang dilengkapi dengan antarmuka grafis (GUI) sederhana.
Pengguna dapat mengganti mode filter citra melalui klik mouse pada tombol visual maupun menggunakan input keyboard.

*Fitur Utama Terdapat empat mode filter citra yang dapat dipilih, yaitu:

Normal (0)
Menampilkan video asli dari webcam tanpa proses filtering.

Average Blur (1)
Menggunakan metode Average Blurring dengan kernel berukuran 9×9 untuk menghaluskan citra.

Gaussian Blur (2)
Mengimplementasikan Gaussian Blur dengan kernel 15×15 yang dihitung secara manual menggunakan perkalian kernel 1D.

Sharpen (3)
Mempertajam citra menggunakan kernel konvolusi kustom:

[ 0  -1   0 ]
[ -1  5  -1 ]
[ 0  -1   0 ]


**Tugas 2: Deteksi Multi-Warna**

Nama File: Tugas2.py

Program ini bertujuan untuk mendeteksi dan melacak objek berdasarkan warna tertentu secara real-time menggunakan ruang warna HSV (Hue, Saturation, Value).
Objek yang terdeteksi akan ditandai dengan Bounding Box dan label warna.

* Fitur Utama

Program dikonfigurasi untuk mendeteksi empat warna sekaligus, yaitu:

🔴 Merah
Menangani wrap-around hue pada rentang 0–10 dan 170–180

🟢 Hijau

🔵 Biru

🟡 Kuning

⚙️ Cara Kerja

Konversi Warna
Frame video dikonversi dari format BGR ke HSV.

Masking Warna
Mask biner dibuat berdasarkan nilai lower dan upper HSV yang telah didefinisikan pada konfigurasi colors_config.

Morphological Operations

Operasi Opening dan Closing

Menggunakan kernel berukuran 5×5

Bertujuan untuk menghilangkan noise kecil pada hasil deteksi

Kontur dan Bounding Box

Mencari kontur dari area yang terdeteksi

Hanya kontur terbesar dengan luas area > 500 piksel yang diproses

Menggambar:

Kotak pembatas (rectangle)

Label nama warna pada frame output
