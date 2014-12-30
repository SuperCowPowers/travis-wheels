
"""Push wheels up to S3 bucket"""
import boto
from boto.s3.key import Key

_bucket = 'workbench-wheels'
_key = 'py27/wheelhouse.tar.gz'

# Spin up the S3 connection
try:
    conn = boto.connect_s3()
    bucket = conn.get_bucket(_bucket)
    mykey = bucket.get_key(_key)
    if not mykey:
        print 'Could not find key %s, creating a new file...' % _key
        mykey = Key(bucket)
        mykey.key = _key

    # Upload the file
    print 'Uploading wheelhouse.tar.gz file...'
    mykey.set_contents_from_filename('wheelhouse.tar.gz')

    # Make sure the file is publicly readable
    mykey.set_acl('public-read')

except Exception as exc: # Failure
    print 'Blar: %s' % exc
    exit(1)
