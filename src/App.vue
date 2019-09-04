<template>
  <q-layout>
    <q-header class="bg-grey-2 text-black">
      <q-toolbar>
        <q-toolbar-title>
          CDS Infra: Gantt
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import Gantt from "./components/Gantt.vue";

export default {
  name: "LayoutDefault",
  data() {
    return {
      leftDrawerOpen: false
    };
  }
};
</script>

<style>
</style>
