from django.db import models

class Session(models.Model):
    pass

class Member(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    toppingPref = models.ManyToManyField(Topping)
    saucePref = models.ForeignKey(Sauce)
    crustPref = models.ForeignKey(Crust)


class Crust(models.Model):
    crustChoices = (
        ('S', 'Thin'),
        ('R', 'Regular'),
        ('L', 'Thick'),
        ('G', 'Garlic Crusted'),
    )

    name = models.CharField(max_length=50, choices=crustChoices)

class Sauce(models.Model):
    sauceChoices = (
        ('M', 'Marinara'),
        ('A', 'Alfredo'),
    )

    name = models.CharField(max_length=50, choices=sauceChoices)

class Size(models.Model):
    sizeChoices = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('X', 'Xtra-Large'),
    )

    name = models.CharField(max_length=50, choices=sizeChoices)

class Pizza(models.Model):
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

class Topping(models.Model):
    toppingChoices = (
        ('PEPI', 'Peperroni'),
        ('S', 'Sausage'),
        ('O', 'Onions'),
        ('PEPR', 'Peppers'),
        ('M', 'Mushrooms'),
        ('PINE', 'Pineapple'),
    )

    name = models.CharField(max_length=50, choices=toppingChoices)
    pizzas = models.ManyToManyField(Pizza, related_name="toppings")
