# Deteksi Objek pada Mobil menggunakan Streamlit

Proyek ini merupakan aplikasi berbasis Streamlit untuk mendeteksi objek pada gambar mobil menggunakan dua model deteksi objek yang populer: **RetinaNet** dan **Faster-RCNN**. Pengguna dapat mengunggah gambar, dan hasil deteksi dari kedua model akan ditampilkan secara berdampingan untuk perbandingan.

---

## Fitur Utama
- **Unggah Gambar:** Unggah gambar mobil untuk dilakukan deteksi objek.
- **Dua Model Deteksi:**
  - **RetinaNet**: Model deteksi objek yang efisien dan cepat.
  - **Faster-RCNN**: Model deteksi objek yang akurat dengan jaringan proposal wilayah.
- **Perbandingan Visual:** Hasil deteksi dari kedua model ditampilkan dalam dua kolom untuk perbandingan langsung.

---

## Persyaratan Sistem
- Python 3.8 atau lebih baru
- Paket yang diperlukan terdapat dalam `requirements.txt`
- Streamlit untuk antarmuka pengguna
- Google Drive untuk model yang telah dilatih

---

## Instalasi
1. Clone repositori ini:
   ```bash
   git clone https://github.com/Ucuuuppp/UAP
   cd UAP
   ```

2. Install semua dependensi:
   ```bash
   pip install -r requirements.txt
   pip install git+https://github.com/facebookresearch/detectron2.git
   ```

3. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## Struktur Proyek
```
repo-name/
├── app.py                  # Aplikasi utama Streamlit
├── requirements.txt        # Daftar dependensi
├── install.py              # Instalasi tambahan untuk library
├── README.md               # Dokumentasi proyek
├── models/                 # Model yang telah dilatih
└── ...
```

---

## Penggunaan
1. Jalankan aplikasi menggunakan perintah `streamlit run main.py`.
2. Unggah gambar dengan format JPG, JPEG, atau PNG.
3. Aplikasi akan memproses gambar menggunakan kedua model.
4. Hasil deteksi akan ditampilkan dalam dua kolom:
   - Kolom kiri: Output dari RetinaNet
   - Kolom kanan: Output dari Faster-RCNN

---

## Perbandingan Loss Kedua Model
Berikut adalah tabel perbandingan metrik loss untuk kedua model:

| **Model**       | **Total Loss**  |
|------------------|----------------|
| **RetinaNet**    | 0.4739          |
| **Faster-RCNN**  | 0.4577|

- **RetinaNet** menunjukkan total loss yang sedikit lebih tinggi, namun lebih cepat dalam inferensi.
- **Faster-RCNN** memberikan hasil yang lebih akurat tetapi membutuhkan waktu inferensi lebih lama.

---

## Model yang Digunakan
Model yang telah dilatih dapat diunduh dari Google Drive:
1. [Faster-RCNN](https://drive.google.com/drive/folders/1o08O30SP23uskXhIHZuQxXSNeEzbUcHh?usp=sharing)
2. [RetinaNet](https://drive.google.com/drive/folders/1Zenq1klMwcDvPXblZ2au92vm7L8KE8se?usp=sharing)

Unduh model ke dalam root direktori `.` sebelum menjalankan aplikasi.

---

## Catatan
- Model telah dilatih pada dataset COCO, sehingga performa pada dataset lain mungkin berbeda.
- Pastikan GPU tersedia untuk mempercepat inferensi jika memungkinkan.

---

## Kontribusi
1. Fork repositori ini.
2. Buat branch fitur baru:
   ```bash
   git checkout -b fitur-baru
   ```
3. Commit perubahan Anda:
   ```bash
   git commit -m "Menambahkan fitur baru"
   ```
4. Push ke branch Anda:
   ```bash
   git push origin fitur-baru
   ```
5. Buat Pull Request.

---