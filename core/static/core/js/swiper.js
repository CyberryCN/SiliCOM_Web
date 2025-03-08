const imgList = [
    { img: window.STATIC_DATA.IMG_PREFIX + 'row_1.jpeg', text: '' },
    { img: window.STATIC_DATA.IMG_PREFIX + 'row_2.jpeg', text: '' },
    { img: window.STATIC_DATA.IMG_PREFIX + 'row_3.jpeg', text: '' }
];
const delay = 3000;
let img = document.querySelector('.slider-wrapper img');
let p = document.querySelector('.slider-footer p');
let i = 0;
// 设置初始状态
img.src = imgList[0].img;
p.innerText = imgList[0].text;

let fn = setInterval(function() {
    i++;
    if (i == imgList.length) {
        i = 0;
    }
    img.src = imgList[i].img;
    p.innerText = imgList[i].text;
    document.querySelector('.slider-indicators li.active').classList.remove('active');
    document.querySelector(`.slider-indicators li:nth-child(${i + 1})`).classList.add('active');
}, delay);

let prev = document.querySelector('.prev');
let next = document.querySelector('.next');

prev.addEventListener('click', function() {
    clearInterval(fn);
    i--;
    if (i < 0) {
        i = imgList.length - 1;
    }
    img.src = imgList[i].img;
    p.innerText = imgList[i].text;
    document.querySelector('.slider-indicators li.active').classList.remove('active');
    document.querySelector(`.slider-indicators li:nth-child(${i + 1})`).classList.add('active');
});

next.addEventListener('click', function() {
    clearInterval(fn);
    i++;
    if (i == imgList.length) {
        i = 0;
    }
    img.src = imgList[i].img;
    p.innerText = imgList[i].text;
    document.querySelector('.slider-indicators li.active').classList.remove('active');
    document.querySelector(`.slider-indicators li:nth-child(${i + 1})`).classList.add('active');
});

// 当鼠标悬停在按钮上时暂停轮播
prev.addEventListener('mouseenter', function() {
    clearInterval(fn);
});

next.addEventListener('mouseenter', function() {
    clearInterval(fn);
});

// 当鼠标离开按钮时重新启动轮播
prev.addEventListener('mouseleave', function() {
    fn = setInterval(function() {
        i++;
        if (i == imgList.length) {
            i = 0;
        }
        img.src = imgList[i].img;
        p.innerText = imgList[i].text;
        document.querySelector('.slider-indicators li.active').classList.remove('active');
        document.querySelector(`.slider-indicators li:nth-child(${i + 1})`).classList.add('active');
    }, delay);
});

next.addEventListener('mouseleave', function() {
    fn = setInterval(function() {
        i++;
        if (i == imgList.length) {
            i = 0;
        }
        img.src = imgList[i].img;
        p.innerText = imgList[i].text;
        document.querySelector('.slider-indicators li.active').classList.remove('active');
        document.querySelector(`.slider-indicators li:nth-child(${i + 1})`).classList.add('active');
    }, delay);
});

// 当鼠标悬停在轮播图上时暂停轮播
let sliderWrapper = document.querySelector('.slider-wrapper');
sliderWrapper.addEventListener('mouseenter', function() {
    clearInterval(fn);
});

// 当鼠标离开轮播图时重新启动轮播
sliderWrapper.addEventListener('mouseleave', function() {
    fn = setInterval(function() {
        i++;
        if (i == imgList.length) {
            i = 0;
        }
        img.src = imgList[i].img;
        p.innerText = imgList[i].text;
        document.querySelector('.slider-indicators li.active').classList.remove('active');
        document.querySelector(`.slider-indicators li:nth-child(${i + 1})`).classList.add('active');
    }, delay);
});