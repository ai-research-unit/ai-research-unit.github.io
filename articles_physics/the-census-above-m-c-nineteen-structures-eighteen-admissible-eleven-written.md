# __The Census Above $M_C$: Nineteen Structures, Eighteen Admissible and Eleven Written__

## Introduction

**The claim, and its scope.** In this corpus's $\mathrm{SU}(4)$ model — one connection, sixteen Weyl fields, one Hermitian $4\times4$ scalar, and the coefficient declarations the corpus makes — the group admits **nineteen** structures at dimension four or below. **Eighteen are admissible**, because the rule's fourth condition removes the total derivative. **Seventeen survive canonical normalisation**, which removes a second scalar kinetic term. **Eleven carry a nonzero coefficient**, and the other six are declared zero and printed with their warrants.

**Four numbers, and each one names a filter.** A number is a claim only when its filter is attached, and the corpus quotes different numbers at different rungs. **This article keeps the ladder explicit: candidates, admissible, canonical, written.** A reader who wants a different total can read the ladder at the rung that matches those conventions.

**It is a count under a stated rule, not a theorem about $\mathrm{SU}(4)$.** A different declaration about coefficients moves the eleven. A different normalisation moves the seventeen. §*What the Number Depends On* gives the number each convention moves. **The artefact is the enumeration; the honesty is in naming what the enumeration depends on.**

**Why the count is not four, and why it is not forty-nine.** The broken phase carries forty-seven invariant rows. **This phase loses the whole electroweak list** — no $W$, no $Z$, no photon, no mixing angle, no vacuum, no Goldstone, no Proca row — because there is one force and no scale. **And it gains a block, because the scalar is a matrix**: a $4\times4$ Hermitian carries eleven polynomial invariants at degree four or below where a doublet carries two. **Eleven of the nineteen are scalar monomials.**

**The answer.**

$$
\boxed{\;19\ \xrightarrow{\ \text{no total derivative}\ }\ 18\ \xrightarrow{\ \text{one kinetic per field}\ }\ 17=11+6,\qquad 11=1+1+1+2+4+2.\;}
$$

## The Ladder

**Four rungs, four filters, and each filter is stated where it is applied.**

| rung | filter | count |
|---|---|---|
| candidates | the group admits: Lorentz scalar, local $\mathrm{SU}(4)$ invariant, dimension $\le4$ | $19$ |
| admissible | not a total derivative | $18$ |
| canonical | one kinetic term per field | $17$ |
| written | nonzero coefficient | $11$ |

**The nineteen decompose as one curvature, one total derivative, one fermion kinetic, one fermion mass, two scalar kinetic, eleven potential and two Yukawa.** That is $1+1+1+1+2+11+2=19$.

**The three filters remove one, one and six, and their warrants differ.** The total derivative is removed by the rule. **The second scalar kinetic term is removed by a normalisation and not by the rule** — the rule admits it, and §*The Structure Removed by Normalisation* says why it goes anyway. **The six zeros are removed by coefficient declarations** and not by the group, and §*The Six Declared Zeros* gives each one's warrant. **A count that merged the three would be unable to say which is which, and that inability is the whole of the difficulty.**

**The coincidence to be avoided.** The row count below is also nineteen — seventeen canonical rows plus the two gauge rows. **One nineteen counts structures the group admits; the other counts rows once two structures the group does not act on are included.** They are equal by arithmetic and for no reason, and the two are never added.

## The Rule

**Four conditions define admissibility, and the fourth is the one that removes $\theta_4$.** A structure is admissible if it is a Lorentz scalar, invariant under the local $\mathrm{SU}(4)$, of dimension four or below, and **not a total derivative**. **The rule is [the census rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) applied to a smaller content, and the fourth condition is applied here exactly as the broken phase applies it**: there, $\theta_{\mathrm{QCD}}$ is "present as a parameter and absent as a row", and $\theta_4$ is that same object above $M_C$.

