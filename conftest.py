import pytest
from selene import browser


@pytest.fixture(params=[
    (1920, 1080),
    (1440, 900),
    (1366, 768),
    (1280, 768),
    (430, 932)
])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width > 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()


@pytest.fixture(params=[
    (1920, 1080),
    (1440, 900),
    (1366, 768),
    (1280, 768)
])
def desktop_browser_setup(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield width, height
    browser.quit()


@pytest.fixture(params=[
    (430, 932),
    (375, 667),
    (320, 568)
])
def mobile_browser_setup(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield width, height
    browser.quit()