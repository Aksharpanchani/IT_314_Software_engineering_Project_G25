function validateForm(){
    var form1=document.forms["form1"];
    var age = form1["Age"];
    var height = form1["Height"];
    var weight = form1["Weight"];
    var systolicbp = form1["SystolicBP"];
    var diastolicbp = form1["DiastolicBP"];
    var cholestrol = form1["CholestrolLevel"];
    var glucose = form1["GlucoseLevel"];


    console.log(glucose.value);

    if(systolicbp.value<=0 || systolicbp.value>300)
    {
        alert("Invalid Systolic Blood Pressure");
        systolicbp.value="";
        return false;
    }

    if(diastolicbp.value<=0 || diastolicbp.value>300)
    {
        alert("Invalid Diastolic Blood Pressure");
        diastolicbp.value="";
        return false;
    }

    if(cholestrol.value<=0 || cholestrol.value>300)
    {
        alert("Invalid Cholestrol Level");
        cholestrol.value="";
        return false;
    }

    if(glucose.value<=0 || glucose.value>200)
    {
        alert("Invalid Glucose Level");
        glucose.value="";
        return false;
    }

    if(age.value<1 || age.value>120)
    {
        alert("Invalid Age");
        age.value="";
        return false;
    }  
    
    if(height.value<=30 || height.value>300)
    {
        alert("Invalid Height");
        height.value="";
        return false;
    }

    if(weight.value<=10 || weight.value>300)
    {
        alert("Invalid weight");
        weight.value="";
        return false;
    }


    return true;

}
