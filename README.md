# Python Data Visualization — Fixed & Cleaned

A collection of Python learning exercises that explore **Matplotlib**, **Plotly**, **random walks**, **dice simulations**, and **weather data visualization**. It also includes separate experimental web-scraping examples for the Development Lotteries Board (DLB) website.

This version preserves the original set of exercises while fixing incorrect CSV column references, broken input handling, unnecessarily brittle paths, and obsolete project files.

## Quick start

**Windows PowerShell (from this project folder):**

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe sitka_highs.py
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python sitka_highs.py
```

For other examples, replace `sitka_highs.py` with the desired script.

## Examples

| File | Description | Output |
| --- | --- | --- |
| `mpl_squares.py` | Simple line graph of squared values | Matplotlib window |
| `scatter_squares.py` | Three scatter plot styles of squared values | Matplotlib windows |
| `random_walk.py` + `rw_visual.py` | Random walk plot or scatter visualization | Matplotlib window |
| `die.py` + `die_visual.py` | Roll one six-sided die 1,000 times | `outputs/d6.html` |
| `dice_visual.py` | Roll two configurable dice | `outputs/d*_d*.html` |
| `dice_visual_2.py` | Roll 1–10 dice and choose bar or pie chart | `outputs/*.html` |
| `sitka_highs.py` | Sitka daily highs in July or for 2021 | Matplotlib window |
| `sitka_highs_lows.py` | Sitka daily highs and lows in 2021 | Matplotlib window |
| `death_vally.py` / `death_valley.py` | Death Valley highs and lows in 2021 | Matplotlib window |
| `lottery_scraping.py` | Explore visible results from the DLB web page | Terminal text |
| `ltry_res_scrap.py` | Alternative DLB HTML parsing exercise | Terminal text |
| `test.py` | Optional Selenium example for DLB | Terminal text |

**Sample commands:**

```powershell
.\.venv\Scripts\python.exe die_visual.py
.\.venv\Scripts\python.exe dice_visual_2.py
.\.venv\Scripts\python.exe rw_visual.py
.\.venv\Scripts\python.exe death_valley.py
```

Open the generated dice `.html` files in your browser. They contain Plotly JavaScript and will work offline.

## Weather datasets

The `data/` folder includes the original 2021 CSV files:

- `sitka_weather_07-2021_simple.csv`
- `sitka_weather_2021_simple.csv`
- `death_valley_2021_simple.csv`

`weather_data.py` reads columns by name (`DATE`, `TMAX`, `TMIN`) and safely skips rows that lack required temperatures. The two station datasets have different column ordering, so this is important.

## Web-scraping limitations

The DLB scripts are **learning exercises**, not a guaranteed or authoritative lottery-results service. They require an internet connection; their selectors are based on older markup and may fail when the live website changes. If no matching elements are found, scripts now explain the problem instead of crashing or fabricating numbers. Verify any official results directly at https://www.dlb.lk/result/en.

To try the optional Selenium example, install the extra dependency and have a supported Chrome browser available:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-selenium.txt
.\.venv\Scripts\python.exe test.py
```

## Testing

Install pytest, then run the offline checks:

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest -q
```

The automated checks do not require a browser or an internet connection.

## Project cleanup

The original archive included a Windows Python 3.9 `venv/`, IDE settings, npm `node_modules`, and large generated HTML charts. Those are *not* part of this clean source release. Recreate the virtual environment locally, and regenerate HTML outputs by running the Plotly scripts. Python dependencies belong in `requirements.txt`, not in `package.json`.

## Technology stack

Python · Matplotlib · Plotly · CSV · BeautifulSoup · Requests · optional Selenium

## Author

[AdheeshaImada](https://github.com/AdheeshaImada) · [Personal portfolio](https://adheeshaimada.github.io/portfolio-website/)
