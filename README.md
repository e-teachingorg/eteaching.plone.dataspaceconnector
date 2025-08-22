
# eteaching.plone.dataspaceconnector

MeinBildungsraum data room integration for Plone.

eteaching.plone.dataspaceconnector synchronises the metadata of all [Plone](https://plone.org/) documents with the [MeinBildungsraum](https://www.meinbildungsraum.de/) data space. This is done on the basis of [subscribers](https://6.docs.plone.org/backend/subscribers.html) (event handlers). Whenever content is created and published, updated or deleted in the CMS, the metadata is synchronised with MeinBildungsraum data space nodes based on [AMB](https://dini-ag-kim.github.io/amb/latest/). In addition, a control panel is provided for creating, deleting or recreating all nodes.

## Features

- Realizes a connection to the MeinBildungsraum (MBR) data space
- Can provide metadata with the AMB metadata schema
- Can create, delete and rebuild MBR nodes of all content of a plone database in the data space
- Can create, delete and update MBR nodes at runtime

## Prerequisites

* Plone 6.1 (Classic UI), Plone 6.0 should also work
* Python 3.10, 3.12, 3.13
* Git
* Valid dataroom credentials (MeinBildungsraum)

## Install with Plone buildout

```bash
git clone https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector.git
cd eteaching.plone.dataspaceconnector
python3 -m venv .
bin/pip install -r https://dist.plone.org/release/6.1-latest/requirements.txt
bin/buildout
```

### Configure

Create a eteaching/plone/dataspaceconnector/credentials.py for your credentials. Use [eteaching/plone/dataspaceconnector/credentialsexample.py](https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector/blob/main/src/eteaching/plone/dataspaceconnector/credentialsexample.py) as template:

```python3
def credentials_mbr():
    return {
        "base_url_aai": "",
        "base_url_dataroom": "",
        "source_id": "",
        "client_id": "",
        "client_secret": "",
    }
```

### Activate

Start the plone instance

```bash
bin/instance fg
```
* Point your browser to http://localhost:8080
* Add a new Plone Site (Classic UI)
* Login with admin admin
* Goto admin --> configuration --> extensions
* eteaching.plone.dataspaceconnector [Install]

## Install as source packages using buildout

Open your dev.cfg

```
[buildout]
extends = buildout.cfg

parts +=
    instance

auto-checkout +=
    eteaching.plone.dataspaceconnector

[instance]
eggs +=
    eteaching.plone.dataspaceconnector

[sources]
eteaching.plone.dataspaceconnector = git https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector.git
```

and then running ``bin/buildout``

### Configure

Create a eteaching/plone/dataspaceconnector/credentials.py for your credentials. Use [eteaching/plone/dataspaceconnector/credentialsexample.py](https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector/blob/main/src/eteaching/plone/dataspaceconnector/credentialsexample.py) as template:

```python3
def credentials_mbr():
    return {
        "base_url_aai": "",
        "base_url_dataroom": "",
        "source_id": "",
        "client_id": "",
        "client_secret": "",
    }
```

### Activate

```bash
* Start Plone
* Point your browser to your plone site
* Login as admin
* Goto configuration --> extensions
* Install eteaching.plone.dataspaceconnector
```

## Authors

[Markus Schmidt](https://github.com/Arkusm)

## Contribute

- Issue Tracker: https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector/issues
- Source Code: https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector

## Support

If you are having issues, please let us know.

## License

The project is licensed under the GPLv2.

## Funding information
The eteaching.plone.dataspaceconnector was funded as part of a publicly financed project by the Federal Ministry of Research, Technology and Space of the Federal Republic of Germany.
