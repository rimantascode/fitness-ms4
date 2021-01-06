/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

$("#submit-button").click(function (e) {
    messages=[];
    // take and proccess the value of the full name
    var full_name = $("[name='full_name']").val();
    var inputRGEX = /[^a-zA-Z ]/g;
    var check_fullname = inputRGEX.test(full_name);
    var result_fullname = full_name.match(inputRGEX, "");
    var full_name_place_holder = $("[name='full_name']").attr('placeholder');

    //  take and proccess the value of the phone 
    var phone_number = $("[name='phone_number']").val();
    var phone_numberRGEX = /[^0-9]/g;
    var check_phoneNumber = phone_numberRGEX.test(phone_number);
    var result_phoneNamber = phone_number.match(phone_numberRGEX, "");
    var phone_number_place_holder = $("[name='phone_number']").attr('placeholder');

    // take and proccess the value of street 1
    var address_street_1 = $("[name='street_address1']").val();
    var adress_street1RGEX = /[^0-9a-zA-Z ]/g;
    var check_address_street_1 = adress_street1RGEX.test(address_street_1);
    var result_phoneNamber = address_street_1.match(adress_street1RGEX, "");
    var address_street_1_place_holder = $("[name='street_address1']").attr('placeholder');

    // take and proccess the value of street 2
    var address_street_2 = $("[name='street_address2']").val();
    var adress_street2RGEX = /[^0-9a-zA-Z ]/g;
    var check_address_street_2 = adress_street2RGEX.test(address_street_2);
    var result_address_street_2 = address_street_2.match(adress_street2RGEX, "");
    var address_street_2_place_holder = $("[name='street_address2']").attr('placeholder');

    //take and proccess the value of City and Town
    var town_or_city = $("[name='town_or_city']").val();
    var town_or_cityRGEX = /[^a-zA-Z ]/g;
    var check_town_or_city = town_or_cityRGEX.test(town_or_city);
    var result_town_or_city = town_or_city.match(town_or_cityRGEX, "");
    var town_or_city_place_holder = $("[name='town_or_city']").attr('placeholder');

    // take and proccess the value of Postal code
    var postcode = $("[name='postcode']").val();
    var postcodeRGEX = /[^0-9a-zA-Z ]/g;
    var check_postcode = postcodeRGEX.test(postcode);
    var result_postcode = postcode.match(postcodeRGEX, "");
    var postcode_place_holder = $("[name='town_or_city']").attr('placeholder');

    // take and proccess the value of county
    var county = $("[name='county']").val();
    var countyRGEX = /[^0-9a-zA-Z]/g;
    var check_county = countyRGEX.test(county);
    var result_county = county.match(countyRGEX, "");
    var county_place_holder = $("[name='county']").attr('placeholder');

    //validate full name
    if (check_fullname == true) {
       
        var message="Sorry, but these symbols ( " + result_fullname +" ) are not allowed in field " + "<strong>"+full_name_place_holder+"</strong>";
        $("[name='full_name']").addClass("border border-danger");
        $("[name='full_name']").focus();
        if ($("[name='full_name']").siblings("label").text() == "") {
            $("[name='full_name']").parent().prepend(
            $('<label class="text-danger" for="id_full_name">' + full_name_place_holder+'</label>'));
        }
        messages.push(message)
        e.preventDefault();
         
    } else {
        $(".error").text("All good");
        $("[name='full_name']").removeClass("border border-danger");
        $("[name='full_name']").siblings("label").remove();
    }
    // validate phone number
    if (check_phoneNumber == true) {
        message_number = "Sorry, but only NUMBERS are allowed in <strong>" + phone_number_place_holder + "</strong>";
        $("[name='phone_number']").addClass("border border-danger");
        $("[name='phone_number']").focus();
        if ($("[name='phone_number']").siblings("label").text() == "") {
            $("[name='phone_number']").parent().prepend(
            $('<label class="text-danger" for="id_phone_nmber">' + phone_number_place_holder + '</label>'));
        }
        messages.push(message_number);
        e.preventDefault();
        
    } else {
        $("[name='phone_number']").removeClass("border border-danger");
        $("[name='phone_number']").siblings("label").remove();
    }

    //validate street address 1
    if (check_address_street_1 == true) {
        message_street_1 = "Sorry, but these symbols ( " + result_phoneNamber + " ) are not allowed in field " + "<strong>" + address_street_1_place_holder + "</strong>";
        $("[name='street_address1']").addClass("border border-danger");
        $("[name='street_address1']").focus();
        if ($("[name='street_address1']").siblings("label").text() == "") {
            $("[name='street_address1']").parent().prepend(
            $('<label class="text-danger" for="id_street_address1">' + address_street_1_place_holder + '</label>'));
        }
        messages.push(message_street_1);
        e.preventDefault();

    } else {
        $("[name='street_address1']").removeClass("border border-danger");
        $("[name='street_address1']").siblings("label").remove();
    }

    //validate street address 2
    if (check_address_street_2 == true) {
        message_street_2 = "Sorry, but these symbols ( " + result_address_street_2 + " ) are not allowed in field " + "<strong>" + address_street_2_place_holder + "</trong>";
        $("[name='street_address2']").addClass("border border-danger");
        $("[name='street_address2']").focus();
        if ($("[name='street_address2']").siblings("label").text() == "") {
            $("[name='street_address2']").parent().prepend(
            $('<label class="text-danger" for="id_street_address2">' + address_street_2_place_holder + '</label>'));
            }
        messages.push(message_street_2);
        e.preventDefault();

    } else {
        $("[name='street_address2']").removeClass("border border-danger");
        $("[name='street_address2']").siblings("label").remove();
    }

    //validate town_or_city
    if (check_town_or_city == true) {
        message_town_or_city = "Sorry, but these symbols ( " + result_town_or_city + " ) are not allowed in field " + "<strong>" + town_or_city_place_holder + "</strong>" ;
        $("[name='town_or_city']").addClass("border border-danger");
        $("[name='town_or_city']").focus();
        if ($("[name='town_or_city']").siblings("label").text()== ""){
            $("[name='town_or_city']").parent().prepend(
            $('<label class="text-danger" for="id_town_or_city">' + town_or_city_place_holder + '</label>')); 
        }
        messages.push(message_town_or_city);
        e.preventDefault();

    } else {
        $("[name='town_or_city']").removeClass("border border-danger");
        $("[name='town_or_city']").siblings("label").remove();
    }
    
    //validate postcode
    if (check_postcode == true) {
        message_postcode = "Sorry, but these symbols ( " + result_postcode + " ) are not allowed in field " + "<strong>" + postcode_place_holder + "</strong>";
        $("[name='postcode']").addClass("border border-danger");
        $("[name='postcode']").focus();
        if ($("[name='postcode']").siblings("label").text() == "") {
            $("[name='postcode']").parent().prepend(
            $('<label class="text-danger" for="id_town_or_city">' + town_or_city_place_holder + '</label>'));
        }
        messages.push(message_postcode);
        e.preventDefault();

    } else {
        $("[name='postcode']").removeClass("border border-danger");
        $("[name='postcode']").siblings("label").remove();
    }
    //validate county
    if (check_county == true) {
        message_county = "Sorry, but these symbols ( " + result_county + " ) are not allowed in field " + "<strong>" + county_place_holder + "</strong>";
        $("[name='county']").addClass("border border-danger");
        $("[name='county']").focus();
        if ($("[name='county']").siblings("label").text() == "") {
            $("[name='county']").parent().prepend(
            $('<label class="text-danger" for="id_county">' + town_or_city_place_holder + '</label>'));
        }
        messages.push(message_county);
        e.preventDefault();

    } else {
        $("[name='county']").removeClass("border border-danger");
        $("[name='county']").siblings("label").remove();
    }
    
    text = "<ul>";
    messages.forEach(display_messages);
    text += "</ul>";
    $(".error").html(text);

    function display_messages(message_disp){
  
        text +="<li>" + message_disp +"</li>";
    }
      
});


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
  
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html =`
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    });
});
  
