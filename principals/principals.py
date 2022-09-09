
from cerbos.sdk.model import *

# Define the principals we are going to use in the demo.

Michelle = Principal(
    id="Michelle",
    roles={},
    attr={
        "type": "human",
        "apps": ["Abacus"],
        "tenants": [
            {
                "account_id": "*",
                "attachments": [
                    {
                        "role": "Abacus_contract_admin"
                    }
                ]
            }
        ]
    }
)

Elaine = Principal(
    id="Elaine",
    roles={},
    attr={
        "type": "human",
        "apps": ["Abacus"],
        "tenants": [
            {
                "account_id": "*",
                "attachments": [
                    {
                        "role": "Abacus_royalties"
                    }
                ]
            }
        ]
    }
)

Oliver = Principal(
    id="Oliver",
    roles={},
    attr={
        "type": "human",
        "apps": ["Documents", "Content"],
        "tenants": [
            {
                "account_id": "999",
                "attachments": [
                    {
                        "role": "Documents_documents_payee_management"
                    },
                    {
                        "role": "Content_label_artist_user",
                        "content_types": ["digital_audio"]
                    },
                ]
            }
        ]
    }
)

Conrad = Principal(
    id="Conrad",
    roles={},
    attr={
        "type": "human",
        "apps": ["Content"],
        "tenants": [
            {
                "account_id": "*",
                "attachments": [
                    {
                        "role": "Content_distribution_reviewer",
                        "content_types": ["digital_audio"]
                    }
                ]
            }
        ]
    }
)

Paul = Principal(
    id="Paul",
    roles={},
    attr={
        "type": "human",
        "apps": ["Content"],
        "tenants": [
            {
                "account_id": "888",
                "attachments": [
                    {
                        "role": "Content_label_artist_user",
                        "content_types": ["digital_audio", "sr_performance"]
                    }
                ]
            }
        ]
    }
)

Allan = Principal(
    id="Allan",
    roles={},
    attr={
        "type": "human",
        "profiles": ["Content"],
        "tenants": [
            {
                "account_id": "888",
                "attachments": [
                    {
                        "role": "Content_label_artist_user",
                        "content_types": ["sr_performance"]
                    }
                ]
            },
            {
                "account_id": "222",
                "attachments": [
                    {
                        "role": "Content_label_artist_user",
                        "content_types": ["digital_audio"]
                    }
                ]
            },
        ]
    }
)


Nate = Principal(
    id="Nate",
    roles={},
    attr={
        "type": "human",
        "apps": ["Insights"],
        "tenants": [
            {
                "account_id": "888",
                "attachments": [
                    {
                        "role": "Insights_analytics",
                        "content_types": ["digital_audio", "sr_performance"]
                    }
                ]
            }
        ]
    }
)

PRINCIPALS = [Michelle, Elaine, Oliver, Conrad, Paul, Allan, Nate]