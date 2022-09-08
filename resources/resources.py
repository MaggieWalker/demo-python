import dataclasses
from cerbos.sdk.model import *

# Define the resources we are going to use in the demo.

# Accounts
account_1 = Resource(
    id="account1",
    kind="account",
    attr={
        "account_id": "1"
    },
)

account_999 = Resource(
    id="account999",
    kind="account",
    attr={
        "account_id": "999"
    },
)

account_888 = Resource(
    id="account888",
    kind="account",
    attr={
        "account_id": "888"
    },
)

account_222 = Resource(
    id="account222",
    kind="account",
    attr={
        "account_id": "222"
    }
)

#Contracts
contract_1 = Resource(
    id="contract1",
    kind="contract",
    attr={
        "account_id": "1"
    },
)

contract_999 = Resource(
    id="contract999",
    kind="contract",
    attr={
        "account_id": "999"
    }
)

contract_888 = Resource(
    id="contract888",
    kind="contract",
    attr={
        "account_id": "888"
    }
)

#Account Payees
account_payee_1 = Resource(
    id="accountpayee1",
    kind="account_payee",
    attr={ 
            "account_id": "1",
    }
)

account_payee_999 = Resource(
    id="accountpayee999",
    kind="account_payee",
    attr={ 
            "account_id": "999",
    }
)

account_payee_888 = Resource(
    id="accountpayee888",
    kind="account_payee",
    attr={ 
            "account_id": "888",
    }
)

#Content
content_digital_888 = Resource(
    id="contentdigital888",
    kind="content",
    attr={
        "account_id": "888",
        "content_type": "digital_audio"
    }
)

content_performance_888 = Resource(
    id="contentperformance888",
    kind="content",
    attr={
        "account_id": "888",
        "content_type": "sr_performance"
    }
)

content_digital_999 = Resource(
    id="contentdigital999",
    kind="content",
    attr={
        "account_id": "999",
        "content_type": "digital_audio"
    }
)

content_physical_999 = Resource(
    id="contentphysical999",
    kind="content",
    attr={
        "account_id": "999",
        "content_type": "physical_audio"
    }
)

content_digital_1 = Resource(
    id="contentdigital1",
    kind="content",
    attr={
        "account_id": "1",
        "content_type": "digital_audio"
    }
)

#Analytics
analytics_public_888 = Resource(
    id="analyticspublic888",
    kind="analytics",
    attr={
        "account_id": "888",
        "is_public": True
    }
)

analytics_public_999 = Resource(
    id="analyticspublic999",
    kind="analytics",
    attr={
        "account_id": "999",
        "is_public": True
    }
)

analytics_not_public_999 = Resource(
    id="analyticsnotpublic999",
    kind="analytics",
    attr={
        "account_id": "999",
        "is_public": False
    }
)

RESOURCES = [
    account_1,
    account_999,
    account_888,
    account_222,
    contract_1,
    contract_999,
    contract_888,
    account_payee_1,
    account_payee_999,
    account_payee_888,
    content_digital_888,
    content_performance_888,
    content_digital_999,
    content_physical_999,
    content_digital_1,
    analytics_public_888,
    analytics_public_999,
    analytics_not_public_999

]