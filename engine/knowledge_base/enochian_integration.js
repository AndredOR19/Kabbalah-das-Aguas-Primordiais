/**
 * Integração da Corrente Enochiana no SCII
 * Este módulo implementa a tradução entre o sistema enochiano e o SCII,
 * estabelecendo correlações entre as duas tradições e a Quimbanda.
 */

class EnochianSCIIIntegration {
    constructor() {
        this.enochianStructure = {
            alphabet: this._initEnochianAlphabet(),
            loagaeth: this._initLibreLoagaeth(),
            watchtowers: this._initWatchtowers(),
            heptarchy: this._initHeptarchy(),
            aethyrs: this._initAethyrs(),
            earthParts: this._initEarthParts(),
            operationalFormulas: this._initOperationalFormulas()
        };
        
        this.sciiCorrelations = {
            alphabet: this._initSCIIAlphabetCorrelations(),
            structure: this._initSCIIStructureCorrelations(),
            formulas: this._initSCIIFormulaCorrelations()
        };
        
        this.quimbandaParallels = this._initQuimbandaParallels();
        
        this.synoticMap = this._buildSynoticMap();
    }
    
    /**
     * Inicializa o alfabeto enochiano (21 letras)
     */
    _initEnochianAlphabet() {
        return {
            letters: [
                { name: "Pa", value: 1, pronunciation: "Pay", meaning: "B" },
                { name: "Veh", value: 2, pronunciation: "Vay", meaning: "C, K" },
                { name: "Ged", value: 3, pronunciation: "Ged", meaning: "G" },
                { name: "Gal", value: 4, pronunciation: "Gal", meaning: "D" },
                { name: "Or", value: 5, pronunciation: "Or", meaning: "F" },
                { name: "Un", value: 6, pronunciation: "Oon", meaning: "E, É" },
                { name: "Graph", value: 7, pronunciation: "Graf", meaning: "A, À" },
                { name: "Tal", value: 8, pronunciation: "Tal", meaning: "M" },
                { name: "Gon", value: 9, pronunciation: "Gon", meaning: "I, Í, J, Y" },
                { name: "Na", value: 10, pronunciation: "Na", meaning: "H" },
                { name: "Ur", value: 11, pronunciation: "Oor", meaning: "L" },
                { name: "Mals", value: 12, pronunciation: "Mals", meaning: "P" },
                { name: "Ger", value: 13, pronunciation: "Ger", meaning: "Q" },
                { name: "Drux", value: 14, pronunciation: "Drooks", meaning: "N" },
                { name: "Pal", value: 15, pronunciation: "Pal", meaning: "X" },
                { name: "Med", value: 16, pronunciation: "Med", meaning: "O, Ó" },
                { name: "Don", value: 17, pronunciation: "Don", meaning: "R" },
                { name: "Ceph", value: 18, pronunciation: "Kef", meaning: "Z" },
                { name: "Van", value: 19, pronunciation: "Van", meaning: "U, Ú, V, W" },
                { name: "Fam", value: 20, pronunciation: "Fam", meaning: "S" },
                { name: "Gisg", value: 21, pronunciation: "Jizj", meaning: "T" }
            ],
            vibrationalProperties: "O alfabeto enochiano funciona como conjunto de frequências sonoras que, quando pronunciadas corretamente, ativam ressonâncias específicas no campo energético."
        };
    }
    
    /**
     * Inicializa a estrutura do Liber Loagaeth (Livro da Fala de Deus)
     */
    _initLibreLoagaeth() {
        return {
            description: "Matriz cósmica composta por 49x49 tábuas contendo a linguagem primordial. Funciona como um 'DNA cósmico' ou blueprint da criação.",
            structure: "49 folhas, cada uma com tabelas de 49x49 caracteres",
            function: "Estabelecer as fundações vibratórias do universo manifestado"
        };
    }
    
