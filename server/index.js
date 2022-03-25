document.querySelector("#send_bttn").addEventListener('click', sendBIN);


async function sendBIN(e){
    let bin = document.querySelector("#bin").value;
    console.info(bin)
    let response = await fetch(`cards/${bin}`);
    console.info(response);
    if(response.status && response.status == 200){
        let json = await response.json();
        console.info(json);
    }else{
        let text = await response.text();
        console.info(text);
    }
}