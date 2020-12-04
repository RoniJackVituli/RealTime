import module1

obj = module1.open_data()


def stores_registered():
    stores_amount_registered = len(obj['Stores'])
    return stores_amount_registered


def costumer_registered():
    costumer_amount_registered = len(obj['Costumers'])
    return costumer_amount_registered


def manager_registered():
    manager_amount_registered = len(obj['Managers'])
    return manager_amount_registered