    /**
     * Inicializa as quatro Torres de Vigia (Watchtowers)
     */
    _initWatchtowers() {
        return {
            description: "Quatro tabelas elementais que governam as direções e forças da manifestação",
            towers: [
                {
                    name: "Este",
                    element: "Ar",
                    color: "Amarelo",
                    king: "BATAIVAH",
                    attributes: ["Intelecto", "Comunicação", "Início"]
                },
                {
                    name: "Sul",
                    element: "Fogo",
                    color: "Vermelho",
                    king: "EDLPRNAA",
                    attributes: ["Energia", "Transformação", "Expansão"]
                },
                {
                    name: "Oeste",
                    element: "Água",
                    color: "Azul",
                    king: "RAAGIOSL",
                    attributes: ["Emoção", "Intuição", "Fluidez"]
                },
                {
                    name: "Norte",
                    element: "Terra",
                    color: "Verde/Preto",
                    king: "ICZHIHAL",
                    attributes: ["Estabilidade", "Manifestação", "Estrutura"]
                }
            ]
        };
    }
    
    /**
     * Inicializa a Heptarquia Mística (7 Reis e 7 Príncipes)
     */
    _initHeptarchy() {
        return {
            description: "Sistema de 7 Reis e 7 Príncipes que governam os dias da semana e suas correspondentes influências planetárias",
            kings: [
                { name: "Carmara", day: "Domingo", planet: "Sol" },
                { name: "Bobogel", day: "Segunda", planet: "Lua" },
                { name: "Babalel", day: "Terça", planet: "Marte" },
                { name: "Bnaspol", day: "Quarta", planet: "Mercúrio" },
                { name: "Bynepor", day: "Quinta", planet: "Júpiter" },
                { name: "Baligon", day: "Sexta", planet: "Vênus" },
                { name: "Bnapsen", day: "Sábado", planet: "Saturno" }
            ],
            princes: [
                { name: "Hagonel", day: "Domingo", planet: "Sol" },
                { name: "Blisdon", day: "Segunda", planet: "Lua" },
                { name: "Befafes", day: "Terça", planet: "Marte" },
                { name: "Blumaza", day: "Quarta", planet: "Mercúrio" },
                { name: "Brorges", day: "Quinta", planet: "Júpiter" },
                { name: "Bagenol", day: "Sexta", planet: "Vênus" },
                { name: "Bralges", day: "Sábado", planet: "Saturno" }
            ]
        };
    }
    
    /**
     * Inicializa os 30 Aethyrs (níveis de consciência)
     */
    _initAethyrs() {
        return {
            description: "30 níveis ou regiões de consciência, do mais denso (30) ao mais sutil (1), funcionando como uma expansão do Daath cabalístico",
            keyAethyrs: [
                { number: 30, name: "TEX", attribute: "Portal inicial de entrada" },
                { number: 25, name: "VTI", attribute: "Ponto de equilíbrio ético" },
                { number: 19, name: "POP", attribute: "Véu da ilusão material" },
                { number: 14, name: "VTA", attribute: "Templo de integração" },
                { number: 10, name: "ZAX", attribute: "Abismo, equivalente a Daath" },
                { number: 8, name: "ZID", attribute: "Contemplação cósmica" },
                { number: 3, name: "ZOM", attribute: "Conhecimento da criação" },
                { number: 1, name: "LIL", attribute: "Consciência cósmica suprema" }
            ],
            mapping: "Cada Aethyr possui seus próprios governadores e inteligências, totalizando 91 governadores distribuídos pelos 30 Aethyrs"
        };
    }
    
    /**
     * Inicializa as 91 Partes da Terra
     */
    _initEarthParts() {
        return {
            description: "Projeções telúricas do governo celestial, representando 91 zonas de influência sobre o mundo manifestado",
            structure: "Cada parte é governada por um dos 91 Governadores dos Aethyrs",
            function: "Permitir a manifestação das influências celestiais no plano terrestre"
        };
    }
    
