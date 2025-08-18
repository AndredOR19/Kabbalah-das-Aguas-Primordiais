async function carregarDadosConcerto() {
  try {
    const response = await fetch('/assets/data/il_grosso_mogul.yml');
    const yamlData = await response.text();
    const concertos = jsyaml.load(yamlData);
    
    // Integrar com player
    window.concertosData = concertos;
    inicializarPlayer(concertos);
    
  } catch (erro) {
    console.error('Erro ao carregar dados YAML:', erro);
  }
}

async function carregarMapeamentoEstacoes() {
  try {
    const response = await fetch('/assets/data/quattro_stagioni.map');
    const mapData = await response.text();
    
    // Converter para JSON
    const estacoes = {};
    const linhas = mapData.split('\n');
    let estacaoAtual = null;
    
    linhas.forEach(linha => {
      if (linha.endsWith(':')) {
        estacaoAtual = linha.replace(':', '');
        estacoes[estacaoAtual] = {};
      } else if (estacaoAtual && linha.includes(':')) {
        const [chave, valor] = linha.split(':').map(item => item.trim());
        estacoes[estacaoAtual][chave] = isNaN(valor) ? valor : Number(valor);
      }
    });
    
    // Integrar com sistema
    window.estacoesData = estacoes;
    configurarEstacoes(estacoes);
    
  } catch (erro) {
    console.error('Erro ao carregar mapeamento:', erro);
  }
}

// Carregar ambos ao iniciar
document.addEventListener('DOMContentLoaded', () => {
  carregarDadosConcerto();
  carregarMapeamentoEstacoes();
});