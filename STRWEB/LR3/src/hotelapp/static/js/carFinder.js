// Базовый класс Car
function Car(brand, number) {
  this.brand = brand;
  this.number = number;
}

// Геттеры и сеттеры
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

// Метод для вывода информации о машине
Car.prototype.displayInfo = function() {
  return `Марка: ${this.brand}, Номер: ${this.number}`;
};

// Метод для добавления объекта
Car.prototype.addCarToList = function(carsArray) {
  carsArray.push(this);
};

// Класс-наследник OwnerCar
function OwnerCar(brand, number, owner) {
  Car.call(this, brand, number); // Вызов конструктора базового класса
  this.owner = owner;
}

// Наследование методов
OwnerCar.prototype = Object.create(Car.prototype);
OwnerCar.prototype.constructor = OwnerCar;

// Геттеры и сеттеры для владельца
OwnerCar.prototype.getOwner = function() {
  return this.owner;
};

OwnerCar.prototype.setOwner = function(owner) {
  this.owner = owner;
};

// Метод для вывода информации о владельце и машине
OwnerCar.prototype.displayFullInfo = function() {
  return `${this.displayInfo()}, Владелец: ${this.owner}`;
};

// Функция для поиска владельцев по марке
function findOwnersByBrand(carsArray, brand) {
  return carsArray.filter(car => car.getBrand() === brand)
                  .map(car => `${car.getOwner()} - ${car.getNumber()}`);
}

// Пример использования
const carsArray = [];
const car1 = new OwnerCar('Toyota', 'A123BC', 'Иванов');
const car2 = new OwnerCar('Honda', 'B456CD', 'Петров');
const car3 = new OwnerCar('Toyota', 'C789EF', 'Сидоров');

car1.addCarToList(carsArray);
car2.addCarToList(carsArray);
car3.addCarToList(carsArray);

console.log(findOwnersByBrand(carsArray, 'Toyota'));