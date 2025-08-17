// Teste de conexão WebSocket com Socket.IO (cliente)
// Uso: node scripts/teste-ws.js

const { io } = require('socket.io-client');

// Ajuste o domínio conforme seu ambiente
const URL = process.env.WS_URL || 'wss://teu-dominio.com';

const socket = io(URL, {
  path: '/socket.io',
  transports: ['websocket'],
  reconnectionAttempts: 3,
});

socket.on('connect', () => console.log('✅ Conectado | ID:', socket.id));
socket.on('connect_error', (err) => console.error('❌ Falha:', err.message));
socket.on('disconnect', (reason) => console.log('🚫 Desconectado:', reason));
socket.on('heartbeat', (ts) => console.log('💓 heartbeat', ts));

// Timeout de 20s para encerrar o teste automaticamente
setTimeout(() => {
  console.log('⏱️ Encerrando teste...');
  socket.close();
  process.exit(0);
}, 20000);