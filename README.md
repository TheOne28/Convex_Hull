# Tugas Kecil 2 : Convex Hull

Vincent Prasetiya Atmadja  
13520099

Repository ini dibuat dalam rangka memenuhi tugas kecil 2 mata kuliah Strategi Algoritma Semester 4 Tahun 2021/2022

## Table of Contents

- [Deskripsi Program](#deskripsi-program)
- [Struktur Repository](#struktur-repository)
- [Requirement](#requirements)
- [How to Use](#how-to-use)

## Deskripsi Program

Repository ini berisi library convexHull dengan memanfaatkan algoritma Divide and Conquer. Libray kemudian akan diterapkan pada main program dengan memanfaatkan beberapa dataset yang disediakan oleh scipy, yaitu Iris, Breast_Cancer, dan Wine. Hasil library kemudian akan di plot dengan memanfaatkan library matplotlib

## Struktur Repository  

Repository ini terdiri dari 4 directory yaitu sebagai berikut

1. **src**, directory berisi source code
2. **test**, directory berisi input.txt dan beberapa contoh hasil output
3. **doc**, directory berisi laporan dan spek tugas

## Requirements

Dalam pembuatannya, saya menggunakan Python 3.10.1 dengan memanfaatkan beberapa library yaitu

1. **matplotpib**, untuk memplot data dan menampilkan convex hull
2. **pandas**, untuk mengolah data  
3. **sklearn**, untuk memberikan beberapa dataset dasar
4. **copy**, untuk membuat copy dari variable
5. **math**, untuk menghitung arccos dan menmbandingkan 2 float

## How to Use

Berikut adalah langkah yang dapat diikuti untuk menggunakan program ini.

1. Clone repository ini.
2. Install beberapa library yang belum tersedia pada python secara umum. Library tersebut dicantumkan di requirements.txt dan dapat dinstall dengan menggunakan command pip (Apabila belum terdapat pip, silahkan menginstall pip terlebih dahulu ([Install Pip](https://pip.pypa.io/en/stable/installation/)) ) di bawah ini.  
    `pip install -r requirements.txt`
3. Open terminal dan pindahkan working directory ke folder src.
4. Jalankan program main.py dan penuhi input yang diinginkan program.

Langkah 3 dan 4 dapat dijalankan dengan menggunakan command shell berikut ini.

```shell
cd src
python .\main.py
```
