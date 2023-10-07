<template>
  <div class="noticias-lista">
    <div class="filtro">
      <input v-model="busqueda" type="text" class="v-input" placeholder="Buscar noticias" @input="realizarBusqueda">
      <select v-model="filtroCategoria" class="v-select categoria-select" @ïnput="busquedaCategoria">
        <option value="">Todas las categorías</option>
        <option v-for="(noticia, index) in noticias" :key="index">{{ noticia.category }}</option>
      </select>
      <input v-model="filtroFecha" type="date" class="v-input" @input="busquedaFecha">
    </div>
    <br>
    <div class="tabla-responsive">
      <table>
        <thead>
          <tr>
            <th>Nombre del remitente</th>
            <th>Categoría de la noticia</th>
            <th>Fecha de publicación</th>
            <th>Días de publicación</th>
            <th>Estado de la noticia</th>
            <th>Opciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(noticia, index) in noticias" :key="index">
            <td>{{ noticia.autor }}</td>
            <td>{{ noticia.category }}</td>
            <td>{{ noticia.time }}</td>
            <td>{{ noticia.diasPublicacion }}</td>
            <td>{{ noticia.estado }}</td>
            <td>
              <button @click="editar(index)" class="boton-editar">
                <i></i> Aceptar
              </button>
              <button @click="borrar(index)" class="boton-borrar">
                <i></i> Rechazar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      busqueda: '',
      filtroCategoria: '',
      filtroFecha: '',
      noticias: [],
      noticiasporDefecto: [],
      categorias: [],
    };
  },
  mounted() {
    axios
      .get('http://localhost:3001/notices')
      .then(response => {
        this.noticias = response.data
        this.noticiasporDefecto = [...response.data]
        this.filtroCategoria = response.data.category
        this.filtroFecha = response.data.datos.fechaPublicacion
        console.log(this.noticias)
      })
      .catch(error => {
        console.error('error al obtener noticias', error);
      })
  },
  methods: {
    realizarBusqueda() {
      if (this.busqueda) {
        this.noticias = this.noticiasporDefecto.filter(noticia =>
          Object.values(noticia).some(valor =>
            String(valor).toLowerCase().includes(this.busqueda.toLowerCase())
          )
        );
      } else {
        this.noticias = [...this.noticiasporDefecto];
      }
    },
    busquedaCategoria() {
      if (this.busqueda) {
        this.noticias = this.noticiasporDefecto.filter(noticia =>
          noticia.category.toLowerCase().includes(this.filtroCategoria.toLowerCase())
        );
      } else {
        this.noticias = [...this.noticiasporDefecto];
      }
    },
    busquedaFecha() {
      if (this.busqueda) {
        this.noticias = this.noticiasporDefecto.filter(noticia =>
          noticia.filtroFecha.toLowerCase().includes(this.filtroFecha.toLowerCase())
        );
      } else {
        this.noticias = [...this.noticiasporDefecto];
      }
    }
  }
}
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  border: 1px solid #ccc;
  text-align: center;
  padding: 10px;
}

th {
  background-color: #00bcd4;
  /* Cambia el color de fondo del encabezado */
  color: white;
  /* Cambia el color del texto del encabezado */
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

.v-input,
.v-select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
}

.v-input[type="date"] {
  padding: 6px;
}

.v-select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
  width: 200px;

}

.categoria-select {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
  width: 12%;
}

.noticias-lista {
  text-align: center;
  padding: 20px;
}

.filtro {
  display: flex;
  justify-content: center;
}

.filtro input,
select {
  margin-right: 40px;
  margin-left: 40px;

}

.boton-editar, .boton-borrar {
  background-color: green;
  color: white;
  border: none;
  padding: 5px 10px;
  margin: 2px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 14px;
}

.boton-editar:hover, .boton-borrar:hover {
  background-color: darkgreen;
}

.boton-borrar {
  background-color: red;
}

.boton-borrar:hover {
  background-color: darkred;
}
</style>