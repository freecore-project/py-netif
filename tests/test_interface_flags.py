from netif import InterfaceFlags


def test_renaming_interface_flag_matches_freebsd_abi():
    assert InterfaceFlags.RENAMING.value == 0x400000
    assert InterfaceFlags(0x400000) is InterfaceFlags.RENAMING
