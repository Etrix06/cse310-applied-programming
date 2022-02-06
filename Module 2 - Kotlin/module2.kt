fun runGame(): Boolean {
  print("Do you want to play? y/n: ")
  var isPlaying = false
  var result = readLine()
  if (result == "y" || result == "Y") {
    isPlaying = true
  }
  else if (result == "n" || result == "N"){
    println("Sorry to hear that, maybe another time.\n\n")
    isPlaying = false
  }
  return isPlaying
}

fun main() {
  println("\n\n\n")
  println("****Welcome to Madlibs****\n")
  var gameOn: Boolean = runGame()
  //println(gameOn)

  // Game loop
  while (gameOn) {
    println("\nPlease enter the following.")
    print("\tPlural noun (hint living thing): ")
    val noun1Input = readLine()

    print("\tPlural noun (hint living thing): ")
    val noun2Input = readLine()

    print("\tType of liquid: ")
    val word1Input = readLine()

    print("\tAdjective (describing a noun): ")
    val adjective1Input = readLine()

    print("\tAnimal sound: ")
    val word2Input = readLine()

    print("\tAnother animal sound: ")
    val word3Input = readLine()

    print("\tAdjective (describing a noun): ")
    val adjective2Input = readLine()

    print("\tAnimal: ")
    val word4Input = readLine()

    print("\tAnother animal: ")
    val word5Input = readLine()

    println("Your story is:\n")
    println("Zoos are places where wild $noun1Input are kept in pens or cages")
    println("so that $noun2Input can come and look at them.  There is a zoo")
    println("in the park beside the $word1Input fountain.  When it is feeding time,")
    println("all the animals make $adjective1Input noises. The elephant goes \"$word2Input\"")
    println("and the turtledoves go \"$word3Input.\"  My favorite animal is the")
    println("$adjective2Input $word4Input, so fast it can outrun a/an $word5Input.")
    println("You never know what you will find at the zoo.\n\n")
    println("Thanks for playing.")
    gameOn = false

  }

}