import os

ROOT = "."  # Pasta raiz do repositório
OUTPUT = "MENU.md"

def gerar_menu(pasta_raiz):
    menu = ["# 📂 MENU AUTOMÁTICO – O Corpo do Verbo\n"]
    for dirpath, _, filenames in os.walk(pasta_raiz):
        if ".git" in dirpath or "__pycache__" in dirpath:
            continue
        nivel = dirpath.count(os.sep)
        indent = "  " * nivel
        rel_dir = os.path.relpath(dirpath, pasta_raiz).replace("\\", "/")
        menu.append(f"{indent}- **{rel_dir}**")
        for f in filenames:
            caminho = os.path.join(rel_dir, f).replace("\\", "/")
            if caminho.startswith(".") or f == OUTPUT:
                continue
            menu.append(f"{indent}  - [{f}]({caminho})")
    return "\n".join(menu)

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(gerar_menu(ROOT))
