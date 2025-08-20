class MantraPlayer {
    constructor() {
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, globalThis.innerWidth / globalThis.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        this.currentMantra = null;
        this.isPlaying = false;
        this.currentSyllable = 0;
        this.audioContext = null;
        
        this.init();
    }

    init() {
        this.renderer.setSize(globalThis.innerWidth * 0.7, globalThis.innerHeight * 0.6);
        document.getElementById('mantra-canvas').appendChild(this.renderer.domElement);
        
        // Iluminação mística
        const ambientLight = new THREE.AmbientLight(0x404040, 0.4);
        this.scene.add(ambientLight);
        
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(0, 10, 10);
        this.scene.add(directionalLight);
        
        this.camera.position.z = 15;
        
        // Inicializar Web Audio API
        this.audioContext = new (globalThis.AudioContext || globalThis.webkitAudioContext)();
    }

    async loadMantra(mantraData) {
        this.currentMantra = mantraData;
        this.currentSyllable = 0;
        this.createTextMesh();
        this.createParticleSystem();
    }

    createTextMesh() {
        if (this.textMesh) {
            this.scene.remove(this.textMesh);
        }
        
        // Criar texto 3D para o mantra
        const geometry = new THREE.PlaneGeometry(10, 2);
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.width = 512;
        canvas.height = 128;
        
        context.fillStyle = 'rgba(0, 0, 0, 0)';
        context.fillRect(0, 0, canvas.width, canvas.height);
        
        context.font = 'bold 48px Arial';
        context.fillStyle = '#7bdff2';
        context.textAlign = 'center';
        context.textBaseline = 'middle';
        context.fillText(this.currentMantra.fonemas[this.currentSyllable], canvas.width / 2, canvas.height / 2);
        
        const texture = new THREE.CanvasTexture(canvas);
        const material = new THREE.MeshBasicMaterial({ 
            map: texture, 
            transparent: true,
            side: THREE.DoubleSide
        });
        
        this.textMesh = new THREE.Mesh(geometry, material);
        this.scene.add(this.textMesh);
    }

    createParticleSystem() {
        if (this.particleSystem) {
            this.scene.remove(this.particleSystem);
        }
        
        const particleCount = 2000;
        const particles = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);
        const colors = new Float32Array(particleCount * 3);
        
        for (let i = 0; i < particleCount * 3; i += 3) {
            positions[i] = (Math.random() - 0.5) * 20;
            positions[i + 1] = (Math.random() - 0.5) * 20;
            positions[i + 2] = (Math.random() - 0.5) * 20;
            
            const color = new THREE.Color(this.currentMantra.cores[this.currentSyllable]);
            colors[i] = color.r;
            colors[i + 1] = color.g;
            colors[i + 2] = color.b;
        }
        
        particles.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        particles.setAttribute('color', new THREE.BufferAttribute(colors, 3));
        
        const particleMaterial = new THREE.PointsMaterial({
            size: 0.1,
            transparent: true,
            blending: THREE.AdditiveBlending,
            vertexColors: true
        });
        
        this.particleSystem = new THREE.Points(particles, particleMaterial);
        this.scene.add(this.particleSystem);
    }

    playTone(frequency, duration = 2000) {
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.type = 'sine';
        oscillator.frequency.value = frequency;
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.3, this.audioContext.currentTime + 0.1);
        gainNode.gain.linearRampToValueAtTime(0, this.audioContext.currentTime + duration / 1000);
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.start();
        oscillator.stop(this.audioContext.currentTime + duration / 1000);
    }

    activateChakra(chakraName) {
        const chakra = document.querySelector(`[data-chakra="${chakraName}"]`);
        if (chakra) {
            chakra.classList.add('active');
            setTimeout(() => chakra.classList.remove('active'), 3000);
        }
    }

    async playSequence(sequence) {
        if (!sequence || !this.currentMantra) return;
        
        this.isPlaying = true;
        
        for (let i = 0; i < this.currentMantra.fonemas.length; i++) {
            this.currentSyllable = i;
            this.createTextMesh();
            this.createParticleSystem();
            
            // Tocar frequência
            this.playTone(this.currentMantra.frequencia_base * (i + 1));
            
            // Ativar chakra correspondente
            if (this.currentMantra.corpo_alvo[i]) {
                this.activateChakra(this.currentMantra.corpo_alvo[i]);
            }
            
            await new Promise(resolve => setTimeout(resolve, 4000));
        }
        
        this.isPlaying = false;
    }

    animate() {
        if (!this.isPlaying) return;
        
        requestAnimationFrame(() => this.animate());
        
        // Animação das partículas
        if (this.particleSystem) {
            const positions = this.particleSystem.geometry.attributes.position.array;
            const time = Date.now() * 0.001;
            
            for (let i = 0; i < positions.length; i += 3) {
                positions[i] += Math.sin(time + i) * 0.01;
                positions[i + 1] += Math.cos(time * 0.7 + i) * 0.01;
            }
            
            this.particleSystem.geometry.attributes.position.needsUpdate = true;
        }
        
        // Pulsação do texto
        if (this.textMesh) {
            const scale = 1 + Math.sin(Date.now() * 0.003) * 0.1;
            this.textMesh.scale.set(scale, scale, scale);
        }
        
        this.renderer.render(this.scene, this.camera);
    }

    stopSequence() {
        this.isPlaying = false;
        if (this.audioContext) {
            this.audioContext.close();
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        }
    }
}

// Inicialização global
const _mantraPlayer = new MantraPlayer();
