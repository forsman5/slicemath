from django.db import models

toppingChoices = (
    ('Peperroni'),
    ('Sausage'),
    ('Onions'),
    ('Peppers'),
    ('Mushrooms'),
    ('Pineapple'),
)

sauceChoices = (
    ('Marinara'),
    ('Alfredo'),
)
sizeChoices = (
    ('Small'),
    ('Medium'),
    ('Large'),
    ('Xtra-Large'),
)
crustChoices = (
    ('Thin')
    ('Reguler')
    ('Thick')
    ('Garlic Crusted')


)
# Create your models here.
<<<<<<< HEAD
class Sessions(models.Model):

    pass
=======
#class Sessions(models.Model):
    # many Members
    # many pizzas
>>>>>>> 927c2f8abc5ee2bec4eb3043329f4272f3928a8f

# Members
class Member(member.Model):
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # for every member, one session

class Pizza(models.Model):
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    crust = models.ForiegnKey(Crust, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)

class Topping(model.Model):
    name = models.CharField(choices=toppingChoices)
    pizzas = models.ManyToManyField(Pizza, related_name="toppings")

class Crust(model.Model):
    name = models.CharField(choices=crustChoices)

class Sauce(model.Model):
    name = models.CharField(choices=sauceChoices)

class Size(model.Model):
    name = models.CharField(choices=sizeChoices)
