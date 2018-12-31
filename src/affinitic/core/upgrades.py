# -*- coding: utf-8 -*-
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces import INavigationSchema
from Products.PlonePAS.tests import dummy
from plone import api
from plone.app.textfield.value import RichTextValue
from plone.formwidget.namedfile.converter import b64encode_file
from plone.namedfile import NamedImage
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
import os


text_small = _(u'Latius iam disseminata licentia onerosus bonis omnibus Caesar \
    nullum post haec adhibens modum orientis latera cuncta vexabat nec honoratis \
    parcens nec urbium primatibus nec plebeiis.')

text_medium = _(u'Inter haec Orfitus praefecti potestate regebat urbem aeternam ultra \
    modum delatae dignitatis sese efferens insolenter, vir quidem prudens et forensium \
    negotiorum oppido gnarus, sed splendore liberalium doctrinarum minus quam nobilem \
    decuerat institutus, quo administrante seditiones sunt concitatae graves ob inopiam \
    vini: huius avidis usibus vulgus intentum ad motus asperos excitatur et crebros.')

text_large = _(u'Quam ob rem vita quidem talis fuit vel fortuna vel gloria, ut nihil posset \
    accedere, moriendi autem sensum celeritas abstulit; quo de genere mortis difficile \
    dictu est; quid homines suspicentur, videtis; hoc vere tamen licet dicere, P. Scipioni \
    ex multis diebus, quos in vita celeberrimos laetissimosque viderit, illum diem clarissimum \
    fuisse, cum senatu dimisso domum reductus ad vesperum est a patribus conscriptis, populo \
    Romano, sociis et Latinis, pridie quam excessit e vita, ut ex tam alto dignitatis gradu \
    ad superos videatur deos potius quam ad inferos pervenisse.')


def add_content(context):
    change_site_title()
    change_site_logo()
    create_homepage()
    create_about_folder()
    add_about_content()
    add_members()
    create_services_folder()
    add_services()
    create_references_folder()
    add_references()
    create_contacts_folder()
    add_contacts()


def change_site_title():
    api.portal.set_registry_record('plone.site_title', u'Affinitic')


def change_site_logo():
    image = image_format('logo_affinitic_blanc.svg')
    image_encode = b64encode_file(image.filename, image.data)
    api.portal.set_registry_record('plone.site_logo', image_encode)


def create_homepage():
    home_id = 'home'
    title = _(u'Home')
    description = _(u'Home')
    create_content('Document', home_id, title, description, None, 'layout_view', 'publish', None)
    portal = api.portal.get()
    portal.setDefaultPage('home')


def create_about_folder():
    about_id = 'about'
    title = _(u'A propos')
    layout = 'about_view'
    create_content('Folder', about_id, title, text_large, None, layout, 'publish', None)
    portal = api.portal.get()
    about = getattr(portal, 'about', None)
    about.article_image = image_format('reference_image.jpg')


def add_about_content():
    portal = api.portal.get()
    parent = getattr(portal, 'about', None)
    create_content('Document', 'history', _(u'History'), text_medium, parent, 'layout_view', 'publish', None)
    create_content('Document', 'philosophy', _(u'Philosophy'), text_large, parent, 'layout_view', 'publish', None)
    portal = api.portal.get()
    history = getattr(parent, 'history', None)
    history.article_image = image_format('reference_image.jpg')
    philosophy = getattr(parent, 'philosophy', None)
    philosophy.article_image = image_format('reference_image.jpg')


