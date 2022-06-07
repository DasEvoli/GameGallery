<template>
  <Bar
    :chart-data="chartData"
    :styles="styles"
    :chart-options="chartOptions"
    :title-text="titleText"
    :x-tick-display="xTickDisplay"
  />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    titleText: {
      default: "Default Text"
    },
    xTickDisplay:{
      type:Boolean,
      default: true
    },
    styles: {
      type:Object,
      default: () => {
      }
    },
    chartData: {
        labels: null,
        datasets: null
      }
  },
  data() {
    return {
      chartOptions: {
        aspectRatio: 1.5,
        plugins: {
          legend: {
            display: false
          },
          title: {
            display: true,
            text: this.titleText,
            color: "#ebebeb"
          }
        },
        scales: {
          x: {
            grid: {
              color: "#ffffff29"
            },
            ticks:{
              color: "#ebebeb",
              display: this.xTickDisplay
            }
          },
          y: {
            grid: {
              color: "#ffffff29"
            },
            ticks:{
              color: "#ebebeb"
            }
          },
          grid: {
            display: false
          },
        }
      }
    }
  },
  mounted(){
  },
  methods: {
  }
}
</script>