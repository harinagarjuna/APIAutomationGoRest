#Payload Data return functions here

def payload_additemtocart(pid1,pid2):
    data = {
        'productId': str(pid1),
        'productId': str(pid2)
    }
    return data

def payrload_modifyitems(numberofitems):
    body = {
        'quantity': numberofitems
    }
    return body

def putReplaceitems(pid,qty):
    body = {
        'productId' : pid,
        'quantity' : qty
    }
    return body


