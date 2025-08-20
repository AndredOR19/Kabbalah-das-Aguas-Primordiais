class MantraEngine {
    constructor() {
        this.mantras = null;
        this.currentMantra = null;
        this.currentSyllable = 0;
        this.isPlaying = false;
        this.audioContext = null;
    }

    async loadMantras() {
        try {
            const response = await fetch('data/mantras.json');
            this.mantras = await response.json();
            return this.mantras;
        } catch (error) {
            console.error('Erro ao carregar mantras:', error);
            return null;
        }
    }

    async playMantra(mantraId) {
        if (!this.mantras) await this.loadMantras();
        
        this.currentMantra = this.mantras.find(m => m.id === mantraId);
        if (!this.currentMantra) return;

        this.isPlaying = true;
        this.currentSyllable = 0;
        
        await this.playNextSyllable();
    }

    async playNextSyllable() {
        if (!this.isPlaying || !this.currentMantra) return;

        const syllable = this.currentMantra.fonemas[this.currentSyllable];
        const color = this.currentMantra.cor[this.currentSyllable];
        const frequency = this.currentMantra.frequencia_base * (this.currentSyllable + 1);

        // Emitir evento para visualização
        globalThis.dispatchEvent(new CustomEvent('mantraSyllable', {
            detail: { syllable, color, frequency }
        }));

        // Tocar som
        await this.playTone(frequency, this.currentMantra.duracao_por_fonema);

        this.currentSyllable++;
        
        if (this.currentSyllable < this.currentMantra.fonemas.length) {
            setTimeout(() => this.playNextSyllable(), this.currentMantra.duracao_por_fonema);
        } else {
            this.isPlaying = false;
            globalThis.dispatchEvent(new CustomEvent('mantraComplete'));
        }
    }

    async playTone(frequency, duration) {
        if (!this.audioContext) {
            this.audioContext = new (globalThis.AudioContext || globalThis.webkitAudioContext)();
        }

        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);

        oscillator.frequency.value = frequency;
        oscillator.type = 'sine';

        gainNode.gain.setValueAtTime(0.3, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + duration / 1000);

        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + duration / 1000);
    }

    stop() {
        this.isPlaying = false;
        this.currentSyllable = 0;
    }
}
