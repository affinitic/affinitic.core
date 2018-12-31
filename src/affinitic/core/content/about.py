# encoding: utf-8
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from affinitic.core.utils import image_format
from affinitic.core.utils import get_user_data
from plone import api


class AboutView(BrowserView):
    index = ViewPageTemplateFile("templates/about.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def documents(self):
        return self.context.listFolderContents(contentFilter={"portal_type": "Document"})

    def team(self):
        self.team = []
        users = api.user.get_users()
        pm = getToolByName(self.context, 'portal_membership')
        for user in users:
            data = get_user_data(pm, user)
            if data:
                self.team.append(data)

        return self.team

    def image(self, item):
        data_image = image_format(item)
        return data_image


class MemberView(BrowserView):
    index = ViewPageTemplateFile("templates/member.pt")

    def render(self):
        return self.index()

    def __call__(self):
        return self.render()

    def member(self):
        data = None
        form = getattr(self.request, 'form', None)
        if form:
            if 'member' in form:
                username = form["member"]
                member = api.user.get(username=username)
                if member:
                    pm = getToolByName(self.context, 'portal_membership')
                    data = get_user_data(pm, member)
        return data
