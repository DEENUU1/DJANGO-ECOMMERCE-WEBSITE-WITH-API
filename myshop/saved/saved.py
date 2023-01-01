from django.conf import settings
from shop.models import Product


class Saved(object):
    def __init__(self, request):
        self.session = request.session
        saved = self.session.get(settings.SAVED_SESSION_ID)
        if not saved:
            saved = self.session[settings.SAVED_SESSION_ID] = {}
        self.saved = saved

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.saved:
            self.saved[product_id] = {'price': str(product.price)}

        self.save()

    def save(self):
        self.session[settings.SAVED_SESSION_ID] = self.saved
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.saved:
            del self.saved[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.saved.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.saved[str(product.id)]['product'] = product

        for item in self.saved.values():
            yield item

    def clear(self):
        del self.session[settings.SAVED_SESSION_ID]
        self.session.modified = True
