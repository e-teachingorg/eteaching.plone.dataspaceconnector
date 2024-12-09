from eteaching.plone.dataspaceconnector import base

def create_node(context):
    base.create_nodes([context,])

def delete_node(context):
    base.delete_nodes([context,])

def modify_node(context):
    base.modify_nodes([context,])
    