**The corpus's rule includes canonical normalisation among its conditions, and this article splits that rule in two on purpose.** The four invariance, dimension and derivative conditions decide what the group admits; **the normalisation condition decides what is written of what the group admits.** Splitting costs nothing and buys the ladder. **A reader who keeps the rule whole gets seventeen directly and loses the ability to say which of the eighteen the one removal was.**

**Two counting conventions sit on top of the four conditions, and neither is a condition.** The hermitian conjugate counts once with its term. **A structure counts once per field it can be built on, and the coefficient is not looked at** — a row exists because the group admits it, and whether its coefficient is zero is a second question and a different column.

**Canonical normalisation is therefore carried as a separate filter here, and it is a condition of the corpus's rule and not of this article's four.** A second scalar kinetic structure, $(\partial_{\imath}\operatorname{tr}\Xi)^{2}$, is a Lorentz scalar, invariant, dimension four and not a total derivative, **so the four conditions admit it and it is one of the eighteen.** It is removed at the next rung, by the requirement that each field carry one kinetic term. **The rule decides what exists; the normalisation decides what is written of what exists; and a census that applied the second while claiming to apply only the first would be wrong at the rung where it was silent.** This article applies it at its own rung, in the open.

**Three bounds close the candidate set.** Locality bounds the derivatives, dimension bounds the total degree, and the carrier bounds the contractions. They are [the closure of the term list](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html)'s three bounds.

**The content is three fields.** Fifteen connections, sixteen Weyl fields, one Hermitian $4\times4$ matrix in sixteen real components. **No second scalar, no second fermion, no second connection** — and the count is finite for that reason and for no other.

## The Content

| field | multiplicity | mass above $M_C$ |
|---|---|---|
| the connection $A_{a,\imath}$ | fifteen, $30$ degrees of freedom | $0$, exactly |
| the Weyl fields $\xi_{f}$ | sixteen, $32$ states | $0$, by declaration |
| the scalar $\Xi$ | sixteen real | $\mu_{\Phi}^{2}$ on $15$; $\mu_{\Phi}^{2}+4\mu_{2}^{2}$ on the trace |

**The phase is not a massless phase.** It has no vector mass and no fermion mass, and it has sixteen scalar masses. **"Above $M_C$ everything is massless" is true of the fifteen directions and false of the scalar.**

**The three counts add to seventy-eight.** $30+32+16$. **The vectors are massless because a mass term for a connection is not invariant**, not because the vacuum is far away: $m^{2}A_{\imath}A_{\imath}$ fails the invariance condition here exactly as it fails it below $M_C$.

**One fermion kinetic structure and not two, and the reason is chirality and not a coefficient.** A kinetic term with $\gamma_{\imath}\gamma_{5}$ differs from the vector one by $\gamma_{5}$, which acts as $\pm1$ on a Weyl field; **so the two are the same row up to a sign on each chirality, and the row counts once.**

## The Lagrangian

**Eleven rows carry a nonzero coefficient, and every row is numbered.**

