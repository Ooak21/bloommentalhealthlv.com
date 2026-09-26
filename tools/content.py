"""Bloom Mental Health · every public fact and every line of page copy, in one place.

Sources (never add a fact that is not in one of these):
  - Michelle's referral packet "Provider Referral Guide" (handed to referring offices, sent 9/21 with the ask to put it on the site)
  - Michelle's provider bios email (9/21; "you can tweak whatever you feel is necessary")
  - The previous site copy (about, mission, vision, values, FAQ)
Nothing here is PHI. Hours are not published as clock times; the packet only says "flexible times".
"""

SITE = "https://bloommentalhealthlv.com"
GA4 = "G-FC50JVCNET"

PRACTICE = {
    "name": "Bloom Mental Health",
    "street": "2450 Chandler Ave Ste 1",
    "city": "Las Vegas",
    "region": "NV",
    "zip": "89120",
    "country": "US",
    "phone": "702-350-1419",
    "phone_e164": "+1-702-350-1419",
    "fax": "702-357-5249",
    "fax_e164": "+1-702-357-5249",
    "email": "michelle@bloommentalhealthlv.com",
    "languages": ["English", "Spanish", "Tagalog"],
    "ages": ["Children", "Adolescents", "Adults", "Older Adults"],
    "times": "Flexible times, including early mornings, evenings, Saturdays and Sundays",
    "accepting": True,
    "self_pay": {"initial": 90, "follow_up": 50},
}

MAPS_EMBED = "https://www.google.com/maps?q=2450+Chandler+Ave+Ste+1,+Las+Vegas,+NV+89120&output=embed"
MAPS_DIR = "https://www.google.com/maps/dir/?api=1&destination=2450+Chandler+Ave+Ste+1,+Las+Vegas,+NV+89120"

INSURANCE = ["Aetna", "Carelon (BCBS)", "CareSource", "Evernorth (Cigna)", "Medicare", "UHC / Optum", "UMR", "Alignment", "Medicaid FFS"]
INSURANCE_PENDING = ["Culinary Health Fund", "SilverSummit", "Molina", "Sierra Health and Life HPN", "Medicaid MCOs"]

# ---------------------------------------------------------------- scenes
# The nature films from the Calm and cinematic concept, self-hosted and compressed.
SCENES = {
    "lake-willow": "A desert lake under willow branches",
    "red-rock": "Red Rock Canyon, just outside Las Vegas",
    "pine-forest": "Light through a quiet pine forest",
    "leaves-light": "Morning sun through leaves",
    "cloud-light": "Evening light above the clouds",
}

