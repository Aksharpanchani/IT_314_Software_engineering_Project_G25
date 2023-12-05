function validateForm(){
    var form1=document.forms["form1"];
    var age = form1["Age"];
    var bmi = form1["BMI"];

    if(age.value<1 || age.value>120)
    {
        alert("Invalid Age");
        age.value="";
        return false;
    }  
    
    if(bmi.value<=0 || bmi.value>100)
    {
        alert("Invalid BMI");
        bmi.value="";
        return false;
    }
    return true;

}
