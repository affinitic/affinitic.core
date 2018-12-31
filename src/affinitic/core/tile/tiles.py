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
        query = {}
        query['portal_type'] = 'Reference'
        brains = self.context.portal_catalog(query)
        if brains:
            results = [brain for brain in brains if getattr(brain.getObject(), 'article_image', False)]
            return results
        return None

    def image(self, item):
        data_image = image_format(item)
        return data_image


class ProjectsTile(Tile):
    """ A tile for mosaic representing a contact card """

    def projects(self):
        query = {}
        query['portal_type'] = 'Reference'
        brains = self.context.portal_catalog(query)
        results = []
        if brains:
            for brain in brains:
                query = {}
                query['portal_type'] = 'Image'
                folder_path = brain.getPath()
                query['path'] = {'query': folder_path, 'depth': 1}
                images_reference = self.context.portal_catalog(query)
                if images_reference:
                    item = {'brain': brain, 'image': images_reference[0]}
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
        self.team = []
        users = api.user.get_users()
        pm = getToolByName(self.context, 'portal_membership')
        for user in users:
            data = get_user_data(pm, user)
            if data:
                self.team.append(data)

        return self.team

    def portal_url(self):
        portal_url = api.portal.get().absolute_url()
        return portal_url