# ---------------------------------------------------------------- providers
# Order = Michelle's email order. Kanittha Thanangamsuwan, APRN is on the roster but no bio was sent: not listed until one arrives.
PROVIDERS = [
    {
        "slug": "michelle-cuevas-romero", "name": "Michelle Cuevas-Romero", "creds": "MSN, APRN, PMHNP-BC",
        "role": "Owner · Psychiatric Mental Health Nurse Practitioner", "npi": "1568358786", "initials": "MC",
        "languages": ["English", "Spanish"],
        "focus": ["Anxiety", "Depression", "Bipolar disorder", "ADHD", "Autism", "Substance use", "MAT", "Pediatric care"],
        "alumni": "Chamberlain University",
        "short": "Board-certified PMHNP with experience across mental health, substance use treatment, medication-assisted treatment and pediatric care. Fluent in English and Spanish.",
        "quote": "Her approach to care is centered on the whole person, because mental health is only one part of your story.",
        "bio": [
            "Michelle Cuevas-Romero is a board-certified Psychiatric Mental Health Nurse Practitioner who is passionate about helping individuals feel heard, understood, and supported throughout their mental health journey.",
            "A nurse since 2022, Michelle has experience across mental health, substance use treatment and rehabilitation, medication-assisted treatment (MAT), and pediatric care. She works with individuals experiencing a variety of mental and behavioral health concerns, including anxiety, depression, bipolar disorder, ADHD, autism spectrum disorder, substance use disorders, and other psychiatric conditions.",
            "Michelle graduated from Chamberlain University and believes that mental health care should never feel one-size-fits-all. She strives to understand the whole person, not simply a diagnosis, and works collaboratively with each patient to develop an individualized treatment plan that reflects their unique needs, experiences, culture, and goals.",
            "Fluent in both English and Spanish, Michelle is especially passionate about helping bridge gaps in mental healthcare within the Latino community. She understands that language, culture, stigma, and access to resources can sometimes create barriers to seeking mental health services. By providing care in Spanish and creating a culturally respectful and welcoming environment, she strives to make it easier for Spanish-speaking individuals and families to feel understood, comfortable, and empowered when seeking care.",
            "In addition to her clinical practice, Michelle serves as a nursing school instructor, where she educates, mentors, and supports future nurses as they develop their clinical skills, confidence, and compassion.",
            "Her passion for mental health also extends beyond the walls of the clinic. Michelle works alongside nonprofit organizations and participates in community outreach efforts focused on improving access to healthcare and reaching individuals who may otherwise experience barriers to receiving services. She strongly believes in meeting people where they are and bringing compassionate mental healthcare closer to the communities that need it.",
            "At Bloom Mental Health, Michelle's goal is to create a welcoming, inclusive, and judgment-free environment where patients can feel comfortable being themselves. She believes everyone deserves to be treated with dignity, kindness, and respect, and to have a provider who genuinely listens.",
        ],
    },
    {
        "slug": "christopher-hansen", "name": "Christopher Hansen", "creds": "MSN, APRN, PMHNP-BC",
        "role": "Psychiatric Mental Health Nurse Practitioner", "npi": "1386344976", "initials": "CH",
        "languages": ["English"],
        "focus": ["Care across the lifespan", "Serious mental illness", "Schizophrenia", "LGBTQ+ affirming care", "Patient education"],
        "short": "Board-certified PMHNP with a background in long-term care and complex psychiatric conditions, and a particular interest in LGBTQ+ affirming care.",
        "bio": [
            "Christopher Hansen is a board-certified Psychiatric Mental Health Nurse Practitioner with a diverse background in nursing and behavioral healthcare. He began his nursing career in 2021, gaining extensive experience in long-term care and working with individuals living with complex psychiatric conditions, including schizophrenia and other serious mental health disorders.",
            "As a PMHNP-BC, Christopher provides psychiatric care across the lifespan and is passionate about delivering individualized, compassionate, and inclusive mental health services. He has a particular interest in supporting members of the LGBTQ+ community and strives to create a welcoming, affirming, and judgment-free environment where every patient feels respected and comfortable being themselves.",
            "Christopher is also passionate about patient education and believes that understanding one's mental health is an important part of treatment. He takes the time to help patients better understand their diagnoses, medications, treatment options, and overall wellness so they can feel informed and actively involved in decisions about their care.",
            "His commitment to mental health extends beyond the clinical setting through his involvement with nonprofit organizations and community outreach initiatives. Christopher believes in meeting people where they are, helping bridge gaps in mental healthcare, and connecting underserved individuals with the support and resources they need.",
            "Above all, Christopher strives to ensure that each patient is treated as an individual, not simply a diagnosis, and receives care that reflects their unique needs, experiences, identity, and goals.",
        ],
    },
    {
        "slug": "brenda-ortiz", "name": "Brenda Ortiz", "creds": "MSN, APRN, PMHNP-BC",
        "role": "Psychiatric Mental Health Nurse Practitioner", "npi": "1265263370", "initials": "BO",
        "languages": ["English", "Spanish"],
        "focus": ["Care across the lifespan", "Culturally responsive care", "Spanish-language care", "Complex medical and emotional needs"],
        "short": "Board-certified PMHNP with a critical-care background, providing culturally responsive care across the lifespan. Fluent in English and Spanish.",
        "bio": [
            "Brenda Ortiz is a board-certified Psychiatric Mental Health Nurse Practitioner with an extensive nursing background. She began her nursing career in 2018, gaining valuable experience in critical care as an ICU nurse, where she developed a strong foundation in caring for individuals with complex medical and emotional needs.",
            "As a PMHNP-BC, Brenda provides psychiatric care across the lifespan and is passionate about delivering compassionate, individualized, and culturally responsive mental health services. Fluent in both English and Spanish, she has a special interest in helping bridge gaps in mental healthcare within the Latino community by providing patients and families with care in the language in which they feel most comfortable.",
            "Her commitment to healthcare extends beyond the clinical setting. Brenda works with nonprofit organizations and participates in community outreach efforts focused on improving access to mental health services and reaching individuals who may otherwise face barriers to care.",
            "Brenda is also passionate about education and has experience teaching and mentoring nursing students throughout her career. She strives to empower both her patients and future healthcare professionals through education, compassion, and understanding.",
            "Above all, Brenda believes in meeting patients where they are and creating a welcoming, respectful, and judgment-free environment where every individual feels heard, valued, and actively involved in their care.",
        ],
    },
    {
        "slug": "heley-bayot", "name": "Heley Vannessa Erdao Bayot", "creds": "MSN, APRN, PMHNP-BC",
        "role": "Psychiatric Mental Health Nurse Practitioner", "npi": "1437040615", "initials": "HB",
        "languages": ["English"],
        "focus": ["Children and adolescents", "Autism", "ADHD", "Anxiety", "Depression", "Family-centered care"],
        "short": "Board-certified PMHNP with nearly a decade in nursing, focused on children, adolescents, autism and ADHD, with family-centered care.",
        "bio": [
            "Heley Vannessa Erdao Bayot is a board-certified Psychiatric Mental Health Nurse Practitioner with an extensive nursing background spanning nearly a decade. She began her nursing career in 2016 and spent much of her clinical career in critical care as an ICU nurse, developing a strong foundation in caring for patients with complex medical and emotional needs.",
            "As a PMHNP-BC, Heley provides psychiatric care across the lifespan, with a special interest in working with children, adolescents, and individuals with developmental and behavioral health needs. Her areas of focus include autism spectrum disorder, ADHD, anxiety, depression, and other psychiatric conditions affecting children and adults.",
            "In addition to her clinical practice, Heley has dedicated many years to nursing education, teaching and mentoring nursing students as they develop their clinical knowledge, skills, and confidence.",
            "Heley believes in providing compassionate, individualized, and family-centered care. She strives to create a supportive environment where patients and families feel heard, respected, and actively involved in their treatment.",
        ],
    },
    {
        "slug": "daniel-fite", "name": "Daniel Hunter Fite", "creds": "MSN, APRN, PMHNP-BC",
        "role": "Psychiatric Mental Health Nurse Practitioner", "npi": "1164363271", "initials": "DF",
        "languages": ["English"],
        "focus": ["Care across the lifespan", "Pediatric patients", "Substance use", "LGBTQ+ affirming care", "Patient education"],
        "short": "Board-certified PMHNP with experience in pediatrics and substance use, and a special interest in LGBTQ+ affirming care.",
        "bio": [
            "Daniel Hunter Fite is a board-certified Psychiatric Mental Health Nurse Practitioner with a diverse background in nursing and behavioral healthcare. Since beginning his nursing career in 2023, Daniel has gained experience working with pediatric patients and individuals affected by mental health and substance use disorders.",
            "As a PMHNP-BC, Daniel provides psychiatric care across the lifespan and is passionate about delivering compassionate, individualized, and inclusive mental health services. He has a special interest in supporting members of the LGBTQ+ community and strives to create a welcoming, affirming, and judgment-free environment where every patient feels respected, understood, and comfortable being themselves.",
            "Daniel strongly believes that education is an important part of mental healthcare. He takes the time to help patients understand their mental health, diagnoses, medications, and treatment options so they can feel informed and empowered to actively participate in their care.",
            "His passion for education also extends to the next generation of healthcare professionals. As a nursing instructor, Daniel teaches and mentors nursing students, emphasizing clinical knowledge, compassion, and patient-centered care.",
            "Above all, Daniel believes that every patient's journey is unique. He is committed to meeting individuals where they are and providing personalized care that considers the whole person, not simply a diagnosis.",
        ],
    },
]

