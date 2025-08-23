// Valores das letras hebraicas para Gematria
const letrasHebraicas = [
	{ letra: 'א', nome: 'Alef', valor: 1, significado: 'Unidade, Deus, o Inefável' },
	{ letra: 'ב', nome: 'Bet', valor: 2, significado: 'Casa, dualidade, sabedoria' },
	{ letra: 'ג', nome: 'Gimel', valor: 3, significado: 'Camelô, recompensa, bondade' },
	{ letra: 'ד', nome: 'Dalet', valor: 4, significado: 'Porta, pobreza, humildade' },
	{ letra: 'ה', nome: 'He', valor: 5, significado: 'Ventana, revelação, vida' },
	{ letra: 'ו', nome: 'Vav', valor: 6, significado: 'Gancho, conexão, harmonia' },
	{ letra: 'ז', nome: 'Zayin', valor: 7, significado: 'Espada, alimento, luta' },
	{ letra: 'ח', nome: 'Chet', valor: 8, significado: 'Cerca, vida, energia vital' },
	{ letra: 'ט', nome: 'Tet', valor: 9, significado: 'Serpente, bondade essencial' },
	{ letra: 'י', nome: 'Yod', valor: 10, significado: 'Mão, poder, fundamento' },
	{ letra: 'כ', nome: 'Kaf', valor: 20, significado: 'Palma, realização, potencial' },
	{ letra: 'ך', nome: 'Kaf Final', valor: 500, significado: 'Realização final' },
	{ letra: 'ל', nome: 'Lamed', valor: 30, significado: 'Aguilhão, ensino, coração' },
	{ letra: 'מ', nome: 'Mem', valor: 40, significado: 'Água, revelação oculta' },
	{ letra: 'ם', nome: 'Mem Final', valor: 600, significado: 'Águas primordiais' },
	{ letra: 'נ', nome: 'Nun', valor: 50, significado: 'Peixe, fé, eternidade' },
	{ letra: 'ן', nome: 'Nun Final', valor: 700, significado: 'Fé transcendente' },
	{ letra: 'ס', nome: 'Samech', valor: 60, significado: 'Suporte, ciclo, proteção' },
	{ letra: 'ע', nome: 'Ayin', valor: 70, significado: 'Olho, visão, fonte' },
	{ letra: 'פ', nome: 'Pe', valor: 80, significado: 'Boca, expressão, poder da fala' },
	{ letra: 'ף', nome: 'Pe Final', valor: 800, significado: 'Expressão divina' },
	{ letra: 'צ', nome: 'Tzadi', valor: 90, significado: 'anzol, justiça, humildade' },
	{ letra: 'ץ', nome: 'Tzadi Final', valor: 900, significado: 'Justiça divina' },
	{ letra: 'ק', nome: 'Kuf', valor: 100, significado: 'Macaco, sagrado, encarnação' },
	{ letra: 'ר', nome: 'Resh', valor: 200, significado: 'Cabeça, pensamento, pobreza' },
	{ letra: 'ש', nome: 'Shin', valor: 300, significado: 'Dente, fogo, transformação' },
	{ letra: 'ת', nome: 'Tav', valor: 400, significado: 'Cruz, verdade, selo' }
];

// Palavras e conceitos importantes na Kabbalah com seus valores
const conceitosKabbalisticos = [
	{ palavra: 'יחוד', valor: 28, significado: 'Unidade (de Deus)' },
	{ palavra: 'אהבה', valor: 13, significado: 'Amor' },
	{ palavra: 'חיים', valor: 68, significado: 'Vida' },
	{ palavra: 'שלום', valor: 376, significado: 'Paz' },
	{ palavra: 'מלכות', valor: 496, significado: 'Reino (Malkuth)' },
	{ palavra: 'חכמה', valor: 73, significado: 'Sabedoria (Chokmah)' },
	{ palavra: 'בינה', valor: 67, significado: 'Entendimento (Binah)' },
	{ palavra: 'חסד', valor: 72, significado: 'Bondade (Chesed)' },
	{ palavra: 'גבורה', valor: 216, significado: 'Força (Gevurah)' },
	{ palavra: 'תפארת', valor: 1081, significado: 'Beleza (Tiferet)' },
	{ palavra: 'נצח', valor: 148, significado: 'Eternidade (Netzach)' },
	{ palavra: 'הוד', valor: 15, significado: 'Esplendor (Hod)' },
	{ palavra: 'יסוד', valor: 80, significado: 'Fundamento (Yesod)' },
	{ palavra: 'שכינה', valor: 385, significado: 'Presença Divina' }
];

// Preencher a tabela de valores das letras
function preencherTabelaLetras() {
	const tabela = document.getElementById('tabela-letras');
	letrasHebraicas.forEach(letra => {
		const linha = document.createElement('tr');
		linha.innerHTML = `
			<td class="letra-hebraica">${letra.letra}</td>
			<td>${letra.nome}</td>
			<td>${letra.valor}</td>
			<td>${letra.significado}</td>
		`;
		tabela.appendChild(linha);
	});
}

