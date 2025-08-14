# 🔐 Configuração de Segredos do GitHub

Para que as automações do Instituto Águas Primordiais funcionem corretamente, você precisa configurar os seguintes segredos no seu repositório GitHub:

## 📋 Passo a Passo

1. **Acesse seu repositório no GitHub**
2. **Vá para Settings → Secrets and variables → Actions**
3. **Clique em "New repository secret"**

## 🔑 Segredos Necessários

### 1. OPENAI_API_KEY
- **Nome**: `OPENAI_API_KEY`
- **Valor**: Sua chave de API da OpenAI (começa com `sk-`)
- **Onde obter**: https://platform.openai.com/api-keys

### 2. GITHUB_TOKEN
- **Nome**: `GITHUB_TOKEN`
- **Valor**: Token do GitHub (gerado automaticamente ou pessoal)
- **Como criar**: 
  - Vá para Settings → Developer settings → Personal access tokens
  - Crie um token com permissões: `repo`, `issues`, `pull_requests`
  - Copie o token gerado

## ✅ Verificação

Após configurar os segredos, teste as automações:

1. **Teste de Deploy**: Faça um push para a branch `main`
2. **Teste do Mestre Digital**: Abra uma nova issue no repositório

## 🚨 Notas Importantes

- **Nunca** compartilhe suas chaves de API publicamente
- **Nunca** commite chaves no código
- Os segredos são criptografados e seguros no GitHub
- As automações funcionarão automaticamente após a configuração

## 🔄 Fluxo de Trabalho

### Deploy Automático
- **Trigger**: Push na branch `main`
- **Ação**: Atualiza o site no GitHub Pages
- **Tempo**: ~2-3 minutos

### Mestre Digital
- **Trigger**: Nova issue ou comentário
- **Ação**: Resposta automática usando IA
- **Tempo**: ~10-30 segundos

## 🛠️ Troubleshooting

Se as automações não funcionarem:
1. Verifique se os segredos estão corretos
2. Confira os logs em Actions → [nome do workflow]
3. Certifique-se de que o repositório é público (GitHub Pages requer repo público para free)