$$
\begin{aligned}
\mathcal{L}={}&
\underbrace{-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}}_{1}
\underbrace{{}+\sum_{f=1}^{16}\bar\xi_{f}\,i\gamma_{\imath}D_{\imath}\xi_{f}}_{2}
\underbrace{{}+\operatorname{tr}\bigl(D_{\imath}\Xi\bigr)^{\dagger}\bigl(D_{\imath}\Xi\bigr)}_{3}\\[3pt]
&{}\underbrace{{}-\mu_{\Phi}^{2}\operatorname{tr}\Xi^{2}}_{4}
\underbrace{{}-\mu_{2}^{2}\bigl(\operatorname{tr}\Xi\bigr)^{2}}_{5}
\underbrace{{}-\lambda_{1}\operatorname{tr}\Xi^{4}}_{6}
\underbrace{{}-\lambda_{2}\bigl(\operatorname{tr}\Xi^{2}\bigr)^{2}}_{7}
\underbrace{{}-\lambda_{3}\bigl(\operatorname{tr}\Xi\bigr)^{2}\operatorname{tr}\Xi^{2}}_{8}
\underbrace{{}-\lambda_{4}\bigl(\operatorname{tr}\Xi\bigr)^{4}}_{9}\\[3pt]
&{}\underbrace{{}+y_{\alpha\beta}\,\bar\xi^{\alpha}\Xi_{0}\,\xi^{\beta}+\text{h.c.}}_{10}
\underbrace{{}+y'_{\alpha\beta}\bigl(\operatorname{tr}\Xi\bigr)\bar\xi^{\alpha}\xi^{\beta}+\text{h.c.}}_{11},
\end{aligned}
$$

with $\Xi_{0}=\Xi-\tfrac14(\operatorname{tr}\Xi)\mathbb 1$ the traceless part. **Rows $10$ and $11$ are two structures and not one**, for the reason §*The Two Yukawa Structures* gives: in the canonical basis the group allows an independent coefficient on each.

**The covariant derivatives are two, and both carry the one coupling.**

$$
D_{\imath}\xi_{f}=\partial_{\imath}\xi_{f}-ig_{4}\sum_{a}A_{a,\imath}\,\bigl(t_{a}\otimes\mathbb 1_{2}\bigr)\xi_{f},
\qquad
D_{\imath}\Xi=\partial_{\imath}\Xi-ig_{4}\sum_{a}A_{a,\imath}\bigl[t_{a},\Xi\bigr].
$$

**The commutator and not a multiplication** is the scalar's matrix index: $\Xi$ carries one line label up and one down, and the mass operator needs both. **The two-index rule on the fermion** — $X\otimes\mathbb 1_{2}$, every generator blind to the copy index — is the whole of the flavour structure of this phase.

**Three structures stand outside the seventeen, and they are of three kinds.**

$$
\mathcal{L}_{\mathrm{gf}}=-\frac{1}{2\zeta}\sum_{a}\bigl(\partial_{\imath}A_{a,\imath}\bigr)^{2},
\quad
\mathcal{L}_{\mathrm{gh}}=\sum_{a}\partial_{\imath}\bar c_{a}D_{\imath}c_{a},
\quad
\mathcal{L}_{\theta}=\theta_{4}\,\varepsilon^{\imath\jmath\kappa\lambda}\operatorname{tr}F_{\imath\jmath}F_{\kappa\lambda}.
$$

**Two of the three are rows and one is not.** The fixing and the ghosts are rows the group does not act on; **$\theta_4$ is not a row at all**, because the fourth condition excluded it. So:

| line | count |
|---|---|
| canonical rows | $17$ |
| gauge rows the group does not act on | $2$ |
| **rows in total** | $19$ |
| parameters of the gauge rows | $\zeta$, in $\mathcal{L}_{\mathrm{gf}}$ |
| parameters with no row | $\theta_4$ |

**$\zeta$ is a parameter of a row, and $\theta_4$ is a parameter of none.** The distinction is not pedantry: $\zeta$ multiplies $\mathcal{L}_{\mathrm{gf}}$, which is written above, and cancels from every observable; **$\theta_4$ multiplies nothing written, because the thing it would multiply was excluded before the row count began.**

## The Structure Removed by Normalisation

**$(\partial_{\imath}\operatorname{tr}\Xi)^{2}$ passes all four conditions, and the canonical kinetic term already carries a piece of it.** With $\Xi=\Xi_{0}+\tfrac14(\operatorname{tr}\Xi)\mathbb 1$ and $\operatorname{tr}\Xi_{0}=0$,

$$
\operatorname{tr}\bigl(D_{\imath}\Xi\bigr)^{\dagger}\bigl(D_{\imath}\Xi\bigr)
=\operatorname{tr}\bigl(D_{\imath}\Xi_{0}\bigr)^{\dagger}\bigl(D_{\imath}\Xi_{0}\bigr)+\tfrac14\bigl(\partial_{\imath}\operatorname{tr}\Xi\bigr)^{2},
$$

**because the cross terms vanish**: $\operatorname{tr}(D_{\imath}\Xi_{0})^{\dagger}=0$, the covariant derivative of a traceless matrix being traceless. **So the scalar's kinetic sector carries two coefficients**, one on each term of the right-hand side, and only their ratio is physical.

**Canonical normalisation sets the second to zero, and that is a choice of basis.** No symmetry removes the term; **a field redefinition of the trace mode does**, and the redefinition is what the normalisation fixes. **The cost is that the same redefinition moves four potential coefficients**, which is why the census is quoted in the basis where the scalar's kinetic term is $\operatorname{tr}(D\Xi)^{\dagger}(D\Xi)$ and nothing else.

**What the rung buys and what it does not.** It buys a unique set of coefficients to count, so that "eleven" is a number and not a class of numbers. **It does not buy a physical statement** — the ratio of the two kinetic coefficients is a parameter of the general theory, and setting it to zero is a point in a one-parameter space. **The census counts the point, and §*What the Number Depends On* records the space.**

**A reader who keeps the second term counts eighteen admissible structures and seventeen parameters.** That is the correct count in that basis, and the ladder says so.

## The Two Mass Rows

**Rows $4$ and $5$ are the only masses carried, and they are the trace decomposition of one quadratic form.**

$$
-\mu_{\Phi}^{2}\operatorname{tr}\Xi^{2}-\mu_{2}^{2}\bigl(\operatorname{tr}\Xi\bigr)^{2}
\;\Longrightarrow\;
m^{2}_{ab}=\mu_{\Phi}^{2}\ (15\ \text{traceless}),\qquad
m^{2}_{\mathrm{tr}}=\mu_{\Phi}^{2}+4\mu_{2}^{2}\ (\text{the trace}).
$$

**The four is $\operatorname{tr}\mathbb 1$**, since along $\Xi=c\,\mathbb 1$ the ratio $(\operatorname{tr}\Xi)^{2}/\operatorname{tr}\Xi^{2}$ is $16/4=4$. **The Hessian is the mass squared in this normalisation**, because $\operatorname{tr}(\partial\Xi)^{2}=\tfrac12\sum_{a}(\partial\chi_{a})^{2}$ on generators with $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ — already canonical, so no factor of two enters.

**Both coefficients are positive above $M_C$, and that is a region and not a tuning.** The symmetric minimum needs $\mu_{\Phi}^{2}>0$ and $\mu_{2}^{2}>0$; every value in that region is a phase. The full spectrum, the boundedness cone and the branch where the sign flips are [the primordial potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html)'s.

**No vector mass row exists, and no fermion mass row carries a coefficient.** A vector mass fails invariance and cannot be written. **A fermion mass is invariant** — the content is $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$, vector-like, so $\bar{\mathbf4}\otimes\mathbf4$ contains a singlet — **and row $12$ is that term with a zero coefficient. One is forbidden and the other is declined**, and a reader who hears "massless fermions" will otherwise conclude that the group forbids the mass.

## The Six Declared Zeros

**Six admissible rows carry a zero coefficient, and their warrants are four different warrants.**

| row | structure | dimension | warrant for the zero |
|---|---|---|---|
| $12$ | $m_{\alpha\beta}\bar\xi^{\alpha}\xi^{\beta}+\text{h.c.}$ | $3$ | declined: the phase has no vacuum, and the masses are made below $M_C$ |
| $13$ | $c\,\operatorname{tr}\Xi$ | $1$ | **forced**: a linear term is not stationary at $\Xi=0$, so a symmetric vacuum sets it to zero |
| $14$ | $c_{1}\operatorname{tr}\Xi^{3}$ | $3$ | declared: evenness under $\Xi\to-\Xi$ |
| $15$ | $c_{2}\operatorname{tr}\Xi^{2}\operatorname{tr}\Xi$ | $3$ | declared: evenness under $\Xi\to-\Xi$ |
| $16$ | $c_{3}\bigl(\operatorname{tr}\Xi\bigr)^{3}$ | $3$ | declared: evenness under $\Xi\to-\Xi$ |
| $17$ | $\lambda_{5}\operatorname{tr}\Xi^{3}\operatorname{tr}\Xi$ | $4$ | **declared separately**: evenness does not remove it |

**Row $13$ is the one that would be dishonest to leave out.** $\operatorname{tr}\Xi$ is gauge-invariant, dimension one, and not a total derivative, so the four conditions admit it. **It is zero because the phase requires $\Xi=0$ to be stationary, which is a statement about the vacuum and not about the group.** A count that dropped it silently would report a rule at work where a phase choice is at work.

**Row $17$ is the declaration that evenness does not cover.** $\operatorname{tr}\Xi^{3}\operatorname{tr}\Xi$ is even under $\Xi\to-\Xi$, since both factors flip sign, so it survives the discrete symmetry that removes rows $14$–$16$. **Its zero is a separate declaration: the potential uses $\Xi$ through $\Xi^{2}$ and $\operatorname{tr}\Xi$ only.** So the cubics are removed by one symmetry and row $17$ by one sentence, and the two are not the same argument.

**What the six zeros would cost if switched on.** Row $12$ brings two, by the same singular-value count alone. Rows $14$–$16$ bring three. Row $17$ brings one. Row $13$ brings one and destroys the phase. **So the declared part of the census is seven parameters deep**, counted separately from the nine the Lagrangian carries. **And the bare mass shares its flavour group with $y$**, so switching both on is not simply additive: one $\mathrm{U}(2)\times\mathrm{U}(2)$ must suffice for two matrices, and the pair then carries more than two.

## The Two Yukawa Structures

**The matrix is a sum of two pieces and the group sees them separately.** With $\Xi=\Xi_{0}+\tfrac14(\operatorname{tr}\Xi)\mathbb 1$,

$$
\bar\xi^{\alpha}\Xi\,\xi^{\beta}=\bar\xi^{\alpha}\Xi_{0}\,\xi^{\beta}+\tfrac14\bigl(\operatorname{tr}\Xi\bigr)\bar\xi^{\alpha}\xi^{\beta},
$$

**and each piece is invariant on its own.** The traceless one contracts the $\mathbf{15}$ of $\bar{\mathbf4}\otimes\mathbf4$ with the $\mathbf{15}$ in $\Xi$; the trace one contracts the singlet with the singlet. **Two contractions, two independent $2\times2$ matrices, two rows.**

**The corpus writes one, and that is a tie.** Writing $y\,\bar\xi\Xi\xi$ is the choice $y'=\tfrac14y$. **The tie is not a group-theoretic fact, and its cost is six parameters** — a pair's eight against a single matrix's two.

**The field redefinition that removes the second kinetic structure acts on the two matrices, and the transformation is not the identity on either.** With $\Xi\to\Xi+b\,(\operatorname{tr}\Xi)\mathbb 1$ the traceless part is unchanged and the trace is rescaled by $1+4b$, so

$$
y\ \longrightarrow\ y,
\qquad
y'\ \longrightarrow\ \frac{y'}{1+4b},
\qquad\text{hence}\qquad
\frac{y'}{y}\ \longrightarrow\ \frac{1}{1+4b}\,\frac{y'}{y}.
$$

