<template>
	<div class="filmWorksContainer">
		<div class="filmWorksList">
			<div class="singleFilm" v-for="film in filmWorks" :key="film.id">
				{{film.title}}
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "FilmWorksList",
		props: ['filmWorks']
	}
</script>

<style scoped>
	.filmWorksContainer {
		display: flex;
		justify-content: space-around;
	}
	.filmWorksList {
		width: 40rem;
		display: flex;
		flex-flow: column;
		gap: 1rem;
	}
	.singleFilm {
		background-color: #42b983;
		display: inline;
		padding: 0.5rem 1rem;
		border-radius: 8px;
		color: white;
		font-size: 1.2rem;
	}
</style>