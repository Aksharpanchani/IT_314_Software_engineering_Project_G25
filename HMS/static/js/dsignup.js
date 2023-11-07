function validateForm(){
    var form1=document.forms["form1"]
    var firstName = form1["first_name"];
    var lastName = form1["last_name"];
    var email = form1["email"];
    var password = form1["pass1"];
    var cpassword = form1["pass2"];


    // Trim the input values to remove leading and trailing spaces
    if (firstName.value.trim().indexOf(" ") !== -1 || lastName.value.trim().indexOf(" ") !== -1) {
        alert("Name Input should not contain blank spaces.");
        firstName.value = "";
        lastName.value = "";
        return false;
    }
    const validRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(!email.value.match(validRegex)){
        alert("Invalid Email.");
        email.value = "";
        return false;
    }
    if(password.value!=cpassword.value){
        alert("Password not matching with Confirm Password.");
        password.value = "";
        cpassword.value = "";
        return false;
    }
    return true;
}
