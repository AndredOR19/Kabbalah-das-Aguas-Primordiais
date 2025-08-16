/**
 * Dashboard de Experiências - Águas Primordiais
 * Gerencia a visualização e análise das experiências registradas
 */

class ExperienceDashboard {
    constructor() {
        this.experiences = this.loadExperiences();
        this.renderDashboard();
    }

    loadExperiences() {
        return JSON.parse(localStorage.getItem('aguas_experiences') || '[]');
    }

    renderDashboard() {
        const dashboardContainer = document.createElement('div');
        dashboardContainer.id = 'experience-dashboard';
        dashboardContainer.innerHTML = '<h2>📜 Registro de Experiências</h2>';
        
        if (this.experiences.length === 0) {
            dashboardContainer.innerHTML += '<p>Nenhuma experiência registrada.</p>';
        } else {
            this.experiences.forEach(exp => {
                const expDiv = document.createElement('div');
                expDiv.className = 'experience-entry';
                expDiv.innerHTML = `
                    <p><strong>Data:</strong> ${new Date(exp.timestamp).toLocaleString()}</p>
                    <p><strong>Parashá:</strong> ${exp.parasha}</p>
                    <p><strong>Registro:</strong> ${exp.log}</p>
                `;
                dashboardContainer.appendChild(expDiv);
            });
        }

        document.body.appendChild(dashboardContainer);
    }
}

// Inicializa o dashboard ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    const dashboard = new ExperienceDashboard();
});