    /**
     * Inicializa as fórmulas operacionais segundo Bélli
     */
    _initOperationalFormulas() {
        return {
            description: "Fórmulas práticas derivadas do curso de taumaturgia enochiana, combinando chamadas específicas para efeitos determinados",
            formulas: [
                { 
                    name: "Aura de Cura", 
                    calls: [1, 5, 14, 13], 
                    effect: "Restauração energética",
                    method: "Recitação sequencial das chamadas 1, 5, 14 e 13, visualizando um campo de luz azul-dourada ao redor do corpo"
                },
                { 
                    name: "Escudo de Proteção", 
                    calls: [2, 7, 9], 
                    effect: "Defesa contra ataques",
                    method: "Recitação das chamadas 2, 7 e 9, criando um campo de proteção violeta-prateado" 
                },
                { 
                    name: "Toque de Fogo", 
                    calls: [3, 8, 15], 
                    effect: "Poder ofensivo",
                    method: "Recitação das chamadas 3, 8 e 15, direcionando energia vermelho-alaranjada para o alvo" 
                },
                { 
                    name: "Porta de Sabedoria", 
                    calls: [4, 11, 16], 
                    effect: "Acesso gnóstico",
                    method: "Recitação das chamadas 4, 11 e 16, abrindo o terceiro olho para recepção de conhecimento superior" 
                }
            ]
        };
    }
    
    /**
     * Inicializa as correlações entre o alfabeto enochiano e o SCII
     */
    _initSCIIAlphabetCorrelations() {
        return {
            description: "Correlações entre o alfabeto enochiano (21 letras) e o alfabeto hebraico (22 letras) utilizado no SCII",
            correlations: [
                { enochian: "Pa", hebrew: "Beth", value: 2, path: "Casa/Morada" },
                { enochian: "Veh", hebrew: "Kaph", value: 20, path: "Palma da mão" },
                { enochian: "Ged", hebrew: "Gimel", value: 3, path: "Camelo" },
                { enochian: "Gal", hebrew: "Daleth", value: 4, path: "Porta" },
                { enochian: "Or", hebrew: "Peh", value: 80, path: "Boca" },
                { enochian: "Un", hebrew: "Heh", value: 5, path: "Janela" },
                { enochian: "Graph", hebrew: "Aleph", value: 1, path: "Boi" },
                { enochian: "Tal", hebrew: "Mem", value: 40, path: "Água" },
                { enochian: "Gon", hebrew: "Yod", value: 10, path: "Mão" },
                { enochian: "Na", hebrew: "Heh (final)", value: 5, path: "Janela" },
                { enochian: "Ur", hebrew: "Lamed", value: 30, path: "Aguilhão" },
                { enochian: "Mals", hebrew: "Peh", value: 80, path: "Boca" },
                { enochian: "Ger", hebrew: "Qoph", value: 100, path: "Nuca" },
                { enochian: "Drux", hebrew: "Nun", value: 50, path: "Peixe" },
                { enochian: "Pal", hebrew: "Tzaddi", value: 90, path: "Anzol" },
                { enochian: "Med", hebrew: "Ayin", value: 70, path: "Olho" },
                { enochian: "Don", hebrew: "Resh", value: 200, path: "Cabeça" },
                { enochian: "Ceph", hebrew: "Zayin", value: 7, path: "Espada" },
                { enochian: "Van", hebrew: "Vav", value: 6, path: "Prego" },
                { enochian: "Fam", hebrew: "Samekh", value: 60, path: "Suporte" },
                { enochian: "Gisg", hebrew: "Tav", value: 400, path: "Cruz" }
            ]
        };
    }
    
