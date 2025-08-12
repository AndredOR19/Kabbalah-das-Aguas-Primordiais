import glob
import json
import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Template
from weasyprint import HTML
import os
from datetime import datetime

# --- Leitura dos dados psicossomáticos ---
files = sorted(glob.glob(".gitpsychodata/entries/*.json"))
if not files:
    print("Nenhuma entrada PSICO_JSON encontrada. Rode commits com dados antes.")
    exit()

data = []
for f in files:
    with open(f, "r", encoding="utf-8") as jf:
        try:
            entry = json.load(jf)
            data.append(entry)
        except:
            continue

df = pd.DataFrame(data)
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
else:
    df["timestamp"] = pd.NaT

df = df.sort_values("timestamp")

# --- Gerar gráficos ---

os.makedirs("reports", exist_ok=True)

def plot_and_save(y, title, filename):
    plt.figure(figsize=(8,4))
    plt.plot(df["timestamp"], df[y], marker='o')
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel(title)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

if {"hr", "timestamp"}.issubset(df.columns):
    plot_and_save("hr", "Frequência Cardíaca (HR)", "reports/hr.png")
if {"hrv", "timestamp"}.issubset(df.columns):
    plot_and_save("hrv", "Variabilidade da Frequência Cardíaca (HRV)", "reports/hrv.png")
if {"focus", "timestamp"}.issubset(df.columns):
    plot_and_save("focus", "Foco (%)", "reports/focus.png")

# --- Gerar HTML do relatório ---

template_html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Relatório Psicossomático</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    h1 { color: #004080; }
    img { max-width: 100%; margin-bottom: 20px; }
    .timestamp { font-size: 0.9em; color: gray; }
  </style>
</head>
<body>
  <h1>Relatório Psicossomático - Kabbalah das Águas Primordiais</h1>
  <p class="timestamp">Gerado em {{ now }}</p>

  {% if hr_img %}<h2>Frequência Cardíaca (HR)</h2><img src="{{ hr_img }}" />{% endif %}
  {% if hrv_img %}<h2>Variabilidade da Frequência Cardíaca (HRV)</h2><img src="{{ hrv_img }}" />{% endif %}
  {% if focus_img %}<h2>Foco (%)</h2><img src="{{ focus_img }}" />{% endif %}

  <h2>Resumo</h2>
  <ul>
    <li>Total de registros: {{ total }}</li>
    <li>Período: {{ start_date }} a {{ end_date }}</li>
  </ul>
</body>
</html>
"""

template = Template(template_html)

html_out = template.render(
    now=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    hr_img="hr.png" if os.path.exists("reports/hr.png") else None,
    hrv_img="hrv.png" if os.path.exists("reports/hrv.png") else None,
    focus_img="focus.png" if os.path.exists("reports/focus.png") else None,
    total=len(df),
    start_date=df["timestamp"].min().strftime("%d/%m/%Y") if not df["timestamp"].isna().all() else "N/A",
    end_date=df["timestamp"].max().strftime("%d/%m/%Y") if not df["timestamp"].isna().all() else "N/A"
)

html_file = "reports/psico_report.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_out)

# --- Converter HTML para PDF ---

HTML(html_file).write_pdf("reports/psico_report.pdf")

print("Relatório gerado em reports/psico_report.pdf e reports/psico_report.html")
