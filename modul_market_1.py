#Membuat list kosong untuk transaksi baru
transaction_data = []

#Creating functions:
    #Menambahkan item ke dalam transaksi dalam bentuk:
    #item_name = nama dari barang (String)
    #item_qty = jumlah dari barang (int)
    #item_price = Harga dari barang per 1 unit (int)
def add_item(item_name, item_qty, item_price):
    global transaction_data #defining list as global supaya bisa dipakai oleh functions lain
    transaction_data.append({
        "item_name": item_name,
        "item_qty": item_qty,
        "item_price": item_price,
    })

#Creating functions:
    #Mengganti nama item dengan nama baru
    #Jika input old_name nya sama dengan item_name yang ada di list, then replace dengan new_name 
def update_item_name(old_name, new_name):
    global transaction_data
    for item in transaction_data:
        if item["item_name"] == old_name:
            item["item_name"] = new_name

#Creating functions:
    #Mengganti harga item dengan harga baru
    #Jika input item_name nya sama dengan item_name yang ada di list, then replace harga yang ada di list denagn new_price
def update_item_price(item_name, new_price):
    global transaction_data
    for item in transaction_data:
        if item["item_name"] == item_name:
            item["item_price"] = new_price

#Creating functions:
    #Menghapus salah satu item yang diinput dengan cara membuat list baru
    #kecuali yang namanya sesuai dengan nama yang diinput
def delete_item(item_name):
    global transaction_data
    transaction_data = [item for item in transaction_data if item["item_name"] != item_name]

#Creating functions:
    #menghapus semua isi list
def reset_transaction():
    global transaction_data
    transaction_data = []

#Creating functions:
    #final check terhadap input nama barang, harga barang, dan quantity barang
    #apakah semua element tersebut sudah sesuai dengan value nya masing-masing?
def check_order():
    global transaction_data
    for item in transaction_data:
        if not isinstance(item["item_name"], str) or not item["item_name"]: #Jika item name bukan string ATAU jika item name kosong maka return text
            return "Terdapat kesalahan input data"
    for item in transaction_data:
        if not isinstance(item["item_price"], int) or item["item_price"] <= 0: #Jika item price bukan integer ATAU jika item price kurang dari nol maka return text
            return "Terdapat kesalahan input data"
    for item in transaction_data:
        if not isinstance(item["item_qty"], int) or item["item_qty"] <= 0: #Jika item qty bukan float ATAU jika item qty kurang dari nol maka return text
            return "Terdapat kesalahan input data"
    for item in transaction_data:
        if item["item_name"] == "":  #Jika item kosong maka return text
            return "Pesanan dihapus!" 
    return "Pemesanan sudah benar" #Jika semua aman return text

#Creating functions:
     #Menjumlahkan total harga
def total_price():
    global transaction_data
    total = sum(item["item_qty"] * item["item_price"] for item in transaction_data)
    return apply_discounts(total)

#Creating functions:
  #Display receipt
def display_receipt():
    global transaction_data
    print("| No |  Nama Item  |  Jumlah Item  |  Harga per Item  |  Total Harga  |")
    print("|----|-------------|---------------|------------------|---------------|")
    for i, item in enumerate(transaction_data, 1):
        item_name = item["item_name"]
        item_qty = item["item_qty"]
        item_price = item["item_price"]
        total_price = item_qty * item_price
        print(f"|  {i}  |  {item_name}  |      {item_qty}     |      {item_price}   |    {total_price}    |")

#Creating functions:
     #Menghitung diskon applicable based on total harga
def apply_discounts(total_price):
    if total_price > 500_000:
        return total_price * 0.90 #Diskon 10% untuk total harga >500k
    elif total_price > 300_000:
        return total_price * 0.92 #Diskon 8% untuk total harga >300k
    elif total_price > 200_000:
        return total_price * 0.95 #Diskon 5% untuk total harga >200k
    else:
        return total_price
