document.querySelector("#send_bttn").addEventListener('click', sendBIN);


async function sendBIN(e){
    let bin = document.querySelector("#bin").value;
    bin = bin.replace(/[ -]/g, '');
    let txt_area = document.querySelector("#response");
    if(bin.match(/^\d{16,20}$/)){
        let response = await fetch(`cards/${bin}`);
        console.info(response);
        if(response.status && response.status == 200){
            let json = await response.json();
            console.info(json);
            txt_area.value = `Карта ${json[1]} ${json[2]}, Банк ${json[4]}, ${json[7]}`;
        }else if(response.status && response.status == 404){
            txt_area.value = `Информация не найдена`;
        }else if(response.status && response.status == 500){
            let text = await response.text();
            console.info(text);
            txt_area.value = `Информация не найдена`;
        }else{
            console.info(response.text());
        }
    }else{
        txt_area.value = "Не верный формат номера карты";
    }
}