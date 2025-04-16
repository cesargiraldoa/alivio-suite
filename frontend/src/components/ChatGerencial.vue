<template>
  <div class="chat-container">
    <h2>Chat Gerencial Inteligente</h2>
    <div class="chat-box">
      <div v-for="(msg, i) in chatHistory" :key="i" class="chat-msg" :class="msg.sender">
        <span class="avatar">{{ msg.sender === 'Tú' ? '🧑‍💼' : '🤖' }}</span>
        <span><strong>{{ msg.sender }}:</strong> {{ msg.text }}</span>
      </div>
    </div>
    <form @submit.prevent="sendMessage">
      <input type="text" v-model="userMessage" placeholder="Escribe tu pregunta..." />
      <button type="submit">Enviar</button>
    </form>
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
      apiUrl: 'https://chat-api-q0jg.onrender.com/ask'
    };
  },
  methods: {
    async sendMessage() {
      if (!this.userMessage.trim()) return;
      const pregunta = this.userMessage;
      this.chatHistory.push({ sender: 'Tú', text: pregunta });
      this.userMessage = '';

      try {
        const res = await fetch(this.apiUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question: pregunta })
        });

        const data = await res.json();
        this.chatHistory.push({ sender: 'Sistema', text: data.respuesta || 'Sin respuesta.' });
      } catch (error) {
        this.chatHistory.push({ sender: 'Sistema', text: '⚠️ Error conectando con el servidor.' });
      }
    }
  }
}
</script>

<style scoped>
.chat-container {
  max-width: 700px;
  margin: 40px auto;
  font-family: sans-serif;
  text-align: center;
}
.chat-box {
  background: #f1f1f1;
  padding: 1rem;
  border-radius: 10px;
  max-height: 350px;
  overflow-y: auto;
  text-align: left;
  margin-bottom: 1rem;
}
.chat-msg {
  margin-bottom: 1rem;
  display: flex;
  gap: 0.5rem;
  align-items: flex-start;
}
.chat-msg.Tú {
  justify-content: flex-end;
}
.avatar {
  font-size: 1.2rem;
}
input {
  width: 70%;
  padding: 0.5rem;
  font-size: 1rem;
}
button {
  padding: 0.5rem 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  margin-left: 0.5rem;
  border-radius: 5px;
  font-size: 1rem;
}
</style>
