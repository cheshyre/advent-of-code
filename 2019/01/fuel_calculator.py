"""Module to calculate fuel needs."""

__all__ = ["get_fuel_needed", "get_fuel_needed_complete"]


def get_fuel_needed(mass: int) -> int:
    """Calculate fuel needed to launch mass."""
    return mass // 3 - 2


def get_fuel_needed_complete(mass: int) -> int:
    """Calculate fuel needed to launch mass and fuel itself."""
    fuel_needed = get_fuel_needed(mass)
    additional_fuel_needed = get_fuel_needed(fuel_needed)
    while additional_fuel_needed > 0:
        fuel_needed += additional_fuel_needed
        additional_fuel_needed = get_fuel_needed(additional_fuel_needed)
    return fuel_needed
