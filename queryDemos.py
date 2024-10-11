# (1) Returns all customers from the customer table
customers = Customer.objects.all()

# (2) Returns the first customer in the table
firstCustomer = Customer.objects.first()

# (3) Returns the last customer in the table
lastCustomer = Customer.objects.last()

# (4) Returns a single customer by name
customerByName = Customer.objects.get(name='Tessy John')

# (5) Returns a single customer by ID
customerById = Customer.objects.get(id=4)

# (6) Returns all orders related to the first customer
firstCustomerOrders = firstCustomer.order_set.all()

# (7) Returns the name of the customer for the first order (Query parent model values)
order = Order.objects.first()
ParentName = order.customer.name

# (8) Returns products from the product table where the category is "Out Door"
products = Product.objects.filter(category="Out Door")

# (9) Orders products by id, ascending and descending
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# (10) Returns all products with a tag of "electronics"
ProductFiltered = Product.objects.filter(tags__name="electronics")  # Double underscore for related field

# Return the total count for the number of times a bulb was ordered
bulbOrderCount = firstCustomer.order_set.filter(product__name="Bulb").count()

# Return total count for each product ordered
allOrders = {}
for order in firstCustomer.order_set.all():
    productName = order.product.name
    if productName in allOrders:
        allOrders[productName] += 1
    else:
        allOrders[productName] = 1
Returns: {'Bulb': 2, 'Eggs': 6}

# Related set example
class ParentModel(models.Model):  # Corrected from model.Model to models.Model
    name = models.CharField(max_length=200, null=True)  # CharField spelling corrected

class ChildModel(models.Model):  # Corrected from model.Model to models.Model
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)  # ForeignKey and related field correction
    name = models.CharField(max_length=200, null=True)  # CharField spelling corrected

# Assuming we have a parent instance
parent = ParentModel.objects.first()

# Return all child models related to the parent
parent.childmodel_set.all()  # childmodel_set (model name in lowercase followed by _set)
























