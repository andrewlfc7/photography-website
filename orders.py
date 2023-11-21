import requests

# === Define headers ===
headers = {
    'Content-Type': 'application/json',
    'X-API-KEY': '{{f25a1b68-6b03-45d7-bcbb-c8d96833d91c-b3ec1e27-024e-47eb-a67c-9f237afdf3b2:b4982875-bdc0-4030-a41a-b3105f3df026}}'
}

# === Set-up order request ===
orderUrl = "https://order.gelatoapis.com/v4/orders"
orderJson = """{
        "orderType": "order",
        "orderReferenceId": "{{myOrderId}}",
        "customerReferenceId": "{{myCustomerId}}",
        "currency": "USD",
        "items": [
            {
                "itemReferenceId": "{{myItemId1}}",
                "productUid": "apparel_product_gca_t-shirt_gsc_crewneck_gcu_unisex_gqa_classic_gsi_s_gco_white_gpr_4-4",
                "files": [
                    {
                        "type": "default",
                        "url": "https://s3-eu-west-1.amazonaws.com/developers.gelato.com/product-examples/test_print_job_BX_4-4_hor_none.pdf"
                    },
                    {
                        "type":"back",
                        "url": "https://s3-eu-west-1.amazonaws.com/developers.gelato.com/product-examples/test_print_job_BX_4-4_hor_none.pdf"
                    }
                ],
                "quantity": 1
            }
        ],        
        "shipmentMethodUid": "express",
        "shippingAddress": {
            "companyName": "Example",
            "firstName": "Paul",
            "lastName": "Smith",
            "addressLine1": "451 Clarkson Ave",
            "addressLine2": "Brooklyn",
            "state": "NY",
            "city": "New York",
            "postCode": "11203",
            "country": "US",
            "email": "apisupport@gelato.com",
            "phone": "123456789"
        }
    }"""

# === Send order request ===
response = requests.request("POST", orderUrl, data=orderJson, headers=headers)
print(response.json())


