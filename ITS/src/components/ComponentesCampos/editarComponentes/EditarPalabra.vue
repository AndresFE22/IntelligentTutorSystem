<template>
    <div>
        <div class="title">
            <v-btn icon @click="atras">
            <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
            <h1>Tabla de Palabras</h1>
        </div>
      <div class="container">
        <div v-if="mensaje" class="mensaje">{{ mensaje }}</div>
        <v-data-table :headers="headers" :items="palabras" item-key="id" class="tabla-palabras">
          <template slot="item" slot-scope="{ item }">
            <tr>
              <td class="text-left">{{ item[0] }}</td>
              <td class="text-left">{{ item[1] }}</td>
              <td class="text-left">
                <v-btn @click="openModalTwo(item[2])">
                  <v-icon>mdi-eye</v-icon>
                </v-btn>
              </td>
              <td class="text-left">
                <v-icon @click="openModal(item[0])">mdi-image</v-icon>
              </td>
              <td class="text-left">
                <v-btn class="editar-button" @click="editarPalabra(item[0])">
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </td>
              <td class="text-left">
                <v-btn class="eliminar-button" @click="eliminarPalabra(item[0])">
                  <v-icon>mdi-delete</v-icon>
                </v-btn>
              </td>
            </tr>
          </template>
          
        </v-data-table>
      </div>
      <v-dialog v-model="modalOpen" max-width="500px">
        <v-card>
          <img :src="selectedImage" width="300px" />
        </v-card>
      </v-dialog>
      <v-dialog v-model="modalOpentwo" max-width="500px">
        <v-card>
          <div class="significado-td">
            <h1>Significado:</h1>
            {{ selectedSignificado }}
          </div>
          <v-btn icon class="modal-close-btn" @click="modalOpentwo = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        palabras: [],
        headers: [
          { text: 'ID', value: 'id' },
          { text: 'Palabra', value: 'palabra' },
          { text: 'Significado', value: 'significado' },
          { text: 'Imagen', value: 'significado' },
          { text: 'Editar', value: 'edit' },
          { text: 'Eliminar', value: 'delete' }
        ],
        modalOpen: false,
        modalOpentwo: false,
        selectedImage: '',
        selectedSignificado: '',
        mensaje: "",
      };
    },
    mounted() {
      this.obtenerPalabras();
    },
    methods: {
      obtenerPalabras() {
        axios
          .get('https://cuentaapi.pythonanywhere.com/apik/showtable')
          .then((response) => {
            this.palabras = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      editarPalabra(id) {
        this.$router.push(`editar-palabra/editar/${id}`);
      },
      eliminarPalabra(id) {
        axios
          .delete(`https://cuentaapi.pythonanywhere.com/apik/palabras/${id}`)
          .then((response) => {
            console.log(response.data);
            this.mensaje = response.data.message;
            setTimeout(() => {
                this.mensaje = "";
            }, 3000
            );
            this.obtenerPalabras();
          })
          .catch((error) => {
            console.error(error);
          });
      },
      openModal(id) {
        axios
          .get(`https://cuentaapi.pythonanywhere.com/apik/palabras/${id}/image`)
          .then((response) => {
            this.selectedImage = this.getImageUrl(
              response.data.imagen_base64,
              response.data.formato_imagen
            );
            this.modalOpen = true;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      getImageUrl(imagenBase64, formato) {
        return `data:image/${formato};base64,${imagenBase64}`;
      },
      openModalTwo(significado) {
        this.selectedSignificado = significado;
        this.modalOpentwo = true;
      },

      atras() {
        this.$router.push("/Campos/ingresar-palabra");
      }
    }
  };
  </script>
  
  <style scoped>

.mensaje {
    background-color: rgb(255, 45, 45);
    color: white;
    padding: 10px;
    border-radius: 20px;

    }

  .title {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    margin-top: 20px;


  }
  .tabla-palabras {
    margin-top: 15px;
    width: 100%;
  }
  
  .editar-button {
    color: #008cff;
    background-color: #1976d2;
  }
  
  .eliminar-button {
    color: #ff2020;
    background-color: #f44336;
  }
  
  .significado-td {
    max-width: 500px;
    padding: 10%;
  }
  
  .text-left {
    text-align: left;
  }
  
  .modal-close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
  }
  </style>
  