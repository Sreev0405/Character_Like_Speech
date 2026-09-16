from llama_cpp import Llama

MODEL_PATH = "./models/qwen2.5-1.5b-instruct-q4_k_m.gguf"

SYSTEM_PROMPT = ("Pinkie Pie My Little Pony Friendship Is Magic. Respond to everything as Pinkie Pie would.")
print("Loading Pinkie Pie's brain... this can take a little while the first time.")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

print("Pinkie Pie: I'm ready!\n")

userInput = input("What would you like to say to SpongeBob?\n Type exit to leave \n\n")

while userInput != "exit":
    prompt = [{"role": "system", "content":SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
    result = model.create_chat_completion(prompt, max_tokens=256, temperature = 2)

   # print(result)
    response = result["choices"][0]["message"]["content"]
    print(response)
    userInput = input("You can type exit to leave\n\n")
    print()
print("Good-bye! Thanks for chatting with me!")