const socket = new WebSocket('ws://localhost:8000/ws/sensors');
const temp_chart = createChart("temperaturechart", 'temperature(Celsius)');
const humidity = createChart("humiditychart", 'humidity(%)');

function createChart(element_id, label){
    const chart = document.getElementById(element_id).getContext('2d');
    return new Chart(chart, {
        type: 'line',
        data:{
            labels: [],
            datasets:[{
                label: label,
                data: [],
                boarderColor: "black",
                boarderWidth: 1
            }]
        },
        options:{
            scales:{
                y:{beginAtZero: true}
            }
        }
    });
}

