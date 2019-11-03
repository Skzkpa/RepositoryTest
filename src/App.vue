<template>
    <div id="app">
        <router-view/>

        <app-footer></app-footer>
    </div>
</template>

<script>

    import Footer from './components/_base/footer.vue'

    export default {
        name: "app",
        data() {
            return {
                leftDrawerOpen: false
            };
        },
        components: {
            'app-footer': Footer,
        },
    };
</script>

<style>
</style>
