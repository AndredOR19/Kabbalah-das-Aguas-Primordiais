// Protocolo Vivaldi - Player Logic and Core Functionality

// Global variables
let currentFrequency = 528;
let currentSeason = 'inverno';
let activeSefira = 'tiferet';
let spinalMapping = 'T5-T7';

// Frequency mappings for seasons
const seasonFrequencies = {
    primavera: 396,
    estate: 417,
    autunno: 528,
    inverno: 639
};

// Sefirot mappings
const sefirotMappings = {
    keter: { frequency: 963, spinal: 'C1-C2', element: 'Coroa' },
    chokmah: { frequency: 852, spinal: 'C3-C4', element: 'Sabedoria' },
    binah: { frequency: 741, spinal: 'C5-C6', element: 'Entendimento' },
    chesed: { frequency: 639, spinal: 'T1-T2', element: 'Misericórdia' },
    gevurah: { frequency: 528, spinal: 'T3-T4', element: 'Severidade' },
    tiferet: { frequency: 417, spinal: 'T5-T7', element: 'Beleza' },
    netzach: { frequency: 396, spinal: 'T8-T9', element: 'Vitória' },
    hod: { frequency: 285, spinal: 'T10-T11', element: 'Esplendor' },
    yesod: { frequency: 174, spinal: 'T12-L1', element: 'Fundação' },
    malchut: { frequency: 63, spinal: 'L2-L5', element: 'Reino' }
};

// Initialize player
function initVortexVisualization() {
    console.log('Vortex Player initialized');
    updateFrequencyDisplay(currentFrequency);
    updateSeasonDisplay(currentSeason);
    updateSefiraDisplay(activeSefira);
}

// Update frequency display
function updateFrequencyDisplay(frequency) {
    currentFrequency = frequency;
    document.getElementById('freq-value').textContent = frequency + ' Hz';
    document.getElementById('current-freq').textContent = frequency + ' Hz';
}

// Update season display
function updateSeasonDisplay(season) {
    currentSeason = season;
    document.getElementById('current-season').textContent = 'Estação: ' + season.toUpperCase();
    updateFrequencyDisplay(seasonFrequencies[season]);
}

// Update sefira display
function updateSefiraDisplay(sefira) {
    activeSefira = sefira;
    const sefiraData = sefirotMappings[sefira];
    document.getElementById('active-sefira').textContent = sefira.charAt(0).toUpperCase() + sefira.slice(1) + ' Ativa';
    document.getElementById('spinal-mapping').textContent = sefiraData.spinal + ': ' + sefiraData.element;
}

// Encode spinal movement
function encodeSpinalMovement(spinalSegment) {
    const [start, end] = spinalSegment.split('-');
    const startNum = parseInt(start.substring(1));
    const endNum = parseInt(end.substring(1));
    
    return {
        frequency: 396 + ((startNum + endNum) * 11),
        pattern: generateDNAPattern(startNum, endNum),
        spinal: spinalSegment
    };
}

// Generate DNA pattern
function generateDNAPattern(start, end) {
    const pattern = [];
    for (let i = start; i <= end; i++) {
        pattern.push({
            base: ['A', 'T', 'C', 'G'][i % 4],
            frequency: 396 + (i * 11),
            position: i
        });
    }
    return pattern;
}

// Activate DNA visualization
function activateDNAVisualization(pattern) {
    console.log('Activating DNA visualization with pattern:', pattern);
    // Implementation for DNA visualization
}

// Update frequency display
function updateFrequencyDisplay(frequency) {
    document.getElementById('freq-value').textContent = frequency + ' Hz';
}

// Generate thunder harmonic
function generateThunderHarmonic() {
    const baseFreq = currentFrequency;
    const harmonics = [baseFreq, baseFreq * 1.5, baseFreq * 2, baseFreq * 2.5];
    
    console.log('Generating thunder harmonics:', harmonics);
    
    // Implementation for thunder generation
    harmonics.forEach((freq, index) => {
        console.log(`Thunder harmonic ${index + 1}: ${freq} Hz`);
    });
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    initVortexVisualization();
});
