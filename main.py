# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import os

import emoji
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.container import CerbosContainer
from cerbos.sdk.model import *

from principals import principals
from resources import resources


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

    with container:
        container.wait_until_ready()
        host = container.http_host()

        # Create a Cerbos client
        with CerbosClient(host) as client:
            # Check access to Accounts
            print("\nCheck access to Account 1\n")
            for principal, action in [
                (principals.Michelle, "view"),
                (principals.Michelle, "edit"),
                (principals.Elaine, "view"),
                (principals.Elaine, "edit"),
                (principals.Oliver, "view"),
                (principals.Oliver, "edit")
            ]:
                check(client, principal, action, resources.account_1)

            print("\nCheck access to Account 999\n")
            for principal, action in [
                (principals.Oliver, "view"),
                (principals.Oliver, "edit")
            ]:
                check(client, principal, action, resources.account_999)


            print("\nCheck access to Account 888\n")
            for principal, action in [
                (principals.Paul, "view"),
                (principals.Paul, "edit"),
                (principals.Nate, "view"),
                (principals.Nate, "edit")
            ]:
                check(client, principal, action, resources.account_888)
