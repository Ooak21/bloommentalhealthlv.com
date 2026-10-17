"""Bloom Mental Health · the Spanish side of the site (Michelle 2026-10-16: "Is there a button to translate the words in Spanish?").

Same approach as Vitality: the header button flips every page, its forms and the chat between English and Spanish in place
(assets/i18n.js) and remembers the choice. build.py turns this file into assets/es.js.

Keys are the EXACT English text a visitor sees (one text node at a time: a sentence split by a link or <em> is several keys).
Change an English line in content.py and its Spanish line here has to change with it, or Spanish visitors silently get English.
build.py prints every page string that has no Spanish ("ES missing"), so run it and read the last lines.
Formal "usted" throughout. Proofread by: (pending, Michelle).
"""
from content import PRACTICE

_SP = PRACTICE["self_pay"]

ES = {
    # ---- /
    "Skip to content": "Saltar al contenido",
    "Home": "Inicio",
    "About": "Nosotros",
    "Providers": "Profesionales",
    "Services": "Servicios",
    "Insurance": "Seguros",
    "Contact": "Contacto",
    "Psychiatric Care in Las Vegas": "Atención psiquiátrica en Las Vegas",
    "Healing begins with": "La sanación comienza con",
    "support": "apoyo",
    "& understanding": "y comprensión",
    "Whole-person outpatient psychiatric care for children, teens, adults and older adults: evaluations, medication management, therapy and telehealth, in English, Spanish and Tagalog.": "Atención psiquiátrica ambulatoria integral para niños, adolescentes, adultos y adultos mayores: evaluaciones, manejo de medicamentos, terapia y telesalud, en inglés, español y tagalo.",
    "Request Appointment": "Solicitar una cita",
    "Our Services": "Nuestros servicios",
    "Accepting New Patients": "Aceptamos pacientes nuevos",
    "Telehealth Available": "Telesalud disponible",
    "Evenings & Weekends": "Tardes y fines de semana",
    "Our Care": "Nuestra atención",
    "Your path to better": "Su camino hacia un mayor",
    "mental wellness": "bienestar mental",
    "At Bloom Mental Health, we are committed to providing personalized psychiatric care in a safe, supportive, and compassionate environment.": "En Bloom Mental Health, nos comprometemos a brindar atención psiquiátrica personalizada en un ambiente seguro, de apoyo y compasivo.",
    "What guides our compassionate care": "Lo que guía nuestra atención compasiva",
    "Providing thoughtful and supportive mental health care in a safe, judgment-free environment.": "Brindamos atención de salud mental considerada y de apoyo en un ambiente seguro y libre de juicios.",
    "Our approach to mental wellness": "Nuestro enfoque del bienestar mental",
    "Every treatment plan is tailored to your unique emotional, mental, and wellness needs.": "Cada plan de tratamiento se adapta a sus necesidades emocionales, mentales y de bienestar.",
    "Personal care ethics & principles": "Ética y principios de atención personal",
    "Helping individuals achieve balance, clarity, healing, and long-term emotional well-being.": "Ayudamos a las personas a lograr equilibrio, claridad, sanación y bienestar emocional a largo plazo.",
    "Care rooted in understanding": "Atención basada en la comprensión",
    "Your privacy, comfort, and trust are always respected throughout your care journey.": "Su privacidad, comodidad y confianza siempre se respetan durante toda su atención.",
    "Meeting You Where You Are": "Lo acompañamos donde usted esté",
    "Mental health is only one part of": "La salud mental es solo una parte de",
    "your story": "su historia",
    "Our providers treat the whole person, not simply a diagnosis. Beyond the clinic, they work with nonprofit organizations and community outreach to bring care closer to the people who need it.": "Nuestros profesionales atienden a la persona en su totalidad, no solo un diagnóstico. Fuera de la clínica, colaboran con organizaciones sin fines de lucro y programas de alcance comunitario para acercar la atención a quienes la necesitan.",
    "Meet Our Providers": "Conozca a nuestros profesionales",
    "A desert lake under willow branches": "Un lago del desierto bajo ramas de sauce",
    "Compassionate": "Compasiva",
    "Personalized": "Personalizada",
    "Confidential": "Confidencial",
    "Why choose": "Por qué elegir",
    "We provide compassionate and personalized mental health care focused on emotional wellness, healing, and long-term support. Our goal is to create a safe and welcoming space where individuals feel heard, understood, and empowered throughout their journey to better mental health.": "Brindamos atención de salud mental compasiva y personalizada, enfocada en el bienestar emocional, la sanación y el apoyo a largo plazo. Nuestra meta es crear un espacio seguro y acogedor donde las personas se sientan escuchadas, comprendidas y empoderadas en su camino hacia una mejor salud mental.",
    "About Us": "Sobre nosotros",
    "A safe and welcoming space": "Un espacio seguro y acogedor",
    "Services & Clinical Support": "Servicios y apoyo clínico",
    "A full continuum of outpatient psychiatric care,": "Atención psiquiátrica ambulatoria completa,",
    "tailored to you": "adaptada a usted",
    "View All Services": "Ver todos los servicios",
    "Psychiatric Evaluations": "Evaluaciones psiquiátricas",
    "Comprehensive assessment to clarify symptoms, diagnoses, treatment needs, and next steps.": "Evaluación completa para aclarar síntomas, diagnósticos, necesidades de tratamiento y próximos pasos.",
    "Medication Management": "Manejo de medicamentos",
    "Ongoing evaluation of medication effectiveness, tolerability, adherence, and treatment goals.": "Evaluación continua de la eficacia, la tolerancia y el cumplimiento de los medicamentos, y de las metas del tratamiento.",
    "ADHD Evaluation & Treatment": "Evaluación y tratamiento del TDAH",
    "Assessment and treatment planning for attention, executive-function, and related concerns.": "Evaluación y plan de tratamiento para problemas de atención, de función ejecutiva y relacionados.",
    "Anxiety & Depression Treatment": "Tratamiento de la ansiedad y la depresión",
    "Evidence-informed psychiatric care for common mood and anxiety concerns.": "Atención psiquiátrica basada en evidencia para problemas comunes del estado de ánimo y de ansiedad.",
    "Bipolar Disorder Treatment": "Tratamiento del trastorno bipolar",
    "Longitudinal medication and symptom management with attention to mood stability.": "Manejo continuo de medicamentos y síntomas, con atención a la estabilidad del estado de ánimo.",
    "PTSD & Trauma Treatment": "Tratamiento del TEPT y el trauma",
    "Psychiatric support for trauma-related symptoms and associated mental health concerns.": "Apoyo psiquiátrico para síntomas relacionados con el trauma y problemas de salud mental asociados.",
    "Rooted in Las Vegas": "Con raíces en Las Vegas",
    "Care close to home,": "Atención cerca de casa,",
    "in your language": "en su idioma",
    "Our office is at 2450 Chandler Ave Ste 1, Las Vegas, NV 89120, with telehealth for visits from home. We see children, adolescents, adults and older adults, with bilingual providers who speak Spanish and Tagalog.": "Nuestra oficina está en 2450 Chandler Ave Ste 1, Las Vegas, NV 89120, y ofrecemos telesalud para consultas desde casa. Atendemos a niños, adolescentes, adultos y adultos mayores, con profesionales bilingües que hablan español y tagalo.",
    "Directions & Contact": "Cómo llegar y contacto",
    "Red Rock Canyon, just outside Las Vegas": "Red Rock Canyon, a las afueras de Las Vegas",
    "Our Providers": "Nuestros profesionales",
    "Board-certified psychiatric": "Enfermeros practicantes psiquiátricos",
    "nurse practitioners": "certificados",
    "All Providers": "Todos los profesionales",
    "Board-certified PMHNP with experience across mental health, substance use treatment, medication-assisted treatment and pediatric care. Fluent in English and Spanish.": "PMHNP certificada con experiencia en salud mental, tratamiento del consumo de sustancias, tratamiento asistido con medicamentos y atención pediátrica. Habla inglés y español con fluidez.",
    "Anxiety": "Ansiedad",
    "Depression": "Depresión",
    "Bipolar disorder": "Trastorno bipolar",
    "ADHD": "TDAH",
    "Languages: English · Spanish · Read bio →": "Idiomas: inglés · español · Leer biografía →",
    "Board-certified PMHNP with a background in long-term care and complex psychiatric conditions, and a particular interest in LGBTQ+ affirming care.": "PMHNP certificado con experiencia en cuidados a largo plazo y condiciones psiquiátricas complejas, y un interés particular en la atención afirmativa para personas LGBTQ+.",
    "Care across the lifespan": "Atención en todas las etapas de la vida",
    "Serious mental illness": "Enfermedad mental grave",
    "Schizophrenia": "Esquizofrenia",
    "LGBTQ+ affirming care": "Atención afirmativa LGBTQ+",
    "Languages: English · Read bio →": "Idiomas: inglés · Leer biografía →",
    "Board-certified PMHNP with a critical-care background, providing culturally responsive care across the lifespan. Fluent in English and Spanish.": "PMHNP certificada con experiencia en cuidados intensivos, que brinda atención culturalmente sensible en todas las etapas de la vida. Habla inglés y español con fluidez.",
    "Culturally responsive care": "Atención culturalmente sensible",
    "Spanish-language care": "Atención en español",
    "Complex medical and emotional needs": "Necesidades médicas y emocionales complejas",
    "Board-certified PMHNP with nearly a decade in nursing, focused on children, adolescents, autism and ADHD, with family-centered care.": "PMHNP certificada con casi una década en enfermería, enfocada en niños, adolescentes, autismo y TDAH, con atención centrada en la familia.",
    "Children and adolescents": "Niños y adolescentes",
    "Autism": "Autismo",
    "Board-certified PMHNP with experience in pediatrics and substance use, and a special interest in LGBTQ+ affirming care.": "PMHNP certificado con experiencia en pediatría y consumo de sustancias, y un interés especial en la atención afirmativa LGBTQ+.",
    "Pediatric patients": "Pacientes pediátricos",
    "Substance use": "Consumo de sustancias",
    "Board-certified Psychiatric Mental Health Nurse Practitioner at Bloom Mental Health. Full bio coming soon.": "Enfermera practicante de salud mental psiquiátrica certificada en Bloom Mental Health. Biografía completa próximamente.",
    "View profile →": "Ver perfil →",
    "Insurance & Pricing": "Seguros y precios",
    "Most major plans, and": "La mayoría de los planes principales, y",
    "simple self-pay": "pago sencillo sin seguro",
    "Insurance Details": "Detalles de seguros",
    f"Self-pay: ${_SP['initial']} initial visit, ${_SP['follow_up']} follow-up. Plan participation and benefits can change, so please call to confirm your coverage.":
        f"Sin seguro: ${_SP['initial']} la consulta inicial, ${_SP['follow_up']} la consulta de seguimiento. La participación en los planes y los beneficios pueden cambiar, así que llámenos para confirmar su cobertura.",
    "Your First Step": "Su primer paso",
    "Begin your journey toward": "Comience su camino hacia el",
    "emotional wellness": "bienestar emocional",
    "today": "hoy mismo",
    "We are accepting new patients, in person in Las Vegas and by telehealth. Flexible times, including early mornings, evenings, Saturdays and Sundays.": "Aceptamos pacientes nuevos, en persona en Las Vegas y por telesalud. Horarios flexibles, incluidos temprano por la mañana, por la tarde, sábados y domingos.",
    "Our goal is to create a safe and welcoming space where individuals feel heard, understood, and empowered throughout their journey to better mental health.": "Nuestra meta es crear un espacio seguro y acogedor donde las personas se sientan escuchadas, comprendidas y empoderadas en su camino hacia una mejor salud mental.",
    "In crisis? Call or text": "¿Está en crisis? Llame o envíe un mensaje de texto al",
    "(Suicide and Crisis Lifeline) or call": "(Línea de Prevención del Suicidio y Crisis) o llame al",
    ". Bloom is an outpatient practice, not an emergency service.": ". Bloom es una clínica ambulatoria, no un servicio de emergencias.",
    "Visit & Contact": "Visítenos y contacto",
    "Phone:": "Teléfono:",
    "Flexible times, including early mornings, evenings, Saturdays and Sundays.": "Horarios flexibles, incluidos temprano por la mañana, por la tarde, sábados y domingos.",
    "Explore": "Explorar",
    "FAQ": "Preguntas frecuentes",
    "For Referring Providers": "Para profesionales que refieren pacientes",
    "Request an Appointment": "Solicitar una cita",
    "Privacy": "Privacidad",
    "Terms": "Términos",
    "Text Messages": "Mensajes de texto",
    "Copyright © 2026 Bloom Mental Health. All Rights Reserved.": "Copyright © 2026 Bloom Mental Health. Todos los derechos reservados.",
    "Back to top ↑": "Volver arriba ↑",
    "Sound on": "Sonido activado",
    "Questions? Chat with us": "¿Preguntas? Escríbanos",
    "Questions & appointment requests": "Preguntas y solicitudes de cita",
    "or call": "o llame al",
    ". This chat is not monitored around the clock.": ". Este chat no se supervisa las 24 horas.",
    "Hi, I'm Bloom's virtual assistant. I can answer questions about our services, providers, insurance and pricing, or send your appointment request to our front desk. Please don't share medical details here.": "Hola, soy la asistente virtual de Bloom. Puedo responder preguntas sobre nuestros servicios, profesionales, seguros y precios, o enviar su solicitud de cita a nuestra recepción. Por favor, no comparta detalles médicos aquí.",
    "Do you take my insurance?": "¿Aceptan mi seguro?",
    "I would like an appointment": "Quisiera hacer una cita",
    "Do you see children?": "¿Atienden a niños?",
    "Your message": "Su mensaje",
    "An automated assistant. Answers come only from our published information. By chatting you agree to our": "Asistente automatizado. Las respuestas provienen solo de nuestra información publicada. Al usar el chat, usted acepta nuestra",
    "Privacy Policy": "Política de Privacidad",
    "Open menu": "Abrir menú",  # aria-label
    "Meeting you where you are": "Lo acompañamos donde usted esté",  # aria-label
    "The water fountain in the Bloom Mental Health office": "La fuente de agua en la oficina de Bloom Mental Health",  # aria-label
    "Water sound": "Sonido del agua",  # aria-label
    "Chat with Bloom Mental Health": "Chatee con Bloom Mental Health",  # aria-label
    "Close chat": "Cerrar chat",  # aria-label
    "Type your question…": "Escriba su pregunta…",  # placeholder
    "Send": "Enviar",  # aria-label
    "Bloom Mental Health | Psychiatric Care & Medication Management in Las Vegas": "Bloom Mental Health | Atención psiquiátrica y manejo de medicamentos en Las Vegas",  # <title>

    # ---- /about-us/
    "Compassionate mental health care focused on": "Atención de salud mental compasiva enfocada en",
    "healing, growth": "la sanación, el crecimiento",
    "& emotional wellness": "y el bienestar emocional",
    "About us": "Sobre nosotros",
    "Who we see": "A quién atendemos",
    "Children, adolescents, adults and older adults.": "Niños, adolescentes, adultos y adultos mayores.",
    "Languages": "Idiomas",
    "English, Spanish and Tagalog.": "Inglés, español y tagalo.",
    "When": "Cuándo",
    "Where": "Dónde",
    "2450 Chandler Ave Ste 1, Las Vegas, NV 89120, and by telehealth.": "2450 Chandler Ave Ste 1, Las Vegas, NV 89120, y por telesalud.",
    "Mission": "Misión",
    "To provide compassionate, personalized, and accessible mental health care that supports healing, emotional wellness, and long-term balance.": "Brindar atención de salud mental compasiva, personalizada y accesible que apoye la sanación, el bienestar emocional y el equilibrio a largo plazo.",
    "Vision": "Visión",
    "To create a community where individuals feel empowered, understood, and supported in their journey toward emotional well-being.": "Crear una comunidad donde las personas se sientan empoderadas, comprendidas y apoyadas en su camino hacia el bienestar emocional.",
    "Values": "Valores",
    "We are guided by compassion, trust, respect, confidentiality, and a commitment to providing patient-centered mental health care.": "Nos guían la compasión, la confianza, el respeto, la confidencialidad y el compromiso de brindar atención de salud mental centrada en el paciente.",
    "A team that believes in": "Un equipo que cree en",
    "meeting people where they are": "acompañar a las personas donde estén",
    "Six board-certified psychiatric mental health nurse practitioners, several of them nursing educators, with backgrounds in critical care, long-term care, pediatrics and substance use treatment.": "Seis enfermeros practicantes de salud mental psiquiátrica certificados, varios de ellos educadores de enfermería, con experiencia en cuidados intensivos, cuidados a largo plazo, pediatría y tratamiento del consumo de sustancias.",
    "Meet the Team": "Conozca al equipo",
    "Breadcrumb": "Ruta de navegación",  # aria-label
    "The coffee and tea bar in the Bloom Mental Health office": "La barra de café y té en la oficina de Bloom Mental Health",  # alt
    "Who we serve": "A quién servimos",  # aria-label
    "Mission, vision and values": "Misión, visión y valores",  # aria-label
    "Our providers": "Nuestros profesionales",  # aria-label
    "About Bloom Mental Health | Psychiatric Practice in Las Vegas, NV": "Sobre Bloom Mental Health | Clínica psiquiátrica en Las Vegas, NV",  # <title>

    # ---- /providers/
    "Board-certified care from people who": "Atención certificada de personas que",
    "genuinely listen": "realmente escuchan",
    "Every Bloom provider is a board-certified Psychiatric Mental Health Nurse Practitioner (PMHNP-BC) who treats the whole person, not simply a diagnosis.": "Cada profesional de Bloom es enfermero practicante de salud mental psiquiátrica certificado (PMHNP-BC) y atiende a la persona en su totalidad, no solo un diagnóstico.",
    "Our Providers | Psychiatric Nurse Practitioners at Bloom Mental Health, Las Vegas": "Nuestros profesionales | Enfermeros practicantes psiquiátricos en Bloom Mental Health, Las Vegas",  # <title>

    # ---- /providers/michelle-cuevas-romero/
    "Owner · Psychiatric Mental Health Nurse Practitioner": "Propietaria · Enfermera practicante de salud mental psiquiátrica",
    "Areas of focus": "Áreas de enfoque",
    "MAT": "Tratamiento asistido con medicamentos (MAT)",
    "Pediatric care": "Atención pediátrica",
    "English": "Inglés",
    "Spanish": "Español",
    "Meet": "Conozca a",
    "Michelle Cuevas-Romero is a board-certified Psychiatric Mental Health Nurse Practitioner who is passionate about helping individuals feel heard, understood, and supported throughout their mental health journey.": "Michelle Cuevas-Romero es una enfermera practicante de salud mental psiquiátrica certificada a quien le apasiona ayudar a las personas a sentirse escuchadas, comprendidas y apoyadas a lo largo de su camino de salud mental.",
    "A nurse since 2022, Michelle has experience across mental health, substance use treatment and rehabilitation, medication-assisted treatment (MAT), and pediatric care. She works with individuals experiencing a variety of mental and behavioral health concerns, including anxiety, depression, bipolar disorder, ADHD, autism spectrum disorder, substance use disorders, and other psychiatric conditions.": "Enfermera desde 2022, Michelle tiene experiencia en salud mental, tratamiento y rehabilitación del consumo de sustancias, tratamiento asistido con medicamentos (MAT) y atención pediátrica. Trabaja con personas que enfrentan diversas inquietudes de salud mental y conductual, como ansiedad, depresión, trastorno bipolar, TDAH, trastorno del espectro autista, trastornos por consumo de sustancias y otras condiciones psiquiátricas.",
    "Michelle graduated from Chamberlain University and believes that mental health care should never feel one-size-fits-all. She strives to understand the whole person, not simply a diagnosis, and works collaboratively with each patient to develop an individualized treatment plan that reflects their unique needs, experiences, culture, and goals.": "Michelle se graduó de Chamberlain University y cree que la atención de salud mental nunca debe ser igual para todos. Se esfuerza por comprender a la persona en su totalidad, no solo un diagnóstico, y trabaja en colaboración con cada paciente para desarrollar un plan de tratamiento individualizado que refleje sus necesidades, experiencias, cultura y metas.",
    "Fluent in both English and Spanish, Michelle is especially passionate about helping bridge gaps in mental healthcare within the Latino community. She understands that language, culture, stigma, and access to resources can sometimes create barriers to seeking mental health services. By providing care in Spanish and creating a culturally respectful and welcoming environment, she strives to make it easier for Spanish-speaking individuals and families to feel understood, comfortable, and empowered when seeking care.": "Con dominio del inglés y el español, a Michelle le apasiona especialmente ayudar a cerrar brechas en la atención de salud mental dentro de la comunidad latina. Entiende que el idioma, la cultura, el estigma y el acceso a recursos a veces crean barreras para buscar servicios de salud mental. Al brindar atención en español y crear un ambiente culturalmente respetuoso y acogedor, se esfuerza por facilitar que las personas y familias de habla hispana se sientan comprendidas, cómodas y empoderadas al buscar atención.",
    "In addition to her clinical practice, Michelle serves as a nursing school instructor, where she educates, mentors, and supports future nurses as they develop their clinical skills, confidence, and compassion.": "Además de su práctica clínica, Michelle es instructora en una escuela de enfermería, donde educa, orienta y apoya a futuros enfermeros mientras desarrollan sus habilidades clínicas, su confianza y su compasión.",
    "Her passion for mental health also extends beyond the walls of the clinic. Michelle works alongside nonprofit organizations and participates in community outreach efforts focused on improving access to healthcare and reaching individuals who may otherwise experience barriers to receiving services. She strongly believes in meeting people where they are and bringing compassionate mental healthcare closer to the communities that need it.": "Su pasión por la salud mental también va más allá de las paredes de la clínica. Michelle colabora con organizaciones sin fines de lucro y participa en iniciativas de alcance comunitario enfocadas en mejorar el acceso a la atención médica y llegar a personas que de otro modo enfrentarían barreras para recibir servicios. Cree firmemente en acompañar a las personas donde estén y acercar una atención de salud mental compasiva a las comunidades que la necesitan.",
    "At Bloom Mental Health, Michelle's goal is to create a welcoming, inclusive, and judgment-free environment where patients can feel comfortable being themselves. She believes everyone deserves to be treated with dignity, kindness, and respect, and to have a provider who genuinely listens.": "En Bloom Mental Health, la meta de Michelle es crear un ambiente acogedor, inclusivo y libre de juicios donde los pacientes se sientan cómodos siendo ellos mismos. Cree que todos merecen ser tratados con dignidad, amabilidad y respeto, y tener un profesional que realmente escuche.",
    "Her approach to care is centered on the whole person, because mental health is only one part of your story.": "Su enfoque de atención se centra en la persona en su totalidad, porque la salud mental es solo una parte de su historia.",
    "Care Michelle provides": "Atención que ofrece Michelle",
    "Child & Adolescent Mental Health": "Salud mental infantil y adolescente",
    "Substance Use & MAT": "Consumo de sustancias y MAT",
    "Biography": "Biografía",  # aria-label

    # ---- /providers/christopher-hansen/
    "Psychiatric Mental Health Nurse Practitioner": "Enfermero(a) practicante de salud mental psiquiátrica",
    "Patient education": "Educación del paciente",
    "Christopher Hansen is a board-certified Psychiatric Mental Health Nurse Practitioner with a diverse background in nursing and behavioral healthcare. He began his nursing career in 2021, gaining extensive experience in long-term care and working with individuals living with complex psychiatric conditions, including schizophrenia and other serious mental health disorders.": "Christopher Hansen es un enfermero practicante de salud mental psiquiátrica certificado con una trayectoria diversa en enfermería y atención de salud conductual. Comenzó su carrera de enfermería en 2021 y adquirió amplia experiencia en cuidados a largo plazo y en el trabajo con personas que viven con condiciones psiquiátricas complejas, como la esquizofrenia y otros trastornos graves de salud mental.",
    "As a PMHNP-BC, Christopher provides psychiatric care across the lifespan and is passionate about delivering individualized, compassionate, and inclusive mental health services. He has a particular interest in supporting members of the LGBTQ+ community and strives to create a welcoming, affirming, and judgment-free environment where every patient feels respected and comfortable being themselves.": "Como PMHNP-BC, Christopher brinda atención psiquiátrica en todas las etapas de la vida y le apasiona ofrecer servicios de salud mental individualizados, compasivos e inclusivos. Tiene un interés particular en apoyar a los miembros de la comunidad LGBTQ+ y se esfuerza por crear un ambiente acogedor, afirmativo y libre de juicios donde cada paciente se sienta respetado y cómodo siendo quien es.",
    "Christopher is also passionate about patient education and believes that understanding one's mental health is an important part of treatment. He takes the time to help patients better understand their diagnoses, medications, treatment options, and overall wellness so they can feel informed and actively involved in decisions about their care.": "A Christopher también le apasiona la educación del paciente y cree que comprender la propia salud mental es una parte importante del tratamiento. Se toma el tiempo para ayudar a los pacientes a entender mejor sus diagnósticos, medicamentos, opciones de tratamiento y bienestar general, para que se sientan informados y participen activamente en las decisiones sobre su atención.",
    "His commitment to mental health extends beyond the clinical setting through his involvement with nonprofit organizations and community outreach initiatives. Christopher believes in meeting people where they are, helping bridge gaps in mental healthcare, and connecting underserved individuals with the support and resources they need.": "Su compromiso con la salud mental va más allá del entorno clínico, a través de su participación en organizaciones sin fines de lucro e iniciativas de alcance comunitario. Christopher cree en acompañar a las personas donde estén, ayudar a cerrar brechas en la atención de salud mental y conectar a personas desatendidas con el apoyo y los recursos que necesitan.",
    "Above all, Christopher strives to ensure that each patient is treated as an individual, not simply a diagnosis, and receives care that reflects their unique needs, experiences, identity, and goals.": "Sobre todo, Christopher se esfuerza por que cada paciente sea tratado como un individuo, no solo como un diagnóstico, y reciba una atención que refleje sus necesidades, experiencias, identidad y metas.",

    # ---- /providers/brenda-ortiz/
    "Brenda Ortiz is a board-certified Psychiatric Mental Health Nurse Practitioner with an extensive nursing background. She began her nursing career in 2018, gaining valuable experience in critical care as an ICU nurse, where she developed a strong foundation in caring for individuals with complex medical and emotional needs.": "Brenda Ortiz es una enfermera practicante de salud mental psiquiátrica certificada con una amplia trayectoria en enfermería. Comenzó su carrera de enfermería en 2018 y adquirió valiosa experiencia en cuidados intensivos como enfermera de UCI, donde desarrolló una base sólida en el cuidado de personas con necesidades médicas y emocionales complejas.",
    "As a PMHNP-BC, Brenda provides psychiatric care across the lifespan and is passionate about delivering compassionate, individualized, and culturally responsive mental health services. Fluent in both English and Spanish, she has a special interest in helping bridge gaps in mental healthcare within the Latino community by providing patients and families with care in the language in which they feel most comfortable.": "Como PMHNP-BC, Brenda brinda atención psiquiátrica en todas las etapas de la vida y le apasiona ofrecer servicios de salud mental compasivos, individualizados y culturalmente sensibles. Con dominio del inglés y el español, tiene un interés especial en ayudar a cerrar brechas en la atención de salud mental dentro de la comunidad latina, brindando a pacientes y familias atención en el idioma en el que se sienten más cómodos.",
    "Her commitment to healthcare extends beyond the clinical setting. Brenda works with nonprofit organizations and participates in community outreach efforts focused on improving access to mental health services and reaching individuals who may otherwise face barriers to care.": "Su compromiso con la atención médica va más allá del entorno clínico. Brenda colabora con organizaciones sin fines de lucro y participa en iniciativas de alcance comunitario enfocadas en mejorar el acceso a los servicios de salud mental y llegar a personas que de otro modo enfrentarían barreras para recibir atención.",
    "Brenda is also passionate about education and has experience teaching and mentoring nursing students throughout her career. She strives to empower both her patients and future healthcare professionals through education, compassion, and understanding.": "A Brenda también le apasiona la educación y tiene experiencia enseñando y orientando a estudiantes de enfermería a lo largo de su carrera. Se esfuerza por empoderar tanto a sus pacientes como a los futuros profesionales de la salud mediante la educación, la compasión y la comprensión.",
    "Above all, Brenda believes in meeting patients where they are and creating a welcoming, respectful, and judgment-free environment where every individual feels heard, valued, and actively involved in their care.": "Sobre todo, Brenda cree en acompañar a los pacientes donde estén y crear un ambiente acogedor, respetuoso y libre de juicios donde cada persona se sienta escuchada, valorada y participe activamente en su atención.",

    # ---- /providers/heley-bayot/
    "Family-centered care": "Atención centrada en la familia",
    "Heley Vannessa Erdao Bayot is a board-certified Psychiatric Mental Health Nurse Practitioner with an extensive nursing background spanning nearly a decade. She began her nursing career in 2016 and spent much of her clinical career in critical care as an ICU nurse, developing a strong foundation in caring for patients with complex medical and emotional needs.": "Heley Vannessa Erdao Bayot es una enfermera practicante de salud mental psiquiátrica certificada con una amplia trayectoria en enfermería de casi una década. Comenzó su carrera de enfermería en 2016 y pasó gran parte de su carrera clínica en cuidados intensivos como enfermera de UCI, donde desarrolló una base sólida en el cuidado de pacientes con necesidades médicas y emocionales complejas.",
    "As a PMHNP-BC, Heley provides psychiatric care across the lifespan, with a special interest in working with children, adolescents, and individuals with developmental and behavioral health needs. Her areas of focus include autism spectrum disorder, ADHD, anxiety, depression, and other psychiatric conditions affecting children and adults.": "Como PMHNP-BC, Heley brinda atención psiquiátrica en todas las etapas de la vida, con un interés especial en trabajar con niños, adolescentes y personas con necesidades del desarrollo y de salud conductual. Sus áreas de enfoque incluyen el trastorno del espectro autista, el TDAH, la ansiedad, la depresión y otras condiciones psiquiátricas que afectan a niños y adultos.",
    "In addition to her clinical practice, Heley has dedicated many years to nursing education, teaching and mentoring nursing students as they develop their clinical knowledge, skills, and confidence.": "Además de su práctica clínica, Heley ha dedicado muchos años a la educación en enfermería, enseñando y orientando a estudiantes de enfermería mientras desarrollan sus conocimientos clínicos, sus habilidades y su confianza.",
    "Heley believes in providing compassionate, individualized, and family-centered care. She strives to create a supportive environment where patients and families feel heard, respected, and actively involved in their treatment.": "Heley cree en brindar una atención compasiva, individualizada y centrada en la familia. Se esfuerza por crear un ambiente de apoyo donde los pacientes y sus familias se sientan escuchados, respetados y participen activamente en su tratamiento.",
    "Care Heley provides": "Atención que ofrece Heley",

    # ---- /providers/daniel-fite/
    "Daniel Hunter Fite is a board-certified Psychiatric Mental Health Nurse Practitioner with a diverse background in nursing and behavioral healthcare. Since beginning his nursing career in 2023, Daniel has gained experience working with pediatric patients and individuals affected by mental health and substance use disorders.": "Daniel Hunter Fite es un enfermero practicante de salud mental psiquiátrica certificado con una trayectoria diversa en enfermería y atención de salud conductual. Desde que comenzó su carrera de enfermería en 2023, Daniel ha adquirido experiencia trabajando con pacientes pediátricos y con personas afectadas por trastornos de salud mental y por consumo de sustancias.",
    "As a PMHNP-BC, Daniel provides psychiatric care across the lifespan and is passionate about delivering compassionate, individualized, and inclusive mental health services. He has a special interest in supporting members of the LGBTQ+ community and strives to create a welcoming, affirming, and judgment-free environment where every patient feels respected, understood, and comfortable being themselves.": "Como PMHNP-BC, Daniel brinda atención psiquiátrica en todas las etapas de la vida y le apasiona ofrecer servicios de salud mental compasivos, individualizados e inclusivos. Tiene un interés especial en apoyar a los miembros de la comunidad LGBTQ+ y se esfuerza por crear un ambiente acogedor, afirmativo y libre de juicios donde cada paciente se sienta respetado, comprendido y cómodo siendo quien es.",
    "Daniel strongly believes that education is an important part of mental healthcare. He takes the time to help patients understand their mental health, diagnoses, medications, and treatment options so they can feel informed and empowered to actively participate in their care.": "Daniel cree firmemente que la educación es una parte importante de la atención de salud mental. Se toma el tiempo para ayudar a los pacientes a entender su salud mental, sus diagnósticos, sus medicamentos y sus opciones de tratamiento, para que se sientan informados y empoderados para participar activamente en su atención.",
    "His passion for education also extends to the next generation of healthcare professionals. As a nursing instructor, Daniel teaches and mentors nursing students, emphasizing clinical knowledge, compassion, and patient-centered care.": "Su pasión por la educación también se extiende a la próxima generación de profesionales de la salud. Como instructor de enfermería, Daniel enseña y orienta a estudiantes de enfermería, con énfasis en el conocimiento clínico, la compasión y la atención centrada en el paciente.",
    "Above all, Daniel believes that every patient's journey is unique. He is committed to meeting individuals where they are and providing personalized care that considers the whole person, not simply a diagnosis.": "Sobre todo, Daniel cree que el camino de cada paciente es único. Está comprometido a acompañar a las personas donde estén y brindar una atención personalizada que considere a la persona en su totalidad, no solo un diagnóstico.",
    "Care Daniel provides": "Atención que ofrece Daniel",

    # ---- /providers/kanittha-thanangamsuwan/
    "Kanittha Thanangamsuwan, MSN, APRN, PMHNP-BC, is a board-certified Psychiatric Mental Health Nurse Practitioner at Bloom Mental Health in Las Vegas.": "Kanittha Thanangamsuwan, MSN, APRN, PMHNP-BC, es enfermera practicante de salud mental psiquiátrica certificada en Bloom Mental Health en Las Vegas.",
    "A full biography is coming soon. To ask about scheduling with Kanittha, call the office or request an appointment online.": "Su biografía completa estará disponible próximamente. Para preguntar sobre citas con Kanittha, llame a la oficina o solicite una cita en línea.",

    # ---- /services/
    "From a first evaluation to long-term medication management, therapy and intensive outpatient support, in the office or by telehealth.": "Desde una primera evaluación hasta el manejo de medicamentos a largo plazo, terapia y apoyo ambulatorio intensivo, en la oficina o por telesalud.",
    "Developmentally informed psychiatric assessment and treatment for younger patients.": "Evaluación y tratamiento psiquiátrico adaptados a la etapa de desarrollo de los pacientes más jóvenes.",
    "Psychiatric support for autism-spectrum concerns alongside co-occurring mental health needs.": "Apoyo psiquiátrico para inquietudes del espectro autista junto con necesidades de salud mental concurrentes.",
    "Psychotherapy": "Psicoterapia",
    "Individual talk therapy offered alongside medication management for comprehensive care.": "Terapia individual de conversación junto con el manejo de medicamentos, para una atención integral.",
    "Medication-assisted treatment and psychiatric support for substance use concerns.": "Tratamiento asistido con medicamentos y apoyo psiquiátrico para problemas de consumo de sustancias.",
    "IOP Services": "Programa ambulatorio intensivo (IOP)",
    "Intensive outpatient programming for patients who benefit from a higher level of structured support.": "Programa ambulatorio intensivo para pacientes que se benefician de un mayor nivel de apoyo estructurado.",
    "Telehealth Services": "Servicios de telesalud",
    "Secure, confidential video visits from the comfort of home.": "Consultas por video seguras y confidenciales desde la comodidad de su hogar.",
    "All services": "Todos los servicios",  # aria-label
    "Psychiatric Services in Las Vegas | Bloom Mental Health": "Servicios psiquiátricos en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/psychiatric-evaluations/
    "All Services": "Todos los servicios",
    "At a glance": "De un vistazo",
    "In office, Las Vegas": "En la oficina, Las Vegas",
    "Telehealth": "Telesalud",
    "English · Spanish · Tagalog": "Inglés · Español · Tagalo",
    "Accepting new patients": "Aceptamos pacientes nuevos",
    "Psychiatric Evaluations in Las Vegas": "Evaluaciones psiquiátricas en Las Vegas",
    "Every patient at Bloom Mental Health starts with a comprehensive psychiatric evaluation. It is a conversation, not a checklist: we take time to listen to your concerns, talk through your symptoms, your history and what has or has not helped before, and learn what you want your life to feel like.": "Cada paciente de Bloom Mental Health comienza con una evaluación psiquiátrica completa. Es una conversación, no una lista de verificación: nos tomamos el tiempo para escuchar sus inquietudes, hablar de sus síntomas, su historia y lo que le ha ayudado o no antes, y conocer cómo quiere que se sienta su vida.",
    "From there, your provider shares what they are seeing, answers your questions and builds an individualized care plan with you. That plan may include medication, therapy, further assessment or a referral, and it is always something you help decide.": "Luego, su profesional le comparte lo que observa, responde sus preguntas y crea con usted un plan de atención individualizado. Ese plan puede incluir medicamentos, terapia, una evaluación adicional o una referencia, y siempre es algo que usted ayuda a decidir.",
    "Evaluations are available in the office on Chandler Avenue and by telehealth, for children, adolescents, adults and older adults.": "Las evaluaciones están disponibles en la oficina de Chandler Avenue y por telesalud, para niños, adolescentes, adultos y adultos mayores.",
    "When it may help": "Cuándo puede ayudar",
    "Symptoms that are complex, persistent, or unclear and would benefit from assessment": "Síntomas complejos, persistentes o poco claros que se beneficiarían de una evaluación",
    "A first step when you are not sure what kind of help you need": "Un primer paso cuando no está seguro de qué tipo de ayuda necesita",
    "A fresh look when a past diagnosis or treatment no longer fits": "Una nueva mirada cuando un diagnóstico o tratamiento anterior ya no encaja",
    "What you can expect": "Qué puede esperar",
    "A respectful, nonjudgmental environment": "Un ambiente respetuoso y sin juicios",
    "Collaborative discussion of treatment options": "Conversación colaborativa sobre las opciones de tratamiento",
    "Medication management when clinically appropriate": "Manejo de medicamentos cuando sea clínicamente apropiado",
    "Coordination with the patient's care team, when authorized": "Coordinación con el equipo de atención del paciente, cuando esté autorizado",
    "Services, availability and age ranges can change. Please contact our office at": "Los servicios, la disponibilidad y los rangos de edad pueden cambiar. Comuníquese con nuestra oficina al",
    "to confirm before your visit. If you are in crisis, call or text 988 or call 911.": "para confirmar antes de su visita. Si está en crisis, llame o envíe un mensaje de texto al 988 o llame al 911.",
    "Who you may": "Con quién puede",
    "see": "consultar",
    "Psychiatric Evaluations in Las Vegas | Bloom Mental Health": "Evaluaciones psiquiátricas en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/medication-management/
    "Psychiatric Medication Management in Las Vegas": "Manejo de medicamentos psiquiátricos en Las Vegas",
    "When medication is clinically appropriate, your provider prescribes it and stays with you from there. Follow-up visits look at how well it is working, how you are tolerating it, whether it fits your day-to-day life and whether it still matches your goals.": "Cuando un medicamento es clínicamente apropiado, su profesional lo receta y le da seguimiento desde ese momento. Las consultas de seguimiento revisan qué tan bien está funcionando, cómo lo está tolerando, si se adapta a su vida diaria y si sigue correspondiendo a sus metas.",
    "Medication support should feel collaborative. We explain what a medication is for, what to expect and what to watch for, and we adjust together rather than leave you guessing between visits.": "El apoyo con medicamentos debe sentirse colaborativo. Le explicamos para qué sirve un medicamento, qué esperar y a qué prestar atención, y hacemos ajustes juntos en lugar de dejarle con dudas entre consultas.",
    "If you already take psychiatric medication and need someone to evaluate, monitor or adjust it, we can take over that care.": "Si ya toma medicamentos psiquiátricos y necesita que alguien los evalúe, supervise o ajuste, podemos encargarnos de esa atención.",
    "A patient on psychiatric medication who needs evaluation, monitoring, or adjustment": "Un paciente que toma medicamentos psiquiátricos y necesita evaluación, supervisión o ajuste",
    "Outpatient psychiatric follow-up after a higher level of care": "Seguimiento psiquiátrico ambulatorio después de un nivel de atención más alto",
    "Side effects or a medication that no longer seems to help": "Efectos secundarios o un medicamento que ya no parece ayudar",
    "Psychiatric Medication Management in Las Vegas | Bloom Mental Health": "Manejo de medicamentos psiquiátricos en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/adhd/
    "ADHD Evaluation & Treatment in Las Vegas": "Evaluación y tratamiento del TDAH en Las Vegas",
    "Trouble focusing, staying organized, finishing tasks or sitting still can affect school, work and relationships at any age. An ADHD evaluation at Bloom looks carefully at attention and executive function, and at the other things that can look similar, such as anxiety, sleep problems or mood.": "La dificultad para concentrarse, mantenerse organizado, terminar tareas o quedarse quieto puede afectar la escuela, el trabajo y las relaciones a cualquier edad. Una evaluación de TDAH en Bloom examina con cuidado la atención y la función ejecutiva, y también otras condiciones que pueden parecer similares, como la ansiedad, los problemas de sueño o del estado de ánimo.",
    "If ADHD is part of the picture, your provider builds a treatment plan with you. That can include medication when it is appropriate, along with practical strategies and regular follow-up to see what is actually helping.": "Si el TDAH es parte del panorama, su profesional crea con usted un plan de tratamiento. Este puede incluir medicamentos cuando sea apropiado, junto con estrategias prácticas y seguimiento regular para ver qué está ayudando realmente.",
    "We see children, adolescents and adults, and we involve parents and families when the patient is young.": "Atendemos a niños, adolescentes y adultos, e involucramos a los padres y a la familia cuando el paciente es pequeño.",
    "Possible ADHD symptoms affecting school, work, relationships, or daily organization": "Posibles síntomas de TDAH que afectan la escuela, el trabajo, las relaciones o la organización diaria",
    "Adults who have wondered about ADHD for years": "Adultos que se han preguntado durante años si tienen TDAH",
    "Children and teens whose teachers or parents have raised attention concerns": "Niños y adolescentes cuyos maestros o padres han notado problemas de atención",
    "ADHD Evaluation & Treatment in Las Vegas | Bloom Mental Health": "Evaluación y tratamiento del TDAH en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/anxiety-depression/
    "Anxiety & Depression Treatment in Las Vegas": "Tratamiento de la ansiedad y la depresión en Las Vegas",
    "Anxiety and depression are among the most common reasons people reach out to us, and among the most treatable. Constant worry, panic, avoidance, persistent sadness, loss of interest, low energy or changes in sleep and appetite are all worth talking about.": "La ansiedad y la depresión están entre las razones más comunes por las que las personas nos buscan, y entre las más tratables. La preocupación constante, el pánico, la evitación, la tristeza persistente, la pérdida de interés, la falta de energía o los cambios en el sueño y el apetito son temas que vale la pena hablar.",
    "Your provider will evaluate what you are experiencing and work with you on an evidence-informed plan. That may include medication, therapy or both, with follow-up visits to make sure you are moving in the right direction.": "Su profesional evaluará lo que está viviendo y trabajará con usted en un plan basado en evidencia. Este puede incluir medicamentos, terapia o ambos, con consultas de seguimiento para asegurarse de que avanza en la dirección correcta.",
    "Care is available in person and by telehealth, and in English or Spanish.": "La atención está disponible en persona y por telesalud, en inglés o en español.",
    "Excessive worry, panic symptoms, avoidance, sleep disruption, or difficulty functioning": "Preocupación excesiva, síntomas de pánico, evitación, alteraciones del sueño o dificultad para funcionar",
    "Persistent low mood, loss of interest, fatigue, sleep or appetite changes, or feelings of worthlessness": "Estado de ánimo bajo persistente, pérdida de interés, fatiga, cambios en el sueño o el apetito, o sentimientos de inutilidad",
    "Irritability, mood changes, or a decline in how you are functioning": "Irritabilidad, cambios de humor o un deterioro en su funcionamiento diario",
    "Anxiety & Depression Treatment in Las Vegas | Bloom Mental Health": "Tratamiento de la ansiedad y la depresión en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/bipolar-disorder/
    "Bipolar Disorder Treatment in Las Vegas": "Tratamiento del trastorno bipolar en Las Vegas",
    "Bipolar disorder is a long-term condition, and good care is long-term too. We focus on mood stability over time: careful medication management, attention to early warning signs and steady follow-up.": "El trastorno bipolar es una condición a largo plazo, y la buena atención también lo es. Nos enfocamos en la estabilidad del estado de ánimo a lo largo del tiempo: manejo cuidadoso de medicamentos, atención a las señales de alerta temprana y seguimiento constante.",
    "Your provider works with you to understand your patterns of elevated and depressed mood, find a treatment plan you can live with, and adjust it as life changes.": "Su profesional trabaja con usted para entender sus patrones de estado de ánimo elevado y deprimido, encontrar un plan de tratamiento con el que pueda vivir y ajustarlo a medida que cambia su vida.",
    "If you have had episodes of elevated or depressed mood, significant cycling, or a past diagnosis you want reviewed, we can help.": "Si ha tenido episodios de estado de ánimo elevado o deprimido, ciclos significativos o un diagnóstico anterior que quiere revisar, podemos ayudarle.",
    "Episodes of elevated or depressed mood, significant cycling, or concerns warranting evaluation": "Episodios de estado de ánimo elevado o deprimido, ciclos significativos o inquietudes que ameritan evaluación",
    "Ongoing medication management for a known bipolar diagnosis": "Manejo continuo de medicamentos para un diagnóstico de trastorno bipolar ya conocido",
    "Continuity of care after a hospital stay or a higher level of care": "Continuidad de la atención después de una hospitalización o un nivel de atención más alto",
    "Bipolar Disorder Treatment in Las Vegas | Bloom Mental Health": "Tratamiento del trastorno bipolar en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/ptsd-trauma/
    "PTSD & Trauma Treatment in Las Vegas": "Tratamiento del TEPT y el trauma en Las Vegas",
    "Trauma can show up long after the event, as intrusive memories, nightmares, being on edge, avoiding reminders, or feeling disconnected. You do not have to explain everything at once to get help.": "El trauma puede manifestarse mucho después del evento, como recuerdos intrusivos, pesadillas, sentirse en alerta constante, evitar lo que lo recuerda o sentirse desconectado. No tiene que explicarlo todo de una vez para recibir ayuda.",
    "At Bloom we provide psychiatric support for trauma-related symptoms and the concerns that often come with them, such as anxiety, depression, sleep problems and substance use. Care moves at your pace, in a safe and judgment-free setting.": "En Bloom brindamos apoyo psiquiátrico para los síntomas relacionados con el trauma y las inquietudes que suelen acompañarlos, como ansiedad, depresión, problemas de sueño y consumo de sustancias. La atención avanza a su ritmo, en un entorno seguro y libre de juicios.",
    "Intrusive memories, hyperarousal, avoidance, nightmares, or other trauma-associated symptoms": "Recuerdos intrusivos, hiperexcitación, evitación, pesadillas u otros síntomas asociados al trauma",
    "Sleep problems, anxiety, or low mood that followed a difficult experience": "Problemas de sueño, ansiedad o estado de ánimo bajo después de una experiencia difícil",
    "PTSD & Trauma Treatment in Las Vegas | Bloom Mental Health": "Tratamiento del TEPT y el trauma en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/child-adolescent/
    "Child & Adolescent Psychiatric Care in Las Vegas": "Atención psiquiátrica infantil y adolescente en Las Vegas",
    "Children and teens are not small adults, and their care should not be either. Our assessments for younger patients are developmentally informed and look at how a child is doing at home, at school and with friends.": "Los niños y adolescentes no son adultos pequeños, y su atención tampoco debe serlo. Nuestras evaluaciones para pacientes jóvenes toman en cuenta su etapa de desarrollo y observan cómo le va al niño en casa, en la escuela y con sus amigos.",
    "Parents and caregivers are part of the process. We explain what we see, talk through options, and build a plan that fits the child and the family, with follow-up that keeps everyone informed.": "Los padres y cuidadores forman parte del proceso. Explicamos lo que observamos, conversamos sobre las opciones y creamos un plan que se adapte al niño y a la familia, con un seguimiento que mantiene a todos informados.",
    "Common reasons families reach out include attention concerns, anxiety, low mood, behavior changes and autism-related concerns. Please contact our office to confirm current age ranges.": "Entre las razones comunes por las que las familias nos buscan están los problemas de atención, la ansiedad, el estado de ánimo bajo, los cambios de conducta y las inquietudes relacionadas con el autismo. Comuníquese con nuestra oficina para confirmar los rangos de edad actuales.",
    "Attention, mood, anxiety, or behavior concerns at home or school": "Problemas de atención, estado de ánimo, ansiedad o conducta en casa o en la escuela",
    "Autism-related concerns or co-occurring mental health needs": "Inquietudes relacionadas con el autismo o necesidades de salud mental concurrentes",
    "A second opinion on a child's diagnosis or medication": "Una segunda opinión sobre el diagnóstico o el medicamento de un niño",
    "Child & Adolescent Psychiatric Care in Las Vegas | Bloom Mental Health": "Atención psiquiátrica infantil y adolescente en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/autism/
    "Autism Psychiatric Support in Las Vegas": "Apoyo psiquiátrico para el autismo en Las Vegas",
    "Many autistic children, teens and adults also live with anxiety, ADHD, mood changes or sleep problems. We provide psychiatric support for autism-spectrum concerns alongside those co-occurring needs.": "Muchos niños, adolescentes y adultos autistas también viven con ansiedad, TDAH, cambios de humor o problemas de sueño. Brindamos apoyo psiquiátrico para las inquietudes del espectro autista junto con esas necesidades concurrentes.",
    "Your provider takes time to understand how the person communicates, what is hard for them and what is going well, and works with the patient and family on a plan that respects who they are.": "Su profesional se toma el tiempo para entender cómo se comunica la persona, qué le resulta difícil y qué le va bien, y trabaja con el paciente y la familia en un plan que respeta quiénes son.",
    "Social communication differences, repetitive behaviors, sensory sensitivities, or concerns warranting evaluation": "Diferencias en la comunicación social, conductas repetitivas, sensibilidades sensoriales o inquietudes que ameritan evaluación",
    "Anxiety, attention, mood, or sleep concerns alongside autism": "Problemas de ansiedad, atención, estado de ánimo o sueño junto con el autismo",
    "Autism Psychiatric Support in Las Vegas | Bloom Mental Health": "Apoyo psiquiátrico para el autismo en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/psychotherapy/
    "Psychotherapy (Talk Therapy) in Las Vegas": "Psicoterapia (terapia de conversación) en Las Vegas",
    "Medication can help, and so can having space to talk. We offer individual talk therapy alongside medication management, so your care can address both.": "Los medicamentos pueden ayudar, y también tener un espacio para hablar. Ofrecemos terapia individual de conversación junto con el manejo de medicamentos, para que su atención pueda abordar ambos aspectos.",
    "Therapy is a place to work through what you are carrying, build skills for hard moments and make changes that last, with someone who is on your side.": "La terapia es un lugar para procesar lo que está cargando, desarrollar habilidades para los momentos difíciles y hacer cambios duraderos, con alguien que está de su lado.",
    "Stress, anxiety, low mood, grief, or life changes you want support with": "Estrés, ansiedad, estado de ánimo bajo, duelo o cambios de vida con los que quiere apoyo",
    "Patients who want therapy alongside their medication care": "Pacientes que desean terapia junto con su tratamiento con medicamentos",
    "Psychotherapy (Talk Therapy) in Las Vegas | Bloom Mental Health": "Psicoterapia (terapia de conversación) en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/substance-use-mat/
    "Substance Use Treatment & MAT in Las Vegas": "Tratamiento del consumo de sustancias y MAT en Las Vegas",
    "Substance use is a health condition, not a moral failing. We offer medication-assisted treatment (MAT) and psychiatric support for substance use concerns, including the anxiety, depression and trauma that often travel with them.": "El consumo de sustancias es una condición de salud, no una falla moral. Ofrecemos tratamiento asistido con medicamentos (MAT) y apoyo psiquiátrico para problemas de consumo de sustancias, incluidas la ansiedad, la depresión y el trauma que a menudo los acompañan.",
    "Care is judgment-free and built around where you are right now, whether you are just starting to think about change or already in recovery and need steady support.": "La atención es libre de juicios y se basa en el punto en el que usted se encuentra ahora, ya sea que apenas empiece a pensar en un cambio o que ya esté en recuperación y necesite apoyo constante.",
    "Substance use you want help with, at any stage": "Consumo de sustancias con el que quiere ayuda, en cualquier etapa",
    "Medication-assisted treatment and ongoing monitoring": "Tratamiento asistido con medicamentos y supervisión continua",
    "Mental health concerns that occur alongside substance use": "Problemas de salud mental que se presentan junto con el consumo de sustancias",
    "Substance Use Treatment & MAT in Las Vegas | Bloom Mental Health": "Tratamiento del consumo de sustancias y MAT en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/iop/
    "Intensive Outpatient Program (IOP) in Las Vegas": "Programa Ambulatorio Intensivo (IOP) en Las Vegas",
    "Some seasons call for more than a visit every few weeks. Our intensive outpatient programming (IOP) offers a higher level of structured support while you continue living at home.": "Algunas etapas de la vida requieren más que una consulta cada pocas semanas. Nuestro programa ambulatorio intensivo (IOP) ofrece un mayor nivel de apoyo estructurado mientras usted sigue viviendo en casa.",
    "IOP can be a step up when outpatient care is not enough, or a step down after a hospital stay or residential program. Please contact our office to confirm current availability.": "El IOP puede ser un paso adicional cuando la atención ambulatoria no es suficiente, o un paso de transición después de una hospitalización o un programa residencial. Comuníquese con nuestra oficina para confirmar la disponibilidad actual.",
    "Patients who benefit from a higher level of structured support": "Pacientes que se benefician de un mayor nivel de apoyo estructurado",
    "Outpatient follow-up after a higher level of care": "Seguimiento ambulatorio después de un nivel de atención más alto",
    "Intensive Outpatient Program (IOP) in Las Vegas | Bloom Mental Health": "Programa Ambulatorio Intensivo (IOP) en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /services/telehealth/
    "Telehealth Psychiatry in Nevada": "Psiquiatría por telesalud en Nevada",
    "Telehealth makes it easier to keep your care going when getting to the office is hard. Video visits are secure and confidential, and they offer the same thoughtful care and professional guidance as an office visit.": "La telesalud facilita continuar con su atención cuando es difícil llegar a la oficina. Las consultas por video son seguras y confidenciales, y ofrecen la misma atención cuidadosa y orientación profesional que una consulta en la oficina.",
    "Many evaluations and follow-up visits can be done by telehealth. When you request an appointment, tell us whether you prefer video, the office on Chandler Avenue, or either one.": "Muchas evaluaciones y consultas de seguimiento pueden hacerse por telesalud. Cuando solicite una cita, díganos si prefiere video, la oficina de Chandler Avenue o cualquiera de las dos.",
    "Busy schedules, transportation or mobility challenges": "Horarios ocupados, dificultades de transporte o de movilidad",
    "Follow-up visits that do not need to be in person": "Consultas de seguimiento que no necesitan ser en persona",
    "Anyone who is more comfortable talking from home": "Cualquier persona que se sienta más cómoda hablando desde casa",
    "Telehealth Psychiatry in Nevada | Bloom Mental Health": "Psiquiatría por telesalud en Nevada | Bloom Mental Health",  # <title>

    # ---- /insurance/
    "Coverage that works for you, and": "Cobertura que le funciona, y",
    "We are credentialed with most major plans in Nevada, and offer straightforward self-pay pricing.": "Estamos acreditados con la mayoría de los planes principales de Nevada y ofrecemos precios claros sin seguro.",
    "Credentialed Insurances": "Seguros acreditados",
    "Plans we": "Planes que",
    "accept": "aceptamos",
    "Pending Credentialing": "Acreditación en trámite",
    "Medicaid MCOs": "MCO de Medicaid",
    "Because insurance participation and plan benefits can change, please contact our office at": "Como la participación en seguros y los beneficios de los planes pueden cambiar, comuníquese con nuestra oficina al",
    "to confirm your coverage before your first visit.": "para confirmar su cobertura antes de su primera consulta.",
    "New Patients & Cash Pricing": "Pacientes nuevos y precios sin seguro",
    "Self-pay": "Consultas",
    "visits": "sin seguro",
    "Initial visit (self-pay)": "Consulta inicial (sin seguro)",
    "Follow-up visit (self-pay)": "Consulta de seguimiento (sin seguro)",
    "We are currently accepting new patients": "Actualmente aceptamos pacientes nuevos",
    "Telehealth available": "Telesalud disponible",
    "Early mornings, evenings, Saturdays & Sundays": "Temprano por la mañana, por la tarde, sábados y domingos",
    "Insurance & Self-Pay Pricing | Bloom Mental Health, Las Vegas": "Seguros y precios sin seguro | Bloom Mental Health, Las Vegas",  # <title>

    # ---- /for-providers/
    "Partnering for better": "Colaborando por una mejor",
    "mental health": "salud mental",
    "A referral resource for the colleagues who trust us with their patients' care. We are accepting new patients, and we aim to make referring as simple and collaborative as possible for your practice.": "Un recurso de referencias para los colegas que nos confían la atención de sus pacientes. Aceptamos pacientes nuevos y buscamos que referir sea lo más sencillo y colaborativo posible para su consultorio.",
    "Call 702-350-1419": "Llame al 702-350-1419",
    "How to refer": "Cómo referir",
    "Phone": "Teléfono",
    "Email": "Correo electrónico",
    "Referring a patient to": "Referir a un paciente a",
    "We provide compassionate, whole-person outpatient psychiatric care for children, adolescents, adults and older adults, with bilingual providers who speak Spanish and Tagalog and telehealth available.": "Brindamos atención psiquiátrica ambulatoria compasiva e integral para niños, adolescentes, adultos y adultos mayores, con profesionales bilingües que hablan español y tagalo, y telesalud disponible.",
    "Before referral": "Antes de referir",
    "Confirm the patient's insurance plan": "Confirme el plan de seguro del paciente",
    "Confirm the service being requested": "Confirme el servicio que se solicita",
    "Provide accurate patient contact information": "Proporcione información de contacto correcta del paciente",
    "Send relevant clinical information": "Envíe la información clínica pertinente",
    "What patients can expect": "Qué pueden esperar los pacientes",
    "A referral does not guarantee an appointment, diagnosis, medication, or insurance coverage. Clinical decisions are based on the patient's individual assessment and needs. Please contact our office to confirm current age ranges, services, availability, and insurance participation before referring. See": "Una referencia no garantiza una cita, un diagnóstico, un medicamento ni cobertura de seguro. Las decisiones clínicas se basan en la evaluación y las necesidades individuales del paciente. Comuníquese con nuestra oficina para confirmar los rangos de edad, los servicios, la disponibilidad y la participación en seguros actuales antes de referir. Consulte",
    "insurance": "seguros",
    "and": "y",
    "services": "servicios",
    "Who May Benefit From Referral": "Quién puede beneficiarse de una referencia",
    "When to": "Cuándo",
    "consider Bloom": "considerar Bloom",
    "Consider Bloom Mental Health when a patient may benefit from outpatient psychiatric assessment, diagnosis, medication management, or ongoing psychiatric follow-up.": "Considere Bloom Mental Health cuando un paciente pueda beneficiarse de una evaluación psiquiátrica ambulatoria, un diagnóstico, el manejo de medicamentos o un seguimiento psiquiátrico continuo.",
    "Mood Concerns": "Problemas del estado de ánimo",
    "Persistent sadness, loss of interest, mood changes, irritability, or functional decline.": "Tristeza persistente, pérdida de interés, cambios de humor, irritabilidad o deterioro funcional.",
    "Anxiety Concerns": "Problemas de ansiedad",
    "Excessive worry, panic symptoms, avoidance, sleep disruption, or difficulty functioning.": "Preocupación excesiva, síntomas de pánico, evitación, alteraciones del sueño o dificultad para funcionar.",
    "Attention Concerns": "Problemas de atención",
    "Possible ADHD symptoms affecting school, work, relationships, or daily organization.": "Posibles síntomas de TDAH que afectan la escuela, el trabajo, las relaciones o la organización diaria.",
    "Mood Instability": "Inestabilidad del estado de ánimo",
    "Episodes of elevated or depressed mood, significant cycling, or concerns warranting evaluation.": "Episodios de estado de ánimo elevado o deprimido, ciclos significativos o inquietudes que ameritan evaluación.",
    "Trauma-Related Symptoms": "Síntomas relacionados con el trauma",
    "Intrusive memories, hyperarousal, avoidance, nightmares, or other trauma-associated symptoms.": "Recuerdos intrusivos, hiperexcitación, evitación, pesadillas u otros síntomas asociados al trauma.",
    "Medication Needs": "Necesidades de medicamentos",
    "A patient on psychiatric medication who needs evaluation, monitoring, or adjustment.": "Un paciente que toma medicamentos psiquiátricos y necesita evaluación, supervisión o ajuste.",
    "Diagnostic Clarification": "Aclaración diagnóstica",
    "Symptoms that are complex, persistent, or unclear and would benefit from assessment.": "Síntomas complejos, persistentes o poco claros que se beneficiarían de una evaluación.",
    "Post-Discharge Continuity": "Continuidad después del alta",
    "A patient who needs outpatient psychiatric follow-up after a higher level of care.": "Un paciente que necesita seguimiento psiquiátrico ambulatorio después de un nivel de atención más alto.",
    "Depression Symptoms": "Síntomas de depresión",
    "Persistent low mood, anhedonia, fatigue, sleep or appetite changes, or feelings of worthlessness.": "Estado de ánimo bajo persistente, anhedonia, fatiga, cambios en el sueño o el apetito, o sentimientos de inutilidad.",
    "Autism-Related Concerns": "Inquietudes relacionadas con el autismo",
    "Social communication differences, repetitive behaviors, sensory sensitivities, or concerns warranting evaluation.": "Diferencias en la comunicación social, conductas repetitivas, sensibilidades sensoriales o inquietudes que ameritan evaluación.",
    "Urgent / Emergency Needs": "Necesidades urgentes o de emergencia",
    "Bloom Mental Health is an outpatient practice. Patients experiencing an immediate safety concern, medical emergency, or acute psychiatric crisis requiring a higher level of care should be directed to the appropriate emergency or crisis service rather than a routine outpatient referral.": "Bloom Mental Health es una clínica ambulatoria. Los pacientes con un problema de seguridad inmediato, una emergencia médica o una crisis psiquiátrica aguda que requiera un nivel de atención más alto deben ser dirigidos al servicio de emergencia o de crisis correspondiente, en lugar de una referencia ambulatoria de rutina.",
    "Refer a Patient | Outpatient Psychiatry in Las Vegas | Bloom Mental Health": "Referir a un paciente | Psiquiatría ambulatoria en Las Vegas | Bloom Mental Health",  # <title>

    # ---- /faq/
    "Answers to common questions about our": "Respuestas a preguntas comunes sobre nuestros",
    "mental health services": "servicios de salud mental",
    "What services does Bloom Mental Health provide?": "¿Qué servicios ofrece Bloom Mental Health?",
    "We provide outpatient psychiatric care, including psychiatric evaluations, medication management, ADHD evaluation and treatment, anxiety and depression treatment, bipolar disorder treatment, PTSD and trauma treatment, child and adolescent mental health, autism support, psychotherapy, substance use treatment and MAT, IOP services and telehealth.": "Brindamos atención psiquiátrica ambulatoria, que incluye evaluaciones psiquiátricas, manejo de medicamentos, evaluación y tratamiento del TDAH, tratamiento de la ansiedad y la depresión, tratamiento del trastorno bipolar, tratamiento del TEPT y el trauma, salud mental infantil y adolescente, apoyo para el autismo, psicoterapia, tratamiento del consumo de sustancias y MAT, servicios de IOP y telesalud.",
    "Are you accepting new patients?": "¿Aceptan pacientes nuevos?",
    "Yes. We are currently accepting new patients. You can request an appointment online or call 702-350-1419.": "Sí. Actualmente aceptamos pacientes nuevos. Puede solicitar una cita en línea o llamar al 702-350-1419.",
    "Who do you see?": "¿A quién atienden?",
    "We see children, adolescents, adults and older adults. Please contact our office to confirm current age ranges.": "Atendemos a niños, adolescentes, adultos y adultos mayores. Comuníquese con nuestra oficina para confirmar los rangos de edad actuales.",
    "Do you offer care in Spanish or Tagalog?": "¿Ofrecen atención en español o tagalo?",
    "Yes. We have bilingual providers who speak Spanish and Tagalog. Let us know your preferred language when you request an appointment.": "Sí. Tenemos profesionales bilingües que hablan español y tagalo. Indíquenos su idioma preferido cuando solicite una cita.",
    "Do you offer virtual or telehealth appointments?": "¿Ofrecen citas virtuales o por telesalud?",
    "Yes, we offer secure and confidential telehealth appointments for individuals seeking convenient access to mental health care from the comfort of home.": "Sí, ofrecemos citas por telesalud seguras y confidenciales para quienes buscan un acceso cómodo a la atención de salud mental desde su hogar.",
    "What insurance do you accept?": "¿Qué seguros aceptan?",
    "We are credentialed with Aetna, Carelon (BCBS), CareSource, Evernorth (Cigna), Medicare, UHC / Optum, UMR, Alignment and Medicaid FFS. Credentialing is pending with Culinary Health Fund, SilverSummit, Molina, Sierra Health and Life HPN and Medicaid MCOs. Because participation and plan benefits can change, please contact our office to confirm your coverage.": "Estamos acreditados con Aetna, Carelon (BCBS), CareSource, Evernorth (Cigna), Medicare, UHC / Optum, UMR, Alignment y Medicaid FFS. La acreditación está en trámite con Culinary Health Fund, SilverSummit, Molina, Sierra Health and Life HPN y las MCO de Medicaid. Como la participación y los beneficios de los planes pueden cambiar, comuníquese con nuestra oficina para confirmar su cobertura.",
    "What does it cost without insurance?": "¿Cuánto cuesta sin seguro?",
    f"Self-pay visits are ${_SP['initial']} for an initial visit and ${_SP['follow_up']} for a follow-up visit.":
        f"Las consultas sin seguro cuestan ${_SP['initial']} la consulta inicial y ${_SP['follow_up']} la consulta de seguimiento.",
    "When can I be seen?": "¿Cuándo me pueden atender?",
    "We offer flexible times, including early mornings, evenings, Saturdays and Sundays. Call 702-350-1419 or request an appointment and our team will find a time with you.": "Ofrecemos horarios flexibles, incluidos temprano por la mañana, por la tarde, sábados y domingos. Llame al 702-350-1419 o solicite una cita y nuestro equipo encontrará un horario con usted.",
    "What can I expect during my first appointment?": "¿Qué puedo esperar en mi primera cita?",
    "Your first appointment includes a comprehensive evaluation where we discuss your concerns, symptoms, medical history, and wellness goals to create a personalized care plan.": "Su primera cita incluye una evaluación completa en la que hablamos de sus inquietudes, síntomas, historial médico y metas de bienestar para crear un plan de atención personalizado.",
    "Do you prescribe medication if needed?": "¿Recetan medicamentos si es necesario?",
    "Yes, medication management is available when appropriate as part of a personalized treatment plan focused on your mental and emotional well-being.": "Sí, el manejo de medicamentos está disponible cuando es apropiado, como parte de un plan de tratamiento personalizado enfocado en su bienestar mental y emocional.",
    "Is my information kept confidential?": "¿Mi información se mantiene confidencial?",
    "Absolutely. Your privacy and confidentiality are extremely important to us, and all services are provided in a safe and secure environment.": "Por supuesto. Su privacidad y confidencialidad son sumamente importantes para nosotros, y todos los servicios se brindan en un entorno seguro y protegido.",
    "How do I know if mental health support is right for me?": "¿Cómo sé si el apoyo de salud mental es adecuado para mí?",
    "If you are experiencing stress, anxiety, depression, emotional overwhelm, trauma, or changes in mood or behavior, mental health support may help provide guidance and healing.": "Si está pasando por estrés, ansiedad, depresión, agobio emocional, trauma o cambios en su estado de ánimo o su conducta, el apoyo de salud mental puede brindarle orientación y ayudarle a sanar.",
    "How often will I need follow-up appointments?": "¿Con qué frecuencia necesitaré citas de seguimiento?",
    "Follow-up care is personalized based on your treatment plan, goals, and progress to ensure ongoing support and continuity of care.": "La atención de seguimiento se personaliza según su plan de tratamiento, sus metas y su progreso, para asegurar un apoyo continuo y la continuidad de la atención.",
    "What if I am in crisis?": "¿Qué hago si estoy en crisis?",
    "Bloom Mental Health is an outpatient practice and this website is not an emergency service. If you are in immediate danger or thinking about harming yourself, call or text 988 (Suicide and Crisis Lifeline) or call 911.": "Bloom Mental Health es una clínica ambulatoria y este sitio web no es un servicio de emergencias. Si está en peligro inmediato o piensa en hacerse daño, llame o envíe un mensaje de texto al 988 (Línea de Prevención del Suicidio y Crisis) o llame al 911.",
    "Frequently asked questions": "Preguntas frecuentes",  # aria-label
    "FAQ | Bloom Mental Health, Las Vegas Psychiatric Care": "Preguntas frecuentes | Bloom Mental Health, atención psiquiátrica en Las Vegas",  # <title>

    # ---- /contact/
    "Contact Us": "Contáctenos",
    "Reach out for personalized mental health support": "Comuníquese con nosotros para recibir apoyo de salud mental personalizado",
    "& guidance": "y orientación",
    "Send us a message below and a member of our team will reach out within one business day. Ready to book? Use the appointment request instead.": "Envíenos un mensaje abajo y un miembro de nuestro equipo se comunicará con usted dentro de un día hábil. ¿Listo para hacer una cita? Use la solicitud de cita.",
    "Send a message": "Enviar un mensaje",
    "Request an appointment": "Solicitar una cita",
    "Tell us what you need. No medical details are necessary here; we will ask when we call.": "Díganos qué necesita. No es necesario incluir detalles médicos aquí; se los preguntaremos cuando le llamemos.",
    "Your name": "Su nombre",
    "Your email": "Su correo electrónico",
    "Subject": "Asunto",
    "(optional)": "(opcional)",
    "Send message": "Enviar mensaje",
    "If you are in crisis or thinking about harming yourself, call or text": "Si está en crisis o piensa en hacerse daño, llame o envíe un mensaje de texto al",
    ". This form is not monitored around the clock.": ". Este formulario no se supervisa las 24 horas.",
    "Visit": "Visítenos",
    "Get directions": "Cómo llegar",
    "Call": "Llámenos",
    "Hours": "Horario",
    "Office details": "Datos de la oficina",  # aria-label
    "Map": "Mapa",  # aria-label
    "Map to Bloom Mental Health, 2450 Chandler Ave Ste 1, Las Vegas, NV 89120": "Mapa a Bloom Mental Health, 2450 Chandler Ave Ste 1, Las Vegas, NV 89120",  # title
    "Contact Bloom Mental Health | 2450 Chandler Ave, Las Vegas, NV": "Contacte a Bloom Mental Health | 2450 Chandler Ave, Las Vegas, NV",  # <title>

    # ---- /request-appointment/
    "Get Started": "Comience",
    "Request an": "Solicite una",
    "appointment": "cita",
    "Tell us a little about what you need and the best way to reach you. A person from our team calls or emails you back to set a time.": "Cuéntenos un poco sobre lo que necesita y la mejor manera de comunicarnos con usted. Una persona de nuestro equipo le devolverá la llamada o le escribirá por correo electrónico para fijar un horario.",
    "You can also call": "También puede llamar al",
    ". If you are in crisis or thinking about harming yourself, call or text": ". Si está en crisis o piensa en hacerse daño, llame o envíe un mensaje de texto al",
    "Appointment request": "Solicitud de cita",  # aria-label
    "Request an appointment with Bloom Mental Health": "Solicite una cita con Bloom Mental Health",  # title
    "Request an Appointment | Bloom Mental Health, Las Vegas": "Solicitar una cita | Bloom Mental Health, Las Vegas",  # <title>

    # ---- /sms/
    "Text Message Program": "Programa de Mensajes de Texto",
    "text messages": "mensajes de texto",
    "Customer-care texts about your request and your appointments, only if you ask for them.": "Mensajes de texto de atención al cliente sobre su solicitud y sus citas, solo si usted los pide.",
    "Questions": "Preguntas",
    "Mail": "Correo",
    "What the program is": "Qué es el programa",
    "Bloom Mental Health sends customer-care text messages to people who ask for them: confirmations of appointment requests, appointment reminders, links to join a telehealth visit, and replies to questions you text us. We never send marketing or promotional texts, and texts never include diagnoses, medications, or other clinical details.": "Bloom Mental Health envía mensajes de texto de atención al cliente a las personas que los solicitan: confirmaciones de solicitudes de cita, recordatorios de citas, enlaces para unirse a una consulta por telesalud y respuestas a las preguntas que nos envíe por mensaje de texto. Nunca enviamos mensajes de marketing ni promocionales, y los mensajes nunca incluyen diagnósticos, medicamentos ni otros detalles clínicos.",
    "How to join": "Cómo inscribirse",
    "Joining is optional. On our": "Inscribirse es opcional. En nuestro",
    "appointment request form": "formulario de solicitud de cita",
    ", enter your mobile number and check the box next to this statement:": ", ingrese su número de celular y marque la casilla junto a esta declaración:",
    "Optional: By providing your phone number and checking this box, you agree to receive customer-care text messages from Bloom Mental Health about your request and your appointments, such as confirmations and reminders. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. We will not share mobile information with third parties for promotional or marketing purposes. See our Text Message Program, SMS Terms, and Privacy Policy.": "Opcional: Al proporcionar su número de teléfono y marcar esta casilla, usted acepta recibir mensajes de texto de atención al cliente de Bloom Mental Health sobre su solicitud y sus citas, como confirmaciones y recordatorios. La frecuencia de los mensajes puede variar. Pueden aplicarse tarifas estándar de mensajes y datos. Responda STOP para cancelar la suscripción. Responda HELP para obtener ayuda. El consentimiento no es una condición de compra. No compartiremos información móvil con terceros con fines promocionales o de marketing. Consulte nuestro Programa de Mensajes de Texto, los Términos de SMS y la Política de Privacidad.",
    "The box is unchecked unless you check it, the form works without it, and the phone number is optional. We only text a number whose owner agreed on our form; we never text a number someone else gave us.": "La casilla está desmarcada a menos que usted la marque, el formulario funciona sin ella y el número de teléfono es opcional. Solo enviamos mensajes de texto a un número cuyo titular aceptó en nuestro formulario; nunca enviamos mensajes a un número que otra persona nos dio.",
    "Frequency and cost": "Frecuencia y costo",
    "Message frequency may vary, usually a few texts around each request or appointment. Standard Message and Data Rates may apply.": "La frecuencia de los mensajes puede variar; por lo general, son unos pocos mensajes por cada solicitud o cita. Pueden aplicarse tarifas estándar de mensajes y datos.",
    "Stop or get help": "Cancelar u obtener ayuda",
    "Reply": "Responda",
    "to any text to opt out. You will get one confirmation and no further messages. Reply": "a cualquier mensaje para cancelar la suscripción. Recibirá una confirmación y ningún mensaje más. Responda",
    "for help, call 702-350-1419, or email care@bloommentalhealthlv.com. To join again later, reply START or check the box on the form again.": "para obtener ayuda, llame al 702-350-1419 o escriba a care@bloommentalhealthlv.com. Para inscribirse de nuevo más adelante, responda START o vuelva a marcar la casilla en el formulario.",
    "We will not share mobile information with third parties for promotional or marketing purposes. Text messaging originator opt-in data and consent will not be shared with any third parties. Details are in our": "No compartiremos información móvil con terceros con fines promocionales o de marketing. Los datos de inscripción y el consentimiento del originador de mensajes de texto no se compartirán con terceros. Los detalles están en nuestro",
    "SMS Terms": "Términos de SMS",
    ", and": " y",
    "Last updated September 25, 2026.": "Última actualización: 25 de septiembre de 2026.",
    "Request an appointment,": "Solicite una cita,",
    "with or without texts": "con o sin mensajes de texto",
    "A person from our team calls, emails or texts you back to set a time. Texts are only sent if you check the box.": "Una persona de nuestro equipo le devolverá la llamada, le escribirá por correo electrónico o le enviará un mensaje de texto para fijar un horario. Los mensajes de texto solo se envían si usted marca la casilla.",
    "First name": "Nombre",
    "Last name": "Apellido",
    "Mobile phone": "Teléfono celular",
    "Optional: By providing your phone number and checking this box, you agree to receive customer-care text messages from Bloom Mental Health about your request and your appointments, such as confirmations and reminders. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. We will not share mobile information with third parties for promotional or marketing purposes. See our": "Opcional: Al proporcionar su número de teléfono y marcar esta casilla, usted acepta recibir mensajes de texto de atención al cliente de Bloom Mental Health sobre su solicitud y sus citas, como confirmaciones y recordatorios. La frecuencia de los mensajes puede variar. Pueden aplicarse tarifas estándar de mensajes y datos. Responda STOP para cancelar la suscripción. Responda HELP para obtener ayuda. El consentimiento no es una condición de compra. No compartiremos información móvil con terceros con fines promocionales o de marketing. Consulte nuestro",
    "Send my request": "Enviar mi solicitud",
    "Text Message Program | Bloom Mental Health": "Programa de Mensajes de Texto | Bloom Mental Health",  # <title>

    # ---- /terms/
    "Terms of use &": "Términos de uso y",
    "SMS terms": "términos de SMS",
    "Using this website": "Uso de este sitio web",
    "This website shares general information about Bloom Mental Health, an outpatient psychiatric practice in Las Vegas, Nevada. It is not medical advice and does not create a patient relationship. Submitting a form is a request to be contacted, not an appointment.": "Este sitio web comparte información general sobre Bloom Mental Health, una clínica psiquiátrica ambulatoria en Las Vegas, Nevada. No es un consejo médico y no crea una relación de paciente. Enviar un formulario es una solicitud para que lo contacten, no una cita.",
    "Not for emergencies": "No es para emergencias",
    "This website, its forms, and our text messages are not monitored around the clock and are not emergency services. If you are in crisis or thinking about harming yourself, call or text 988 (Suicide and Crisis Lifeline) or call 911.": "Este sitio web, sus formularios y nuestros mensajes de texto no se supervisan las 24 horas y no son servicios de emergencia. Si está en crisis o piensa en hacerse daño, llame o envíe un mensaje de texto al 988 (Línea de Prevención del Suicidio y Crisis) o llame al 911.",
    "Program:": "Programa:",
    "Bloom Mental Health customer-care text messages about your request and your appointments, such as confirmations, reminders, and telehealth visit links. No marketing messages.": "Mensajes de texto de atención al cliente de Bloom Mental Health sobre su solicitud y sus citas, como confirmaciones, recordatorios y enlaces para consultas por telesalud. Sin mensajes de marketing.",
    "Opt-in:": "Inscripción:",
    "only by checking the optional box on our appointment request form with your mobile number. Consent is not a condition of purchase or of receiving care.": "solo marcando la casilla opcional de nuestro formulario de solicitud de cita con su número de celular. El consentimiento no es una condición de compra ni para recibir atención.",
    "Message frequency may vary.": "La frecuencia de los mensajes puede variar.",
    "Standard Message and Data Rates may apply.": "Pueden aplicarse tarifas estándar de mensajes y datos.",
    "Opt out:": "Cancelar:",
    "reply STOP at any time; you will receive one confirmation and no further messages.": "responda STOP en cualquier momento; recibirá una confirmación y ningún mensaje más.",
    "Help:": "Ayuda:",
    "reply HELP, call 702-350-1419, or email care@bloommentalhealthlv.com.": "responda HELP, llame al 702-350-1419 o escriba a care@bloommentalhealthlv.com.",
    "Carriers are not liable for delayed or undelivered messages.": "Los operadores no son responsables de los mensajes retrasados o no entregados.",
    "We will not share mobile information with third parties for promotional or marketing purposes. See our": "No compartiremos información móvil con terceros con fines promocionales o de marketing. Consulte nuestro",
    "Bloom Mental Health, 2450 Chandler Ave Ste 1, Las Vegas, NV 89120. Phone 702-350-1419. Email michelle@bloommentalhealthlv.com.": "Bloom Mental Health, 2450 Chandler Ave Ste 1, Las Vegas, NV 89120. Teléfono 702-350-1419. Correo electrónico michelle@bloommentalhealthlv.com.",
    "Terms & SMS Terms | Bloom Mental Health": "Términos y términos de SMS | Bloom Mental Health",  # <title>

    # ---- /privacy/
    "policy": "política",
    "How this website handles the information you give us.": "Cómo maneja este sitio web la información que usted nos da.",
    "What we collect on this website": "Qué recopilamos en este sitio web",
    "What you type into our forms: name, email, optional phone number, the kind of visit you are looking for, and any note you add.": "Lo que escribe en nuestros formularios: nombre, correo electrónico, número de teléfono opcional, el tipo de consulta que busca y cualquier nota que agregue.",
    "Whether you checked the optional text message box, the exact wording you agreed to, and when.": "Si marcó la casilla opcional de mensajes de texto, el texto exacto que aceptó y cuándo.",
    "Basic, non-identifying website analytics (pages visited, general location, device type) through Google Analytics.": "Análisis básicos del sitio web que no lo identifican (páginas visitadas, ubicación general, tipo de dispositivo) mediante Google Analytics.",
    "How we use it": "Cómo la usamos",
    "To contact you about your request, schedule and remind you of appointments, answer your questions, and improve this website. Health information you share as a patient is protected under HIPAA and our Notice of Privacy Practices, which you receive when you become a patient.": "Para comunicarnos con usted sobre su solicitud, programar sus citas y recordárselas, responder sus preguntas y mejorar este sitio web. La información de salud que comparte como paciente está protegida por HIPAA y por nuestro Aviso de Prácticas de Privacidad, que recibe cuando se convierte en paciente.",
    "We do not sell or share your information": "No vendemos ni compartimos su información",
    "We do not sell or share your personal information with third parties for their marketing or promotional purposes. We use service providers who help us run our practice (for example, our secure practice system, email, and text message delivery), and they may only use information to provide those services to us.": "No vendemos ni compartimos su información personal con terceros para sus fines de marketing o promocionales. Usamos proveedores de servicios que nos ayudan a operar nuestra clínica (por ejemplo, nuestro sistema seguro de la clínica, el correo electrónico y el envío de mensajes de texto), y solo pueden usar la información para prestarnos esos servicios.",
    "Text messages (SMS)": "Mensajes de texto (SMS)",
    "If you opt in to our text messages, we use your mobile number only to send the customer-care messages you asked for.": "Si se inscribe en nuestros mensajes de texto, usamos su número de celular solo para enviarle los mensajes de atención al cliente que solicitó.",
    "We will not share mobile information with third parties for promotional or marketing purposes. Text messaging originator opt-in data and consent will not be shared with any third parties.": "No compartiremos información móvil con terceros con fines promocionales o de marketing. Los datos de inscripción y el consentimiento del originador de mensajes de texto no se compartirán con terceros.",
    "Reply STOP to opt out at any time, or HELP for help. See our": "Responda STOP para cancelar en cualquier momento, o HELP para obtener ayuda. Consulte nuestro",
    "Your choices": "Sus opciones",
    "You can ask us to update or delete the information you submitted through this website by calling 702-350-1419 or emailing michelle@bloommentalhealthlv.com.": "Puede pedirnos que actualicemos o eliminemos la información que envió a través de este sitio web llamando al 702-350-1419 o escribiendo a michelle@bloommentalhealthlv.com.",
    "Changes": "Cambios",
    "We may update this policy. The date below shows the latest version.": "Podemos actualizar esta política. La fecha de abajo muestra la versión más reciente.",
    "Privacy Policy | Bloom Mental Health": "Política de Privacidad | Bloom Mental Health",  # <title>

    # ---- /404.html
    "Page not found": "Página no encontrada",
    "This page has": "Esta página se ha",
    "drifted away": "ido a la deriva",
    "The page you are looking for is not here. Try our services, or request an appointment.": "La página que busca no está aquí. Pruebe nuestros servicios o solicite una cita.",
    "Page not found | Bloom Mental Health": "Página no encontrada | Bloom Mental Health",  # <title>

    # ---- text the page scripts write after load (site.js forms, sw.js sound button, the phone menu, chat link buttons)
    "Sound off": "Sonido apagado",
    "Close menu": "Cerrar menú",
    "Sending…": "Enviando…",
    "Please add your name and a valid email address.": "Por favor, escriba su nombre y un correo electrónico válido.",
    "Please add your first and last name.": "Por favor, escriba su nombre y apellido.",
    "Please add a valid email address.": "Por favor, escriba un correo electrónico válido.",
    "Please enter a 10-digit mobile number, or leave it blank.": "Escriba un número de celular de 10 dígitos o deje el campo en blanco.",
    "Something went wrong. Please call 702-350-1419 or try again in a moment.": "Algo salió mal. Llame al 702-350-1419 o inténtelo de nuevo en un momento.",
    "Insurance & pricing →": "Seguros y precios →",
    "Request an appointment →": "Solicitar una cita →",
    "Meet our providers →": "Conozca a nuestros profesionales →",
    "Our services →": "Nuestros servicios →",
    "Directions & contact →": "Cómo llegar y contacto →",
    "Text message program →": "Programa de mensajes de texto →",
    "For referring providers →": "Para profesionales que refieren pacientes →",
    "Your message": "Su mensaje",
    "Tagalog": "Tagalo",
    "Language / Idioma": "Idioma / Language",
}

