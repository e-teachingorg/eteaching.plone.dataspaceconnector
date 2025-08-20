
# eteaching.plone.dataspaceconnector

Plone add-on to connect Plone 6 to the data space of MeinBildungsraum.

eteaching.plone.dataspaceconnector synchronizes the metadata of all CMS documents with the MeinBildungsraum data space. This is done on the basis of subscribers. Every time content is created, updated, or deleted in the CMS, the metadata is synchronized with the MeinBildungsraum data space on the basis of the [AMB](https://dini-ag-kim.github.io/amb/latest/). In addition, a function is provided that initially synchronizes, deletes, or recreates all metadata in the data space.

## Features

- Realizes a connection to the MeinBildungsraum (MBR) data space
- Can provide metadata with the AMB metadata schema
- Can create, delete and rebuild MBR nodes of all content of a plone database in the data space
- Can create, delete and update MBR nodes at runtime

## Prerequisites
* Plone 6.1 (Classic UI), Plone 6.0 (Classic UI)
* Python3 3.10, 3.12, 3.13 (Plone 6.1), 3.8, 3.9, 3.10, 3.11 (Plone 6.0)
* Python3 venv module
* Git
* Valid dataroom credentials (MeinBildungsraum)

## Install with Plone buildout (Plone 6.1)

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
