/**
 * Classe Menu - Implementa um menu dinâmico para o sistema Kabbalah das Águas Primordiais
 * 
 * Esta classe cria e gerencia um menu interativo que:
 * - Renderiza uma estrutura hierárquica de navegação
 * - Suporta submenus para categorias principais
 * - Atualiza estados ativos automaticamente
 * - Gerencia eventos de interação do usuário
 */
class Menu {
    /**
     * Construtor da classe Menu
     * @param {string} containerId - ID do elemento HTML que conterá o menu
     */
    constructor(containerId) {
        // Elemento DOM principal que conterá o menu
        this.container = document.getElementById(containerId);
        
        // Estrutura de dados que define os itens do menu
        this.items = [
            {
                id: 'inicio',
                title: 'Início',
                link: '/',
                description: 'Página inicial do Corpo do Verbo'
            },
            {
                id: 'metodo',
                title: 'O Método',
                link: '#metodo',
                description: 'Fundamentos filosóficos e teóricos',
                submenu: [
                    { 
                        id: 'visao',
                        title: 'A Visão',
                        link: '/documentos/textos-fundamentais/manifesto.md',
                        description: 'O manifesto e propósito do Corpo do Verbo'
                    },
                    { 
                        id: 'scii',
                        title: 'SCII',
                        link: '/SCII 5.0/',
                        description: 'Sistema de Correspondência Integrada e Inteligente'
                    },
                    { 
                        id: 'corpo-somatico',
                        title: 'O Corpo Somático',
                        link: '/diagramas/letras_hebraicas_pontos_corporais.md',
                        description: 'O conceito central das letras no corpo'
                    }
                ]
            },
            {
                id: 'biblioteca',
                title: 'A Biblioteca do Verbo',
                link: '#biblioteca',
                description: 'Arquivo sagrado de conhecimento',
                submenu: [
                    { 
                        id: 'textos',
                        title: 'Textos Fundamentais',
                        link: '/documentos/textos-fundamentais',
                        description: 'Artigos, teses e dissertações'
                    },
                    { 
                        id: 'diagramas',
                        title: 'Diagramas e Selos',
                        link: '/diagramas',
                        description: 'Representações visuais e selos sagrados'
                    },
                    { 
                        id: 'protocolos',
                        title: 'Protocolos Operativos',
                        link: '/Protocolos',
                        description: 'Instruções práticas e rituais'
                    }
                ]
            },
            {
                id: 'praxis',
                title: 'Práxis',
                link: '#praxis',
                description: 'Aplicação prática do conhecimento',
                submenu: [
                    { 
                        id: 'oraculo',
                        title: 'O Oráculo Encarnado',
                        link: '/ORACULO-APP',
                        description: 'Aplicação interativa do oráculo'
                    },
                    { 
                        id: 'praticas',
                        title: 'Práticas e Rituais',
                        link: '/Livro_do_Templo_Interno',
                        description: 'Guias para danças, meditações e exercícios somáticos'
                    }
                ]
            },
            {
                id: 'blog',
                title: 'Blog',
                link: 'https://kabbalahdasaguasprimordiais.blogspot.com/',
                description: 'Kabbalah das Águas Primordiais'
            },
            {
                id: 'contato',
                title: 'Contato',
                link: '#contato',
                description: 'Entre em contato conosco'
            }
        ];
        
        this.init();
    }
    
    /**
     * Inicializa o menu e configura a atualização automática
     * @private
     */
    init() {
        this.render();
        // Configura atualização periódica do estado ativo
        this._startAutoUpdate();
    }

    /**
     * Configura o intervalo de atualização automática do menu
     * @private
     */
    _startAutoUpdate() {
        const UPDATE_INTERVAL = 8000; // 8 segundos
        this._updateInterval = setInterval(() => this._atualizarMenu(), UPDATE_INTERVAL);
    }
    
    /**
     * Renderiza o menu completo com todos os seus itens e submenus
     * @public
     */
    render() {
        const menuHTML = this._generateMenuHTML();
        this.container.innerHTML = menuHTML;
        this._setupEventListeners();
    }

