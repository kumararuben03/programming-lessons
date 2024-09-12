<template>
    <Pie
    :options="chartOptions"
    :data="chartData"
    />
</template>

<script>
    import {Pie} from 'vue-chartjs'
    import {Chart as ChartJS, Tooltip, Legend, ArcElement} from 'chart.js'
    ChartJS.register(Tooltip, Legend, ArcElement)

    export default{
        name: 'PieChart',
        components: {Pie},
        data() {
            return{
                chartData: {
                    labels: ['Saving', 'Food', 'Transport', 'Room Rental','Others'],
                    datasets:[{
                        label: 'City X',
                        backgroundColor: ['#5cc0e9', '#f5a505','#dff505', '#0551f5', '#9305f5'],
                        data: [200, 500, 300, 1000, 250]
                    }]
                },
                chartOptions: {
                    responsive: true,
                    
                    plugins: {
                        title:{
                            display: true,
                            text: 'Monthly Expenses'
                        },
                    },
                }
            }
        }
    }
</script>