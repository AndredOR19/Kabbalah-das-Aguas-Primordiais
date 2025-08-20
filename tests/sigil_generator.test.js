import { assertEquals, assertExists, assert } from "https://deno.land/std/testing/asserts.ts";
import { SigilGenerator } from "../engine/sigils/sigil_generator.js";

Deno.test("SigilGenerator - Inicialização", () => {
    const generator = new SigilGenerator();
    assertExists(generator);
    assertEquals(generator.gridSize, 9);
});

Deno.test("SigilGenerator - Geração de Sigilo", async () => {
    const generator = new SigilGenerator();
    const sigil = await generator.generateSigil("Proteção e Sabedoria");
    
    assertExists(sigil);
    assert(sigil.startsWith('data:image/png;base64,'));
});

Deno.test("SigilGenerator - Grid de Elementos", () => {
    const generator = new SigilGenerator();
    const mockHash = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    
    const grid = generator._createGrid(mockHash);
    assertEquals(grid.length, 9);
    assertEquals(grid[0].length, 9);
});

Deno.test("SigilGenerator - Elementos Visuais", () => {
    const generator = new SigilGenerator();
    
    // Verificar elementos disponíveis
    assertExists(generator.elements.fire);
    assertExists(generator.elements.water);
    assertExists(generator.elements.air);
    assertExists(generator.elements.earth);
    assertExists(generator.elements.spirit);
});

Deno.test("SigilGenerator - Animação de Sigilo", async () => {
    const generator = new SigilGenerator();
    const sigil = await generator.generateSigil("Teste de Animação");
    
    const animation = await generator.animateSigil(sigil);
    assertExists(animation);
});
