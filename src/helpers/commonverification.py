#HTTP Status Verification

def verify_http_status_code(response_data,expect_data):
    assert response_data.status_code == expect_data,"Expected HTTP Status Code"+expect_data

def verify_json_key_is_not_null(key):
   assert key!=0, "Key is not Empty"+key
   assert key>0, "key is greater than zero"


