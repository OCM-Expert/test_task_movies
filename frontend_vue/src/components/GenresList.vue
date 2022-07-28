<template>
	<div class="genreSelecting">
		<div class="genresContainer">
			<div class="singleGenre"
			     v-for="genre in allGenres"
			     :key="genre.name"
			     @click="clickGenre(el, String(genre.name))">
				{{genre.name}}
			</div>
		</div>
		<button @click="submitActiveGenres">Выбрать по жанрам</button>
	</div>
</template>

<script>
	export default {
		name: "GenresList",
		data() {
			return {
				activeGenres: []
			}
		},
		props: [
			'allGenres'
		],
		methods: {
			clickGenre(element, name) {
				if (this.activeGenres.includes(name)) {
					this.activeGenres = this.activeGenres.filter(function (genreName) { return genreName !== name });
				} else {
					this.activeGenres.push(name);
				}
			},
			submitActiveGenres() {
				this.$emit('getActiveGenres', this.activeGenres);
			}
		},
		emits: [
			'getActiveGenres'
		]
	}
</script>

<style scoped>
	.genreSelecting {
		padding: 5rem 10rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.genresContainer {
		display: flex;
		flex-flow: row wrap;
		gap: 0.5rem;
	}
	.singleGenre {
		border: gray 1px solid;
		display: inline;
		padding: 0.5rem 1rem;
		border-radius: 5px;
	}
	.activeGenre {
		background-color: #42b983;
		color: white;
	}
	button {
		padding: 0.5rem 1rem;
		border-radius: 5px;
		background-color: darkorchid;
		color: white;
		font-size: 1.2rem;
		align-self: flex-end;
	}
</style>