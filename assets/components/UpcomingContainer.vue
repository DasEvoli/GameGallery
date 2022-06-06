<template>
    <div class="col-12" v-if="data.length > 0">
        <h1>Upcoming Games</h1>
        <div class="upcoming-container">
            <div v-for="item in data" :key="item" class="upcoming-item">
                <img :src="getCoverImage(item)"/>
                <div class="game-info">
                    <p class="title">{{item.game_name}}</p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data(){
            return{
                data: []
            }
        },
        props:['apiUrl'],
        mounted(){
            fetch(this.apiUrl)
            .then(res => res.json())
            .then(data => this.data = JSON.parse(data))
            .catch(err => console.log(err.message))
        },
        methods:{
            getCoverImage(item){
                if(item.cover == null){
                    return "images/game_images/no_cover.jpg"
                }
                else return "images/upcoming_images/" + item.cover
            }
        }
    }
</script>

<style scoped>

    h1 {
        text-align: center;
    }

    .upcoming-container {
        display: flex;
        justify-content: center;
        text-align: center;
    }

    .upcoming-item {
        height: fit-content;
        width: 7rem;
        margin: 1rem;
    }

    img {
        width: 100%;
        height: 100%;
        border-radius: 1rem;
    }

</style>