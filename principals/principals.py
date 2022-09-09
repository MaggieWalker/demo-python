
from cerbos.sdk.model import *

# Define the principals we are going to use in the demo.

Michelle = Principal(
    id="Michelle",
    roles={
        "Abacus_contract_admin"
    },
    attr={
        "profiles": ["Abacus"],
        "accounts": {
            "*": {
                "content_type": ["*"]
            }
        }
    }
)

Elaine = Principal(
    id="Elaine",
    roles={
        "Abacus_royalties"
    },
    attr={
        "profiles": ["Abacus"],
        "accounts": {
            "*": {
                "content_type": ["*"]
            }
        }
    }
)

Oliver = Principal(
    id="Oliver",
    roles={
        "Documents_documents_payee_management",
        "Content_label_artist_user_digital_audio"
    },
    attr={
        "profiles": ["Documents"],
        "accounts": {
            "999": {
                "content_type": ["digital_audio"]
            }
        }
    }
)

Conrad = Principal(
    id="Conrad",
    roles={
        "Content_distribution_reviewer_digital_audio"
    },
    attr={
        "profiles": ["Content"],
        "accounts": {
            "*": {
                "content_type": ["*"]
            }
        }
    }
)

Paul = Principal(
    id="Paul",
    roles={
        "Content_label_artist_user_digital_audio",
        "Content_content_manager_performance_neighbouring_rights"
    },
    attr={
        "profiles": ["Content"],
        "accounts": {
            "888": {
                "content_type": ["digital_audio", "sr_performance"]
            }
        }
    }
)

Allan = Principal(
    id="Allan",
    roles={
        "Content_content_manager_performance_neighbouring_rights"
    },
    attr={
        "profiles": ["Content"],
        "accounts": {
            "888": {
                "content_type": ["sr_performance"]
            },
            "222": {
                "content_type": ["digital_audio"]
            }
        }
    }
)


Nate = Principal(
    id="Nate",
    roles={
        "Insights_analytics_digital_audio",
        "Insights_analytics_performance_neighbouring_rights"
    },
    attr={
        "profiles": ["Insights"],
        "accounts": {
            "888": {
                "content_type": ["digital_audio", "sr_performance"]
            }
        }
    }
)

PRINCIPALS = [Michelle, Elaine, Oliver, Conrad, Paul, Allan, Nate]