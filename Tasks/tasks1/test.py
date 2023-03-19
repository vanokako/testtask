from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float

    def __str__(self):
        return f"{self.name} - {self.price}"


@dataclass
class Customer:
    name: str
    phone: str
    repaired_items: list[Item]

    def __str__(self):
        return f"{self.name} {self.phone}: " \
               f"{', '.join([str(item) for item in self.repaired_items])}"


def get_customers(technic: list) -> list:
    result = {}
    for customer in technic:
        customer_class = result.get(customer[3], None)
        if not result.get(customer[3], None):
            result[customer[3]] = Customer(
                customer[2],
                customer[3],
                [Item(customer[0], customer[1])]
            )
        else:
            customer_class.repaired_items.append(
                Item(customer[0], customer[1])
            )
    return list(result.values())