**Nothing here is invariant, and the article does not claim that anything is.** The ratio $y'/y$ is not preserved by the redefinition; **it is moved by exactly the amount that the kinetic normalisation then undoes**, because the same $b$ which rescales $y'$ is the one which rescales the coefficient of $(\partial_{\imath}\operatorname{tr}\Xi)^{2}$.

**So the physical statement is a statement about a fixed basis and not about an invariant.** Canonical normalisation sets $b$ once and for all, and what remains is the flavour content of the pair, **which is the eight numbers §*The Tally* counts**; the tie $y'=\tfrac14y$ is **one point in those eight rather than a symmetry of them.**

**Two consequences, and both matter for the count.** First, **the two rows are independent in the canonical basis**, which is why the census counts two and not one. Second, **the tie is a basis statement**, so a reader working in a basis with a nonzero second kinetic coefficient will find $y'$ adjustable and the same physics. **The census is quoted in one basis and says which.**

## The Tally

**Seven interaction types, and each one is read off a written row.**

| type | from row | realisation count |
|---|---|---|
| $AAA$ | $1$ | $80$ nonzero structure-constant components, of $105$ pairs |
| $AAAA$ | $1$ | one Lorentz structure |
| $\bar\xi A\xi$ | $2$ | one Lorentz structure, fifteen generators, both blocks |
| $A\Xi\Xi$ | $3$ | $15$ |
| $AA\Xi\Xi$ | $3$ | $120$ symmetric pairs $(a,b)$ |
| $\Xi\Xi\Xi\Xi$ | $6$–$9$ | four monomials, one Lorentz structure |
| $\bar\xi\xi\Xi$ | $10$, $11$ | two structures, one type |

