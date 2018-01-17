func evenOrOdd(_ number:Int) -> String {
  if number%2 == 1 {
    return "Odd"
  } else {
    return "Even"
  }
}
print(evenOrOdd(2))
print(evenOrOdd(0))
print(evenOrOdd(7))
print(evenOrOdd(1))