#To make to GET, POST, PUT, PATCH, DELETE
import requests
import json
from src.constants.api_constants import *
from src.helpers.payload_manager import *
from src.helpers.utils import *
import re

#HTTP Methods - Generic Functions






def get_request(url):
        response = requests.get(url=url)
        return response.json()

            #This method can return card_id

def post_request(url):
        response = requests.post(url=url)
        res = response.json()
        cart_id = res['cartId']
        return cart_id

            #This method can return item_id
def post_itemTocartrequests(url,data,header):
                b_data = json.dumps(data)
                hdr = header
                response = requests.post(url=url, data=b_data, headers=hdr)
                return response.json()

def patch_modifyitemscartrequests(body,header,url):
                b_data = json.dumps(body)
                hdr = header
                response = requests.patch(url=url, data=b_data, headers=hdr)
                return response


def put_modifyitemscartrequests(body,header,url):
                b_data = json.dumps(body)
                hdr = header
                response = requests.put(url=url, data=b_data, headers=hdr)
                return response

def delete_itemsrequests(url,header):
                hdr = header
                response = requests.delete(url=url, headers=hdr)
                return response


def set_cart_id():
    newcart = post_request(url=APIConstants.url_createnewcart())
    return newcart

def get_cart_id():
    c_id = set_cart_id()
    return c_id

            #apiitemconstant = APIConstants()




            # match = re.match(r"([a-z]+)([0-9]+)", getitempostitemurl, re.I)
            # items = ()
            # if match:
            #     items = match.groups()
            # c_id = items[1]
getitempostitemurl = APIConstants()
def get_item_id(prod1,prod2):
    crt_id = get_cart_id()
    response = post_itemTocartrequests(getitempostitemurl.url_additemstocart(crt_id),payload_additemtocart(pid1=prod1,pid2=prod2),common_headers())
    item_id = response['itemId']
    return item_id,crt_id

            #itm_id = get_item_id(prod1=4646,prod2=4641)










# data = post_request("http://simple-grocery-store-api.online/carts")
# print(data)
