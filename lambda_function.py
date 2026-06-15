import boto3
import os

ec2 = boto3.client('ec2', region_name='ap-southeast-1')

INSTANCE_ID = os.environ.get('INSTANCE_ID', 'i-0719c9f1692803620')

def lambda_handler(event, context):
    action = event.get('action', 'stop')

    if action == 'stop':
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        print(f"Stopped instance: {INSTANCE_ID}")
        return {'status': 'stopped', 'instance': INSTANCE_ID}

    elif action == 'start':
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        print(f"Started instance: {INSTANCE_ID}")
        return {'status': 'started', 'instance': INSTANCE_ID}