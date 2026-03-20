
let div1 = document.querySelector("#div1");
let btn2 = document.querySelector("#btn2");

btn2.addEventListener("click", () =>{
    if (btn2.textContent === "OFF"){
        btn2.textContent = "ON";
        div1.classList.toggle("add1");
    }else if (btn2.textContent === "ON"){
        btn2.textContent = "OFF";
    }
});
























