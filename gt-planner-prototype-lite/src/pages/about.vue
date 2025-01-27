<template>
  <p>
    <router-link to="/">
      Home
    </router-link>
  </p>
  <h1 text-9xl fw400 op90>
    Intro
  </h1>
  <p text-lg>
    <span style="color: #c39d4c">GT-Planner</span> is an experimental application that calculates an optimal 4-year academic plan for your time in Georgia Tech.
    <!-- It analyzes the pre-requisite relationships so that you can visually see in what order you'd need to take classes. -->
  </p>
  <h1 text-9xl fw400 op90>
    Motivation
  </h1>
  <p text-lg>
    <span style="color: #c39d4c">GT-Planner</span> was a passion project inspired by the awesome <a href="https://gt-scheduler.org/"><span style="color: #c39d4c"><i>GT Scheduler</i></span></a>. <br><br>
    Throughout my first year, I kept wondering: "Why is it so <span text-xs op70>fucking</span> hard to plan out upcoming semesters?" <br>
    Well, no wonder: it is a complex optimization problem with a large number of multiplicit variables:
    <ul>
      <li>• the pre-requisite relationship between courses,</li>
      <li>• the availability of courses in a certain semester,</li>
      <li>• the quality of professors teaching the sections,</li>
      <li>• balancing the load across semesters,</li>
      <li>• course availability constraints in study-abroads,</li>
      <li>• taking classes together with your friends,</li>
      <li>• add light mode,</li>
      <li>... and possibly much more.</li>
    </ul>
    <br>
    Normally, we end up tracking all these variables in our heads, making our best decisions based on our intuition and heuristics—which works. <br>
    But when you have a busy schedule (that registration takes place in the middle of hell week of the semester doesn't help), this can be mentally taxing. <br>
    Plus, <a href="https://www.secondrightanswer.com/home/2021/5/8/you-only-college-once-by-makayla-sheehan">YOCO</a> (<a href="https://quchronicle.com/30573/opinion/yoco-you-only-college-once/">You Only College Once</a>). What if that one elective that is only available in <a href="https://europe.gatech.edu/en"><span style="color: #c39d4c">GT-Lorraine</span></a> ends up unveiling a life-changing passion of yours?
  </p>
  <h1 text-9xl fw400 op90>
    <s>Planned Features</s>
  </h1>
  <p />
  <ul>
    <li>• a suitable data structure to represent user-defined constraints (overrides),</li>
    <li>• showing possible degree requirements (for majors with threads or otherwise large flexibility),</li>
    <li>• better (actually usable) UI,</li>
    <li>• a constraint to take the same section with your friends,</li>
    <li>• a way to explore cool classes that are offered,</li>
  </ul>
  <h1 text-9xl fw400 op90>
    Contribute!
  </h1>
  <p>
    All of the source code is available on <a href="https://github.com/yunho-c/gt-curriculum-planner/"><span style="color: #4c1b6b">GitHub</span></a>. <br>
    It is extremely messy (sorry), but I will gladly review as PRs that are submitted!
  </p>
</template>

<script lang="ts">
// export default {
//   data() {
//     return {
//     }
//   },
//   mounted() {
//     this.router = useRouter()
//   },
// }
</script>
