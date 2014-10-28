# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class ZafFolderView(BrowserView):
    """
    """

    def getZafs(self):
        return self.context.listFolderContents(contentFilter={"portal_type": "zaf"})
