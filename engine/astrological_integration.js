/**
 * Sistema de Integração Astrológica - Águas Primordiais
 * Integra dados astrológicos com o sistema de Tikun
 */

class AstrologicalIntegration {
    constructor() {
        this.currentDate = new Date();
        this.planetPositions = {};
        this.natalChart = null;
    }

    // Calcula posição planetária para data específica
    calculatePlanetPositions(date) {
        const planets = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto'];
        const positions = {};

        planets.forEach(planet => {
            positions[planet] = this.getPlanetPosition(planet, date);
        });

        return positions;
    }

    getPlanetPosition(planet, date) {
        // Implementação simplificada - em produção usaria biblioteca astrológica
        const baseDate = new Date('2000-01-01');
        const daysSince = Math.floor((date - baseDate) / (1000 * 60 * 60 * 24));
        
        // Cálculo orbital simplificado
        const orbitalPeriods = {
            sun: 365.25,
            moon: 27.3,
            mercury: 87.97,
            venus: 224.7,
            mars: 686.98,
            jupiter: 4332.59,
            saturn: 10759.22,
            uranus: 30688.5,
            neptune: 60182,
            pluto: 90560
        };

        return (daysSince / orbitalPeriods[planet]) * 360 % 360;
    }

    // Calcula Tikun baseado em trânsitos planetários
    calculateTransitTikun(birthDate, currentDate) {
        const natalPositions = this.calculatePlanetPositions(birthDate);
        const currentPositions = this.calculatePlanetPositions(currentDate);
        
        const transits = this.findSignificantTransits(natalPositions, currentPositions);
        
        return {
            transits: transits,
            recommendedMantras: this.getMantrasForTransits(transits),
            affectedChakras: this.getAffectedChakras(transits)
        };
    }

    findSignificantTransits(natal, current) {
        const transits = [];
        const planets = Object.keys(natal);
        
        planets.forEach(planet => {
            const natalPos = natal[planet];
            const currentPos = current[planet];
            const aspect = Math.abs(currentPos - natalPos);
            
            if (aspect < 10 || aspect > 350) {
                transits.push({
                    planet: planet,
                    type: 'conjunction',
                    strength: 'strong'
                });
            } else if (aspect > 80 && aspect < 100) {
                transits.push({
                    planet: planet,
                    type: 'square',
                    strength: 'challenging'
                });
            } else if (aspect > 110 && aspect < 130) {
                transits.push({
                    planet: planet,
                    type: 'trine',
                    strength: 'harmonious'
                });
            }
        });
        
        return transits;
    }

    getMantrasForTransits(transits) {
        const mantraMap = {
            sun: ['אלהים', 'יהוה'],
            moon: ['שדי', 'אל שדי'],
            mercury: ['אלוהי ישראל', 'דבר יהוה'],
            venus: ['אהיה אשר אהיה', 'אל חי'],
            mars: ['אלהים צבאות', 'יהוה אלהים'],
            jupiter: ['אל', 'אל עליון'],
            saturn: ['אלהים', 'יהוה אלהים'],
            uranus: ['אלהים חיים', 'יהוה צבאות'],
            neptune: ['אלהים אמת', 'יהוה אלהים'],
            pluto: ['אלהים צבאות', 'יהוה אלהים']
        };

        const mantras = [];
        transits.forEach(transit => {
            if (mantraMap[transit.planet]) {
                mantras.push(...mantraMap[transit.planet]);
            }
        });
        
        return [...new Set(mantras)];
    }

    getAffectedChakras(transits) {
        const chakraMap = {
            sun: ['coroa', 'plexo'],
            moon: ['sacral', 'base'],
            mercury: ['garganta', 'terceiro-olho'],
            venus: ['coracao', 'sacral'],
            mars: ['base', 'plexo'],
            jupiter: ['coroa', 'garganta'],
            saturn: ['base', 'coroa'],
            uranus: ['terceiro-olho', 'coroa'],
            neptune: ['coroa', 'terceiro-olho'],
            pluto: ['base', 'coroa']
        };

        const chakras = new Set();
        transits.forEach(transit => {
            if (chakraMap[transit.planet]) {
                chakraMap[transit.planet].forEach(chakra => chakras.add(chakra));
            }
        });
        
        return Array.from(chakras);
    }

    // Gera visualização do mapa astral
    generateAstroChart(birthDate) {
        const positions = this.calculatePlanetPositions(birthDate);
        
        return {
            date: birthDate,
            positions: positions,
            houses: this.calculateHouses(birthDate),
            aspects: this.calculateAspects(positions)
        };
    }

    calculateHouses(date) {
        // Implementação simplificada de casas astrológicas
        const houses = [];
        for (let i = 1; i <= 12; i++) {
            houses.push({
                house: i,
                cusp: (i - 1) * 30,
                sign: this.getZodiacSign((i - 1) * 30)
            });
        }
        return houses;
    }

    calculateAspects(positions) {
        const aspects = [];
        const planets = Object.keys(positions);
        
        for (let i = 0; i < planets.length; i++) {
            for (let j = i + 1; j < planets.length; j++) {
                const aspect = Math.abs(positions[planets[i]] - positions[planets[j]]);
                if (aspect < 10 || aspect > 350) {
                    aspects.push({
                        planets: [planets[i], planets[j]],
                        type: 'conjunction',
                        orb: Math.min(aspect, 360 - aspect)
                    });
                }
            }
        }
        
        return aspects;
    }

    getZodiacSign(degree) {
        const signs = [
            'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
            'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
        ];
        return signs[Math.floor(degree / 30)];
    }

    // Interface para o sistema principal
    getAstrologicalTikun(birthDate, currentDate = new Date()) {
        return {
            natalChart: this.generateAstroChart(birthDate),
            currentTransits: this.calculateTransitTikun(birthDate, currentDate),
            dailyGuidance: this.getDailyGuidance(currentDate)
        };
    }

    getDailyGuidance(date) {
        const dayOfWeek = date.getDay();
        const guidance = {
            0: { sefirah: 'Malkuth', mantra: 'אדני', focus: 'manifestação' },
            1: { sefirah: 'Yesod', mantra: 'שדי', focus: 'fundação' },
            2: { sefirah: 'Hod', mantra: 'אלהים צבאות', focus: 'glória' },
            3: { sefirah: 'Netzach', mantra: 'יהוה צבאות', focus: 'vitória' },
            4: { sefirah: 'Tiferet', mantra: 'יהוה', focus: 'beleza' },
            5: { sefirah: 'Gevurah', mantra: 'אלהים', focus: 'força' },
            6: { sefirah: 'Chesed', mantra: 'אל', focus: 'misericórdia' }
        };
        
        return guidance[dayOfWeek];
    }
}

// Export para uso global
window.AstrologicalIntegration = AstrologicalIntegration;
