# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import simplesconsultoria.volto


class SCVoltoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=simplesconsultoria.volto)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "simplesconsultoria.volto:default")


SC_SITE_FIXTURE = SCVoltoLayer()


SC_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SC_SITE_FIXTURE,),
    name="SCVoltoLayer:IntegrationTesting",
)


SC_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SC_SITE_FIXTURE,),
    name="SCVoltoLayer:FunctionalTesting",
)


SC_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SC_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="SCVoltoLayer:AcceptanceTesting",
)
