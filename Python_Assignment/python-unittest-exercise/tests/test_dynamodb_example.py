from msilib import Table
from turtle import title
import unittest
import boto3
from moto import mock_dynamodb
from botocore.exceptions import ParamValidationError
from src.boto3_example import DynamodBExample

@mock_dynamodb
def test_create_dynamo_table():
    '''
        Implement the test logic here for testing create_dynamo_table method
    '''

    model_instance = DynamodBExample()
    model_instance.create_movies_table()

@mock_dynamodb
def test_add_dynamo_record_table():
    '''
        Implement the test logic here for testing add_dynamo_record_table method
    '''
    conn = boto3.resource('dynamodb', region_name='us-east-1')
    model_instance = DynamodBExample()
    result = model_instance.add_dynamo_record('Movies', {'year':'2016','title':'The Big Movie'})
    conn.assertEqual(200, result['HTTPStatusCode'])


@mock_dynamodb
def test_add_dynamo_record_table_failure():
    '''
        Implement the test logic here test_add_dynamo_record_table method for failures
    '''
