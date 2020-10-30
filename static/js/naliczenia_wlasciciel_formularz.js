<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

<script>
    $("#id_wspolnota").change(function () {
        const url = $("#naliczenieForm").attr("data-wspolnoty-url");  // get the url of the `load_wspolnoty` view
        const wspolnotaId = $(this).val();  // get the selected wspolnota ID from the HTML input

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= ajax/load_wspolnoty/ )
            data: {
                'wspolnota_id': wspolnotaId       // add the wspolnota id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_wspolnoty` view function
                $("#id_wlasciciel").html(data);  // replace the contents of the wlasciciel input with the data that came from the server
                /*

                let html_data = '<option value="">---------</option>';
                data.forEach(function (wlasciciel) {
                    html_data += `<option value="${wlasciciel.id}">${wlasciciel.name}</option>`
                });
                console.log(html_data);
                $("#id_wlasciciel").html(html_data);

                */
            }
        });

    });
</script>