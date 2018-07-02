from purchaseItem import purchaseItem
from pickupItem import pickupItem
from products import products


#adding products

prod = products()
prod.add_products("1", "potatos", 2.5, 0)
prod.add_products("2", "oranges", 2, 0)
prod.add_products("3", "bananas", 5, 0)
prod.add_products("4", "apples", 5.5, 0)
prod.add_products("5", "tomatos", 3.6, 0)

print(prod.get_all_products())

#get all prices
prod.update_amount("1", 10)
prod.update_amount("2", 20)
prod.update_amount("3", 20)
prod.get_all_prices()
#get all amount
prod.get_all_amounts()

#purchase items
#pickup items
pick = pickupItem
pick.add_item("1", 2)
pick.add_item("2", 3)
pickedItems = pick.get_pick()
print(pickedItems)



