import pytest

from netif import InterfaceCapability, bitmask_to_set


def test_bitmask_to_set_decodes_bit_31_as_unsigned():
    # IFCAP_TXTLS_RTLMT (0x80000000) has no InterfaceCapability member and is skipped
    n = 0x80000000 | InterfaceCapability.RXCSUM | InterfaceCapability.HWSTATS
    assert bitmask_to_set(n, InterfaceCapability) == {InterfaceCapability.RXCSUM, InterfaceCapability.HWSTATS}


def test_bitmask_to_set_rejects_negative_bitmask():
    # A C int with bit 31 set arrives as a negative Python int; this used to loop forever
    with pytest.raises(ValueError):
        bitmask_to_set(-0x80000000, InterfaceCapability)
