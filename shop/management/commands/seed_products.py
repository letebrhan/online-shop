from decimal import Decimal
from django.core.management.base import BaseCommand
from django.apps import apps
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Seed the database with demo categories and products."

    def handle(self, *args, **kwargs):
        Category = apps.get_model("shop", "Category")
        Product = apps.get_model("shop", "Product")

        # Adjust field names if needed (title vs name, etc.)
        cat, _ = Category.objects.get_or_create(
            title="T-Shirts",  # change to 'name' if your model uses that
            slug="t-shirts",
        )

        demo_items = [
            ("Demo T-Shirt", 19.99),
            ("Coffee Mug", 12.50),
            ("Sticker Pack", 3.99),
            ("Hoodie", 39.00),
        ]

        for label, amt in demo_items:
            Product.objects.get_or_create(
                title=label,  # or 'name' depending on your Product model
                price=Decimal(str(amt)),
                category=cat,
                slug=slugify(label),
                defaults={"stock": 20, "is_available": True},
            )

        self.stdout.write(self.style.SUCCESS("✅ Demo products seeded!"))
