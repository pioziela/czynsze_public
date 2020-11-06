$("#id_wspolnota").change(function () {
    const url = $("#naliczenieForm").attr("data-wspolnoty-url");
    const wspolnotaId = $(this).val();

    $.ajax({
        url: url,
        data: {
            'wspolnota_id': wspolnotaId
        },
        success: function (data) {
            $("#id_wlasciciel").html(data);
        }
    });

});