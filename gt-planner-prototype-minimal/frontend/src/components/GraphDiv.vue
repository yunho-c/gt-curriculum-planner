<template>
  <div id="graph" style="text-align: center;"/>
</template>

<script>
// d3-graphviz
import * as d3 from 'd3'
import 'd3-graphviz'

// load webassembly
let wasm = document.createElement('script')
wasm.setAttribute('src', 'https://unpkg.com/@hpcc-js/wasm/dist/index.min.js')
wasm.setAttribute('type', 'application/javascript')
document.head.appendChild(wasm)

// d3-graphviz utils
function attributer(datum) { // deleted arguments (lint complaint) index, nodes
    var selection = d3.select(this);
    if (datum.tag == "svg") {
        var width = window.innerWidth;
        var height = window.innerHeight;
        var x = 200;
        var y = 10
        var scale = 0.75;
        selection
            .attr("width", width + "pt")
            .attr("height", height + "pt")
            .attr("viewBox", -x + " " + -y + " " + (width / scale) + " " + (height / scale));
        datum.attributes.width = width + "pt";
        datum.attributes.height = height + "pt";
        datum.attributes.viewBox = -x + " " + -y + " " + (width / scale) + " " + (height / scale);
    }
}

function transitionFactory() {
    return d3.transition("main")
        .ease(d3.easeLinear)
        .delay(40)
        .duration(500);
}

export default {
  methods: {
    // call after vue loads (i.e. mounted())
    attach_graphviz() {
      this.g = d3.select("#graph").graphviz()
      .logEvents(true)
      .transition(transitionFactory)
      .tweenShapes(false)
      .attributer(attributer);
      // .on("initEnd", render)
    },

    draw(dot) {
      this.g.renderDot(dot)
    }
  },
  
  mounted() {
    this.attach_graphviz()
  }
}
</script>
