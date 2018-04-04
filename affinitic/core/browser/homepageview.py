# -*- coding: utf-8 -*-
from datetime import datetime
from Products.Five import BrowserView
from urllib2 import urlopen
import json


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

    def getNumberRepoGit(self):
        try:
            response = urlopen("https://api.github.com/users/affinitic")
            data = response.read().decode("utf-8")
            json_data = json.loads(data)
            repo = json_data["public_repos"]
        except:
            repo = None
        return repo

    def getBirthday(self):
        date_now = datetime.now()
        year_now = date_now.year
        date_birth = datetime(2006, 7, 11)
        year_birth = date_birth.year
        birthday = year_now - year_birth
        return birthday
