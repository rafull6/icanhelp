<template>
  <div class="login">
    <img class="login__bg" src="@/assets/bg.jpg"/>
    <img class="login__logo" alt="I Can Help" src="@/assets/logo.png"/>
    <form class="login__content" v-on:submit="goToDashboard($event)">
      <form-field label='E-mail' name='email' type='email' placeholder='Wpisz swój e-mail'/>
      <form-field label='Hasło' name='password' type='password' placeholder='Wpisz swoje hasło'/>
      <blue-button class="login__button">Zaloguj się</blue-button>
      <div class="login__links">
        <a class="login__remind-password" href="">Zapomniałeś hasła?</a><br>
        <a class="login__register" href="">Załóż konto</a>
      </div>
    </form>
  </div>
</template>

<script>
import router from '../../router';
import FormField from './FormField';
import Button from './Button';

export default {
  name: "Login",
  components: { FormField, BlueButton: Button },
  methods: {
    goToDashboard: function(event){
      event.preventDefault();
      const { email, password } = event.target;

      if(email.value === 'admin@admin.com' && password.value === 'admin'){
        router.push('/');
      }
    }
  }
};
</script>

<style scoped lang="scss">
  .login {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    &__bg {
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
      z-index: -1;
    }

    &__logo {
      position: absolute;
      left: 40px;
      top: 30px;
    }

    &__content {
      max-width: 430px;
      width: 100%;
      padding: 0 15px;
    }

    &__button {
      margin-top: 5px;
      margin-bottom: 20px;
    }

    &__links {
      font-size: 16px;
      text-align: center;
    }

    &__remind-password {
      color: $black;
      font-weight: 600;
      text-decoration: none;
      display: inline-block;
      margin-bottom: 15px;
      &:hover {
        text-decoration: underline;
      }
    }

    &__register {
      color: $blue;
      font-weight: 600;
      text-decoration: none;
      display: inline-block;
      &:hover {
        text-decoration: underline;
      }
    }
  }
</style>
