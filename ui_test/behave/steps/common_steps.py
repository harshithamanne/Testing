from behave import when, then
from nose.tools import assert_equals, assert_in
from ui_test.behave.steps import page_dict


@when('user goes to "{url}" as "{page}" page')
def go_to_page(context, url, page):
    """
    Go to url and set page variable
    :param context:
    :param url:
    :param page:
    :return:
    """
    context.w.get(url)
    context.page = page_dict[page](context.w)


@then('user sees "{identifier}" contains text "{text}"')
def element_contains_text(context, identifier, text):
    """
    This method matches to following type of step:
        user sees "{identifier}" contains text "{text}"
    Verify element exists and contains with some text
    :param context:
    :param identifier:
    :param text:
    :return:
    """
    page = context.page
    actual = page.get_text(page.get_element(identifier))
    assert_in(text, actual)


@when('user clicks "{identifier}"')
def click(context, identifier):
    """
    Click on element
    :param context:
    :param identifier:
    :return:
    """
    context.page.click_element(identifier)


@then('user is on "{url}" as "{page}" page')
def on_page(context, url, page):
    """
    Verify current url and set page variable
    :param context:
    :param url:
    :param page:
    :return:
    """
    context.page = page_dict[page](context.w)
    context.w.wait_for_condition(lambda _: context.w.current_url == url)
    assert_equals(context.w.current_url, url)


@when('user types "{text}" in "{identifier}"')
def type_text(context, text, identifier):
    """
    Type text in the element
    :param context:
    :param text:
    :param identifier:
    :return:
    """
    context.page.send_keys_to_element(text, identifier)
