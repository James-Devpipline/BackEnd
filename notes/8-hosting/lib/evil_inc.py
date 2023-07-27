import config
from db import db
from models.organizations import Organizations

query = db.session.query


def create_default_org():
    print(f"Checking if {config.org_name} exists in organizations")
    org_data = query(Organizations).filter(Organizations.name == config.org_name).first()

    if org_data == None:
        print({f"{config.org_name} not found, Curse you Perry the Platypus! Creating {config.org_name} in database"})

        org_data = Organizations(
            name=config.org_name,
            address=config.org_address,
            city=config.org_city,
            state=config.org_state,
            phone=config.org_phone,
            active=True
        )

        db.session.add(org_data)
        db.session.commit()

    else:
        print(f"{config.org_name} found!")
