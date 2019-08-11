from ui_test.behave.utilities.driver import WebDriver
from behave import fixture, use_fixture


@fixture
def selenium_browser(context):
    """Start driver before ui_test run"""
    context.w = WebDriver()
    yield context.w
    context.w.quit()


def before_all(context):
    """Prepare ui_test run"""
    use_fixture(selenium_browser, context)
    context.config.setup_logging()
