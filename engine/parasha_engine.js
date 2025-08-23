/**
 * Placeholder legado para ParashaEngine.
 * A lógica de Parashá foi consolidada em CosmicEngine (engine/cosmic_sync.js).
 * Este arquivo evita erro 404 no carregamento do GitHub Pages e mantém compatibilidade.
 */
(function (global) {
  if (global.ParashaEngine) return;

  function ParashaEngine() {
    console.warn('[ParashaEngine] Placeholder carregado. Utilize CosmicEngine em engine/cosmic_sync.js');

    // Encaminha para o CosmicEngine quando disponível
    this.loadCurrentParasha = async function () {
      if (global.cosmicEngine && typeof global.cosmicEngine.loadCurrentParasha === 'function') {
        try {
          return await global.cosmicEngine.loadCurrentParasha();
        } catch (e) {
          console.error('[ParashaEngine] Erro ao delegar para CosmicEngine:', e);
        }
      }
      return null;
    };

    this.generateTikunSequence = function (parasha) {
      if (global.cosmicEngine && typeof global.cosmicEngine.generateTikunSequence === 'function') {
        return global.cosmicEngine.generateTikunSequence(parasha);
      }
      return null;
    };
  }

  // Expõe no escopo global (compatível com tag <script>)
  global.ParashaEngine = ParashaEngine;
})(typeof window !== 'undefined' ? window : this);
