type Status = "child" | "teenager" | "adult" | "senior" | "invalid age";

function getStatus(age: number): Status {
  let status: Status;
  if (age >= 0 && age <= 12) {
    status = "child";
  } else if (age >= 13 && age <= 19) {
    status = "teenager";
  } else if (age >= 20 && age <= 64) {
    status = "adult";
  } else if (age >= 65) {
    status = "senior";
  } else {
    status = "invalid age";
  }
  return status;
}

const ageStatus = getStatus(25);
// => 'adult'
