
// $('#enviar').click(() => {
//     console.log('hola');
//     $.ajax({
//         url: '/show_indicators/get-data',
//         data: { 'url': $('#security').val() },
//         dataType: 'json',
//         success: (res) => {
//             console.log('success');
//             console.log(res.URL);
//             plotData('/show_indicators/result',$('#security').val())
//         }
//     });
// });
function toggleIndicatorsParams(indicator){
    if(!$(indicator).prop('checked')){
        $('#days').hide();
    }else{
        $('#days').show();
    }
}

$(function(){
    $('.EMA').change(function(){toggleIndicatorsParams('.EMA')} );
    $('.SMA').change(function(){toggleIndicatorsParams('.SMA')} );
    $('.KAMA').change(function(){toggleIndicatorsParams('.KAMA')} );
    $('.TEMA').change(function(){toggleIndicatorsParams('.TEMA')} );
    $('.TRIMA').change(function(){toggleIndicatorsParams('.TRIMA')} );
    $('.WMA').change(function(){toggleIndicatorsParams('.WMA')} );
    $('.SAR').change(function(){
        if(!$(this).prop('checked')){
            $('#sar').hide();
        }else{
            $('#sar').show();
        }
    } );
})

//----Solicitar Best Strategy
$('#bestStrategy').click(()=>{
    console.log('solicitando best strategy');
    $.ajax({
        type: 'post',
        data:{
            security: $('#security').val()
        },
        url:'/show_indicators/bestStrategy/',
        success: function(data){
            console.log(data);
            var strategy = "";  
            for(var x in data.strategy){
                for(var y in data.strategy[x]){
                    strategy +=`Indicador: ${x} <br>
                                &nbsp parametros: <br>  `
                    for(var z in data.strategy[x][y]){
                        strategy += `&nbsp &nbsp ${z}: ${(data.strategy[x][y][z])} <br>`;
                    }
                }                
            }
            //console.log(strategy);|
            
            $('#bestStrategyResult').html(strategy);
        }
    });
})

$('#enviar').click(function() {
    var selected = [];
    $(":checkbox[name=indi]").each(function() {
      if (this.checked) {
        selected.push($(this).val());
      }
    });
    if (selected.length) {
      $.ajax({
        //cache: false,
        type: 'post',
        dataType: 'json', 
        data:{'security':$('#security').val(),'indicators': selected}, 
        csrfmiddlewaretoken: '{{ csrf_token }}', // TODO csrf token send cookie
        url: '/show_indicators/get-data/',
        success: function(data) {
          console.log('datos enviados');
        }
      });
      console.log(JSON.stringify(selected));
    } else
      alert('Debes seleccionar al menos un indicador.');

    return false;
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
            x: unpack(rows, 'Date'),
            y: unpack(rows, 'High'),
            line: { color: '#17BECF' }
        }

        var trace2 = {
            type: "scatter",
            mode: "lines",
            name: 'Low',
            x: unpack(rows, 'Date'),
            y: unpack(rows, 'Low'),
            line: { color: '#7F7F7F' }
        }
        var trace3 = {
            type: "scatter",
            mode: "lines+markets",
            name: 'ProMovShort',
            x: unpack(rows, 'Date'),
            y: unpack(rows, 'SMA-50_data'),
            line: { color: '#2eb82e' },
            marker: { color: 'j#2eb82e', size: 4 }
        }

        var trace4 = {
            type: "scatter",
            mode: "lines+markers",
            name: 'ProMovLong',
            x: unpack(rows, 'Date'),
            y: unpack(rows, 'SMA-20_data'),
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
        console.log('DONE');
        
    })
}
