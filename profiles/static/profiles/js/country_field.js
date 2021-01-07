// This code was copied from the code instite project
//It will change the color to match the placeholder
let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#726d6d');
}
//if the country selected it will change the color
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#726d6d');
    } else {
        $(this).css('color', '#000');
    }
});
