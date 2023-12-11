const carsTable = document.querySelector('.main-page-machines');
const maintenancesTable = document.querySelector('.main-page-maintenance');
const claimsTable = document.querySelector('.main-page-claims');

const btnCars = document.querySelector('.info-btn-cars');
const btnMaintenance = document.querySelector('.info-btn-maintenance');
const btnClaims = document.querySelector('.info-btn-claims');

const searchCarsBtn = document.querySelector('.search-cars-btn');
const searchMaintenanceBtn = document.querySelector('.search-maintenance-btn');
const searchClaimsBtn = document.querySelector('.search-claims-btn');

const headerLogo = document.querySelector('.header-logo');

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM готов!");
    console.log(localStorage.getItem('search'));
    maintenancesTable.classList.add('hidden');
    carsTable.classList.add('hidden');
    claimsTable.classList.add('hidden');

    console.log(localStorage.getItem('search'));
    if (localStorage.getItem('search')) {
        document.querySelector(localStorage.getItem('search')).classList.remove('hidden');
    } else {
        document.querySelector('.main-page-machines').classList.remove('hidden');
    }
    
  });

searchCarsBtn.addEventListener('click', () => {
    console.log('search Cars');
    localStorage.setItem('search', '.main-page-machines');
    
});

searchMaintenanceBtn.addEventListener('click', () => {
    console.log('search Maintenance');
    localStorage.setItem('search', '.main-page-maintenance');
    
});

searchClaimsBtn.addEventListener('click', () => {
    console.log('search Claims');
    localStorage.setItem('search', '.main-page-claims');
    
});


btnCars.addEventListener('click', () => {
    carsTable.classList.remove('hidden');
    maintenancesTable.classList.add('hidden');
    claimsTable.classList.add('hidden');
});

btnMaintenance.addEventListener('click', () => {
    maintenancesTable.classList.remove('hidden');
    carsTable.classList.add('hidden');
    claimsTable.classList.add('hidden');
});

btnClaims.addEventListener('click', () => {
    claimsTable.classList.remove('hidden');
    carsTable.classList.add('hidden');
    maintenancesTable.classList.add('hidden');
    
});

headerLogo.addEventListener('click', () => {
    localStorage.setItem('search', '.main-page-machines');
});