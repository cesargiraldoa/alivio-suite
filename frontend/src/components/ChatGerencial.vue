<!-- FRONTEND - Vue 3 con Vite -->
<template>
  <div class="chat-container">
    <h1>Chat Gerencial Inteligente</h1>

    <div class="chat-box">
      <div v-for="(msg, index) in chatHistory" :key="index" class="message">
        <span class="sender">
          <span v-if="msg.sender === 'Sistema'">🤖 <strong>{{ msg.sender }}:</strong></span>
          <span v-else>🧑‍💼 <strong>{{ msg.sender }}:</strong></span>
        </span>
        <span class="text">{{ msg.text }}</span>
      </div>
    </div>

    <div class="input-box">
      <input
        v-model="userMessage"
        type="text"
        placeholder="Escribe tu pregunta..."
        @keyup.enter="sendMessage"
      />
      <button @click="sendMessage">Enviar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatGerencial',
  data() {
    return {
      userMessage: '',
      chatHistory: [
        { sender: 'Sistema', text: 'Hola 👋 soy tu asistente gerencial. ¿En qué puedo ayudarte?' }
      ],
      apiUrl: 'https://chat-api-q0jg.onrender.com/ask' // <-- Asegúrate de que este sea el link correcto al backend
    };
  },
  methods: {
    async sendMessage() {
      const msg = this.userMessage.trim();
      if (msg === '') return;

      this.chatHistory.push({ sender: 'Tú', text: msg });
      this.userMessage = '';

      try {
        const response = await fetch(this.apiUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question: msg })
        });

        if (!response.ok) throw new Error('Error en la respuesta del servidor');

        const data = await response.json();
        this.chatHistory.push({ sender: 'Sistema', text: data.respuesta });
      } catch (error) {
        this.chatHistory.push({ sender: 'Sistema', text: '⚠️ Error conectando con el servidor.' });
      }
    }
  }
};
</script>

<style scoped>
.chat-container {
  max-width: 700px;
  margin: auto;
  font-family: Arial, sans-serif;
  text-align: center;
}
.chat-box {
  background: #f2f2f2;
  border-radius: 10px;
  padding: 1.5em;
  margin-bottom: 1em;
  min-height: 200px;
  text-align: left;
}
.message {
  margin: 0.5em 0;
}
.input-box {
  display: flex;
  gap: 0.5em;
}
input {
  flex: 1;
  padding: 0.5em;
  font-size: 1em;
}
button {
  padding: 0.5em 1em;
  background-color: #2ecc71;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
