# Alvos para facilitar uso do SCII CLI

PY=python

scii:
	$(PY) src/scii_cli.py --emocao "$(EMOCAO)"

scii-json:
	$(PY) src/scii_cli.py --emocao "$(EMOCAO)" --json

scii-org:
	$(PY) src/scii_cli.py --emocao "$(EMOCAO)" --filtro-orgao "$(ORG)"

scii-arq:
	$(PY) src/scii_cli.py --emocao "$(EMOCAO)" --filtro-arquetipo "$(ARQ)"