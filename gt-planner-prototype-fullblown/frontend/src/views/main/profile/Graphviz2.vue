<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">User Profile</div>
      </v-card-title>
      <div>
        <script src="https://unpkg.com/@hpcc-js/wasm/dist/index.min.js" type="javascript/worker" />
        <!-- <script src="https://unpkg.com/@hpcc-js/wasm/dist/index.min.js" type="application/javascript" /> -->
        <!-- <script src="https://unpkg.com/@hpcc-js/wasm/dist/index.min.js" type="application/wasm" /> -->
        <h3>from Component</h3>
        <div id="graph" />
      </div>
      <v-card-text>
        <div class="my-4">
          <div class="subheading secondary--text text--lighten-3">Full Name</div>
          <div class="title primary--text text--darken-2" v-if="userProfile && userProfile.full_name">{{userProfile.full_name}}</div>
          <div class="title primary--text text--darken-2" v-else>-----</div>
        </div>
        <div class="my-3">
          <div class="subheading secondary--text text--lighten-3">Email</div>
          <div class="title primary--text text--darken-2" v-if="userProfile && userProfile.email">{{userProfile.email}}</div>
          <div class="title primary--text text--darken-2" v-else>-----</div>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn to="/main/profile/edit">Edit</v-btn>
        <v-btn to="/main/profile/password">Change password</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>



<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readUserProfile } from '@/store/main/getters';

// import '@hpcc-js/wasm'
import * as d3 from 'd3';
import 'd3-graphviz';

@Component
export default class Graphviz2 extends Vue {
  get userProfile() {
    return readUserProfile(this.$store);
  }

  public goToEdit() {
    this.$router.push('/main/profile/edit');
  }

  public goToPassword() {
    this.$router.push('/main/profile/password');
  }

  public mounted() {
    d3.select('#graph').graphviz('#graph').renderDot('digraph {a -> b -> c}');
  }
}
</script>