// Calcular o valor da Gematria para uma palavra
function calcularGematria(palavra) {
	let valorTotal = 0;
	let letrasEncontradas = [];
    
	for (let i = 0; i < palavra.length; i++) {
		const caractere = palavra[i];
		const letraInfo = letrasHebraicas.find(l => l.letra === caractere);
        
		if (letraInfo) {
			valorTotal += letraInfo.valor;
			letrasEncontradas.push({
				letra: letraInfo.letra,
				nome: letraInfo.nome,
				valor: letraInfo.valor
			});
		}
	}
    
	return { valorTotal, letrasEncontradas };
}

// Encontrar conceitos kabbalísticos com valores similares
function encontrarConceitosSimilares(valor, margem = 10) {
	return conceitosKabbalisticos.filter(conceito => 
		Math.abs(conceito.valor - valor) <= margem
	);
}

// Formatador de número para exibição
function formatarNumero(numero) {
	// Adicionar pontos como separadores de milhar
	return numero.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

// Mostrar resultado do cálculo
function mostrarResultado(resultado) {
	const valorElemento = document.getElementById('valor-gematria');
	const interpretacaoElemento = document.getElementById('interpretacao');
    
	valorElemento.textContent = formatarNumero(resultado.valorTotal);
    
	let interpretacaoHTML = `
		<div class="decomposicao">
			<h3>Decomposição:</h3>
			<ul>
	`;
    
	resultado.letrasEncontradas.forEach(letra => {
		interpretacaoHTML += `
			<li>${letra.letra} (${letra.nome}): ${formatarNumero(letra.valor)}</li>
		`;
	});
    
	interpretacaoHTML += `
			</ul>
		</div>
	`;
    
	// Encontrar conceitos similares
	const conceitosSimilares = encontrarConceitosSimilares(resultado.valorTotal);
	if (conceitosSimilares.length > 0) {
		interpretacaoHTML += `
			<div class="conceitos-similares">
				<h3>Conceitos Kabbalísticos Relacionados:</h3>
				<ul>
		`;
        
		conceitosSimilares.forEach(conceito => {
			interpretacaoHTML += `
				<li>${conceito.palavra} (${formatarNumero(conceito.valor)}): ${conceito.significado}</li>
			`;
		});
        
		interpretacaoHTML += `
				</ul>
			</div>
		`;
	}
    
	// Adicionar interpretação baseada no valor total
	interpretacaoHTML += `
		<div class="interpretacao-valor">
			<h3>Interpretação do Valor ${formatarNumero(resultado.valorTotal)}:</h3>
			<p>${gerarInterpretacao(resultado.valorTotal)}</p>
		</div>
	`;
    
	interpretacaoElemento.innerHTML = interpretacaoHTML;
}

// Gerar uma interpretação baseada no valor numérico
function gerarInterpretacao(valor) {
	if (valor <= 10) return "Representa unidade e princípios fundamentais.";
	if (valor <= 22) return "Relaciona-se com as 22 letras do alfabeto hebraico.";
	if (valor <= 32) return "Conectado aos 32 Caminhos da Sabedoria da Kabbalah.";
	if (valor === 50) return "Representa os 50 Portões de Entendimento (Binah).";
	if (valor === 72) return "Relacionado aos 72 Nomes de Deus na tradição kabbalística.";
	if (valor === 231) return "Conectado aos 231 Portões mencionados no Sefer Yetzirah.";
	if (valor === 613) return "Relacionado aos 613 mandamentos da Torá.";
    
	// Verificar se é um número triangular
	const n = Math.floor(Math.sqrt(2 * valor));
	if (n * (n + 1) === 2 * valor) {
		return `O valor ${formatarNumero(valor)} é um número triangular (T${n}), representando completude e equilíbrio.`;
	}
    
	// Verificar se é um número quadrado
	const raiz = Math.sqrt(valor);
	if (raiz === Math.floor(raiz)) {
		return `O valor ${formatarNumero(valor)} é um quadrado perfeito (${raiz}²), simbolizando estabilidade e fundamento.`;
	}
    
	return "Este valor possui significados diversos na tradição kabbalística, dependendo do contexto e das palavras relacionadas.";
}

// Inicializar a calculadora quando a página carregar
window.addEventListener('DOMContentLoaded', function() {
	preencherTabelaLetras();

	const btnCalcular = document.getElementById('btn-calcular');
	const palavraInput = document.getElementById('palavra-input');

	function calcularEExibir() {
		const valor = palavraInput.value.trim();
		if (valor === '') {
			alert('Por favor, digite uma palavra em hebraico.');
			return;
		}
		const resultado = calcularGematria(valor);
		mostrarResultado(resultado);
	}

	btnCalcular.onclick = calcularEExibir;
	palavraInput.onkeydown = function(e) {
		if (e.key === 'Enter') {
			calcularEExibir();
		}
	};
	palavraInput.value = 'חכמה';
});
