<template>
  <div class="container">
    <div class="genre"
         v-for="genre in genres"
         :key="genre.name">
      <h5>{{genre.name}}</h5>
    </div>
<!--    <div class="film-work"-->
<!--         v-for="filmWork in filmWorks"-->
<!--         :key="filmWork.title">-->
<!--      <h5>{{filmWork.title}}</h5>-->
<!--      <p>{{filmWork.rating}}</p>-->
<!--    </div>-->
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        filmWorks: [],
        genres: []
      }
    },
    mounted() {
      this.getGenres();
      this.getFilmWorks();
    },
    methods: {
      getGenres() {
        axios
          .get('/api/v1/genres-list')
          .then(response => {
            this.genres = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },
      getFilmWorks() {
        axios
        .get('/api/v1/film-works-list', {
          params: {
            whatToGet: 'filmWorks'
          }
        })
        .then(response => {
          this.filmWorks = response.data;
        })
        .catch(error => {
          console.log(error);
        });
      }
    }
  }
</script>

<style lang="scss">

</style>
