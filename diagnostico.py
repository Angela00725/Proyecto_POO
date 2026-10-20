import importlib
import os

print("--- INICIANDO DIAGNÓSTICO DE IMPORTACIONES ---")
errores = 0

for root, _, files in os.walk("."):
    if "venv" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".py") and not file.startswith("__") and file != "diagnostico.py":
            rel_path = os.path.relpath(os.path.join(root, file), ".")
            modulo = rel_path[:-3].replace(os.sep, ".")
            try:
                importlib.import_module(modulo)
                print(f" OK: {modulo}")
            except Exception as e:
                print(f"❌ ERROR EN [{modulo}]: {e}")
                errores += 1

print(f"\n--- RESUMEN: {errores} errores encontrados ---")