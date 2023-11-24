const username=document.querySelector(".username");
const password=document.querySelector(".password");
const error=document.querySelector(".error");
const body=document.querySelector("body");

body.addEventListener("click",()=>{
    console.log(error.innerText);
    error.innerHTML="";
})