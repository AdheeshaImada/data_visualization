"""Alternative DLB result inspection using the shared robust parser."""
import requests
from dlb_scraper import URL, extract_result_groups, fetch_html, print_groups


def main():
    try:
        html = fetch_html()
    except requests.RequestException as exc:
        print(f"Unable to retrieve {URL}: {exc}")
        return
    print_groups(extract_result_groups(html))


if __name__ == "__main__":
    main()
