<template>
    <Doughnut
    :options="chartOptions"
    :data="chartData"
    />
</template>

<script>
    import {Doughnut} from 'vue-chartjs'
    import {Chart as ChartJS, Tooltip, Legend, ArcElement} from 'chart.js'
    ChartJS.register(Tooltip, Legend, ArcElement)

    export default{
        name: 'DoughnutChart',
        components: {Doughnut},
        data() {
            return{
                chartData: {
                    labels: ['A', 'B', 'C', 'D','E', 'F'],
                    datasets:[{
                        label: 'City X',
                        backgroundColor: ['#5cc0e9', '#f5a505','#dff505', '#0551f5', '#9305f5','#eef505'],
                        data: [320, 250, 180, 100, 80, 70]
                    }]
                },
                chartOptions: {
                    responsive: true,
                    
                    plugins: {
                        title:{
                            display: true,
                            text: 'Test Samples from January to March 2024'
                        },
                    },
                }
            }
        }
    }
</script>