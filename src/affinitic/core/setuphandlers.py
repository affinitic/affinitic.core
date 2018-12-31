# -*- coding: utf-8 -*-
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces import INonInstallable
from plone import api
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation
from zope.interface import implementer
from Products.PlonePAS import config


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'affinitic.core:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    hide_element_navigation(['front-page', 'Members'])
    create_group_managers()
    create_group_employees()
    change_size_user_image()


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def hide_element_navigation(contents):
    portal = api.portal.get()
    for content in contents:
        content_type = getattr(portal, content, None)
        if content_type:
            adapter = IExcludeFromNavigation(content_type, None)
            adapter.exclude_from_nav = True
            content_type.reindexObject()


def create_group_managers():
    api.group.create(
        groupname='manager',
        title=_(u'Managers'),
        description=_(u'Our managers'),
        roles=['Site Administrator', ],
    )


def create_group_employees():
    api.group.create(
        groupname='employees',
        title=_(u'Employees'),
        description=_(u'Our employees'),
        roles=['Contributor', ],
    )


def change_size_user_image():
    MEMBER_IMAGE_SCALE = (300, 300)
    MEMBER_IMAGE_QUALITY = 100
    config.MEMBER_IMAGE_SCALE = MEMBER_IMAGE_SCALE
    config.IMAGE_SCALE_PARAMS['scale'] = MEMBER_IMAGE_SCALE
    config.IMAGE_SCALE_PARAMS['quality'] = MEMBER_IMAGE_QUALITY
