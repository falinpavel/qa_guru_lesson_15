from selene import browser, be, have
from selene.core.condition import Condition


def test_login_github_run_only_mobile_browsers(mobile_browser_setup):
    browser.open("https://github.com")
    browser.element('.js-header-menu-toggle').should(Condition.by_and(be.clickable)).click()
    browser.element('.HeaderMenu-link--sign-up').should(
        Condition.by_and(be.clickable, have.text("Sign up"))).click()

def test_login_github_run_only_desktop_browser(desktop_browser_setup):
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-up').should(Condition.by_and(
        be.clickable, have.text("Sign up"))).click()
