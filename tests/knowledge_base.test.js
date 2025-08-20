import { assertEquals, assertExists } from "https://deno.land/std/testing/asserts.ts";
import { EsotericKnowledgeBase } from "../engine/knowledge_base/knowledge_base.js";

Deno.test("EsotericKnowledgeBase - Inicialização", async () => {
    const kb = new EsotericKnowledgeBase();
    assertExists(kb);
    assertEquals(kb.sources.liber777, null);
});

Deno.test("EsotericKnowledgeBase - Carregamento de Fontes", async () => {
    const kb = new EsotericKnowledgeBase();
    await kb.loadSources();
    assertExists(kb.sources.liber777);
    assertExists(kb.sources.claviculaSalomonis);
});

Deno.test("EsotericKnowledgeBase - Correlações", async () => {
    const kb = new EsotericKnowledgeBase();
    await kb.loadSources();
    
    const sefirotCorrelations = kb.correlations.get('sefirot');
    assertExists(sefirotCorrelations);
    assertExists(sefirotCorrelations.keter);
    assertEquals(sefirotCorrelations.keter.element, 'Primordial Air');
});

Deno.test("EsotericKnowledgeBase - Consulta", async () => {
    const kb = new EsotericKnowledgeBase();
    await kb.loadSources();
    
    const result = await kb.queryKnowledge("What is the correspondence of Mars in Geburah?");
    assertExists(result);
    assertExists(result.passages);
    assertExists(result.correlations);
});

Deno.test("EsotericKnowledgeBase - Geração de Ritual", async () => {
    const kb = new EsotericKnowledgeBase();
    await kb.loadSources();
    
    const ritual = await kb.generateRitual("Invocar força de Marte em Geburah");
    assertExists(ritual);
    assertEquals(typeof ritual, "object");
});
