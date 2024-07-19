import pytest
from src.helpers.api_requests_wrapper import *
from src.constants.api_constants import *
import re




def test_createcart():
    newcart = post_request(APIConstants.url_createnewcart())
    assert newcart['created'] == True,"Case Failed"
    assert newcart['cartId'] is not None

apiconstants = APIConstants()

def test_additemtocart(prod1=4646,prod2=4641):
    response = post_itemTocartrequests(apiconstants.url_additemstocart(get_cart_id()),payload_additemtocart(prod1,prod2),common_headers())
    print(response)

def test_modifyPATCHitemscart():
    itemcartids = get_item_id(prod1=4646,prod2=4641)
    ct_id = itemcartids[1]
    itm_id = itemcartids[0]
    response = patch_modifyitemscartrequests(payrload_modifyitems(2),common_headers(),apiconstants.modifyorputorreplaceordeleteitemsincart(cart_id=ct_id,item_id=itm_id))
    print(response)
    print(ct_id)
    print(itm_id)

def test_modifyPUTitemscart():
    itemcartids = get_item_id(prod1=4646,prod2=4641)
    ct_id = itemcartids[1]
    itm_id = itemcartids[0]
    response = put_modifyitemscartrequests(putReplaceitems(pid=4641,qty=1),common_headers(),apiconstants.modifyorputorreplaceordeleteitemsincart(cart_id=ct_id,item_id=itm_id))
    print(response)
    print(ct_id)
    print(itm_id)

def test_deleteitemscart():
    itemcartids = get_item_id(prod1=4646,prod2=4641)
    ct_id = itemcartids[1]
    itm_id = itemcartids[0]
    response = delete_itemsrequests(apiconstants.modifyorputorreplaceordeleteitemsincart(cart_id=ct_id,item_id=itm_id),common_headers())
    print(response)
    print(ct_id)
    print(itm_id)

