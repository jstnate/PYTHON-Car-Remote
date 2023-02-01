const buttonKey = document.querySelectorAll('button');
const url = 'http://127.0.0.1:3000/'

buttonKey.forEach((button) => {
    button.addEventListener('click', (e) => {
        sendDirection(e.target.value)
    })
});

function sendDirection(direction) {
    fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            direction: direction
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.log(error))
}
