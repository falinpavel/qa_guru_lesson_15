from selene import browser


def test_login_github():
    browser.open("https://github.com")
