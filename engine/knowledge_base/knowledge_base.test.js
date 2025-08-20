/**
 * Testes para o módulo de Base de Conhecimento Esotérica
 */

// Importa biblioteca de testes Deno
import { assertEquals, assertExists } from "https://deno.land/std/testing/asserts.ts";

// Importar o módulo de integração enochiana
import "./enochian_integration.js";

// Mock de dados para testes
const mockData = {
  liber777: {
    correspondences: [
      {
        sefirah: "keter",
        godName: "Eheieh",
        element: "Primordial Air",
        planet: null
      },
      {
        sefirah: "chokmah",
        godName: "Yah",
        element: "Zodiac",
        planet: "Uranus"
      }
    ]
  },
  claviculaSalomonis: {
    pentacles: [
      {
        name: "First Pentacle of Saturn",
        purpose: "Protection against evil",
        description: "This pentacle is suitable for protection..."
      }
    ],
    invocations: [
      {
        spirit: "Cassiel",
        day: "Saturday",
        hour: "First hour of Saturn",
        incense: "Asafoetida"
      }
    ]
  }
};

// Classe de teste para a Base de Conhecimento
Deno.test("EsotericKnowledgeBase - Carregar fontes", async () => {
  const kb = new EsotericKnowledgeBase();
  
  // Sobrescrever método loadSources para usar dados de teste
  kb.loadSources = async () => {
    kb.sources = {
      liber777: mockData.liber777,
      claviculaSalomonis: mockData.claviculaSalomonis,
      seferYetzirah: {} // mock vazio
    };
    kb._buildCorrelations();
  };
  
  await kb.loadSources();
  
  // Verificar se os dados foram carregados
  assertExists(kb.sources.liber777);
  assertExists(kb.sources.claviculaSalomonis);
  
  // Verificar se as correlações foram construídas
  assertExists(kb.correlations);
});

Deno.test("EsotericKnowledgeBase - Consultar conhecimento", async () => {
  const kb = new EsotericKnowledgeBase();
  
  // Sobrescrever métodos necessários
  kb.loadSources = async () => {
    kb.sources = {
      liber777: mockData.liber777,
      claviculaSalomonis: mockData.claviculaSalomonis,
      seferYetzirah: {} // mock vazio
    };
    kb._buildCorrelations();
  };
  
  kb._semanticSearch = async (query) => {
    // Simular retorno de busca semântica
    return [
      {
        source: "liber777",
        content: "The sefirah of Keter corresponds to Primordial Air..."
      }
    ];
  };
  
  kb._findCorrelations = (passages) => {
    // Simular correlações encontradas
    return {
      sefirah: "keter",
      element: "Primordial Air",
      godName: "Eheieh"
    };
  };
  
  kb._suggestPractices = (correlations) => {
    // Simular práticas sugeridas
    return [
      {
        type: "meditation",
        description: "Meditação na Coroa cósmica",
        duration: "20 minutos"
      }
    ];
  };
  
  await kb.loadSources();
  const result = await kb.queryKnowledge("O que é Keter?");
  
  // Verificar resultado da consulta
  assertExists(result.passages);
  assertExists(result.correlations);
  assertExists(result.suggestedPractices);
  assertEquals(result.passages.length, 1);
  assertEquals(result.passages[0].source, "liber777");
});

Deno.test("EsotericKnowledgeBase - Gerar ritual", async () => {
  const kb = new EsotericKnowledgeBase();
  
  // Sobrescrever métodos necessários
  kb.loadSources = async () => {
    kb.sources = mockData;
    kb._buildCorrelations();
  };
  
  kb._analyzeIntention = async (intention) => {
    // Simular análise da intenção
    return {
      purpose: "protection",
      elements: ["earth", "fire"],
      planetary: "saturn",
      crystals: ["obsidian"]
    };
  };
  
  kb._constructRitual = (components) => {
    // Simular construção do ritual
    return {
      title: "Ritual de Proteção Saturnina",
      preparations: ["Incenso de Asafoetida", "Cristal de Obsidiana"],
      steps: [
        "Trace o pentagrama da terra nos quatro quadrantes",
        "Invoque Cassiel com a conjuração apropriada",
        "Visualize uma esfera de proteção obsidiana"
      ],
      closing: "Agradeça às forças evocadas e feche o círculo"
    };
  };
  
  await kb.loadSources();
  const ritual = await kb.generateRitual("Proteger minha casa");
  
  // Verificar resultado do ritual
  assertExists(ritual.title);
  assertExists(ritual.preparations);
  assertExists(ritual.steps);
  assertEquals(ritual.title, "Ritual de Proteção Saturnina");
  assertEquals(ritual.steps.length, 3);
});

// Testes para a integração enochiana
Deno.test("EsotericKnowledgeBase - Integração Enochiana", async () => {
  const kb = new EsotericKnowledgeBase();
  
  // Simular inicialização da integração enochiana
  kb.loadSources = async () => {
    kb.sources = {
      liber777: {},
      claviculaSalomonis: {},
      seferYetzirah: {},
      enochian: {}
    };
    kb.enochianIntegration = new EnochianSCIIIntegration();
  };
  
  await kb.loadSources();
  
  // Verificar se a integração enochiana foi inicializada
  assertExists(kb.enochianIntegration);
  
  // Testar tradução de fórmula
  const formula = kb.translateEnochianFormula("Aura de Cura");
  assertExists(formula);
  assertEquals(formula.name.includes("Aura de Cura"), true);
  
  // Testar obtenção do mapa de correspondências
  const map = kb.getEnochianCorrespondenceMap();
  assertExists(map.synoticMap);
  assertExists(map.enochianStructure);
  
  // Testar geração de prática integrativa
  const practice = kb.generateIntegrativePractice("Necessito de proteção");
  assertExists(practice);
  assertEquals(practice.type, "proteção");
  assertExists(practice.systems.enochian);
  assertExists(practice.systems.scii);
  assertExists(practice.systems.quimbanda);
});
