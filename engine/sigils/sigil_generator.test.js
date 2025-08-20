/**
 * Testes para o módulo de Gerador de Sigilos
 */

import { assertEquals, assertExists, assertStringIncludes } from "https://deno.land/std/testing/asserts.ts";

// Mock da API crypto para testes
const cryptoMock = {
  subtle: {
    digest: async (algorithm, data) => {
      // Retornar um array buffer fixo para testes
      return new Uint8Array([
        0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
        0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10,
        0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
        0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10
      ]).buffer;
    }
  }
};

// Mock do canvas para testes
class CanvasMock {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }
  
  getContext() {
    return {
      strokeStyle: '',
      lineWidth: 0,
      fillStyle: '',
      beginPath: () => {},
      moveTo: () => {},
      lineTo: () => {},
      arc: () => {},
      closePath: () => {},
      stroke: () => {},
      fill: () => {},
      font: '',
      fillText: () => {}
    };
  }
  
  toDataURL() {
    return 'data:image/png;base64,MOCK_DATA';
  }
}

// Classe de teste para o Gerador de Sigilos
Deno.test("SigilGenerator - Criar instância", () => {
  const generator = new SigilGenerator();
  
  // Verificar propriedades iniciais
  assertEquals(generator.gridSize, 9);
  assertExists(generator.elements.fire);
  assertExists(generator.elements.water);
  assertExists(generator.elements.air);
  assertExists(generator.elements.earth);
  assertExists(generator.elements.spirit);
});

Deno.test("SigilGenerator - Gerar sigilo", async () => {
  const generator = new SigilGenerator();
  
  // Substituir crypto global com o mock
  const originalCrypto = globalThis.crypto;
  globalThis.crypto = cryptoMock;
  
  // Substituir criação de canvas
  generator._createCanvas = () => new CanvasMock(500, 500);
  
  // Testar geração de sigilo
  const sigil = await generator.generateSigil("Proteção e prosperidade");
  
  // Restaurar crypto original
  globalThis.crypto = originalCrypto;
  
  // Verificar resultado
  assertExists(sigil);
  assertStringIncludes(sigil, 'data:image/png;base64');
});

Deno.test("SigilGenerator - Criar grid", () => {
  const generator = new SigilGenerator();
  
  // Criar array de hash fixo para teste
  const hashArray = [
    0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
    0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10
  ];
  
  const grid = generator._createGrid(hashArray);
  
  // Verificar dimensões do grid
  assertEquals(grid.length, 9);
  assertEquals(grid[0].length, 9);
  
  // Verificar que alguns pontos foram ativados
  let activatedCount = 0;
  grid.forEach(row => {
    row.forEach(cell => {
      if (cell) activatedCount++;
    });
  });
  
  // Deve haver pelo menos alguns pontos ativos
  assertTrue(activatedCount > 0);
});

Deno.test("SigilGenerator - Obter tipo de elemento", () => {
  const generator = new SigilGenerator();
  
  // Testar mapeamento para diferentes bytes
  const elementTypes = [
    generator._getElementType(0),
    generator._getElementType(1),
    generator._getElementType(2),
    generator._getElementType(3),
    generator._getElementType(4)
  ];
  
  // Verificar que retorna tipos válidos
  elementTypes.forEach(type => {
    assertExists(generator.elements[type]);
  });
  
  // Verificar que os tipos são distintos (baseado no valor do byte)
  assertEquals(elementTypes[0], 'fire');
  assertEquals(elementTypes[1], 'water');
  assertEquals(elementTypes[2], 'air');
  assertEquals(elementTypes[3], 'earth');
  assertEquals(elementTypes[4], 'spirit');
});

// Função auxiliar para o teste
function assertTrue(condition) {
  assertEquals(condition, true);
}
