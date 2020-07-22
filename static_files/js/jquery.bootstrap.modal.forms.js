/*
django-bootstrap-modal-forms
version : 1.4.2
Copyright (c) 2018 Uros Trstenjak
https://github.com/trco/django-bootstrap-modal-forms
*/
var SUCCESS_COLOR = '#65bd77';

function message_success(data){
    message = '<article class="media">' +
        '<span class="pull-left thumb-sm" style="padding-top: 9%;"><i class="fa fa-bell fa-2x"></i></span>'+                
        '<div class="media-body">' +
        '<div class="pull-right media-xs text-center text-muted">' +
        '<br>' +
        '</div>' +
        '<small class="block m-t-sm">'+data.message+'</small>' +   
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

(function ($) {
    //console.log("modalContent")
    // Open modal & load the form at formURL to the modalContent element
    var newForm = function (modalID, modalContent, modalForm, formURL, errorClass, submitBtn, elementID) {
        $(modalContent).load(formURL, function () {
            $(modalID).modal("show");
            $(modalForm).attr("action", formURL);
            // Add click listener to the submitBtn
            ajaxSubmit(modalID, modalContent, modalForm, formURL, errorClass, submitBtn, elementID);
        });
        
    };

    // Submit form callback function
    var submitForm = function(modalForm) {
        $(modalForm).submit(); 
    }

    // Add click listener to the submitBtn
    var ajaxSubmit = function (modalID, modalContent, modalForm, formURL, errorClass, submitBtn, elementID) {
        $(submitBtn).on("click", function () {
            // Check if form.is_valid() via ajax request when submitBtn is clicked
            
            isFormValid(modalID, modalContent, modalForm, formURL, errorClass, submitBtn, submitForm, elementID);
        });
    };

    // Check if form.is_valid() & either show errors or submit it
    var isFormValid = function (modalID, modalContent, modalForm, formURL, errorClass, submitBtn, elementID, callback) {
        
        $.ajax({
            type: $(modalForm).attr("method"),
            url: $(modalForm).attr("action"),
            // Serialize form data
            data: $(modalForm).serialize(),
            // success: function (response, modalID, data, textStatus, jqXHR)
            success: function (response) {  
                console.log(response)  
                if (typeof(response) == typeof('a')) {
                    
                    // Form is not valid, update it with errors
                    $(modalID).find(modalContent).html(response);
                    $(modalForm).attr("action", formURL);
                    
                    // Reinstantiate click listener on submitBtn
                    ajaxSubmit(modalID, modalContent, modalForm, formURL, errorClass, submitBtn, elementID);
                } else {
                    console.log(response)
                    // Hide modal form                    
                    $(modalID).modal("hide");
                    
                    // Show message success with json response as content
                    message_success(response);  
                                        
                    //Esto es nuevo
                    //si acaso borrar
                }
            }
       
          
        });
       
    };


    $.fn.modalForm = function (options) {
        // Default settings
        var defaults = {
            modalID: "#modal",
            modalContent: ".modal-content",
            modalForm: ".modal-content form",
            formURL: null,
            errorClass: ".errorlist",
            submitBtn: ".submit-btn",

            //Added by user
            elementID: options.elementID,
        };

        // Extend default settings with provided options
        var settings = $.extend(defaults, options);

        return this.each(function () {
            // Add click listener to the element with attached modalForm
            $(this).click(function (event) {
                // Instantiate new modalForm in modal
                newForm(settings.modalID,
                    settings.modalContent,
                    settings.modalForm,
                    settings.formURL,
                    settings.errorClass,
                    settings.submitBtn,
                    settings.elementID);
            });
        });
    };

}(jQuery));
