import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from utils.read_config import get_base_url, get_browser_name
from utils.logger import get_logger

logger = get_logger(__name__)   #  pass module name


@pytest.fixture(scope="function")
def setup(request):
    """Pytest fixture to initialize WebDriver and open the application URL."""
    browser_name = get_browser_name()
    base_url = get_base_url()
    driver = None

    logger.info(f"Setting up WebDriver for browser: {browser_name}")

    if browser_name == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        service = Service()  #  default ChromeDriver service
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(base_url)
    request.cls.driver = driver
    logger.info(f"Navigated to base URL: {base_url}")

    yield
    logger.info("Closing browser session...")
    driver.quit()
    logger.info("Browser closed successfully.")
