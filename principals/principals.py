
from cerbos.sdk.model import *

# Define the principals we are going to use in the demo.

amelia = Principal(
    id="amelia",
    roles={
        "content_user",
        "insights_user"
},
    attr={}
)

jess = Principal(
    id="jess",
    roles={
        "documents_payee_management",
        "internal_employee"
    },
    attr={
            "account": 
                {
                    "id": "7123"
                },
        },
)

maggie = Principal(
    id="maggie",
    roles={"internal_employee", "engineer"},
    attr={"team": "permissions_platform"},
)

todd = Principal(
    id="todd",
    roles={"updater"},
    attr={
            "account": 
                {
                    "id": "7123"
                },
        },
)

machine = Principal(
    id="machine12345",
    roles={"abacus_machine"},
    attr={
        "group": "MachineGroup_Abacus"
    }
)