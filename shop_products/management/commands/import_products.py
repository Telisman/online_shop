import requests
from django.core.management.base import BaseCommand
from shop_products.models import Product

class Command(BaseCommand):
    help = 'Import products from JSON dataset'

    def handle(self, *args, **options):
        # Replace 'https://30hills.com/api/products.json' with your dataset URL
        url = 'https://30hills.com/api/products.json'
        response = requests.get(url)
        data = response.json()

        # Loop through the products in the JSON data and create Product objects
        for item in data['products']['data']['items']:
            try:
                images = item['images']
            except KeyError:
                images = []

            product = Product(
                id=item['id'],
                name=item['name'],
                description=item['description'],
                price=float(item['price']),
                category=item['category'],
                subcategory=item['subcategory'],
                image_urls=images  # Use the images list or an empty list if 'images' key is missing
            )
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully imported product: {product.name}'))
