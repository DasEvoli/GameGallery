<template>
    <div class="container">
        <div v-if="gamelist.length > 0" class="container row" style="justify-content: center">
            <h1 style="text-align:center">Current statistics</h1>
            <BarChart  class="bar-chart" :title-text="'Score Distribution'" id="scoreBarChart" :chart-data="distributedScore"></BarChart>
            <BarChart  class="bar-chart" :x-tick-display="false" :title-text="'Console Distribution (all games)'" id="consoleBarChart" :chart-data="distributedConsoles"></BarChart>
            <BarChart  class="bar-chart" :x-tick-display="false" :title-text="'Console Distribution (scored games)'" id="consoleBarChart" :chart-data="distributedConsolesScored"></BarChart>
        </div>
    </div>
    <div v-if="upcominglist.length > 0" class="container">
        <h1 style="text-align:center">Upcoming games</h1>
        <div class="gallery">
            <div v-for="game in upcominglist" class="game-item" :key="game">
                <GameThumbnail :game="game"></GameThumbnail>
            </div>
        </div>
    </div>
    <hr/>
    <ControlWindow></ControlWindow>
    <hr/>
    <div v-if="gamelist.length > 0" class="container-fluid" style="height: 70vh; overflow-y: scroll;">
        <div id="game-gallery" class="gallery">
            <div v-for="game in gamelist" class="game-item" :key="game">
                <GameThumbnail :game="game"></GameThumbnail>
            </div>
        </div>
    </div>
    <Footer></Footer>
</template>

<script>
export default {
    data(){
        return {
            gamelist: [],
            upcominglist: [],
        }
    },
    async mounted(){
        this.fetchGamelist('http://localhost:8000/gamelist/challenges')
        this.fetchUpcoming('http://localhost:8000/gamelist/upcoming') 
    },

    computed: {
        distributedScore(){
            let list = this.gamelist
            let allScores = []
            list.forEach(element => {
                if(element.score <= 0 || element.score == "") return
                else allScores.push(element.score)
            });

            let distributed = []
            for(let i = 1; i < 11; i++){
                distributed.push(allScores.filter(x => x==i).length)
            }

            let obj = {
                chartData:{
                    labels: ['1','2','3','4','5','6','7','8','9','10'],
                    datasets: [{
                        data: null,
                        backgroundColor: '#e7e091',
                    }],
                }
            }
            obj.chartData.datasets[0].data = distributed
            return obj.chartData
        },
        distributedConsoles(){
            let list = this.gamelist;
            let uniqueConsoles = []
            list.forEach(element => {
                if(uniqueConsoles.includes(element.console_name)) return
                else uniqueConsoles.push(element.console_name)
            })
            
            let distributedConsoles = {}
            for(let i = 0; i < uniqueConsoles.length; i++){
                distributedConsoles[uniqueConsoles[i]] = list.filter(x => x.console_name==uniqueConsoles[i]).length
            }
            let obj = {
                chartData:{
                    labels: [],
                    datasets: [{
                        data:[],
                        backgroundColor: '#e7e091',
                    }],
                }
            }
            Object.entries(distributedConsoles).forEach(entry => {
                obj.chartData.labels.push(String(entry[0]))
                obj.chartData.datasets[0].data.push(entry[1])
            });
            return obj.chartData
        },
        distributedConsolesScored(){
            let uniqueConsoles = []
            let list = this.gamelist;
            list.forEach(element => {
                if(uniqueConsoles.includes(element.console_name)) return
                else uniqueConsoles.push(element.console_name)
            })

            let distributedConsoles = {}
            for(let i = 0; i < uniqueConsoles.length; i++){
                distributedConsoles[uniqueConsoles[i]] = list.filter(x => x.console_name==uniqueConsoles[i] && x.score > 0).length
            }

            let obj = {
                chartData:{
                    labels: [],
                    datasets: [{
                        data:[],
                        backgroundColor: '#e7e091',
                    }],
                }
            }
            Object.entries(distributedConsoles).forEach(entry => {
                obj.chartData.labels.push(String(entry[0]))
                obj.chartData.datasets[0].data.push(entry[1])
            });
            return obj.chartData 
        }
    },

    methods: {
        fetchGamelist(url){
            fetch(url)
            .then(res => res.json())
            .then(data => this.gamelist = JSON.parse(data))
            .catch(err => console.log(err.message))
        },
        fetchUpcoming(url){
            fetch(url)
            .then(res => res.json())
            .then(data => this.upcominglist = JSON.parse(data))
            .catch(err => console.log(err.message))
        }
    }
}
</script>

<style scoped>
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery .game-item {
    margin-bottom: 0.4rem;
    width: 8rem;
    position: relative;
    margin: 1rem 1rem;
    height: fit-content;
}

.bar-chart {
    width: 34rem
}
</style>






