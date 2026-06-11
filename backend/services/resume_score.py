from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)

def calculate_matching_score(
    resume_text,
    jd_text
):

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    jd_embedding = model.encode(
        jd_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        resume_embedding,
        jd_embedding
    )[0][0].item()

    return round(similarity * 100, 2)