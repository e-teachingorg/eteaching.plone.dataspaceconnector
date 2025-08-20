from eteaching.plone.dataspaceconnector import client
from plone import api
from eteaching.plone.dataspaceconnector.logger import LOG
from eteaching.plone.dataspaceconnector.amb import AMBMetadata
import math
from eteaching.plone.dataspaceconnector.utils import eid

try:
    from eteaching.plone.dataspaceconnector.credentials import credentials_mbr
except ImportError:
    from eteaching.plone.dataspaceconnector.credentialsexample import credentials_mbr


def access_token(r):
    """Auth"""
    auth_response = client.auth(r["base_url_aai"], r["client_id"], r["client_secret"])
    if not auth_response:
        return False
    if auth_response.status_code != 200:
        LOG.error(
            f"Error Auth: Non expected HTTP response code {auth_response.status_code}"
        )
        return False
    # Token
    return auth_response.json()["access_token"]


def create_nodes(objs):
    # Definitions
    amb_metadata = AMBMetadata()
    r = credentials_mbr()
    bearer_token = access_token(r)
    nodes_len = len(objs)
    result = [f"Creation of {nodes_len} nodes. "]
    if not bearer_token:
        LOG.error("No bearer token found.")
        return False
    # Create objs
    for entry in objs:
        try:
            obj = entry.getObject()
        except Exception:
            obj = entry
        external_id = eid(obj)
        if not external_id:
            continue
        title = getattr(obj, "title", "")
        description = getattr(obj, "description", "")
        amb = amb_metadata.get_amb_metadata(obj)
        # post_node
        create_response = client.post_node(
            r["base_url_dataroom"], bearer_token, r["source_id"], external_id,
            title, description, amb)
        # Analyze result
        if create_response.status_code == 401:  # If Token has expired, try again with new one
            bearer_token = access_token(r)
            create_response = client.post_node(
                r["base_url_dataroom"], bearer_token, r["source_id"],
                external_id, title, description, amb)
        if create_response.status_code != 201:  # If != success log error
            LOG.error(
                f"Creation of node {external_id} failed ({create_response.status_code}). ")
            result.append(
                f"Creation of node {external_id} failed ({create_response.status_code}). ")
            LOG.error(create_response.json())
        else:  # If success log result
            LOG.info(
                f"Successful creation of {external_id}: {create_response.status_code}")

    return result


def delete_nodes(objs):
    # Definitions
    r = credentials_mbr()
    bearer_token = access_token(r)
    nodes_len = len(objs)
    result = [f"Deletion of {nodes_len} nodes. "]
    if not bearer_token:
        LOG.error("No bearer token found.")
        return False
    # Delete objs
    for obj in objs:
        # Get node_id
        external_id = eid(obj)
        if not external_id:
            continue
        node_id = client.get_node_by_external_id(
            r["base_url_dataroom"], bearer_token, r["source_id"], external_id
        )
        if not node_id:
            LOG.error(f"Node with given externalId not found")
            continue
        # delete_node
        delete_response = client.delete_node(r["base_url_dataroom"], bearer_token, node_id)
        # Analyze result
        if (
            delete_response.status_code == 401
        ):  # If Token has expired, try again with new one
            bearer_token = access_token(r)
            delete_response = client.delete_node(
                r["base_url_dataroom"], bearer_token, external_id, node_id
            )
        if delete_response.status_code != 204:  # If != success log error
            LOG.error(f"Deletion of node {external_id} failed ({delete_response.status_code}). ")
            result.append(f"Deletion of node {external_id} failed ({delete_response.status_code}). ")
            LOG.error(delete_response.json())
        else:  # If success log result
            LOG.info(
                f"Successful deletion of {external_id}: {delete_response.status_code}"
            )

    return result


def modify_nodes(objs):
    # Definitions
    amb_metadata = AMBMetadata()
    r = credentials_mbr()
    bearer_token = access_token(r)
    if not bearer_token:
        LOG.error("No bearer token found.")
        return False
    # modify objs
    for obj in objs:
        # Get node_id
        external_id = eid(obj)
        if not external_id:
            continue
        node_id = client.get_node_by_external_id(
            r["base_url_dataroom"], bearer_token, r["source_id"], external_id
        )
        if not node_id:
            LOG.error(f"Modify: Node with given externalId not found!")
            LOG.error(f"Try to create node...")
            create_nodes([obj,])
            continue
        title = getattr(obj, "title", "")
        description = getattr(obj, "description", "")
        amb = amb_metadata.get_amb_metadata(obj)
        # modify_node
        modify_response = client.put_node(
            r["base_url_dataroom"], bearer_token, node_id, title, description, amb
        )
        # Analyze result
        if (
            modify_response.status_code == 401
        ):  # If Token has expired, try again with new one
            bearer_token = access_token(r)
            modify_response = client.delete_node(
                r["base_url_dataroom"], bearer_token, external_id, node_id
            )
        if modify_response.status_code != 204:  # If != success log error
            LOG.error(f"Creation of {external_id}: {modify_response.status_code}")
            LOG.error(modify_response.json())
        else:  # If success log result
            LOG.info(
                f"Successful modification of {external_id}: {modify_response.status_code}"
            )

    return True


def delete_all_nodes():
    """
    Delete all 'nodes' attached to our organization's 'sourceId'"""
    # Definitions
    r = credentials_mbr()
    bearer_token = access_token(r)
    if not bearer_token:
        LOG.error("No bearer token found.")
        return False
    limit = 20
    # Get total
    result = client.get_nodes_by_source(
        r["base_url_dataroom"], bearer_token, r["source_id"], offset=0, limit=1
    )
    total = result.json()["total"]
    result = [f"Deletion of {total} nodes. "]
    # Get count
    e = total / limit
    count = math.ceil(e)
    for _ in range(count):
        nodes = client.get_nodes_by_source(
            r["base_url_dataroom"], bearer_token, r["source_id"], offset=0, limit=20
        )
        for node in nodes.json()["_embedded"]["nodes"]:
            delete_response = client.delete_node(
                r["base_url_dataroom"], bearer_token, node["id"]
            )
            if delete_response.status_code == 401:
                print(f"Token expired. Get new one")
                bearer_token = access_token(r)
                if not bearer_token:
                    LOG.error("No bearer token found.")
                    continue
                delete_response = client.delete_node(
                    r["base_url_dataroom"], bearer_token, node["id"]
                )
            if delete_response.status_code != 204:  # If != success log error
                LOG.error(f"Deletion of node {node['id']} failed ({delete_response.status_code}). ")
                result.append(f"Deletion of node {node['id']} failed ({delete_response.status_code}). ")
                LOG.error(delete_response.json())

            else:  # If success log result
                LOG.info(
                    f"Successful deletion of {node['id']}: {delete_response.status_code}"
                )

    return "".join(result)


def create_all_nodes():
    """Create all nodes"""
    brains = api.content.find(oer_content=True, review_state="published")
    result = create_nodes(brains)
    return "".join(result)


def recreate_all_nodes():
    """Recreate all nodes"""
    r1 = delete_all_nodes()
    r2 = create_all_nodes()
    result = r1 + r2
    return result
