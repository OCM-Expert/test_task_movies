<template>
  <genres-list :allGenres="genres" @getActiveGenres="sortByGenre"></genres-list>
  <search-form @searchByActor="sortByActor"></search-form>
  <film-works-list v-if="filmWorks.length !== 0" :film-works="filmWorks"></film-works-list>
  <p v-if="filmWorks.length === 0">Фильмы не найдены</p>
<!--  <actors-list :allActors="actors"></actors-list>-->
</template>

<script>
  import axios from 'axios'
  import GenresList from "@/components/GenresList";
  import FilmWorksList from "@/components/FilmWorksList";
  import ActorsList from "@/components/ActorsList";
  import SearchForm from "@/components/SearchForm";
  export default {
    components: {
      GenresList,
      FilmWorksList,
      ActorsList,
      SearchForm
    },
    data() {
      return {
        filmWorks: [],
        genres: [],
        actors: []
      }
    },
    created() {
      this.getGenres();
      this.getFilmWorks();
    },
    methods: {
      async getGenres() {
        await axios
          .get('/api/v1/genres-list')
          .then(response => {
            this.genres = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },
      async getActors() {
        await axios
          .get('/api/v1/actors-list')
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },
      async getFilmWorks() {
        await axios
        .get('/api/v1/film-works-list')
        .then(response => {
          this.filmWorks = response.data;
        })
        .catch(error => {
          console.log(error);
        });
      },
      async sortByGenre(genre) {
        await axios
          .get('/api/v1/film-works-list', {
            params: { genreToSelect: genre }
          })
          .then(response => {
            this.filmWorks = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },
      async sortByActor(actor) {
        console.log(actor);
        await axios
          .get('/api/v1/film-works-list', {
            params: { actorToSelect: actor }
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
  @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Open+Sans:wght@400;700&display=swap');

  *{
    padding: 0;
    margin: 0;
    border: 0;
    font-family: Lato;
  }
  *,*:before,*:after{
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }
  :focus,:active{outline: none;}
  a:focus,a:active{outline: none;}

  nav,footer,header,aside{display: block;}

  html,body{
    height: 100%;
    width: 100%;
    font-size: 100%;
    line-height: 1;
    font-size: 16px;
    -ms-text-size-adjust: 100%;
    -moz-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
  }
  input,button,textarea{font-family:inherit;}

  input::-ms-clear{display: none;}
  button{cursor: pointer;}
  button::-moz-focus-inner {padding:0;border:0;}
  a, a:visited{text-decoration: none;}
  a:hover{text-decoration: none;}
  ul li{list-style: none;}
  img{vertical-align: top;}

  h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight: 400;}

  .container {
    padding: 5rem 0;
    display: flex;
    justify-content: center;
    font-family: 'Open Sans', 'Lato', sans-serif;
  }

  table {
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
    font-size: 1.5rem;
  }

  p {
    text-align: center;
    color: red;
    font-size: 1.2rem;
    font-family: 'Open Sans', 'Lato', sans-serif;
  }
</style>