def add_members():
    jeff_properties = {
        'fullname': 'Jean-François Roche',
        'function': _(u'Directeur technique - Gérant'),
        'phone': '+32 (0)497 155 900',
        'cv': text_large,
    }
    api.user.create(
        username='jeff',
        email='jfroche@affinitic.be',
        password='secret',
        properties=jeff_properties,
    )
    api.group.add_user(groupname='manager', username='jeff')

    martin_properties = {
        'fullname': 'Martin Peeters',
        'function': _(u'Software Architect - Gérant'),
        'phone': '+ 32 (0)483 46 08 40',
        'twitter': 'martin',
        'cv': text_large,
    }
    api.user.create(
        username='martin',
        email='martin@affinitic.be',
        password='secret',
        properties=martin_properties,
    )
    api.group.add_user(groupname='manager', username='martin')

    laz_properties = {
        'fullname': 'Laurent Lasudry',
        'function': _(u'Analyste développeur - Chef de projets - Gérant'),
        'phone': '+32 (0)476 733 664',
        'twitter': 'laz',
        'cv': text_large,
    }
    api.user.create(
        username='laz',
        email='laurent@affinitic.be',
        password='secret',
        properties=laz_properties,
    )
    api.group.add_user(groupname='manager', username='laz')

    aurore_properties = {
        'fullname': 'Aurore Mariscal',
        'function': _(u'Développeur - Graphiste'),
        'cv': text_large,
        'linkedin': 'aurore-mariscal',
        'github': 'AuroreMariscal',
    }
    api.user.create(
        username='aurore',
        email='aurore@affinitic.be',
        password='secret',
        properties=aurore_properties,
    )
    api.group.add_user(groupname='employees', username='aurore')

    valentin_properties = {
        'fullname': 'Valentin Piret',
        'function': _(u'Analyste développeur'),
        'cv': text_large,
    }
    api.user.create(
        username='valentin',
        email='valentin@affinitic.be',
        password='secret',
        properties=valentin_properties,
    )
    api.group.add_user(groupname='employees', username='valentin')

    nicolas_properties = {
        'fullname': 'Nicolas Demonte',
        'function': _(u'Analyste développeur'),
        'cv': text_large,
    }
    api.user.create(
        username='nicolas',
        email='nicolas@affinitic.be',
        password='secret',
        properties=nicolas_properties,
    )
    api.group.add_user(groupname='employees', username='nicolas')

    mtool = api.portal.get_tool(name='portal_membership')
    mtool.changeMemberPortrait(user_image_format('jeff.jpg'), id='jeff')
    mtool.changeMemberPortrait(user_image_format('laurent.jpg'), id='laz')
    mtool.changeMemberPortrait(user_image_format('martin.jpg'), id='martin')
    mtool.changeMemberPortrait(user_image_format('aurore.jpg'), id='aurore')
    mtool.changeMemberPortrait(user_image_format('valentin.jpg'), id='valentin')
    mtool.changeMemberPortrait(user_image_format('nicolas.jpg'), id='nicolas')


def create_services_folder():
    folder_id = 'services'
    title = _(u'Services')
    description = _(u'Nos services')
    layout = 'services_list_view'
    create_content('ServicesList', folder_id, title, description, None, layout, 'publish', None)
    portal = api.portal.get()
    services = getattr(portal, 'services', None)
    services.article_image = image_format('reference_image.jpg')
    services.text = RichTextValue(text_large)


def add_services():
    add_service_content(
        'webdesign',
        _(u'Web Design'),
        text_small,
        'service_webdesign.svg',
    )
    add_service_content(
        'development',
        _(u'Development'),
        text_small,
        'service_development.svg',
    )
    add_service_content(
        'cicd_devops',
        _(u'CICD / Devops'),
        text_small,
        'service_cicd.svg',
    )
    add_service_content(
        'webhosting',
        _(u'Web hosting'),
        text_small,
        'service_webhosting.svg',
    )
    add_service_content(
        'coaching',
        _(u'Coaching'),
        text_small,
        'service_coaching.svg',
    )


def add_service_content(service_id, service_title, service_description, image):
    portal = api.portal.get()
    parent = getattr(portal, 'services', None)
    layout = 'service_view'
    create_content('Service', service_id, service_title, service_description, parent, layout, 'publish', True)
    portal = api.portal.get()
    service = getattr(parent, service_id, None)
    service.article_image = image_format(image)


def create_references_folder():
    folder_id = 'references'
    title = _(u'References')
    description = _(u'Nos clients')
    layout = 'references_list_view'
    create_content('ReferencesList', folder_id, title, description, None, layout, 'publish', None)
    portal = api.portal.get()
    references = getattr(portal, 'references', None)
    references.article_image = image_format('reference_image.jpg')
    references.text = RichTextValue(text_large)


