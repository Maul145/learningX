// Tooggle class active--------x----------x-----x--->
const navbarNav = document.querySelector('.navbar-nav');

//  ketika hamburger di klik--------x----------x-----x--->
document.querySelector('#hamburger-menu').onclick = () => {
    navbarNav.classList.toggle('active');
};

// klik diluar sidebar untuk menghilangkan nav--------x----------x-----x--->
const hamburger = document.querySelector('#hamburger-menu');
document.addEventListener('click', function(e){
    if(!hamburger.contains(e.target) && !navbarNav.contains(e.target)) {
        navbarNav.classList.remove('active');
    }
})