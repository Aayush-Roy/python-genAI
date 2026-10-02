class InvalidChaiError: pass

def bill(flavour, cups):
    menus = {
        "masala":20,
        "ginger":40
    }

    try:
        if flavour not in menus:
            raise InvalidChaiError(f"This{flavour} not in menu")
        if not isinstance(cups, int):
            raise TypeError("cups shoulb be in number")
        total = menus[flavour] * cups
        print(f"your Bill is {total}")
    except Exception as e:
        print("Error", e)
    finally:
        print("Thanks")

bill("ginger","2")