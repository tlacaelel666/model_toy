"""Quantum operators for the toy model"""

import numpy as np

PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PI = np.pi

def crear_operador_O():
    """
    Construye la matriz del operador Ô a partir de su definición formal.
    
    λ_n = cos(πn) * cos(πφn)
    
    Returns:
        np.ndarray: 2x2 matrix with eigenvalues for n=0 and n=1
    """
    # Para n = 0
    P_0 = np.cos(PI * 0)           # Componente de Paridad
    Q_0 = np.cos(PI * PHI * 0)     # Componente Cuasiperiódico
    lambda_0 = P_0 * Q_0

    # Para n = 1
    P_1 = np.cos(PI * 1)           # Componente de Paridad
    Q_1 = np.cos(PI * PHI * 1)     # Componente Cuasiperiódico
    lambda_1 = P_1 * Q_1

    # Matriz diagonal con autovalores
    O_matrix = np.array([
        [lambda_0, 0],
        [0, lambda_1]
    ])

    return O_matrix

def operador_O_aplicado(psi_superposicion, O_matrix):
    """
    Aplica el operador Ô a un estado de superposición.
    
    Args:
        psi_superposicion: np.ndarray - estado |ψ⟩ = 1/√2 * |0⟩ + 1/√2 * |1⟩
        O_matrix: np.ndarray - matriz del operador Ô
        
    Returns:
        tuple: (amplitud_0, amplitud_1, prob_0, prob_1)
    """
    resultado = O_matrix @ psi_superposicion
    
    prob_0 = np.abs(resultado[0][0])**2
    prob_1 = np.abs(resultado[1][0])**2
    
    # Normalizar probabilidades
    total_prob = prob_0 + prob_1
    prob_0 /= (total_prob + 1e-10)
    prob_1 /= (total_prob + 1e-10)
    
    return resultado[0][0], resultado[1][0], prob_0, prob_1

def obtener_estado_medido(prob_0, prob_1):
    """
    Simula la medición colapsando a |0⟩ o |1⟩ basado en probabilidades.
    
    Args:
        prob_0: float - probabilidad de medir |0⟩
        prob_1: float - probabilidad de medir |1⟩
        
    Returns:
        int: 0 o 1 (el estado medido)
    """
    return np.random.choice([0, 1], p=[prob_0, prob_1])

def calcular_propiedades_O():
    """
    Calcula y retorna propiedades del operador Ô para documentación.
    
    Returns:
        dict: propiedades del operador
    """
    O = crear_operador_O()
    
    return {
        'matriz': O,
        'lambda_0': O[0, 0],
        'lambda_1': O[1, 1],
        'traza': np.trace(O),
        'determinante': np.linalg.det(O),
        'autovalores': np.linalg.eigvals(O),
        'phi': PHI,
        'descripcion': 'Ô_n = cos(πn) * cos(πφn)'
    }

if __name__ == "__main__":
    # Test: mostrar propiedades del operador
    props = calcular_propiedades_O()
    print("\nOperador Ô - Propiedades:")
    print(f"  λ_0 = cos(0) * cos(0) = {props['lambda_0']:.4f}")
    print(f"  λ_1 = cos(π) * cos(πφ) = {props['lambda_1']:.4f}")
    print(f"  Traza = {props['traza']:.4f}")
    print(f"  Determinante = {props['determinante']:.4f}")
