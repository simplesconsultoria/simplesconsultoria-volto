# -*- coding: utf-8 -*-
from AccessControl.SecurityManagement import newSecurityManager
from Products.CMFPlone.factory import _DEFAULT_PROFILE, addPloneSite
from Testing.makerequest import makerequest

import transaction


app = makerequest(app)

admin = app.acl_users.getUserById("admin")
admin = admin.__of__(app.acl_users)
newSecurityManager(None, admin)

site_id = "simples"
payload = {
    "title": "Simples Consultoria",
    "profile_id": _DEFAULT_PROFILE,
    "extension_ids": [
        "simplesconsultoria.volto:default",
    ],
    "setup_content": False,
    "default_language": "en",
    "portal_timezone": "Europe/Berlin",
}

if site_id in app.objectIds():
    app.manage_delObjects([site_id])

transaction.commit()

site = addPloneSite(app, site_id, **payload)
transaction.commit()
