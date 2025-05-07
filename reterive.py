from qdrant_client import QdrantClient
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter
from response import token


Recipe_qdrant = QdrantClient(
    url="<your_url>", 
    api_key="<your_api_key>",
)

Recipe_qdrant.set_model("sentence-transformers/all-MiniLM-L6-v2")
Recipe_qdrant.set_sparse_model("Qdrant/bm25")

User_input = input("Hello i am Your Recipe Suggesting Assistant.What do want to have, Enter Your Delightful Cravings:")

question  = User_input

points = Recipe_qdrant.query(
    collection_name = "recip",
    query_text = question,
    limit = 5,
    )

# for i, point in enumerate(points):
#     print(f"=== {i} ===")
#     print(point.document)
#     print(point.score)

final_points = ""

for point in points:
    final_points += point.document


prompt = f"""
 context: {final_points}
 Question: {question}
Based on the context provided, answer the question.
"""

# print(token(prompt, "openai/gpt-4.1"))
for tok in token(prompt, "openai/gpt-4.1"):
    print(tok, end="", flush=True)

