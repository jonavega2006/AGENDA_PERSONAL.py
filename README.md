#  Agenda Personal 

Esta es una **agenda personal** desarrollada en **Python** con interfaz gráfica usando **Tkinter** y **tkcalendar**. Permite registrar eventos con fecha, hora y descripción, mostrarlos en una lista, eliminarlos y mantener un contador de eventos guardados.

---

## ✨ Características

- Selección de **fecha** mediante calendario.  
- Ingreso de **hora** y **descripción** del evento.  
- **Agregar** eventos a una lista (tabla).  
- **Eliminar** eventos seleccionados.  
- **Contador** automático de eventos guardados.  
- **Interfaz oscura** (#2F2F2F) con texto blanco, fácil de usar.

---

## 🛠️ Requisitos

- **Python 3.x**  
- Librerías de Python:  
  - `tkinter` (generalmente incluido en Python)  
  - `tkcalendar`  

Instalar `tkcalendar` si no lo tienes:

```bash
pip install tkcalendar
Cómo ejecutar
Descarga o clona el repositorio.

Abre la terminal o CMD y navega a la carpeta del proyecto.

Ejecuta el archivo principal:

bash
Copiar código
python agenda_personal.py
La ventana se abrirá. Ingresa fecha, hora y descripción, luego haz clic en Agregar Evento para guardar o Eliminar Evento para borrar un evento seleccionado.

Observa el contador de eventos actualizado automáticamente.

⚠️ Notas
La validación impide agregar eventos sin hora o descripción.

La interfaz está optimizada para un diseño oscuro, fácil de leer y usar.
