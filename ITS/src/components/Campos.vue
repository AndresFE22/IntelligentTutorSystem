<template>
  <div>
    <nav class="campo-nav">
      <ul>
        <li><router-link to="/" exact exact-active-class="active-link">Inicio</router-link></li>
        <li><router-link to="/Campos/ingresar-palabra" exact exact-active-class="active-link">Palabras</router-link></li>
        <li><router-link to="/Campos/ingresar-oracion" exact exact-active-class="active-link">Oraciones</router-link></li>
        <li><router-link to="/Campos/ingresar-info" exact exact-active-class="active-link">Información</router-link></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<style scoped>
.campo-nav {
  background-color: #f0f0f0;
  padding: 10px;
}

.campo-nav ul {
  list-style-type: none;
  display: flex;
  justify-content: center;
}

.campo-nav li {
  margin-right: 10px;
}

.campo-nav a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  padding: 5px 10px;
}

.campo-nav a:hover {
  background-color: #ccc;
}

.active-link {
  background-color: #ccc; /* Cambia el color de fondo para el enlace activo */
}
</style>


<script>
   export default {
  name: 'CamposL',

};
</script>
