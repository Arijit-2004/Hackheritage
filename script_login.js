const wrap = document.querySelector('.wrap');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const iconClose = document.querySelector('.icon-close');

    wrap .classList.add('active-popup');

iconClose.addEventListener('click',()=>{
    wrap .classList.remove('active-popup');
})
registerLink.addEventListener('click',()=>{
    wrap .classList.add('active');
})
loginLink.addEventListener('click',()=>{
    wrap .classList.remove('active');
})
