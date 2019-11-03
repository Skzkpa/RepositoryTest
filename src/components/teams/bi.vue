<template>
    <gantt :area="area" :tasks="tasks"></gantt>
</template>

<script>
    import Gantt from '../_base/gantt.vue';
    import tasks from "../../data/tasks/bi.yaml"

    export default {
        name: "bi",
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
