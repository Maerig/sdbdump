import argparse
import json
import sys

from sdbdump.sdb_helper import SdbHelper


def run():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Command", dest='command')
    subparsers.required = True

    import_parser = subparsers.add_parser('import', help="Import a JSON file into SimpleDB")
    import_parser.add_argument("-d", "--domain", required=True, help="SimpleDB domain")
    import_parser.add_argument("-i", "--input-file", required=True, help="Path for the input JSON file")

    export_parser = subparsers.add_parser('export', help="Import a JSON file into SimpleDB")
    export_parser.add_argument("-d", "--domain", required=True, help="SimpleDB domain")
    export_parser.add_argument("-o", "--output-file", help="Path for the output JSON file")

    args = parser.parse_args()

    sdb_helper = SdbHelper()

    command = args.command
    if command == 'import':
        with open(args.input_file) as json_file:
            items = json.load(json_file)
        sdb_helper.set_items(args.domain, items)

    elif command == 'export':
        domain = args.domain
        items = sdb_helper.get_items(domain)

        if args.output_file:
            with open(args.output_file, 'w+') as json_file:
                json.dump(list(items), json_file, separators=(',', ':'))
        else:
            json.dump(list(items), sys.stdout, separators=(',', ':'))


if __name__ == '__main__':
    run()
