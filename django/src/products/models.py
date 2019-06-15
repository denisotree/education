from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    slug = models.CharField(
        max_length=255,
        default="#",
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=255
    )

    slug = models.CharField(
        max_length=255,
        default="#",
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
