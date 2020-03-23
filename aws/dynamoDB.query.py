#!/usr/bin/env python3
#from __future__ import print_function

import os, sys, time
import amazondax
import botocore.session

region = os.environ.get('AWS_DEFAULT_REGION', 'us-west-2')

session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region) # low-level client

table_name = "tenant_merge_requests"

if len(sys.argv) > 1:
    endpoint = sys.argv[1]
    dax = amazondax.AmazonDaxClient(session, region_name=region, endpoints=[endpoint])
    client = dax
else:
    client = dynamodb

#pk = 'dev-AUM-1554214712503@autodesk.pw'
pk = '550501_550503'
sk1 = 'SO-259'
sk2 = 'SO-3099'
iterations = 5

params = {
    'TableName': table_name,
    'IndexName': 'requested_by-updated_date-index',
    'ConsistentRead': False,
    'KeyConditionExpression': 'requested_by = :pkval',
    'ExpressionAttributeValues': {
        ":pkval": 'str(pk)'
    }
}
start = time.time()
for i in range(iterations):
 #   result = client.query(**params)
#'ProjectionExpression' : 'requested_by = :pkval',
    result = client.transact_get_items(
        TransactItems =[
            {
                'Get': {
                    'Key': {
                        'id': {
                            'S': pk,
                            } },
                'TableName' : table_name,
                'ProjectionExpression': "#pkval",
                'ExpressionAttributeNames' : {
                    "#pkval": 'id'
                }
                }
            }
        ]
    )

end = time.time()
print('Total time: {} sec - Avg time: {} sec'.format(end - start, (end-start)/iterations))

#print(result)
