
$('#enviar').click(() => {
    console.log('hola');
    $.ajax({
        url: '/show_indicators/get-data',
        data: { 'url': $('#security').val() },
        dataType: 'json',
        success: (res) => {
            console.log('success');
            console.log(res.URL);
            plotData('/show_indicators/result',$('#security').val())
        }
    });
});
function plotData(dir,name) {
    Plotly.d3.csv(dir, function (err, rows) {   

        function unpack(rows, key) {
            return rows.map(function (row) { return row[key]; });
        }


        var trace1 = {
            type: "scatter",    
            mode: "lines",
            name: 'High',
            x: unpack(rows, 'FECHA'),
            y: unpack(rows, 'MAXIMO'),
            line: { color: '#17BECF' }
        }

        var trace2 = {
            type: "scatter",
            mode: "lines",
            name: 'Low',
            x: unpack(rows, 'FECHA'),
            y: unpack(rows, 'MINIMO'),
            line: { color: '#7F7F7F' }
        }
        var trace3 = {
            type: "scatter",
            mode: "lines+markets",
            name: 'ProMovShort',
            x: unpack(rows, 'FECHA'),
            y: unpack(rows, 'ProMovShort'),
            line: { color: '#2eb82e' },
            marker: { color: '#2eb82e', size: 4 }
        }

        var trace4 = {
            type: "scatter",
            mode: "lines+markers",
            name: 'ProMovLong',
            x: unpack(rows, 'FECHA'),
            y: unpack(rows, 'ProMovLong'),
            line: { color: '#ff0000' },
            connectgaps: true
        };

        var data = [trace1, trace2, trace3, trace4];

        var layout = {
            title: name ,
            xaxis: {
                autorange: true,
                range: ['1993-02-17', '2013-02-16'],
                rangeselector: {
                    buttons: [
                        {
                            count: 5,
                            label: '5y',
                            step: 'year',
                            stepmode: 'backward'
                        },
                        { step: 'all' }
                    ]
                },
                rangeslider: { range: ['2000-02-17', '2013-02-16'] },
                type: 'date'
            },
            yaxis: {
                autorange: true,
                range: [86.8700008333, 138.870004167],
                type: 'linear'
            }
        };

        Plotly.newPlot('myDiv', data, layout);
    })
}
