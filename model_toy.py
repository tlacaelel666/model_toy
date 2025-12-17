"""Terminal-based interactive toy model with Ô operator"""

import random
import numpy as np
from operators import PHI, crear_operador_O, operador_O_aplicado, obtener_estado_medido

# Constants
GOLDEN_PHASE_ACCUMULATOR = 0.0
SEEN_STATES = set()
QUBITS = {
    'qubit_1': {'q0': 1, 'q1': 6, 'name': 'a|y'},
    'qubit_2': {'q0': 2, 'q1': 5, 'name': 'b|e'},
    'qubit_3': {'q0': 3, 'q1': 4, 'name': 'c|d'}
}

BRIDGE = [1, 2, 3, 4, 5, 6]
STATE_NAMES = {0: 'h', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'y'}

# Crear operador Ô una sola vez
OPERADOR_O = crear_operador_O()

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

def measure_system_with_operator():
    """
    Simulates quantum measurement using Ô operator.
    
    1. Start with superposition |ψ⟩ = 1/√2 * |0⟩ + 1/√2 * |1⟩
    2. Apply Ô operator
    3. Get collapse probabilities
    4. Measure and map to toy model states
    """
    # Estado inicial de superposición
    ket_0 = np.array([[1], [0]])
    ket_1 = np.array([[0], [1]])
    psi_superposicion = (1 / np.sqrt(2)) * ket_0 + (1 / np.sqrt(2)) * ket_1
    
    # Aplicar operador Ô
    _, _, prob_0, prob_1 = operador_O_aplicado(psi_superposicion, OPERADOR_O)
    
    # Obtener estado medido
    measured_binary = obtener_estado_medido(prob_0, prob_1)
    
    # Elegir qubit aleatorio para medir
    qubit_to_measure = random.choice(list(QUBITS.keys()))
    qubit_data = QUBITS[qubit_to_measure]
    
    # Mapear resultado binario a estado del toy model
    measured_state = qubit_data['q1'] if measured_binary == 1 else qubit_data['q0']
    hidden_state = get_complementary_state(measured_state)
    qubit_name, binary_value, pair = identify_qubit(measured_state)
    
    return {
        'measured': measured_state,
        'hidden': hidden_state,
        'qubit': qubit_name,
        'value': binary_value,
        'pair': pair,
        'prob_0': prob_0,
        'prob_1': prob_1,
        'measured_binary': measured_binary
    }

def display_measurement(result):
    """Pretty print measurement result with operator info"""
    print(f"\n{'='*50}")
    print(f"  QUANTUM MEASUREMENT (Operator Ô)")
    print(f"{'='*50}\n")
    print(f"Operator Ô applied to superposition |ψ⟩")
    print(f"  P(|0⟩) = {result['prob_0']:.4f}")
    print(f"  P(|1⟩) = {result['prob_1']:.4f}")
    print(f"  → Collapsed to: |{result['measured_binary']}⟩\n")
    print(f"Qubit measured: {result['qubit']}")
    print(f"State: {STATE_NAMES[result['measured']]} (value={int(result['value'])})")
    print(f"Hidden state: {STATE_NAMES[result['hidden']]}")
    print(f"H = {result['measured']} + {result['hidden']} = 7")
    print()

def main():
    print("\n" + "="*50)
    print("  QUANTUM TOY MODEL - Interactive")
    print("="*50)
    print("\nInitial state: 3 qubits in superposition |ψ⟩")
    print("Sum of all states: 1+2+3+4+5+6 = 21")
    print("Operator Ô: cos(πn) * cos(πφn)\n")

    while True:
        user_input = input("Press ENTER to measure (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        result = measure_system_with_operator()
        display_measurement(result)

        # --- Golden Phase Accumulator Logic ---
        global GOLDEN_PHASE_ACCUMULATOR, SEEN_STATES

        measured_state = result['measured']

        # Calculate the golden phase for the measured state n
        golden_phase = np.cos(np.pi * PHI * measured_state)

        if measured_state in SEEN_STATES:
            # If the state has been seen before, it's cancelled (subtracted)
            GOLDEN_PHASE_ACCUMULATOR -= golden_phase
            SEEN_STATES.remove(measured_state)
            print(f"State {measured_state} seen before. CANCELLING phase.")
        else:
            # If it's a new state, it's accumulated (added)
            GOLDEN_PHASE_ACCUMULATOR += golden_phase
            SEEN_STATES.add(measured_state)
            print(f"New state {measured_state} measured. ACCUMULATING phase.")

        # --- Display Accumulator ---
        print(f"Golden Phase Accumulator: {GOLDEN_PHASE_ACCUMULATOR:.4f}")

        # Simple progress bar visualization
        # The accumulator can range from approx -1.4 to +1.4
        progress = int((GOLDEN_PHASE_ACCUMULATOR + 1.5) / 3.0 * 50)
        progress = max(0, min(50, progress)) # Ensure it's within bounds

        bar = "[" + "=" * progress + " " * (50 - progress) + "]"
        print(f"Accumulator Bar: {bar}\n")

if __name__ == "__main__":
    main()
