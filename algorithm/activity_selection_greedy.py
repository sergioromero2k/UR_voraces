#!/usr/bin/env python3

"""
def actividad_greedy(inicio, fin):
    # Create a list of activities using enumerate and zip
    actividades = list(enumerate(zip(inicio, fin)))

    # Sort by completion time
    actividades.sort(key=lambda x: x[1][1])

    seleccionadas = []
    ultima_fin = -1

    for indice, (start, end) in actividades:
        if start >= ultima_fin:
            seleccionadas.append(indice)
            ultima_fin = end

    return seleccionadas
"""

def activity_greedy(start, end) -> list:
    activity = list(zip(start, end, range(len(end))))
    
    print(activity)
    activity.sort(key=lambda x:x[1], reverse=False)
    print(activity)

    selection = []
    last_end = -1

    for a in activity:
        if a[0] >= last_end:
            selection.append(a[2])
            last_end = a[1]
        
    return selection

def main() -> None:
    start = [1, 3, 0, 5, 8, 5]
    end = [9, 4, 6, 7, 1, 2]
    
    result = activity_greedy(start, end)
    print(result)
    
if __name__ == "__main__":
    main()
