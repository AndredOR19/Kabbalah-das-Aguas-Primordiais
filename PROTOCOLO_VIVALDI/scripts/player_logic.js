function inicializarPlayer(concertos) {
  const player = {
    concertoAtual: null,
    audioContext: new (window.AudioContext || window.webkitAudioContext)(),
    
    iniciarConcerto(nomeConcerto) {
      const concerto = concertos.find(c => c.titulo.includes(nomeConcerto));
      if (!concerto) return;
      
      this.concertoAtual = concerto;
      this.atualizarUI();
      this.carregarAudio(concerto.caminho_audio);
      this.iniciarEfeitosVisuais(concerto.cores);
      
      // Integrar com neurostorm
      window.postMessage({ 
        type: 'CONCERTO_INICIADO', 
        dados: concerto 
      }, '*');
    },
    
    atualizarUI() {
      document.getElementById('concerto-titulo').textContent = this.concertoAtual.titulo;
      document.getElementById('frequencia-display').textContent = 
        `${this.concertoAtual.frequencia_base} Hz`;
      
      document.querySelectorAll('#concerto-info .dado').forEach((span, i) => {
        span.textContent = Object.values(this.concertoAtual)[i+2];
      });
    },
    
    carregarAudio(caminho) {
      // Implementação de carregamento de áudio
    },
    
    iniciarEfeitosVisuais(cores) {
      // Implementação de Three.js
    }
  };
  
  // Event listeners para controles
  document.getElementById('btn-primavera').addEventListener('click', () => {
    player.iniciarConcerto('Primavera');
  });
  
  // ... outros botões
  
  window.vortexPlayer = player;
}

function configurarEstacoes(estacoes) {
  // Implementar lógica das estações
}