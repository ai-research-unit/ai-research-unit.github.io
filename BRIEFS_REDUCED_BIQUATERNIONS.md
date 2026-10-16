# __Briefs — the Reduced Biquaternions Category__

Eleven hand-off briefs, one per agent. **Nothing is launched by this file.** Each brief is self-contained and is meant to be pasted as the first message of a child conversation.

## 0. The object, the code and the rules (common to every brief)

**The object.** The reduced biquaternion space is the commutative algebra

$$\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C},$$

with basis $1, i, j, ij$, the relations $i^{2} = -1$, $j^{2} = +1$, $ji = ij$, and the two idempotents $\Pi_{1,2} = \tfrac12(1\pm j)$. An element is $T = A + Bj$ with $A = a + ia'$ and $B = b + ib'$ complex, and the idempotent decomposition is $T = (A+B)\Pi_1 + (A-B)\Pi_2$. It is the engineering **reduced biquaternion** algebra, equivalently the **tessarines**, the **double-complex** numbers or the **commutative hypercomplex** algebra. The glyph $\mathbb{B}_{\mathrm{r}}$ and the element $T = A+Bj$ are fixed in *Conventions in Mathematics*, §*The Elements and their Coefficients*; the engineering sources write $z = z_{1} + z_{2}e$, and the corpus does not.

**The involutions.** The **bar** conjugates the coefficients, $\overline{A+Bj} = \bar A + \bar B j$; the **natural sign** ${}^{\natural}$ negates the second slot, $(A+Bj)^{\natural} = A - Bj$; the **star** is their composite, ${}^{*} = \bar{\cdot}\circ{}^{\natural}$, and the **flat** is ${}^{\flat} = -{}^{*}$.

