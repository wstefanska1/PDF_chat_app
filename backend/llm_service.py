from backend.prompt import chain
from backend.vector import retriever


def generate_summary(topic: str, file: str = "all") -> str:
    docs = retriever.invoke(topic)

    # filtr dokumentów
    if file != "all":
        docs = [
            d for d in docs
            if file in d.metadata.get("source", "")
        ]

    text = "\n\n".join(d.page_content for d in docs)

    response = chain.invoke({
        "text": text,
        "topic": topic
    })

    return response