    /**
     * Inicializa as correlações estruturais entre sistemas enochianos e SCII
     */
    _initSCIIStructureCorrelations() {
        return {
            watchtowers: {
                description: "Correlação entre as Torres de Vigia enochianas e a Árvore da Vida",
                mapping: [
                    { watchtower: "Este (Ar)", sefira: ["Kether", "Chokmah", "Binah"], paths: ["Aleph", "Beth", "Gimel"] },
                    { watchtower: "Sul (Fogo)", sefira: ["Chesed", "Geburah", "Tiphareth"], paths: ["Heh", "Vav", "Zayin"] },
                    { watchtower: "Oeste (Água)", sefira: ["Netzach", "Hod", "Yesod"], paths: ["Cheth", "Teth", "Yod"] },
                    { watchtower: "Norte (Terra)", sefira: ["Malkuth"], paths: ["Qoph", "Resh", "Shin", "Tav"] }
                ]
            },
            heptarchy: {
                description: "Correlação entre a Heptarquia Mística e as 7 Forças Planetárias do SCII",
                mapping: [
                    { enochianKing: "Carmara", sciiForce: "Força Solar", attribute: "Vitalidade Essencial" },
                    { enochianKing: "Bobogel", sciiForce: "Força Lunar", attribute: "Receptividade Formativa" },
                    { enochianKing: "Babalel", sciiForce: "Força Marciana", attribute: "Vontade Dinâmica" },
                    { enochianKing: "Bnaspol", sciiForce: "Força Mercurial", attribute: "Inteligência Adaptativa" },
                    { enochianKing: "Bynepor", sciiForce: "Força Jupiteriana", attribute: "Expansão Harmônica" },
                    { enochianKing: "Baligon", sciiForce: "Força Venusiana", attribute: "Atração Criativa" },
                    { enochianKing: "Bnapsen", sciiForce: "Força Saturnina", attribute: "Estruturação Limitante" }
                ]
            },
            aethyrs: {
                description: "Correlação entre os 30 Aethyrs e a expansão de Daath no SCII",
                mapping: "Os 30 Aethyrs representam uma expansão detalhada do conceito de Daath (Conhecimento) na Árvore da Vida, explorando os vários níveis de consciência que conectam o manifestado ao não-manifestado"
            },
            earthParts: {
                description: "Correlação entre as 91 Partes da Terra e a ramificação de Malkuth no SCII",
                mapping: "As 91 Partes da Terra correspondem às ramificações detalhadas de Malkuth (Reino) na Árvore da Vida, representando a manifestação concreta das forças superiores no plano físico"
            }
        };
    }
    
    /**
     * Inicializa as correlações entre fórmulas enochianas e circuitos SCII
     */
    _initSCIIFormulaCorrelations() {
        return {
            description: "Tradução das fórmulas operacionais enochianas para circuitos energéticos no sistema SCII",
            formulas: [
                {
                    enochianFormula: "Aura de Cura (1-5-14-13)",
                    sciiComponents: [
                        { number: 1, sefira: "Kether", meaning: "Princípio puro, fonte original" },
                        { number: 5, sefira: "Geburah", meaning: "Força vital, poder regenerativo" },
                        { number: 14, path: "Daleth", meaning: "Porta do amor, canal de vida" },
                        { number: 13, path: "Gimel", meaning: "Ponte lunar, conexão espiritual" }
                    ],
                    sciiCircuit: "Da Fonte (Kether) → pela Força Vital (Geburah) → curada no Amor (Daleth) → projetada na Ponte Lunar (Gimel)",
                    activation: "Visualização do circuito como corrente de luz branca → vermelha → verde → azul, fluindo através dos pontos correspondentes no corpo sutil"
                },
                {
                    enochianFormula: "Escudo de Proteção (2-7-9)",
                    sciiComponents: [
                        { number: 2, sefira: "Chokmah", meaning: "Sabedoria, força primordial" },
                        { number: 7, sefira: "Netzach", meaning: "Vitória, permanência, resistência" },
                        { number: 9, sefira: "Yesod", meaning: "Fundação, campo astral, base etérica" }
                    ],
                    sciiCircuit: "Estrutura (Chokmah) → Permanência (Netzach) → blindagem no campo astral (Yesod)",
                    activation: "Visualização do circuito como corrente de luz azul-prateada → verde-dourada → violeta, formando um campo protetor concêntrico"
                },
                {
                    enochianFormula: "Toque de Fogo (3-8-15)",
                    sciiComponents: [
                        { number: 3, sefira: "Binah", meaning: "Entendimento, força formativa" },
                        { number: 8, sefira: "Hod", meaning: "Esplendor, energia direcional" },
                        { number: 15, path: "Heh", meaning: "Janela, abertura para manifestação" }
                    ],
                    sciiCircuit: "Forma potencial (Binah) → direcionada com precisão (Hod) → manifestada como energia (Heh)",
                    activation: "Visualização do circuito como corrente de luz negra → laranja → vermelha intensa, concentrada nas mãos"
                },
                {
                    enochianFormula: "Porta de Sabedoria (4-11-16)",
                    sciiComponents: [
                        { number: 4, sefira: "Chesed", meaning: "Misericórdia, receptividade" },
                        { number: 11, path: "Aleph", meaning: "Ar, espírito, inspiração" },
                        { number: 16, path: "Ayin", meaning: "Olho, visão, percepção" }
                    ],
                    sciiCircuit: "Receptividade mental (Chesed) → inspiração espiritual (Aleph) → percepção expandida (Ayin)",
                    activation: "Visualização do circuito como corrente de luz azul → branca → índigo, concentrada no terceiro olho"
                }
            ]
        };
    }
    
