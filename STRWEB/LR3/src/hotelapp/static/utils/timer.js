document.addEventListener('DOMContentLoaded', function() {
  let timeLeft;
  const savedTime = localStorage.getItem("timeLeft");
  if (savedTime) {
    timeLeft = parseInt(savedTime, 10);
  } else {
    timeLeft = 59*60 + 59;
  }
  let timerId = null;
  const minutesElement = document.querySelector('.timer-minutes');
  const secondsElement = document.querySelector('.timer-seconds');

  function declensionNum(num, words) {
    return words[(num % 100 > 4 && num % 100 < 20) ? 2 : [2, 0, 1, 1, 1, 2][(num % 10 < 5) ? num % 10 : 5]];
  }

  function countdownTimer() {
    if (timeLeft <= 0) {
      clearInterval(timerId);
      localStorage.removeItem('timeLeft');
    }

    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;

    minutesElement.textContent = minutes;
    secondsElement.textContent = seconds;

    minutesElement.dataset.title = declensionNum(minutes, ['минута', 'минуты', 'минут']);
    secondsElement.dataset.title = declensionNum(seconds, ['секунда', 'секунды', 'секунд']);
    if (timeLeft > 0) {
      timeLeft--;
    }
    localStorage.setItem('timeLeft', timeLeft);
  }

  countdownTimer();

  timerId = setInterval(countdownTimer, 1000);
});