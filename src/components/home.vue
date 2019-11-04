<template>
    <b-tabs size="is-small" class="block">
        <b-tab-item :label="ar.area" v-for="ar in areas" :key="ar.area">
            <gantt :area="ar" :tasks="tasks[ar.area]"></gantt>
        </b-tab-item>

    </b-tabs>
</template>

<script>
    import Gantt from './_base/gantt.vue';

    import areas from "../data/tasks/teams.yaml"
    import infrastructure from "../data/tasks/infrastructure.yaml"
    import bi from "../data/tasks/bi.yaml"
    import sm from "../data/tasks/sm.yaml"
    import integration from "../data/tasks/integration.yaml"
    import epsui from "../data/tasks/epsui.yaml"


    export default {
        name: "Home",
        data() {
            return {
                areas,
                tasks: {
                    infrastructure,
                    bi,
                    sm,
                    integration,
                    epsui,
                }
            }
        },
        components: {
            Gantt
        },
    }

</script>

<style scoped>

</style>