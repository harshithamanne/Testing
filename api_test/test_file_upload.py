import os
import argparse
from api_test.rescale_api import RescaleApi
from nose.tools import assert_equals, assert_true


def test_file_upload(api_key):
    api = RescaleApi(api_key)
    data = api.request('files/contents/', data={'file': open(os.getcwd() + '/Test.pdf', 'rb')},
                       http_method='POST')
    assert_true(data['isUploaded'])
    data = api.request('files/{file_id}/'.format(file_id=data['id']))
    assert_equals(data['name'], 'Test.pdf')


def main():
    parser = argparse.ArgumentParser(epilog='', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--api_key", help="Please provide api key")
    args = parser.parse_args()
    test_file_upload(args.api_key)


main()
