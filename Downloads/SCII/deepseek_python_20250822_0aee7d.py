from web3 import Web3
import json

class RegistroImutavel:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/SEU_PROJETO'))
        self.contrato = self.carregar_contrato()
    
    def carregar_contrato(self):
        with open('contrato_abi.json', 'r') as f:
            abi = json.load(f)
        return self.w3.eth.contract(address='0x...', abi=abi)
    
    def registrar_pratica(self, tipo_pratica, duracao, metricas):
        """
        Registra prática na blockchain para criar histórico imutável
        """
        tx_hash = self.contrato.functions.registrarPratica(
            tipo_pratica, duracao, metricas
        ).transact()
        return tx_hash