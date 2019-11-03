<template>
    <footer class="footer">
        <div class="columns">
            <div class="column is-offset-11">
                v.{{ version }}
            </div>
        </div>

    </footer>
</template>

<script>
    export default {
        name: 'appFooter',
        data() {
            return {
                version: '0.2.0'
            }
        },
    }
</script>

<style scoped>
    footer {
        padding: 1.5rem;
    }
</style>