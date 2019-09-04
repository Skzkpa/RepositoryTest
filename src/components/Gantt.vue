<template>
    <q-page class="q-pa-sm">
        <gantt-elastic
                :options="options"
                :tasks="tasks"
                @tasks-changed="tasksUpdate"
                @options-changed="optionsUpdate"
                @dynamic-style-changed="styleUpdate"
        >
            <gantt-header slot="header" :options="options">RR: Infra</gantt-header>
        </gantt-elastic>
    </q-page>
</template>

<style>
</style>

<script>
    import GanttElastic from "gantt-elastic";
    import GanttHeader from "gantt-elastic-header";
    import dayjs from "dayjs";
    import tasks from "../data/tasks.json"
    import rtasks from "../data/repetable_tasks.json"

    function getDate(days) {
        const currentDate = new Date();
        const currentYear = currentDate.getFullYear();
        const currentMonth = currentDate.getMonth();
        const currentDay = currentDate.getDate();
        const timeStamp = new Date(
            currentYear,
            currentMonth,
            currentDay,
            0,
            0,
            0
        ).getTime();
        return new Date(timeStamp + days * 60 * 60 * 1000 * 24).getTime();
    }

    function addDays(date, days) {
        var result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
    }

    for (let task of tasks) {
        task.duration = task.duration * 24 * 3600 * 1000;
    }

    for (let rtask of rtasks) {
        let duration = rtask.duration;
        rtask.duration = 0;
        tasks.push(rtask);
        rtask.duration = duration;
        for (let i = 0, len = rtask.repeats + 0, tid = rtask.id; i < len; i++) {
            // let atask = JSON.parse(JSON.stringify(rtask));
            let atask = Object.assign({}, rtask);
            atask.id = atask.id + i + 1;
            atask.type = "task";
            atask.start = addDays(atask.start, 14 * i);
            atask.parentId = tid;
            atask.duration = atask.duration * 24 * 3600 * 1000;
            tasks.push(atask);
        }
    }

    let options = {
        taskMapping: {
            progress: "percent"
        },
        maxRows: 100,
        maxHeight: 500,
        title: {
            label: "RR: Infra",
            html: false
        },
        row: {
            height: 24
        },
        calendar: {
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
                // {
                //     id: 1,
                //     label: "ID",
                //     value: "id",
                //     width: 40
                // },
                {
                    id: 2,
                    label: "Description",
                    value: "label",
                    width: 300,
                    expander: true,
                    html: true,
                    events: { // eslint-disable-next-line
                        click({data, column}) {
                            alert("description clicked!\n" + data.label);
                        }
                    }
                },
                {
                    id: 3,
                    label: "FTEs",
                    value: "user",
                    width: 130,
                    html: true
                },
                {
                    id: 3,
                    label: "Start",
                    value: task => dayjs(task.start).format("YYYY-MM-DD"),
                    width: 78
                },
                {
                    id: 4,
                    label: "Type",
                    value: "type",
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
            return {
                tasks,
                options,
                dynamicStyle: {},
                lastId: 16
            };
        },
        methods: {
            addTask() {
                this.tasks.push({
                    id: this.lastId++,
                    label:
                        '<a href="https://images.pexels.com/photos/423364/pexels-photo-423364.jpeg?auto=compress&cs=tinysrgb&h=650&w=940" target="_blank" style="color:#0077c0;">Yeaahh! you have added a task bro!</a>',
                    user:
                        '<a href="https://images.pexels.com/photos/423364/pexels-photo-423364.jpeg?auto=compress&cs=tinysrgb&h=650&w=940" target="_blank" style="color:#0077c0;">Awesome!</a>',
                    start: getDate(24 * 3),
                    duration: 1 * 24 * 60 * 60 * 1000,
                    percent: 50,
                    type: "project"
                });
            },
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
