class FlavourNotAvailableError(Exception): pass

def order_chai(flavor, cups):
    menus = {"masala":20, "ginger":30}
    try:
        if flavor not in menus:
            raise FlavourNotAvailableError(f"Thats {flavor} flavor not in menu")
        if not  isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menus[flavor] * cups
        print(f"your total amount of {cups} for {flavor} chai is: {total}")
    except Exception as e:
        print("Error", e)
    finally:
        print("Thanks")

order_chai("mint", 2)
order_chai("masala", "three")
order_chai("masala", 2)