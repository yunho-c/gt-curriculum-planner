<template>
  <div>
    <div>
      <v-select :options="majors" placeholder="Major" />
    </div>
    <!-- checkbox for debug -->
    <br />
    Completed:
    <div v-for="(content, course) in curr" :key="course.id">
      <label>{{ course }}</label>
      <input
        type="checkbox"
        v-model="content.done"
        :value="course"
        @change="onCheckBoxClick"
      />
    </div>
  </div>
</template>

<script>
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";

export default {
  name: "SetupPage",
  data() {
    return {
      a: "b",
      b: "d",
      majors: [
        {
          id: 0,
          label: "ME",
        },
        {
          id: 1,
          label: "BME",
        },
      ],
      curr: false,
    };
  },
  methods: {
    // make this actualy work (specify a major)
    fetch_curr() {
      let courses = JSON.parse(localStorage.getItem("courses"));
      if (courses != null) {
        this.curr = courses;
        return;
      }

      this.axios.get("http://localhost:8000/curr/ME").then((response) => {
        this.curr = response.data;
        localStorage.setItem("courses", JSON.stringify(this.curr));
      });
    },
    onCheckBoxClick(event) {
      const checked = event.target.checked;

      //   let courses = JSON.parse(localStorage.getItem("courses"));

      if (checked) return;
    },
  },
  components: {
    vSelect,
  },
  mounted() {
    this.fetch_curr();
  },
};
</script>