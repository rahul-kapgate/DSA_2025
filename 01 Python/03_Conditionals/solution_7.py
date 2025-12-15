order_size = "Small"
# order_size = "Medium"
# order_size = "Large"

# extra_shot = True
extra_shot = False

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)