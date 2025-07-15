import boto3

def get_ec2_instance_status(region_name='us-east-1'):
    # Create EC2 client connection using boto
    ec2 = boto3.client('ec2', region_name=region_name)

    try:
        # Fetch EC2 instances data
        response = ec2.describe_instances()
        instances = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance.get('InstanceId')
                state = instance.get('State', {}).get('Name')
                instances.append({
                    'InstanceId': instance_id,
                    'Status': state
                })

        return instances

    except Exception as e:
        print(f"Error fetching EC2 instances: {e}")
        return []

# Example usage
if __name__ == "__main__":
    ec2_status_list = get_ec2_instance_status()
    for instance in ec2_status_list:
        print(f"Instance ID: {instance['InstanceId']} - Status: {instance['Status']}")
