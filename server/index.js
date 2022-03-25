document.querySelector("#send_bttn").addEventListener('click', sendBIN);


async function sendBIN(e){
    let bin = document.querySelector("#bin").value;
    let txt_area = document.querySelector("#response");
    if(bin.match(/^\b(?:\d[ -]*?){13,16}\b$/)){
        bin = bin.replace(/[ -]/g, '');
        let response = await fetch(`cards/${bin}`);
        console.info(response);
        if(response.status && response.status == 200){
            let json = await response.json();
            console.info(json);
            txt_area.value = `Карта ${json[1]} ${json[2]}, Банк ${json[4]}, ${json[7]}`;
        }else if(response.status && response.status == 500){
            let text = await response.text();
            console.info(text);
            txt_area.value = `Информация не найдена`;
        }else{
            console.info(response.text());
        }
    }else{
        txt_area.value = "Введите номера карты";
    }
}