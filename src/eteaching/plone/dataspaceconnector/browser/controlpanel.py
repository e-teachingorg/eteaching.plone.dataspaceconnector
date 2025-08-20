from plone import api
from eteaching.plone.dataspaceconnector import base
from Products.Five.browser import BrowserView


class DataroomMangementControlpanel(BrowserView):
    """ Data room control panel """    
    
    def __call__(self):

        create = self.request.get("create")
        delete = self.request.get("delete")
        rebuild = self.request.get("rebuild")

        if create:
            result = base.create_all_nodes()
            api.portal.show_message(message=result, request=self.request)
        elif delete:
            result = base.delete_all_nodes()
            api.portal.show_message(message=result, request=self.request)
        elif rebuild:
            result = base.recreate_all_nodes()
            api.portal.show_message(message=result, request=self.request)

        return self.index()
