import pytest
from pathlib import Path

from source.wind_farms import WindFarms


def test_properties():
    farms = WindFarms()
    assert farms.count == 0
    assert 'Country' in farms.parameter


def test_add_first_farm():
    farms = WindFarms()
    farms.add({
        'Name': 'DanTysk',
        'Country': 'Germany',
        'Commissioning Year': 2014,
        'Capacity MW': 288
    })
    assert farms.count == 1


# user defined fixture:
@pytest.fixture
def two_farms():
    farms = WindFarms()
    farms.add({
        'Name': 'DanTysk',
        'Country': 'Germany',
        'Commissioning Year': 2014,
        'Capacity MW': 288
    })
    farms.add({
        'Name': 'Horns Rev 3',
        'Country': 'Denmark',
        'Commissioning Year': 2019,
        'Capacity MW': 407
    })
    return farms


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


# showcase build-in pytest fixture `tmpdir`
def test_to_csv(two_farms, tmpdir):
    filename = Path(tmpdir, 'WindFarms.csv')
    two_farms.to_csv(filename)
    assert filename.exists()


def test_to_csv_missing_parameter(two_farms, tmpdir):
    filename = Path(tmpdir, 'WindFarms.csv')
    two_farms.add({
        'Name': 'Hollandse Kust Zuid',
        'Capacity MW': 760
    })
    assert not two_farms.get_parameter(
        'Hollandse Kust Zuid', 'Country')
    two_farms.to_csv(filename)
    assert filename.exists()


# showcase build-in pytest fixture monkeypatch
def test_forcast_production(two_farms, monkeypatch):
    def mock_flh(country, year):
        return 2000
    monkeypatch.setattr(
        'source.wind_farms.magic_full_load_hours', mock_flh)
    two_farms.forecast_production()
    assert two_farms.get_parameter(
        'DanTysk', 'Annual Production GWh') == 576
    assert two_farms.get_parameter(
        'Horns Rev 3', 'Annual Production GWh') == 814
