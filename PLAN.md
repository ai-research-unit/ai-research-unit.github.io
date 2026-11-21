
################################
### GENERAL RULES FOR THE PLANNER
################################

**CHECK THE PERSISTENT MEMORY FILE BEFORE EACH MESSAGE** /home/hp/.openhands/memory/MEMORY.md

**CHECK THE PLAN GENERAL RULES BEFORE EACH MESSAGE** /home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/PLAN.md

**DO NOT CREATE OR MODIFY ANY PERSISTENT MEMORY FILE OR ANY PLAN WITHOUT APPROBAL**

**DO NOT LAUNCH SUB AGENTS WITHOUT APPROVAL**

**DO NOT TOUCH THE DEPLOY FOLDER**

**Never touch git and version control.** No `commit`, `add`, `push`, `stash`,  `checkout`, `reset`, or `clean. This is the author's task.

Do not create AGENTS.md, the articles should be sable to defend themselves without it.


The author can instruct you to bypass some plan rules occasionally. His instructions are a priority compared to the plan rules.

READ THE CONVENTIONS

Verify by recomputation ON A MAXIMUM ON 100 elements. Every claim is recomputed on a maximum of 100 elements before it is edited or asserted.

Never sleep, never time out, never wait, never poll. No agent runs `sleep`, `watch`, `tail -f`, `timeout`, a background job it then waits on, a retry loop, or any command whose purpose is to let time pass or to bound how long it is allowed to take.

Do not let scratch files in the repository. Verification scripts and other throwaway files are written outside the repository (a temporary directory) or not at all, and are deleted before the pass ends whatever their location.

The path of the project is /home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/ 

The menus of the articles are maths.md for maths articles and physics.md for physics articles.

The folders containing the articles are articles_maths for maths articles and articles_physics for physics articles.

From time to time, update the article "Introduction to the Biquaternion Algebra Physical Interpretations" with the links toward the new maths articles that may have been written category of biquaternions.

From time to time, strip the proof-end marks :
grep -rnE '(\$\\square\$|\\\(\\square\\\)|\$\\blacksquare\$)[ \t]*$' articles_maths articles_physics | wc -l   # expect 0

################################
### RULES DURING THE CHATTING MODE
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

When chatting, use chat-math mode — write math as $…$ inline and $$…$$ for display, never in backticks, never bare, never \(…\).


When there is an issue, explain it clearly.

Avoid verbiage, jargon, over-engineering, complacency.

################################
### RULE ON GAUGE COUPLINGS (BINDING)
################################

One coupling, one place. Every gauge-coupling statement of the particle category lives in
`articles_physics/the-one-coupling-that-returns-the-standard-model.md`, which sits first in the
flagged section *The Standard Model as the Low-Energy Phase: The One Coupling That Returns It*.

A coupling statement is a **scale-bearing** statement: it cannot be written without naming a scale.
The five forms are a value, a boundary condition at a scale, a running or a one-loop slope, a matching
relation at a threshold, and a ratio called exact because two couplings are equal. Use the name
**scale-bearing coupling** for the class, and the test "can the sentence drop the scale?" as the
filter. Three categories follow: structural couplings (symbols, scale-free, stay everywhere);
scale-bearing couplings (flagged article only); measured couplings (external data, may stay where
used, marked as data).

Yukawa couplings and the scalar quartic obey the same rule. The one-bidoublet defect survives as a
counting statement (one matrix for two sectors, so proportional spectra); its values and its running
are in the flagged article, section 6.

DONE: the frame article is now "Four Colours, 21 Generators, One Declaration"; the menu entry, five
backlinks, the internal note and the Landau section heading ("The Near Miss at the Planck Scale") were
renamed with it.

DONE: the running article is now "Asymptotic Freedom and the Running of the Strong Force: One
Coefficient, One Line, One Scale", with section "The Strength at Every Scale" and a status block
declaring it a data article: it states no coupling of the model and its values are the measured
strong force. Twelve references renamed with it.

DONE: the six internal notes quoting the one-bidoublet equality carry a binding ledger banner: the
values in them are the literature's, the corpus's single coupling statement is the flagged article.
The internal coupling-sector note is retired to "A Retired Working Record", kept for its
recomputation history, and its own mass-relation sentence is now the counting form.

DONE: the sixteen menu comments that carried model coupling claims are rewritten. The word survives
in twenty-five comments where it names a structure (self-coupling, strong coupling as a regime,
anomalous coupling, Yukawa normalisations), which is not a scale-bearing value.

REMAINING, for a later session: the Standard Model data articles (deep inelastic scattering, jets,
R ratio, Landau pole and triviality, QCD rules, hadron structure, the nineteen parameters) still print
measured coupling values. They are data, not claims, and cutting them would gut the articles.
"The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism" keeps the word in its title
because minimal coupling is a covariant derivative and carries no scale.

DONE: the boundary is now a page, not prose. `articles_physics/the-data-boundary-which-articles-may-print-a-measured-strength.md`
is the third entry of the flagged section: three categories from one test, the claim register (2), the
data register (16), the structural count (107), five tests for a new article, four abuses the boundary
forbids. It carries no strength value of its own. Site baseline is now 3140 urls.

PATI–SALAM PURGE, DONE (visible corpus): the name is gone from `articles_physics` and `articles_maths`.
The model is no longer presented. What replaced it:
- the group symbol: `G_{PS}` -> `G_{4LR}`, 55 occurrences in 6 articles, and every prose mention of
  "the Pati–Salam scale" -> "the colour-breaking scale".
- the scale symbol: `M_{PS}` -> `M_{C}` where it meant the SU(4) breaking scale (3 articles), and
  `M_{PS}` -> `M_{U}` in the one-coupling article, where the equal-coupling threshold is a distinct
  scale ($M_U > M_C > M_R$ in the three-scale variant).
- the frame article: heading now "…and Where the Equal-Coupling Case Departs From It", with a
  opening paragraph that defines the departure as a scale-bearing coupling, states that it fails,
  and sends the equation and the number to the flagged article. The 1974 attribution sentence, the
  bibliography entry and the model's name are gone.
- the one-coupling article: "Pati–Salam is the case g_4=g_L=g_R" -> "The equal-coupling case is …".
- the breaking chain: the coupling boundary-condition sentence removed and referred to the flagged
  article.
- stale link title in why-su-2 fixed (it still said "…One Coupling").
- algebro: a reference to a menu section that no longer exists ("Electromagnetism in Pati–Salam
  Model") replaced.
KEPT ON PURPOSE: the citation "A. K. Pati and S. L. Braunstein, Impossibility of deleting an unknown
quantum state" in no-cloning — a different physicist, quantum information, nothing to do with the
model. PROVENANCE: the Pati & Salam 1974 citation survives in two internal notes
(`the-pati-salam-model`, `Indistinguishable-theories-standard-model`) and in the coupling-sector
note, which is where the coupling is now discussed. OUT OF SCOPE: `articles_external/Pati-Salam/`
(source papers, not in any menu).

ELECTROWEAK CONFIRMATION: the sector needs no scale-bearing coupling to represent electromagnetism and
the weak interaction. Seven articles, five with no measured value at all. Structural and scale-free:
the group and the anomaly conditions; Q=T_3+Y/2; the covariant derivative; e=g sin(theta_W) as a
DEFINITION of the angle; m_W/m_Z=cos(theta_W); rho=1 from custodial symmetry; the photon as the null
vector of the neutral mass matrix. Scale-bearing only where data is confronted: v, G_F, the pole masses,
the measured angle. Two of the seven print those, and both do so to compare two routes.

Everything else in the category carries couplings as symbols only, with no value attached, and
links to the flagged article instead of repeating the number. The one exception is the Weinberg
angle article, which sits in the same flagged section.

Never reintroduce a coupling number into an article outside that section, and never split a
coupling claim across two articles. If a new number is needed, it goes into the flagged article,
with its inputs and its status.



################################
### RULES DURING THE QUESTION MODE
################################

The agent reads carefully the convention articles.

He focuses on the questions asked. 

He reads possible related articles of the corpus.

He does not waste time doing other things, checking unrelated things.

The agent answers the question in plain declarative prose.

Sentences are short, active, one idea per paragraph.

Vocabulary is plain and consistent. No verbiage, No filler, no flourish. NO VERBIAGE.


################################
### RULES DURING THE ANALYSIS MODE
################################

The agent reads carefully the convention articles.

He analyses the subject. 

He reads possible related articles of the corpus.

The agent does not waste time doing other things, checking unrelated things.

The agent renders its analysis in plain declarative prose.

Sentences are short, active, one idea per paragraph.

Vocabulary is plain and consistent. No verbiage, No filler, no flourish. NO VERBIAGE.


################################
### RULES DURING THE ENRICHMENT MODE
################################

The agent reads carefully the convention articles.

He reads the paper provided.

He reads possible related articles of the corpus.

He evaluates the potential enrichment the paper could bring to the corpus, especially the new interesting ideas. 

The agent does not waste time doing other things, checking unrelated things.

The agent renders the potential new ideas the paper could brig in plain declarative prose.

Sentences are short, active, one idea per paragraph.

Vocabulary is plain and consistent. No verbiage, No filler, no flourish. NO VERBIAGE.


################################
### RULES DURING THE WRITING MODE
################################

The agent reads carefully the convention articles.

The agent reads the subject of the article to write.

Concerning the choice of titles: the title names the object and the result.

Write it before the article, not after.

A physicist who reads only the title should know what is studied. If not, rewrite it.


He searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

If needed, the agent then gathers interesting complementary information from the internet.

Then the agent writes the article .md file. Here are editorial preferences :

 - every article starts with the title line `# __Title__`, then `## Introduction`, then thematic `##` sections, closing with `## Summary`, `## Summary of Notation`, `## Further Reading`.

 - give every intersection a ### heading, define before tabulating.

 - tables are Markdown, never LaTeX array.

  - LaTeX: never write q'_0^2 (prime is the superscript); never let $...$ span a line break; indent display math four spaces in a list; errors are silent (red #c00, not reported); \dddot and \slashed are template macros; |{}<> inside $...$ need no escaping.

  - prefer "physical interpretation" to "physical reading"