    /**
     * Gera a estrutura HTML do menu
     * @private
     * @returns {string} HTML do menu
     */
    _generateMenuHTML() {
        return `
            <nav class="menu" role="navigation" aria-label="Menu principal">
                <ul>
                    ${this.items.map(item => this._generateMenuItem(item)).join('')}
                </ul>
            </nav>
        `;
    }

    /**
     * Gera o HTML para um item específico do menu
     * @private
     * @param {Object} item - Item do menu
     * @returns {string} HTML do item
     */
    _generateMenuItem(item) {
        const hasSubmenu = item.submenu && item.submenu.length > 0;
        return `
            <li class="menu-item ${hasSubmenu ? 'has-submenu' : ''}" 
                data-id="${item.id}"
                role="menuitem"
                ${hasSubmenu ? 'aria-haspopup="true"' : ''}
                aria-label="${item.description || item.title}">
                <a href="${item.link}" 
                   class="menu-link"
                   ${item.active ? 'aria-current="page"' : ''}>
                    ${item.title}
                    ${hasSubmenu ? '<span class="submenu-indicator">▾</span>' : ''}
                </a>
                ${hasSubmenu ? this._generateSubmenu(item.submenu) : ''}
            </li>
        `;
    }

    /**
     * Gera o HTML para um submenu
     * @private
     * @param {Array} submenu - Array de itens do submenu
     * @returns {string} HTML do submenu
     */
    _generateSubmenu(submenu) {
        return `
            <ul class="submenu" 
                role="menu" 
                aria-label="Submenu">
                ${submenu.map(subItem => `
                    <li class="submenu-item"
                        data-id="${subItem.id}"
                        role="menuitem">
                        <a href="${subItem.link}" 
                           class="submenu-link"
                           title="${subItem.description || subItem.title}">
                            ${subItem.title}
                        </a>
                    </li>
                `).join('')}
            </ul>
        `;
    }

    /**
     * Configura os event listeners para interatividade do menu
     * @private
     */
    _setupEventListeners() {
        // Event delegation para melhor performance
        this.container.addEventListener('click', (e) => {
            const link = e.target.closest('a');
            if (!link) return;

            const href = link.getAttribute('href');
            if (href === '#') {
                e.preventDefault();
                this._toggleSubmenu(link.parentElement);
            }
        });

        // Adiciona suporte a navegação por teclado
        this._setupKeyboardNavigation();
    }

    /**
     * Configura navegação por teclado para acessibilidade
     * @private
     */
    _setupKeyboardNavigation() {
        this.container.addEventListener('keydown', (e) => {
            const item = e.target.closest('li');
            if (!item) return;

            switch(e.key) {
                case 'Enter':
                case ' ':
                    e.preventDefault();
                    if (item.querySelector('.submenu')) {
                        this._toggleSubmenu(item);
                    }
                    break;
                case 'Escape':
                    const openSubmenu = item.querySelector('.submenu.active');
                    if (openSubmenu) {
                        this._toggleSubmenu(item, false);
                    }
                    break;
            }
        });
    }

    /**
     * Atualiza o estado ativo dos itens do menu
     * @private
     */
    _atualizarMenu() {
        const randomIndex = Math.floor(Math.random() * this.items.length);
        this.items.forEach((item, index) => {
            item.active = index === randomIndex;
        });
        this.render();
    }

    /**
     * Toggle do estado de submenu
     * @private
     * @param {HTMLElement} item - Elemento LI do menu
     * @param {boolean} [force] - Força um estado específico
     */
    _toggleSubmenu(item, force) {
        const submenu = item.querySelector('.submenu');
        if (submenu) {
            const isActive = force !== undefined ? force : !submenu.classList.contains('active');
            submenu.classList.toggle('active', isActive);
            item.setAttribute('aria-expanded', isActive);
        }
    }
}

/**
 * Inicializa o menu quando o DOM estiver completamente carregado
 * Isso garante que todos os elementos necessários estejam disponíveis
 */
window.addEventListener('DOMContentLoaded', () => {
    try {
        const menu = new Menu('menu-container');
        // Expõe a instância do menu globalmente para debugging se necessário
        window._menuInstance = menu;
    } catch (error) {
        console.error('Erro ao inicializar o menu:', error);
    }
});
