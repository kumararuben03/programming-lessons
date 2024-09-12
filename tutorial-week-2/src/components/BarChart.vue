<template>
    <Bar
    :options="chartOptions"
    :data="chartData"
    />
</template>

<script>
    import {Bar} from 'vue-chartjs'
    import {Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale} from 'chart.js'
    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

    export default{
        name: 'BarChart',
        components: {Bar},
        data() {
            return{
                chartData: {
                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    datasets:[{
                        label: 'Set 1',
                        backgroundColor:'#5cc0e9',
                        borderColor: '#5cc0e9',
                        data: [5200, 4800, 6100, 5500, 7200, 8100, 9300, 8700, 7600, 6900, 6300, 7800],
                    },
                    {
                        label: 'Set 1',
                        backgroundColor:'#f5a505',
                        borderColor: '#f5a505',
                        data: [5200, 4800, 6100, 5500, 7200, 8100, 9300, 8700, 7600, 6900, 6300, 7800],
                        type: 'line'
                    },]
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
                                text: 'Sales Price ($)'
                            }
                        }      
                    },
                    plugins: {
                        title:{
                            display: true,
                            text: 'Company Sales Revenue in ($)'
                        },
                        legend:{
                            display: false,
                        }
                    },
                }
            }
        }
    }
</script>