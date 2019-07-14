const startTimer = display => {
    let minutes, seconds;
    daun = setInterval(() => {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
            fetch('http://127.0.0.1:8000/api/create?type=1&time='+timing, {
                method: 'POST',
                mode: 'cors',
                credentials: 'include',
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json',
                }
            }).then(function (response) {
                if (!response.ok) {
                    throw Error(response.statusText);
                }
                location.reload(true);
                return console.log(response.json());


            });
            clearInterval(daun);
            document.querySelector('#start').disabled = false;
        }
    }, 1000);
};
let daun;
const duration = timing*60;
let timer = duration;
let flag = 0;
window.onload = () => {
    const display = document.querySelector('#time');
    document.querySelector('#start').addEventListener('click', () => {
        if (flag === 1) {
            flag = 0;
            clearInterval(daun);
            document.querySelector('#pause').id = 'start';
            return
        }
        flag = 1;
        startTimer(display);
        document.querySelector('#start').id = 'pause';
        return false;

    });
    document.querySelector('#restart').addEventListener('click', () => {
        timer = duration;
        flag = 1;
        document.querySelector('#start').id = 'pause';
        clearInterval(daun);
        startTimer(display);
        document.querySelector('#start').disabled = true;
    });
};
