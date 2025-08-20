import { assertEquals, assertExists, assert } from "https://deno.land/std/testing/asserts.ts";
import { OracularSystem } from "../engine/oracular/system.js";

Deno.test("Sistema Oracular - Inicialização", () => {
    const sistema = new OracularSystem();
    assertExists(sistema);
    assertExists(sistema.control);
    assertExists(sistema.templates);
});

Deno.test("Sistema Oracular - Consulta Completa", async () => {
    const sistema = new OracularSystem();
    const consulta = {
        pergunta: "Como posso encontrar equilíbrio espiritual?",
        nome: "João",
        dataNascimento: "1990-01-01"
    };
    
    const resposta = await sistema.realizarConsulta(consulta);
    assertExists(resposta);
    assertExists(resposta.texto);
    assertExists(resposta.sigilo);
    assertExists(resposta.elementosDominantes);
});

Deno.test("Sistema Oracular - Análise de Perfil", async () => {
    const sistema = new OracularSystem();
    const perfil = await sistema.analisarPerfil({
        nome: "Maria",
        dataNascimento: "1985-06-15"
    });
    
    assertExists(perfil);
    assertExists(perfil.elementoPrimario);
    assertExists(perfil.elementoSecundario);
});

Deno.test("Sistema Oracular - Geração de Relatório", async () => {
    const sistema = new OracularSystem();
    const dados = {
        consulta: "Propósito de vida",
        nome: "Pedro",
        dataNascimento: "1995-12-25"
    };
    
    const relatorio = await sistema.gerarRelatorio(dados);
    assertExists(relatorio);
    assert(relatorio.includes(dados.nome));
    assert(relatorio.includes("Propósito"));
});

Deno.test("Sistema Oracular - Cache de Respostas", async () => {
    const sistema = new OracularSystem();
    const pergunta = "Qual o significado do número 3?";
    
    const resposta1 = await sistema.realizarConsulta({ pergunta });
    const resposta2 = await sistema.realizarConsulta({ pergunta });
    
    assertEquals(resposta1.id, resposta2.id);
});
