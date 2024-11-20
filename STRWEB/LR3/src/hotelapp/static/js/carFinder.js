// Базовый класс Car
function Car(brand, number) {
  this.brand = brand;
  this.number = number;
}

Car.prototype.getBrand = function() {
  return this.brand;
};

Car.prototype.setBrand = function(brand) {
  this.brand = brand;
};

Car.prototype.getNumber = function() {
  return this.number;
};

Car.prototype.setNumber = function(number) {
  this.number = number;
};

Car.prototype.displayInfo = function() {
  return `Марка: ${this.brand}, Номер: ${this.number}`;
};

Car.prototype.addCarToList = function(carsArray) {
  carsArray.push(this);
};

function OwnerCar(brand, number, owner) {
  Car.call(this, brand, number); 
  this.owner = owner;
}

OwnerCar.prototype = Object.create(Car.prototype);
OwnerCar.prototype.constructor = OwnerCar;

OwnerCar.prototype.getOwner = function() {
  return this.owner;
};

OwnerCar.prototype.setOwner = function(owner) {
  this.owner = owner;
};

OwnerCar.prototype.displayFullInfo = function() {
  return `${this.displayInfo()}, Владелец: ${this.owner}`;
};

function findOwnersByBrand(carsArray, brand) {
  return carsArray.filter(car => car.getBrand() === brand)
                  .map(car => `${car.getOwner()} - ${car.getNumber()}`);
}

const carsArray = [];
const car1 = new OwnerCar('Toyota', 'A123BC', 'Иванов');
const car2 = new OwnerCar('Honda', 'B456CD', 'Петров');
const car3 = new OwnerCar('Toyota', 'C789EF', 'Сидоров');

car1.addCarToList(carsArray);
car2.addCarToList(carsArray);
car3.addCarToList(carsArray);

console.log(findOwnersByBrand(carsArray, 'Toyota'));