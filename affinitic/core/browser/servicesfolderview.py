# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class ServicesFolderView(BrowserView):
    """
    """

    def getServices(self, tag):
        return self.context.listFolderContents(contentFilter={"Subject": tag})
