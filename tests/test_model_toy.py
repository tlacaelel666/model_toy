import pytest
from model_toy import (
    get_complementary_state, identify_qubit, measure_system
)

def test_complementary_states_are_correct():
    assert get_complementary_state(1) == 6  # a ↔ y
    assert get_complementary_state(2) == 5  # b ↔ e
    assert get_complementary_state(3) == 4  # c ↔ d

def test_complementary_sum_to_seven():
    for state in [1, 2, 3, 4, 5, 6]:
        comp = get_complementary_state(state)
        assert state + comp == 7

def test_identify_qubit_works():
    assert identify_qubit(1)[0] == 'qubit_1'
    assert identify_qubit(2)[0] == 'qubit_2'
    assert identify_qubit(4)[0] == 'qubit_3'

def test_measure_returns_valid_structure():
    result = measure_system()
    assert 'measured' in result
    assert 'hidden' in result
    assert result['measured'] + result['hidden'] == 7

# Run: pytest tests/
