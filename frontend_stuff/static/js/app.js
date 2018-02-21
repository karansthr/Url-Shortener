    var clipboard = new Clipboard('.btn');

    clipboard.on('success', function(e) {
            e.clearSelection();

        setTooltip(e.trigger, 'Copied!');
        hideTooltip(e.trigger);
    });

    clipboard.on('error', function(e) {
        setTooltip(e.trigger, 'Failed!');
        hideTooltip(e.trigger);
    });

    $('#copy-button').tooltip({
      trigger: 'click',
      placement: 'bottom'
    });

    function hideTooltip(btn) {
      setTimeout(function() {
        $(btn).tooltip('hide');
      }, 1000);
    }

    function setTooltip(btn, message) {
      $(btn).tooltip('hide')
        .attr('data-original-title', message)
        .tooltip('show');
    }


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

    $('#divB').hide()

    var $myForm = $('#url_shortener_form');
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $(this).serialize()
        $.ajax({
            method: "POST",
            url: '/shorten',
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    });

    function invalidFeedback(message) {
        var t = '<div  class="invalid-feedback">'+ message + '</div>'
        return t;
    }

    function handleFormSuccess(response){

        $('#id_link').removeClass("is-invalid");
        $('#div_id_link > div:nth-child(2) > .invalid-feedback').empty();
        $('#id_suggestion').removeClass("is-invalid");
        $('#div_id_suggestion > div:nth-child(2) > .invalid-feedback').empty();


        if(response.message){
            var str = response.message;
            var json = JSON.parse(str);
            if(json['link']) {
                if (!$('#id_link').hasClass('is-invalid')) {
                    $('#div_id_link > div:nth-child(2)').append(invalidFeedback(json['link']));
                    $('#id_link').addClass("is-invalid");
                }
            }

            if(json['suggestion']){
                $('#div_id_suggestion > div:nth-child(2)').append(invalidFeedback(json['suggestion']));
                $('#id_suggestion').addClass("is-invalid");
            }
        }
        else
        if(response.status != 404) {
            $('#foo').val(response.trimmed_url);
            $('#divA').fadeOut("slow");
            $('#divA').hide();
            $('#divB').fadeIn();
        }
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)
    }
