class Menu {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.items = [
            {
                id: 1,
                title: 'Livro do Templo Interno',
                link: '#templo',
                submenu: [
                    { id: 'prefacio', title: 'Prefácio do Silêncio', link: '/Livro_do_Templo_Interno/01_Prefacio_do_Silencio.md' },
                    { id: 'chokmah', title: 'A Voz de Chokmah', link: '/Livro_do_Templo_Interno/02_A_Voz_de_Chokmah.md' },
                    { id: 'binah', title: 'A Resposta de Binah', link: '/Livro_do_Templo_Interno/03_A_Resposta_de_Binah.md' }
                ]
            },
            {
                id: 2,
                title: 'SCII Neural',
                link: '#scii-neural',
                submenu: [
                    { id: 'oracle', title: 'Oráculo Bot', link: '/SCII-NEURAL/ai/oracle_bot.py' },
                    { id: 'gematria', title: 'Gematria', link: '/SCII-NEURAL/core/gematria.py' },
                    { id: 'letters', title: 'Letras Hebraicas', link: '/SCII-NEURAL/data/hebrew_letters.json' }
                ]
            },
            {
                id: 3,
                title: 'Práticas Somáticas',
                link: '#praticas',
                submenu: [
                    { id: 'aleph', title: 'Aleph - O Sopro', link: '/zorar-operativo/praticas_somaticas/PRATICA_ALEPH_O_SOPRO_PARADOXAL.md' },
                    { id: 'bet', title: 'Bet - A Casa', link: '/zorar-operativo/praticas_somaticas/PRATICA_BET_A_CASA_DO_VERBO.md' },
                    { id: 'gimel', title: 'Gimel - O Camelo', link: '/zorar-operativo/praticas_somaticas/PRATICA_GIMEL_A_JORNADA_DO_CAMELO.md' }
                ]
            },
            {
                id: 4,
                title: 'Axiomas SCII',
                link: '#axiomas',
                submenu: [
                    { id: 'campo', title: 'Leitura de Campo', link: '/SCII_Corpo_Do_Verbo/axiomas/axioma_SCII-001_leitura_de_campo.json' },
                    { id: 'numero', title: 'Roupagens do Número', link: '/SCII_Corpo_Do_Verbo/axiomas/axioma_SCII-002_roupagens_do_numero.json' },
                    { id: 'matriz', title: 'Matriz Somática', link: '/SCII_Corpo_Do_Verbo/axiomas/axioma_SCII-005_matriz_somatica_letra.json' }
                ]
            },
            {
                id: 5,
                title: 'Zohar Operativo',
                link: '#zohar',
                submenu: [
                    { id: 'bereshit', title: 'Bereshit Comentado', link: '/zorar-operativo/comentarios-zohar/bereshit-comentado.md' },
                    { id: 'shemot', title: 'Shemot e a Luz', link: '/zorar-operativo/comentarios-zohar/shemot-e-a-luz-do-verbo.md' },
                    { id: 'portas', title: '231 Portas', link: '/zorar-operativo/letras/combinacoes/231-portas.md' }
                ]
            }
        ];
        
        this.init();
    }
    
    init() {
        this.render();
    }
    
    render() {
        const menuHTML = `
            <nav class="menu">
                <ul>
                    ${this.items.map(item => `
                        <li>
                            <a href="${item.link}">${item.title}</a>
                            ${item.submenu ? `
                                <ul class="submenu">
                                    ${item.submenu.map(subItem => `
                                        <li>
                                            <a href="${subItem.link}">${subItem.title}</a>
                                        </li>
                                    `).join('')}
                                </ul>
                            ` : ''}
                        </li>
                    `).join('')}
                </ul>
            </nav>
        `;
        
        this.container.innerHTML = menuHTML;
    }
}

window.addEventListener('DOMContentLoaded', () => {
    new Menu('menu-container');
});
