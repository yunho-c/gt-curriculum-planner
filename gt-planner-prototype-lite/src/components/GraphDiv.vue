<template>
  <!-- let's go back to percent based width once css understanding settles -->
  <div
    id="graph"
    style="
      text-align: center;
      width: 1900px;
      height: 1000px;
      border: 1px solid black;
    "
  />
</template>

<script lang="ts">
import * as d3 from 'd3'
import * as d3Graphviz from 'd3-graphviz'
// d3-graphviz
// import * as d3 from 'd3'
// console.log(d3)
// import * as d3graphviz from 'd3-graphviz'
// import { graphviz } from 'd3-graphviz'
// import 'd3-graphviz'

// load webassembly
const wasm = document.createElement('script')
wasm.setAttribute('src', 'https://unpkg.com/@hpcc-js/wasm/dist/index.min.js')
wasm.setAttribute('type', 'application/javascript') // it works but I don't know why..
document.head.appendChild(wasm)

export default {
  inject: ['d3', 'd3Graphviz'],
  data() {
    return {
      curr: null,
    }
  },
  mounted() {
    this.attach_graphviz()
  },
  methods: {
    transitionFactory() {
      return d3.transition('main').delay(130).duration(1000)
    },
    // call after vue loads (i.e. mounted())
    attach_graphviz() {
      const graphContainer = d3.select('#graph')
      // // console.log(graphContainer)
      // // console.log(d3)
      const width = graphContainer.node().clientWidth
      const height = graphContainer.node().clientHeight

      this.g = d3Graphviz.graphviz('#graph')
      // this.g = graphviz('#graph')
        .logEvents(true)
        .transition(this.transitionFactory)
        .tweenShapes(false)
        // .attributer(attributer)
        // .on("initEnd", render)
        .scale(1)
        .width(width)
        .height(height)
        .fit(true)
        .zoom(false)
        // .attr("font-family", function(d,i) {return i<5 ? "Arvo" : "Sancreek"; })
      // console.log(d3.select("#graph").attr("viewbox"));
      // .attr("width", 960)
      //   .attr("height", 500)
      //   .attr('viewbox', `0 0 300 600`)
      //   .call(responsivefy)
      console.log(this.g)
    },

    draw(dot) {
      this.g.transition(this.transitionFactory).renderDot(dot).on('renderEnd', this.interactive)
    },

    interactive() {
      this.nodes = d3.selectAll('.node')
      // console.log(this.nodes)

      // to make sure it works as toggle not infinitely-repeating increment,
      // let's create a custom attribute storing original rx and ry.
      this.nodes
        .on('mouseover', function() {
          // attempt to select the path (to access geometry variables)
          const node = d3.select(this)
          const path = d3.select(this).selectChild('path')

          // if baseRx doesn't exist, create it.
          if (node.attr('baseRx') == null)
            node.attr('baseRx', path.attr('rx'))
            // console.log('baseRx set!')

          // set rx to 1.2*bRx.
          const baseRx = node.attr('baseRx')
          // console.log(baseRx)
          path
            .transition()
            .duration('200')
            .attr('rx', baseRx * 1.2)

          // // opacity
          // node.transition()
          //   .duration('300')
          //   .attr('opacity', 0.5)
        })
        .on('mouseout', function() {
          const node = d3.select(this)
          const path = d3.select(this).selectChild('path')

          // set rx to bRx.
          const baseRx = node.attr('baseRx')
          path.transition().duration('200').attr('rx', baseRx)

          // node.transition()
          //   .duration('300')
          //   .attr('opacity', '1.0')
        })
      this.nodes.on('click', function() {
        // create a 'clicked' attribute
        const node = d3.select(this)
        const path = d3.select(this).selectChild('path')
        const courseName = this.textContent.split('\n')[1]
        const courses = JSON.parse(localStorage.getItem('courses'))

        const done = courses[courseName].done
        if (done)
          courses[courseName].done = false

        else
          courses[courseName].done = true

        localStorage.setItem('courses', JSON.stringify(courses))

        if (path.attr('baseColor') == null)
          path.attr('baseColor', path.attr('fill'))

        if (node.attr('clicked') == null || node.attr('clicked') == 'false')
          node.attr('clicked', true)

        else
          node.attr('clicked', false)

        if (node.attr('clicked') == 'true') {
          path.transition().duration('200').attr('fill', '#0d8201')
        }
        else {
          path
            .transition()
            .duration('200')
            .attr('fill', path.attr('baseColor'))
        }

        // d3.select(this)
        //   .transition()
        //   .duration("300")
        //   .attr("style", "font-weight: bold");
      })
    },
  },
}
</script>
