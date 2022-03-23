<template>
  <div
    id="graph"
    style="
      text-align: center;
      width: 70%;
      height: 700px;
      border: 1px solid black;
    "
  />
</template>

<script>
// d3-graphviz
import * as d3 from "d3";
import "d3-graphviz";

// load webassembly
let wasm = document.createElement("script");
wasm.setAttribute("src", "https://unpkg.com/@hpcc-js/wasm/dist/index.min.js");
wasm.setAttribute("type", "application/javascript"); // it works but I don't know why..
document.head.appendChild(wasm);

function transitionFactory() {
  return d3.transition("main").delay(130).duration(1000);
}

// function responsivefy(svg) {
//   // get container + svg aspect ratio
//   var container = d3.select(svg.node().parentNode),
//     width = parseInt(svg.style("width")),
//     height = parseInt(svg.style("height")),
//     aspect = width / height;

//   // add viewBox and preserveAspectRatio properties,
//   // and call resize so that svg resizes on inital page load
//   svg
//     .attr("viewBox", "0 0 " + width + " " + height)
//     .attr("perserveAspectRatio", "xMinYMid")
//     .call(resize);

//   // to register multiple listeners for same event type,
//   // you need to add namespace, i.e., 'click.foo'
//   // necessary if you call invoke this function for multiple svgs
//   // api docs: https://github.com/mbostock/d3/wiki/Selections#on
//   d3.select(window).on("resize." + container.attr("id"), resize);

//   // get width of container and resize svg to fit it
//   function resize() {
//     var targetWidth = parseInt(container.style("width"));
//     svg.attr("width", targetWidth);
//     svg.attr("height", Math.round(targetWidth / aspect));
//   }
// }

export default {
  data() {
    return {
      curr: null,
    };
  },
  methods: {
    // call after vue loads (i.e. mounted())
    attach_graphviz() {
      const graphContainer = d3.select("#graph");
      const width = graphContainer.node().clientWidth;
      const height = graphContainer.node().clientHeight;
      console.log(width, height);

      this.g = d3
        .select("#graph")
        .graphviz()
        // .logEvents(true)
        .transition(transitionFactory)
        .tweenShapes(false)
        // .attributer(attributer)
        // .on("initEnd", render)
        .scale(1)
        .width(width)
        .height(height)
        .fit(true)
        .zoom(false);
      console.log(d3.select("#graph").attr("viewbox"));
      // d3.select('#graph').append("svg")
      // .attr("width", 960)
      //   .attr("height", 500)
      //   .attr('viewbox', `0 0 300 600`)
      //   .call(responsivefy)
    },

    draw(dot) {
      this.g.renderDot(dot).on("renderEnd", this.interactive);
    },

    interactive() {
      this.nodes = d3.selectAll(".node");
      // console.log(this.nodes)

      // to make sure it works as toggle not infinitely-repeating increment,
      // let's create a custom attribute storing original rx and ry.
      this.nodes
        .on("mouseover", function () {
          // attempt to select the ellipse (to access geometry variables)
          const node = d3.select(this);
          const ellipse = d3.select(this).selectChild("ellipse");

          // if baseRx doesn't exist, create it.
          if (node.attr("baseRx") == null) {
            node.attr("baseRx", ellipse.attr("rx"));
            // console.log('baseRx set!')
          }
          // set rx to 1.2*bRx.
          const baseRx = node.attr("baseRx");
          // console.log(baseRx)
          ellipse
            .transition()
            .duration("200")
            .attr("rx", baseRx * 1.2);

          // // opacity
          // node.transition()
          //   .duration('300')
          //   .attr('opacity', 0.5)
        })
        .on("mouseout", function () {
          const node = d3.select(this);
          const ellipse = d3.select(this).selectChild("ellipse");

          // set rx to bRx.
          const baseRx = node.attr("baseRx");
          ellipse.transition().duration("200").attr("rx", baseRx);

          // node.transition()
          //   .duration('300')
          //   .attr('opacity', '1.0')
        });
      this.nodes.on("click", function () {
        // create a 'clicked' attribute
        const node = d3.select(this);
        const ellipse = d3.select(this).selectChild("ellipse");
        console.log(this.textContent);

        if (ellipse.attr("baseColor") == null) {
          ellipse.attr("baseColor", ellipse.attr("fill"));
        }

        if (node.attr("clicked") == null || node.attr("clicked") == "false") {
          node.attr("clicked", true);
        } else {
          node.attr("clicked", false);
        }

        if (node.attr("clicked") == "true") {
          ellipse.transition().duration("200").attr("fill", "#0d8201");
        } else {
          ellipse
            .transition()
            .duration("200")
            .attr("fill", ellipse.attr("baseColor"));
        }

        d3.select(this)
          .transition()
          .duration("300")
          .attr("style", "font-weight: bold");
      });
    },
  },

  mounted() {
    this.attach_graphviz();
  },
};
</script>
