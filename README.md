# Python Screening Task 3: Evaluating Open Source Models for Student Competence Analysis

## Objective
This task explores whether existing open-source AI models can be adapted to **analyze student-written Python code** and generate **meaningful prompts** that assess conceptual understanding, identify gaps in reasoning, and encourage deeper learning without directly giving away solutions.

---

## Research Plan

**Approach to identifying & evaluating models**  
I began by surveying open-source large language models (LLMs) and code-focused NLP tools such as **[StarCoder](https://huggingface.co/bigcode/starcoder)**, **[CodeT5](https://huggingface.co/Salesforce/codet5-base)**, and **[CodeBERT](https://huggingface.co/microsoft/codebert-base)**. These models were shortlisted because they are trained extensively on code and natural-language discussions of code, especially with strong Python coverage. I considered each model’s training data scope, context length, availability of instruction-tuned variants, compute requirements, and benchmark performance (e.g., CodeXGLUE). This helps determine whether a model can not only generate code but also *understand* student submissions and produce formative prompts.

**How I would test/validate applicability**  
To validate applicability, I would compile a small dataset of real or simulated student Python submissions at different competence levels (novice → advanced). Each submission would be annotated with expert-identified misconceptions and a rubric of conceptual depth. Models would then be prompted to (1) analyze the code, (2) highlight reasoning gaps, and (3) generate 2–4 reflective questions without directly fixing the solution. Validation would use both **automatic metrics** (e.g., CodeBERTScore for semantic alignment, classification F1 for misconception detection) and **human evaluation** (instructors rating prompt usefulness, non-spoiler quality, and whether questions encourage deeper reasoning). This combined approach ensures both measurable consistency and real-world educational value.

---

##  Reasoning

**1. What makes a model suitable for high-level competence analysis?**  
- Strong *code understanding* (control flow, logic, intent).  
- Ability to generate *explainable diagnostics* and *formative prompts*.  
- Configurable to avoid direct solution leakage.  
- Practical to deploy (reasonable inference cost, licensing, and privacy compliance).  

**2. How would you test whether a model generates meaningful prompts?**  
- **Human evaluation:** Instructors judge prompt usefulness, depth, and whether it avoids spoilers.  
- **Student testing:** Observe if prompts improve revisions and explanations in follow-up submissions.  
- **Automatic proxies:** Measure semantic similarity to expert prompts using embeddings or CodeBERTScore.  

**3. What trade-offs might exist between accuracy, interpretability, and cost?**  
- *Accuracy vs cost:* Large LLMs (e.g., 15B+ parameters) are more accurate but expensive to run.  
- *Accuracy vs interpretability:* Large models may generate fluent but opaque reasoning, while smaller models (e.g., CodeT5) are more interpretable but less powerful.  
- *Interpretability vs usability:* Structured outputs improve clarity but reduce richness of feedback.  

**4. Why did you choose the model you evaluated? Strengths & limitations.**  
I chose **StarCoder** as the primary candidate because it is openly available, highly capable for Python, and trained on a large, diverse code corpus with an extended context window (helpful for multi-file projects).  
- *Strengths:* Strong code understanding, multi-language support, long context length, active Hugging Face ecosystem.  
- *Limitations:* Higher compute cost for large variants, potential hallucinations, and dataset provenance/licensing concerns.  
As lighter alternatives, **CodeT5** and **CodeBERT** can be used for quick code-understanding tasks or as evaluation metrics but may not produce as rich formative prompts out of the box.  

---

## References
- [StarCoder on Hugging Face](https://huggingface.co/bigcode/starcoder) – Open large language model for code.  
- [CodeT5 (Salesforce)](https://huggingface.co/Salesforce/codet5-base) – Encoder-decoder model for code understanding/generation.  
- [CodeBERT (Microsoft)](https://huggingface.co/microsoft/codebert-base) – Pretrained model for programming languages and natural language.  
- [CodeXGLUE Benchmark](https://github.com/microsoft/CodeXGLUE) – Standard benchmark suite for code intelligence tasks.  

---

