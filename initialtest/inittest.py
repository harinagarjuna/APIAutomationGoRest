import json

import requests
import pytest
from urllib.parse import quote


access_token = ""
get_post_url = "http://simple-grocery-store-api.online"

def test_getallproducts():
    getallproductsurl = "http://simple-grocery-store-api.online/products"
    response = requests.get(url=getallproductsurl)
    data = response.json()
    print(data)
    #assert data[0]['id'] is not None,"invalid"

def createNewCart():
    getallproductsurl = "http://simple-grocery-store-api.online/carts"
    response = requests.post(url=getallproductsurl)
    data = response.json()
    cartId = data['cartId']
    print(data['cartId'])
    return cartId






def AddItemToCart():
    cart_id = createNewCart()
    url = "http://simple-grocery-store-api.online/carts/{}/items".format(quote(cart_id))
    b_data = {
        'productId': '4646',
        'productId': '4641'
    }
    header = {
        'content-type' : 'application/json'
    }
    j_data = json.dumps(b_data)
    response = requests.post(url=url,data=j_data,headers=header)
    data = response.json()
    print(data)
    item_id = data['itemId']
    return item_id,cart_id

def test_values():
    item_cart_ids = AddItemToCart()
    item_id = item_cart_ids[0]
    cart_id = item_cart_ids[1]
    print(item_id)
    print(cart_id)

def test_ModifyItemsinCart():
    item_cart_ids = AddItemToCart()
    item_id = item_cart_ids[0]
    cart_id = item_cart_ids[1]
    b_data = {
        'quantity': '2'
    }
    header = {
        'content-type': 'application/json'
    }
    j_data = json.dumps(b_data)
    url = "http://simple-grocery-store-api.online/carts/{}/items/{}".format(quote(cart_id),quote(str(item_id)))
    response = requests.patch(url=url,data=j_data,headers=header)
    #data = response.json()
    print(response)


def test_PutReplaceItemsinCart():
    item_cart_ids = AddItemToCart()
    item_id = item_cart_ids[0]
    cart_id = item_cart_ids[1]
    b_data = {
        'productId' : '4641',
        'quantity' : '1'
    }
    header = {
        'content-type': 'application/json'
    }
    j_data = json.dumps(b_data)
    url = "http://simple-grocery-store-api.online/carts/{}/items/{}".format(quote(cart_id),quote(str(item_id)))
    response = requests.put(url=url,data=j_data,headers=header)
    #data = response.json()
    print(response)


def test_PutReplaceItemsinCart():
    item_cart_ids = AddItemToCart()
    item_id = item_cart_ids[0]
    cart_id = item_cart_ids[1]
    header = {
        'content-type': 'application/json'
    }
    url = "http://simple-grocery-store-api.online/carts/{}/items/{}".format(quote(cart_id),quote(str(item_id)))
    response = requests.patch(url=url,headers=header)
    #data = response.json()
    print(response)


def test_DeleteItemsinCart():
    item_cart_ids = AddItemToCart()
    item_id = item_cart_ids[0]
    cart_id = item_cart_ids[1]
    header = {
        'content-type': 'application/json'
    }
    url = "http://simple-grocery-store-api.online/carts/{}/items/{}".format(quote(cart_id),quote(str(item_id)))
    response = requests.delete(url=url,headers=header)
    #data = response.json()
    print(response)




def test_getItemsinCart():
    item_cart_ids = AddItemToCart()
    item_id = item_cart_ids[0]
    cart_id = item_cart_ids[1]
    url = "http://simple-grocery-store-api.online/carts/{}/items".format(quote(cart_id))
    response = requests.get(url=url)
    data = response.json()
    print(data)

def test_getsingleproduct():
    getsingleproducturl = "http://simple-grocery-store-api.online/products/:"
    variable = {"productid": 4643}
    response = requests.get(url=getsingleproducturl,params=variable)
    data = response.json()
    print(data)

def test_createUser():
    #posturl = "https://gorest.co.in/public/v2/users"
    json_body =[
    {
        "field": "email",
        "message": "hari@gmail.com"
    },
    {
        "field": "name",
        "message": "Hari Nagarjuna"
    },
    {
        "field": "gender",
        "message": "Male"
    },
    {
        "field": "status",
        "message": "Active"
    }
    ]
    headervalue = {"Content-Type": "application/json",
                   "Authorization" : access_token}
    response = requests.post(url=get_post_url,json=json_body,headers=headervalue)
    data = response.json()
    print(data)




