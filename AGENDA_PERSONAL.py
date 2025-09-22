import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry   # se instala con: pip install tkcalendar

# ================== FUNCIONES ==================
def actualizar_contador():
    """Actualiza la etiqueta que muestra la cantidad de eventos guardados"""
    cantidad = len(lista_eventos.get_children())
    lbl_contador.config(text=f"Eventos guardados: {cantidad}")

def agregar_evento():
    # Obtiene los datos de las entradas
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_desc.get()

    # Validación: que no estén vacíos
    if hora == "" or descripcion == "":
        messagebox.showwarning("Atención", "Debe llenar todos los campos")
        return

    # Inserta en la tabla
    lista_eventos.insert("", "end", values=(fecha, hora, descripcion))

    # Limpia las entradas de hora y descripción
    entrada_hora.delete(0, tk.END)
    entrada_desc.delete(0, tk.END)

    # Actualiza contador
    actualizar_contador()

def eliminar_evento():
    seleccionado = lista_eventos.selection()
    if not seleccionado:
        messagebox.showwarning("Error", "No ha seleccionado ningún evento")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este evento?")
    if confirmar:
        lista_eventos.delete(seleccionado)
        actualizar_contador()

# ================== VENTANA PRINCIPAL ==================
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("700x500")
ventana.configure(bg="#2F2F2F")

# Mensaje de bienvenida al abrir
messagebox.showinfo("Bienvenido", "Bienvenido a tu Agenda Personal ")

# ----- Título -----
lbl_titulo = tk.Label(ventana, text="Agenda Personal Universitaria",
                      bg="#2F2F2F", fg="white", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

# ----- Frame del formulario -----
frame_formulario = tk.Frame(ventana, bg="#2F2F2F")
frame_formulario.pack(fill="x", padx=10, pady=5)

tk.Label(frame_formulario, text="Fecha:", bg="#2F2F2F", fg="white").grid(row=0, column=0, padx=5, pady=5)
entrada_fecha = DateEntry(frame_formulario, date_pattern="dd/mm/yyyy",
                          background="#2F2F2F", foreground="white", borderwidth=2)
entrada_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_formulario, text="Hora:", bg="#2F2F2F", fg="white").grid(row=0, column=2, padx=5, pady=5)
entrada_hora = tk.Entry(frame_formulario, bg="#2F2F2F", fg="white", insertbackground="white")
entrada_hora.grid(row=0, column=3, padx=5, pady=5)
entrada_hora.config(state="normal")
entrada_hora.bind("<Button-1>", lambda e: entrada_hora.config(state="normal"))

tk.Label(frame_formulario, text="Descripción:", bg="#2F2F2F", fg="white").grid(row=1, column=0, padx=5, pady=5)
entrada_desc = tk.Entry(frame_formulario, width=50, bg="#2F2F2F", fg="white", insertbackground="white")
entrada_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entrada_desc.config(state="normal")
entrada_desc.bind("<Button-1>", lambda e: entrada_desc.config(state="normal"))

# ----- Frame de los botones -----
frame_botones = tk.Frame(ventana, bg="#2F2F2F")
frame_botones.pack(fill="x", padx=10, pady=5)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento,
                        bg="#2F2F2F", fg="white", activebackground="#444444", activeforeground="white")
btn_agregar.pack(side="left", padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento,
                         bg="#2F2F2F", fg="white", activebackground="#444444", activeforeground="white")
btn_eliminar.pack(side="left", padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit,
                      bg="#2F2F2F", fg="white", activebackground="#444444", activeforeground="white")
btn_salir.pack(side="right", padx=5)

# ----- Frame de la lista (TreeView) -----
frame_lista = tk.Frame(ventana, bg="#2F2F2F")
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

style = ttk.Style()
style.theme_use("default")

# Estilo para Treeview
style.configure("Treeview",
                background="#2F2F2F",
                fieldbackground="#2F2F2F",
                foreground="white")
style.configure("Treeview.Heading",
                background="#2F2F2F",
                foreground="white")

lista_eventos = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
lista_eventos.heading("Fecha", text="Fecha")
lista_eventos.heading("Hora", text="Hora")
lista_eventos.heading("Descripción", text="Descripción")
lista_eventos.pack(fill="both", expand=True, side="left")

# Scrollbar
scroll = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_eventos.yview)
lista_eventos.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

# ----- Contador de eventos -----
lbl_contador = tk.Label(ventana, text="Eventos guardados: 0", bg="#2F2F2F", fg="white", font=("Arial", 10, "italic"))
lbl_contador.pack(pady=5)

# ================== INICIO ==================
# Colocar el cursor automáticamente en la entrada de descripción al iniciar
entrada_desc.focus_set()
entrada_desc.select_range(0, tk.END)  # selecciona todo el texto (aunque esté vacío)

ventana.mainloop()
