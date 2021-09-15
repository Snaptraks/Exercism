def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int
    :param neutrons_emitted: int
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    temperature_less_800 = temperature < 800
    neutrons_more_500 = neutrons_emitted > 500
    temperature_neutron_product = temperature * neutrons_emitted < 500_000

    return (temperature_less_800
            and neutrons_more_500
            and temperature_neutron_product)


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int
    :param current: int
    :param theoretical_max_power: int
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    print(efficiency)

    if 80 <= efficiency:
        return "green"

    elif 60 <= efficiency < 80:
        return "orange"

    elif 30 <= efficiency < 60:
        return "red"

    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return safety range.

    :param temperature:
    :param neutrons_produced_per_second:
    :param threshold:
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    """

    temperature_neutron_product = temperature * neutrons_produced_per_second

    if temperature_neutron_product < 0.4 * threshold:
        return "LOW"

    elif 0.9 * threshold <= temperature_neutron_product <= 1.1 * threshold:
        return "NORMAL"

    else:
        return "DANGER"
