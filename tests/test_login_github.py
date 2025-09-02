import pytest

from selene import browser, be, have
from selene.core.condition import Condition


@pytest.mark.parametrize('browser_type', ['chrome', 'firefox', 'edge'], indirect=True)
@pytest.mark.parametrize('resolution', ['1920x1080', '430x932'],
                         ids=['web (fullscreen)', 'mobile (iPhone 14 Pro Max)'],
                         indirect=True)
def test_login_github_run_all_combinations(browser_type, resolution):
    browser.open("https://github.com")
    if resolution == '430x932':
        browser.element('.js-header-menu-toggle').should(Condition.by_and(be.clickable)).click()
        browser.element('.HeaderMenu-link--sign-up').should(
            Condition.by_and(be.clickable, have.text("Sign up"))).click()
    else:
        browser.element('.HeaderMenu-link--sign-up').should(Condition.by_and(
            be.clickable, have.text("Sign up"))).click()


@pytest.mark.parametrize('browser_type', ['chrome', 'firefox', 'edge'], indirect=True)
@pytest.mark.parametrize('resolution', ['1920x1080', '430x932'],
                         ids=['web (fullscreen)', 'mobile (iPhone 14 Pro Max)'],
                         indirect=True)
def test_login_github_skip_all_mobile(browser_type, resolution):
    if resolution == '430x932':
        pytest.skip(reason="TASK-12 'All mobile is not supported this'")
    else:
        browser.open("https://github.com")
        browser.element('.HeaderMenu-link--sign-up').should(Condition.by_and(
            be.clickable, have.text("Sign up"))).click()


@pytest.mark.parametrize('browser_type', ['chrome', 'firefox', 'edge'], indirect=True)
@pytest.mark.parametrize('resolution', ['1920x1080', '430x932'],
                         ids=['web (fullscreen)', 'mobile (iPhone 14 Pro Max)'],
                         indirect=True)
def test_login_github_skip_edge_browser_fullscreen(browser_type, resolution):
    if browser_type == 'edge' and resolution != '430x932':
        pytest.skip(reason="TASK-96 'Browser Edge (fullscreen) is not supported this'")
    else:
        if resolution == '430x932':
            browser.open("https://github.com")
            browser.element('.js-header-menu-toggle').should(Condition.by_and(be.clickable)).click()
            browser.element('.HeaderMenu-link--sign-up').should(
                Condition.by_and(be.clickable, have.text("Sign up"))).click()
        else:
            browser.open("https://github.com")
            browser.element('.HeaderMenu-link--sign-up').should(Condition.by_and(
                be.clickable, have.text("Sign up"))).click()
