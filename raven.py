"""Dictate the app behaviour."""

import boto3
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://jmck.raven.s3-website-eu-west-1.amazonaws.com'])

# Initialize dynamodb access
dynamodb = boto3.resource('dynamodb')
db = dynamodb.Table('raven-dev')


@app.route('/counter', methods=['GET'])
def counter_get():
    """Return counter number."""
    res = db.get_item(Key={'id': 'counter'})
    return jsonify({'counter': res['Item']['counter_value']})


@app.route('/counter/increase', methods=['POST'])
def counter_increase():
    """Add to counter."""
    res = db.get_item(Key={'id': 'counter'})
    value = res['Item']['counter_value'] + 1
    res = db.update_item(
        Key={'id': 'counter'},
        UpdateExpression='set counter_value=:value',
        ExpressionAttributeValues={':value': value},
    )
    return jsonify({'counter': value})
