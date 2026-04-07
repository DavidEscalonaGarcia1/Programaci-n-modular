import time
import os

fps = float(input("Introduce los FPS: "))
delay = 1 / fps

movimientos = {
    'L': -1,
    'R': 1,
    'U': -3,
    'D': 3    
}

frames = [
    [['#','X','X'], ['X','O','X'], ['X','X','X']],  # 0
    [['X','#','X'], ['X','O','X'], ['X','X','X']],  # 1
    [['X','X','#'], ['X','O','X'], ['X','X','X']],  # 2
    [['X','X','X'], ['X','O','#'], ['X','X','X']],  # 3
    [['X','X','X'], ['X','O','X'], ['X','X','#']],  # 4
    [['X','X','X'], ['X','O','X'], ['X','#','X']],  # 5
    [['X','X','X'], ['X','O','X'], ['#','X','X']],  # 6
    [['X','X','X'], ['#','O','X'], ['X','X','X']]   # 7
]

secuencia = input("Introduce la secuencia de movimientos (L, R, U, D): ").upper()

pos = 0

def movimiento_valido(pos_actual, mov):
    nuevo_pos = pos_actual + movimientos[mov]
    if mov == 'L':
        if pos_actual % 3 == 0:
            return False
    if mov == 'R':
        if pos_actual % 3 == 2:
            return False
    if mov == 'U':
        if pos_actual &lt; 3:
            return False
    if mov == 'D':
        if pos_actual &gt; 4:
            return False
    if 0 &lt;= nuevo_pos &lt; len(frames):
        return True
    return False

ruta = [pos]

for mov in secuencia:
    if mov in movimientos and movimiento_valido(pos, mov):
        pos += movimientos[mov]
        ruta.append(pos)
    else:
        print(f"Movimiento '{mov}' inválido desde posición {pos+1}, se descarta.")

renderizados = []
for idx in ruta:
    lineas = []
    for fila in frames[idx]:
        lineas.append(" ".join(fila))
    renderizados.append(lineas)

while True:
    for frame in renderizados:
        os.system('clear')
        for linea in frame:
            print(linea)
        time.sleep(delay)