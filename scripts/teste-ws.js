// Teste de conexão WebSocket com Socket.IO (cliente)
// Uso: WS_URL=wss://seu-dominio node scripts/teste-ws.js

const { io } = require('socket.io-client');

const WS_URL = Deno.env.get('WS_URL') || 'wss://kabbalah-aguas-primordiais.com';
const TIMEOUT_MS = 10000; // timeout de segurança

console.log(`🔌 Conectando em ${WS_URL}...`);

const socket = io(WS_URL, {
  path: '/socket.io',
  transports: ['websocket'],
  reconnectionAttempts: 3,
  timeout: 10000,
});

let finished = false;

function done(code = 0) {
  if (finished) return;
  finished = true;
  try { socket.close(); } catch (e) {}
  Deno.exit(code);
}

socket.on('connect', () => {
  console.log('✅ Conectado! ID:', socket.id);
  console.log('🔥 Teste de envio/recebimento (ping/ack)...');
  const startTime = Date.now();
  // Envia ping com callback para ACK
  socket.emit('ping', startTime, (ackTime) => {
    if (typeof ackTime !== 'number') {
      console.error('❌ ACK inválido recebido');
      return done(1);
    }
    const latency = ackTime - startTime;
    console.log(`⏱️ Latência: ${latency}ms`);
    done(0);
  });
});

socket.on('connect_error', (err) => {
  console.error('❌ Falha na conexão:', err.message);
  done(1);
});

// Fallback para servidores sem handler de ping
setTimeout(() => {
  console.error('⌛ Timeout: Servidor não respondeu ao ping (handler ausente?)');
  console.log('ℹ️ Certifique-se de implementar no servidor:');
  console.log("socket.on('ping', (ts, ack) => ack(Date.now()));");
  done(1);
}, TIMEOUT_MS);