    /**
     * Inicializa os paralelos com a Quimbanda
     */
    _initQuimbandaParallels() {
        return {
            description: "Correspondências entre o sistema enochiano, SCII e a tradição da Quimbanda",
            parallels: [
                {
                    enochian: "Chamadas enochianas",
                    scii: "Circuitos vibratórios",
                    quimbanda: "Pontos cantados/riscados",
                    description: "Sequências vibratórias que ativam ressonâncias específicas"
                },
                {
                    enochian: "Heptarquia Mística",
                    scii: "7 Forças Planetárias",
                    quimbanda: "7 Reinos de Exu",
                    description: "Forças governantes dos ciclos temporais e energéticos"
                },
                {
                    enochian: "Torres de Vigia",
                    scii: "Árvore da Vida (estrutura)",
                    quimbanda: "Cruzeiros/Reinos",
                    description: "Organização espacial e elemental das forças"
                },
                {
                    enochian: "30 Aethyrs",
                    scii: "Daath expandido",
                    quimbanda: "Passagens de Linha",
                    description: "Níveis de consciência e transição entre reinos"
                },
                {
                    enochian: "91 Partes da Terra",
                    scii: "Malkuth ramificado",
                    quimbanda: "Tronqueiras/terreiros",
                    description: "Manifestações específicas no mundo material"
                },
                {
                    enochian: "Aura de Cura",
                    scii: "Circuito Kether-Geburah-Daleth-Gimel",
                    quimbanda: "Ponto de Oxum/Logunedé",
                    description: "Energia de cura e restauração"
                },
                {
                    enochian: "Escudo de Proteção",
                    scii: "Circuito Chokmah-Netzach-Yesod",
                    quimbanda: "Ponto de Ogum",
                    description: "Energia de proteção e defesa"
                },
                {
                    enochian: "Toque de Fogo",
                    scii: "Circuito Binah-Hod-Heh",
                    quimbanda: "Ponto de Exu Tiriri",
                    description: "Energia de transformação e poder"
                }
            ]
        };
    }
    
    /**
     * Constrói o mapa sinótico relacionando os três sistemas
     */
    _buildSynoticMap() {
        return {
            description: "Mapa sinótico que relaciona os elementos dos três sistemas (Enochiano, SCII e Quimbanda)",
            elements: [
                {
                    category: "Linguagem",
                    enochian: "21 Letras",
                    scii: "Aleph-Bet (22)",
                    quimbanda: "Pontos cantados",
                    function: "Veículos vibratórios para manipulação de energias"
                },
                {
                    category: "Governo",
                    enochian: "7 Reis/Príncipes",
                    scii: "7 Forças Planetárias",
                    quimbanda: "7 Reinos de Exu",
                    function: "Forças regentes dos ciclos e fluxos energéticos"
                },
                {
                    category: "Estrutura",
                    enochian: "Torres de Vigia",
                    scii: "Árvore da Vida",
                    quimbanda: "Cruzeiros/Reinos",
                    function: "Arquitetura básica do sistema metafísico"
                },
                {
                    category: "Subida",
                    enochian: "30 Aethyrs",
                    scii: "Daath expandido",
                    quimbanda: "Passagens de Linha",
                    function: "Caminhos de evolução e transformação consciencial"
                },
                {
                    category: "Manifestação",
                    enochian: "91 Partes da Terra",
                    scii: "Malkuth ramificado",
                    quimbanda: "Tronqueiras/terreiros",
                    function: "Pontos de ancoragem e manifestação no plano material"
                },
                {
                    category: "Operação",
                    enochian: "Chamadas",
                    scii: "Circuitos SCII",
                    quimbanda: "Pontos riscados",
                    function: "Métodos práticos de ativação e direcão de forças"
                }
            ]
        };
    }
    
