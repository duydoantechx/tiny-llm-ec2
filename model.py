import torch
from transformers import pipeline

def model_query(query:str):
    pipe = pipeline(
        "text-generation",
        model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype= torch.bfloat16,
        device_map = "auto"
    )
    
    messages = [
        {
            "role": "system",
            "content": "You are a serious chatbot who always answers questions with highest precision and correctness. You only reply with the actual answer without repeating my question."
        },
        {
            "role": "user",
            "content": f"{query}"
        }
    ]
    
    prompt = pipe.tokenizer.apply_chat_template(
        messages, tokenize = False, add_generation_prompt= True
    )
    
    outputs = pipe(
        prompt,
        max_new_tokens = 256,
        do_sample = True,
        temperature = 0.7,
        top_k = 50,
        top_p = 0.95
    )
    
    output = outputs[0]["generated_text"]
    return output

if __name__ == "__main__":
    print(model_query("What is the meaning of life?"))