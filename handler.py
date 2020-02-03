import boto3
import json
import os
import urllib

client = boto3.client('lambda')


def main(event=None, context=None):
    print(event)
    body = event['body']
    params = urllib.parse.parse_qs(body)
    print(params)

    text = params.get('text')
    if text is None:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'text': 'なに？',
                'response_type': 'in_channel',
            })
        }

    action = text[0]
    if action not in ['calc', 'choice']:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'text': '？？？？？',
                'response_type': 'in_channel',
            })
        }

    client.invoke(
        FunctionName=os.environ[action],
        InvocationType='Event',
        Payload=json.dumps(params)
    )
    return {
        'statusCode': 200,
        'body': 'ちょっと待ってね',
    }
    # client.invoke()
