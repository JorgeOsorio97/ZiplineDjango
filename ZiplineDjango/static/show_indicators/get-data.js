
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
$(function(){
	$('.EMA').change(function(){
  	if(!$(this).prop('checked')){
    	$('#days').hide();
    }else{
        $('#days').show();
    }
  
  })

})
$(function(){
	$('.SMA').change(function(){
  	if(!$(this).prop('checked')){
    	$('#days').hide();
    }else{
        $('#days').show();
    }
  
  })

})
$(function(){
	$('.SAR').change(function(){
  	if(!$(this).prop('checked')){
    	$('#sar').hide();
    }else{
        $('#sar').show();
    }
  
  })

})
$(function(){
	$('.KAMA').change(function(){
  	if(!$(this).prop('checked')){
    	$('#days').hide();
    }else{
        $('#days').show();
    }
  
  })

})
$(function(){
	$('.TEMA').change(function(){
  	if(!$(this).prop('checked')){
    	$('#days').hide();
    }else{
        $('#days').show();
    }
  
  })

})
$(function(){
	$('.TRIMA').change(function(){
  	if(!$(this).prop('checked')){
    	$('#days').hide();
    }else{
        $('#days').show();
    }
  
  })

})
$(function(){
	$('.WMA').change(function(){
  	if(!$(this).prop('checked')){
    	$('#days').hide();
    }else{
        $('#days').show();
    }
  
  })

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
        csrfmiddlewaretoken: '{{ csrf_token }}',
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
