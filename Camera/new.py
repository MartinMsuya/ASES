import boto3


s3 = boto3.resource('s3',
  endpoint_url = 'https://2bf52450aac554dba7bbf2c208c160eb.r2.cloudflarestorage.com',
  aws_access_key_id = '6fcfed8a198cb47f1de028ce1488c654',
  aws_secret_access_key = 'c4d55fcab6f38efc96c91d4b14b6ce9e1e1be98aaebc2401775e1984f15fb66e'
)

print('Buckets:')
for bucket in s3.buckets.all():
  print(' - ', bucket.name)


bucket = s3.Bucket('imageserver')

print('Objects:')
for item in bucket.objects.all():
  print(' - ', item.key)

s3.meta.client.upload_file('overspeeding\\cars\\22-06-2023-09-20-15-297046.jpeg', 'imageserver', 'pic1.jpeg')