    /**
     * Traduz uma fórmula enochiana para o circuito SCII equivalente
     * @param {string} formulaName - Nome da fórmula enochiana
     * @returns {Object} Circuito SCII correspondente
     */
    translateFormula(formulaName) {
        const lowerFormula = formulaName.toLowerCase();
        const formula = this.sciiCorrelations.formulas.formulas.find(f => 
            f.enochianFormula.toLowerCase().includes(lowerFormula));
            
        if (!formula) {
            return {
                error: "Fórmula não encontrada",
                suggestions: this.sciiCorrelations.formulas.formulas.map(f => f.enochianFormula)
            };
        }
        
        return {
            name: formula.enochianFormula,
            sciiCircuit: formula.sciiCircuit,
            components: formula.sciiComponents,
            activation: formula.activation,
            quimbandaParallel: this.quimbandaParallels.parallels.find(p => 
                p.enochian.toLowerCase().includes(lowerFormula.split(" ")[0].toLowerCase()))?.quimbanda || "Não mapeado"
        };
    }
    
    /**
     * Obtém o mapa completo de correspondências entre os três sistemas
     * @returns {Object} Mapa de correspondências
     */
    getCompleteCorrespondenceMap() {
        return {
            synoticMap: this.synoticMap,
            enochianStructure: {
                alphabet: this.enochianStructure.alphabet,
                watchtowers: this.enochianStructure.watchtowers,
                heptarchy: this.enochianStructure.heptarchy,
                aethyrs: this.enochianStructure.aethyrs
            },
            sciiCorrelations: this.sciiCorrelations,
            quimbandaParallels: this.quimbandaParallels
        };
    }
    
