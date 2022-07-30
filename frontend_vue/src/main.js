import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios"

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

createApp(App).use(store).use(router, axios).mount('#app');

getRatings();

function getRatings() {
	const response = axios
		.get('api/v1/ratings')
		.then(response => {
			const ratings = response.data;
			console.log(ratings);
			let ratingKeys = Object.keys(ratings);
			console.log(ratingKeys);
			ratingKeys.sort();
			let labels = []
			let data = []
			for (let i = 0; i < ratingKeys.length; i++) {
				console.log(ratingKeys[i]);
				labels.push(ratingKeys[i]);
				data.push(ratings[ratingKeys[i]])
			}
			console.log(labels);
			console.log(data);
			new Chart(document.getElementById("bar-chart"), {
				type: 'bar',
				data: {
					labels: labels,
					datasets: [
						{
							label: "Rating Popularity",
							backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
							data: data
						}
					]
				},
				options: {
					legend: { display: false },
					title: {
						display: true,
						text: 'Predicted world population (millions) in 2050'
					}
				}
			});
		})
		.catch(error => {
			console.log(error);
		});
}

