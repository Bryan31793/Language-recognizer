import tkinter as tk

# ==== Variables globales ====
root = tk.Tk()
root.title("Simulación de autómata")

cola = []
boxes = []
i_global = 0

entry = tk.Entry(root, font=("Arial", 16), width=40)
entry.pack(pady=10)

canvas = tk.Canvas(root, height=100)
canvas.pack(fill="x", expand=True)

scroll_x = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
scroll_x.pack(fill="x")
canvas.configure(xscrollcommand=scroll_x.set)

content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=5)


# ==== Autómata visual ====
def actualizar_cola():
    for idx, simbolo in enumerate(cola):
        boxes[idx].config(text=simbolo)
        if simbolo == "Ø":
            boxes[idx].config(bg="lightgray")
        else:
            boxes[idx].config(bg="white")

def resaltar(idx):
    if 0 <= idx < len(boxes):
        boxes[idx].config(bg="lightblue")
        canvas.xview_moveto(max(0, (idx - 2) / len(boxes)))

def estado_0():
    actualizar_cola()
    if cola[0] == "Ø":
        root.after(500, estado_1, 1, 0)

def estado_1(i, prev):
    actualizar_cola()
    if prev != i:
        # Restaurar el anterior
        if cola[prev] == "Ø":
            boxes[prev].config(bg="lightgray")
        else:
            boxes[prev].config(bg="white")
    resaltar(i)

    if cola[i] == "a":
        cola[i] = "Ø"
        actualizar_cola()
        root.after(600, estado_2, "a", i, i)

    elif cola[i] == "b":
        cola[i] = "Ø"
        actualizar_cola()
        root.after(600, estado_2, "b", i, i)

    elif cola[i] == "c":
        cola[i] = "Ø"
        actualizar_cola()
        status_label.config(text="Cadena correcta", fg="green")
    else:
        status_label.config(text="Cadena inválida", fg="red")

def estado_2(caracter, i, prev):
    j = i
    def avanzar():
        nonlocal j, prev
        actualizar_cola()
        if prev != j:
            if cola[prev] == "Ø":
                boxes[prev].config(bg="lightgray")
            else:
                boxes[prev].config(bg="white")
        resaltar(j)
        prev = j

        if cola[j + 1] != "Ø":
            j += 1
            root.after(500, avanzar)
        else:
            if cola[j] == caracter:
                cola[j] = "Ø"
                actualizar_cola()
                root.after(500, estado_3, j, j)
            else:
                status_label.config(text="Cadena inválida", fg="red")
    avanzar()

def estado_3(j, prev):
    i = j
    def retroceder():
        nonlocal i, prev
        actualizar_cola()
        if prev != i:
            if cola[prev] == "Ø":
                boxes[prev].config(bg="lightgray")
            else:
                boxes[prev].config(bg="white")
        resaltar(i)
        prev = i

        if cola[i - 1] != "Ø":
            i -= 1
            root.after(500, retroceder)
        else:
            root.after(500, estado_1, i, i)
    retroceder()

# ==== Función de inicio ====
def iniciar_analisis():
    global cola, boxes
    cola = ["Ø"]
    boxes.clear()
    for widget in content_frame.winfo_children():
        widget.destroy()
    status_label.config(text="")

    cadena = entry.get()
    for c in cadena:
        cola.append(c)
    cola.append("Ø")

    for idx, c in enumerate(cola):
        lbl = tk.Label(content_frame, text=c, font=("Arial", 20), width=3, height=2,
                       borderwidth=2, relief="solid", bg="white")
        lbl.grid(row=0, column=idx, padx=0)
        boxes.append(lbl)

    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.after(500, estado_0)

btn = tk.Button(root, text="Analizar", command=iniciar_analisis)
btn.pack(pady=10)

root.mainloop()
