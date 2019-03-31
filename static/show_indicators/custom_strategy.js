$('#submit').click( function (){
    
    $.ajax({
        url: '/show_indicators/index/',
        type : "post",
        dataType : "json",
        data : {
            start_date : $("#init_date").val(),
            end_date : $("#end_date").val(),
            amount : $("#amount").val(),
            security : $("#security").val(),
            strategy_type : $("#selectStrategy").val(),
        }   
    }).done((data)=>{
        console.log(data);  
    }).fail((data)=>{ 
        console.log(data);
    })
});