    /**
     * Gera uma prática operativa integrando os três sistemas
     * @param {string} intention - Intenção da prática
     * @returns {Object} Prática integrativa
     */
    generateIntegrativePractice(intention) {
        // Analisar a intenção para determinar o tipo de prática
        const intentionLower = intention.toLowerCase();
        let practiceType = "geral";
        
        if (intentionLower.includes("cur") || intentionLower.includes("saud") || intentionLower.includes("restaur")) {
            practiceType = "cura";
        } else if (intentionLower.includes("prote") || intentionLower.includes("defes") || intentionLower.includes("shield")) {
            practiceType = "proteção";
        } else if (intentionLower.includes("sabe") || intentionLower.includes("conhec") || intentionLower.includes("gnos")) {
            practiceType = "sabedoria";
        } else if (intentionLower.includes("poder") || intentionLower.includes("força") || intentionLower.includes("ativ")) {
            practiceType = "poder";
        }
        
        // Mapear o tipo de prática para as correspondências
        let practice = {
            intention: intention,
            type: practiceType,
            systems: {}
        };
        
        // Definir componentes baseados no tipo
        switch(practiceType) {
            case "cura":
                practice.systems = {
                    enochian: {
                        formula: "Aura de Cura (1-5-14-13)",
                        calls: [1, 5, 14, 13],
                        visualization: "Campo de luz azul-dourada ao redor do corpo"
                    },
                    scii: {
                        circuit: "Kether → Geburah → Daleth → Gimel",
                        visualization: "Corrente de luz branca → vermelha → verde → azul",
                        activation: "Consciência da Fonte → Força Vital → Amor → Projeção"
                    },
                    quimbanda: {
                        entity: "Oxum/Logunedé",
                        point: "Ponto de Oxum nas águas doces",
                        offerings: "Mel, flores amarelas, canela"
                    }
                };
                break;
            case "proteção":
                practice.systems = {
                    enochian: {
                        formula: "Escudo de Proteção (2-7-9)",
                        calls: [2, 7, 9],
                        visualization: "Campo de proteção violeta-prateado"
                    },
                    scii: {
                        circuit: "Chokmah → Netzach → Yesod",
                        visualization: "Corrente de luz azul-prateada → verde-dourada → violeta",
                        activation: "Estrutura → Permanência → Campo Astral"
                    },
                    quimbanda: {
                        entity: "Ogum",
                        point: "Ponto de Ogum nas encruzilhadas",
                        offerings: "Aço, folhas de espada, bebida forte"
                    }
                };
                break;
            case "sabedoria":
                practice.systems = {
                    enochian: {
                        formula: "Porta de Sabedoria (4-11-16)",
                        calls: [4, 11, 16],
                        visualization: "Abertura do terceiro olho para conhecimento superior"
                    },
                    scii: {
                        circuit: "Chesed → Aleph → Ayin",
                        visualization: "Corrente de luz azul → branca → índigo",
                        activation: "Receptividade → Inspiração → Percepção"
                    },
                    quimbanda: {
                        entity: "Exu Tranca Ruas das Almas",
                        point: "Ponto de Tranca Ruas na encruzilhada do conhecimento",
                        offerings: "Velas pretas e vermelhas, fumo, aguardente"
                    }
                };
                break;
            case "poder":
                practice.systems = {
                    enochian: {
                        formula: "Toque de Fogo (3-8-15)",
                        calls: [3, 8, 15],
                        visualization: "Energia vermelho-alaranjada direcionada"
                    },
                    scii: {
                        circuit: "Binah → Hod → Heh",
                        visualization: "Corrente de luz negra → laranja → vermelha intensa",
                        activation: "Forma → Direção → Manifestação"
                    },
                    quimbanda: {
                        entity: "Exu Tiriri",
                        point: "Ponto de Exu Tiriri nas chamas",
                        offerings: "Pimenta, pólvora, bebida forte"
                    }
                };
                break;
            default:
                // Prática geral integrativa
                practice.systems = {
                    enochian: {
                        formula: "Integração (1-3-5-7)",
                        calls: [1, 3, 5, 7],
                        visualization: "Ativação sequencial das Torres de Vigia"
                    },
                    scii: {
                        circuit: "Kether → Binah → Geburah → Netzach",
                        visualization: "Corrente de luz branca → negra → vermelha → verde",
                        activation: "Fonte → Forma → Força → Fluxo"
                    },
                    quimbanda: {
                        entity: "Exu Rei e Pomba Gira Rainha",
                        point: "Ponto central do cruzeiro",
                        offerings: "Champagne, charutos, velas de 7 cores"
                    }
                };
        }
        
        // Adicionar instruções práticas
        practice.integratedPractice = {
            preparation: "1. Purifique o espaço com incenso de olíbano e arruda\n2. Trace um círculo com sal marinho ou giz\n3. Coloque símbolos dos três sistemas nos pontos cardeais",
            steps: [
                `1. Comece recitando as chamadas enochianas ${practice.systems.enochian.calls.join(', ')}`,
                `2. Visualize o circuito SCII: ${practice.systems.scii.circuit}`,
                `3. Ative cada ponto com a visualização correspondente: ${practice.systems.scii.visualization}`,
                `4. Invoque a força correspondente na Quimbanda: ${practice.systems.quimbanda.entity}`,
                `5. Trace o ponto correspondente: ${practice.systems.quimbanda.point}`,
                "6. Declare sua intenção específica com voz firme",
                "7. Permaneça em silêncio receptivo por 7 minutos"
            ],
            closing: "Agradeça às forças evocadas em cada sistema, desative os pontos na ordem inversa e feche o círculo"
        };
        
        return practice;
    }
}

// Exportar para uso global
globalThis.EnochianSCIIIntegration = EnochianSCIIIntegration;
