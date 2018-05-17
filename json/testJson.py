#import boto3
from gzip import GzipFile
import io
import json
import simplejson
import ijson
from ijson import parse
import time

# S3バケット名
S3_BUCKET_FROM = 'from-bucket'
S3_BUCKET_TO = 'to-bucket'


# 取得するファイル名
KEY1 = 'one.json.gz'
KEY2 = 'two.json.gz'
KEY3 = 'two-big.json.gz'

# オブジェクト生成
#s3_client = boto3.client('s3')
#s3_resource = boto3.resource('s3')

def do_one():
    f = open(KEY1,'rb')
    buffer = io.BytesIO(f.read())
    unzipFile=GzipFile(None, 'rb', fileobj=buffer)
    #for prefix, event, value in parser:
    #    print('prefix={}, event={}, value={}'.format(prefix, event, value))
    ones = ijson.items(unzipFile,'ones.item')
    #for one in ones:
    #  print(json.dumps(one))
    with open('ones.json','w') as outFile:
        outFile.write("\n".join(json.dumps(one) for one in ones))
    #s3_client.upload_fileobj(GzipFile(None, 'rb', fileobj=buffer), S3_BUCKET_TO, "twos_loop_2000.json")


def do_two():
    f = open(KEY2,'rb')
    buffer = io.BytesIO(f.read())
    unzipFile=GzipFile(None, 'rb', fileobj=buffer)
    twos = ijson.items(unzipFile,'twos')
    with open('twos_big.json','w') as outFile:
        for two in twos:
            outFile.write("\n".join(simplejson.dumps(twoValue) for twoValue in two.values()))
    #s3_client.upload_fileobj(GzipFile(None, 'rb', fileobj=buffer), S3_BUCKET_TO, "twos_loop_2000.json")

def do_big_two():
    start = time.time()
    f = open(KEY3,'rb')
    buffer = io.BytesIO(f.read())
    unzipFile=GzipFile(None, 'rb', fileobj=buffer)
    twos = ijson.items(unzipFile,'twos')
    with open('twos.json','w') as outFile:
        for two in twos:
            outFile.write("\n".join(simplejson.dumps(twoValue) for twoValue in two.values()))
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

#do_one()
#do_two()
do_big_two()

