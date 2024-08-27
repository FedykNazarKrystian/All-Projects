const socket = new WebSocket('ws://localhost:8000/ws/sensors');
const temp_chart = createChart("temperaturechart", 'temperature(Celsius)');
const humidity = createChart("humiditychart", 'humidity(%)');

socket.onmessage = function (event){
    const data = JSON.parse(event.data);
    const chart = data.sensor_id == "temperaturechart" ? temp_chart : humidity;
    updateChart(chart, data);
}

function updateChart(chart, data){
    chart.data.labels.push(new Date().toLocaleTimeString());
    chart.data.datasets[0].data.push(data.med_value);
    chart.update();
}
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

