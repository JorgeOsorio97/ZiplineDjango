
$('#enviar').click( () =>{
    console.log('hola');
    $.ajax({
        url: '/show_indicators/get-data',
        data: {'url':$('#security').val()},
        dataType: 'json',
        success: (res) => {
            console.log('success');
            console.log(res.URL);
        }
      });
}); 

