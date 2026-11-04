# Project Simple ETL with Pandas

⚠️ **Disclaimer:** Dataset yang digunakan dalam repositori ini bersifat **fiktif (mock data)**. Data ini dibuat secara mandiri untuk mereplikasi struktur dan studi kasus *Data Engineer Challenge (DQThon)* dari platform pembelajaran **DQLab**, tanpa membagikan data asli yang bersifat tertutup.

Proyek Data Engineering sederhana ini menerapkan proses ETL (Extract, Transform, Load) menggunakan library **Pandas** di Python. Proyek ini bertujuan untuk membersihkan, menstrukturkan, dan menstandarkan format data mentah peserta hackathon agar siap diimpor ke dalam *relational database* seperti MySQL.

## 🚀 Fitur Utama & Transformasi Data

Proyek ini melakukan beberapa tahap manipulasi dan pembersihan data, antara lain:
1. **Ekstraksi Teks dengan Regex:** Mengambil data spesifik seperti **Kode Pos** dan **Kota** dari kolom alamat yang panjang dan tidak terstruktur.
2. **Data Cleansing (Pembersihan Data):** Menyeragamkan format nomor telepon (mengubah awalan `+62` atau `62` menjadi `0`, serta menghapus tanda baca dan spasi).
3. **Pembuatan Kolom Dinamis (Lambda & Apply):** Membuat kolom **Nama Tim** yang merupakan gabungan inisial nama depan, nama belakang, negara, dan inisial institusi.
4. **Logika Kondisional Spesifik:** Menghasilkan alamat **Email** peserta secara otomatis berdasarkan aturan bisnis tertentu (misal: membedakan format *domain* email antara institusi universitas dan perusahaan/umum).
5. **Standardisasi Format Tanggal (Datetime):** Mengonversi teks string tanggal lahir dan nilai *Unix timestamp* (waktu registrasi) menjadi format `YYYY-MM-DD HH:mm:ss` yang valid dan dapat dibaca oleh sistem MySQL.

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3.x
* **Library:** Pandas, NumPy
* **Konsep:** ETL Pipeline, Regular Expression (Regex), Data Cleansing, Data Transformation

## 📁 Struktur Direktori
```text
Project-Simple-ETL-with-Pandas/
│
├── data/
│   ├── input/
│   │   └── dqthon-participants-mock.csv       # Dataset fiktif replikasi (Mock Data)
│   └── output/
│       └── dqthon-participants-cleaned.csv    # Dataset hasil pembersihan (Siap pakai)
│
├── Project_Simple_ETL_with_Pandas.py          # Skrip utama proses ETL
└── README.md                                  # Dokumentasi proyek
