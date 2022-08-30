# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import os

import emoji
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.container import CerbosContainer
from cerbos.sdk.model import *

# Define the principals and resources we are going to use in the demo.

jess = Principal(
    id="jess",
    roles={"documents_payee_management"},
    attr={
            "account": 
                {
                    "id": "7123"
                },
        },
)

maggie = Principal(
    id="maggie",
    roles={"internal_employee",},
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

account_7123 = Resource(
    id="account7123",
    kind="account",
    attr={"account": 
            {
                "id": "7123"
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


# Check whether the principal is allowed to perform a specific action on the given resource
def check(
    client: CerbosClient,
    principal: Principal,
    action: str,
    resource: Resource,
):
    try:
        effect = "_cannot_"
        icon = emoji.emojize(":cross_mark:")

        if client.is_allowed(action=action, principal=principal, resource=resource):
            effect = "_can_"
            icon = emoji.emojize(":thumbs_up:")

        print(
            f"{icon} {principal.id} {effect} {action} on "
            f"{resource.kind} {resource.id}"
        )
    except Exception as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    # Use the Cerbos TestContainer to start Cerbos automatically. This is for demonstration purposes only.
    # In production scenarios Cerbos would be deployed as a separate service.
    container = CerbosContainer()
    policy_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "policies")
    container.with_volume_mapping(policy_dir, "/policies")
    print('ok got policies')
    with container:
        container.wait_until_ready()
        host = container.http_host()

        # Create a Cerbos client
        with CerbosClient(host) as client:
            # Check access to Account 7123
            print("\nCheck access to Account 7123\n")
            for principal, action in [
                (jess, "create"),
                (jess, "read"),
                (maggie, "read"),
                (maggie, "approve"),
                (jess, "approve"),
                (jess, "submit"),
            ]:
                check(client, principal, action, account_7123)

            # Check access to Payee 8
            print("\nCheck access to Payee 8\n")

            for principal, action in [
                (jess, "read"),
                (jess, "create"),
                (jess, "update"),
                (maggie, "read"),
                (maggie, "update"),
                (machine, "read"),
                (machine, "create"),
                (machine, "update"),
                (todd, "update")
            ]:
                check(client, principal, action, payee_8)