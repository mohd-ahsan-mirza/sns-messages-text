import boto3
sns = boto3.client('sns')
def process(context,event):
    topicArn = [x for x in sns.list_topics()['Topics'] if x['TopicArn'].endswith('personal-site-message')][0]['TopicArn']
    print(topicArn)
    sns.publish(TopicArn=topicArn,Message='Coming from the script')