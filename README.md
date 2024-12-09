
# eteaching.plone.dataspaceconnector

Plone add-on to connect Plone 6 to the data space of MeinBildungsraum

## Features

- Realizes a connection to the MeinBildungsraum (MBR) data room
- Can provide metadata with the AMB metadata schema
- Can create, delete and rebuild MBR nodes of all content of a plone database in the data room
- Can create, delete and update MBR nodes at runtime

##  Installation

The package can currently only be installed as a source package. Open your dev.cfg

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
eteaching.mbr.dataroom = git https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector.git
```

and then running ``bin/buildout``

Create a credentials.py for your credentials. Use credentialsexample.py as template.

## Authors

Markus Schmidt

## Contribute

- Issue Tracker: https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector/issues
- Source Code: https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector

## Support

If you are having issues, please let us know.

## License

The project is licensed under the GPLv2.
