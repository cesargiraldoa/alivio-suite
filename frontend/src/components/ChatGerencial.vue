<template>
  <div class="chat-container">
    <h1>Chat Gerencial Inteligente</h1>
    <div class="chat-box">
      <div v-for="(msg, index) in chatHistory" :key="index" class="message">
        <strong>🤖 <span style="color: black">{{ msg.sender }}:</span></strong>
        <span>{{ msg.text }}</span>
      </div>
    </div>
    <div class="input-container">
      <input
        v-model="userMessage"
        @keyup.enter="sendMessage"
        placeholder="Escribe tu pregunta..."
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
        {
          sender: 'Sistema',
          text: 'Hola 👋 soy tu asistente gerencial. ¿En qué puedo ayudarte?'
        }
      ],
      apiUrl: 'https://chat-api-q0jg.onrender.com/ask'
    };
  },
  methods: {
    async sendMessage() {
      const message = this.userMessage.trim();
      if (!message) return;

      // Mostrar mensaje del usuario
      this.chatHistory.push({ sender: 'Tú', text: message });
      this.userMessage = '';

      try {
        const response = await fetch(this.apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ question: message })
        });

        if (!response.ok) {
          throw new Error('Error al llamar a la API');
        }

        const data = await response.json();
        this.chatHistory.push({ sender: 'Sistema', text: data.respuesta });
      } catch (error) {
        this.chatHistory.push({
          sender: 'Sistema',
          text: '⚠️ Error conectando con el servidor.'
        });
      }
    }
  }
};
</script>

<style scoped>
.chat-container {
  max-width: 800px;
  margin: 40px auto;
  font-family: 'Arial', sans-serif;
  text-align: center;
}

.chat-box {
  background-color: #f1f1f1;
  padding: 20px;
  border-radius: 15px;
  min-height: 200px;
  margin-bottom: 20px;
  text-align: left;
}

.message {
  margin: 10px 0;
}

.input-container {
  display: flex;
  justify-content: center;
  gap: 10px;
}

input {
  width: 70%;
  padding: 10px;
  font-size: 16px;
  border: 2px solid #ccc;
  border-radius: 8px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #2ecc71;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

button:hover {
  background-color: #27ae60;
