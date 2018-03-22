import boto3


class SdbHelper(object):
    def __init__(self):
        self.client = boto3.client('sdb')

    def get_items(self, domain):
        select_params = {
            'SelectExpression': f"SELECT * FROM `{domain}`",
            'ConsistentRead': True
        }

        while True:
            resp = self.client.select(**select_params)
            for item in resp['Items']:
                yield {
                    'Name': item['Name'],
                    'Attributes': item['Attributes']
                }

            if 'NextToken' not in resp:
                break
            # Else continue pagination
            select_params['NextToken'] = resp['NextToken']

    def set_items(self, domain, items):
        self.client.batch_put_attributes(
            DomainName=domain,
            Items=[
                {
                    'Name': item['Name'],
                    'Attributes': [
                        {
                            'Name': attribute['Name'],
                            'Value': attribute['Value'],
                            'Replace': True
                        }
                        for attribute in item['Attributes']
                    ]
                }
                for item in items
            ]
        )
