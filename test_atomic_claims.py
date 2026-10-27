
from src.atomic_claims import extract_atomic_claims


def test_empty_text():
    assert extract_atomic_claims("") == []


def test_single_sentence():
    text = "The Earth revolves around the Sun."

    claims = extract_atomic_claims(text)

    assert len(claims) == 1


def test_multiple_sentences():
    text = (
        "The Earth revolves around the Sun. "
        "The Moon revolves around the Earth."
    )

    claims = extract_atomic_claims(text)

    assert len(claims) == 2


def test_claims_are_not_empty():
    text = (
        "Python is widely used in data science. "
        "SQL is used for querying databases."
    )

    claims = extract_atomic_claims(text)

    assert all(
        claim.strip()
        for claim in claims
    )


print("All basic atomic claim tests passed.")
