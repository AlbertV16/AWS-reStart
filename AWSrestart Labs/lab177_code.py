# Python function to count the words in a text file
# This will be the lambda function uploaded

'''
TODO Python
Open text file
Count words
    words are separated by spaces (" ") and newlines (\n)
    I will assume punctuation is always besides a word
return the word count
    (for loop?)
'''

#import boto3

#s3_client = boto3.client('s3')

# Open the text file
def countWords(textfile):
    # open file, split words, and count the number of words
    with open(textfile) as f:
        wordCount = len(f.read().split())
    # return the number of words
    return wordCount

count = countWords('test.txt')
print(count)
'''
# code is made through a combination of qwiklabs(intro to lambda), lab 178, and online sources in the .md file
def handler(event, context):

    # Retrieve the topic ARN and the region where the lambda function is running from the environment variables.

    TOPIC_ARN = os.environ['topicARN']

    # Extract the topic region from the topic ARN.

    arnParts = TOPIC_ARN.split(':')
    TOPIC_REGION = arnParts[3]

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    response = s3.get_object(Bucket=bucket, Key=key)
    print("CONTENT TYPE: " + response['ContentType'])
    return response['ContentType']

    # Create an SNS client, and format and publish a message containing the word count based on the text file uploaded.
    snsClient = boto3.client('sns', region_name=TOPIC_REGION)

    # Publish the message to the topic.
    response = snsClient.publish(
        TopicArn = TOPIC_ARN,
        Subject = 'Word Count Result',
        Message = f("The word count in the file {} is {}.", textfile, wordCount)
    )
'''
