async function calcolaIMC_conPost() {
    const pesoVal = document.getElementById("peso").value;
    const altezzaVal = document.getElementById("altezza").value;

    if (!pesoVal || !altezzaVal) {
        return alert("Inserisci tutti i valori richiesti");
    }

    const formData = new URLSearchParams();
    formData.append('peso', pesoVal);
    formData.append('altezza', altezzaVal);

    const res = await fetch("/imc2", {
        method: "POST",
        headers: { "Content-Type":"/workspaces/Verifica_FastAPI/IMC.xlsx" },
        body: formData
    });

    const data = await res.json();
    document.getElementById("risultato").innerText = `IMC calcolato: ${data.risultato}`;
}

document.getElementById('btn_calcoloIMC').addEventListener('click', calcolaIMC_conPost);