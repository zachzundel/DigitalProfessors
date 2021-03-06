function updateBilled() {
    let start = $('#id_start_time').val();
    let end = $('#id_end_time').val();
    let date = $('#id_date').val();
    let hourly = $('#id_hourly').val();

    if(start && end && date && hourly) {
        let start_dt = new Date(date + ' ' + start);
        let end_dt = new Date(date + ' ' + end);
        let difference = end_dt - start_dt;
        let hours = difference / (1000 * 60 * 60);
        hours = Math.round(hours * 2) / 2;
        let billed = hours * hourly;

        if(billed < 30) {
            billed = 30;
        }

        billed = billed.toFixed(2);

        $('#id_billed').val(billed);
    }
}

$(document).on('blur', '#id_start_time', updateBilled);
$(document).on('blur', '#id_end_time', updateBilled);
$(document).on('blur', '#id_date', updateBilled);
$(document).on('blur', '#id_hourly', updateBilled);

$(document).ready(function () {
    $('#id_start_time').clockpicker({
        donetext: 'Done'
    });
    
    $('#id_end_time').clockpicker({
        donetext: 'Done'
    });
})