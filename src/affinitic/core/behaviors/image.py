# encoding: utf-8
from affinitic.viewlet.geomarker import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedImage
from zope.interface import Interface
from zope.interface import alsoProvides


class IImage(Interface):
    """
    """

    article_image = NamedImage(
        title=_(u"Image"),
        required=False,
    )


alsoProvides(IImage, IFormFieldProvider)