def add_references():
    portal = api.portal.get()
    parent = getattr(portal, 'references', None)
    obj = api.content.create(
        type='Reference',
        id='reference1',
        title=_(u'CIRB'),
        description=_(u"Le Centre d’Informatique pour la Région Bruxelloise (CIRB)  est le partenaire informatique de confiance qui, en Région de Bruxelles-Capitale, peut être chargé de toute mission de développement et d'assistance informatique, télématique et cartographique."),
        reference_technology=['python', 'plone 5'],
        reference_website='https://cirb.brussels/',
        reference_service=[u'Web Design', u'Development', u'Coaching', u'CICD / Devops'],
        reference_author=u'Panpan',
        reference_function=u'Lapin',
        reference_testimony=u'Drame en Sologne : un chasseur confond son fils avec un sanglier... \
            et donne une gifle au sanglier!',
        container=parent,
    )
    api.content.transition(obj=obj, transition='publish')
    obj.article_image = image_format('logo_cirb.png')
    obj.text = RichTextValue(text_large)

    api.content.create(
        type='Image',
        id='cirb_image1',
        title=_(u'Homepage'),
        description=_(u'Image 1'),
        image=image_format('cirb_image1.png'),
        container=obj,
    )


def create_contacts_folder():
    folder_id = 'contacts'
    title = _(u'Contacts')
    description = _(u'Contacts')
    layout = 'contacts_list_view'
    create_content('ContactsList', folder_id, title, description, None, layout, 'publish', None)
    portal = api.portal.get()
    folder = getattr(portal, 'contacts', None)
    setattr(folder, 'map_google', True)


def add_contacts():
    portal = api.portal.get()
    parent = getattr(portal, 'contacts', None)
    obj = api.content.create(
        type='Contact',
        id='contact',
        title=_(u'Contact'),
        description=_(u'Contact us'),
        contact_image=image_format('logo_affinitic_blanc.svg'),
        contact_email=u'info@affinitic.be',
        contact_business=u'0882 564 990',
        contact_address=u'rue de la Maîtrise',
        contact_number=u'5B',
        contact_city=u'Belgium',
        contact_code=1400,
        contact_country=u'Nivelles',
        contact_phone=u'+32 (0) 67 63 61 03',
        contact_cellphone1=u'+32 (0) 483 46 08 40',
        twitter=u'affinitic',
        facebook=u'affinitic',
        github=u'affinitic',
        map_google=True,
        marker=True,
        marker_color=u'#025A8F',
        marker_latitude=u'50.581953',
        marker_longitude=u'4.357299',
        container=parent,
    )
    api.content.transition(obj=obj, transition='publish')


def create_content(content_type, id, title, description, parent, layout, transition, exclude):
    portal = api.portal.get()
    if not parent:
        parent = portal
    obj = api.content.create(
        type=content_type,
        id=id,
        title=title,
        description=description,
        container=parent,
    )
    if layout:
        obj.setLayout(layout)
    if not exclude:
        registry = getUtility(IRegistry)
        navigation_settings = registry.forInterface(INavigationSchema, prefix='plone')
        if content_type not in navigation_settings.displayed_types:
            list_types = list(navigation_settings.displayed_types)
            list_types.append(content_type)
            navigation_settings.displayed_types = tuple(list_types)
    obj.reindexObject()
    api.content.transition(obj=obj, transition=transition)


def image_format(filename):
    path_package = os.path.dirname(__file__)
    path_folder = '/static/'
    file_path = '%s%s%s' % (path_package, path_folder, filename)
    image = NamedImage(
        data=open(file_path, 'r').read(),
        filename=unicode(filename),
    )
    return image


def user_image_format(filename):
    path_package = os.path.dirname(__file__)
    path_folder = '/static/team/'
    file_path = '%s%s%s' % (path_package, path_folder, filename)
    data = open(file_path, 'rb')
    image = dummy.FileUpload(dummy.FieldStorage(data))
    return image
