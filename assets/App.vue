<template>
    <div class="container">
        <h1 style="text-align:center">Upcoming games</h1>
        <div v-if="upcoming.length > 0" class="gallery">
            <div v-for="game in upcoming" class="game-item" :key="game">
                <GameThumbnail :game="game"></GameThumbnail>
            </div>
        </div>
    </div>
    <hr/>
    <ControlWindow></ControlWindow>
    <hr/>
    <div class="container-fluid" style="height: 70vh; overflow-y: scroll;">
        <div v-if="gamelist.length > 0" id="game-gallery" class="gallery">
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
            upcoming: []
        }
    },
    mounted(){
        this.fetchGamelist('http://localhost:8000/gamelist/challenges')
        this.fetchUpcoming('http://localhost:8000/gamelist/upcoming')
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
            .then(data => this.upcoming = JSON.parse(data))
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
</style>






