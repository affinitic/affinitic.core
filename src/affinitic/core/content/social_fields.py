# encoding: utf-8
from plone.supermodel import model
from plone import schema
from Products.CMFPlone import PloneMessageFactory as _


class ISocialFields(model.Schema):
    """
    """

    model.fieldset(
        'socialnetworks',
        label=_(u'Social networks'),
        fields=[
            'twitter',
            'facebook',
            'linkedin',
            'github',
            'gitlab',
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

    gitlab = schema.TextLine(
        title=_(u'Gitlab'),
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
