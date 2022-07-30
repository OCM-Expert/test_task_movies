<template>
	<div class="actorSelecting">
		<div class="actorContainer">
			<button
				v-for="actor in allActors"
				:key="actor.name">
				{{actor.full_name}}
			</button>
		</div>
	</div>
</template>

<script>
	export default {
		name: "ActorsList",
		props: ['allActors'],
	}
</script>

<style scoped>

</style>