// Spinal Encoder - Codificador Espinal Sagrado
// Baseado na Kabbalah e no mapeamento espinal

// Mapeamento espinal completo
const spinalMap = {
    cervical: {
        C1: { frequency: 963, sefira: 'keter', element: 'éter' },
        C2: { frequency: 852, sefira: 'chokmah', element: 'ar' },
        C3: { frequency: 741, sefira: 'binah', element: 'terra' },
        C4: { frequency: 639, sefira: 'chesed', element: 'água' },
        C5: { frequency: 528, sefira: 'gevurah', element: 'fogo' },
        C6: { frequency: 417, sefira: 'tiferet', element: 'sol' },
        C7: { frequency: 396, sefira: 'netzach', element: 'vênus' }
    },
    thoracic: {
        T1: { frequency: 285, sefira: 'hod', element: 'mercúrio' },
        T2: { frequency: 174, sefira: 'yesod', element: 'lua' },
        T3: { frequency: 963, sefira: 'malchut', element: 'terra' },
        T4: { frequency: 852, sefira: 'keter', element: 'éter' },
        T5: { frequency: 741, sefira: 'chokmah', element: 'ar' },
        T6: { frequency: 639, sefira: 'binah', element: 'terra' },
        T7: { frequency: 528, sefira: 'chesed', element: 'água' },
        T8: { frequency: 417, sefira: 'gevurah', element: 'fogo' },
        T9: { frequency: 396, sefira: 'tiferet', element: 'sol' },
        T10: { frequency: 285, sefira: 'netzach', element: 'vênus' },
        T11: { frequency: 174, sefira: 'hod', element: 'mercúrio' },
        T12: { frequency: 963, sefira: 'yesod', element: 'lua' }
    },
    lumbar: {
        L1: { frequency: 852, sefira: 'malchut', element: 'terra' },
        L2: { frequency: 741, sefira: 'keter', element: 'éter' },
        L3: { frequency: 639, sefira: 'chokmah', element: 'ar' },
        L4: { frequency: 528, sefira: 'binah', element: 'terra' },
        L5: { frequency: 417, sefira: 'chesed', element: 'água' }
    }
};

// Função principal de codificação espinal
function encodeSpinalMovement(spinalSegment) {
    const [region, segment] = parseSpinalSegment(spinalSegment);
    const segmentData = spinalMap[region][segment];
    
    if (!segmentData) {
        console.error('Segmento espinal não encontrado:', spinalSegment);
        return null;
    }
    
    return {
        segment: spinalSegment,
        frequency: segmentData.frequency,
        sefira: segmentData.sefira,
        element: segmentData.element,
        pattern: generateSpinalPattern(segment, region),
        harmonics: generateHarmonics(segmentData.frequency)
    };
}

// Parse segmento espinal
function parseSpinalSegment(segment) {
    const match = segment.match(/^([CTL])(\d+)$/);
    if (!match) {
        throw new Error('Formato de segmento inválido. Use C1-C7, T1-T12, ou L1-L5');
    }
    
    const region = {
        'C': 'cervical',
        'T': 'thoracic',
        'L': 'lumbar'
    }[match[1]];
    
    return [region, segment];
}

// Gerar padrão espinal
function generateSpinalPattern(segment, region) {
    const patterns = {
        cervical: [1, 0, 1, 0, 1, 0, 1],
        thoracic: [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        lumbar: [1, 0, 1, 0, 1]
    };
    
    const segmentIndex = parseInt(segment.substring(1)) - 1;
    return patterns[region][segmentIndex] || 0;
}

// Gerar harmônicos
function generateHarmonics(baseFreq) {
    return [
        baseFreq,
        baseFreq * 1.5,
        baseFreq * 2,
        baseFreq * 2.5,
        baseFreq * 3
    ];
}

// Mapear região completa
function mapSpinalRegion(region) {
    const regionData = spinalMap[region];
    if (!regionData) {
        console.error('Região espinal não encontrada:', region);
        return null;
    }
    
    return Object.keys(regionData).map(segment => ({
        segment: segment,
        ...regionData[segment]
    }));
}

// Calcular frequência média de uma região
function calculateRegionFrequency(region) {
    const regionData = spinalMap[region];
    if (!regionData) return 0;
    
    const frequencies = Object.values(regionData).map(data => data.frequency);
    return frequencies.reduce((sum, freq) => sum + freq, 0) / frequencies.length;
}

// Exportar funções para uso global
if (typeof window !== 'undefined') {
    window.encodeSpinalMovement = encodeSpinalMovement;
    window.mapSpinalRegion = mapSpinalRegion;
    window.calculateRegionFrequency = calculateRegionFrequency;
}

// Para uso em Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        encodeSpinalMovement,
        mapSpinalRegion,
        calculateRegionFrequency,
        spinalMap
    };
}
