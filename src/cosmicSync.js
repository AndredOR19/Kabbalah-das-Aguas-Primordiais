class _CosmicSync {
    constructor() {
        this.currentParasha = null;
        this.currentYear = 5785;
        this.parashiotData = null;
    }

    async loadParashiotData() {
        try {
            const response = await fetch('data/parashiot.json');
            const data = await response.json();
            this.parashiotData = data[this.currentYear.toString()];
            return this.parashiotData;
        } catch (error) {
            console.error('Erro ao carregar dados de parashiot:', error);
            return null;
        }
    }

    getCurrentParasha() {
        const today = new Date();
        const todayStr = today.toISOString().split('T')[0];
        
        if (!this.parashiotData) return null;

        return this.parashiotData.find(parasha => {
            const [start, end] = parasha.data_gregoriana.split(' a ');
            return today >= new Date(start) && today <= new Date(end);
        });
    }
}
