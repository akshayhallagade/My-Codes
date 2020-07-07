# for first append
question = "Question: What is the difference between a pizza and pizza jock."
# for 2nd append
answer = "\nAnswer: My jock is can'nt be topped."

# Opening and adding question to the file.
appendFile = open("4.Puns.txt", "w")
appendFile.write(question)
appendFile.close()

# again opening and appending to the file.
appendFile = open("4.Puns.txt", "a")
appendFile.write(answer)
appendFile.close()
