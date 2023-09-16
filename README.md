# Latar Belakang
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur - fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

# Requirements
Dibutuhkan program yang dapat membantu customer membeli barang secara self-service menggunakan bahasa pemrograman Python yang diconvert dalam script dan dijalnkan dapat dijalankan sebagai modular codek:
1. **modul_market_1** = 
Compiled script dari semua fungsi yang dibutuhkan
2. **main** = 
Input dari customer (Test case)
3. **Test Output** = 
Running !phyton main.py

# Flow Chart
![Flow Chart Final Project Pacmann - Ghifari Syuhada](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/d72e646d-0da9-45aa-bace-f3156dfe5676)


# Functions Dibutuhkan
1. **add_item**
    Menambahkan item ke dalam transaksi dalam bentuk:
    item_name = nama dari barang (String)
    item_qty = jumlah dari barang (int)
    item_price = Harga dari barang per 1 unit (int)
2. **update_item_name**
    Mengganti nama item dengan nama baru
    Jika input old_name nya sama dengan item_name yang ada di list, then replace dengan new_name 
3. **update_item_price**
    Mengganti harga item dengan harga baru
    Jika input item_name nya sama dengan item_name yang ada di list, then replace harga yang ada di list denagn new_price
4. **delete_item**
    Menghapus salah satu item yang diinput dengan cara membuat list baru
    kecuali yang namanya sesuai dengan nama yang diinput
6. **reset_transaction**
    menghapus semua isi list
8. **check_order**
    final check terhadap input nama barang, harga barang, dan quantity barang
    apakah semua element tersebut sudah sesuai dengan value nya masing-masing?
10. **total_price**
    Menjumlahkan total harga
12. **display_receipt**
    Melakukan print untuk receipt
14. **apply_discounts**
    Menghitung diskon applicable based on total harga

# Demonstrasi Code
1. **TEST CASE 1**

_Input_

![Input Test Case 1](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/0e1a3339-c711-4ace-9f26-84287ae06502)


_Output_

![Output Test Case 1](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/d01204ee-580c-4704-9066-82d064232140)


2. **TEST CASE 2**

_Input_

![Input Test Case 2](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/81d58c82-fd17-413a-9888-afee5047aa68)


_Output_

![Output Test Case 2](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/b2bf9158-b45a-40d9-9885-2606561f549b)


3. **TEST CASE 3**

_Input_

![Input Test Case 3](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/c9a02095-a007-490f-9d18-f3d53a00541c)


_Output_

![Output Test Case 3](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/ab0ec305-12f5-4fd8-9045-4766d09b491a)


4. **TEST CASE 4**

_Input_

![Output Test Case 4](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/96a3a1a2-7228-4479-80c5-b91cb374ca97)


_Output_

![Input Test Case 4](https://github.com/Moltan22/Super_cashier_ghifari/assets/145213849/8c56e30d-ad78-4d48-a1cf-a25dc44c0892)

# Conclusion
1. This program can be used for simple grocery shopping, while it would be great to also add the flexibility of choosing payment methods and other customized shopping experience for the customers
2. Any further improvement can be revisited after some real market testing and feedback gained from customers
