#Add your constants here
from src.helpers.api_requests_wrapper import *
from urllib.parse import quote

class APIConstants():
    @staticmethod
    def base_url():
        return "http://simple-grocery-store-api.online"

    @staticmethod
    def url_getallproducts():
        return "http://simple-grocery-store-api.online/products"

    @staticmethod
    def url_createnewcart():
        return "http://simple-grocery-store-api.online/carts"


    def url_additemstocart(self,cart_id):
        return "http://simple-grocery-store-api.online/carts/{}/items".format(quote(cart_id))


    def modifyorputorreplaceordeleteitemsincart(self,cart_id, item_id):
        return "http://simple-grocery-store-api.online/carts/{}/items/{}".format(quote(cart_id), quote(str(item_id)))