**The third column counts realisations and not operators.** $80$ is not eighty Feynman rules; it is eighty nonzero commutator components out of a hundred and five pairs, and $120$ is a hundred and twenty symmetric index pairs in the component expansion of one structure. **Both numbers are counts of how many distinct arrays a vertex can carry; neither is a count of independent gauge-invariant operators.** The column heading says so.

**Seven is the count of types for the eleven written rows, and it is not a group-theoretic seven.** Three additions would move it: **the three cubics switched on add $\Xi^{3}$, making eight; $\theta_4$ written adds two parity-odd structures in $AAAA$ and $AAA$, making ten; and a second Lorentz structure in the fermion bilinear would add a type of its own** — the Pauli term, which is dimension five and out of range.

**Fifteen parameters are carried.** $g_{4}$; $\mu_{\Phi}^{2}$ and $\mu_{2}^{2}$; $\lambda_{1}$–$\lambda_{4}$; and eight in the Yukawa sector. **Sixteen including $\zeta$, which is a gauge parameter and not physical. Seventeen including $\theta_4$.**

**The eight in the Yukawa sector are singular values, and the count is not four per matrix.** A single $2\times2$ matrix has eight real entries; **the copy basis removes six**, because a global $\mathrm{U}(2)$ on $\xi^{\alpha}$ and an independent one on $\bar\xi^{\alpha}$ act as $y\to W^{\dagger}yV$ and leave a generic $y$ alone only through the two diagonal phases. So one matrix carries $8-6=2$. **A count by phases alone removes four and reports four, and it double-counts**, because the copy basis is unobservable and the gauge group is blind to it. [The Yukawa sector](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html) states $8-6=2$ by the same route.

