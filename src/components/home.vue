<template>
    <b-tabs size="is-small" class="block">
        <b-tab-item :label="ar.area" v-for="ar in areas" :key="ar.area">
            <component :is="ar.area" :area="ar"></component>
        </b-tab-item>

    </b-tabs>
</template>

<script>
    import areas from "../data/tasks/teams.yaml"
    import infrastructure from './teams/infrastructure'
    import bi from './teams/bi'
    import sm from './teams/sm'
    import integration from './teams/integration'

    export default {
        name: "Home",
        data() {
            return {
                areas,
            }
        },
        components: {
            infrastructure,
            bi,
            sm,
            integration
        },
    }

</script>

<style scoped>

</style>