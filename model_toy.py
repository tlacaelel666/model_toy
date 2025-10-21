"""Terminal-based interactive toy model"""

import random
import numpy as np

# Constants
QUBITS = {
    'qubit_1': {'q0': 1, 'q1': 6, 'name': 'a|y'},
    'qubit_2': {'q0': 2, 'q1': 5, 'name': 'b|e'},
    'qubit_3': {'q0': 3, 'q1': 4, 'name': 'c|d'}
}

BRIDGE = [1, 2, 3, 4, 5, 6]
STATE_NAMES = {0: 'h', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'y'}

def get_complementary_state(measured_state):
    """Returns the hidden complementary state"""
    pairs = {6: 1, 1: 6, 5: 2, 2: 5, 4: 3, 3: 4}
    return pairs.get(measured_state, None)

def identify_qubit(state):
    """Identifies which qubit this state belongs to"""
    for qname, qdata in QUBITS.items():
        if state in [qdata['q0'], qdata['q1']]:
            is_one = (state == qdata['q1'])
            return qname, is_one, qdata['name']
    return None, None, None

def measure_system():
    """Simulates quantum measurement with Ô operator"""
    # Apply quantum operator to superposition
    measured_state = random.choice(BRIDGE)
    hidden_state = get_complementary_state(measured_state)
    qubit_name, binary_value, pair = identify_qubit(measured_state)

    return {
        'measured': measured_state,
        'hidden': hidden_state,
        'qubit': qubit_name,
        'value': binary_value,
        'pair': pair
    }

def display_measurement(result):
    """Pretty print measurement result"""
    print(f"\n{'='*50}")
    print(f"  QUANTUM MEASUREMENT (Operator Ô)")
    print(f"{'='*50}\n")
    print(f"Qubit measured: {result['qubit']}")
    print(f"Collapsed to: {STATE_NAMES[result['measured']]} (value={int(result['value'])})")
    print(f"Hidden state: {STATE_NAMES[result['hidden']]}")
    print(f"H = {result['measured']} + {result['hidden']} = 7")
    print()

def main():
    print("\n" + "="*50)
    print("  QUANTUM TOY MODEL - Interactive")
    print("="*50)
    print("\nInitial state: 3 qubits in superposition |ψ⟩")
    print("Sum of all states: 1+2+3+4+5+6 = 21\n")

    while True:
        user_input = input("Press ENTER to measure (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        result = measure_system()
        display_measurement(result)

if __name__ == "__main__":
    main()
