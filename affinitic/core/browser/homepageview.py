
# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class HomepageView(BrowserView):
    """
    """
    def getObjectType(self, type_name):
        catalog = getattr(self.context, 'portal_catalog')
        brains = catalog.searchResults(portal_type=type_name)
        return brains

    def getObjectTag(self, tag_name):
        catalog = getattr(self.context, 'portal_catalog')
        brains = catalog.searchResults(Subject=(tag_name))
        return brains
