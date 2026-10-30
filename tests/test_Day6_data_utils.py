import numpy as np

from congestion.Day6_data_utils import build_metadata, label_stats, parse_sample_name


def test_parse_regular_name():
    d = parse_sample_name("4489-RISCY-FPU-a-1-c20-u0.85-m4-p1-f0")
    assert d["design"] == "RISCY-FPU-a"
    assert d["sample_id"] == 4489
    assert d["util"] == 0.85
    assert d["macros"] == 4


def test_parse_name_with_extension_and_none_macros():
    d = parse_sample_name("2275-RISCY-b-1-c5-u0.7-mNone-p1-f0.npy")
    assert d["design"] == "RISCY-b"
    assert d["macros"] is None


def test_bad_name_returns_none_and_is_reported():
    table, failed = build_metadata(["1-RISCY-a-1-c2-u0.7-m1-p1-f0", "not-a-sample"])
    assert len(table) == 1
    assert failed == ["not-a-sample"]


def test_label_stats():
    a = np.array([[0.0, 1.0], [2.0, 0.5]])
    s = label_stats(a)
    assert s["max"] == 2.0
    assert s["frac_gt1"] == 0.25
    assert s["frac_eq1"] == 0.25
