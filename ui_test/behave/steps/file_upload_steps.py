import sys
import os
from behave import when, then
from nose.tools import assert_raises, assert_equals
from selenium.common.exceptions import WebDriverException

Before = 0


@when('user uploads "{file_name}" in "{identifier}"')
def user_file_upload(context, file_name, identifier):
    """
    File upload
    :param context:
    :param identifier:
    :param file_name: file_name of the file to be uploaded
    :return:
    """
    try:
        context.page.get_element(identifier).send_keys(os.getcwd() + '/' + file_name)
    except WebDriverException as exc:
        sys.stderr.write(str(exc) + ' Please create a ui_test file in the specified path')

    context.Before = len(context.page.get_elements('uploaded_files'))


@then('verify "{file_name}" is in uploaded file list')
def verify_file_upload(context, file_name):
    """
    Verify file upload
    :param context:
    :param file_name:
    :return:
    """
    context.w.wait_for_condition(lambda _: len(context.page.get_elements('uploaded_files')) == context.Before + 1)
    files = context.page.get_elements('uploaded_files')
    assert_equals(len(context.page.get_elements('uploaded_files')), context.Before+1)
    for file in files:
        if file_name == file.find_element_by_css_selector('.file-list-name.break-word').text:
            return
    assert_raises('file did not successfully get uploaded')
