/**
 * Testes para o módulo de Controle Oracular
 */

import { assertEquals, assertExists, assertArrayIncludes } from "https://deno.land/std/testing/asserts.ts";
import { spy, assertSpyCalled, assertSpyCallArgs } from "https://deno.land/std/testing/mock.ts";

// Mocks para as dependências
const knowledgeBaseMock = {
  loadSources: async () => {},
  queryKnowledge: async (query) => ({
    passages: [{ source: "liber777", content: "Texto de teste" }],
    correlations: { sefirah: "tiferet" },
    suggestedPractices: [{ type: "meditation", description: "Meditação solar" }]
  })
};

const sigilGeneratorMock = {
  generateSigil: async (intention) => "data:image/png;base64,MOCK_SIGIL"
};

// Classe de teste para o Controle Oracular
Deno.test("OracularControl - Criar instância", () => {
  // Substituir dependências por mocks
  const control = new OracularControl();
  control.knowledgeBase = knowledgeBaseMock;
  control.sigilGenerator = sigilGeneratorMock;
  
  // Verificar propriedades iniciais
  assertExists(control.readings);
  assertExists(control.patterns);
  assertExists(control.subscribers);
  assertEquals(control.readings.length, 0);
  assertEquals(control.subscribers.size, 0);
});

Deno.test("OracularControl - Inicializar", async () => {
  const control = new OracularControl();
  
  // Sobrescrever métodos para teste
  control.knowledgeBase = knowledgeBaseMock;
  control.setupEventListeners = () => {};
  control.setupWebSocket = () => {};
  control.startPatternDetection = () => {};
  
  await control.initialize();
  
  // Nenhuma exceção deve ser lançada
  assertEquals(true, true);
});

Deno.test("OracularControl - Realizar leitura", async () => {
  const control = new OracularControl();
  
  // Sobrescrever dependências e métodos
  control.knowledgeBase = knowledgeBaseMock;
  control.sigilGenerator = sigilGeneratorMock;
  control.detectPatterns = () => ["padrão de teste"];
  control.updateDashboard = () => {};
  
  const query = "Como alcançar equilíbrio espiritual?";
  const reading = await control.performReading(query);
  
  // Verificar resultado da leitura
  assertExists(reading);
  assertEquals(reading.query, query);
  assertExists(reading.knowledge);
  assertExists(reading.sigil);
  assertExists(reading.patterns);
  assertArrayIncludes(reading.patterns, ["padrão de teste"]);
  
  // Deve ter adicionado a leitura ao histórico
  assertEquals(control.readings.length, 1);
  assertEquals(control.readings[0], reading);
});

Deno.test("OracularControl - Sistema de alertas", () => {
  const control = new OracularControl();
  
  // Criar uma função de callback para teste
  const callbackFn = spy(() => {});
  
  // Assinar para alertas
  control.subscribeToAlerts(callbackFn);
  assertEquals(control.subscribers.size, 1);
  
  // Disparar um alerta
  const alert = { type: "test", message: "Alerta de teste" };
  control.notifySubscribers(alert);
  
  // Verificar se o callback foi chamado com o alerta
  assertSpyCalled(callbackFn);
  assertSpyCallArgs(callbackFn, 0, [alert]);
  
  // Cancelar assinatura
  control.unsubscribeFromAlerts(callbackFn);
  assertEquals(control.subscribers.size, 0);
});

Deno.test("OracularControl - Exportar e importar dados", () => {
  const control = new OracularControl();
  
  // Adicionar algumas leituras de teste
  control.readings = [
    {
      timestamp: new Date("2025-08-19T12:00:00"),
      query: "Teste 1",
      knowledge: {},
      sigil: "data:image/png;base64,TEST1",
      patterns: ["padrão 1"]
    },
    {
      timestamp: new Date("2025-08-20T12:00:00"),
      query: "Teste 2",
      knowledge: {},
      sigil: "data:image/png;base64,TEST2",
      patterns: ["padrão 2"]
    }
  ];
  
  // Adicionar alguns padrões
  control.patterns = new Map([
    ["padrão 1", { count: 3, lastSeen: new Date() }],
    ["padrão 2", { count: 1, lastSeen: new Date() }]
  ]);
  
  // Exportar dados
  const exported = control.exportData();
  
  // Verificar dados exportados
  assertExists(exported.readings);
  assertExists(exported.patterns);
  assertExists(exported.timestamp);
  assertEquals(exported.readings.length, 2);
  assertEquals(exported.patterns.length, 2);
  
  // Criar nova instância e importar dados
  const newControl = new OracularControl();
  newControl.updateDashboard = () => {}; // mock
  
  newControl.importData(exported);
  
  // Verificar dados importados
  assertEquals(newControl.readings.length, 2);
  assertEquals(newControl.patterns.size, 2);
  assertEquals(newControl.readings[0].query, "Teste 1");
  assertEquals(newControl.readings[1].query, "Teste 2");
});
