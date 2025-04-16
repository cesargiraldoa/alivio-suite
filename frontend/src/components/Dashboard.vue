<template>
  <div class="dashboard">
    <h2>Bienvenido a Alivio</h2>
    <div class="cards">
      <div class="card" @click="$emit('go-chat')">
        <span class="icon">🤖</span>
        <h3>Chat Gerencial</h3>
        <p>Consulta inteligente para decisiones</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard'
}
</script>

<style scoped>
.dashboard {
  padding: 2rem;
  text-align: center;
  font-family: sans-serif;
}
.cards {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}
.card {
  border: 1px solid #ccc;
  padding: 1.5rem;
  border-radius: 10px;
  cursor: pointer;
  width: 300px;
  box-shadow: 0 0 5px #ddd;
}
.card:hover {
  background: #f0f0f0;
}
.icon {
  font-size: 2rem;
}
</style>
