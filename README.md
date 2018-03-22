# sdbdump

Import/export AWS SimpleDB databases from/to JSON files.

## Requirements

Python 3.6+

## Install

```
pip install sdbdump
```

## Usage
### Import

```
AWS_PROFILE=YOUR_PROFILE sdbdump import --domain=DOMAIN_NAME --input_file=file.json
```

Existing items won't be deleted, but items with the same name will be replaced.

### Export

```
AWS_PROFILE=YOUR_PROFILE sdbdump export --domain=DOMAIN_NAME --output_file=file.json
```
