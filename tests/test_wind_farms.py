import pytest
from pathlib import Path

from source.wind_farms import WindFarms


@pytest.fixture
def empty_farms():
    return WindFarms()


@pytest.fixture
def two_farms(empty_farms):
    empty_farms.add({
        'Name': 'DanTysk',
        'Country': 'Germany',
        'Commissioning Year': 2014,
        'Capacity MW': 288
    })
    empty_farms.add({
        'Name': 'Horns Rev 3',
        'Country': 'Denmark',
        'Commissioning Year': 2019,
        'Capacity MW': 407
    })
    return empty_farms


def test_properties(empty_farms):
    assert empty_farms.count == 0
    assert 'Country' in empty_farms.parameter


def test_add_first_farm(empty_farms):
    empty_farms.add({
        'Name': 'DanTysk',
        'Country': 'Germany',
        'Commissioning Year': 2014,
        'Capacity MW': 288
    })
    assert empty_farms.count == 1


def test_get_farm_parameter(two_farms):
    assert two_farms.get_parameter(
        'DanTysk', 'Capacity MW') == 288
    assert two_farms.get_parameter(
        'DanTysk', 'Annual Production GWh') is None


def test_add_new_farm(two_farms):
    two_farms.add({
        'Name': 'Hollandse Kust Zuid',
        'Country': 'Netherlands',
        'Commissioning Year': 2023,
        'Capacity MW': 760
    })
    assert two_farms.count == 3


def test_add_existing_farm(two_farms):
    with pytest.raises(ValueError):
        two_farms.add({
            'Name': 'Horns Rev 3',
            'Country': 'Denmark',
            'Commissioning Year': 2019,
            'Capacity MW': 407
        })


def test_update_existing_farm(two_farms):
    two_farms.update({
        'Name': 'DanTysk',
        'Annual Production GWh': 600
    })
    assert two_farms.count == 2
    assert two_farms.get_parameter(
        'DanTysk', 'Capacity MW') == 288
    assert two_farms.get_parameter(
        'DanTysk', 'Annual Production GWh') == 600


def test_update_unknown_farm(two_farms):
    with pytest.raises(ValueError):
        two_farms.update({
            'Name': 'Aberdeen Bay',
            'Annual Production GWh': 600
        })


def test_remove_existing_farm(two_farms):
    two_farms.remove('Horns Rev 3')
    assert two_farms.count == 1


def test_remove_unknown_farm(two_farms):
    with pytest.raises(ValueError):
        two_farms.remove('Aberdeen Bay')


def test_to_csv(two_farms, tmpdir):
    # build-in pytest fixture tmpdir
    filename = Path(tmpdir, 'WindFarms.csv')
    two_farms.to_csv(filename)
    assert filename.exists()


def test_forcast_production(two_farms, monkeypatch):
    # build-in pytest fixture monkeypatch
    def mock_flh(country, year):
        return 2000
    monkeypatch.setattr(
        'source.wind_farms.magic_full_load_hours', mock_flh)
    two_farms.forecast_production()
    assert two_farms.get_parameter(
        'DanTysk', 'Annual Production GWh') == 576
    assert two_farms.get_parameter(
        'Horns Rev 3', 'Annual Production GWh') == 814
