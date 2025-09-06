import pytest
from selene import browser, be, have
from selene.core.condition import Condition


def test_login_github_run_with_skip_desktop(setup_browser):
    if setup_browser == 'desktop':
        pytest.xfail(reason='TASK-123 Desktop not supported, check letter')
    browser.open("https://github.com")
    browser.element('.js-header-menu-toggle').should(Condition.by_and(be.clickable)).click()
    browser.element('.HeaderMenu-link--sign-up').should(
        Condition.by_and(be.clickable, have.text("Sign up"))).click()


def test_login_github_run_with_skip_mobile(setup_browser):
    if setup_browser == 'mobile':
        pytest.xfail(reason='TASK-321 Support mobile in develop, check after TASK-4421')
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-up').should(Condition.by_and(
        be.clickable, have.text("Sign up"))).click()
