# -*- coding: utf-8 -*-
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from affinitic.core.content.services import vocabularyServices
from affinitic.core.utils import image_format
from plone import schema
from plone.app.textfield import RichText
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope.interface import implements
from plone import api


class IReferencesList(model.Schema):
    """IReferencesList"""

    text = RichText(
        title=_(u"Text"),
        description=_(u"The text to render"),
        required=False)


class ReferencesList(Container):
    implements(IReferencesList)


class ReferencesListView(BrowserView):
    """
    """
    index = ViewPageTemplateFile("templates/references_list.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def references(self):
        return self.context.getFolderContents()

    def image(self, item):
        data_image = image_format(item)
        return data_image

    def gallery(self, brain):
        query = {}
        query['portal_type'] = 'Image'
        folder_path = brain.getPath()
        query['path'] = {'query': folder_path, 'depth': 1}
        images_reference = self.context.portal_catalog(query)
        if images_reference:
            return images_reference[0]
        return None

    def services(self):
        catalog = api.portal.get_tool('portal_catalog')
        services = catalog.searchResults(portal_type='Service', sort_order='ascending')
        references = self.references()
        results = []

        if services is not None:
            for service in services:
                service_data = {}
                service_data["name"] = service.Title
                service_data["url"] = service.getURL()
                service_data["number"] = 0
                for reference in references:
                    list_services = getattr(reference.getObject(), 'reference_service', None)
                    if service.Title in list_services:
                        service_data["number"] += 1
                if service_data["number"]:
                    results.append(service_data)
        return results

    def tags(self):
        tags = []
        references = self.references()
        for reference in references:
            list_tags = getattr(self.context.getFolderContents()[0].getObject(), 'reference_technology', None)
            tags.extend(list_tags)
        results = list(set(tags))
        return results


class IReference(model.Schema):
    """IReference"""

    text = RichText(
        title=_(u"Text"),
        description=_(u"The text to render"),
        required=False)

    reference_website = schema.TextLine(
        title=_(u'Website'),
        required=False,
        default=None,
    )

    reference_technology = schema.Tuple(
        title=_(u'Technology'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )

    directives.widget(
        'reference_technology',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )

    reference_service = schema.List(
        title=_(u'Services'),
        required=False,
        value_type=schema.Choice(source=vocabularyServices),
    )
    directives.widget(reference_service=CheckBoxFieldWidget)

    reference_author = schema.Text(
        title=_(u'Author testimony'),
        required=False,
        default=None,
    )

    reference_function = schema.Text(
        title=_(u'Function of the author of the testimony'),
        required=False,
        default=None,
    )

    reference_testimony = schema.Text(
        title=_(u'Testimony'),
        required=False,
        default=None,
    )

    reference_display = schema.Bool(
        title=_(u'Display in reference'),
        required=False,
        default=True,
    )


class Reference(Container):
    implements(IReference)


class ReferenceView(BrowserView):
    """
    """
    index = ViewPageTemplateFile("templates/reference.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def reference(self):
        return self.context

    def gallery(self):
        return self.context.listFolderContents(contentFilter={"portal_type": "Image"})

    def image(self, item):
        data_image = image_format(item)
        return data_image

    def services(self):
        services = api.content.find(portal_type='Service')
        results = [service.getObject() for service in services if service.id in self.context.reference_service]
        return results
