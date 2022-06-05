<template>
    <div v-if="data.length > 0" class="gallery">
        <div v-for="item in data" class="item" :key="item">
            <GameThumbnail :game="item"></GameThumbnail>
        </div>
    </div>
</template>
<script>
    import GameThumbnail from "./GameThumbnail.vue"
    export default {
        name: 'Gallery',
        components: [GameThumbnail],
        props: ['apiUrl'],
        data(){
            return {
                data: []
            }
        },
        mounted(){
            fetch(this.apiUrl)
            .then(res => res.json())
            .then(data => this.data = JSON.parse(data))
            .catch(err => console.log(err.message))
        }
    }
</script>

<style scoped>
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.item {
    margin-bottom: 0.4rem;
    width: 12rem;
    position: relative;
    margin: 1rem 1rem;
    height: fit-content;
    min-height: 20rem;
}
</style>