# ---------------------------------------------------------------- services
# "short" = the packet's own one-line description. The body copy expands it without adding claims about the practice.
ALL = [p["slug"] for p in PROVIDERS]
SERVICES = [
    {
        "slug": "psychiatric-evaluations", "name": "Psychiatric Evaluations", "scene": "pine-forest", "icon": "rings",
        "short": "Comprehensive assessment to clarify symptoms, diagnoses, treatment needs, and next steps.",
        "title": "Psychiatric Evaluations in Las Vegas",
        "body": [
            "Every patient at Bloom Mental Health starts with a comprehensive psychiatric evaluation. It is a conversation, not a checklist: we take time to listen to your concerns, talk through your symptoms, your history and what has or has not helped before, and learn what you want your life to feel like.",
            "From there, your provider shares what they are seeing, answers your questions and builds an individualized care plan with you. That plan may include medication, therapy, further assessment or a referral, and it is always something you help decide.",
            "Evaluations are available in the office on Chandler Avenue and by telehealth, for children, adolescents, adults and older adults.",
        ],
        "helps": ["Symptoms that are complex, persistent, or unclear and would benefit from assessment", "A first step when you are not sure what kind of help you need", "A fresh look when a past diagnosis or treatment no longer fits"],
        "providers": ALL,
    },
    {
        "slug": "medication-management", "name": "Medication Management", "scene": "leaves-light", "icon": "drop",
        "short": "Ongoing evaluation of medication effectiveness, tolerability, adherence, and treatment goals.",
        "title": "Psychiatric Medication Management in Las Vegas",
        "body": [
            "When medication is clinically appropriate, your provider prescribes it and stays with you from there. Follow-up visits look at how well it is working, how you are tolerating it, whether it fits your day-to-day life and whether it still matches your goals.",
            "Medication support should feel collaborative. We explain what a medication is for, what to expect and what to watch for, and we adjust together rather than leave you guessing between visits.",
            "If you already take psychiatric medication and need someone to evaluate, monitor or adjust it, we can take over that care.",
        ],
        "helps": ["A patient on psychiatric medication who needs evaluation, monitoring, or adjustment", "Outpatient psychiatric follow-up after a higher level of care", "Side effects or a medication that no longer seems to help"],
        "providers": ALL,
    },
    {
        "slug": "adhd", "name": "ADHD Evaluation & Treatment", "scene": "leaves-light", "icon": "rings",
        "short": "Assessment and treatment planning for attention, executive-function, and related concerns.",
        "title": "ADHD Evaluation & Treatment in Las Vegas",
        "body": [
            "Trouble focusing, staying organized, finishing tasks or sitting still can affect school, work and relationships at any age. An ADHD evaluation at Bloom looks carefully at attention and executive function, and at the other things that can look similar, such as anxiety, sleep problems or mood.",
            "If ADHD is part of the picture, your provider builds a treatment plan with you. That can include medication when it is appropriate, along with practical strategies and regular follow-up to see what is actually helping.",
            "We see children, adolescents and adults, and we involve parents and families when the patient is young.",
        ],
        "helps": ["Possible ADHD symptoms affecting school, work, relationships, or daily organization", "Adults who have wondered about ADHD for years", "Children and teens whose teachers or parents have raised attention concerns"],
        "providers": ["michelle-cuevas-romero", "heley-bayot"],
    },
    {
        "slug": "anxiety-depression", "name": "Anxiety & Depression Treatment", "scene": "lake-willow", "icon": "waves",
        "short": "Evidence-informed psychiatric care for common mood and anxiety concerns.",
        "title": "Anxiety & Depression Treatment in Las Vegas",
        "body": [
            "Anxiety and depression are among the most common reasons people reach out to us, and among the most treatable. Constant worry, panic, avoidance, persistent sadness, loss of interest, low energy or changes in sleep and appetite are all worth talking about.",
            "Your provider will evaluate what you are experiencing and work with you on an evidence-informed plan. That may include medication, therapy or both, with follow-up visits to make sure you are moving in the right direction.",
            "Care is available in person and by telehealth, and in English or Spanish.",
        ],
        "helps": ["Excessive worry, panic symptoms, avoidance, sleep disruption, or difficulty functioning", "Persistent low mood, loss of interest, fatigue, sleep or appetite changes, or feelings of worthlessness", "Irritability, mood changes, or a decline in how you are functioning"],
        "providers": ["michelle-cuevas-romero", "heley-bayot"],
    },
    {
        "slug": "bipolar-disorder", "name": "Bipolar Disorder Treatment", "scene": "cloud-light", "icon": "waves",
        "short": "Longitudinal medication and symptom management with attention to mood stability.",
        "title": "Bipolar Disorder Treatment in Las Vegas",
        "body": [
            "Bipolar disorder is a long-term condition, and good care is long-term too. We focus on mood stability over time: careful medication management, attention to early warning signs and steady follow-up.",
            "Your provider works with you to understand your patterns of elevated and depressed mood, find a treatment plan you can live with, and adjust it as life changes.",
            "If you have had episodes of elevated or depressed mood, significant cycling, or a past diagnosis you want reviewed, we can help.",
        ],
        "helps": ["Episodes of elevated or depressed mood, significant cycling, or concerns warranting evaluation", "Ongoing medication management for a known bipolar diagnosis", "Continuity of care after a hospital stay or a higher level of care"],
        "providers": ["michelle-cuevas-romero"],
    },
    {
        "slug": "ptsd-trauma", "name": "PTSD & Trauma Treatment", "scene": "pine-forest", "icon": "shield",
        "short": "Psychiatric support for trauma-related symptoms and associated mental health concerns.",
        "title": "PTSD & Trauma Treatment in Las Vegas",
        "body": [
            "Trauma can show up long after the event, as intrusive memories, nightmares, being on edge, avoiding reminders, or feeling disconnected. You do not have to explain everything at once to get help.",
            "At Bloom we provide psychiatric support for trauma-related symptoms and the concerns that often come with them, such as anxiety, depression, sleep problems and substance use. Care moves at your pace, in a safe and judgment-free setting.",
        ],
        "helps": ["Intrusive memories, hyperarousal, avoidance, nightmares, or other trauma-associated symptoms", "Sleep problems, anxiety, or low mood that followed a difficult experience"],
        "providers": [],
    },
    {
        "slug": "child-adolescent", "name": "Child & Adolescent Mental Health", "scene": "lake-willow", "icon": "drop",
        "short": "Developmentally informed psychiatric assessment and treatment for younger patients.",
        "title": "Child & Adolescent Psychiatric Care in Las Vegas",
        "body": [
            "Children and teens are not small adults, and their care should not be either. Our assessments for younger patients are developmentally informed and look at how a child is doing at home, at school and with friends.",
            "Parents and caregivers are part of the process. We explain what we see, talk through options, and build a plan that fits the child and the family, with follow-up that keeps everyone informed.",
            "Common reasons families reach out include attention concerns, anxiety, low mood, behavior changes and autism-related concerns. Please contact our office to confirm current age ranges.",
        ],
        "helps": ["Attention, mood, anxiety, or behavior concerns at home or school", "Autism-related concerns or co-occurring mental health needs", "A second opinion on a child's diagnosis or medication"],
        "providers": ["heley-bayot", "michelle-cuevas-romero", "daniel-fite"],
    },
    {
        "slug": "autism", "name": "Autism", "scene": "leaves-light", "icon": "rings",
        "short": "Psychiatric support for autism-spectrum concerns alongside co-occurring mental health needs.",
        "title": "Autism Psychiatric Support in Las Vegas",
        "body": [
            "Many autistic children, teens and adults also live with anxiety, ADHD, mood changes or sleep problems. We provide psychiatric support for autism-spectrum concerns alongside those co-occurring needs.",
            "Your provider takes time to understand how the person communicates, what is hard for them and what is going well, and works with the patient and family on a plan that respects who they are.",
        ],
        "helps": ["Social communication differences, repetitive behaviors, sensory sensitivities, or concerns warranting evaluation", "Anxiety, attention, mood, or sleep concerns alongside autism"],
        "providers": ["heley-bayot", "michelle-cuevas-romero"],
    },
    {
        "slug": "psychotherapy", "name": "Psychotherapy", "scene": "lake-willow", "icon": "waves",
        "short": "Individual talk therapy offered alongside medication management for comprehensive care.",
        "title": "Psychotherapy (Talk Therapy) in Las Vegas",
        "body": [
            "Medication can help, and so can having space to talk. We offer individual talk therapy alongside medication management, so your care can address both.",
            "Therapy is a place to work through what you are carrying, build skills for hard moments and make changes that last, with someone who is on your side.",
        ],
        "helps": ["Stress, anxiety, low mood, grief, or life changes you want support with", "Patients who want therapy alongside their medication care"],
        "providers": [],
    },
    {
        "slug": "substance-use-mat", "name": "Substance Use & MAT", "scene": "red-rock", "icon": "shield",
        "short": "Medication-assisted treatment and psychiatric support for substance use concerns.",
        "title": "Substance Use Treatment & MAT in Las Vegas",
        "body": [
            "Substance use is a health condition, not a moral failing. We offer medication-assisted treatment (MAT) and psychiatric support for substance use concerns, including the anxiety, depression and trauma that often travel with them.",
            "Care is judgment-free and built around where you are right now, whether you are just starting to think about change or already in recovery and need steady support.",
        ],
        "helps": ["Substance use you want help with, at any stage", "Medication-assisted treatment and ongoing monitoring", "Mental health concerns that occur alongside substance use"],
        "providers": ["michelle-cuevas-romero", "daniel-fite"],
    },
    {
        "slug": "iop", "name": "IOP Services", "scene": "cloud-light", "icon": "rings",
        "short": "Intensive outpatient programming for patients who benefit from a higher level of structured support.",
        "title": "Intensive Outpatient Program (IOP) in Las Vegas",
        "body": [
            "Some seasons call for more than a visit every few weeks. Our intensive outpatient programming (IOP) offers a higher level of structured support while you continue living at home.",
            "IOP can be a step up when outpatient care is not enough, or a step down after a hospital stay or residential program. Please contact our office to confirm current availability.",
        ],
        "helps": ["Patients who benefit from a higher level of structured support", "Outpatient follow-up after a higher level of care"],
        "providers": [],
    },
    {
        "slug": "telehealth", "name": "Telehealth Services", "scene": "cloud-light", "icon": "waves",
        "short": "Secure, confidential video visits from the comfort of home.",
        "title": "Telehealth Psychiatry in Nevada",
        "body": [
            "Telehealth makes it easier to keep your care going when getting to the office is hard. Video visits are secure and confidential, and they offer the same thoughtful care and professional guidance as an office visit.",
            "Many evaluations and follow-up visits can be done by telehealth. When you request an appointment, tell us whether you prefer video, the office on Chandler Avenue, or either one.",
        ],
        "helps": ["Busy schedules, transportation or mobility challenges", "Follow-up visits that do not need to be in person", "Anyone who is more comfortable talking from home"],
        "providers": ALL,
    },
]

