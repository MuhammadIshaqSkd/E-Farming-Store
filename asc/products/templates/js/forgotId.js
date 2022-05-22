
<script>
$('#trackerForms').submit(function(event) {
    var formData = {
        'cnic': $('input[name=cnic]').val(),
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    };
    $.ajax({
            type: 'POST',
            url: '/products/forgot_id/',
            data: formData,
            encode: true
        })
        .done(function(data) {
            $('#titems').empty();
            console.log(data)
            data = JSON.parse(data);
            if (data['status'] == 'okay') {

//            For display total number of orders
                ids = data['ids'];
                for (i = 0; i < ids.length; i++) {
                    let order_id = ids[i]['order_id'];
                    mystr3 = `<li>
                    ${order_id}
                    </li>`
                }
//                ENDS--------------------------------------------------------

//                  For Append data into ids --------------------

                    $('#titems').append(mystr3);
                }
//                ENDS----------------------------------

                // Fill in the order details
                cart = JSON.parse(data['itemsJson']);
                console.log(cart);
                for (item in cart) {
                    let name = cart[item][1];
                    let qty = cart[item][0];
                    mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                    ${name}
                    <span class="badge badge-primary badge-pill">${qty}</span>
                </li>`
                    $('#ritems').append(mystr);
                }
            } else {
                mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                    Sorry, We are not able to fetch this order id and CNIC. Make sure to type correct order Id and CNIC</li>`
                $('#titems').append(mystr);
            }
        });
    event.preventDefault();
});
</script>