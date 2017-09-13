var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'scatter',
    data: {
        datasets: [{
            label: 'Temperature',
            data: [{
                x: 0,
                y: 20
            }, {
                x: 1,
                y: 40
            }]
        }]
    },
    options: {
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
                scaleStartValue: 10,
                max: 50,
            }],
        }
    },
});

function addData() {
    myChart.data.datasets[0].data[myChart.data.datasets[0].data.length] = {x: 3, y: 10};
    myChart.update();
}
