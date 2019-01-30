function whichOptionIsChecked() {
    if (document.getElementById('op-bloodBank').checked) {
        document.getElementById('div-bloodBank').style.display = "inline";
        document.getElementById('div-hospital').style.display = "none";
        document.getElementById('div-personal').style.display = "none";
    }
    if (document.getElementById('op-hospital').checked) {
        document.getElementById('div-bloodBank').style.display = "none";
        document.getElementById('div-hospital').style.display = "inline";
        document.getElementById('div-personal').style.display = "none";
    }
    if (document.getElementById('op-personal').checked) {
        document.getElementById('div-bloodBank').style.display = "none";
        document.getElementById('div-hospital').style.display = "none";
        document.getElementById('div-personal').style.display = "inline";
    }
}

function signup(link) {
    let password, confirmPassword;
    if (!link.localeCompare('/ursignup')) {
        password = document.getElementById("person-Password").value;
        confirmPassword = document.getElementById("person-confirmPass").value;
    } else if (!link.localeCompare('/hpsignup')) {
        password = document.getElementById("hospital-password").value;
        confirmPassword = document.getElementById("hospital-confirmPass").value;
    } else if (!link.localeCompare('/bbsignup')) {
        password = document.getElementById("bloodBank-password").value;
        confirmPassword = document.getElementById("bloodBank-confirmPass").value;
    }

    if (!password.localeCompare(confirmPassword))
    {
        var n = password.length;
        if (n < 8)
        {
            alert("Password should be more than 8 characters");
            return false;
        }
        else
        {
            if (!link.localeCompare('/ursignup'))
            {
                var selected = $('#bg-options').find(":selected").text();
                $.ajax({
                    url: '/ursignup',
                    type: 'post',
                    data: {
                        person_name: $('input[name="person-name"]').val(),
                        person_username: $('input[name="person-username"]').val(),
                        person_Email: $('input[name="person-Email"]').val(),
                        person_Password: $('input[name="person-Password"]').val(),
                        person_location: $('input[name="person-location"]').val(),
                        person_city: $('input[name="person-city"]').val(),
                        person_SeqQues: $('input[name="person-SeqQues"]').val(),
                        person_phone: $('input[name="person-phone"]').val(),
                        person_SeqAns: $('input[name="person-SeqAns"]').val(),
                        person_bloodgroup: (selected),
                    },
                    success: function (data) {
                        if (!data.status) {
                            return false;
                        } else {
                            alert("Account Created");
                           window.location = "http://127.0.0.1:8080/login";
                            return true;
                        }
                    }
                });
            }
            else if(!link.localeCompare('/hpsignup'))
            {
                var selected = $('#bg-options').find(":selected").text();

                $.ajax({
                    url: '/hpsignup',
                    type: 'post',
                    data: {
                        hospital_name: $('input[name="hospital-name"]').val(),
                        hospital_location: $('input[name="hospital-location"]').val(),
                        hospital_city: $('input[name="hospital-city"]').val(),
                        hospital_contact: $('input[name="hospital-contact"]').val(),
                        hospital_Email: $('input[name="hospital-Email"]').val(),
                        hospital_password: $('input[name="hospital-password"]').val(),
                        hospital_licence: $('input[name="hospital-licence"]').val(),
                        hospital_seqQues: $('input[name="hospital-seqQues"]').val(),
                        hospital_seqAns: $('input[name="hospital-seqAns"]').val(),
                    },
                    success: function (data) {
                        if (!data.status) {
                            return false;
                        } else {
                            alert("Account Created");
                            window.location = "http://127.0.0.1:8080/login";
                            return true;
                        }
                    }
                });
            }
            else if(!link.localeCompare('/bbsignup'))
            {
                $.ajax({
                    url: '/bbsignup',
                    type: 'post',
                    data: {
                        bloodBank_campName: $('input[name="bloodBank-campName"]').val(),
                        bloodBank_campEmail: $('input[name="bloodBank-campEmail"]').val(),
                        bloodBank_password: $('input[name="bloodBank-password"]').val(),
                        bloodBank_seqQues: $('input[name="bloodBank-seqQues"]').val(),
                        bloodBank_seqAns: $('input[name="bloodBank-seqAns"]').val(),
                        bloodBank_location: $('input[name="bloodBank-location"]').val(),
                        bloodBank_city: $('input[name="bloodBank-city"]').val(),
                        bloodBank_contact: $('input[name="bloodBank-contact"]').val(),
                    },
                    success: function (data) {
                        if (!data.status) {
                            return false;
                        } else {
                            alert("Account Created");
                            window.location = "http://127.0.0.1:8080/login";
                            return true;
                        }
                    }
                });
            }
            return false;
        }
    }
    else
    {
        alert("Both Passwords Don't Match");
        return false;
    }
}


function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("pwd").value;
    var n = password.length;

    if (n < 8) {
        alert("Password should be more than 8 digits");
        return false;
    } else {
        $.ajax({
            url: '/checkLogin',
            type: 'post',
            data: {
                email: email,
                password: password,
            },
            success: function (data) {
                if (data.status) {
                    if(data.value == 1){
                        window.location = "http://127.0.0.1:8080/bloodBank";
                    }
                    else if(data.value == 2){
                        window.location = "http://127.0.0.1:8080/hospital";
                    }
                    else if(data.value == 3){
                        window.location = "http://127.0.0.1:8080/personal";
                    }
                    return true;
                }
                else{
                    alert("Credentials incorrect!");
                }

            }
        });
    }
}


function search() {
    console.log("started");

    $.ajax({
        url: '/searchQuery',
        type: 'post',
        data: {
            query: $('input[name="search"]').val(),
        },

        success: function (data) {
            if (data.status) {
                console.log("ajaaaaaaxxx");
                document.getElementById("search-items").style.display = "flex";
            }
        }
    })
}