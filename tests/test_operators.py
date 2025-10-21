# Agrega esto a tests/test_model_toy.py

def test_operator_O_exists():
    """Test that Ô operator can be created"""
    from operators import crear_operador_O
    O = crear_operador_O()
    assert O.shape == (2, 2)

def test_operator_eigenvalues():
    """Test that Ô eigenvalues are correct"""
    from operators import crear_operador_O
    import numpy as np
    O = crear_operador_O()
    
    # λ_0 = cos(0) * cos(0) = 1
    assert np.isclose(O[0, 0], 1.0)
    
    # λ_1 = cos(π) * cos(πφ) = -1 * cos(πφ)
    phi = (1 + np.sqrt(5)) / 2
    expected_lambda_1 = -1 * np.cos(np.pi * phi)
    assert np.isclose(O[1, 1], expected_lambda_1)

def test_operator_applied_returns_probabilities():
    """Test probability calculation"""
    from operators import crear_operador_O, operador_O_aplicado
    import numpy as np
    
    O = crear_operador_O()
    ket_0 = np.array([[1], [0]])
    ket_1 = np.array([[0], [1]])
    psi = (1 / np.sqrt(2)) * ket_0 + (1 / np.sqrt(2)) * ket_1
    
    _, _, prob_0, prob_1 = operador_O_aplicado(psi, O)
    
    # Probabilidades deben sumar a 1
    assert np.isclose(prob_0 + prob_1, 1.0)
