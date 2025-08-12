#!/usr/bin/env node
/**
 * DEMO: Ponte SCII-Core em Ação
 * Demonstração prática da integração Sismógrafo-Atlas
 */

const fs = require('fs');
const path = require('path');

// Carregar o SCII-Core
const sciiCore = JSON.parse(
  fs.readFileSync(path.join(__dirname, 'scii_database.js/data/scii_database.json'), 'utf8')
);

class SCIIBridge {
  constructor(sciiData) {
    this.sciiData = sciiData;
    this.ponte = sciiData.ponte_sismografo_atlas;
    this.config = this.ponte.configuracao_ponte;
  }

  // Simular detecção do Sismógrafo
  detectarEmocao(textoCommit) {
    const emocoesDetectadas = [];
    const mapeamento = this.ponte.mapeamento_emocoes_anatomia;
    
    for (const [emocao, dados] of Object.entries(mapeamento)) {
      // Busca simples por palavras-chave
      const palavrasChave = emocao.split('_');
      const encontrou = palavrasChave.some(palavra => 
        textoCommit.toLowerCase().includes(palavra.toLowerCase())
      );
      
      if (encontrou) {
        emocoesDetectadas.push({
          emocao,
          dados,
          intensidade: dados.intensidade_base + Math.random() * 0.3
        });
      }
    }
    
    return emocoesDetectadas;
  }

  // Simular comando para o Atlas
  iluminarSistema(meshId, intensidade, cor, duracao = 3000) {
    console.log(`🔥 ATLAS: Iluminando ${meshId}`);
    console.log(`   💡 Intensidade: ${(intensidade * 100).toFixed(1)}%`);
    console.log(`   🎨 Cor: ${cor}`);
    console.log(`   ⏱️  Duração: ${duracao}ms`);
    
    // Simular fade out
    setTimeout(() => {
      console.log(`🌙 ATLAS: Fade out ${meshId}`);
    }, duracao);
  }

  // Buscar informação espiritual da letra
  obterSabedoriaEspiritual(nomeLetra) {
    const letra = this.sciiData.letras[nomeLetra];
    if (!letra) return null;
    
    return {
      letra_hebraica: letra.letra_hebraica,
      funcao_espiritual: letra.funcao_espiritual,
      comando_ritualistico: letra.comando_ritualistico,
      pratica_sugerida: letra.pratica_sugerida
    };
  }

  // Processar commit completo
  processarCommit(autor, mensagem) {
    console.log(`\n🔍 SISMÓGRAFO: Analisando commit de ${autor}`);
    console.log(`📝 Mensagem: "${mensagem}"`);
    console.log('─'.repeat(60));
    
    const emocoesDetectadas = this.detectarEmocao(mensagem);
    
    if (emocoesDetectadas.length === 0) {
      console.log('😌 Nenhuma emoção significativa detectada');
      return;
    }

    emocoesDetectadas.forEach((deteccao, index) => {
      const { emocao, dados, intensidade } = deteccao;
      
      console.log(`\n${index + 1}. 🎭 EMOÇÃO DETECTADA: ${emocao}`);
      console.log(`   🫀 Sistema: ${dados.sistema_anatomico}`);
      console.log(`   🔤 Letra: ${dados.letra_hebraica} (${dados.nome_letra})`);
      
      // Iluminar no Atlas
      this.iluminarSistema(
        dados.id_mesh_3d,
        intensidade,
        dados.cor_visualizacao,
        this.config.fade_duration_ms
      );
      
      // Mostrar sabedoria espiritual
      const sabedoria = this.obterSabedoriaEspiritual(dados.nome_letra);
      if (sabedoria) {
        console.log(`\n   ✨ SABEDORIA ESPIRITUAL:`);
        console.log(`   🎯 Função: ${sabedoria.funcao_espiritual}`);
        console.log(`   📿 Comando: ${sabedoria.comando_ritualistico}`);
        console.log(`   🧘 Prática: ${sabedoria.pratica_sugerida}`);
      }
      
      console.log('─'.repeat(40));
    });
  }
}

// DEMONSTRAÇÃO PRÁTICA
console.log('🌟 DEMO: SCII-Core - Ponte Sismógrafo-Atlas');
console.log('═'.repeat(60));

const ponte = new SCIIBridge(sciiCore);

// Simular diferentes commits com emoções
const commits = [
  {
    autor: "João",
    mensagem: "Fix: Corrigindo bug frustante que estava me deixando louco"
  },
  {
    autor: "Maria", 
    mensagem: "Feature: Implementando nova funcionalidade, mas estou com ansiedade sobre o prazo"
  },
  {
    autor: "Pedro",
    mensagem: "Refactor: Limpando código, me sinto perdido sem direção clara"
  },
  {
    autor: "Ana",
    mensagem: "Docs: Atualizando documentação, superando medo da mudança"
  },
  {
    autor: "Carlos",
    mensagem: "Style: Ajustando CSS, meu ego está inflado hoje"
  }
];

// Processar cada commit
commits.forEach((commit, index) => {
  setTimeout(() => {
    ponte.processarCommit(commit.autor, commit.mensagem);
  }, index * 4000); // Espaçar as demonstrações
});

// Mostrar estatísticas finais
setTimeout(() => {
  console.log('\n🎉 DEMONSTRAÇÃO CONCLUÍDA!');
  console.log('═'.repeat(60));
  console.log(`📊 ESTATÍSTICAS DO SCII-CORE:`);
  console.log(`   🔤 Letras hebraicas: 22/22 completas`);
  console.log(`   🎭 Emoções mapeadas: ${Object.keys(ponte.ponte.mapeamento_emocoes_anatomia).length}`);
  console.log(`   🫀 Estados fisiológicos: ${Object.keys(ponte.ponte.estados_fisiologicos).length}`);
  console.log(`   🌉 Status da ponte: OPERACIONAL`);
  console.log('\n🚀 Pronto para integração com sistemas reais!');
}, commits.length * 4000 + 2000);