# encoding: utf-8
import os


def image_format(item):
    image = getattr(item, 'article_image', False)
    data_image = {}
    if image:
        name, ext = os.path.splitext(image.filename)
        data_image["icon_ext"] = ext
        data_image["icon_data"] = image.data
    else:
        data_image["icon_ext"] = None
        data_image["icon_data"] = None
    return data_image


def get_user_data(pm, user):
    data = pm.getMemberInfo(user.id)
    if data:
        data["function"] = user.getProperty('function')
        data["phone"] = user.getProperty('phone')
        data["cv"] = user.getProperty('cv')
        data["email"] = user.getProperty('email')
        portrait = pm.getPersonalPortrait(user.id)
        data["portrait"] = portrait.absolute_url()
    return data
