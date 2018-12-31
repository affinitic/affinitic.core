# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implements
from plone import schema
from plone.namedfile.field import NamedImage
from Products.CMFPlone import PloneMessageFactory as _
from zope.schema import URI
import os


class IContactsList(model.Schema):
    """IContactsList"""


class ContactsList(Container):
    implements(IContactsList)


class ContactsListView(BrowserView):
    """
    """
    index = ViewPageTemplateFile("templates/contacts_list.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def contacts(self):
        return self.context.getFolderContents()

    def link(self, item):
        item_obj = item.getObject()
        if getattr(item_obj, 'contact_link', False):
            link = getattr(item_obj, 'contact_website', False)
            if link:
                return link
            return item.getURL()
        return False

    def image(self, item):
        image = getattr(item, 'contact_image', False)
        data_image = {}
        if image:
            name, ext = os.path.splitext(image.filename)
            data_image["icon_ext"] = ext
            data_image["icon_data"] = image.data
        else:
            data_image["icon_ext"] = None
            data_image["icon_data"] = None
        return data_image


class IContact(model.Schema):
    """IContact"""

    contact_image = NamedImage(
        title=_(u"Image"),
        required=False,
    )

    contact_email = schema.Email(
        title=_(u'Email'),
        required=False,
        default=None,
    )

    contact_business = schema.TextLine(
        title=_(u'Business Number'),
        required=False,
        default=None,
    )

    contact_date = schema.Date(
        title=u'Date of first activity',
        required=False,
        default=None,
    )

    contact_birthdate = schema.Date(
        title=u'Birth date',
        required=False,
        default=None,
    )

    contact_link = schema.Bool(
        title=_(u'Add link'),
        required=False,
        default=False,
    )

    contact_website = URI(
        title=u'Website',
        required=False,
        default=None,
    )

    # Address
    model.fieldset(
        'address',
        label=_(u'Address'),
        fields=[
            'contact_address',
            'contact_number',
            'contact_city',
            'contact_code',
            'contact_country',
        ],
    )

    contact_address = schema.TextLine(
        title=_(u'Address Line'),
        description=_(u'Street address, P.O box, company name, c/o'),
        required=False,
        default=None,
    )

    contact_number = schema.TextLine(
        title=_(u'Number'),
        description=_(u'Apartement, suite, unit, building, florr, etc.'),
        required=False,
        default=None,
    )

    contact_city = schema.TextLine(
        title=_(u'City'),
        required=False,
        default=None,
    )

    contact_code = schema.Int(
        title=_(u'Postal Code'),
        required=False,
        default=None,
    )

    contact_country = schema.TextLine(
        title=_(u'Country'),
        required=False,
        default=None,
    )

    # Phone
    model.fieldset(
        'phone',
        label=_(u'Phone'),
        fields=[
            'contact_phone',
            'contact_cellphone1',
            'contact_cellphone2',
            'contact_fax',
        ],
    )

    contact_phone = schema.TextLine(
        title=_(u'Phone'),
        required=False,
        default=None,
    )

    contact_cellphone1 = schema.TextLine(
        title=_(u'Cellphone 1'),
        required=False,
        default=None,
    )

    contact_cellphone2 = schema.TextLine(
        title=_(u'Cellphone 2'),
        required=False,
        default=None,
    )

    contact_fax = schema.TextLine(
        title=_(u'Fax'),
        required=False,
        default=None,
    )

    model.fieldset(
        'socialnetworks',
        label=_(u'Social networks'),
        fields=[
            'twitter',
            'facebook',
            'linkedin',
            'github',
            'pinterest',
            'googleplus',
            'instagram',
            'reddit',
            'youtube',
            'vimeo',
            'whatsapp',
        ]
    )

    twitter = schema.TextLine(
        title=_(u'Twitter'),
        required=False,
        default=u'')

    facebook = schema.TextLine(
        title=_(u'Facebook'),
        required=False,
        default=u'')

    linkedin = schema.TextLine(
        title=_(u'Linkedin'),
        required=False,
        default=u'')

    github = schema.TextLine(
        title=_(u'Github'),
        required=False,
        default=u'')

    pinterest = schema.TextLine(
        title=_(u'Pinterest'),
        required=False,
        default=u'')

    googleplus = schema.TextLine(
        title=_(u'Google+'),
        required=False,
        default=u'')

    instagram = schema.TextLine(
        title=_(u'Instagram'),
        required=False,
        default=u'')

    reddit = schema.TextLine(
        title=_(u'Reddit'),
        required=False,
        default=u'')

    youtube = schema.TextLine(
        title=_(u'Youtube'),
        required=False,
        default=u'')

    vimeo = schema.TextLine(
        title=_(u'Vimeo'),
        required=False,
        default=u'')

    whatsapp = schema.TextLine(
        title=_(u'Whatsapp'),
        required=False,
        default=u'')


class Contact(Container):
    implements(IContact)


class ContactView(BrowserView):
    """
    """
    index = ViewPageTemplateFile("templates/contact.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def contact(self):
        return self.context

    def link(self, item):
        if getattr(item, 'contact_link', False):
            link = getattr(item, 'contact_website', False)
            if link:
                return link
            return item.absolute_url()
        return False

    def image(self, item):
        image = getattr(item, 'contact_image', False)
        data_image = {}
        if image:
            name, ext = os.path.splitext(image.filename)
            data_image["icon_ext"] = ext
            data_image["icon_data"] = image.data
        else:
            data_image["icon_ext"] = None
            data_image["icon_data"] = None
        return data_image
