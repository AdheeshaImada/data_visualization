"""Simple DLB lottery result page inspection with BeautifulSoup."""
import requests
from dlb_scraper import URL, extract_result_groups, fetch_html, print_groups


def main():
    try:
        groups = extract_result_groups(fetch_html())
    except requests.RequestException as exc:
        print(f"Unable to retrieve {URL}: {exc}")
        return
    print_groups(groups)


if __name__ == "__main__":
    main()