# Shown as-is in both languages (names, credentials, plans, addresses). Listed so the coverage check stays quiet about them.
SAME = [
    "2450 Chandler Ave Ste 1",
    "2450 Chandler Ave Ste 1, Las Vegas, NV 89120",
    "Aetna",
    "Alignment",
    "Bayot",
    "Bloom",
    "Bloom Mental Health",
    "Brenda",
    "Brenda Ortiz",
    "Brenda Ortiz, MSN, APRN, PMHNP-BC",
    "Brenda Ortiz, MSN, APRN, PMHNP-BC | Bloom Mental Health, Las Vegas",
    "CareSource",
    "Carelon (BCBS)",
    "Christopher",
    "Christopher Hansen",
    "Christopher Hansen, MSN, APRN, PMHNP-BC",
    "Christopher Hansen, MSN, APRN, PMHNP-BC | Bloom Mental Health, Las Vegas",
    "Cuevas-Romero",
    "Culinary Health Fund",
    "DF",
    "Daniel",
    "Daniel Hunter Fite",
    "Daniel Hunter Fite, MSN, APRN, PMHNP-BC | Bloom Mental Health, Las Vegas",
    "Erdao",
    "Evernorth (Cigna)",
    "Fax",
    "Fax: 702-357-5249",
    "Fite",
    "HELP",
    "Hansen",
    "Heley",
    "Heley Vannessa Erdao Bayot",
    "Heley Vannessa Erdao Bayot, MSN, APRN, PMHNP-BC",
    "Heley Vannessa Erdao Bayot, MSN, APRN, PMHNP-BC | Bloom Mental Health, Las Vegas",
    "Hunter",
    "Kanittha",
    "Kanittha Thanangamsuwan",
    "Kanittha Thanangamsuwan, MSN, APRN, PMHNP-BC",
    "Kanittha Thanangamsuwan, MSN, APRN, PMHNP-BC | Bloom Mental Health, Las Vegas",
    "Las Vegas, NV 89120",
    "MSN, APRN, PMHNP-BC",
    "Medicaid FFS",
    "Medicare",
    "Michelle",
    "Michelle Cuevas-Romero",
    "Michelle Cuevas-Romero, MSN, APRN, PMHNP-BC",
    "Michelle Cuevas-Romero, MSN, APRN, PMHNP-BC | Bloom Mental Health, Las Vegas",
    "Molina",
    "NPI",
    "Ortiz",
    "STOP",
    "Sierra Health and Life HPN",
    "SilverSummit",
    "Thanangamsuwan",
    "UHC / Optum",
    "UMR",
    "Vannessa",
    "michelle@bloommentalhealthlv.com",
    "¿Hablan español?",
]

