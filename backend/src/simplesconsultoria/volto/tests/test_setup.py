# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from Products.CMFPlone.utils import get_installer
from simplesconsultoria.volto.testing import SC_SITE_INTEGRATION_TESTING  # noqa: E501

import unittest


class TestSetup(unittest.TestCase):
    """Test that simplesconsultoria.volto is properly installed."""

    layer = SC_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if simplesconsultoria.volto is installed."""
        self.assertTrue(self.installer.isProductInstalled("simplesconsultoria.volto"))

    def test_browserlayer(self):
        """Test that ISCVoltoLayer is registered."""
        from plone.browserlayer import utils
        from simplesconsultoria.volto.interfaces import ISCVoltoLayer

        self.assertIn(ISCVoltoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SC_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["simplesconsultoria.volto"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if simplesconsultoria.volto is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("simplesconsultoria.volto"))

    def test_browserlayer_removed(self):
        """Test that ISCVoltoLayer is removed."""
        from plone.browserlayer import utils
        from simplesconsultoria.volto.interfaces import ISCVoltoLayer

        self.assertNotIn(ISCVoltoLayer, utils.registered_layers())
