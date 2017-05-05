# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class ServicesFolderView(BrowserView):
    """
    """

    def getServices(self):
        return self.context.listFolderContents(contentFilter={"portal_type": "slides"})
