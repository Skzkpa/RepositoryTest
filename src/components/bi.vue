<template>
    <gantt :area="area" :tasks="tasks"></gantt>
</template>

<script>
    import Gantt from './Gantt.vue';
    import tasks from "../data/bi.yaml"

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
