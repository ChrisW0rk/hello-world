#!/usr/bin/env python3

import boto3
iam = boto3.client('iam')

def makeuser():
    for response in range(int(input("How many users do you want to create?: "))):
        # create user
        response = iam.create_user(
            UserName=input()
        )
        print(response)
makeuser()