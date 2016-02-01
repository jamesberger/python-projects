import boto

from boto.s3.connection import S3Connection

conn = S3Connection('AKIAJ44SU64NZ7HNNKVA','lWQEXu1Q0noSDujRr78eNSK6jwxDTjAArjmpZwxH')

bucket = conn.create_bucket('mahbuckitlogshalp')

from boto.s3.key import Key

k = Key(bucket)

k.key = 'initial-test-file'

k.set_contents_from_string('Halp theyze stealin mah buckit')