**Two matrices are not twice one, and the answer is eight and not four or ten.** Rows $10$ and $11$ transform under the same $\mathrm{U}(2)\times\mathrm{U}(2)$, so the pair is sixteen real numbers acted on by one group of eight. **A generic pair has no stabiliser** — the diagonalisation a single matrix admits is spent once, and the second matrix's rotation is then fixed — so $16-8=8$ survive. **They are the two singular values of $y$, the two of $y'$, and the four numbers in the relative unitary $y'y^{-1}$** — two magnitudes, one angle and three phases. **The corpus writes one matrix**, which is the tie $y'=\tfrac14y$, and the tie collapses the pair to a single matrix's two.

**Seven sleep in the declared zeros**: two in the bare mass, one in the linear term, three in the cubics and one in the fifth quartic. **A count of "twelve parameters" would have been a count of a different convention, and a count of four per Yukawa matrix would have been a count that stops one removal early.**

## What the Number Depends On

**Three conventions move the row count, each at its own rung, and a fourth moves the parameters.**

| convention | choice made here | what it moves |
|---|---|---|
| total derivatives | excluded as rows, kept as parameters | $19\to18$, and the row count $20\to19$ |
| canonical normalisation | one kinetic term per field | $18\to17$, and fixes $b$, which makes $y'/y$ a parameter |
| zero coefficients | printed as rows and marked | $17\to11$ written; keeping them gives $17=11+6$ |
| the Yukawa tie | **untied**: two rows and eight parameters | tying $y'=\tfrac14y$ removes a row ($11\to10$) and six parameters ($15\to9$) |

