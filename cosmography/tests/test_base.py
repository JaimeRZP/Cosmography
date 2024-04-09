import cosmography as CG


def tests():
    # sixdf
    Sixdf = CG.Sixdf()
    assert Sixdf.z is not None
    assert Sixdf.data is not None
    assert Sixdf.cov is not None

    # BOSS
    BOSS = CG.BOSSDR12()
    assert BOSS.z is not None
    assert BOSS.data is not None
    assert BOSS.cov is not None

    # CC
    CC = CG.CC()
    assert CC.z is not None
    assert CC.data is not None
    assert CC.cov is not None

    # CMB
    CMB = CG.CMB()
    assert CMB.z is not None
    assert CMB.data is not None
    assert CMB.cov is not None

    # DSS
    DSS = CG.DSS()
    assert DSS.z is not None
    assert DSS.data is not None
    assert DSS.cov is not None

    # eBOSS
    eBOSS = CG.eBOSSDR16()
    assert eBOSS.z is not None
    assert eBOSS.data is not None
    assert eBOSS.cov is not None

    # FastSound
    FastSound = CG.FastSound()
    assert FastSound.z is not None
    assert FastSound.data is not None
    assert FastSound.cov is not None

    # PantheonDS17
    PantheonDS17 = CG.PantheonDS17(path='data/PantheonDS17/')
    assert PantheonDS17.z is not None
    assert PantheonDS17.data is not None
    assert PantheonDS17.cov is not None

    # Vipers
    Vipers = CG.Vipers()
    assert Vipers.z is not None
    assert Vipers.data is not None
    assert Vipers.cov is not None

    # Wigglez
    Wigglez = CG.Wigglez()
    assert Wigglez.z is not None
    assert Wigglez.data is not None
    assert Wigglez.cov is not None
