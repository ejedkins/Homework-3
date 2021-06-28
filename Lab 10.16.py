#Elijah Jedkins PSID: 1786452
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = str(item_name)
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        cost = (self.item_price * self.item_quantity)
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, str(cost)))


if __name__ == "__main__":
    print('Item 1')
    item1 = ItemToPurchase()
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    print()
    print('Item 2')
    item2 = ItemToPurchase()
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    item1_cost = item1.item_price * item1.item_quantity
    item2_cost = item2.item_price * item2.item_quantity
    total_price = (item1_cost) + (item2_cost)
    print()
    print("Total: ${}".format(str(total_price)))
