
def Order(item,qty):
    menus = {"chole bhature":150, "naan":120, "rajma chawal":60}
    if item not in menus:
        raise ValueError(f"This {item} is not in menu")
    
    total_price = menus[item] * int(qty)
    print(f"your total price is {total_price}")


Order("chole bhatur",2)
