
################################
### GENERAL RULES FOR THE PLANNER
################################

**CHECK THE PERSISTENT MEMORY FILE BEFORE EACH MESSAGE** /home/hp/.openhands/memory/MEMORY.md

**CHECK THE PLAN GENERAL RULES BEFORE EACH MESSAGE*** /home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/PLAN.md

**DO NOT CREATE OR MODIFY ANY PERSISTENT MEMORY FILE OR ANY PLAN WITHOUT APPROBAL**

**DO NOT LAUNCH SUB AGENTS WITHOUT APPROVAL**

**DO NOT TOUCH THE DEPLOY FOLDER**

**Never touch version control or the build.** No `commit`, `add`, `push`, `stash`,  `checkout`, `reset`, or `clean`; do not run `build.py`. This is the author's task.

Do not create AGENTS.md, the articles should be sable to defend themselves without it.


The author can instruct you to bypass some plan rules occasionally. His instructions are a priority compared to the plan rules.


Verify by recomputation ON A MAXIMUM ON 100 elements. Every claim is recomputed on a maximum of 100 elements before it is edited or asserted.

Never sleep, never time out, never wait, never poll. No agent runs `sleep`, `watch`, `tail -f`, `timeout`, a background job it then waits on, a retry loop, or any command whose purpose is to let time pass or to bound how long it is allowed to take.

Do not let scratch files in the repository. Verification scripts and other throwaway files are written outside the repository (a temporary directory) or not at all, and are deleted before the pass ends whatever their location.

The path of the project is /home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/ 

The menus of the articles are maths.md for maths articles and physics.md for physics articles.

The folders containing the articles are articles_maths for maths articles and articles_physics for physics articles.

################################
### RULES DURING THE CHATTING PHASE
################################


Use plain words.
Use plain words.
Use plain words.
Use plain words.
Use plain words.
Use plain words.
Use plain words.
Use plain words.
Use plain words.

When a simple question is asked, make a simple response using a clear language, if possible under 200 words.

When there is an issue, explain it clearly.

Avoid verbiage, jargon, over-engineering, complacency.


################################
### RULES DURING THE WRITING PHASE
################################

The agent reads the subject of the article to write.

He searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

For example, for a physics article, among the articles to read, they are always 4 foundational articles, Introduction to the Biquaternion Universe, The Anti-Hermitian Subspace M- as the Material Sector, The Hermitian Subspace M+ as the Informational Sector, Conventions in the Biquaternion Universe.

If needed, the agent then gathers interesting complementary information from the internet.

Then the agent writes the article .md file. Here are editorial preferences :

 - every article starts with the title line `# __Title__`, then `## Introduction`, then thematic `##` sections, closing with `## Summary`, `## Summary of Notation`, `## Further Reading`.

 - give every intersection a real ### heading, define before tabulating.

 - tables are Markdown, never LaTeX array.

  - LaTeX: never write q'_0^2 (prime is the superscript); never let $...$ span a line break; indent display math four spaces in a list; errors are silent (red #c00, not reported); \dddot and \slashed are template macros; |{}<> inside $...$ need no escaping.



He appends his ideas, suggestions, interesting observations, decisions and reasons, speculations, verified facts, ownership/boundary rules, standing weaknesses to the companion file .context, created next to the article .md file.

During this phase, the agent modifies the article, its companion file .context, and the menu if necessary.

In case the agent spots an obious mistake in another related article, he can also patch it, patch its .context file if necessary, and he reports about the change implemented.

This requires judgment and organization.


################################
### RULES DURING THE REVIEWING PHASE
################################


The agent reads the article to review.

He searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

For example, for a physics article, among the articles to read, they are always 3 foundational articles, Introduction to the Biquaternion Universe, The Anti-Hermitian Subspace M- as the Material Sector, The Hermitian Subspace M+ as the Informational Sector.

If needed, the agent then gathers interesting complementary information from the internet.

Then the agent reviews the article .md file. He searches for errors, notational inconsistencies and incoherences and he corrects them. 

The agent respects the format of the article.

He appends his ideas, suggestions, interesting observations, decisions and reasons, speculations, verified facts, ownership/boundary rules, standing weaknesses to the companion file .context, created next to the article .md file.


During this phase, the agent modifies the article, its companion file .context, and the menu if necessary.

In case the agent spots an obious mistake in another related article, he can also patch it, patch its .context file if necessary, and he reports about the change implemented.

This requires rigor, carefulness, and suspicion to check assertions.



################################
### RULES DURING THE RESEARCH PHASE
################################


The agent reads the article, the companion .context file.

He searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

For example, for a physics article, among the articles to read, they are always 3 foundational articles, Introduction to the Biquaternion Universe, The Anti-Hermitian Subspace M- as the Material Sector, The Hermitian Subspace M+ as the Informational Sector.


The agent creates or modifies the companion file .ideas and writes inside it the open questions, the suggestions, the speculations contained or suggested in the article and its companion .context file that have not been implemented so far (nothing is excluded for being unproven).

During this phase, the agent can modify the companion file .ideas of the article.

In case the agent spots an obious mistake in an article, he can also patch it, patch its .context file if necessary, and he reports about the change implemented.

For example, the article fields.md would be along fields.ideas.


This requires judgment and creativity.




################################
### RULES DURING THE INNOVATION PHASE
################################


The agent reads the article, the companion .ideas file.

He searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

For example, for a physics article, among the articles to read, they are always 3 foundational articles, Introduction to the Biquaternion Universe, The Anti-Hermitian Subspace M- as the Material Sector, The Hermitian Subspace M+ as the Informational Sector.

The agent suggests some modifications about the article, based on the ideas contained in the .ideas file.

If modifications are approved by the author, he writes them.

The agent respects the format of the article.

He appends his ideas, suggestions, interesting observations, decisions and reasons, speculations, verified facts, ownership/boundary rules, standing weaknesses to the companion file .context, created next to the article .md file.

Once the changes are implemented in the article, he removes the implemented ideas from the .ideas file.

During this phase, the agent modifies the article and the companion files .context and .ideas of the article.

In case the agent spots an obious mistake in an article, he can also patch it, patch its .context file if necessary, and he reports about the change implemented.

This requires judgement and organization.



################################
### RULES DURING THE CLEANING PHASE
################################


The agent reads the companion .context file, and he removes the verbiage, the uninteresting things, the past checks, ... he only keep the interesting points and lets a lean file.

During this phase, the agent does not touch any other file than the  companion file .context of the article.


This requires judgment and focus.



################################
### RULES WHEN MANAGING SUB AGENTS 
################################

**DO NOT LAUNCH SUB AGENTS WITHOUT APPROVAL**

When there are a lot of similar complex tasks to do, for example reviewing 50 articles, we may use specialized agents.

Usually you will prepare the instruction, containing the general rules and the rules applicable to the specific task.

After that the author will launch the sub agents, because the setup seems to limit some memory capacities when sub agents are launched automatically by an agent. In any case, 15 sub agents is the maximum the setup can do.
