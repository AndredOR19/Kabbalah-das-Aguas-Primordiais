// Sistema Principal - Integração de Todos os Componentes
class AguasPrimordiaisSystem {
    constructor() {
        this.cosmicEngine = new CosmicEngine();
        this.mantraPlayer = new MantraPlayer();
        this.isInitialized = false;
        
        this.init();
    }

    async init() {
        await this.setupEventListeners();
        await this.cosmicEngine.updateInterface();
        this.setupUI();
        console.log('🌊 Sistema das Águas Primordiais Ativado');
    }

    setupEventListeners() {
        // Tikun da Parashá
        document.getElementById('parasha-tikun').addEventListener('click', async () => {
            await this.activateParashaTikun();
        });

        // Mantra Selecionado
        document.getElementById('mantra-select').addEventListener('change', (e) => {
            this.loadMantra(e.target.value);
        });

        // Tikun Pessoal
        document.getElementById('personal-tikun').addEventListener('click', () => {
            this.activatePersonalTikun();
        });

        // Salvar Experiência
        document.getElementById('save-experience').addEventListener('click', () => {
            this.saveExperience();
        });

        // Auto-deteção de Parashá ao carregar
        window.addEventListener('load', async () => {
            await this.autoDetectParasha();
        });
    }

    async activateParashaTikun() {
        const parasha = await this.cosmicEngine.loadCurrentParasha();
        if (parasha) {
            const sequence = this.cosmicEngine.generateTikunSequence(parasha);
            this.displayTikunInfo(parasha);
            this.mantraPlayer.playSequence(sequence);
            this.animateChakras(parasha.corpo_alvo);
        }
    }

    async autoDetectParasha() {
        const parasha = await this.cosmicEngine.loadCurrentParasha();
        if (parasha) {
            const infoDiv = document.getElementById('parasha-info');
            if (infoDiv) {
                infoDiv.innerHTML = this.cosmicEngine.renderCosmicContext();
            }
        }
    }

    loadMantra(mantraId) {
        if (!mantraId) return;
        
        fetch('data/mantras.json')
            .then(response => response.json())
            .then(mantras => {
                const mantra = mantras.find(m => m.id === mantraId);
                if (mantra) {
                    this.mantraPlayer.loadMantra(mantra);
                    this.displayMantraInfo(mantra);
                }
            });
    }

    activatePersonalTikun() {
        const birthdate = document.getElementById('birthdate').value;
        if (!birthdate) {
            alert('Por favor, insira sua data de nascimento');
            return;
        }

        const tikun = this.cosmicEngine.calculatePersonalTikun(birthdate);
        this.displayPersonalTikun(tikun);
        
        // Criar sequência personalizada
        const sequence = {
            tipo: "tikun_pessoal",
            elementos: tikun.letras_correcao.map((letra, index) => ({
                tipo: "letra",
                hebrew: letra,
                duracao: 4000,
                frequencia: tikun.frequencias[index]
            }))
        };
        
        this.mantraPlayer.playSequence(sequence);
    }

    displayTikunInfo(parasha) {
        const infoDiv = document.getElementById('parasha-info');
        if (infoDiv) {
            infoDiv.innerHTML = `
                <div class="tikun-display">
                    <h3>🌀 ${parasha.parasha}</h3>
                    <p><strong>Tikun:</strong> ${parasha.tikun}</p>
                    <p><strong>Letras:</strong> ${parasha.hebrewLetters.join(' ')}</p>
                    <p><strong>Corpo:</strong> ${parasha.corpo_alvo.join(', ')}</p>
                </div>
            `;
        }
    }

    displayMantraInfo(mantra) {
        const infoDiv = document.getElementById('parasha-info');
        if (infoDiv) {
            infoDiv.innerHTML = `
                <div class="mantra-display">
                    <h3>🕉️ ${mantra.nome}</h3>
                    <p><strong>Fonemas:</strong> ${mantra.fonemas.join(' - ')}</p>
                    <p><strong>Efeito:</strong> ${mantra.efeito}</p>
                </div>
            `;
        }
    }

    displayPersonalTikun(tikun) {
        const infoDiv = document.getElementById('parasha-info');
        if (infoDiv) {
            infoDiv.innerHTML = `
                <div class="personal-display">
                    <h3>🌟 Seu Tikun Pessoal</h3>
                    <p><strong>Sefirah:</strong> ${tikun.sefirah}</p>
                    <p><strong>Letras:</strong> ${tikun.letras_correcao.join(' ')}</p>
                    <p><strong>Frequências:</strong> ${tikun.frequencias.join('Hz - ')}Hz</p>
                </div>
            `;
        }
    }

    animateChakras(bodyParts) {
        bodyParts.forEach((part, index) => {
            setTimeout(() => {
                const chakra = document.querySelector(`[data-chakra="${part.toLowerCase().replace(' ', '-')}"]`);
                if (chakra) {
                    chakra.classList.add('active');
                    setTimeout(() => chakra.classList.remove('active'), 3000);
                }
            }, index * 1000);
        });
    }

