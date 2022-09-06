
from cerbos.sdk.model import *

# Define the principals we are going to use in the demo.

Michelle = Principal(
    id="Michelle",
    roles={
        "AbacusProfile_contract_admin"
    },
    attr={
        "profiles": ["Abacus"],
        "account_id": '*'
    }
)

Elaine = Principal(
    id="Elaine",
    roles={
        "AbacusProfile_royalties"
    },
    attr={
        "profiles": ["Abacus"],
        "account_id": '*'
    }
)

Oliver = Principal(
    id="Oliver",
    roles={
        "DocumentsProfile_documents_payee_management",
        "ContentProfile_content_manager_digital_audio"
    },
    attr={
        "profiles": ["Documents"],
        "account_id": '999'
    }
)

Paul = Principal(
    id="Paul",
    roles={
        "ContentProfile_content_manager_digital_audio",
        "ContentProfile_content_manager_performance_neighbouring_rights"
    },
    attr={
        "profiles": ["Content"],
        "account_id": '888'
    }
)

Allan = Principal(
    id="Allan",
    roles={
        "ContentProfile_content_manager_performance_neighbouring_rights"
    },
    attr={
        "profiles": ["Content"],
        "account_id": '888'
    }
)

Conrad = Principal(
    id="Conrad",
    roles={
        "ContentProfile__content_reviewer_digital_audio"
    },
    attr={
        "profiles": ["Content"],
        "account_id": '*'
    }
)

Nate = Principal(
    id="Nate",
    roles={
        "InsightsProfile_analytics_digital_audio",
        "InsightsProfile_analytics_performance_neighbouring_rights"
    },
    attr={
        "profiles": ["Insights"],
        "account_id": '888'
    }
)
