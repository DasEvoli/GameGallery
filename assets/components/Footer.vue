<template>
    <div class="container-fluid footer">
        <p>© 2022 - Vinzenz Wetzel - Data provided by <a href="https://www.twitch.tv/bangerra">Bangeraa</a></p>
        <img :src="'images/icons/github_icon.png'">
        <a href="https://github.com/DasEvoli"> DasEvoli</a>
    </div>
</template>

<style scoped>
    .footer {
        background-color: var(--dark-blue);
        border-top: 2px solid var(--lighter-blue);
        height: 5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1.2rem;
    }

    .footer * {
        vertical-align: middle;
        margin-right: 1rem;
    }

    .footer p {
        margin-bottom: unset;
    }
</style>