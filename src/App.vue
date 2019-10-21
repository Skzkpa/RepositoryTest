<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<script>
    export default {
        name: "app",
        data() {
            return {
                leftDrawerOpen: false
            };
        }
    };
</script>

<style>
</style>