    saveExperience() {
        const log = document.getElementById('journey-log').value;
        if (!log.trim()) {
            alert('Por favor, escreva sua experiência');
            return;
        }

        const experience = {
            timestamp: new Date().toISOString(),
            parasha: this.currentParasha?.parasha || 'Personal',
            log: log,
            type: 'manual'
        };

        // Salvar no localStorage
        let experiences = JSON.parse(localStorage.getItem('aguas_experiences') || '[]');
        experiences.push(experience);
        localStorage.setItem('aguas_experiences', JSON.stringify(experiences));

        // Feedback visual
        document.getElementById('journey-log').value = '';
        alert('Experiência salva nos registros akáshicos!');
    }

    setupUI() {
        // Adicionar efeitos visuais
        this.addCosmicEffects();
    }

    addCosmicEffects() {
        // Efeito de brilho nas bordas
        document.body.style.animation = 'cosmicGlow 4s ease-in-out infinite';
        
        // Adicionar keyframes via JavaScript
        const style = document.createElement('style');
        style.textContent = `
            @keyframes cosmicGlow {
                0%, 100% { box-shadow: 0 0 5px var(--crystal-glow); }
                50% { box-shadow: 0 0 20px var(--crystal-glow), 0 0 30px var(--crystal-glow); }
            }
        `;
        document.head.appendChild(style);
    }

    async loadMantras() {
        try {
            const response = await fetch('data/mantras.json');
            const data = await response.json();
            this.mantras = data.mantras;
            this.populateMantraSelect();
        } catch (error) {
            console.error('Erro ao carregar mantras:', error);
        }
    }

    populateMantraSelect() {
        const select = document.getElementById('mantra-select');
        if (select && this.mantras) {
            // Limpar opções existentes
            select.innerHTML = '<option value="">Escolha um Mantra</option>';
            
            // Adicionar mantras
            this.mantras.forEach(mantra => {
                const option = document.createElement('option');
                option.value = mantra.id;
                option.textContent = mantra.nome;
                select.appendChild(option);
            });
        }
    }

    // Novo método para Tikun astrológico
    async activateAstrologicalTikun() {
        const birthdate = document.getElementById('birthdate').value;
        if (!birthdate) {
            alert('Por favor, insira sua data de nascimento');
            return;
        }

        const tikun = this.astrologicalSystem.getAstrologicalTikun(new Date(birthdate));
        this.displayAstrologicalTikun(tikun);
        
        // Gerar sequência baseada nos trânsitos
        const sequence = {
            tipo: "astrological_tikun",
            elementos: tikun.currentTransits.recommendedMantras.map((mantra, index) => ({
                tipo: "mantra",
                hebrew: mantra,
                duracao: 5000,
                frequencia: this.mantras?.find(m => m.hebrew === mantra)?.frequencia || 528
            }))
        };
        
        this.mantraPlayer.playSequence(sequence);
        this.animateChakras(tikun.currentTransits.affectedChakras);
    }

    displayAstrologicalTikun(tikun) {
        const infoDiv = document.getElementById('parasha-info');
        if (infoDiv) {
            infoDiv.innerHTML = `
                <div class="astrological-display">
                    <h3>🌟 Tikun Astrológico</h3>
                    <p><strong>Guia Diário:</strong> ${tikun.dailyGuidance.sefirah} - ${tikun.dailyGuidance.mantra}</p>
                    <p><strong>Foco:</strong> ${tikun.dailyGuidance.focus}</p>
                    <p><strong>Mantras Recomendados:</strong> ${tikun.currentTransits.recommendedMantras.join(' ')}</p>
                    <p><strong>Chakras Afetados:</strong> ${tikun.currentTransits.affectedChakras.join(', ')}</p>
                </div>
            `;
        }
    }
}

// Inicialização do Sistema Completo
document.addEventListener('DOMContentLoaded', async () => {
    // Carregar módulos adicionais
    const astrologicalSystem = new AstrologicalIntegration();
    const dashboard = new ExperienceDashboard();
    
    // Inicializar sistema principal
    const system = new AguasPrimordiaisSystem();
    
    // Adicionar integração astrológica ao sistema principal
    system.astrologicalSystem = astrologicalSystem;
    system.dashboard = dashboard;
    
    // Adicionar efeito de carregamento
    const loading = document.createElement('div');
    loading.innerHTML = '🌊 Carregando Protocolo do Verbo...';
    loading.style.position = 'fixed';
    loading.style.top = '50%';
    loading.style.left = '50%';
    loading.style.transform = 'translate(-50%, -50%)';
    loading.style.color = 'var(--primary-color)';
    loading.style.fontSize = '1.5em';
    document.body.appendChild(loading);
    
    // Carregar mantras
    await system.loadMantras();
    
    setTimeout(() => {
        loading.remove();
    }, 2000);
});

// Utilitários de debug
window.debugSystem = {
    showCurrentParasha: () => console.log(cosmicEngine.currentParasha),
    showPersonalTikun: (date) => console.log(cosmicEngine.calculatePersonalTikun(date)),
    showAllMantras: () => console.log('Carregue data/mantras.json para ver mantras disponíveis')
};
