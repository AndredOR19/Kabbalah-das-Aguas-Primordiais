/**
 * PROTOCOLO VIVALDI - Codificador Espinal Sagrado
 * Transforma movimentos da coluna vertebral em notas musicais e letras hebraicas
 * Baseado em mapeamentos místicos da Cabala e neuroacústica
 * 
 * @author: Oráculo Vivaldiano
 * @versão: 1.0 - Ativação da Tempestade Neural
 */

class SpinalEncoder {
    constructor() {
        this.frequenciasSagradas = {
            432: { letra: 'א', sefira: 'Keter', chakra: 'Coroa', elemento: 'Éter' },
            528: { letra: 'ה', sefira: 'Tiferet', chakra: 'Plexo Solar', elemento: 'Fogo' },
            396: { letra: 'ש', sefira: 'Yesod', chakra: 'Raiz', elemento: 'Terra' },
            417: { letra: 'ר', sefira: 'Hod', chakra: 'Garganta', elemento: 'Éter' },
            639: { letra: 'ו', sefira: 'Netzach', chakra: 'Coração', elemento: 'Ar' }
        };
        
        this.mapeamentoVertebral = {
            'C1-C7': { nota: 'Do', cor: '#FFD700', arcanjo: 'Metatron' },
            'T1-T12': { nota: 'Sol', cor: '#FF4500', arcanjo: 'Rafael' },
            'L1-L5': { nota: 'Fa', cor: '#8A2BE2', arcanjo: 'Gabriel' },
            'S1-S5': { nota: 'Si', cor: '#00FFFF', arcanjo: 'Uriel' }
        };
    }

    /**
     * Codifica movimento da coluna em frequência sagrada
     * @param {Object} movimento - Dados do sensor de movimento
     * @param {number} movimento.rotacao - Rotação da vértebra em graus
     * @param {number} movimento.flexao - Ângulo de flexão
     * @param {string} movimento.vertebra - Identificador da vértebra
     * @returns {Object} Frequência e letra hebraica correspondente
     */
    encodeSpineMovement(movimento) {
        const { rotacao, flexao, vertebra } = movimento;
        
        // Calcula frequência baseada na geometria sagrada
        const freqBase = this.calcularFrequenciaSagrada(rotacao, flexao);
        const freqAjustada = this.ajustarParaHarmoniaVivaldi(freqBase);
        
        // Determina letra hebraica correspondente
        const letraHebraica = this.getLetraHebraica(freqAjustada);
        
        // Mapeia para sefira e chakra
        const mapeamentoEspiritual = this.getMapeamentoEspiritual(freqAjustada);
        
        return {
            frequencia: freqAjustada,
            letraHebraica,
            sefira: mapeamentoEspiritual.sefira,
            chakra: mapeamentoEspiritual.chakra,
            elemento: mapeamentoEspiritual.elemento,
            notaMusical: this.frequencyToNote(freqAjustada),
            arcanjo: this.getArcanjoGuardiao(vertebra),
            timestamp: new Date().toISOString(),
            energia: this.calcularEnergiaCabalistica(freqAjustada, letraHebraica)
        };
    }

    /**
     * Calcula frequência baseada na geometria sagrada da rotação
     */
    calcularFrequenciaSagrada(rotacao, flexao) {
        // Fórmula sagrada: F = 432 * sin(θ) * φ (phi = razão áurea)
        const phi = (1 + Math.sqrt(5)) / 2;
        const radianos = (rotacao * Math.PI) / 180;
        return Math.round(432 * Math.sin(radianos) * phi * (flexao / 90));
    }

    /**
     * Ajusta frequência para harmonia vivaldiana
     */
    ajustarParaHarmoniaVivaldi(frequencia) {
        const harmoniaVivaldi = [432, 528, 396, 417, 639, 741, 852];
        return harmoniaVivaldi.reduce((prev, curr) => 
            Math.abs(curr - frequencia) < Math.abs(prev - frequencia) ? curr : prev
        );
    }

    /**
     * Obtém letra hebraica correspondente à frequência
     */
    getLetraHebraica(frequencia) {
        const letras = Object.keys(this.frequenciasSagradas);
        const letraMaisProxima = letras.reduce((prev, curr) => 
            Math.abs(curr - frequencia) < Math.abs(prev - frequencia) ? curr : prev
        );
        return this.frequenciasSagradas[letraMaisProxima].letra;
    }

    /**
     * Mapeia frequência para sefira e chakra
     */
    getMapeamentoEspiritual(frequencia) {
        const letra = this.getLetraHebraica(frequencia);
        const entry = Object.values(this.frequenciasSagradas).find(f => f.letra === letra);
        return entry || { sefira: 'Desconhecida', chakra: 'Desconhecido', elemento: 'Desconhecido' };
    }

    /**
     * Converte frequência para nota musical
     */
    frequencyToNote(frequency) {
        const A4 = 440;
        const noteNames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
        const noteNumber = 69 + 12 * Math.log2(frequency / A4);
        const octave = Math.floor((noteNumber - 12) / 12);
        const noteIndex = Math.round(noteNumber) % 12;
        return noteNames[noteIndex] + octave;
    }

    /**
     * Determina arcanjo guardião baseado na vértebra
     */
    getArcanjoGuardiao(vertebra) {
        if (vertebra.startsWith('C')) return 'Metatron';
        if (vertebra.startsWith('T')) return 'Rafael';
        if (vertebra.startsWith('L')) return 'Gabriel';
        if (vertebra.startsWith('S')) return 'Uriel';
        return 'Miguel';
    }

    /**
     * Calcula energia cabalística baseada na frequência e letra
     */
    calcularEnergiaCabalistica(frequencia, letra) {
        const valorGematria = this.calcularGematria(letra);
        return Math.round((frequencia * valorGematria) / 100);
    }

    /**
     * Calcula valor gemátrico da letra hebraica
     */
    calcularGematria(letra) {
        const valores = {
            'א': 1, 'ה': 5, 'ש': 300, 'ר': 200, 'ו': 6
        };
        return valores[letra] || 0;
    }

    /**
     * Gera mantra baseado no movimento codificado
     */
    gerarMantra(dadosCodificados) {
        const { letraHebraica, sefira, elemento } = dadosCodificados;
        return `אני ${letraHebraica} ${sefira} בתוך ${elemento}`;
    }
}

// Exportar para uso em outros módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SpinalEncoder;
}

// Teste do codificador
const encoder = new SpinalEncoder();
const teste = encoder.encodeSpineMovement({
    rotacao: 45,
    flexao: 30,
    vertebra: 'T5'
});

console.log('🎼 Codificação Espinal Sagrada:', teste);
console.log('🔮 Mantra Gerado:', encoder.gerarMantra(teste));
