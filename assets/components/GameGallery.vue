<template>
    <div v-if="games.length > 0" class="game-list">
        <div v-for="n in games" class="item" :key="n.score">
            <span class="ranking">{{n.score}}</span>
            <img src="images/example_cover.png"/>
            <div class="game-info">
                <p class="console">{{n.console_name}}</p>
                <p class="title">{{n.game_name}}</p>
                <p class="time">{{n.time}}</p>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data(){
            return {
                games: []
            }
        },
        mounted(){
            fetch('http://localhost:8000/gamelist/challenges')
            .then(res => res.json())
            .then(data => this.games = JSON.parse(data))
            .catch(err => console.log(err.message))
        }
    }
</script>

<style scoped>
    .game-list {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }

    .game-list .item {
        margin-bottom: 0.4rem;
        width: 12rem;
        position: relative;
        margin: 0rem 1rem;
    }

    .game-list .item img {
        margin-top: 1rem;
        display: flex;
        min-height: 200px;
        height: 200px;
        border-radius: 1rem;
        padding-bottom: 0.3rem;
        margin-right: auto;
        margin-left: auto;
    }

    .game-info {
        width: 60%;
        margin: 0 auto;
    }

    .game-info p {
        overflow-wrap: break-word;

        margin-bottom: 0;
        display: block;
        text-align: center;
        padding: 0;
    }

    .ranking {
        position: absolute;
        font-size: 2rem;
        background-color: #e3e3e3;
        width: 2rem;
        height: 2rem;
        display: flex;
        border-radius: 20%;
        text-align: center;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        left: 80%;
    }
</style>