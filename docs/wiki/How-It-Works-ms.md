# Cara Ia Berfungsi

🌐 [English](How-It-Works) · [Dansk](How-It-Works-da) · **Bahasa Melayu**

## Kaedahnya

Robot mengikut dinding kanan:

1. Berjalan ke hadapan sehingga terkena dinding, kemudian pusing ke kiri. Ini meletakkan dinding di sebelah kanan dan mengelakkan perjalanan tanpa penghujung di ruang terbuka.
2. Sehingga matlamat dicapai: jika sebelah kanan kosong, pusing ke kanan dan bergerak; jika tidak, jika bahagian hadapan kosong, bergerak; jika tidak, pusing ke kiri.

Dunia Reeborg tiada "pusing ke kanan", jadi pusing ke kanan ialah tiga kali pusing ke kiri.

## Bahagian-bahagiannya

| Lapisan | Folder dalam `src/reeborg_maze` | Kandungannya |
| --- | --- | --- |
| Domain | `domain/` | Peraturan mengikut dinding dan antara muka robot; tidak mengimport yang lain |
| Aplikasi | `application/` | Kes guna yang menyelesaikan fail dunia, dan port yang diperlukannya |
| Infrastruktur | `infrastructure/` | Simulator tanpa talian dan pembaca fail dunia Reeborg |
| Persembahan | `presentation/` | Baris arahan, lukisan teks dan skrip untuk ditampal ke dunia Reeborg |

Skrip dalam `presentation/reeborg_script.py` mengulang peraturan itu kerana dunia Reeborg tidak boleh mengimport kod. Satu ujian menjalankan skrip terhadap simulator dari setiap permulaan yang kosong, supaya kedua-dua salinan tidak boleh menyimpang.
