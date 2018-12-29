$('#add_security').click( function (){
    console.log("enviando");
    
    $.ajax({
        url: '/show_indicators/new_security/',
        type : "post",
        dataType : "json",
        data : {
            name : $("#security_name").val(),
            code : $("#security_code").val(),
            market : $("#market").val(),
            csv_file : $("#csv_file").val()
        },
        succes:function(data){
            console.log("hola");
            console.log(data);
        },
        error:function(data){
            console.log("adios");
            console.log(data);
            
        }
        
    })
});