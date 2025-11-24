// bakground colour chang in button thorugh
let modeBtn=document.querySelector("#mood")
let currmode="light";
modeBtn.addEventListener("click",()=>{
 if (currmode === "light"){
    currmode="dark";
    document.querySelector('body').style.backgroundColor ="black";
}else{
      currmode="light"
      document.querySelector('body').style.backgroundColor ="white";
      
}
  console.log(currmode)
});