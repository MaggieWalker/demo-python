import dataclasses
from cerbos.sdk.model import *

# Define the resources we are going to use in the demo.

account_7777 = Resource(
    id="account7777",
    kind="account",
    attr={"account": 
            {
                "id": "7777"
            }
        },
)

payee_8 = Resource(
    id="payee8",
    kind="payee",
    attr={ 
            "payee_id": "8",
            "account": 
            {
                "id": "7123"
            }
        },
)

top_secret_product = Resource(
    id="secret4000",
    kind="product",
    attr={
        "security_clearance": "top_secret"
    }
)

not_secret_product = Resource(
    id="notsecret4000",
    kind="product",
    attr={
        "security_clearance": "normal"
    },
)
