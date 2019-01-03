# encoding: utf-8
from Products.CMFCore.utils import getToolByName
from affinitic.core.utils import get_user_data
from affinitic.core.utils import image_format
from plone import api
from plone.tiles.tile import Tile
from random import randint


class ServicesTile(Tile):
    """ A tile for mosaic representing a contact card """

    def services(self):
        query = {}
        query['portal_type'] = 'Service'
        brains = self.context.portal_catalog(query)
        return brains

    def image(self, item):
        return image_format(item.getObject())


class AboutTile(Tile):
    """ A tile for mosaic representing a contact card """

    def about(self):
        portal = api.portal.get()
        about = getattr(portal, 'about', None)
        return about


class ReferencesTile(Tile):
    """ A tile for mosaic representing a contact card """

    def references(self):
        portal = api.portal.get()
        references = getattr(portal, 'references', None)
        results = []
        if references:
            brains = references.listFolderContents(contentFilter={"portal_type": "Reference"})
        if brains:
            results = [brain for brain in brains if getattr(brain, 'article_image', False) and getattr(brain, 'reference_display', False)]
            return results
        return None

    def image(self, item):
        data_image = image_format(item)
        return data_image


class ProjectsTile(Tile):
    """ A tile for mosaic representing a contact card """

    def projects(self):
        portal = api.portal.get()
        references = getattr(portal, 'references', None)
        results = []
        if references:
            brains = references.listFolderContents(contentFilter={"portal_type": "Reference"})
        if brains:
            for brain in brains:
                images_reference = brain.listFolderContents(contentFilter={"portal_type": "Image"})
                if images_reference:
                    item = {'url': brain.absolute_url(),
                            'image': images_reference[0].absolute_url(),
                            'title': brain.Title}
                    results.append(item)
        return results


class TestimonyTile(Tile):
    """ A tile for mosaic representing a contact card """

    def service(self):
        query = {}
        query['portal_type'] = 'Reference'
        brains = self.context.portal_catalog(query)
        if brains:
            results = [brain for brain in brains if getattr(brain.getObject(), 'reference_testimony', False)]
            if results:
                result = results[randint(0, len(results) - 1)]
                if result:
                    return result.getObject()
        return None


class TeamTile(Tile):
    """ A tile for mosaic representing a contact card """

    def team(self):
        return api.content.find(portal_type='Member')
