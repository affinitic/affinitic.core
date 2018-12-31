# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from affinitic.core.testing import AFFINITIC_CORE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that affinitic.core is properly installed."""

    layer = AFFINITIC_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if affinitic.core is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'affinitic.core'))

    def test_browserlayer(self):
        """Test that IAffiniticCoreLayer is registered."""
        from affinitic.core.interfaces import (
            IAffiniticCoreLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IAffiniticCoreLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = AFFINITIC_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['affinitic.core'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if affinitic.core is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'affinitic.core'))

    def test_browserlayer_removed(self):
        """Test that IAffiniticCoreLayer is removed."""
        from affinitic.core.interfaces import \
            IAffiniticCoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IAffiniticCoreLayer,
            utils.registered_layers())
