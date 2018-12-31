# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from affinitic.core.utils import image_format
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import directlyProvides
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
import os


class IServicesList(model.Schema):
    """IServicesList"""

    text = RichText(
        title=_(u"Text"),
        description=_(u"The text to render"),
        required=True)


class ServicesList(Container):
    implements(IServicesList)


class ServicesListView(BrowserView):
    """
    """
    index = ViewPageTemplateFile("templates/services_list.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def services(self):
        return self.context.getFolderContents()

    def image(self, item):
        return image_format(item.getObject())


class IService(model.Schema):
    """IService"""

    text = RichText(
        title=_(u"Text"),
        description=_(u"The text to render"),
        required=True)


class Service(Container):
    implements(IService)


class ServiceView(BrowserView):
    """
    """
    index = ViewPageTemplateFile("templates/service.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def service(self):
        return self.context

    def image(self, item):
        image = getattr(item, 'article_image', False)
        data_image = {}
        if image:
            name, ext = os.path.splitext(image.filename)
            data_image["icon_ext"] = ext
            data_image["icon_data"] = image.data
        else:
            data_image["icon_ext"] = None
            data_image["icon_data"] = None
        return data_image


def vocabularyServices(context):
    catalog = getToolByName(context, 'portal_catalog')
    services = catalog.searchResults(portal_type='Service', sort_order='ascending')
    terms = []

    if services is not None:
        for service in services:
            service_data = service.getObject()
            service_title = service_data.title
            service_id = service_data.id
            terms.append(SimpleVocabulary.createTerm(service_title, service_id, service_title))

    return SimpleVocabulary(terms)


directlyProvides(vocabularyServices, IContextSourceBinder)
