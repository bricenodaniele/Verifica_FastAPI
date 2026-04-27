async function calcolaIMC() {
    let a = document.getElementById("peso").value;
    let b = document.getElementById("altezza").value;
    if (!peso || !altezza ) 
        return alert("Scrivi  un peso e  un altezza");
    
    let response = await fetch(`/imc?a=${a}&b=${b}`);
    let data = await response.json();

    document.getElementById("risultato").innerText = "Il tuo IMC è: " + data.risultato;
     }
async function CalocloIMC_conPost() {

    const a = document.getElementById("peso").value;
    const b = document.getElementById("altezza").value;

    if (!peso || !altezza)
        return alert("Scrivi il pesa e la altezza");

    const res = await fetch("/imc2", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `a=${peso}&b=${altezza}`
       
    });
 const json = await res.json();

         }
   
    document.getElementById('btn_calcoloIMC').addEventListener('click', calcolaIMC);