Plain declarative prose that argues one claim from the start.

Sentences are short, active, one idea per paragraph.

It argues by contrast, and it names the strongest objection before answering it.

Every claim carries a warrant: a proof, a check, or a stated reading of the conventions.

Vocabulary is plain and consistent. No filler, no flourish. NO VERBIAGE.

The agent does not waste time doing other things, checking unrelated things.


Under this mode, the agent modifies the article, and the menu if necessary.

In case the agent spots an obious mistake in another related article, he can also patch it, and he reports about the change implemented.

This requires judgment and organization.


################################
### RULES DURING THE REVIEW MODE
################################

The agent reads carefully the convention articles.

The agent reads the article to review.

He searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

For example, for a physics article, among the articles to read, they are always 3 foundational articles, Introduction to the Biquaternion Universe, The Anti-Hermitian Subspace M- as the Material Sector, The Hermitian Subspace M+ as the Informational Sector. Note: the two named foundation articles were merged into *The Algebraic Vocabulary: Element, Conjugations, Six Subspaces and Two Ledgers* and *The Two Sectors: The Hermitian Split and the Four Bridges*; the shelf is those two plus the three carrier introductions, and the two old titles are superseded, not missing.

If needed, the agent then gathers interesting complementary information from the internet.

Then the agent reviews the article .md file. He searches for errors, notational inconsistencies and incoherences and he corrects them.

