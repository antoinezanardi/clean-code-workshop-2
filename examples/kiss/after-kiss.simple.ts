type Status = "child" | "teenager" | "adult" | "senior" | "invalid age";

function getStatus(age: number): Status {
    if (age < 0) {
      return "invalid age";
    }
    if (age <= 12) {
      return "child";
    }
    if (age <= 19) {
      return "teenager";
    }
    if (age <= 64) {
      return "adult";
    }
    return 'senior';
}

const ageStatus = getStatus(25);
// => 'adult'
