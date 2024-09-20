print(r'''
                                __           
 _____   __  __     __   __  __/\_\  ____    
/\ '__`\/\ \/\ \  /'__`\/\ \/\ \/\ \/\_ ,`\  
\ \ \L\ \ \ \_\ \/\ \L\ \ \ \_\ \ \ \/_/  /_ 
 \ \ ,__/\/`____ \ \___, \ \____/\ \_\/\____\
  \ \ \/  `/___/> \/___/\ \/___/  \/_/\/____/
   \ \_\     /\___/    \ \_\                 
    \/_/     \/__/      \/_/                 

      ''')

print("🎉 Do you want to play? 🎉")
choice = input("Default is yes, type no to exit 🛑\nElse press enter to start playing: ")
if choice.lower() in ['no', 'n']:
    print("👋 Goodbye!")
    quit()
else:
    print("🎊 Great! Let's get started with the quiz. Good luck! 🍀")

score = 0

# Question 1
print("Q1. What does CPU stand for?")
ans1 = input().strip().lower()
if ans1 in ["central processing unit", "central processor unit"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is 'Central Processing Unit'.")

# Question 2
print("Q2. What does RAM stand for?")
ans2 = input().strip().lower()
if ans2 in ["random access memory", "random-access memory"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is 'Random Access Memory'.")

# Question 3
print("Q3. What does GPU stand for?")
ans3 = input().strip().lower()
if ans3 in ["graphics processing unit", "graphics processor unit"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is 'Graphics Processing Unit'.")

# Question 4
print("Q4. What does HTTP stand for?")
ans4 = input().strip().lower()
if ans4 in ["hypertext transfer protocol", "hyper text transfer protocol"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is 'Hypertext Transfer Protocol'.")

# Question 5
print("Q5. What does HTML stand for?")
ans5 = input().strip().lower()
if ans5 in ["hypertext markup language", "hyper text markup language", "hypertext mark-up language", "hyper text mark-up language"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is 'Hypertext Markup Language'.")

print(f"🎉 You completed the quiz! Your score is {score}/5.")
if score == 5:
    print("🏆 Excellent! You got all the answers correct!")
elif score >= 3:
    print("👍 Good job! You got most of the answers correct!")
else:
    print("👋 Better luck next time!")