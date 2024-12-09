import chromadb

client = chromadb.Client()
collection = client.create_collection("my_collection")

collection.add(
    documents=["This document about New York City",
                "This document about Delhi",
               ],
    ids=["id1", "id2"],
)


all_docs = collection.get()

# print(all_docs)

result = collection.query(
    query_texts=["jantar mantar"],
    n_results=2
)

print(result)

