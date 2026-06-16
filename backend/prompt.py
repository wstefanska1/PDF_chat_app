from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
You are an academic assistant helping to prepare content for a diploma thesis.

You will be given a document and a topic.

TASK:
Create an academic-style overview of the topic: {topic} based ONLY on the provided document.

TEXT SOURCE:
{text}

REQUIREMENTS:
- Use formal, academic language suitable for a diploma thesis.
- Do NOT use conversational tone.
- Focus on synthesis, not explanation of the task.
- Base the answer strictly on the provided text (do not add external knowledge).
- The output should be usable as a foundation for a thesis paragraph.
- Present information in a structured way (logical flow of ideas).
- Avoid repetition and unnecessary filler words.
- Do not include phrases like "here is a summary" or "based on the text".

"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model