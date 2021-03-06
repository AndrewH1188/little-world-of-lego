from django.db import models
from profiles.models import UserProfile
from products.models import Product


class WishList(models.Model):
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='wishlist')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile}'s wishlist"


class WishItem(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
