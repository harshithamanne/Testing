from ui_test.behave.pages.BasePage import BasePage


class Login(BasePage):
    header = 'h3.greeting'
    email_input = 'div.box.email-box input.active-input'
    next_step = 'div.next-step'
    password_input = 'input[name=password]'
    sign_in = 'button[type=submit].input-link'
