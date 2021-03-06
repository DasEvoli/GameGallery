/*
 * Welcome to your app's main JavaScript file!
 *
 * We recommend including the built version of this JavaScript file
 * (and its CSS file) in your base layout (base.html.twig).
 */



// any CSS you import will output into a single css file (app.css in this case)
import './styles/app.css';

// start the Stimulus application
import './bootstrap';

// vue
import { createApp } from 'vue';
import App from "./App.vue";

import GameThumbnail from "./components/GameThumbnail.vue"
import ControlWindow from "./components/ControlWindow.vue"
import Footer from "./components/Footer.vue"
import BarChart from "./components/BarChart.vue"


const app = createApp(App);
app.component('GameThumbnail', GameThumbnail);
app.component('ControlWindow', ControlWindow);
app.component('Footer', Footer);
app.component('BarChart', BarChart);
app.mount('#app');