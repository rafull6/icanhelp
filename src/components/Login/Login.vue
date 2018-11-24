<template>
  <div class="login">
    <img class="login__logo" alt="I Can Help" src="@/assets/logo.png" />
    <div class="login__content">
      <form-field label='E-mail' type='email' placeholder='Wpisz swój e-mail'/>
      <form-field label='Hasło' type='password' placeholder='Wpisz swoje hasło'/>
      <blue-button class="login__button">Zaloguj się</blue-button>
      <div class="login__links">
        <a class="login__remind-password" href="">Zapomniałeś hasła?</a><br>
        <a class="login__register" href="">Załóż konto</a>
      </div>
    </div>
  </div>
</template>

<script>
import FormField from './FormField';
import Button from './Button';

export default {
  name: "Login",
  components: { FormField, BlueButton: Button }
};
</script>

<style scoped lang="scss">
  .login {
    background: url(~/assets/bg.jpg) no-repeat center center;
    background-size: cover;
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
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
