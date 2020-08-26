$(document).ready(function () {
    $(".alert").slideDown(1000);
    $(".alert").each((index, element) => {
        let timeout = 5000; // success
        if ($(element).hasClass('alert-warning')) {
            timeout = 10000;
        }
        if ($(element).hasClass('alert-danger')) {
            timeout = 15000;
        }
        setTimeout(() => {
            $(element).slideUp(1000, null, () => {
                $(element).alert('close');
                $(element).on('closed.bs.alert', () => {
                    alerts = document.getElementsByClassName('alert');
                    if (alerts.length == 0) {
                        $('#alerts-container').remove();
                    }
                });
            });
        }, timeout);
    });
});