# bank_chat spec
 
## Purpose
A chat program where a customer asks a bank assistant questions
and sees what each answer cost us.
 
## User
A bank customer typing in a terminal window.
 
## It must
- Show the assistant's answer to each question.
- Keep chatting until the user types "quit".
- Remember what the user said earlier in the same chat.
- Show each answer's cost in ₹ and the total so far.
 
## It must not
- Keep the secret key inside the code.
- Answer questions unrelated to banking.
 
## Done when
1. I ask "What is a fixed deposit?" → a short, sensible answer.
2. I type "My name is Ravi", then "What's my name?" → it answers "Ravi".
3. I ask three questions → the ₹ total goes up after every answer.
4. I type "quit" → the program ends.