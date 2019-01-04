$('#submit').click( function (){
    console.log("enviando");
    
    $.ajax({
        url: '/show_indicators/strategy_creator/',
        type : "post",
        dataType : "json",
        data : {
            quantity : $("#quantity").val(),
        }   
    }).done((data)=>{
        console.log("hola");
        console.log(data);  
    }).fail((data)=>{
        console.log("adios"); 
        console.log(data);
    })
});