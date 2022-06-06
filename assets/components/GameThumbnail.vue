<template>
    <span class="ranking">{{getScore()}}</span>
    <a :href="game.video_url"><img :src="getCoverImage()"/></a>
    <div class="game-info">
        <p class="console">{{game.console_name}}</p>
        <p class="title">{{game.game_name}}</p>
        <p class="time">{{game.time}}</p>
    </div>
</template>
<script>
    export default {     
        props: ['game'],
        computed: {
        },
        methods: {
            getCoverImage(){
                if(this.game.cover == null){
                    return "images/game_images/no_cover.jpg"
                }
                else return "images/game_images/" + this.game.cover
            },
            getScore(){
                if(this.game.score == null){
                    return 0
                }
                else return this.game.score
            }
        }
    }
</script>

<style scoped>

img {
    width: 100%;
    height: 100%;
    border-radius: 0.7rem 0.7rem 0rem 0rem;
}

.game-info p {
    overflow-wrap: break-word;
    margin-bottom: 0;
    text-align: center;
}

.ranking {
    position: absolute;
    font-size: 2rem;
    background-color: black;
    color: white;
    font-weight: bold;
    width: 1rem;
    height: 1rem;
    display: flex;
    border-radius: 20%;
    text-align: center;
    justify-content: center;
    align-items: center;
    padding: 1.5rem;
    left: 80%;
    top: -3%;
}
</style>