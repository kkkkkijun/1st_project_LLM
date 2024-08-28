
// =======================swiper===============================
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

// =====================time================================
  function printTime() {
    const today = new Date();
    const hours = document.querySelector(".hours");
    const minutes = document.querySelector(".minutes");
    const seconds = document.querySelector(".seconds");

    // 12시간제로 사용한다면 %12 나눈 나머지를 사용
    // 오후, 오전 붙일때는 앞에, am,pm는 뒤에 붙인다.
    hours.innerHTML = today.getHours();

    if (today.getMinutes() <= 9) {
      minutes.innerHTML = "0" + today.getMinutes();
    } else {
      minutes.innerHTML = today.getMinutes();
    }

    seconds.innerHTML = `${today.getSeconds()}`.padStart(2, "0");
  }

  printTime();

  //const timer = setInterval(printTime, 1000 * 60 * 60 * 24);
  const timer = setInterval(printTime, 1000);

  // =========================== questions ================================

let questions = document.querySelectorAll('.question .title');
let questionContainers = document.querySelectorAll('.question > .question_container');
let pushMinus = document.querySelectorAll('.question span');
let questionContents = document.querySelectorAll('.question .content');
let heights = [];

// heights 각 questionContainers의 높이 저장
function contentsHight(){
    heights = [];
    questionContents.forEach((questionContent) => {
        let height = questionContent.offsetHeight;
        heights.push(height);
    });
};
contentsHight();

// main 동작 코드
let FAQ = [];
questions.forEach((question, index) => {
    question.addEventListener('click', () => {
        if(!FAQ[index]){
            questionContainers[index].style.height = `${75 + heights[index]}px`;
            pushMinus[index].innerHTML = '+';
            pushMinus[index].style.fontSize = '35px';
            FAQ[index] = 1;
        }else{
            questionContainers[index].style.height = '75px';
            pushMinus[index].innerHTML = '-';
            pushMinus[index].style.fontSize = '50px';
            FAQ[index] = 0;
        };
    });
});

// 화면의 넓이에 따라 heights의 높이 갱신 및 questionContainers높이 조절
window.addEventListener('resize', () => {
    contentsHight();
    for(let index = 0; index < questionContainers.length; index++){
        if(FAQ[index]) {
            questionContainers[index].style.height = `${75 + heights[index]}px`;
        };
    };
});