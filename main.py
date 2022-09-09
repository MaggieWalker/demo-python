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
        effect = "is not allowed to"
        icon = emoji.emojize(":cross_mark:")
        if client.is_allowed(action=action, principal=principal, resource=resource):
            effect = "is allowed to"
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
            def time_check():
                ACTIONS = [
                    'view',
                    'create',
                    'edit',
                    'review',
                ]
                num_checks = 0
                for principal in principals.PRINCIPALS:
                    for resource in resources.RESOURCES:
                        for action in ACTIONS:
                            num_checks += 1
                            check(client, principal, action, resource)
                print(f'Executed {num_checks} authorization checks')

            import timeit
            print(timeit.timeit("time_check()", number=1, setup="from __main__ import time_check"))
