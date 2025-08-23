// Visualização Interativa da Árvore da Vida com D3.js
// Definição das Sefirot e Caminhos
const sefirot = [
	{ id: 1, nome: 'Kether', significado: 'Coroa', x: 400, y: 50 },
	{ id: 2, nome: 'Chokmah', significado: 'Sabedoria', x: 250, y: 150 },
	{ id: 3, nome: 'Binah', significado: 'Entendimento', x: 550, y: 150 },
	{ id: 4, nome: 'Chesed', significado: 'Misericórdia', x: 150, y: 250 },
	{ id: 5, nome: 'Geburah', significado: 'Julgamento', x: 650, y: 250 },
	{ id: 6, nome: 'Tiferet', significado: 'Beleza', x: 400, y: 350 },
	{ id: 7, nome: 'Netzach', significado: 'Vitória', x: 250, y: 450 },
	{ id: 8, nome: 'Hod', significado: 'Glória', x: 550, y: 450 },
	{ id: 9, nome: 'Yesod', significado: 'Fundamento', x: 400, y: 550 },
	{ id: 10, nome: 'Malkuth', significado: 'Reino', x: 400, y: 650 }
];

const caminhos = [
	[1,2],[1,3],[1,6],
	[2,3],[2,4],[2,6],
	[3,5],[3,6],
	[4,5],[4,6],[4,7],
	[5,6],[5,8],
	[6,7],[6,8],[6,9],
	[7,8],[7,9],[7,10],
	[8,9],[8,10],
	[9,10]
];

// Inicialização da visualização
document.addEventListener('DOMContentLoaded', function() {
	const width = 800;
	const height = 700;
	const svg = d3.select('#visualizacao-arvore')
		.append('svg')
		.attr('width', width)
		.attr('height', height)
		.style('background', '#f9f5ff');

	// Desenhar caminhos
	svg.selectAll('line.caminho')
		.data(caminhos)
		.enter()
		.append('line')
		.attr('class', 'caminho')
		.attr('x1', d => sefirot[d[0]-1].x)
		.attr('y1', d => sefirot[d[0]-1].y)
		.attr('x2', d => sefirot[d[1]-1].x)
		.attr('y2', d => sefirot[d[1]-1].y)
		.attr('stroke', '#b39ddb')
		.attr('stroke-width', 4)
		.attr('opacity', 0.7);

	// Desenhar sefirot
	const sefirotGroup = svg.selectAll('g.sefira')
		.data(sefirot)
		.enter()
		.append('g')
		.attr('class', 'sefira')
		.attr('transform', d => `translate(${d.x},${d.y})`);

	sefirotGroup.append('circle')
		.attr('r', 32)
		.attr('fill', '#7e57c2')
		.attr('stroke', '#4527a0')
		.attr('stroke-width', 4)
		.on('mouseover', function(e,d) {
			d3.select(this).attr('fill', '#fff176');
			mostrarInfoPainel(d);
		})
		.on('mouseout', function() {
			d3.select(this).attr('fill', '#7e57c2');
			esconderInfoPainel();
		});

	sefirotGroup.append('text')
		.attr('y', 8)
		.attr('text-anchor', 'middle')
		.attr('font-size', '1.2rem')
		.attr('fill', '#fff')
		.attr('font-weight', 'bold')
		.text(d => d.nome);

	// Zoom e pan
	let zoom = d3.zoom()
		.scaleExtent([0.5, 2])
		.on('zoom', (event) => {
			svg.selectAll('g.sefira').attr('transform', d => {
				const t = event.transform;
				return `translate(${t.apply([d.x, d.y])})`;
			});
			svg.selectAll('line.caminho')
				.attr('x1', d => event.transform.apply([sefirot[d[0]-1].x, sefirot[d[0]-1].y])[0])
				.attr('y1', d => event.transform.apply([sefirot[d[0]-1].x, sefirot[d[0]-1].y])[1])
				.attr('x2', d => event.transform.apply([sefirot[d[1]-1].x, sefirot[d[1]-1].y])[0])
				.attr('y2', d => event.transform.apply([sefirot[d[1]-1].x, sefirot[d[1]-1].y])[1]);
		});
	svg.call(zoom);

	document.getElementById('btn-zoom-in').onclick = () => svg.transition().call(zoom.scaleBy, 1.2);
	document.getElementById('btn-zoom-out').onclick = () => svg.transition().call(zoom.scaleBy, 0.8);
	document.getElementById('btn-reiniciar').onclick = () => svg.transition().call(zoom.transform, d3.zoomIdentity);

	// Painel de informações
	function mostrarInfoPainel(sefira) {
		const painel = document.getElementById('info-painel');
		painel.classList.remove('painel-escondido');
		document.getElementById('info-titulo').textContent = sefira.nome;
		document.getElementById('info-conteudo').innerHTML = `<p><strong>Significado:</strong> ${sefira.significado}</p>`;
	}
	function esconderInfoPainel() {
		document.getElementById('info-painel').classList.add('painel-escondido');
	}
	document.getElementById('btn-fechar').onclick = esconderInfoPainel;
});
