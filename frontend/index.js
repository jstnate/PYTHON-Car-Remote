const buttonKey = document.querySelectorAll('.direction-key');
const url = 'http://127.0.0.1:3000/'
const giro = document.getElementById('giro')
let giroStatus = 'off'
let direction

buttonKey.forEach((button) => {
    button.addEventListener('click', (e) => {
        direction = e.target.value
        sendDirection(direction, giroStatus)
    })
});

giro.addEventListener('click', e=>{
    giroStatus === 'off' ? giroStatus = 'on' : giroStatus = 'off'
    sendDirection(direction, giroStatus)
})


function sendDirection(direction, giro) {
    fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            direction: direction,
            giro: giro
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.log(error))
}
