# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class ClientFolderView(BrowserView):
    """
    """

    def getClients(self):
        return self.context.listFolderContents(contentFilter={"portal_type": "Client"})
