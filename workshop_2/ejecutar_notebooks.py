"""Ejecuta los notebooks completos con el Python que invoca este archivo."""

from pathlib import Path
import argparse
import sys
import time

import nbformat
from jupyter_client import KernelManager
from nbclient import NotebookClient


def ejecutar(ruta: Path, timeout: int) -> None:
    notebook = nbformat.read(ruta, as_version=4)
    nbformat.validate(notebook)
    inicio = time.perf_counter()
    manager = KernelManager(kernel_name="python3")
    manager.kernel_spec.argv = [
        sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"
    ]

    def informar(cell, cell_index, **kwargs):
        if cell.cell_type == "code":
            primera_linea = cell.source.strip().splitlines()
            etiqueta = primera_linea[0][:90] if primera_linea else "(vacía)"
            print(f"  Celda {cell_index + 1}/{len(notebook.cells)}: {etiqueta}", flush=True)

    cliente = NotebookClient(
        notebook,
        km=manager,
        timeout=timeout,
        allow_errors=False,
        resources={"metadata": {"path": str(ruta.parent)}},
        on_cell_start=informar,
    )
    print(f"Ejecutando {ruta.name} con {sys.executable}", flush=True)
    try:
        cliente.execute()
        nbformat.validate(notebook)
        nbformat.write(notebook, ruta)
    finally:
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
    print(f"Completado: {ruta.name} ({time.perf_counter() - inicio:.1f} s)", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "notebooks", nargs="*", help="Nombres o rutas; por defecto ejecuta ambos notebooks."
    )
    parser.add_argument("--timeout", type=int, default=7200, help="Segundos máximos por celda.")
    opciones = parser.parse_args()
    carpeta = Path(__file__).resolve().parent
    nombres = opciones.notebooks or [
        "01_regresion_vuelos.ipynb", "02_clasificacion_tiroides.ipynb"
    ]
    for nombre in nombres:
        ruta = Path(nombre)
        ejecutar(ruta if ruta.is_absolute() else carpeta / ruta, opciones.timeout)