# ---------------------------------------------------------------- referral guide (packet page 2 + 4)
REFER_REASONS = [
    ("Mood Concerns", "Persistent sadness, loss of interest, mood changes, irritability, or functional decline."),
    ("Anxiety Concerns", "Excessive worry, panic symptoms, avoidance, sleep disruption, or difficulty functioning."),
    ("Attention Concerns", "Possible ADHD symptoms affecting school, work, relationships, or daily organization."),
    ("Mood Instability", "Episodes of elevated or depressed mood, significant cycling, or concerns warranting evaluation."),
    ("Trauma-Related Symptoms", "Intrusive memories, hyperarousal, avoidance, nightmares, or other trauma-associated symptoms."),
    ("Medication Needs", "A patient on psychiatric medication who needs evaluation, monitoring, or adjustment."),
    ("Diagnostic Clarification", "Symptoms that are complex, persistent, or unclear and would benefit from assessment."),
    ("Post-Discharge Continuity", "A patient who needs outpatient psychiatric follow-up after a higher level of care."),
    ("Depression Symptoms", "Persistent low mood, anhedonia, fatigue, sleep or appetite changes, or feelings of worthlessness."),
    ("Autism-Related Concerns", "Social communication differences, repetitive behaviors, sensory sensitivities, or concerns warranting evaluation."),
]
BEFORE_REFERRAL = ["Confirm the patient's insurance plan", "Confirm the service being requested", "Provide accurate patient contact information", "Send relevant clinical information"]
EXPECT = ["A respectful, nonjudgmental environment", "Collaborative discussion of treatment options", "Medication management when clinically appropriate", "Coordination with the patient's care team, when authorized"]

