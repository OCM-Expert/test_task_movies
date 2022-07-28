<template>
  <div class="container">
    <div class="film-work"
         v-for="filmWork in filmWorks"
         :key="filmWork.title">
      <h5>{{filmWork.title}}</h5>
      <p>{{filmWork.rating}}</p>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        filmWorks: []
      }
    },
    mounted() {
      this.getFilmWorks();
    },
    methods: {
      getFilmWorks() {
        axios
        .get('/api/v1/film-works-list')
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
