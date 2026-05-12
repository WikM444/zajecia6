import pytest

from src.manager import Manager
from src.models import Parameters

def test_check_total_sum():
    parameters = Parameters()
    manager = Manager(parameters)

    #manager.create_tenants_settlements()

    settlement = manager.get_settlement('apart-polanka', 2026, 6)
    rozliczenie = manager.get_apartment_costs('apart-polanka', 2026, 6)

    assert settlement.total_due_pln == rozliczenie



