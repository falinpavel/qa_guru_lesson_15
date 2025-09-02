import pytest

from selene import browser

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope='function')
def browser_type(request):
    return request.param


@pytest.fixture(scope='function')
def resolution(request):
    return request.param


@pytest.fixture(
    autouse=True,
    scope='function'
)
def setup_browser(request, browser_type, resolution):

    width, height = map(int, resolution.split('x'))

    if browser_type == 'chrome':

        chrome_options = ChromeOptions()

        chrome_options.page_load_strategy = 'eager'
        chrome_options.add_argument(f"--window-size={width},{height}")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-dev-shm-usage")

        browser.config.driver_options = chrome_options
        browser.config.driver_name = 'chrome'

    elif browser_type == 'firefox':

        firefox_options = FirefoxOptions()

        firefox_options.page_load_strategy = 'eager'
        firefox_options.add_argument(f"--width={width}")
        firefox_options.add_argument(f"--height={height}")
        firefox_options.add_argument("--disable-web-security")
        firefox_options.add_argument("--allow-running-insecure-content")
        firefox_options.add_argument("--purgecaches")
        firefox_options.add_argument("--disable-gpu")

        browser.config.driver_options = firefox_options
        browser.config.driver_name = 'firefox'

    elif browser_type == 'edge':

        edge_options = EdgeOptions()

        edge_options.page_load_strategy = 'eager'
        edge_options.add_argument(f"--window-size={width},{height}")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--ignore-certificate-errors")

        edge_options.add_argument("--disable-edge-features=msWelcomePage")
        edge_options.add_argument("--disable-edge-features=msHub")
        edge_options.add_argument("--disable-features=msEdgeShoppingAssistant")
        edge_options.add_argument("--disable-features=msEdgeSidebar")

        browser.config.driver_options = edge_options
        browser.config.driver_name = 'edge'

    yield

    browser.quit()

# def pytest_addoption(parser):
#
#     parser.addoption(
#         "--run-mode",
#         help="Run tests in mobile mode or web mode",
#         choices=["web", "mobile"],
#         required=False,
#         default=False
#     )
#
#     parser.addoption(
#         "--browser-type",
#         help="Choose browser",
#         choices=["chrome", "firefox"],
#         required=False,
#         default="chrome"
#     )
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_browser(request):
#
#     browser_type = request.config.getoption("--browser-type")
#     run_mode = request.config.getoption("--run-mode")
#
#     if browser_type == "chrome":
#
#         chrome_options = ChromeOptions()
#         chrome_options.page_load_strategy = 'eager'
#         chrome_options.add_argument("--window-size=430,932") if run_mode == "mobile" \
#             else chrome_options.add_argument("--window-size=1920,1080")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--disable-web-security")
#         chrome_options.add_argument("--allow-running-insecure-content")
#         chrome_options.add_argument("--ignore-certificate-errors")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--disable-software-rasterizer")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#
#         browser.config.driver_options = chrome_options
#
#         yield
#
#         browser.quit()
#
#     if browser_type == "firefox":
#
#         firefox_options = FirefoxOptions()
#         firefox_options.page_load_strategy = 'eager'
#         if run_mode == "mobile":
#             firefox_options.add_argument("--width=430")
#             firefox_options.add_argument("--height=932")
#         else:
#             firefox_options.add_argument("--width=1920")
#             firefox_options.add_argument("--height=1080")
#         firefox_options.add_argument("--disable-web-security")
#         firefox_options.add_argument("--allow-running-insecure-content")
#         firefox_options.add_argument("--purgecaches")
#         firefox_options.add_argument("--disable-gpu")
#
#         browser.config.driver_options = firefox_options
#
#         yield
#
#         browser.quit()
