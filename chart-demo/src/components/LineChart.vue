<template>
    <Line
    :options="chartOptions"
    :data="chartData"
    />
</template>

<script>
    import {Line} from 'vue-chartjs'
    import {Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement} from 'chart.js'
    ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

    export default{
        name: 'LineChart',
        components: {Line},
        data() {
            return{
                chartData: {
                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                    datasets:[{
                        label: 'City X',
                        backgroundColor: ['#5cc0e9', '#f5a505','#dff505', '#f50584', '#9305f5', '#2df505',],
                        data: [30, 26, 28, 31, 29, 27]
                    }]
                },
                chartOptions: {
                    responsive: true,
                    scales: {
                        x: {
                            display: true,
                            title:{
                                display: true,
                                text: 'Month'
                            }
                        },

                        y: {
                            display: true,
                            title: {
                                display: true,
                                text: 'Temperature in Celsius Degree'
                            }
                        }      
                    },
                    plugins: {
                        title:{
                            display: true,
                            text: 'Monthly Average Temperature (Jan-June, 2024)'
                        },
                    },
                }
            }
        }
    }
</script>