**The four general products** (verify these; they are the corpus's construction applied to the space):

$$\mathrm{GPA} = T W,\qquad \mathrm{GQA} = T^{\natural}W,\qquad \mathrm{GPS} = TW^{*},\qquad \mathrm{GQS} = T^{\natural}W^{*}.$$

On $T = A+Bj$, $W = C+Dj$:

| code | value | scalar part | $j$-part |
|---|---|---|---|
| $\mathrm{GPA}$ | $TW$ | $AC+BD$ | $AD+BC$ |
| $\mathrm{GQA}$ | $T^{\natural}W$ | $AC-BD$ | $AD-BC$ |
| $\mathrm{GPS}$ | $TW^{*}$ | $A\bar C - B\bar D$ | $B\bar C - A\bar D$ |
| $\mathrm{GQS}$ | $T^{\natural}W^{*}$ | $A\bar C + B\bar D$ | $-(A\bar D + B\bar C)$ |

**The twelve slots and the four that die.** Each general product splits into a symmetric and an antisymmetric part by the two exchanges — the bare interchange for the two $\mathbb{C}$-bilinear products, the interchange followed by the coefficientwise conjugation of the value for the two sesquilinear ones (*The Symmetric and Antisymmetric Parts of an Algebra Product*, *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). Because the algebra is **commutative** four of the twelve slots are not new operations:

$$\mathrm{SPA} = \mathrm{GPA},\qquad \mathrm{APA} = 0,\qquad \mathrm{SQS} = \mathrm{GQS},\qquad \mathrm{AQS} = 0.$$

The space therefore carries **eight distinct algebraic structures**: $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and the four live halves $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$. The code is the corpus's (*Conventions in the Biquaternion Universe*, §*The Twelve Products and Their Names*): $\mathrm G/\mathrm S/\mathrm A$ the general product and its two parts, $\mathrm P/\mathrm Q$ the plain and the quaternionic first slot, $\mathrm A/\mathrm S$ the algebra over $\mathbb{C}$ and the sesqualgebra over $(\mathbb{C},\bar{\cdot})$.

**The eight, in words.** $\mathrm{GPA}$ is the multiplication. $\mathrm{GQA}$ is $\mathrm{GPA}$ with the first factor read through ${}^{\natural}$. $\mathrm{GPS}$ and $\mathrm{GQS}$ are the sesquilinear pair. $\mathrm{SQA}$ and $\mathrm{AQA}$ are the two halves of $\mathrm{GQA}$; $\mathrm{SPS}$ and $\mathrm{APS}$ the two halves of $\mathrm{GPS}$. The four live halves are: $\mathrm{SQA}(T,W) = A C - B D$ (central), $\mathrm{AQA}(T,W) = (AD-BC)\,j$ (in $\mathbb{C}j$), $\mathrm{SPS}(T,W) = A\bar C - B\bar D$ (central), $\mathrm{APS}(T,W) = (B\bar C - A\bar D)\,j$ (in $\mathbb{C}j$).

**Hard rules (from `PLAN.md`, not negotiable).**

1. Read `/home/hp/.openhands/memory/MEMORY.md` and `PLAN.md` first.
2. Read *Conventions in Mathematics* and *Conventions in the Biquaternion Universe* before writing.
3. Every article: title line `# __Title__`, then `## Introduction`, thematic `##` sections, then `## Summary`, `## Summary of Notation`, `## Further Reading`.
4. Write the `.md`. When the article is written, **drop the leading `+`** from its entry in `maths.md` (the `+` marks a planned article).
5. Cite, do not restate: a concept is introduced once, in the article that owns it. Every deferral is stated explicitly.
6. **Verify by recomputation on at most 100 elements** before asserting anything. Scripts are written **outside** the repository and deleted afterwards.
7. **Never touch version control or the build** (no `git`, no `build.py`).
8. **Do not launch sub-agents.**
9. Chat in the plain-words style; chat-math in `$…$` / `$$…$$`.

**The reading list every agent shares** (in the corpus's own articles): *Conventions in Mathematics*; *Conventions in the Biquaternion Universe*; *Biquaternions as a Vector Space over $\mathbb{C}$*; *Remarkable Subspaces* (introduction, decompositions, comparison); *The Four General Products of the Biquaternion $\mathbb{C}$ Space*; *Relations Between the Four General Products*; *Comparison Between the Four General Products*; *The 12 Products of the Biquaternion Complex Space*; *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; *Definitions for the Study of the Algebraic Structures*; *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*; *The Symmetric and Antisymmetric Parts of an Algebra Product*; *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; *List of Algebras by Dimension*; *The Eight Algebras Compared*; *Harmonic Analysis over Hypercomplex Systems*; and, as the article-for-article template, the counterpart Quaternion and Biquaternion articles named inside each brief.

**The template, one line.** A general structure is 13 articles in the order: Commons 7 (introduction; norm and invertibility; zero divisors; annihilators; roots of $1$ and idempotents; roots of $0$ and nilpotents; roots of a general element) — Specific Theory 3 (specificities; ideals and Peirce decomposition; group of units) — Form 1 — Operators 1 — Representations 1. A live half is 11: Commons 7 (same seven) — specificities — algebraic norm — multiplication operators — $2\times2$ representation. Each block also carries the corpus's `###### Common Theory` / `###### Specific Theory` / `###### Form` / `###### Operators` / `###### Representations` sub-headings from the Biquaternion menu.

---

## Brief 1 — Agent 1 — the shared Algebra of the space (19 articles)

**Deliverable: 19 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `reduced-biquaternion-space`  —  Reduced Biquaternion Space
  - `reduced-biquaternions-as-a-vector-space-over-r-and-c`  —  Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$
  - `the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions`  —  The Two Involutions and the Group of Involutions
  - `introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions`  —  Introduction to the Remarkable Subspaces
  - `decompositions-along-the-remarkable-subspaces-of-the-reduced-biquaternions`  —  Decompositions Along the Remarkable Subspaces
  - `comparison-of-the-remarkable-subspaces-of-the-reduced-biquaternions`  —  Comparison of the Remarkable Subspaces
  - `introduction-to-reduced-biquaternion-element-representations`  —  Introduction to Reduced Biquaternion Element Representations
  - `the-four-vector-element-representation-of-the-reduced-biquaternions`  —  The Four-Vector Element Representation of the Reduced Biquaternions
  - `introduction-to-the-2x2-matrix-element-representation-of-reduced-biquaternions`  —  Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions
  - `reduced-biquaternion-other-algebraic-element-representations`  —  Reduced Biquaternion Other Algebraic Element Representations
  - `the-four-general-products-of-the-reduced-biquaternion-c-space`  —  The Four General Products of the Reduced Biquaternion $\mathbb{C}$ Space
  - `relations-between-the-four-general-products-of-the-reduced-biquaternions`  —  Relations Between the Four General Products
  - `comparison-between-the-four-general-products-of-the-reduced-biquaternions`  —  Comparison Between the Four General Products
  - `the-four-general-products-and-operators-of-the-reduced-biquaternions`  —  The Four General Products and Operators
  - `remarkable-subspaces-and-the-four-general-products-of-the-reduced-biquaternions`  —  Remarkable Subspaces and the Four General Products
  - `the-12-products-of-the-reduced-biquaternion-complex-space`  —  The 12 Products of the Reduced Biquaternion Complex Space
  - `the-algebraic-structures-over-the-reduced-biquaternion-c-space`  —  The Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space
  - `definitions-for-the-study-of-the-algebraic-structures-of-the-reduced-biquaternions`  —  Definitions for the Study of the Algebraic Structures
  - `the-4-forms-over-the-reduced-biquaternion-c-space`  —  The 4 Forms over the Reduced Biquaternion $\mathbb{C}$ Space

### What this agent does

Writes the shared Algebra the whole category stands on: the **space**, its **involutions**, its **remarkable subspaces**, its **element representations**, and the **introduction to the algebraic structures** that fixes the four general products, the twelve slots and the eight structures.

### What each article must contain

- **Reduced Biquaternion Space** — the algebra $T = A+Bj$, the relations, the two idempotents, the isomorphism $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, the historical names (tessarines, double-complex, Cockle), the comparison with $\mathbb{H}_{\mathbb{D}}$.
- **as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$** — dimension $4$ over $\mathbb{R}$ and $2$ over $\mathbb{C}$, the realification, the effect of the change of scalars.
- **The Two Involutions and the Group of Involutions** — bar and natural sign, their fixed and anti-fixed spaces, the Klein group $\{\mathrm{id},\bar{\cdot},{}^{\natural},{}^{*}\}$, following *The Group of Involutions* of the biquaternion category.
- **Remarkable Subspaces** — centre $\mathbb{C}_{\mathbb{B}_{\mathrm{r}}}$, the $j$-line $\mathbb{C}j$, the fixed and anti-fixed spaces of each involution, and the idempotent lines $\mathbb{C}\Pi_{1,2}$.
- **Standard Element Representations** — the four-vector (real quadruple; complex pair) and the $2\times2$ matrix model; the second one must show $\mathbb{B}_{\mathrm{r}}\cong$ the diagonal $2\times2$ complex matrices.
- **The 4 General Products, Relations, Comparison** — the four coordinate displays above, the identities that link them, the property table; the drop of the cross terms relative to $\mathbb{B}$.
- **The Four General Products and Operators / Remarkable Subspaces and the Four General Products** — the operators the products generate and their behaviour on the subspaces.
- **The 12 Products of the Reduced Biquaternion Complex Space** — the twelve slots, the four dead ones with their proof ($\mathrm{SPA}=\mathrm{GPA}$, $\mathrm{APA}=0$, $\mathrm{SQS}=\mathrm{GQS}$, $\mathrm{AQS}=0$), mirroring *The 12 Products of the Biquaternion Complex Space*.
- **The Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space** — the eight structures named with their laws and classical identities; **Definitions for the Study of the Algebraic Structures** — the vocabulary; **The 4 Forms** — $B$, $N$, $H$, $K$ and the four algebraic norms.

### Readings specific to this brief

The biquaternion counterparts *Biquaternions as a Vector Space over $\mathbb{R}$* / *over $\mathbb{C}$*, *The Group of Involutions*, *Introduction to the Remarkable Subspaces* and its two companions, *Introduction to Biquaternion Element Representations*, *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *Relations Between the Four General Products*, *Comparison Between the Four General Products*, *The 12 Products of the Biquaternion Complex Space*, *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Definitions for the Study of the Algebraic Structures*, *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. Sources: Pei–Chang–Ding (2004); Cockle (1849); *List of Algebras by Dimension*; *Harmonic Analysis over Hypercomplex Systems*, §*The Commutative Alternative*.

### Acceptance

The four general products and the eight structures agree with the tables above; the four collapse identities are proven, not asserted; the $2\times2$ model carries the zero divisors explicitly; the menu entries lose their `+`.
---

## Brief 2 — Agent 2 — General Plain Algebra (GPA), 13 articles

**Deliverable: 13 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Introduction to the General Plain Algebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions
  - `zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Zero Divisors of the General Plain Algebra of the Reduced Biquaternions
  - `annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Annihilators of the General Plain Algebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the General Plain Algebra of the Reduced Biquaternions
  - `the-specificities-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  The Specificities of the General Plain Algebra of the Reduced Biquaternions
  - `ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions
  - `the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  The Group of Units of the General Plain Algebra of the Reduced Biquaternions
  - `the-forms-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  The Forms of the General Plain Algebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions
  - `the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the complete structure of the **General Plain Algebra** over $\mathbb{B}_{\mathrm{r}}$, following article for article the counterpart block *General Plain Algebra of the Biquaternions over $\mathbb{C}$* and the quaternion block of the same name. The operation here is the multiplication $TW$ (associative, commutative, unital).

### Structure-specific content

- **Norm and invertibility** — the algebraic norm of the operation and its invertibility criterion. $\mathrm{GPA}$: $N(T) = A^{2}-B^{2}$ (complex, multiplicative, vanishing on the two idempotents, so every element of the null cone is a zero divisor). $\mathrm{GQA}$: $N(T)=A^{2}+B^{2}$. $\mathrm{GPS}$: $H(T)=|A|^{2}-|B|^{2}$ (real). $\mathrm{GQS}$: $K(T)=|A|^{2}+|B|^{2}$ (real, positive definite).
- **Zero divisors** — the null cone of the above norm; $\mathrm{GPA}$ and $\mathrm{GPS}$ have zero divisors and $\mathrm{GQS}$ has none; the idempotents $\Pi_{1,2}$ are zero divisors of $\mathrm{GPA}$ (and each is a unit of $\mathrm{GPS}$).
- **Annihilators**; **roots of $1$ and the idempotents** (the $\Pi_{1,2}$ and the central $\pm1$, beside the further roots of the operation); **roots of $0$ and the nilpotents**; **roots of a general element**.
- **Specificities**; **ideals and Peirce decomposition** (the idempotent decomposition $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2$ is the central one, and it is an algebra decomposition exactly for $\mathrm{GPA}$); **group of units** — for $\mathrm{GPA}$ it is the complement of the null cone, $A^{2}\neq B^{2}$.
- **Form**; **multiplication operators and the bi-module structure**; **the $2\times2$ matrix element representation**.

### Readings specific to this brief

The counterpart *General Plain Algebra of the Biquaternions over $\mathbb{C}$* (and the *Quaternions over $\mathbb{R}$* block of the same code, where it exists), plus *The 12 Products of the Reduced Biquaternion Complex Space* and *The Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space* for the fixed conventions.

### Acceptance

Every algebraic claim recomputed on at most 100 elements; the norm, the zero-divisor set and the unit criterion proven; the block's 13 `.md` written; the menu entries lose their `+`. For $\mathrm{GPA}$ only, note explicitly that it is the associative case and that the central idempotents split the algebra.
---

## Brief 3 — Agent 3 — General Quaternionic Algebra (GQA), 13 articles

**Deliverable: 13 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Introduction to the General Quaternionic Algebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the General Quaternionic Algebra of the Reduced Biquaternions
  - `zero-divisors-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Zero Divisors of the General Quaternionic Algebra of the Reduced Biquaternions
  - `annihilators-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Annihilators of the General Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the General Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the General Quaternionic Algebra of the Reduced Biquaternions
  - `the-specificities-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Specificities of the General Quaternionic Algebra of the Reduced Biquaternions
  - `ideals-and-peirce-decomposition-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  Ideals and Peirce Decomposition of the General Quaternionic Algebra of the Reduced Biquaternions
  - `the-group-of-units-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Group of Units of the General Quaternionic Algebra of the Reduced Biquaternions
  - `the-forms-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Forms of the General Quaternionic Algebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-general-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the General Quaternionic Algebra of the Reduced Biquaternions
  - `the-general-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the complete structure of the **General Quaternionic Algebra** over $\mathbb{B}_{\mathrm{r}}$, following article for article the counterpart block *General Quaternionic Algebra of the Biquaternions over $\mathbb{C}$* and the quaternion block of the same name. The operation here is the multiplication $T^{\natural}W$ (not associative, commutative after the conjugation).

### Structure-specific content

- **Norm and invertibility** — the algebraic norm of the operation and its invertibility criterion. $\mathrm{GPA}$: $N(T) = A^{2}-B^{2}$ (complex, multiplicative, vanishing on the two idempotents, so every element of the null cone is a zero divisor). $\mathrm{GQA}$: $N(T)=A^{2}+B^{2}$. $\mathrm{GPS}$: $H(T)=|A|^{2}-|B|^{2}$ (real). $\mathrm{GQS}$: $K(T)=|A|^{2}+|B|^{2}$ (real, positive definite).
- **Zero divisors** — the null cone of the above norm; $\mathrm{GPA}$ and $\mathrm{GPS}$ have zero divisors and $\mathrm{GQS}$ has none; the idempotents $\Pi_{1,2}$ are zero divisors of $\mathrm{GPA}$ (and each is a unit of $\mathrm{GPS}$).
- **Annihilators**; **roots of $1$ and the idempotents** (the $\Pi_{1,2}$ and the central $\pm1$, beside the further roots of the operation); **roots of $0$ and the nilpotents**; **roots of a general element**.
- **Specificities**; **ideals and Peirce decomposition** (the idempotent decomposition $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2$ is the central one, and it is an algebra decomposition exactly for $\mathrm{GPA}$); **group of units** — for $\mathrm{GPA}$ it is the complement of the null cone, $A^{2}\neq B^{2}$.
- **Form**; **multiplication operators and the bi-module structure**; **the $2\times2$ matrix element representation**.

### Readings specific to this brief

The counterpart *General Quaternionic Algebra of the Biquaternions over $\mathbb{C}$* (and the *Quaternions over $\mathbb{R}$* block of the same code, where it exists), plus *The 12 Products of the Reduced Biquaternion Complex Space* and *The Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space* for the fixed conventions.

### Acceptance

Every algebraic claim recomputed on at most 100 elements; the norm, the zero-divisor set and the unit criterion proven; the block's 13 `.md` written; the menu entries lose their `+`. For $\mathrm{GPA}$ only, note explicitly that it is the associative case and that the central idempotents split the algebra.
---

## Brief 4 — Agent 4 — General Plain Sesqualgebra (GPS), 13 articles

**Deliverable: 13 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Introduction to the General Plain Sesqualgebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the General Plain Sesqualgebra of the Reduced Biquaternions
  - `zero-divisors-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Zero Divisors of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `annihilators-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Annihilators of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the General Plain Sesqualgebra of the Reduced Biquaternions
  - `the-specificities-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Specificities of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `ideals-and-peirce-decomposition-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Ideals and Peirce Decomposition of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `the-group-of-units-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Group of Units of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `the-forms-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Forms of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-general-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the General Plain Sesqualgebra of the Reduced Biquaternions
  - `the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the complete structure of the **General Plain Sesqualgebra** over $\mathbb{B}_{\mathrm{r}}$, following article for article the counterpart block *General Plain Sesqualgebra of the Biquaternions over $\mathbb{C}$* and the quaternion block of the same name. The operation here is the sesquilinear product $TW^{*}$ (not associative, sesquilinear over $(\mathbb{C},\bar{\cdot})$, right unit only).

### Structure-specific content

- **Norm and invertibility** — the algebraic norm of the operation and its invertibility criterion. $\mathrm{GPA}$: $N(T) = A^{2}-B^{2}$ (complex, multiplicative, vanishing on the two idempotents, so every element of the null cone is a zero divisor). $\mathrm{GQA}$: $N(T)=A^{2}+B^{2}$. $\mathrm{GPS}$: $H(T)=|A|^{2}-|B|^{2}$ (real). $\mathrm{GQS}$: $K(T)=|A|^{2}+|B|^{2}$ (real, positive definite).
- **Zero divisors** — the null cone of the above norm; $\mathrm{GPA}$ and $\mathrm{GPS}$ have zero divisors and $\mathrm{GQS}$ has none; the idempotents $\Pi_{1,2}$ are zero divisors of $\mathrm{GPA}$ (and each is a unit of $\mathrm{GPS}$).
- **Annihilators**; **roots of $1$ and the idempotents** (the $\Pi_{1,2}$ and the central $\pm1$, beside the further roots of the operation); **roots of $0$ and the nilpotents**; **roots of a general element**.
- **Specificities**; **ideals and Peirce decomposition** (the idempotent decomposition $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2$ is the central one, and it is an algebra decomposition exactly for $\mathrm{GPA}$); **group of units** — for $\mathrm{GPA}$ it is the complement of the null cone, $A^{2}\neq B^{2}$.
- **Form**; **multiplication operators and the bi-module structure**; **the $2\times2$ matrix element representation**.

### Readings specific to this brief

The counterpart *General Plain Sesqualgebra of the Biquaternions over $\mathbb{C}$* (and the *Quaternions over $\mathbb{R}$* block of the same code, where it exists), plus *The 12 Products of the Reduced Biquaternion Complex Space* and *The Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space* for the fixed conventions.

### Acceptance

Every algebraic claim recomputed on at most 100 elements; the norm, the zero-divisor set and the unit criterion proven; the block's 13 `.md` written; the menu entries lose their `+`. For $\mathrm{GPA}$ only, note explicitly that it is the associative case and that the central idempotents split the algebra.
---

## Brief 5 — Agent 5 — General Quaternionic Sesqualgebra (GQS), 13 articles

**Deliverable: 13 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Introduction to the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `zero-divisors-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Zero Divisors of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `annihilators-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Annihilators of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `the-specificities-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  The Specificities of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `ideals-and-peirce-decomposition-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  Ideals and Peirce Decomposition of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `the-group-of-units-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  The Group of Units of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `the-forms-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  The Forms of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-general-quaternionic-sesqualgebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the General Quaternionic Sesqualgebra of the Reduced Biquaternions
  - `the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the complete structure of the **General Quaternionic Sesqualgebra** over $\mathbb{B}_{\mathrm{r}}$, following article for article the counterpart block *General Quaternionic Sesqualgebra of the Biquaternions over $\mathbb{C}$* and the quaternion block of the same name. The operation here is the sesquilinear product $T^{\natural}W^{*}$ (not associative, no unit).

### Structure-specific content

- **Norm and invertibility** — the algebraic norm of the operation and its invertibility criterion. $\mathrm{GPA}$: $N(T) = A^{2}-B^{2}$ (complex, multiplicative, vanishing on the two idempotents, so every element of the null cone is a zero divisor). $\mathrm{GQA}$: $N(T)=A^{2}+B^{2}$. $\mathrm{GPS}$: $H(T)=|A|^{2}-|B|^{2}$ (real). $\mathrm{GQS}$: $K(T)=|A|^{2}+|B|^{2}$ (real, positive definite).
- **Zero divisors** — the null cone of the above norm; $\mathrm{GPA}$ and $\mathrm{GPS}$ have zero divisors and $\mathrm{GQS}$ has none; the idempotents $\Pi_{1,2}$ are zero divisors of $\mathrm{GPA}$ (and each is a unit of $\mathrm{GPS}$).
- **Annihilators**; **roots of $1$ and the idempotents** (the $\Pi_{1,2}$ and the central $\pm1$, beside the further roots of the operation); **roots of $0$ and the nilpotents**; **roots of a general element**.
- **Specificities**; **ideals and Peirce decomposition** (the idempotent decomposition $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2$ is the central one, and it is an algebra decomposition exactly for $\mathrm{GPA}$); **group of units** — for $\mathrm{GPA}$ it is the complement of the null cone, $A^{2}\neq B^{2}$.
- **Form**; **multiplication operators and the bi-module structure**; **the $2\times2$ matrix element representation**.

### Readings specific to this brief

The counterpart *General Quaternionic Sesqualgebra of the Biquaternions over $\mathbb{C}$* (and the *Quaternions over $\mathbb{R}$* block of the same code, where it exists), plus *The 12 Products of the Reduced Biquaternion Complex Space* and *The Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space* for the fixed conventions.

### Acceptance

Every algebraic claim recomputed on at most 100 elements; the norm, the zero-divisor set and the unit criterion proven; the block's 13 `.md` written; the menu entries lose their `+`. For $\mathrm{GPA}$ only, note explicitly that it is the associative case and that the central idempotents split the algebra.
---

## Brief 6 — Agent 6 — SQA, the symmetric quaternionic algebra (11 articles)

**Deliverable: 11 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Introduction to the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `zero-divisors-of-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Zero Divisors of the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `annihilators-of-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Annihilators of the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-specificities-of-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Specificities of the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-algebraic-norm-of-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Algebraic Norm of the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-symmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the Symmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the **symmetric quaternionic algebra** $\mathrm{SQA}$, the symmetric part of $\mathrm{GQA}$ under the bare interchange:
$$\mathrm{SQA}(T,W) = \tfrac12\bigl(T^{\natural}W + W^{\natural}T\bigr) = AC - BD,$$
a **central** commutative operation, value in $\mathbb{C}_{\mathbb{B}_{\mathrm{r}}} = \mathbb{C}$.

### Structure-specific content

- **Norm and invertibility** — the operation is central-valued, so it is a **form read as a product**, the algebraic norm of the quaternion form $N(T) = A^{2}-B^{2}$; it has no unit and no invertibility in the algebra sense, and the article must say so.
- **Zero divisors** — where $AC-BD = 0$ for nonzero $W$; the sets and their structure.
- **Annihilators**; **roots of $1$ and the idempotents**; **roots of $0$ and the nilpotents**; **roots of a general element** — the roots of a value read in the operation, per *Square Roots of a General Element in the Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space*.
- **Specificities**; **the algebraic norm** (central, ring-valued); **multiplication operators**; **the $2\times2$ representation**.

### Readings specific to this brief

The counterpart *Symmetric Quaternionic Algebra of the Biquaternions over $\mathbb{C}$* and *of the Quaternions over $\mathbb{R}$*; *The Symmetric and Antisymmetric Parts of an Algebra Product*; *The 12 Products of the Reduced Biquaternion Complex Space*.

### Acceptance

The central-valued property proven; the contrast with the biquaternion $\mathrm{SQA}$ (non-central there, central here) stated; 11 `.md`; the `+` dropped.
---

## Brief 7 — Agent 7 — SPS, the symmetric plain sesqualgebra (11 articles)

**Deliverable: 11 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Introduction to the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `zero-divisors-of-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Zero Divisors of the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `annihilators-of-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Annihilators of the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-specificities-of-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Specificities of the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-algebraic-norm-of-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Algebraic Norm of the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-symmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the Symmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-symmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the **symmetric plain sesqualgebra** $\mathrm{SPS}$, the symmetric part of $\mathrm{GPS}$ under the conjugate transpose:
$$\mathrm{SPS}(T,W) = \tfrac12\bigl(TW^{*} + \overline{WZ^{*}}\bigr) = A\bar C - B\bar D,$$
a **central** conjugate-commutative sesquilinear operation, the Hermitian form $H$ read as a product.

### Structure-specific content

- **Norm and invertibility** — the algebraic norm is $H(T) = |A|^{2}-|B|^{2}$, real and indefinite; the operation is the Hermitian form of the algebra.
- **Zero divisors** — the null cone $|A| = |B|$ and the isotropic structure; the relation to the light cone of the Lorentz group of the geometry slot.
- **Annihilators**; **roots of $1$ and the idempotents**; **roots of $0$ and the nilpotents**; **roots of a general element**.
- **Specificities**; **the algebraic norm**; **multiplication operators**; **the $2\times2$ representation**.

### Readings specific to this brief

The counterpart *Symmetric Plain Sesqualgebra of the Biquaternions over $\mathbb{C}$*; *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; *The 12 Products of the Reduced Biquaternion Complex Space*.

### Acceptance

The central-valued and conjugate-commutative properties proven; the indefinite norm and its null cone carried; 11 `.md`; the `+` dropped.
---

## Brief 8 — Agent 8 — AQA, the antisymmetric quaternionic algebra (11 articles)

**Deliverable: 11 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Introduction to the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `zero-divisors-of-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Zero Divisors of the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `annihilators-of-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Annihilators of the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-specificities-of-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Specificities of the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-algebraic-norm-of-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Algebraic Norm of the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-antisymmetric-quaternionic-algebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the Antisymmetric Quaternionic Algebra of the Reduced Biquaternions
  - `the-antisymmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the **antisymmetric quaternionic algebra** $\mathrm{AQA}$, the antisymmetric part of $\mathrm{GQA}$:
$$\mathrm{AQA}(T,W) = \tfrac12\bigl(T^{\natural}W - W^{\natural}T\bigr) = (AD-BC)\,e,$$
an alternating operation **with values in the $j$-line $\mathbb{C}j$** — so it is not a Lie bracket on the space, and the article must establish the identity it does satisfy and the one it fails, beside the corresponding biquaternion $\mathrm{AQA}$.

### Structure-specific content

- **Norm and invertibility** — the operation is not a multiplication and has no unit; its algebraic norm is the diagonal value $\mathrm{AQA}(T,T)$.
- **Zero divisors** — the elements $T$ with $\mathrm{AQA}(T,W)=0$ for some nonzero $W$.
- **Annihilators**; **roots of $1$ and the idempotents**; **roots of $0$ and the nilpotents**; **roots of a general element**.
- **Specificities**; **the algebraic norm**; **multiplication operators**; **the $2\times2$ representation**.

### Readings specific to this brief

The counterpart *Antisymmetric Quaternionic Algebra of the Biquaternions over $\mathbb{C}$* and *of the Quaternions over $\mathbb{R}$*; *The Symmetric and Antisymmetric Parts of an Algebra Product*, §*Lie-Admissible Algebras*.

### Acceptance

The $\mathbb{C}j$-valued property and the failure of the Jacobi identity on the space (with witness) proven; the difference from the biquaternion $\mathrm{AQA}$ stated; 11 `.md`; the `+` dropped.
---

## Brief 9 — Agent 9 — APS, the antisymmetric plain sesqualgebra (11 articles)

**Deliverable: 11 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `introduction-to-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Introduction to the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `norm-and-invertibility-in-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Norm and Invertibility in the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `zero-divisors-of-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Zero Divisors of the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `annihilators-of-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Annihilators of the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-one-and-the-idempotents-of-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `square-roots-of-a-general-element-in-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-specificities-of-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Specificities of the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-algebraic-norm-of-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Algebraic Norm of the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-multiplication-operators-of-the-antisymmetric-plain-sesqualgebra-of-the-reduced-biquaternions`  —  The Multiplication Operators of the Antisymmetric Plain Sesqualgebra of the Reduced Biquaternions
  - `the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`  —  The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions

### What this agent does

Writes the **antisymmetric plain sesqualgebra** $\mathrm{APS}$, the antisymmetric part of $\mathrm{GPS}$:
$$\mathrm{APS}(T,W) = \tfrac12\bigl(TW^{*} - \overline{WZ^{*}}\bigr) = (B\bar C - A\bar D)\,e,$$
a conjugate-alternating sesquilinear operation **with values in the $j$-line $\mathbb{C}j$**, whose algebraic norm is the antisymmetrised square $\mathrm{APS}(T,T) = 2\,\mathrm{Im}(A\bar B)\,j$.

### Structure-specific content

- **Norm and invertibility** — the operation has no unit; the algebraic norm is the antisymmetrised square, non-zero in general.
- **Zero divisors**; **annihilators**; **roots of $1$ and the idempotents**; **roots of $0$ and the nilpotents**; **roots of a general element**.
- **Specificities**; **the algebraic norm**; **multiplication operators**; **the $2\times2$ representation**.

### Readings specific to this brief

The counterpart *Antisymmetric Plain Sesqualgebra of the Biquaternions over $\mathbb{C}$*; *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Diagonal and the Square*.

### Acceptance

The $\mathbb{C}j$-valued property, the non-vanishing diagonal and the failure of the Jacobi identity proven; 11 `.md`; the `+` dropped.
---

## Brief 10 — Agent 10 — the Algebra closers, Topology and Analysis (16 articles)

**Deliverable: 16 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `comparison-of-the-algebraic-structures-over-the-reduced-biquaternion-c-space`  —  Comparison of the Algebraic Structures over the Reduced Biquaternion $\mathbb{C}$ Space
  - `reduced-biquaternions-polar-element-representation`  —  Reduced Biquaternions Polar Element Representation
  - `operators-on-the-reduced-biquaternions`  —  Operators on the Reduced Biquaternions
  - `topology-in-the-space-of-reduced-biquaternions`  —  Topology in the Space of Reduced Biquaternions
  - `the-euclidean-topology-of-the-reduced-biquaternion-algebra`  —  The Euclidean Topology of the Reduced Biquaternion Algebra
  - `topology-and-metric-for-each-of-the-eight-operations-of-the-reduced-biquaternions`  —  Topology and Metric for Each of the Eight Operations
  - `reduced-biquaternion-analysis`  —  Reduced Biquaternion Analysis
  - `reduced-biquaternion-regular-functions`  —  Reduced Biquaternion Regular Functions
  - `reduced-biquaternion-spectral-theory`  —  Reduced Biquaternion Spectral Theory
  - `reduced-biquaternion-integration`  —  Reduced Biquaternion Integration
  - `reduced-biquaternion-elementary-functions`  —  Reduced Biquaternion Elementary Functions
  - `reduced-biquaternion-higher-special-functions`  —  Reduced Biquaternion Higher Special Functions
  - `reduced-biquaternion-lie-group-and-exponential-structure`  —  Reduced Biquaternion Lie Group and Exponential Structure
  - `reduced-biquaternion-discrete-harmonic-analysis`  —  Reduced Biquaternion Discrete Harmonic Analysis
  - `reduced-biquaternion-continuous-harmonic-analysis`  —  Reduced Biquaternion Continuous Harmonic Analysis
  - `fueter-theory-for-reduced-biquaternions`  —  Fueter Theory for Reduced Biquaternions

### What this agent does

Closes the Algebra of the category and writes **Topology** and **Analysis**.

### Specific content

- **Comparison of the Algebraic Structures** — the eight structures side by side, with laws, units, images, norms; the four dead slots restated; the comparison mirroring *Comparison of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.
- **Polar Element Representation** — the polar form of $T = A+Bj$, its uniqueness under the phase-range convention, the two-factor reading through $\Pi_{1,2}$; the corpus's counterpart is *The Polar Element Representation of Biquaternions*.
- **Operators** — the operators of the eight structures collected and compared.
- **Topology** — the Euclidean topology of $\mathbb{R}^{4}$, the unit group as a topological group, the zero-divisor cone, and the topology and metric attached to each of the eight structures (the counterpart is *Topology and Metric for Each of the Twelve Operations*).
- **Analysis** — the analysis on the algebra; the reduction by the idempotents to **two copies of the complex theory** (from *Harmonic Analysis over Hypercomplex Systems*, §*The Commutative Alternative*), with the discrete reduced biquaternion Fourier transform of Pei–Chang–Ding, its two kernel conventions, its convolution theorem and its cost in complex transforms; regular functions, spectral theory, integration, elementary and higher special functions, the exponential and Lie group structure, and Fueter theory.

### Readings specific to this brief

*Comparison of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; *Biquaternions Polar Element Representation*; the biquaternion Topology and Analysis articles; *Harmonic Analysis over Hypercomplex Systems*; *Biquaternion Discrete Harmonic Analysis*, §*The Commutative Alternative*; Pei–Chang–Ding (2004).

### Acceptance

The two-factor reduction is proven and used, not cited alone; the transform cost (two complex DFTs per convolution) is derived; 16 `.md`; the `+` dropped.
---

## Brief 11 — Agent 11 — Geometry and Fractal Geometry (14 articles)

**Deliverable: 14 articles**, each as `articles_maths/<slug>.md`.

### The articles

  - `reduced-biquaternion-rotations-and-lorentz-transformations`  —  Reduced Biquaternion Rotations and Lorentz Transformations
  - `reduced-biquaternion-automorphisms-and-derivations`  —  Reduced Biquaternion Automorphisms and Derivations
  - `the-null-quadric-and-its-projective-geometry-for-the-reduced-biquaternions`  —  The Null Quadric and its Projective Geometry
  - `reduced-biquaternion-versors-and-the-orthogonal-group`  —  Reduced Biquaternion Versors and the Orthogonal Group
  - `the-unitary-group-of-the-reduced-biquaternion-algebra`  —  The Unitary Group of the Reduced Biquaternion Algebra
  - `reduced-biquaternions-and-hyperbolic-geometry`  —  Reduced Biquaternions and Hyperbolic Geometry
  - `reduced-biquaternion-objects-and-their-matrix-correspondences`  —  Reduced Biquaternion Objects and their Matrix Correspondences
  - `reduced-biquaternion-spin-geometry`  —  Reduced Biquaternion Spin Geometry
  - `the-reduced-biquaternion-quadratic-map-and-its-julia-sets`  —  The Reduced Biquaternion Quadratic Map and its Julia Sets
  - `the-idempotent-decomposition-and-the-reduced-biquaternion-split-fractal`  —  The Idempotent Decomposition and the Split Fractal
  - `the-slices-of-the-reduced-biquaternion-julia-sets`  —  The Slices of the Reduced Biquaternion Julia Sets
  - `the-reduced-biquaternion-iterated-function-systems`  —  The Reduced Biquaternion Iterated Function Systems
  - `the-reduced-biquaternion-mandelbrot-set-and-the-connectedness-locus`  —  The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus
  - `the-hausdorff-dimension-of-the-reduced-biquaternion-julia-sets`  —  The Hausdorff Dimension of the Reduced Biquaternion Julia Sets

### What this agent does

Writes **Geometry** and **Fractal Geometry**, closing the category.

### Specific content

- **Rotations and Lorentz Transformations** — the algebra carries an elliptic rotation from the complex factor and a hyperbolic rotation from the $e$-direction at once; the polar form is read as a rotation and a Lorentz transformation (the polar form of Pei–Chang–Ding, §V).
- **Automorphisms and Derivations** — the automorphism group and the derivations of $\mathbb{B}_{\mathrm{r}}$.
- **The Null Quadric** — the quadric $A^{2}=B^{2}$ (equivalently $|A|^{2}=|B|^{2}$ for $\mathrm{SPS}$) and its projective geometry.
- **Versors and the Orthogonal Group; the Unitary Group** — the level sets of the two forms and the groups they carry.
- **Reduced Biquaternions and Hyperbolic Geometry**; **Objects and their Matrix Correspondences**; **Spin Geometry**.
- **Fractal Geometry** — the quadratic family and its Julia sets; the idempotent decomposition and the split fractal (the dynamics reduces to two complex slices, so the fractal is a **product** of two complex Julia sets, not a rotational hull — mirror *The Idempotent Decomposition and the Split Fractal* of the biquaternion category); the slices; the iterated function systems; the Mandelbrot set and the connectedness locus; the Hausdorff dimension.

### Readings specific to this brief

*Biquaternion Rotations and Lorentz Transformations*; *Biquaternion Automorphisms and Derivations*; *The Null Quadric and its Projective Geometry*; *Biquaternion Versors and the Orthogonal Group*; *The Unitary Group of the Biquaternion Algebra*; *The Split-Biquaternion Fractal* articles; *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, §*The Commutative Alternative in Dimension Four*; *List of Algebras by Dimension*.

### Acceptance

The reduction of the dynamics to two complex slices is proven, with the effect of the zero divisors on the singular sets; the rotation-versus-boost reading is derived from the polar form; 14 `.md`; the `+` dropped.
---

