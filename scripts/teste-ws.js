// Teste de conexão WebSocket com Socket.IO (cliente)
// Uso: WS_URL=wss://seu-dominio node scripts/teste-ws.js

const { io } = require('socket.io-client');

const URL = process.env.WS_URL || 'wss://teu-dominio.com';
const TIMEOUT_MS = 10000; // timeout de segurança

console.log(`🔌 Conectando em ${URL}...`);

const socket = io(URL, {
  path: '/socket.io',
  transports: ['websocket'],
  reconnectionAttempts: 3,
  timeout: 5000,
});

let finished = false;

function done(code = 0) {
  if (finished) return;
  finished = true;
  try { socket.close(); } catch (e) {}
  process.exit(code);
}

socket.on('connect', () => {
  console.log('✅ Conectado! ID:', socket.id);
  console.log('🔥 Teste de envio/recebimento (ping com ACK)...');
  const start = Date.now();
  socket.emit('ping', start, (ackTs) => {
    const rtt = Date.now() - start;
    console.log(`⏱️ Latência (RTT): ${rtt}ms`);
    done(0);
  });
});

socket.on('connect_error', (err) => {
  console.error('❌ Falha na conexão:', err.message);
  done(1);
});

socket.on('disconnect', (reason) => {
  console.log('🚫 Desconectado:', reason);
});

socket.on('heartbeat', (ts) => console.log('💓 heartbeat', ts));

setTimeout(() => {
  console.error('⌛ Timeout: Nenhuma resposta em 10s');
  done(1);
}, TIMEOUT_MS);