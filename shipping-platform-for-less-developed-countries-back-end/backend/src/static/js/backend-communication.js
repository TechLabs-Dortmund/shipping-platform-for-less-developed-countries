const server = "http://127.0.0.1:8000"


function post_login() {

    const email = document.getElementById("input-email").value;
    const password = document.getElementById("input-password").value;
    const bodyPayload = JSON.stringify({email: email, password: password});
    axios.post(server + '/login', bodyPayload, {
            headers: {
            // Overwrite Axios's automatically set Content-Type
            'Content-Type': 'application/json'
            }
        })
        .then(resp => {
            console.log(resp.data);
            alert(JSON.stringify(resp.data));
            // TODO: do something after login
            
            if (resp.data.successful) {
                get_shipments()
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

function post_register() {
    const firstName = document.getElementById("fname").value;
    const lastName = document.getElementById("lname").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const phone = document.getElementById("phone").value;
    const bodyPayload = JSON.stringify({firstName: firstName, lastName: lastName, email: email, password: password, phone: phone});
    axios.post(server + '/register', bodyPayload, {
            headers: {
            // Overwrite Axios's automatically set Content-Type
            'Content-Type': 'application/json'
            }
        })
        .then(resp => {
            console.log(resp.data);
            alert(JSON.stringify(resp.data));
            if (resp.status == 200) {
                window.location.href = "/static/index.html"
            }
            // TODO: do something after register
            
            if (resp.data.successful) {
                get_shipments()
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}




function get_shipments() {
    axios.get(server + '/get-shipments')
    .then(resp => {
        console.log(resp.data);
        alert(JSON.stringify(resp.data));
        // TODO: do something after login
    })
    .catch(function (error) {
        console.log(error);
    });
}
