/**
 * Sistema de Geração de Sigilos Digitais
 * Usa hash SHA256 para criar sigilos baseados em análises
 */

class SigilGenerator {
    constructor() {
        this.gridSize = 9; // Grid 9x9 para complexidade adequada
        this.elements = {
            fire: ['triangle', 'upward-arrow'],
            water: ['crescent', 'wave'],
            air: ['circle', 'spiral'],
            earth: ['square', 'cross'],
            spirit: ['pentagram', 'hexagram']
        };
    }

    async generateSigil(intention) {
        try {
            // Gerar hash da intenção
            const encoder = new TextEncoder();
            const data = encoder.encode(intention);
            const hashBuffer = await crypto.subtle.digest('SHA-256', data);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            
            // Transformar hash em elementos visuais
            return this._transformHashToSigil(hashArray);
            
        } catch (error) {
            console.error('Erro ao gerar sigilo:', error);
            return null;
        }
    }

    _transformHashToSigil(hashArray) {
        const canvas = document.createElement('canvas');
        canvas.width = 500;
        canvas.height = 500;
        const ctx = canvas.getContext('2d');
        
        // Configurar estilo base
        ctx.strokeStyle = '#1a1a1a';
        ctx.lineWidth = 2;
        ctx.fillStyle = 'rgba(26, 26, 26, 0.1)';
        
        // Criar grid
        const grid = this._createGrid(hashArray);
        
        // Desenhar elementos baseados no hash
        this._drawElements(ctx, grid, hashArray);
        
        // Adicionar elementos planetários
        this._addPlanetaryInfluences(ctx, hashArray);
        
        return canvas.toDataURL();
    }

    _createGrid(hashArray) {
        const grid = Array(this.gridSize).fill().map(() => 
            Array(this.gridSize).fill(false)
        );
        
        // Usar bytes do hash para ativar pontos no grid
        for (let i = 0; i < hashArray.length; i += 2) {
            const x = hashArray[i] % this.gridSize;
            const y = hashArray[i + 1] % this.gridSize;
            grid[y][x] = true;
        }
        
        return grid;
    }

    _drawElements(ctx, grid, hashArray) {
        const cellSize = 500 / this.gridSize;
        
        grid.forEach((row, y) => {
            row.forEach((active, x) => {
                if (active) {
                    const elementType = this._getElementType(hashArray[y * this.gridSize + x]);
                    this._drawElement(ctx, x * cellSize, y * cellSize, cellSize, elementType);
                }
            });
        });
    }

    _getElementType(byte) {
        const elements = ['fire', 'water', 'air', 'earth', 'spirit'];
        return elements[byte % elements.length];
    }

    _drawElement(ctx, x, y, size, elementType) {
        const shapes = this.elements[elementType];
        const shape = shapes[Math.floor(Math.random() * shapes.length)];
        
        switch (shape) {
            case 'triangle':
                this._drawTriangle(ctx, x, y, size);
                break;
            case 'circle':
                this._drawCircle(ctx, x, y, size);
                break;
            // ... outros casos
        }
    }

    _addPlanetaryInfluences(ctx, hashArray) {
        const planetarySymbols = ['☉', '☽', '☿', '♀', '♂', '♃', '♄'];
        const byte = hashArray[0];
        const symbol = planetarySymbols[byte % planetarySymbols.length];
        
        ctx.font = '30px Arial';
        ctx.fillText(symbol, 250, 250);
    }

    async animateSigil(sigilDataUrl) {
        // Implementar animação do sigilo
        // Pode usar Three.js ou WebGL
    }

    _drawTriangle(ctx, x, y, size) {
        ctx.beginPath();
        ctx.moveTo(x + size/2, y);
        ctx.lineTo(x + size, y + size);
        ctx.lineTo(x, y + size);
        ctx.closePath();
        ctx.stroke();
        ctx.fill();
    }

    _drawCircle(ctx, x, y, size) {
        ctx.beginPath();
        ctx.arc(x + size/2, y + size/2, size/2, 0, Math.PI * 2);
        ctx.closePath();
        ctx.stroke();
        ctx.fill();
    }
}

// Export para uso global
globalThis.SigilGenerator = SigilGenerator;
