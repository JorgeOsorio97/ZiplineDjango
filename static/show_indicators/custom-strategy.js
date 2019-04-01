$('#customStrategy').click( function (){
    
    $.ajax({
        url: '/show_indicators/get_personalized_result/',
        type : "post",
        dataType : "json",
        data : {
            init_date : $("#init_date").val(),
            end_date : $("#end_date").val(),
            quantity : $("#quantity").val(),
            security : $("#security").val(),
            strategy_type : $("#selectStrategy").val(),
        }   
    }).done((data)=>{
        console.log(data);  
    }).fail((data)=>{ 
        console.log(data);
    })
});