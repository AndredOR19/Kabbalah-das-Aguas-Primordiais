/**
 * Testes para o módulo de Integração Enochiana no SCII
 */

// Importa biblioteca de testes Deno
import { assertEquals, assertExists } from "https://deno.land/std/testing/asserts.ts";

// Importar o módulo de integração enochiana
import "../engine/knowledge_base/enochian_integration.js";

// Testes para a classe EnochianSCIIIntegration
Deno.test("EnochianSCIIIntegration - Inicialização", () => {
  const integration = new EnochianSCIIIntegration();
  
  // Verificar se as estruturas principais foram inicializadas
  assertExists(integration.enochianStructure);
  assertExists(integration.sciiCorrelations);
  assertExists(integration.quimbandaParallels);
  assertExists(integration.synoticMap);
  
  // Verificar estruturas enochianas
  assertEquals(integration.enochianStructure.alphabet.letters.length, 21);
  assertEquals(integration.enochianStructure.watchtowers.towers.length, 4);
  assertEquals(integration.enochianStructure.heptarchy.kings.length, 7);
  assertEquals(integration.enochianStructure.heptarchy.princes.length, 7);
  assertEquals(integration.enochianStructure.aethyrs.keyAethyrs.length, 8);
  assertEquals(integration.enochianStructure.operationalFormulas.formulas.length, 4);
  
  // Verificar correlações SCII
  assertEquals(integration.sciiCorrelations.alphabet.correlations.length, 21);
  assertEquals(integration.sciiCorrelations.structure.watchtowers.mapping.length, 4);
  assertEquals(integration.sciiCorrelations.structure.heptarchy.mapping.length, 7);
  
  // Verificar paralelos com Quimbanda
  assertEquals(integration.quimbandaParallels.parallels.length, 8);
  
  // Verificar mapa sinótico
  assertEquals(integration.synoticMap.elements.length, 6);
});

Deno.test("EnochianSCIIIntegration - Tradução de Fórmula", () => {
  const integration = new EnochianSCIIIntegration();
  
  // Testar tradução de fórmula existente
  const auraFormula = integration.translateFormula("Aura de Cura");
  assertExists(auraFormula);
  assertEquals(auraFormula.name.includes("Aura de Cura"), true);
  assertExists(auraFormula.sciiCircuit);
  assertExists(auraFormula.components);
  assertEquals(auraFormula.components.length, 4);
  
  // Testar tradução de fórmula inexistente
  const invalidFormula = integration.translateFormula("Fórmula Inexistente");
  assertExists(invalidFormula.error);
  assertExists(invalidFormula.suggestions);
  assertEquals(invalidFormula.suggestions.length, 4);
});

Deno.test("EnochianSCIIIntegration - Mapa de Correspondências", () => {
  const integration = new EnochianSCIIIntegration();
  
  // Obter mapa completo
  const map = integration.getCompleteCorrespondenceMap();
  
  // Verificar estrutura do mapa
  assertExists(map.synoticMap);
  assertExists(map.enochianStructure);
  assertExists(map.sciiCorrelations);
  assertExists(map.quimbandaParallels);
  
  // Verificar elementos específicos
  assertEquals(map.synoticMap.elements.some(e => e.category === "Linguagem"), true);
  assertEquals(map.synoticMap.elements.some(e => e.category === "Estrutura"), true);
  assertEquals(map.synoticMap.elements.some(e => e.category === "Operação"), true);
});

Deno.test("EnochianSCIIIntegration - Geração de Prática Integrativa", () => {
  const integration = new EnochianSCIIIntegration();
  
  // Testar geração de prática para cura
  const curaPratica = integration.generateIntegrativePractice("Necessito de cura energética");
  assertEquals(curaPratica.type, "cura");
  assertExists(curaPratica.systems.enochian);
  assertExists(curaPratica.systems.scii);
  assertExists(curaPratica.systems.quimbanda);
  assertEquals(curaPratica.systems.enochian.formula.includes("Aura de Cura"), true);
  
  // Testar geração de prática para proteção
  const protecaoPratica = integration.generateIntegrativePractice("Preciso de proteção espiritual");
  assertEquals(protecaoPratica.type, "proteção");
  assertEquals(protecaoPratica.systems.enochian.formula.includes("Escudo de Proteção"), true);
  
  // Testar geração de prática para sabedoria
  const sabedoriaPratica = integration.generateIntegrativePractice("Busco sabedoria espiritual");
  assertEquals(sabedoriaPratica.type, "sabedoria");
  assertEquals(sabedoriaPratica.systems.enochian.formula.includes("Porta de Sabedoria"), true);
  
  // Testar geração de prática para poder
  const poderPratica = integration.generateIntegrativePractice("Necessito ativar meu poder pessoal");
  assertEquals(poderPratica.type, "poder");
  assertEquals(poderPratica.systems.enochian.formula.includes("Toque de Fogo"), true);
  
  // Verificar estrutura comum nas práticas
  assertExists(curaPratica.integratedPractice);
  assertExists(curaPratica.integratedPractice.preparation);
  assertExists(curaPratica.integratedPractice.steps);
  assertExists(curaPratica.integratedPractice.closing);
  assertEquals(curaPratica.integratedPractice.steps.length, 7);
});
