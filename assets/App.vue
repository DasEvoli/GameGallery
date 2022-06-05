<template>
<div class="row">
    <div class="col-9" style="height: 100vh; overflow-y: scroll;">
        <Gallery apiUrl="http://localhost:8000/gamelist/challenges"></Gallery>
    </div>
    <div class="col-3">
        <ControlWindow></ControlWindow>
    </div>
</div>
</template>