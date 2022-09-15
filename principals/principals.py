
from cerbos.sdk.model import *

# Define the principals we are going to use in the demo.

Michelle = Principal(
    id="Michelle",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Abacus"],
        "tenants": {
            "*": {
                "account_id": "*",
                "attachments": {
                    "Abacus_contract_admin": {
                        "role": "Abacus_contract_admin"
                    }
                }
            }
        }
    }
)

Elaine = Principal(
    id="Elaine",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Abacus"],
        "tenants": {
            "*": {
                "account_id": "*",
                "attachments": {
                    "Abacus_royalties": {
                        "role": "Abacus_royalties"
                    }
                }
            }
        }
    }
)

Oliver = Principal(
    id="Oliver",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Documents", "Content"],
        "tenants": {
            "999": {
                "account_id": "999",
                "attachments": {
                    "Documents_payee_management": {
                        "role": "Documents_payee_management"
                    },
                    "Content_label_artist_user": {
                        "role": "Content_label_artist_user",
                        "content_types": ["digital_audio"]
                    },
                }
            }
        }
    }
)

Conrad = Principal(
    id="Conrad",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Content"],
        "tenants": {
            "*": {
                "account_id": "*",
                "attachments": {
                    "Content_distribution_reviewer": {
                        "role": "Content_distribution_reviewer",
                        "content_types": ["digital_audio"]
                    }
                }
            }
        }
    }
)

Paul = Principal(
    id="Paul",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Content"],
        "tenants": {
            "888": {
                "account_id": "888",
                "attachments": {
                    "Content_label_artist_user": {
                        "role": "Content_label_artist_user",
                        "content_types": ["digital_audio", "sr_performance"]
                    }
                }
            }
        }
    }
)

Allan = Principal(
    id="Allan",
    roles={"user"},
    attr={
        "type": "human",
        "profiles": ["Content"],
        "tenants": {
            "888": {
                "account_id": "888",
                "attachments": {
                    "Content_label_artist_user": {
                        "role": "Content_label_artist_user",
                        "content_types": ["sr_performance"]
                    }
                }
            },
            "222": {
                "account_id": "222",
                "attachments": {
                    "Content_label_artist_user": {
                        "role": "Content_label_artist_user",
                        "content_types": ["digital_audio"]
                    }
                }
            },
        }
    }
)


Nate = Principal(
    id="Nate",
    roles={"user"},
    attr={
        "type": "machine",
        "apps": ["Insights"],
        "tenants": {
            "888": {
                "account_id": "888",
                "attachments": {
                    "Insights_analytics": {
                        "role": "Insights_analytics",
                        "content_types": ["digital_audio", "sr_performance"]
                    }
                }
            }
        }
    }
)

Ginger = Principal(
    id="Ginger",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Content"],
        "tenants": {
            "3": {
                "account_id": "3",
                "subaccount_ids": ["31", "32"],
                "attachments": {
                    "Label_administrator": {
                        "role": "Label_administrator",
                        "content_types": ["digital_audio"]
                    }
                }
            }
        }
    }
)

Colin = Principal(
    id="Colin",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Content"],
        "tenants": {
            "31": {
                "account_id": "31",
                "attachments": {
                    "Label_user": {
                        "role": "Label_user",
                        "content_types": ["digital_audio"]
                    }
                }
            }
        }
    }
)

Donny = Principal(
    id="Donny",
    roles={"user"},
    attr={
        "type": "human",
        "apps": ["Content"],
        "tenants": {
            "32": {
                "account_id": "32",
                "attachments": {
                    "Label_user": {
                        "role": "Label_user",
                        "content_types": ["digital_audio"]
                    }
                }
            }
        }
    }
)

PRINCIPALS = [
    Michelle,
    Elaine,
    Oliver,
    Conrad,
    Paul,
    Allan,
    Nate,
    Ginger,
    Colin,
    Donny
]