**The first is the rule's and the second and third are the author's.** A reader who disagrees with either of the two gets a different total, and the table says which total. **A reader who disagrees with the first is disagreeing with the category's rule, and the broken phase applies the same rule to forty-seven rows.**

**What does not depend on a convention.** The partition count $1,2,3,5$ for degree $1,2,3,4$; the trace mass split $\mu_{\Phi}^{2}$ and $\mu_{\Phi}^{2}+4\mu_{2}^{2}$; the degrees of freedom $30+32+16$; the realisation counts $15$, $80$ and $120$; and the exclusion of the vector mass. **Those are the arithmetic, and the arithmetic is not what the headline rests on.**

## What Is Not in It

**No electroweak sector.** No $W$, no $Z$, no photon, no mixing angle, no Fermi constant, no $v$. **The phase has no scale in it**: $\mu_{\Phi}$ is a mass and not a vacuum expectation, and $M_C$ is where the vacuum forms.

**No strong sector.** No $\mathrm{SU}(3)$, no confinement, no gluon. **The phase distinguishes no direction among the fifteen**: the eight that the restructuring will call colour are eight of the fifteen here, massless with the other seven and equal to them in every coupling. **That is a statement about the restructuring and not a result of the count** — nothing in this article names the eight, and [no confinement](no-confinement-above-m-c.html) states the negative.

**No flavour structure beyond two matrices.** No CKM, no PMNS, no Jarlskog invariant. **The copy index is a commutant**: every generator acts as $X\otimes\mathbb 1_{2}$, so no boson changes it and the whole of flavour sits in $y$ and $y'$.

**Not Pati–Salam.** Pati–Salam gauges $\mathrm{SU}(4)\times\mathrm{SU}(2)_{L}\times\mathrm{SU}(2)_{R}$ and puts $B-L$ inside the four as a fourth colour. **This theory gauges one simple factor and nothing beside it**: rank three, one coupling, no second factor to break, no $B-L$ boson. The four lines $(t,x,y,z)$ are coordinates on one multiplet and the lepton line is a declaration. **The $\mathrm{SU}(3)$ below $M_C$ is $\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb C e_{t})$ and not a factor of a product**, and the $B-L$ the corpus uses is a number the cells carry, computed entry by entry. **Rank three cannot reach the endpoint's five**, which is why the weak factors arrive as a copy index and not as debris. **A Pati–Salam reader will look for $\mathrm{SU}(2)_{R}$ and find an index in its place.**

## Checks

1. The ladder. $19$ candidates, $18$ admissible, $17$ canonical, $11$ written, $6$ zero.
2. The candidates. $1+1+1+1+2+11+2=19$ by class: curvature, total derivative, fermion kinetic, fermion mass, scalar kinetic (two), potential, Yukawa (two).
3. The reductions. The fourth condition removes $\theta_4$; canonical normalisation removes $(\partial\operatorname{tr}\Xi)^{2}$; the coefficient declarations remove six. Nothing is removed twice and nothing is counted twice.
4. The potential's monomials. Partitions of $d$ into at most four parts: $1,2,3,5$ for $d=1,2,3,4$, so $11$.
5. The canonical split. $17=11$ written $+6$ zero.
6. The row count. $17+2=19$, and $20$ would require seating $\theta_4$, which the fourth condition forbids.
7. The parameter ledger. $\zeta$ belongs to $\mathcal{L}_{\mathrm{gf}}$, which is a row; $\theta_4$ belongs to no row.
8. The trace's mass. $\mu_{\Phi}^{2}+4\mu_{2}^{2}$ with $4=\operatorname{tr}\mathbb 1$.
9. The kinetic split. The canonical term supplies $\tfrac14(\partial\operatorname{tr}\Xi)^{2}$, since $\operatorname{tr}(D\Xi_0)^{\dagger}=0$.
10. The realisation counts. $15$ generators, $80$ nonzero brackets of $105$ pairs, $15\cdot16/2=120$ symmetric pairs.
11. The carried parameters. $1+1+1+4+8=15$; with $\zeta$, $16$; with $\theta_4$, $17$.
12. The Yukawa count. One matrix: $8-8+2=2$. A generic pair: $16-8+0=8$. Neither is four, and the pair is not twice the single matrix.
13. The sleeping parameters. Two in the bare mass, one in the linear term, three in the cubics and one in the fifth quartic: $7$.
14. The Yukawa transformation. $y\to y$ and $y'\to y'/(1+4b)$, so $y'/y$ is moved and is fixed only once $b$ is.
15. The degrees of freedom. $30+32+16=78$.
16. The one coupling. $g_{4}$ appears in rows $1$, $2$, $3$ and in no coefficient of rows $4$–$11$.

