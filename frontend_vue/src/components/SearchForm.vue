<template>
	<div class="form-container">
		<form @submit.prevent="submitSearch">
			<div class="form-control">
				<label for="actors">Искать по актёрам</label>
				<input type="text" id="actors" v-model.trim="currentName">
			</div>
			<button class="searchButton">Искать</button>
		</form>
	</div>
</template>

<script>
	export default {
		name: "SearchForm",
		data() {
			return {
				currentName: ''
			}
		},
		emits: ['searchByActor'],
		methods: {
			submitSearch() {
				if (this.currentName !== '') {
					this.$emit('searchByActor', this.currentName);
					this.currentName = '';
				}
			}
		}
	}
</script>

<style scoped>
	.form-container {
		display: flex;
		padding: 2.5rem 5rem;
		justify-content: space-around;
	}
	form {
		width: 20rem;
	}
	.form-control {
		 margin: 1rem 0;
	 }
	.searchButton {
		display: inline;
		padding: 0.5rem 1rem;
		border-radius: 5px;
		cursor: pointer;
		background-color: darkorchid;
		color: white;
		align-self: flex-end;
		font-family: sans-serif;
	}
	.form-control {
		margin: 0.5rem 0;
	}

	label {
		font-weight: bold;
		display: block;
		margin-bottom: 0.5rem;
	}
	input,
	textarea {
		display: block;
		width: 100%;
		border: 1px solid #ccc;
		font: inherit;
	}

	input:focus,
	textarea:focus {
		background-color: #f0e6fd;
		outline: none;
		border-color: #3d008d;
	}
</style>