
<template>
  <div class="chat-container">
    <h1>Chat Gerencial Inteligente</h1>
    <div class="chat-box">
      <div v-for="(msg, index) in chatHistory" :key="index">
        <p><strong>🤖 Sistema:</strong> {{ msg.text }}</p>
      </div>
    </div>
    <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Escribe tu pregunta..." />
    <button @click="sendMessage">Enviar</button>
  </div>
</template>

<script>
export default {
  name: 'ChatGerencial',
  data() {
    return {
      userMessage: '',
      chatHistory: [
        { text: 'Hola 👋 soy tu asistente gerencial. ¿En qué puedo ayudarte?' }
      ],
      apiUrl: 'https://chat-api-q0jg.onrender.com/ask'
    };
  },
  methods: {
    async sendMessage() {
      if (!this.userMessage) return;
      const mensaje = this.userMessage;
      this.chatHistory.push({ text: `👤 Tú: ${mensaje}` });
      this.userMessage = '';
      try {
        const response = await fetch(this.apiUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question: mensaje })
        });
        const data = await response.json();
        this.chatHistory.push({ text: `🤖 ${data.respuesta}` });
      } catch (error) {
        this.chatHistory.push({ text: '⚠️ Error conectando con el servidor.' });
      }
    }
  }
}
</script>

<style>
.chat-container {
  font-family: Arial, sans-serif;
  max-width: 700px;
  margin: 0 auto;
  padding: 1rem;
}
.chat-box {
  background: #eee;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  min-height: 150px;
}
input {
  width: 70%;
  padding: 0.5rem;
  margin-right: 0.5rem;
}
button {
  padding: 0.5rem 1rem;
  background-color: #2ecc71;
  border: none;
  color: white;
  border-radius: 5px;
}
</style>