## Summary

**Nineteen structures the group admits, eighteen admissible, seventeen in the canonical basis, eleven written.** The eleven are the curvature square, the two kinetic terms, the two scalar quadratics, the four quartics and the two Yukawa structures. **The three reductions are three different kinds of removal**: one by the rule's fourth condition, one by a normalisation that the rule permits and the census declines, and six by coefficient declarations whose warrants are themselves four different warrants.

**The count is a count under a rule, and the rule is the broken phase's.** The ladder is the article's spine because the corpus's numbers differ at different rungs, and **a number quoted without its rung is not a claim but a coincidence.**

**Two masses, both the scalar's**, and no vector mass because invariance forbids it and no fermion mass because the phase declines it. **One force, one coupling, no scale, and a $4\times4$ scalar that supplies eleven of the nineteen rows.**

**Fifteen parameters are carried, and the Yukawa block contributes eight.** Singular values and not entries: **the copy basis is unobservable, and a count that forgets it stops one removal early — and a count that treats the two matrices independently overcounts, because one group serves both.**

**And the census is not a derivation.** It enumerates what a declared set of fields and coefficients admits. **What the enumeration cannot say is why these coefficients**, and no article in this category claims otherwise.

## Summary of Notation

| symbol | meaning |
|---|---|
| $F_{a,\imath\jmath}$ | the curvature of generator $a$; $F_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a}$ |
| $t_{a}$ | the fifteen normalised Hermitian generators, $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $g_{4}$ | the one coupling, the same in rows $1$, $2$, $3$ |
| $\Xi$, $\Xi_{0}$ | the Hermitian $4\times4$ scalar and its traceless part |
| $\xi_{f}$ | the sixteen Weyl fields; $\alpha$ the copy index, $i$ the quartet index |
| $y$, $y'$ | the traceless and trace Yukawa matrices |
| $m_{\alpha\beta}$ | the bare Dirac mass matrix, row $12$, coefficient zero |
| $\theta_{4}$ | the vacuum angle, a parameter with no row |
| $b$ | the trace-mode shift; fixed by canonical normalisation |
| $d$ | the degree of a potential monomial; the invariants number $1,2,3,5$ for $d=1,2,3,4$ |

## Further Reading

- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The minimal reading of the same content, and the normalisation that fixes $\tfrac14$.
- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The two quadratics and four quartics at working size, the boundedness cone, and the branch where the vacuum forms.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html). Rows $3$–$9$ expanded, and the $120$ computed.
- [The Lagrangian and the Sixteen](the-lagrangian-and-the-sixteen-kinetic-term-and-yukawa-coupling.html). Rows $2$ and $10$, the state count and the mass matrix after the condensate.
- [The Feynman Rules of the $\mathrm{SU}(4)$ Model](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The interaction types at working size, and the two bases' normalisations.
- [The Closure of the Term List](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html). Why the candidate space is finite, and the three reasons a row can fail.
- [One Obstruction, Four Groups](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html). Why no vector mass row exists.
- [The Complete Lagrangian: Forty-Seven Terms](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). The other side of the vacuum, counted by the same rule.
