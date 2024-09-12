interface User {
  name: string;
  age: number;
  type: "user" | "admin";
}

function createUser(name: string, age: number): User {
  return {
    name: name,
    age: age,
    type: "user",
  };
}

function createAdmin(name: string, age: number): User {
  return {
    name: name,
    age: age,
    type: "admin",
  };
}

const user = createUser("Alice", 30);
const admin = createAdmin("Bob", 40);