# Same English, different Spanish on one page ("<path>|text"), or inside one heading on that page ("<path> h1|text").
_ENF_M = "Enfermero practicante de salud mental psiquiátrica"
_ENF_F = "Enfermera practicante de salud mental psiquiátrica"
ES_SCOPED = {
    "/providers/christopher-hansen/|Psychiatric Mental Health Nurse Practitioner": _ENF_M,
    "/providers/daniel-fite/|Psychiatric Mental Health Nurse Practitioner": _ENF_M,
    "/providers/brenda-ortiz/|Psychiatric Mental Health Nurse Practitioner": _ENF_F,
    "/providers/heley-bayot/|Psychiatric Mental Health Nurse Practitioner": _ENF_F,
    "/providers/kanittha-thanangamsuwan/|Psychiatric Mental Health Nurse Practitioner": _ENF_F,
    # <h1>Bloom Mental Health <em>text messages</em></h1> reads backwards in Spanish
    "/sms/ h1|Bloom Mental Health": "Mensajes de texto de",
    "/sms/ h1|text messages": "Bloom Mental Health",
    # <h1>Privacy <em>policy</em></h1>
    "/privacy/ h1|Privacy": "Política de",
    "/privacy/ h1|policy": "privacidad",
}

# Messages with a name in them (site.js success lines). JavaScript regex source -> replacement ($1 = the name).
ES_PATTERNS = [
    [r"^Thank you, (.+)\. Your message is in\. A member of our team will reach out within one business day\.$",
     "Gracias, $1. Recibimos su mensaje. Un miembro de nuestro equipo se comunicará con usted dentro de un día hábil."],
    [r"^Thank you, (.+)\. Your request is in\. A member of our team will reach out within one business day\.$",
     "Gracias, $1. Recibimos su solicitud. Un miembro de nuestro equipo se comunicará con usted dentro de un día hábil."],
]
