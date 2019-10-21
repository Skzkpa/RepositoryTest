<template>
    <q-layout>
        <q-page-container>
            <router-view/>
        </q-page-container>
    </q-layout>
</template>

<script>
    export default {
        name: "LayoutDefault",
        data() {
            return {
                leftDrawerOpen: false
            };
        }
    };
</script>

<style>
</style>
