from django.conf import settings

from slavasity.models import Game


class Korzina:
    def __init__(self, request):
        self.session = request.session
        korzina = self.session.get(settings.KORZINA_SESSION_ID)
        if not korzina:
            korzina = self.session[settings.KORZINA_SESSION_ID] = {}
        self.korzina = korzina

    def __iter__(self):
        product_ids = self.korzina.keys()
        product_list = Game.objects.filter(pk__in=product_ids)
        korzina = self.korzina.copy()
        for product in product_list:
            korzina[str(product.pk)]['product'] = product

        for item in korzina.values():
            item['total_price'] = float(item['price']) * int(item['count'])
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.korzina.values())
    
    def save(self):
        self.session[settings.KORZINA_SESSION_ID] = self.korzina
        self.session.modified = True

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.korzina:
            self.korzina[product_id] = {'count': 0, 
                                        'price': str(product.price)}
        if update_count:
            self.korzina[product_id]['count'] = count
        else:
            self.korzina[product_id]['count'] += count
        self.save()

    def remove(self, product):
        product_id = str(product.id) 
        if product_id in self.korzina:
            del self.korzina[product_id]
        self.save()
    
    def get_total(self):
        return sum(float(item['price']) * int(item['count']) for item in self.korzina.values())
    
    def clear(self):
        del self.session[settings.KORZINA_SESSION_ID]
        self.session.modified = True