The agent respects the format of the article.

Plain declarative prose that argues one claim from the start.

Sentences are short, active, one idea per paragraph.

It argues by contrast, and it names the strongest objection before answering it.

Every claim carries a warrant: a proof, a check, or a stated reading of the conventions.

Vocabulary is plain and consistent. No filler, no flourish. NO VERBIAGE.

The agent does not waste time doing other things, checking unrelated things.

Under this mode, the agent modifies the article, and the menu if necessary.

In case the agent spots an obious mistake in another related article, he can also patch it, and he reports about the change implemented.

This requires rigor, carefulness, and suspicion to check assertions.



################################
### RULES DURING THE RESEARCH MODE
################################

The agent reads carefully the convention articles.

The agent reads the article.

He searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

For example, for a physics article, among the articles to read, they are always 3 foundational articles, Introduction to the Biquaternion Universe, The Anti-Hermitian Subspace M- as the Material Sector, The Hermitian Subspace M+ as the Informational Sector. Note: the two named foundation articles were merged into *The Algebraic Vocabulary: Element, Conjugations, Six Subspaces and Two Ledgers* and *The Two Sectors: The Hermitian Split and the Four Bridges*; the shelf is those two plus the three carrier introductions, and the two old titles are superseded, not missing.

The agent does not waste time doing other things, checking unrelated things.

The agent report in chat the open questions, the suggestions, the speculations contained or suggested in the article that have not been implemented so far (nothing is excluded for being unproven).

In case the agent spots an obious mistake in an article, he can also patch it, and he reports about the change implemented.

This requires judgment and creativity.




################################
### RULES DURING THE INNOVATION MODE
################################

The agent reads carefully the convention articles.

The agent searches in the menus (maths.md for maths articles and physics.md for physics articles), the interesting related articles to provide him some context and notational conventions.

For example, for a physics article, among the articles to read, they are always 3 foundational articles, Introduction to the Biquaternion Universe, The Anti-Hermitian Subspace M- as the Material Sector, The Hermitian Subspace M+ as the Informational Sector. Note: the two named foundation articles were merged into *The Algebraic Vocabulary: Element, Conjugations, Six Subspaces and Two Ledgers* and *The Two Sectors: The Hermitian Split and the Four Bridges*; the shelf is those two plus the three carrier introductions, and the two old titles are superseded, not missing.

The agent suggests some modifications about the article.

If modifications are approved by the author, he writes them.

The agent respects the format of the article.

The agent does not waste time doing other things, checking unrelated things.

Under this mode, the agent modifies the article.

In case the agent spots an obious mistake in an article, he can also patch it, and he reports about the change implemented.

This requires judgement and organization.




################################
### RULES WHEN MANAGING SUB AGENTS 
################################

**DO NOT LAUNCH SUB AGENTS WITHOUT APPROVAL**

When there are a lot of similar complex tasks to do, for example reviewing 50 articles, we may use specialized agents.

Usually you will prepare the instruction, containing the general rules and the rules applicable to the specific task.

Make sure the sub agents read the introduction and conventions (maths or physics depending the subject), and perhaps a few related articles to understand the template.

After that the author will launch the sub agents, because the setup seems to limit some memory capacities when sub agents are launched automatically by an agent. In any case, 15 sub agents is the maximum the setup can do.
