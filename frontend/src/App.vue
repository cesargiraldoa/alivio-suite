<template>
  <div>
    <Login v-if="!isLoggedIn" @login-success="handleLoginSuccess" />
    <Dashboard v-else-if="view === 'dashboard'" @go-chat="view = 'chat'" />
    <ChatGerencial v-else-if="view === 'chat'" />
  </div>
</template>

<script>
import Login from './components/Login.vue'
import Dashboard from './components/Dashboard.vue'
import ChatGerencial from './components/ChatGerencial.vue'

export default {
  name: 'App',
  components: { Login, Dashboard, ChatGerencial },
  data() {
    return {
      isLoggedIn: false,
      view: 'dashboard'
    }
  },
  methods: {
    handleLoginSuccess() {
      this.isLoggedIn = true;
      this.view = 'dashboard';
    }
  }
}
</script>
