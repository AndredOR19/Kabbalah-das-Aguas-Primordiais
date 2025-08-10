fetch('scii_database.json')
  .then(res => res.json())
  .then(data => console.log(data.letras.Aleph.acao_espiritual));
