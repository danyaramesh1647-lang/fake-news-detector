"""
generate_dataset.py
Creates a varied synthetic dataset of REAL and FAKE news snippets.
"""

import csv
import random

random.seed(42)

organizations = [
    "the Ministry of Education",
    "the Health Department",
    "the Reserve Bank",
    "the United Nations",
    "NASA",
    "the World Bank",
    "the Election Commission",
    "the Transport Department",
    "the Energy Ministry",
    "the National Statistics Office"
]

places = [
    "India",
    "the United States",
    "Japan",
    "Germany",
    "Canada",
    "Australia",
    "the United Kingdom",
    "Singapore"
]

topics = [
    "public health",
    "education",
    "climate change",
    "renewable energy",
    "transportation",
    "cybersecurity",
    "agriculture",
    "economic growth",
    "digital technology",
    "water management"
]

research_topics = [
    "crop resilience during drought",
    "battery storage efficiency",
    "air quality in urban areas",
    "early disease detection",
    "solar panel efficiency",
    "water conservation methods",
    "traffic management systems",
    "online learning outcomes",
    "cybersecurity risks",
    "renewable energy adoption"
]

sources = [
    "official data",
    "a government report",
    "a university study",
    "an independent analysis",
    "a quarterly report",
    "published research"
]

real_actions = [
    "announced",
    "reported",
    "published",
    "released",
    "reviewed",
    "evaluated",
    "examined",
    "introduced"
]

real_phrases = [
    "after reviewing recent data",
    "following a detailed assessment",
    "after consultations with researchers",
    "according to recently published information",
    "as part of a broader review",
    "following an analysis of available evidence",
    "after collecting data from several regions",
    "based on findings from the study"
]

fake_claims = [
    "a secret method",
    "a miracle technique",
    "a hidden technology",
    "an instant solution",
    "a revolutionary discovery",
    "a previously unknown treatment",
    "a mysterious invention",
    "a breakthrough supposedly kept from the public"
]

fake_sources = [
    "an anonymous source",
    "a viral social media post",
    "an unverified website",
    "a message circulating online",
    "an unnamed researcher",
    "an internet user",
    "an unknown organization",
    "a widely shared online claim"
]

fake_endings = [
    "with no further testing required",
    "within just a few days",
    "without any known side effects",
    "with guaranteed results for everyone",
    "without the need for expert approval",
    "almost immediately",
    "without any supporting evidence being published",
    "despite no independent confirmation"
]

real_templates = [
    "{org} {action} a new initiative related to {topic} {phrase}.",
    "Researchers published findings about {research} in a peer-reviewed journal {phrase}.",
    "Officials in {place} {action} new measures to improve {topic} {phrase}.",
    "A new report examined changes in {topic} and compared results from the previous year {phrase}.",
    "Researchers reported that a new approach may improve {research}, although further testing is required.",
    "The {org} released updated information about {topic} based on {source}.",
    "A study involving several research institutions examined {research} and identified areas for further research.",
    "Authorities announced plans to evaluate {topic} before introducing the proposed changes nationwide.",
    "Researchers found a possible connection between {topic} and changes observed during the study period.",
    "A public report described recent developments in {topic} and included data from multiple sources."
]

fake_templates = [
    "A viral report claims that {place} has discovered {claim} that will completely solve {topic} overnight.",
    "Social media users are sharing a claim that {claim} can instantly eliminate every problem related to {topic}.",
    "An unverified report from {source} claims that researchers have discovered {claim} for {research}.",
    "BREAKING: {source} claims that officials secretly tested {claim} that can permanently eliminate {topic}.",
    "A widely shared post claims that {claim} can make {research} completely unnecessary within a few days.",
    "Online posts claim that scientists have hidden evidence showing that {topic} can be solved immediately using {claim}.",
    "A sensational article claims that a secret experiment has already solved {research} {ending}.",
    "An unverified claim circulating online says that authorities have confirmed {claim} for {topic}.",
    "Viral messages claim that {claim} can guarantee success in {research} {ending}.",
    "A post making the rounds online claims that scientists are hiding a breakthrough involving {topic}."
]

rows = []

# Generate 600 REAL examples
for i in range(600):
    template = random.choice(real_templates)

    text = template.format(
        org=random.choice(organizations),
        place=random.choice(places),
        topic=random.choice(topics),
        research=random.choice(research_topics),
        source=random.choice(sources),
        action=random.choice(real_actions),
        phrase=random.choice(real_phrases)
    )

    # Add a small unique detail to prevent duplicates
    text += f" Reference number {i + 1} was included in the dataset."

    rows.append((text, "REAL"))


# Generate 600 FAKE examples
for i in range(600):
    template = random.choice(fake_templates)

    text = template.format(
        place=random.choice(places),
        topic=random.choice(topics),
        research=random.choice(research_topics),
        claim=random.choice(fake_claims),
        source=random.choice(fake_sources),
        ending=random.choice(fake_endings)
    )

    # Add a small unique detail to prevent duplicates
    text += f" Online claim reference {i + 1} was included in the dataset."

    rows.append((text, "FAKE"))


# Shuffle the complete dataset
random.shuffle(rows)


# Save dataset
with open("dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(rows)


print(f"Wrote {len(rows)} rows to dataset.csv")
print("REAL examples:", sum(1 for r in rows if r[1] == "REAL"))
print("FAKE examples:", sum(1 for r in rows if r[1] == "FAKE"))