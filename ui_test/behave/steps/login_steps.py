import os
from behave import when
from ui_test.behave.steps import page_dict


@when('user logs in')
def login(context):
    """
    user login
    :type context: behave.runner.Context
    """
    context.execute_steps(
        """
            When user types "{email}" in "email_input"
            And user clicks "next_step"
            When user types "{password}" in "password_input"
            When user clicks "sign_in"

        """.format(email=os.environ['email'], password=os.environ['password']))

    context.page = page_dict['Introduction'](context.w)
