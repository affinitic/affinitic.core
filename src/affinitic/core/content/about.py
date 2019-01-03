# encoding: utf-8
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from affinitic.core.utils import image_format
from plone import api


class AboutView(BrowserView):
    index = ViewPageTemplateFile("templates/about.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def documents(self):
        return self.context.listFolderContents(contentFilter={"portal_type": "Document"})

    def team(self):
        return api.content.find(portal_type='Member')

    def image(self, item):
        data_image = image_format(item)
        return data_image
