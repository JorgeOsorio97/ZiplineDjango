$('#add_security').click( function (){
    $.ajax({
        url: 
        type="post",
        dataType = "json",
        data = {
            name = $("#security_name").val(),
            code = $("#security_code").val(),
            market = $("#market").val(),
            csv_file = $("#csv_file").val()
        },
        url:'show_indicators/new_security',
        succes:function(data){
            console.log(data);
            
        }
    })

});