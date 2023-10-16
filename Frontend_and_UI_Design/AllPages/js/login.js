function convertDivtoInput(divid,divuserid,defaultName) {
    const divContainer = document.getElementById(divid);
    divHTML = divContainer.innerHTML;
    const inputElement = document.createElement('input');
    inputElement.className = 'divtoinput'; // to give CSS
    if(typeof divContainer.value == 'undefined'){
        inputElement.value ="";
    }else{
        inputElement.value = divContainer.value;
    }
    inputElement.addEventListener('blur', () => {
        divContainer.innerHTML = divHTML;
        divContainer.value = inputElement.value;
        const divuser=document.getElementById(divuserid);
        if(inputElement.value==""){
            divuser.innerText = defaultName;
        }else{
            divuser.innerText = inputElement.value;
            if(divid=="password"){
                divuser.textContent = divuser.textContent.replace(/./g, '*');
            }
        }
        divContainer.className = divid;
        divContainer.style.display = 'flex';// for making non-none in display for username
        inputElement.remove();
    });
    divContainer.style.display = 'none';
    divContainer.parentNode.insertBefore(inputElement, divContainer.nextSibling);
    inputElement.focus();
}
