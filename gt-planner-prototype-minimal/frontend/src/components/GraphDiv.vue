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
        .delay(130)
        .duration(1000);
}

// function interactive() {

//     nodes = d3.selectAll('.node,.edge');
//     nodes
//         .on("click", function () {
//             var title = d3.select(this).selectAll('title').text().trim();
//             var text = d3.select(this).selectAll('text').text();
//             var id = d3.select(this).attr('id');
//             var class1 = d3.select(this).attr('class');
//             dotElement = title.replace('->',' -> ');
//             console.log('Element id="%s" class="%s" title="%s" text="%s" dotElement="%s"', id, class1, title, text, dotElement);
//             console.log('Finding and deleting references to %s "%s" from the DOT source', class1, dotElement);
//             for (i = 0; i < dotSrcLines.length;) {
//                 if (dotSrcLines[i].indexOf(dotElement) >= 0) {
//                     console.log('Deleting line %d: %s', i, dotSrcLines[i]);
//                     dotSrcLines.splice(i, 1);
//                 } else {
//                     i++;
//                 }
//             }
//             dotSrc = dotSrcLines.join('\n');
//             render();
//         });
// }


export default {
  methods: {
    // call after vue loads (i.e. mounted())
    attach_graphviz() {
      this.g = d3.select("#graph").graphviz()
      // .logEvents(true)
      .transition(transitionFactory)
      .tweenShapes(false)
      .attributer(attributer);
      // .on("initEnd", render)
    },

    draw(dot) {
      this.g.renderDot(dot)
        .on('renderEnd', this.interactive)
    },

    interactive() {
      this.nodes = d3.selectAll('.node');
      // console.log(this.nodes)

      // to make sure it works as toggle not infinitely-repeating increment,
      // let's create a custom attribute storing original rx and ry.
      this.nodes
        .on('mouseover', function () {
          // attempt to select the ellipse (to access geometry variables)
          const node = d3.select(this)
          const ellipse = d3.select(this).selectChild('ellipse')
          // console.log(ellipse)

          // inspect
          console.log(this)
          console.log(node)
          console.log(ellipse)

          // if baseRx doesn't exist, create it. 
          if (node.attr('baseRx') == null) {
            node.attr('baseRx', ellipse.attr('rx'))
            console.log('baseRx set!')
          }
          // set rx to 1.2*bRx.
          const baseRx = node.attr('baseRx')
          console.log(baseRx)
          ellipse
            .transition()
            .duration('200')
            .attr('rx', baseRx*1.2)

          // // opacity
          // node.transition()
          //   .duration('300')
          //   .attr('opacity', 0.5)
        })
        .on('mouseout', function () {
          const node = d3.select(this)
          const ellipse = d3.select(this).selectChild('ellipse')

          // set rx to bRx.
          const baseRx = node.attr('baseRx')
          ellipse
            .transition()
            .duration('200')
            .attr('rx', baseRx)

          // node.transition()
          //   .duration('300')
          //   .attr('opacity', '1.0')
        })
      this.nodes
        .on('click', function() {
            d3.select(this).transition()
            .duration('300')
            .attr('style', 'font-weight: bold')
            console.log(this)
            console.log(d3.select(this))
        })
    }
  },

  mounted() {
    this.attach_graphviz()
  }
}
</script>
