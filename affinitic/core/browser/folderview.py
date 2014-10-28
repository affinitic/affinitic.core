# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class FolderView(BrowserView):
    """
    """

    def getZafs(self):
        return self.context.listFolderContents(contentFilter={"portal_type": "zaf"})
