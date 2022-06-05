<template>
    <span class="ranking">{{game.score}}</span>
    <img :src="getCoverImage()"/>
    <div class="game-info">
        <p class="console">{{game.console_name}}</p>
        <p class="title">{{game.game_name}}</p>
        <p class="time">{{game.time}}</p>
    </div>
</template>
<script>
    export default {
        //data() {
            //return {
                //game: null
            //}
        //},        
        props: ['game'],
        computed: {
        },
        methods: {
            getCoverImage(){
                if(this.game.cover == null){
                    return "images/game_images/no_cover.jpg"
                }
                else return "images/game_images/" + this.game.cover
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
    top: -3%;
}
</style>