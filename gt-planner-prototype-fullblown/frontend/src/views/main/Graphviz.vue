<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Graphviz</div>
      </v-card-title>
      <v-card-text>
        <div class="headline font-weight-light ma-5">Hi {{greetedUser}}</div>
      </v-card-text>
      <!-- <div id="graph" style="text-align: center;"></div> -->
      <v-card-actions>
        <v-btn to="/main/profile/view">View Profile</v-btn>
        <v-btn to="/main/profile/edit">Edit Profile</v-btn>
        <v-btn to="/main/profile/password">Change Password</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

// <script src="https://unpkg.com/@hpcc-js/wasm/dist/index.min.js" type="javascript/worker" />

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readUserProfile } from '@/store/main/getters';

import * as d3 from 'd3';
// import * as d3Graphviz from 'd3-graphviz'
// const _ = d3Graphviz.graphviz; // Preload d3Graphiz so it register itself in d3 as a plugin
// import { graphviz } from 'd3-graphviz';
import 'd3-graphviz';


@Component
export default class Graphviz extends Vue {
  get greetedUser() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      if (userProfile.full_name) {
        return userProfile.full_name;
      } else {
        return userProfile.email;
      }
    }
  }

  public mounted() {
    function attributer(datum, index, nodes) {
      const selection = d3.select(function(this: typeof d3, err: any) {
        // tslint:disable-next-line:no-console
        // console.log(err);
        this.emit('end');  // error: `this` implicitly has type `any`
      });
      if (datum.tag === 'svg') {
        const width = window.innerWidth;
        const height = window.innerHeight;
        const x = 200;
        const y = 10;
        const scale = 0.75;
        selection
          .attr('width', width + 'pt')
          .attr('height', height + 'pt')
          .attr('viewBox', -x + ' ' + -y + ' ' + (width / scale) + ' ' + (height / scale));
        datum.attributes.width = width + 'pt';
        datum.attributes.height = height + 'pt';
        datum.attributes.viewBox = -x + ' ' + -y + ' ' + (width / scale) + ' ' + (height / scale);
      }
    }

    function transitionFactory() {
      return d3.transition('main')
            .ease(d3.easeLinear)
            .delay(40)
            .duration(300 * dotIndex);
    }


    let dotIndex = 0;
    const graphviz = d3.select('#graph').graphviz()
        .logEvents(true)
        .transition(transitionFactory)
        .tweenShapes(false)
        .on('initEnd', render)
        .attributer(attributer);

    function render() {
        const dotLines = dots[dotIndex % dots.length];
        const dot = dotLines.join('');
        graphviz
            .renderDot(dot)
            .on('end', () => {
                dotIndex += 1;
                if (dotIndex !== dots.length) {
                    render();
                }
            });
    }

    const colors = d3.scaleOrdinal(d3.schemeBlues[9]);

    const dots = [
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '    a0 -> a3',
            '    a1 -> a3',
            '    a2 -> a3',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '    a0 -> a3',
            '    a1 -> a3',
            '    a2 -> a3',
            '    a0 -> a4',
            '    a1 -> a4',
            '    a2 -> a4',
            '    a3 -> a4',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '    a0 -> a3',
            '    a1 -> a3',
            '    a2 -> a3',
            '    a0 -> a4',
            '    a1 -> a4',
            '    a2 -> a4',
            '    a3 -> a4',
            '    a0 -> a5',
            '    a1 -> a5',
            '    a2 -> a5',
            '    a3 -> a5',
            '    a4 -> a5',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '    a0 -> a3',
            '    a1 -> a3',
            '    a2 -> a3',
            '    a0 -> a4',
            '    a1 -> a4',
            '    a2 -> a4',
            '    a3 -> a4',
            '    a0 -> a5',
            '    a1 -> a5',
            '    a2 -> a5',
            '    a3 -> a5',
            '    a4 -> a5',
            '    a0 -> a6',
            '    a1 -> a6',
            '    a2 -> a6',
            '    a3 -> a6',
            '    a4 -> a6',
            '    a5 -> a6',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '    a0 -> a3',
            '    a1 -> a3',
            '    a2 -> a3',
            '    a0 -> a4',
            '    a1 -> a4',
            '    a2 -> a4',
            '    a3 -> a4',
            '    a0 -> a5',
            '    a1 -> a5',
            '    a2 -> a5',
            '    a3 -> a5',
            '    a4 -> a5',
            '    a0 -> a6',
            '    a1 -> a6',
            '    a2 -> a6',
            '    a3 -> a6',
            '    a4 -> a6',
            '    a5 -> a6',
            '    a0 -> a7',
            '    a1 -> a7',
            '    a2 -> a7',
            '    a3 -> a7',
            '    a4 -> a7',
            '    a6 -> a7',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '    a0 -> a3',
            '    a1 -> a3',
            '    a2 -> a3',
            '    a0 -> a4',
            '    a1 -> a4',
            '    a2 -> a4',
            '    a3 -> a4',
            '    a0 -> a5',
            '    a1 -> a5',
            '    a2 -> a5',
            '    a3 -> a5',
            '    a4 -> a5',
            '    a0 -> a6',
            '    a1 -> a6',
            '    a2 -> a6',
            '    a3 -> a6',
            '    a4 -> a6',
            '    a5 -> a6',
            '    a0 -> a7',
            '    a1 -> a7',
            '    a2 -> a7',
            '    a3 -> a7',
            '    a4 -> a7',
            '    a6 -> a7',
            '    a0 -> a8',
            '    a1 -> a8',
            '    a2 -> a8',
            '    a3 -> a8',
            '    a4 -> a8',
            '    a6 -> a8',
            '    a7 -> a8',
            '}',
        ],
        [
            'digraph  {',
            '    graph [rankdir=TB]',
            '    node [style="filled"]',
            '    a0 [shape="circle" label="" fillcolor="' + colors[0] + '"]',
            '    a1 [shape="circle" label="" fillcolor="' + colors[1] + '"]',
            '    a2 [shape="circle" label="" fillcolor="' + colors[2] + '"]',
            '    a3 [shape="circle" label="" fillcolor="' + colors[3] + '"]',
            '    a4 [shape="circle" label="" fillcolor="' + colors[4] + '"]',
            '    a5 [shape="circle" label="" fillcolor="' + colors[5] + '"]',
            '    a6 [shape="circle" label="" fillcolor="' + colors[6] + '"]',
            '    a7 [shape="circle" label="" fillcolor="' + colors[7] + '"]',
            '    a8 [shape="circle" label="" fillcolor="' + colors[8] + '"]',
            '    a9 [shape="circle" label="" fillcolor="' + colors[9] + '"]',
            '    a0 -> a1',
            '    a0 -> a2',
            '    a1 -> a2',
            '    a0 -> a3',
            '    a1 -> a3',
            '    a2 -> a3',
            '    a0 -> a4',
            '    a1 -> a4',
            '    a2 -> a4',
            '    a3 -> a4',
            '    a0 -> a5',
            '    a1 -> a5',
            '    a2 -> a5',
            '    a3 -> a5',
            '    a4 -> a5',
            '    a0 -> a6',
            '    a1 -> a6',
            '    a2 -> a6',
            '    a3 -> a6',
            '    a4 -> a6',
            '    a5 -> a6',
            '    a0 -> a7',
            '    a1 -> a7',
            '    a2 -> a7',
            '    a3 -> a7',
            '    a4 -> a7',
            '    a6 -> a7',
            '    a0 -> a8',
            '    a1 -> a8',
            '    a2 -> a8',
            '    a3 -> a8',
            '    a4 -> a8',
            '    a6 -> a8',
            '    a7 -> a8',
            '    a0 -> a9',
            '    a1 -> a9',
            '    a2 -> a9',
            '    a3 -> a9',
            '    a4 -> a9',
            '    a6 -> a9',
            '    a7 -> a9',
            '    a8-> a9',
            '}',
        ],
    ];

  }
}

// import * as _d3 from 'd3';
// import * as d3Graphviz from 'd3-graphviz'
// const _ = d3Graphviz.graphviz; // Preload d3Graphiz so it register itself in d3 as a plugin
// import { graphviz } from 'd3-graphviz';

// const d3 = Object.assign({ graphviz }, _d3)


</script>
