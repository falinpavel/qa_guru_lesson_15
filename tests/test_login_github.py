import pytest
from selene import browser, be, have
from selene.core.condition import Condition


def test_login_github(request):
    browser.open("https://github.com")
    if request.config.getoption("--run-mode") == "mobile":
        browser.element('.js-header-menu-toggle').should(Condition.by_and(be.clickable)).click()
        browser.element('.HeaderMenu-link--sign-up').should(
            Condition.by_and(be.clickable, have.text("Sign up"))).click()
    else:
        browser.element('.HeaderMenu-link--sign-up').should(Condition.by_and(
            be.clickable, have.text("Sign up"))).click()
