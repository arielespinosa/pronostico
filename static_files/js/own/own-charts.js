//--Variables Globales----------------------------
var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
};

var config = {
    type: 'line',
    data: {
        labels: [['June', '2015'], 'July', 'August', 'September', 'October', 'November', 'December', ['January', '2016'], 'February', 'March', 'April', 'May'],
        datasets: [{
            label: 'My First dataset',
            fill: false,
            backgroundColor: window.chartColors.red,
            borderColor: window.chartColors.red,
            data: [
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor()
            ]
        }, {
            label: 'My Second dataset',
            fill: false,
            backgroundColor: window.chartColors.blue,
            borderColor: window.chartColors.blue,
            data: [
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor()
            ],
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Chart with Multiline Labels'
        },
    }
};

//--Plotea un grafo lineal----------------------------
function PlotLineChart(ctx){
    var myChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
            datasets: [{
                label: 'Number of Votes',
                data: [12, 19, 13, 15, 20, 17],
                data: [22, 15, 10, 11, 14, 13],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',                            
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',                            
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                display: false
            }
        }
    });
};


function PlotMultiLineChart(ctx2){
    window.myLine = new Chart(ctx2, config);
};

$(document).ready(function () {  

    var titulo = document.title;
    
    //var ctx = document.getElementById("myChart").getContext('2d');
    //PlotLineChart(ctx);
 /*
    if(titulo.indexOf("|") == -1){      
      var ctx2 = document.getElementById('canvas').getContext('2d');
      PlotMultiLineChart(ctx2);
    };
 */
  });			 

