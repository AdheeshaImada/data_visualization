"""Offline tests for simulations, parsing, and included weather records."""
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from die import Die
from dice_utils import simulate
from random_walk import RandomWalk
from weather_data import DATA_DIR, load_temperatures
from dlb_scraper import extract_result_groups


def test_die_results_within_bounds():
    die = Die(8)
    assert all(1 <= die.roll() <= 8 for _ in range(200))
    with pytest.raises(ValueError):
        Die(0)


def test_dice_frequencies_sum_to_roll_count():
    totals, frequencies = simulate([Die(6), Die(8)], 500)
    assert totals[0] == 2 and totals[-1] == 14
    assert sum(frequencies) == 500


def test_simulation_rejects_empty_dice():
    with pytest.raises(ValueError):
        simulate([], 100)
    with pytest.raises(ValueError):
        simulate([Die()], 0)


def test_random_walk_length_and_origin():
    rw = RandomWalk(300)
    rw.fill_walk()
    assert len(rw.x_val) == len(rw.y_val) == 300
    assert rw.x_val[0] == rw.y_val[0] == 0
    rw.fill_walk()
    assert len(rw.x_val) == 300
    with pytest.raises(ValueError):
        RandomWalk(0)


def test_sitka_july_reads_correct_tmax_column():
    dates, highs = load_temperatures(DATA_DIR / "sitka_weather_07-2021_simple.csv")
    assert dates[0].strftime("%Y-%m-%d") == "2021-07-01"
    assert highs[0] == 61
    assert len(dates) == 31


def test_sitka_yearly_uses_sitka_file():
    dates, highs, lows = load_temperatures(DATA_DIR / "sitka_weather_2021_simple.csv", include_lows=True)
    assert len(dates) >= 360
    assert highs[0] == 44 and lows[0] == 40


def test_death_valley_reads_named_columns():
    dates, highs, lows = load_temperatures(DATA_DIR / "death_valley_2021_simple.csv", include_lows=True)
    assert dates[0].strftime("%Y-%m-%d") == "2021-01-01"
    assert highs[0] == 71 and lows[0] == 51


def test_missing_temperature_rows_are_skipped(tmp_path):
    source = tmp_path / "broken.csv"
    source.write_text("DATE,TMAX,TMIN\n2021-01-01,50,30\n2021-01-02,,25\n2021-01-03,60,40\n", encoding="utf-8")
    dates, highs, lows = load_temperatures(source, include_lows=True)
    assert len(dates) == 2 and highs == [50, 60] and lows == [30, 40]


def test_dlb_parser_when_expected_markup_is_present():
    sample = "<html><ul class='res_allnumber'><li>N</li><li>27</li><li>56</li></ul></html>"
    assert extract_result_groups(sample) == ["N 27 56"]
    assert extract_result_groups("<html><p>changed layout</p></html>") == []
