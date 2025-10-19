from src.llms.groq_llm import GroqLlm

llm = GroqLlm().get_llm()

print(llm.invoke("Hi"))