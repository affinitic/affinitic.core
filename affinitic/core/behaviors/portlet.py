# encoding: utf-8

from plone.supermodel import model, directives
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import alsoProvides
from plone.namedfile.field import NamedImage
from plone.app.textfield import RichText


class IPortlet(model.Schema):

    directives.fieldset(
        'portlet',
        label=u'Portlet',
        fields=('title_portlet', 'description_portlet', 'background1', 'background2'),
    )

    title_portlet = schema.TextLine(
        title=u"Title",
        required=False,
    )

    description_portlet = RichText(
        title=u"Description",
        required=False,
    )

    background1 = NamedImage(
        title=u"Background 1",
        required=False,
    )

    background2 = NamedImage(
        title=u"Background 2",
        required=False,
    )


alsoProvides(IPortlet, IFormFieldProvider)
