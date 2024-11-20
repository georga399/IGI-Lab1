class Car {
  constructor(brand, number) {
      this.brand = brand;
      this.number = number;
  }

  get brand() {
      return this._brand;
  }

  set brand(value) {
      this._brand = value;
  }

  get number() {
      return this._number;
  }

  set number(value) {
      this._number = value;
  }

  displayInfo() {
      return `Марка: ${this.brand}, Номер: ${this.number}`;
  }
}

class OwnerCar extends Car {
  constructor(brand, number, owner) {
      super(brand, number);
      this.owner = owner;
  }

  get owner() {
      return this._owner;
  }

  set owner(value) {
      this._owner = value;
  }

  displayFullInfo() {
      return `${super.displayInfo()}, Владелец: ${this.owner}`;
  }
}

function findOwnersByBrand(carsArray, brand) {
  return carsArray.filter(car => car.brand === brand)
                  .map(car => `${car.owner} - ${car.number}`);
}

const carsArray = [];
const car1 = new OwnerCar('Toyota', 'A123BC', 'Иванов');
const car2 = new OwnerCar('Honda', 'B456CD', 'Петров');
const car3 = new OwnerCar('Toyota', 'C789EF', 'Сидоров');

carsArray.push(car1, car2, car3);

console.log(findOwnersByBrand(carsArray, 'Toyota'));