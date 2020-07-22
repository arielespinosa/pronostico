function message_success_file(){
    message = '<article class="media">' +
        '<span class="pull-left thumb-sm" style="padding-top: 9%;"><i class="fa fa-bell fa-2x"></i></span>'+                
        '<div class="media-body">' +
        '<div class="pull-right media-xs text-center text-muted">' +
        '<br>' +
        '</div>' +
        '<small class="block m-t-sm">'+"hola mensage"+'</small>' +   
        '</div></article>';

    $.amaran({
        'theme'     :'colorful',
        'content'   :{		
            bgcolor: SUCCESS_COLOR,
            color:'#fff',
            message: message,
        },
        'cssanimationIn'    :'bounceInRight',
        'cssanimationOut'   :'slideBottom',
        'position'  		:'bottom right',
        'sticky'        :true,
        'closeOnClick'  :false,
        'closeButton'   :true
    }); 
}