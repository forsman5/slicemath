from django.db import models

class Sessions(models.Model):
    pass

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
    toppingChoices = (
        ('PEPI', 'Peperroni'),
        ('S', 'Sausage'),
        ('O', 'Onions'),
        ('PEPR', 'Peppers'),
        ('M', 'Mushrooms'),
        ('PINE', 'Pineapple'),
    )

    name = models.CharField(choices=toppingChoices)
    pizzas = models.ManyToManyField(Pizza, related_name="toppings")

class Crust(model.Model):
    crustChoices = (
        ('S', 'Thin'),
        ('R', 'Regular'),
        ('L', 'Thick'),
        ('G', 'Garlic Crusted'),
    )

    name = models.CharField(choices=crustChoices)

class Sauce(model.Model):
    sauceChoices = (
        ('M', 'Marinara'),
        ('A', 'Alfredo'),
    )

    name = models.CharField(choices=sauceChoices)

class Size(model.Model):
    sizeChoices = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('X', 'Xtra-Large'),
    )

    name = models.CharField(choices=sizeChoices)
