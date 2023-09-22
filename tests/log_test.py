import pytest
import lmParse as lp
import numpy as np


def test_empty_log():
    log = lp.Log()
    assert log.run == 0


def test_single_run_log():
    log = lp.Log("tests/single_run.log")
    assert log.run == 1
    assert log["Step"].iloc[0] == 0
    assert log["Step"].iloc[-1] == 2000000
    assert log["N"] == 445960
    assert log.N == 445960
    assert log.getN() == 445960
    refKeys = (
        "Step",
        "Temp",
        "TotEng",
        "PotEng",
        "KinEng",
        "Press",
        "Volume",
        "Lx",
        "Ly",
        "Lz",
        "Pxx",
        "Pyy",
        "Pzz",
        "Pxy",
        "Pxz",
        "Pyz",
        "Run",
    )
    assert len(refKeys) == len(log.keys())
    for rk, k in zip(sorted(refKeys), sorted(log.keys())):
        assert k == rk


def test_add_later_log():
    log = lp.Log()
    log.parseLog("tests/single_run.log")
    assert log.run == 1
    assert log["Step"].iloc[0] == 0
    assert log["Step"].iloc[-1] == 2000000
    assert log["N"] == 445960
    assert log.N == 445960
    assert log.getN() == 445960
    refKeys = (
        "Step",
        "Temp",
        "TotEng",
        "PotEng",
        "KinEng",
        "Press",
        "Volume",
        "Lx",
        "Ly",
        "Lz",
        "Pxx",
        "Pyy",
        "Pzz",
        "Pxy",
        "Pxz",
        "Pyz",
        "Run",
    )
    assert len(refKeys) == len(log.keys())
    for rk, k in zip(sorted(refKeys), sorted(log.keys())):
        assert k == rk


def test_multi_run_log():
    log = lp.Log("tests/multi_run.log")
    assert min(log["Run"]) == 0
    assert max(log["Run"]) == 9
    assert log["Step"].iloc[0] == 0
    assert log["Step"].iloc[-1] == 5769

    refKeys = (
        "Step",
        "PotEng",
        "Enthalpy",
        "Press",
        "Lx",
        "Ly",
        "Lz",
        "Volume",
        "Pxx",
        "Pyy",
        "Pzz",
        "Pxy",
        "Pxz",
        "Pyz",
        "Fmax",
        "Run",
    )
    assert len(refKeys) == len(log.keys())
    for rk, k in zip(sorted(refKeys), sorted(log.keys())):
        assert k == rk


def test_elastic_log():
    log = lp.ElasticConstantsLog("tests/elastic_run.log")

    refCMat = np.array(
        (
            (
                167.294982943099,
                124.227999477183,
                124.227999477184,
                -4.74536901975208e-14,
                7.65201534687098e-14,
                -4.81763777661888e-14,
            ),
            (
                124.227999477183,
                167.294982943098,
                124.227999477183,
                -6.8601538520345e-14,
                2.64498835334722e-14,
                -2.04852560622529e-15,
            ),
            (
                124.227999477184,
                124.227999477183,
                167.294982943098,
                -2.20422192462953e-13,
                4.13060068982008e-14,
                -1.31140090278198e-14,
            ),
            (
                -4.74536901975208e-14,
                -6.8601538520345e-14,
                -2.20422192462953e-13,
                76.4624040252973,
                -3.89081434252285e-14,
                -8.18910109161895e-14,
            ),
            (
                7.65201534687098e-14,
                2.64498835334722e-14,
                4.13060068982008e-14,
                -3.89081434252285e-14,
                76.4624040252972,
                1.02697636863157e-14,
            ),
            (
                -4.81763777661888e-14,
                -2.04852560622529e-15,
                -1.31140090278198e-14,
                -8.18910109161895e-14,
                1.02697636863157e-14,
                76.4624040252973,
            ),
        )
    )
    assert np.allclose(log.Cmat, refCMat)
