function inicializarPlayer(concertos) {
  const AudioCtx = window.AudioContext || window.webkitAudioContext;
  const player = {
    concertoAtual: null,
    audio: null,
    ctx: null,
    osc: null,
    gain: null,
    notasTimer: null,

    iniciarConcerto(nomeConcerto) {
      const concerto = concertos.find(c => c.titulo.toLowerCase().includes(nomeConcerto.toLowerCase()));
      if (!concerto) return;

      this.concertoAtual = concerto;
      this.atualizarUI();
      this.iniciarAudio(concerto);
      this.iniciarEfeitosVisuais(concerto.cores);

      // Integrar com neurostorm
      window.postMessage({ type: 'CONCERTO_INICIADO', dados: concerto }, '*');
    },

    atualizarUI() {
      document.getElementById('concerto-titulo').textContent = this.concertoAtual.titulo;
      document.getElementById('frequencia-display').textContent = `${this.concertoAtual.frequencia_base} Hz`;
      const infoEl = document.getElementById('concerto-info');
      if (infoEl) infoEl.innerHTML = `Sefira: <span class="dado">${this.concertoAtual.sefira}</span> | Chakra: <span class="dado">${this.concertoAtual.chakra}</span>`;
    },

    iniciarAudio(concerto) {
      // Preferir arquivo se existir; se falhar, usar síntese
      const caminho = concerto.caminho_audio;
      if (caminho && typeof caminho === 'string' && !caminho.startsWith('data:')) {
        this.tocarArquivo(caminho, () => this.tocarSintese(concerto));
      } else {
        this.tocarSintese(concerto);
      }
    },

    tocarArquivo(caminho, onErro) {
      try {
        if (this.audio) { this.audio.pause(); this.audio.src = ''; }
        this.pararSintese();
        this.audio = new Audio(caminho);
        this.audio.loop = true;
        this.audio.onerror = () => { console.warn('Áudio não encontrado, usando síntese.'); onErro && onErro(); };
        this.audio.play().catch(() => onErro && onErro());
      } catch (e) {
        console.error('Falha ao tocar arquivo, usando síntese:', e);
        onErro && onErro();
      }
    },

    tocarSintese(concerto) {
      try {
        if (!this.ctx) this.ctx = new AudioCtx();
        this.pararSintese();
        this.audio && this.audio.pause();

        this.osc = this.ctx.createOscillator();
        this.gain = this.ctx.createGain();
        this.osc.type = 'sine';

        const base = Number(concerto.frequencia_base) || 440;
        this.osc.frequency.setValueAtTime(base, this.ctx.currentTime);

        // Envelope suave
        this.gain.gain.setValueAtTime(0.0001, this.ctx.currentTime);
        this.gain.gain.exponentialRampToValueAtTime(0.08, this.ctx.currentTime + 0.4);

        this.osc.connect(this.gain).connect(this.ctx.destination);
        this.osc.start();

        // Sequenciar notas se houver
        const notas = Array.isArray(concerto.notas) ? concerto.notas : [];
        let i = 0;
        clearInterval(this.notasTimer);
        if (notas.length) {
          this.notasTimer = setInterval(() => {
            const n = notas[i % notas.length];
            const f = Number(n?.frequencia) || base;
            this.osc.frequency.exponentialRampToValueAtTime(f, this.ctx.currentTime + 0.25);
            i++;
          }, 4000);
        }
      } catch (e) {
        console.error('Falha na síntese de áudio:', e);
      }
    },

    pararSintese() {
      try {
        if (this.notasTimer) clearInterval(this.notasTimer);
        if (this.osc) { this.osc.stop(); this.osc.disconnect(); this.osc = null; }
        if (this.gain) { this.gain.disconnect(); this.gain = null; }
      } catch {}
    },

    iniciarEfeitosVisuais(cores) {
      // Placeholder para integrar com Three.js no futuro
      document.body.style.setProperty('--vortex-color-a', cores?.[0] || '#00BCD4');
      document.body.style.setProperty('--vortex-color-b', cores?.[1] || '#263238');
    }
  };

  // Controles
  document.getElementById('btn-primavera').addEventListener('click', () => player.iniciarConcerto('Primavera'));
  document.getElementById('btn-estate')?.addEventListener('click', () => player.iniciarConcerto("Estade"));
  document.getElementById('btn-autunno')?.addEventListener('click', () => player.iniciarConcerto('Autunno'));
  document.getElementById('btn-inverno')?.addEventListener('click', () => player.iniciarConcerto('Inverno'));

  window.vortexPlayer = player;
}

function configurarEstacoes(estacoes) {
  // Implementar lógica das estações
}