"""Optional Selenium demonstration for inspecting DLB's rendered HTML.

Requires `pip install -r requirements-selenium.txt` and Google Chrome.
"""
from bs4 import BeautifulSoup
from dlb_scraper import URL, print_groups


def main():
    try:
        from selenium import webdriver
        from selenium.common.exceptions import WebDriverException
    except ImportError:
        print("Install Selenium first: pip install -r requirements-selenium.txt")
        return
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(20)
        driver.get(URL)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        groups = [" ".join(n.stripped_strings) for n in soup.select("ul.res_allnumber")]
        print_groups([g for g in groups if g])
    except WebDriverException as exc:
        print(f"Browser could not load DLB results: {exc}")
    finally:
        if driver is not None:
            driver.quit()


if __name__ == "__main__":
    main()
