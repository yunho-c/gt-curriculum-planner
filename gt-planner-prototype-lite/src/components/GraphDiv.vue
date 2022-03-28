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
// import 'd3-graphviz'


// load webassembly
const wasm = document.createElement('script')
wasm.setAttribute('src', 'https://unpkg.com/@hpcc-js/wasm/dist/index.min.js')
wasm.setAttribute('type', 'application/javascript') // it works but I don't know why..
document.head.appendChild(wasm)

function transitionFactory2() {
  return d3.transition('main').delay(130).duration(1000)
}

export default {
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
      return d3.transition("main").delay(130).duration(1000)
    },
    attach_graphviz() {
      const graphContainer = d3.select('#graph')
      // // console.log(graphContainer)
      // // console.log(d3)
      const width = graphContainer.node().clientWidth
      const height = graphContainer.node().clientHeight

      // console.log(d3.select('#graph').graphviz().graphvizVersion())

      console.log(this.transitionFactory)

      // this.g = d3.select('#graph').graphviz()
      this.g = d3Graphviz.graphviz('#graph')
      // this.g = graphviz('#graph')
        .logEvents(true)
        .transition(this.transitionFactory) // .tweenShapes(false)
        .width(width).height(height)
        .fit(true)
        .zoom(false)
      // console.log(this.g)
      // this.g.transition.duration = '1000'
      // console.log(this.g.transition.duration)
        // .on('renderEnd', console.log('a'))
        // .on('renderEnd', this.draw('digraph {a -> b}'))
    },
    draw(dot) {
      // this.g.renderDot(dot)
      // const t = d3.transition('main').duration(750)
      // console.log(t)
      // this.g.transition(d3.transition()).renderDot(dot)
      // this.g.transition(this.transitionFactory)
      // console.log(this.g)
      this.g.renderDot(dot).on('renderEnd', this.interactive)
      // console.log(this.g)
      // this.g.transition(this.transitionFactory).renderDot(dot) // .on('renderEnd', this.interactive)
    },

    interactive() {
      const nodes = d3.selectAll('.node') // ; console.log(this.nodes)

      // hover event
      nodes
        .on('mouseover', function() {
          const node = d3.select(this)
          const path = d3.select(this).selectChild('path')

          // if baseRx doesn't exist, create it.
          if (node.attr('baseRx') == null) node.attr('baseRx', path.attr('rx'))// ; console.log('baseRx set!')

          // set rx to 1.2*baseRx
          path
            .transition()
            .duration('200')
            .attr('rx', node.attr('baseRx') * 1.2)

          // // set opacity to 0.5
          // node.transition()
          //   .duration('300')
          //   .attr('opacity', 0.5)
        })
        .on('mouseout', function() {
          const node = d3.select(this)
          const path = d3.select(this).selectChild('path')

          // revert rx
          path.transition().duration('200').attr('rx', node.attr('baseRx'))

          // revert opacity
          // node.transition()
          //   .duration('300')
          //   .attr('opacity', '1.0')
        })

      // click event
      nodes.on('click', function() {
        const node = d3.select(this)
        const path = d3.select(this).selectChild('path')
        const courseName = this.textContent.split('\n')[1]

        // manipulate localStorage
        const courses = JSON.parse(localStorage.getItem('courses'))
        const done = courses[courseName].done
        if (done) courses[courseName].done = false
        else courses[courseName].done = true
        localStorage.setItem('courses', JSON.stringify(courses))

        // set baseColor
        if (path.attr('baseColor') == null) path.attr('baseColor', path.attr('fill'))

        // toggle 'clicked'
        if (node.attr('clicked') === 'true') node.attr('clicked', 'false')
        else node.attr('clicked', 'true')

        if (node.attr('clicked') === 'true') path.transition().duration('200').attr('fill', '#0d8201')
        else path.transition().duration('200').attr('fill', path.attr('baseColor'))
      })
    },
  },
}
</script>
