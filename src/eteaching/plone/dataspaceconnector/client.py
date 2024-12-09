import requests
import base64
import json
from requests.exceptions import MissingSchema


def auth(base_url_aai, client_id, client_secret):
    """Requests a new Bearer-Token from the AAI oidc provider"""
    """This Bearer-Token is necessary to access the 'Datenraum' API"""
    # Definitions
    url = base_url_aai + "/realms/nbp-aai/protocol/openid-connect/token"
    authstring = f"{client_id}:{client_secret}"
    # Headers
    headers = {
        "Authorization": "Basic " + base64.b64encode(authstring.encode()).decode(), # Use base64 encoded CLIENT_ID:CLIENT_SECRET for basic authentication
        "content-type": "application/x-www-form-urlencoded"
    }
    # Payload
    payload = { "grant_type": "client_credentials" }
    # Request
    try:
        response = requests.post(url, data=payload, headers=headers)
    except MissingSchema:
        return False
    return response


def post_node(base_url_dataroom, bearer_token, source_id, external_id, title, description, amb):
    """Creates a new 'node' in the 'Datenraum' API"""
    # Definitions
    url = base_url_dataroom + "/datenraum/api/core/nodes"
    # Headers
    headers = {
        "authorization": "Bearer " + bearer_token,
        "content-type": "application/json"
    }
    # Payload
    payload_dict = {
        "externalId": external_id,
        "sourceId": source_id,
        "title": title,
        "description": description,
        "metadata": amb,
    }
    payload = json.dumps(payload_dict)
    # Request
    response = requests.post(url, data=payload, headers=headers)
    return response


def put_node(base_url_dataroom, bearer_token, node_id, title, description, amb):
    """Updates a 'node' in the 'Datenraum' API"""
    # Definitions
    url = base_url_dataroom + "/datenraum/api/core/nodes/" + node_id    
    # Headers
    headers = {
        "Authorization": "Bearer " + bearer_token,
        "content-type": "application/json"
    }
    # Payload
    payload_dict = {
        "title": title,
        "description": description,
        "metadata": amb,
    }
    payload = json.dumps(payload_dict)
    # Request
    response = requests.put(url, data=payload, headers=headers)
    return response


def delete_node(base_url_dataroom, bearer_token, node_id):
    """Deletes a certain 'node' in de Datenraum API"""
    """Given external_id is an 'internal ID' we know in our system"""
    # Definitions
    url = base_url_dataroom + "/datenraum/api/core/nodes/" + node_id
    # Headers
    headers = {"authorization": "Bearer " + bearer_token}
    # Resopnse    
    response = requests.delete(url, headers=headers)
    return response


def get_node_by_external_id(base_url_dataroom, bearer_token, source_id, external_id):
    """Gets data of a 'node' by its external ID in the 'Datenraum' API"""
    # Definitions
    url = base_url_dataroom + "/datenraum/api/core/nodes/external/" + source_id
    # Headers    
    headers = {"authorization": "Bearer " + bearer_token}
    # Params    
    querystring = {"externalId": external_id}
    # Response
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return False
    return response.json()["id"]


def get_nodes_by_source(base_url_dataroom, bearer_token, source_id, offset=0, limit=20):
    """Gets nodes from the 'Datenraum' API attached to given source"""
    # Definitions
    url = base_url_dataroom + "/datenraum/api/core/nodes"
    # Headers
    headers = {"authorization": "Bearer " + bearer_token}
    # Params
    querystring = {"sourceId": source_id, "offset": offset, "limit": limit}
    # Request
    response = requests.get(url, headers=headers, params=querystring)
    return response
