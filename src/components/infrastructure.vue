<template>
    <gantt :area="area" :tasks="tasks"></gantt>
</template>

<script>
    import Gantt from './Gantt.vue';
    import tasks from "../data/infrastructure.yaml"

    export default {
        name: "infrastructure",
        components: {
            Gantt
        },
        data(){
            return {
                name: "infrastructure",
                tasks
            }
        },
        props: {
            area: {
                type: Object,
                required: true
            }
        }
    }
</script>
