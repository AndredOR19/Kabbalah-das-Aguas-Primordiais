import { assertEquals, assertExists, assert } from "https://deno.land/std/testing/asserts.ts";
import { OracularControl } from "../engine/oracular/oracular_control.js";
import { KnowledgeBase } from "../engine/knowledge_base/knowledge_base.js";
import { SigilGenerator } from "../engine/sigils/sigil_generator.js";

Deno.test("OracularControl - Inicialização", () => {
    const control = new OracularControl();
    assertExists(control);
    assertExists(control.knowledgeBase);
    assertExists(control.sigilGenerator);
});

Deno.test("OracularControl - Integração KnowledgeBase", async () => {
    const control = new OracularControl();
    const pergunta = "Qual o significado da Árvore da Vida?";
    
    const resposta = await control.consultarOracle(pergunta);
    assertExists(resposta);
    assert(resposta.texto.length > 0);
});

Deno.test("OracularControl - Integração SigilGenerator", async () => {
    const control = new OracularControl();
    const intencao = "Sabedoria Divina";
    
    const sigilo = await control.gerarSigiloOracular(intencao);
    assertExists(sigilo);
    assert(sigilo.startsWith('data:image/png;base64,'));
});

Deno.test("OracularControl - Validação de Entrada", async () => {
    const control = new OracularControl();
    
    try {
        await control.consultarOracle("");
        assert(false, "Deveria ter lançado erro para entrada vazia");
    } catch (e) {
        assert(e instanceof Error);
    }
});

Deno.test("OracularControl - Processamento de Múltiplos Pedidos", async () => {
    const control = new OracularControl();
    const pedidos = [
        "Significado do número 7",
        "Simbolismo da Lua",
        "Energia do Sol"
    ];
    
    const respostas = await Promise.all(pedidos.map(p => control.consultarOracle(p)));
    assertEquals(respostas.length, 3);
    respostas.forEach(r => assertExists(r.texto));
});
