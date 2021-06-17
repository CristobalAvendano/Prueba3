fn_ocultarEtiquetas();


function fn_ocultarEtiquetas() {

    $('#lbl_nombre').hide();
    $('#lbl_contrasena').hide();
    $('#lbl_error_login').hide();
}

function fn_nombreVacio() {

    var nombre = $('#txt_nombre').val();

    if (nombre == "") {

        $('#lbl_nombre').show();

        $('#txt_nombre').addClass('is-invalid');

    }

    else {

        $('#lbl_nombre').hide();

        $('#txt_nombre').removeClass('is-invalid');

        $('#txt_nombre').addClass('is-valid');

    }

    function fn_contrasenaVacia() {

        var contrasena = $('#txt_contrasena').val();

        if (contrasena == "") {

            $('#lbl_contrasena').show();

            $('#txt_contrasena').addClass('is-invalid');

        }
        else {

            $('#lbl_contrasena').hide();

            $('#txt_contrasena').removeClass('is-invalid');

            $('#txt_contrasena').addClass('is-valid');
        }
    } fn_contrasenaVacia();

    function fn_loginCorrecto() {
        var nombre = $('#txt_nombre').val();
        var contrasena = $('#txt_contrasena').val();

        if (nombre == 'admin' && contrasena == 'admin') {
            window.location.href = "/index.html"
        }
        else {
            $('#lbl_error_login').show();
            $('#txt_contrasena').removeClass('is-valid');
            $('#txt_contrasena').addClass('is-invalid');
            $('#txt_nombre').removeClass('is-valid');
            $('#txt_nombre').addClass('is-invalid');

        }


    } fn_loginCorrecto();
}