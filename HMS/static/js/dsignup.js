function updateFileName(input) {
    var file = input.files[0]; /* if uploaded multiple files will only take first file*/
    var fileName = file.name;
    if(file.size/(1024**2) > 10){
        alert("File too big!!");
        return;
    }
    document.getElementById('file-label').innerText = fileName;
  }

function validateForm(){
    var form1=document.forms["form1"]
    var firstName = form1["first_name"];
    var lastName = form1["last_name"];
    var email = form1["email"];
    var password = form1["pass1"];
    var cpassword = form1["pass2"];
    var number = form1["number"];
    var year = form1["birthdate"];  
    var birthyear = new Date(year.value).getFullYear();  
    var file = form1["certificate"];
    //console.log(number);

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
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!*%?&])[A-Za-z\d@.#$*!%?&]{8,15}$/;
    if(!password.value.match(regex)){
        alert("Your Password does not contain one of the following:- \n1.At least one lowercase alphabet \n2.At least one uppercase alphabet \n3.At least one Numeric digit \n4.At least one special character \n5.The total length must be in the range [8-15]");
        password.value = "";
        return false;
    }
    if(number.value.length!=10){
        alert("Invalid Number.");
        number.value = "";
        return false;
    }
    if(birthyear>2005)
    {
        alert("Invalid Date of birthdate");
        year.value="";
        return false;
    }
    if(file.files[0].size/(1024**2)>10){
        alert("File too big!!");
        return false;
    }
    return true;
}
