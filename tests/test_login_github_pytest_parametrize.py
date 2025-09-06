import pytest
from selene import browser, be, have
from selene.core.condition import Condition


@pytest.mark.parametrize(
    'mobile_browser_setup', [(430, 932)],
    indirect=True,
    ids=['iphone 14 pro max']
)
def test_login_github_run_only_mobile_browsers(mobile_browser_setup):
    browser.open("https://github.com")
    browser.element('.js-header-menu-toggle').should(Condition.by_and(be.clickable)).click()
    browser.element('.HeaderMenu-link--sign-up').should(
        Condition.by_and(be.clickable, have.text("Sign up"))).click()

@pytest.mark.parametrize(
    'desktop_browser_setup', [(1920, 1080), (1366, 768)],
    indirect=True,
    ids=['full hd','760p']
)
def test_login_github_run_only_desktop_browser(desktop_browser_setup):
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-up').should(Condition.by_and(
        be.clickable, have.text("Sign up"))).click()
