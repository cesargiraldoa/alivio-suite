<template>
  <div class="login-container">
    <h2>Iniciar sesión en Alivio</h2>
    <form @submit.prevent="handleLogin">
      <input type="email" v-model="email" placeholder="Correo electrónico" required />
      <input type="password" v-model="password" placeholder="Contraseña" required />
      <button type="submit">Ingresar</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
export default {
  emits: ['login-success'],
  data() {
    return {
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    handleLogin() {
      if (this.email === 'admin@alivio.com' && this.password === '123456') {
        this.$emit('login-success')
      } else {
        this.error = 'Credenciales inválidas'
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 2rem;
  box-shadow: 0 0 10px #ccc;
  border-radius: 10px;
  font-family: sans-serif;
}
input {
  display: block;
  width: 100%;
  margin: 1rem 0;
  padding: 0.5rem;
  font-size: 1rem;
}
button {
  width: 100%;
  padding: 0.7rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
}
.error {
  color: red;
  margin-top: 1rem;
  text-align: center;
}
</style>
