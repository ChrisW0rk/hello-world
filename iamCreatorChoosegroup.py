#!/usr/bin/env python3

import boto3
iam = boto3.client('iam')

def makeuser():
    for response in range(int(input("How many users do you want to create?: "))):
        # create user
        user = input('user name?: ')
        response = iam.create_user(
            UserName = user
        )
        print(response)

        # add to group
        response = iam.add_user_to_group(
            GroupName=input('Choose group to add to: '),
            UserName = user
        )
makeuser()


