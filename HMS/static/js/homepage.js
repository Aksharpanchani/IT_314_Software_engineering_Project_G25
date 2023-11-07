function validateForm(){
    var form1=document.forms["form1"]
    var email = form1["email"];

    const validRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(!email.value.match(validRegex)){
        alert("Invalid Email.");
        email.value = "";
        return false;
    }
    return true;
}
