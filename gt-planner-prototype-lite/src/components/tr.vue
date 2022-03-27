<template>
  <Renderer ref="renderer" alpha antialias resize="window">
    <Camera :position="{ z: 5 }" />
    <Scene background="#191919">
      <PointLight :color="light1Color" :position="{ x: -2 , y: -2, z: 2 }" :intensity="0.5" />
      <PointLight :color="light2Color" :position="{ x: -2 , y: 2, z: 2 }" :intensity="0.5" />
      <PointLight :color="light3Color" :position="{ x: 2 , y: 2, z: 2 }" :intensity="0.5" />
      <PointLight :color="light4Color" :position="{ x: 2 , y: -2, z: 2 }" :intensity="0.5" />
      <Tube v-for="t in tubes" :ref="t.key" v-bind="t">
        <StandardMaterial :props="{ roughness: 0.4, metalness: 1 }" />
      </Tube>
    </Scene>
    <EffectComposer>
      <RenderPass />
      <!-- <UnrealBloomPass :strength="1" /> -->
      <!-- <HalftonePass :radius="1" :scatter="0" /> -->
      <HalftonePass :radius="1" :scatter="0.1" />
    </EffectComposer>
  </Renderer>
</template>

<script lang="ts">
import { Vector3 } from 'three'
import SimplexNoise from 'simplex-noise'
import chroma from 'chroma-js'

import {
  AmbientLight,
  Camera,
  PointLight,
  Renderer,
  Scene,
  StandardMaterial,
  Tube,
} from 'troisjs'

const NX = 40
const NY = 15
const RADIUS = 0.1

const simplex = new SimplexNoise()

export default {
  name: "bg",
  components: {
    AmbientLight,
    Camera,
    PointLight,
    Renderer,
    Scene,
    StandardMaterial,
    Tube,
  },
  data() {
    return {
      tubes: [],
      light1Color: '#000000', // '#b307b5',
      light2Color: '#4a4a4a',
      light3Color: '#000000',
      light4Color: '#4a4a00',
    }
  },
  mounted() {
    this.renderer = this.$refs.renderer
    this.size = this.renderer.three.size
    console.log(this.size)
    this.initTubes()

    const pPositionN = this.renderer.three.pointer.positionN
    this.renderer.onBeforeRender(() => {
      const time = Date.now() * 0.00005
      let points, x, y, x1, y1, noisey, noisez
      for (let j = 0; j < NY; j++) {
        points = this._points[j]
        for (let i = 0; i < NX; i++) {
          x = this.x0 + i * this.dx; x1 = x * 0.25
          y = this.y0 + j * this.dy; y1 = y * 0.25
          noisey = simplex.noise2D(x1 - time + pPositionN.x * 0.3, y1 - time + pPositionN.y * 0.3) * 0.3
          noisez = simplex.noise2D(y1 + time, x1 + time) * 0.3
          points[i].x = x
          points[i].y = y + noisey
          points[i].z = noisez
        }
        this.$refs[this.tubes[j].key][0].updatePoints(points)
        // console.log(this.$refs[this.tubes[j].key][0].updatePoints)
      }
    })

    // this.renderer.onResize(() => {
    //   this.initTubes();
    // });
  },
  methods: {
    initTubes() {
      this._points = [] // point copy (not reactive)
      this.tubes.splice(0)
      this.dx = this.size.wWidth / (NX - 1)
      this.dy = this.size.wHeight / (NY - 1)
      this.x0 = -this.size.wWidth / 2
      this.y0 = -this.size.wHeight / 2
      for (let j = 0; j < NY; j++) {
        const points = []
        this._points[j] = []
        for (let i = 0; i < NX; i++) {
          const v = new Vector3(this.x0 + i * this.dx, this.y0 + j * this.dy, 0)
          points.push(v)
          this._points[j].push(v.clone())
        }
        this.tubes.push({
          key: `tube-${j}`,
          points,
          radius: RADIUS,
          tubularSegments: NX,
          radialSegments: 8,
        })
      }
    },
    randomColors() {
      this.light1Color = chroma.random().hex()
      this.light2Color = chroma.random().hex()
      this.light3Color = chroma.random().hex()
      this.light4Color = chroma.random().hex()
    },
  },
}
</script>

<style>
canvas {
  width: 100vw;
  height: 100vh;
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 0;
}
</style>
