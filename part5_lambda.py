import boto3
 
def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    filters = [{
                  'Name': 'tag:AutoStart',
                  'Values': ['True']
                 },
                 {
                  'Name': 'instance-state-name',
                  'Values': ['stopped']
}]
    instances = ec2.instances.filter(Filters=filters)
    StoppedInstances = [instance.id for instance in instances]
 
    if len(StoppedInstances) > 0:
        StartInstances = 
ec2.instances.filter(InstanceIds=StoppedInstances).start()
        print (StartInstances)
    else:
        print ("Nothing to see here")