# ---------------------------------------------------------------- FAQ (previous site copy, updated with the packet facts)
FAQ = [
    ("What services does Bloom Mental Health provide?", "We provide outpatient psychiatric care, including psychiatric evaluations, medication management, ADHD evaluation and treatment, anxiety and depression treatment, bipolar disorder treatment, PTSD and trauma treatment, child and adolescent mental health, autism support, psychotherapy, substance use treatment and MAT, IOP services and telehealth."),
    ("Are you accepting new patients?", "Yes. We are currently accepting new patients. You can request an appointment online or call 702-350-1419."),
    ("Who do you see?", "We see children, adolescents, adults and older adults. Please contact our office to confirm current age ranges."),
    ("Do you offer care in Spanish or Tagalog?", "Yes. We have bilingual providers who speak Spanish and Tagalog. Let us know your preferred language when you request an appointment."),
    ("Do you offer virtual or telehealth appointments?", "Yes, we offer secure and confidential telehealth appointments for individuals seeking convenient access to mental health care from the comfort of home."),
    ("What insurance do you accept?", "We are credentialed with Aetna, Carelon (BCBS), CareSource, Evernorth (Cigna), Medicare, UHC / Optum, UMR, Alignment and Medicaid FFS. Credentialing is pending with Culinary Health Fund, SilverSummit, Molina, Sierra Health and Life HPN and Medicaid MCOs. Because participation and plan benefits can change, please contact our office to confirm your coverage."),
    ("What does it cost without insurance?", "Self-pay visits are $90 for an initial visit and $50 for a follow-up visit."),
    ("When can I be seen?", "We offer flexible times, including early mornings, evenings, Saturdays and Sundays. Call 702-350-1419 or request an appointment and our team will find a time with you."),
    ("What can I expect during my first appointment?", "Your first appointment includes a comprehensive evaluation where we discuss your concerns, symptoms, medical history, and wellness goals to create a personalized care plan."),
    ("Do you prescribe medication if needed?", "Yes, medication management is available when appropriate as part of a personalized treatment plan focused on your mental and emotional well-being."),
    ("Is my information kept confidential?", "Absolutely. Your privacy and confidentiality are extremely important to us, and all services are provided in a safe and secure environment."),
    ("How do I know if mental health support is right for me?", "If you are experiencing stress, anxiety, depression, emotional overwhelm, trauma, or changes in mood or behavior, mental health support may help provide guidance and healing."),
    ("How often will I need follow-up appointments?", "Follow-up care is personalized based on your treatment plan, goals, and progress to ensure ongoing support and continuity of care."),
    ("What if I am in crisis?", "Bloom Mental Health is an outpatient practice and this website is not an emergency service. If you are in immediate danger or thinking about harming yourself, call or text 988 (Suicide and Crisis Lifeline) or call 911."),
]
