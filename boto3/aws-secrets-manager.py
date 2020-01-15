#!/usr/bin/python3

# Just a quick reference for the basics you need to get and store secrets in
# AWS Secrets Manager using Python and Boto3
#
# There are what some might consider an excessive amount of comments here.
# "No such thing as overkill."
#
# Written by James Berger, January 15th 2020

import boto3
from botocore.exceptions import ClientError

# Usage: variable_you_want_to_contain_secret = get_secret('Name of your secret')
# Note: The secret name and the secret ARN are two different things.
def get_secret(secret_name):
    # Note: The region name doesn't need to be hardcoded, you can pass it in if
    # desired. It was just simpler to have it definined in the function itself
    # for my use case.
    region_name = "us-west-2"
    # If you're using stored credentials on your server in the ~/.aws directory
    # for example, and you have multiple sets of credentials, say one set for
    # prod and one for dev, you can specify which credentials to use by
    # uncommenting line 37 below and swapping 'prod' with the name of your
    # actual credential profile name.
    #
    # For example, your ~/.aws/credentials file might look like this:
    #
    # [prod]
    # aws_access_key_id = YOUR_AWS_ACCESS_KEY_ID
    # aws_secret_access_key = YOUR_AWS_SECRET_ACCESS_KEY
    #
    # [dev]
    # aws_access_key_id = YOUR_AWS_ACCESS_KEY_ID
    # aws_secret_access_key = YOUR_AWS_SECRET_ACCESS_KEY

    #session = boto3.session.Session(profile_name='prod')
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
    )
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
    else:
        # Secrets Manager decrypts the secret value using the associated KMS CMK
        # Depending on whether the secret was a string or binary, only one of
        # these fields will be populated
        if 'SecretString' in get_secret_value_response:
            text_secret_data = get_secret_value_response['SecretString']
            return (text_secret_data)
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']


# Usage: create_secret('MySecretName', 'MySecretValue', 'DescriptionOfMySecret', 'SecretTagKey', 'SecretTagValue')
# Note: You can have multiple tags, there's just a single one here for clarity
def create_secret(secret_name, secret_string, secret_description, secret_tag_key1, secret_tag_value1):
    region_name = "us-west-2"
    #session = boto3.session.Session(profile_name='prod')
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
    )
    try:
        response = client.create_secret(
            Name=secret_name,
            Description=secret_description,
            SecretString=secret_string,
            Tags=[
                {
                    'Key': secret_tag_key1,
                    'Value': secret_tag_value1
                },
            ]
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)


# Example variables we're using to pass values to our functions
secret_name = 'YourSecretNameHere'
secret_value = 'YourStrongPasswordHere'
secret_tag_key = 'YourTagKeyHere'
secret_tag_value = 'YourTagValueHere'


# Storing secrets:

# A more simple method for clarity
# Note: This does not store it in JSON format, so there's no secret key / value pairs
create_secret(secret_name, secret_value, 'This secret contains the credentials for YourExampleHere', secret_tag_key, secret_tag_value)

# Storing a secret in valid JSON so you get nice secret key / secret value pairs
# In this example, we're storing a root password so the resulting secret looks like this:
# user: root
# root password: YourStrongPasswordHere
create_secret('an/example/path/' + secret_name, '{\"user\": \"root\", \"root password\": \"' + secret_value + '\"}', 'This secret contains the credentials for YourExampleHere', secret_tag_key, secret_tag_value)


# Retrieving secrets:
# Note: The secret name and the secret ARN are two different things.

your_secure_secret = get_secret('NameOfYourSecret')
