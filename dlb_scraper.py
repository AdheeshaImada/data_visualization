"""Shared utilities for exploring results on the DLB website.

Selectors may change when the third-party website is redesigned. No Selenium
browser or guessing of lottery results is required for these basic examples.
"""
import requests
from bs4 import BeautifulSoup

URL = "https://www.dlb.lk/result/en"


def fetch_html(url=URL, timeout=15):
    response = requests.get(url, timeout=timeout, headers={
        "User-Agent": "Mozilla/5.0 (compatible; learning-project/1.0)"
    })
    response.raise_for_status()
    return response.text


def extract_result_groups(html):
    """Find result number lists, or return [] if the site's markup differs."""
    soup = BeautifulSoup(html, "html.parser")
    groups = []
    # Existing DLB examples used these HTML classes; keep selectors isolated.
    for node in soup.select("ul.res_allnumber"):
        text = " ".join(node.stripped_strings)
        if text:
            groups.append(text)
    return groups


def print_groups(groups):
    if not groups:
        print("No result groups matched the expected HTML. The website layout may have changed.")
        print(f"Please check {URL} directly instead of relying on an unverified extraction.")
        return
    for index, group in enumerate(groups, start=1):
        print(f"Result group {index}: {group}")
