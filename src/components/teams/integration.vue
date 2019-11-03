<template>
    <gantt :area="area" :tasks="tasks"></gantt>
</template>

<script>
    import Gantt from '../_base/gantt.vue';
    import tasks from "../../data/tasks/integration.yaml"

    export default {
        name: "integration",
        components: {
            Gantt
        },
        data() {
            return {
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
