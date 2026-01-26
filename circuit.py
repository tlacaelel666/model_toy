from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute
from qiskit.visualization import plot_histogram

def circuito_maestro_original():
    # -----------------------------------------------------
    # 1. Arquitectura: 3 Qubits (Ser) + 2 Ancillas (Hacer)
    # -----------------------------------------------------
    q_sys = QuantumRegister(3, name='q_sys')
    q_anc = QuantumRegister(2, name='ancilla')
    c_out = ClassicalRegister(2, name='lectura')
    
    qc = QuantumCircuit(q_sys, q_anc, c_out)

    # -----------------------------------------------------
    # 2. Inicialización de Ancillas (Sensor Activo)
    # -----------------------------------------------------
    # Las ancillas deben estar en superposición para actuar como
    # controles cuánticos sin colapsar el sistema prematuramente.
    qc.h(q_anc)
    
    qc.barrier()

    # -----------------------------------------------------
    # 3. EL NÚCLEO (Tu intuición original)
    # -----------------------------------------------------
    # "No hace nada en 000, pero si mueve si Q1 está activo"
    
    # Si Q1=0 (y Anc=0/1), la puerta NO se dispara. Q0 queda intacto.
    # Si Q1=1, la puerta SE dispara y Q0 cambia (se entrelaza con Ancilla).
    qc.ccx(q_anc[0], q_sys[1], q_sys[0])
    
    # Conexión secundaria para cerrar el circuito de información
    # (Q0 y Q2 informan a la segunda ancilla)
    qc.cx(q_sys[0], q_anc[1])
    qc.cx(q_sys[2], q_anc[1])

    qc.barrier()

    # -----------------------------------------------------
    # 4. Cierre y Lectura
    # -----------------------------------------------------
    # Cerramos la superposición para leer el resultado del "latido"
    qc.h(q_anc)
    
    # Solo medimos las ancillas. El sistema sigue vivo.
    qc.measure(q_anc, c_out)

    return qc
# 1. Elegimos el simulador (la "máquina de disparos")
simulador = Aer.get_backend('qasm_simulator')

# 2. Ejecutamos el experimento (Shots = repeticiones)
# Es como lanzar los dados 1024 veces para ver si están cargados
job = execute(qc, simulador, shots=1024)

# 3. Obtenemos los conteos brutos
result = job.result()
counts = result.get_counts(qc)

print("Conteos Brutos:", counts)

# 4. Calculamos la Probabilidad (Matemática simple)
total_shots = 1024
for estado, cantidad in counts.items():
    probabilidad = (cantidad / total_shots) * 100
    print(f"Estado Ancilla {estado}: {probabilidad}%")
# Generar y validar visualmente
qc = circuito_maestro_original()
print("--- El Circuito Validador (Tu Diseño Original) ---")
print(qc.draw(output='text'))