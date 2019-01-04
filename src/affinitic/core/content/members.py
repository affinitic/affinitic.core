# -*- coding: utf-8 -*-
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from affinitic.core.content.services import vocabularyServices
from affinitic.core.utils import image_format
from plone import api
from plone import schema
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope.interface import implements
from affinitic.core.content.social_fields import ISocialFields


class IMembersList(model.Schema):
    """IMembersList"""

    text = RichText(
        title=_(u"Text"),
        description=_(u"The text to render"),
        required=False)


class MembersList(Container):
    implements(IMembersList)


class MembersListView(BrowserView):
    """
    """
    index = ViewPageTemplateFile("templates/members_list.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def members(self):
        return self.context.getFolderContents()

    def image(self, item):
        return image_format(item.getObject())


class IMember(model.Schema, ISocialFields):
    """IMember"""

    member_function = schema.TextLine(
        title=_(u'Function'),
        required=False,
        default=None,
    )

    member_email = schema.Email(
        title=_(u'Email'),
        required=False,
        default=None,
    )

    member_phone = schema.TextLine(
        title=_(u'Phone'),
        required=False,
        default=None,
    )

    member_service = schema.List(
        title=_(u'Compétences'),
        required=False,
        value_type=schema.Choice(source=vocabularyServices),
    )
    directives.widget(member_service=CheckBoxFieldWidget)

    member_cv = RichText(
        title=_(u"CV"),
        description=_(u"CV complet"),
        required=False)


class Member(Container):
    implements(IMember)


class MemberView(BrowserView):
    index = ViewPageTemplateFile("templates/member.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def member(self):
        return self.context

    def image(self, item):
        data_image = image_format(item)
        return data_image

    def services(self):
        results = None
        if self.context.member_service:
            services = api.content.find(portal_type='Service')
            results = [service.getObject() for service in services if service.id in self.context.member_service]
        return results
