<template>
    <div class="about">
        <div class="content">
            <gantt-elastic
                    :options="options"
                    :tasks="tasks"
                    @tasks-changed="tasksUpdate"
                    @options-changed="optionsUpdate"
                    @dynamic-style-changed="styleUpdate"
            >
                <gantt-header slot="header" :options="options">CDS: {{ area.area }}</gantt-header>
            </gantt-elastic>
        </div>
    </div>
</template>

<style>
</style>

<script>
    import GanttElastic from "gantt-elastic";
    import GanttHeader from "gantt-elastic-header";
    // import dayjs from "dayjs";


    let options = {
        taskMapping: {
            progress: "percent"
        },
        maxRows: 100,
        // maxHeight: 500,
        row: {
            height: 16
        },
        calendar: {
            workingDays: [1, 2, 3, 4, 5],
            hour: {
                display: false
            }
        },
        chart: {
            progress: {
                bar: false
            },
            expander: {
                display: true
            }
        },
        taskList: {
            expander: {
                straight: false
            },
            columns: [
                {
                    id: 1,
                    label: "ID",
                    value: "id",
                    width: 65
                },
                {
                    id: 2,
                    label: "Title",
                    value: "title",
                    width: 300,
                    expander: true,
                    html: true,
                    events: { // eslint-disable-next-line
                        click({data, column}) {
                            let url = "https://productfactory.visualstudio.com/Future%20EHM%20Platform/_workitems/edit/";
                            url += data.id;
                            window.open(url);
                        }
                    }
                },
                {
                    id: 3,
                    label: "Story Points",
                    value: "story_points",
                    width: 30,
                    html: true
                },
                // {
                //     id: 3,
                //     label: "Start",
                //     value: task => dayjs(task.start).format("YYYY-MM-DD"),
                //     width: 78
                // },
                {
                    id: 4,
                    label: "Team",
                    value: "team",
                    width: 68
                },
                {
                    id: 5,
                    label: "%",
                    value: "progress",
                    width: 35,
                    style: {
                        "task-list-header-label": {
                            "text-align": "center",
                            width: "100%"
                        },
                        "task-list-item-value-container": {
                            "text-align": "center",
                            width: "100%"
                        }
                    }
                }
            ]
        },
        locale: {
            name: "en",
            Now: "Now",
            "X-Scale": "Zoom-X",
            "Y-Scale": "Zoom-Y",
            "Task list width": "Task list",
            "Before/After": "Expand",
            "Display task list": "Task list"
        }
    };

    export default {
        name: "Gantt",
        components: {
            GanttElastic,
            GanttHeader
        },
        data() {
            options.title = {
                label: "CDS: " + this.area,
                html: false
            }
            return {
                options,
                dynamicStyle: {},
                lastId: 16
            };
        },

        props: {
            area: {
                type: Object,
                required: true
            },
            tasks: {
                type: Array,
                required: true
            },
        },
        methods: {
            tasksUpdate(tasks) {
                this.tasks = tasks;
            },
            optionsUpdate(options) {
                this.options = options;
            },
            styleUpdate(style) {
                this.dynamicStyle = style;
            }
        }
    };
</script>
