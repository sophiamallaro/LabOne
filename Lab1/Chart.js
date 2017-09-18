var ctx = document.getElementById("chart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'scatter',
    data: {
        datasets: [{
            label: 'Temperature',
            data: [{
                x: 0,
                y: 0
            }]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        title: {
            display: true,
            text: "Temperature Over Time"
        },
        scales: {
            xAxes: [{
                type: 'linear',
                position: 'bottom'
            }],
            yAxes: [{
                max: 50,
                scaleStartValue: 10,
            }],
        }
    },
});

function addData() {
    myChart.data.datasets[0].data[myChart.data.datasets[0].data.length] = {x: 8, y: 50};
    myChart.update();
}
