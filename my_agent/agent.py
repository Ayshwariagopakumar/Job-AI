# interview_prep_agent.py

from google.adk.agents.llm_agent import Agent
from google.adk.agents import SequentialAgent

GEMINI_MODEL = "gemini-2.5-flash-lite"

# --- 1. Open Job Positions Agent ---
open_positions_agent = Agent(
    model=GEMINI_MODEL,
    name="OpenPositionsAgent",
    description="Finds 5 open job positions based on user query.",
    instruction="""
You are a Job search assistant. Based on the user query, do your research on web and
list 5 open job positions.

For each position include:
- Job Title
- Company
- Location

Output as a numbered list.
""",
    output_key="open_positions",
)

# --- 2. Interview Q&A Agent ---
interview_qa_agent = Agent(
    model=GEMINI_MODEL,
    name="InterviewQAAgent",
    description="Creates interview Q&A based on open job positions.",
    instruction="""
You are an interview coach. For the given query and referring to {open_positions},
create 5 common interview questions with strong sample answers.

Format:
Q: <question>
A: <answer>
""",
    output_key="interview_qa",
)

# --- 3. Interview Tips Agent ---
interview_tips_agent = Agent(
    model=GEMINI_MODEL,
    name="InterviewTipsAgent",
    description="Provides interview preparation advice tailored to the job roles.",
    instruction="""
You are a career mentor. Provide practical tips & tricks (~200 words) to excel in interviews
for the given user query. Use {open_positions} to tailor your advice, and refer to {interview_qa}.

Cover:
- How to research the company
- What to prepare technically
- Behavioral interview strategies
- Body language & communication tips

Output as a bulleted list.
""",
    output_key="interview_tips",
)

# --- Combine them into a Sequential Agent ---
root_agent = SequentialAgent(
    name="InterviewPrepPipeline",
    description="Suggests open jobs, interview Q&A, and tailored interview preparation tips.",
    sub_agents=[open_positions_agent, interview_qa_agent, interview_tips_agent],
)
