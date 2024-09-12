type UserType = "user" | "admin";

interface Person {
  name: string;
  age: number;
  type: UserType;
}

function createPerson(name: string, age: number, type: UserType): Person {
  return {
    name,
    age,
    type,
  };
}

const user = createPerson("Alice", 30, "user");
const admin = createPerson("Bob", 40, "admin");
