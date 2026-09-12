from functools import total_ordering


@total_ordering
class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"price={self.price}, quantity={self.quantity})"
        )

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __mul__(self, quantity):
        if not isinstance(quantity, int):
            return NotImplemented

        return Product(
            self.name,
            self.price,
            self.quantity * quantity
        )

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        if self.name != other.name:
            raise ValueError("Different products cannot be added")

        return Product(
            self.name,
            self.price,
            self.quantity + other.quantity
        )


class ShoppingCart:
    def __init__(self):
        self.items = []

    def __str__(self):
        if not self.items:
            return "Shopping Cart is Empty"

        return "\n".join(
            f"{index + 1}. {item.name} "
            f"x {item.quantity} = ₹{item.price * item.quantity}"
            for index, item in enumerate(self.items)
        )

    def __repr__(self):
        return f"ShoppingCart(items={self.items!r})"

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Product):
            raise TypeError("Only Product objects are allowed")

        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, product_name):
        return any(
            item.name == product_name
            for item in self.items
        )

    def __iter__(self):
        return iter(self.items)

    def __add__(self, product):
        if not isinstance(product, Product):
            return NotImplemented

        self.add_product(product)
        return self

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects are allowed")

        for item in self.items:
            if item.name == product.name:
                item.quantity += product.quantity
                return

        self.items.append(product)

    def remove_product(self, product_name):
        self.items = [
            item for item in self.items
            if item.name != product_name
        ]

    def total_price(self):
        return sum(
            item.price * item.quantity
            for item in self.items
        )

    def __enter__(self):
        print("Shopping session started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Shopping session ended")

    def __call__(self):
        print("Checkout initiated")
        print(f"Total Amount: ₹{self.total_price()}")


# --------------------------------------------------
# Creating Product Objects
# --------------------------------------------------

laptop = Product("Laptop", 60000)
mouse = Product("Mouse", 1000)
keyboard = Product("Keyboard", 2500)

print(laptop)
print(repr(laptop))


# --------------------------------------------------
# Product Operator Overloading
# --------------------------------------------------

print("\n--- Product Operations ---")

laptop_copy = Product("Laptop", 60000)

print("Equal:", laptop == laptop_copy)

print(
    "Laptop cheaper than Mouse:",
    laptop < mouse
)

double_mouse = mouse * 2

print(
    "Double Mouse:",
    double_mouse
)

mouse1 = Product("Mouse", 1000, 2)
mouse2 = Product("Mouse", 1000, 3)

combined_mouse = mouse1 + mouse2

print(
    "Combined Mouse Quantity:",
    combined_mouse.quantity
)


# --------------------------------------------------
# Shopping Cart
# --------------------------------------------------

cart = ShoppingCart()

cart.add_product(laptop)
cart.add_product(mouse)
cart.add_product(keyboard)

print("\n--- Shopping Cart ---")
print(cart)


# --------------------------------------------------
# __len__()
# --------------------------------------------------

print("\nNumber of products:", len(cart))


# --------------------------------------------------
# __bool__()
# --------------------------------------------------

if cart:
    print("Cart contains products")
else:
    print("Cart is empty")


# --------------------------------------------------
# __getitem__()
# --------------------------------------------------

print("\nFirst Product:")
print(cart[0])


# --------------------------------------------------
# __setitem__()
# --------------------------------------------------

cart[1] = Product("Wireless Mouse", 1500)

print("\nAfter Updating Product:")
print(cart)


# --------------------------------------------------
# __contains__()
# --------------------------------------------------

print(
    "\nIs Laptop in cart?",
    "Laptop" in cart
)

print(
    "Is Phone in cart?",
    "Phone" in cart
)


# --------------------------------------------------
# __iter__()
# --------------------------------------------------

print("\nIterating over cart:")

for product in cart:
    print(product.name)


# --------------------------------------------------
# __add__()
# --------------------------------------------------

cart + Product("Keyboard", 2500)

print("\nAfter Adding Another Keyboard:")
print(cart)


# --------------------------------------------------
# Total Price
# --------------------------------------------------

print(
    "\nTotal Price:",
    f"₹{cart.total_price()}"
)


# --------------------------------------------------
# __call__()
# --------------------------------------------------

print("\nCalling Cart Object:")
cart()


# --------------------------------------------------
# __delitem__()
# --------------------------------------------------

del cart[0]

print("\nAfter Removing First Product:")
print(cart)


# --------------------------------------------------
# Context Manager
# __enter__ and __exit__
# --------------------------------------------------

print("\nUsing Context Manager:")

with ShoppingCart() as temporary_cart:
    temporary_cart.add_product(
        Product("Headphones", 3000)
    )

    print(temporary_cart)


# --------------------------------------------------
# Final Cart
# --------------------------------------------------

print("\nFinal Cart:")
print(cart)

print("\nFinal Representation:")
print(repr(cart))