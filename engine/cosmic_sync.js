class CosmicEngine {
    constructor() {
        this.currentParasha = null;
        this.userTikun = null;
    }

    async loadCurrentParasha() {
        const today = new Date();
        const parashiot = await this.loadParashiotData();
        
        // Encontra a Parashá atual baseada no calendário
        this.currentParasha = parashiot.find(p => {
            const start = new Date(p.startDate);
            const end = new Date(p.endDate);
            return today >= start && today <= end;
        });
        
        return this.currentParasha;
    }

    async loadParashiotData() {
        // Carrega o calendário completo
        const response = await fetch('data/parashiot.json');
        const data = await response.json();
        return data["5785"];
    }

    generateTikunSequence(parasha) {
        if (!parasha) return null;
        
        return {
            tipo: "tikun_parashico",
            elementos: [
                ...parasha.hebrewLetters.map(l => ({
                    tipo: "letra",
                    hebrew: l,
                    duracao: 4000,
                    intencao: parasha.tikun,
                    frequencia: parasha.frequencias[parasha.hebrewLetters.indexOf(l)],
                    cor: parasha.cores[parasha.hebrewLetters.indexOf(l)]
                })),
                {
                    tipo: "mantra",
                    id: parasha.mantra,
                    repeticoes: 12,
                    intencao: parasha.tikun
                }
            ]
        };
    }

    calculatePersonalTikun(birthdate) {
        const birth = new Date(birthdate);
        const today = new Date();
        const daysLived = Math.floor((today - birth) / (1000 * 60 * 60 * 24));
        
        // Algoritmo baseado no Zohar III, 216b
        const cycle = daysLived % 7;
        const sefirah = ["Chesed", "Gevurah", "Tiferet", "Netzach", "Hod", "Yesod", "Malchut"][cycle];
        
        return {
            sefirah: sefirah,
            dias_ciclo: cycle,
            letras_correcao: this.getLettersForSefirah(sefirah),
            frequencias: this.getFrequenciesForSefirah(sefirah)
        };
    }

    getLettersForSefirah(sefirah) {
        const map = {
            "Chesed": ["ח", "ס", "ד"],
            "Gevurah": ["ג", "ב", "ר"],
            "Tiferet": ["ת", "פ", "ר"],
            "Netzach": ["נ", "צ", "ח"],
            "Hod": ["ה", "ו", "ד"],
            "Yesod": ["י", "ס", "ד"],
            "Malchut": ["מ", "ל", "כ"]
        };
        return map[sefirah];
    }

    getFrequenciesForSefirah(sefirah) {
        const map = {
            "Chesed": [144, 288, 432],
            "Gevurah": [216, 432, 648],
            "Tiferet": [333, 666, 999],
            "Netzach": [111, 222, 333],
            "Hod": [222, 444, 666],
            "Yesod": [369, 738, 1107],
            "Malchut": [111, 222, 333]
        };
        return map[sefirah];
    }

    renderCosmicContext() {
        if (!this.currentParasha) return '';
        
        return `
            <div class="cosmic-panel">
                <h3>🌀 PARASHÁ: ${this.currentParasha.parasha}</h3>
                <p>⏳ ${this.currentParasha.data_gregoriana}</p>
                <p>🛠️ <em>${this.currentParasha.tikun}</em></p>
                <div class="sefirot-chain">
                    ${this.currentParasha.sefirot.map(s => `<span class="sephira">${s}</span>`).join('→')}
                </div>
                <p>📜 ${this.currentParasha.versos_chave.join(' | ')}</p>
            </div>
        `;
    }

    async updateInterface() {
        await this.loadCurrentParasha();
        
        const parashaInfo = document.getElementById('parasha-info');
        if (parashaInfo && this.currentParasha) {
            parashaInfo.innerHTML = this.renderCosmicContext();
        }
    }
}

// Inicialização global
const _cosmicEngine = new CosmicEngine();
