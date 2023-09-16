import modul_market_1 #import module name

# Test 1
modul_market_1.add_item("Ayam Goreng", 2, 20000)
modul_market_1.add_item("Pasta Gigi", 3, 15000)

# Test 2
modul_market_1.delete_item("Pasta Gigi")

# Test 3
modul_market_1.reset_transaction()

# # Test 4
# modul_market_1.add_item("Ayam Goreng", 2, 20000)
# modul_market_1.add_item("Pasta Gigi", 3, 15000)
# modul_market_1.add_item("Mainan Mobil", 1, 200000)
# modul_market_1.add_item("Mi Instan", 5, 3000)

print(modul_market_1.check_order())
print("Total Price:", modul_market_1.total_price())
modul_market_1.display_receipt()