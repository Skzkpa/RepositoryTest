<template>
    <gantt :area="area" :tasks="tasks"></gantt>
</template>

<script>
    import Gantt from '../_base/gantt.vue';
    import tasks from "../../data/tasks/infrastructure.yaml"

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
