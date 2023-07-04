
//message remove from the template
document.addEventListener('DOMContentLoaded', function() {
    var djangoMessages = document.querySelectorAll('.messages .alert');
    if (djangoMessages.length > 0) {
        setTimeout(function() {
            djangoMessages.forEach(function(message) {
                message.remove();
            });
        }, 2000);
    }
});

