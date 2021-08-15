$('#btn-submit-review').click(function () {
    console.log("Aye!")
    var name = $('#input-name').val();
    var email = $('#input-email').val();
    var review = $('#input-review').val();

    var data = {}
    data['name'] = name;
    data['email'] = email;
    data['review'] = review;

    console.log(data)

    $.ajax({
        type: "POST",
        url: "/api/review/create/",
        data: data,
        dataType: "json",
        success: function (response) {
            console.log("success mengirim");
            console.log(response);
        }
    });
});

$('#btn-submit-review').click(function () {
    console.log("Aye!")
    var name = $('#input-name').val();
    var email = $('#input-email').val();
    var review = $('#input-review').val();

    var data = {}
    data['name'] = name;
    data['email'] = email;
    data['review'] = review;

    console.log(data)

    $.ajax({
        type: "POST",
        url: "/api/review/create/",
        data: data,
        dataType: "json",
        success: function (response) {
            console.log("success mengirim");
            console.log(response);
        }
    });
});

// $('#btn-submit-review').click(function () {
    
// }