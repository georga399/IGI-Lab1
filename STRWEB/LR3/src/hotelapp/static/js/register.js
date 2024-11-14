document.getElementById('id_date_of_birth').addEventListener('change', function() {
  const dob = new Date(this.value);
  const today = new Date();
  
  let age = today.getFullYear() - dob.getFullYear();
  const monthDiff = today.getMonth() - dob.getMonth();
  if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dob.getDate())) {
      age--;
  }

  const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  const dayOfWeek = daysOfWeek[dob.getDay()];

  const ageInfoDiv = document.getElementById('age-info');
  if (age < 18) {
      alert("You need parental consent to use this site.");
      ageInfoDiv.innerHTML = `You are ${age} years old. Day of Birth: ${dayOfWeek}.`;
  } else {
      ageInfoDiv.innerHTML = `You are ${age} years old. Day of Birth: ${dayOfWeek}.`;
  }
});