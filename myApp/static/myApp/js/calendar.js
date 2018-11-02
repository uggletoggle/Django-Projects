function deleteCalendarEntry(evento) {
    var $evento = $(evento)
    var id = $evento.data('id')
    $evento.parent().parent().remove()

    $.ajax({
        url :'/evento/delete/' + id,
        method : 'DELETE',
        beforeSend: function(xhr){
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        }
    })
}