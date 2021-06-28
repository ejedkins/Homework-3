#Elijah Jedkins PSID: 1786452
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_desription="none"):
        self.item_name = str(item_name)
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = str(item_desription)

    def print_item_cost(self):
        cost = (self.item_price * self.item_quantity)
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, str(cost)))

    def print_item_description(self):
        print('{}: {}', format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)
        self.cart_items = list(cart_items)
#adding an item to cart
    def add_item(self, string):
        print("\nADD ITEM TO CART")
        item_name = input('Enter the item name:\n')
        item_description = input('Enter the item description:\n')
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))
#removing an item from cart
    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        itemName = input('Enter name of item to remove:\n')
        i = 0
        item_rem = False
        for item in self.cart_items:
            if item.item_name == itemName:
                del self.cart_items[i]
                i += 1
                item_rem = True
                break

            if item_rem == False:
                print('Item not found in cart. Nothing removed.')
#changing the  quantity in cart
    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY')
        itemName = input('Enter the item name:\n')
        qty = int(input('Enter the new quantity:\n'))
        itemToPurchase = ItemToPurchase(itemName, 0, qty)

        item_mod = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemToPurchase.item_name:
                qty = int(input('Enter the new quantity:\n'))
                self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                item_mod = True
                break
            if item_mod != True:
                print('Item not found in cart. Nothing modified.')
#getting the amount of items in cart
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
            return num_items
#getting the cost of the items in cart
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
            return total_cost
#getting the to total cost of items in cart
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
            print('\nTotal: $0')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: %dn' % self.get_num_items_in_cart())
            for item in self.cart_items:
                total = item.item_price * item.item_quantity
                print('%s %d @ $%d = $%d' % (item.item_name, item.item_quantity, item.item_price, total))
            print('\nTotal: $%d' % (total_cost))
#get descriptions of items
    def print_decriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Item Descriptions')
            for item in self.cart_items:
                item.print_item_description()

    def output_cart(self):
        print('OUTPUT SHOPPING CART\n')
        new = ShoppingCart()
        print('{}\'s Shooping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('Number of Items:',new.get_num_items_in_cart() , end='\n\n')


def print_menu(newCart):
    customer_Cart = newCart

    command = ' '

    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')

    while (command != 'q'):
        print(menu, end='\n')
        command = input('Choose an option:\n')
        string = ''
        if (command == 'a'):
            customer_Cart.add_item(string)

        elif (command == 'o'):
            customer_Cart.output_cart()

        elif (command == 'i'):
            print('\nOUTPUT ITEMS DESCRIPTIONS')
            customer_Cart.print_decriptions()

        elif (command == 'r'):
            customer_Cart.remove_item()

        elif (command == 'c'):
            customer_Cart.modify_item()

        else:
            break


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print('\nCustomer name:', customer_name, end='\n')
    print('Today\'s date:', current_date, end='\n')
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)