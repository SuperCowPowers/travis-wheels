
"""Push wheels up to S3 bucket"""
import boto
conn = boto.connect_s3()
k = Key('workbench-wheels')
k.key = 'py27/wheelhouse.tar.gz'
k.set_contents_from_filename('wheelhouse.tar.gz')
