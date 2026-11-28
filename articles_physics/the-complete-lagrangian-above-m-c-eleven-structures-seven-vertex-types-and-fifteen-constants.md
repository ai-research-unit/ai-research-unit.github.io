# __The Complete Lagrangian Above $M_C$: Eleven Structures, Seven Vertex Types and Fifteen Constants__

## Introduction

**The question.** What is the whole Lagrangian of this phase, written once, and which of its pieces are interactions?

**The answer.**

$$
\boxed{\;11\ \text{rows},\quad 7\ \text{types},\quad 15=1+2+4+8,\quad 19=11+6+1+1.\;}
$$

**Eleven rows with nonzero coefficients, seven interaction types, fifteen constants, and three items outside the row count.**

**"Complete" means complete at dimension four, for the content of §*The Assembly*, with the six scalar coefficients as declared in [the boundary](the-boundary-of-the-list-above-m-c-the-bare-mass-the-cubics-and-theta-four.html) and no bare fermion mass.** The tower above dimension four, and the general potential with its cubics restored, are outside this article; both are named at the end.

**Three items sit outside the eleven: the gauge-fixing row, the ghost row and the vacuum angle.** Two of them carry a parameter and one carries none, and the distinction is stated in §*The Last Line*.

**What this article is for.** The pieces are built one at a time in the articles of this category. **This article puts them in one expression and reads the interactions off it.** The count that produces the eleven is [the census](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html)'s argument and is not repeated here. The warrants of the six zeros are [the boundary](the-boundary-of-the-list-above-m-c-the-bare-mass-the-cubics-and-theta-four.html)'s and are not repeated either. **What is new here is the assembly and the vertex list.**

**The scope sentence.** The eleven are dimension four or below, one canonical kinetic term per field, with hermitian conjugates counted once, coefficients invisible and nothing that is a total derivative. **The last line of the expression is outside that scope and is written anyway**: a fixing, its ghosts and a vacuum angle are what a complete expression carries, and they are not what the eleven count.

## The Assembly

**The eleven rows, numbered as the census numbers them so that the two articles can be read against each other.**

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
\underbrace{{}+y'_{\alpha\beta}\bigl(\operatorname{tr}\Xi\bigr)\bar\xi^{\alpha}\xi^{\beta}+\text{h.c.}}_{11}\\[3pt]
&{}\underbrace{-\frac{1}{2\zeta}\sum_{a}\bigl(\partial_{\imath}A_{a,\imath}\bigr)^{2}}_{\mathrm{gf}}
\underbrace{{}-\sum_{a}\partial_{\imath}\bar c_{a}D_{\imath}c_{a}}_{\mathrm{gh}}
\underbrace{{}+\theta_{4}\,\varepsilon^{\imath\jmath\kappa\lambda}\operatorname{tr}F_{\imath\jmath}F_{\kappa\lambda}}_{\theta_{4}},
\end{aligned}
$$

**$\Xi_{0}=\Xi-\tfrac14(\operatorname{tr}\Xi)\mathbb 1$ is the traceless part.**

**The last line is not among the eleven.** Its first two terms are rows the group does not act on and the third is not a row at all, **and the expression is complete only with them**: a computation needs a gauge and therefore a fixing and its ghosts, and the vacuum angle is a parameter of the theory whether or not it is written.

**The covariant derivatives are two, and both carry the one coupling.**

$$
D_{\imath}\xi_{f}=\partial_{\imath}\xi_{f}-ig_{4}\sum_{a}A_{a,\imath}\,\bigl(t_{a}\otimes\mathbb1_{2}\bigr)\xi_{f},
\qquad
D_{\imath}\Xi=\partial_{\imath}\Xi-ig_{4}\sum_{a}A_{a,\imath}\bigl[t_{a},\Xi\bigr].
$$

**The commutator on the scalar and the matrix on the fermion are the two ways one connection can act.** The scalar carries one line index up and one down, so the adjoint action is the only invariant derivative. **The fermion carries the quartet index and not the copy index**, hence $t_{a}\otimes\mathbb 1_{2}$: the copy index is a commutant and no generator sees it.

**The content is vector-like, and that is what makes the expression gauge-consistent.** It is $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$, so the cubic anomaly $\mathrm{Tr}\,[t_{a}\{t_{b},t_{c}\}]$ cancels between the $\mathbf4$ and the $\bar{\mathbf4}$ within one copy. **The cancellation is a property of the content and not of a coefficient**, and it is the reason no row above is adjusted to secure it. [The anomalies article](anomalies-and-anomaly-cancellation.html) states the condition and its solution.

**Rows $4$–$9$ are one potential: two quadratics and four quartics.** They are the invariant monomials of a Hermitian $4\times4$ matrix — the eleven monomials of the potential, the six zeros and the partition count $1,2,3,5$ are [the scalar article](five-quartics-and-three-cubics-above-m-c-what-a-four-by-four-matrix-admits.html)'s.

**Rows $10$ and $11$ are the tie the corpus writes.** Writing one matrix $y\,\bar\xi\Xi\xi$ sets $y'=\tfrac14y$. **The tie is a choice of coefficient and not a group-theoretic fact**, and [the Yukawa article](the-yukawa-block-above-m-c-two-matrices-eight-numbers-and-no-phase.html) prices it: eight numbers against two.

## The Interactions, Type by Type

**Seven types, and each one is read off a written row.**

| type | row | constant | realisations |
|---|---|---|---|
| $AAA$ | $1$ | $g_{4}$ | $80$ nonzero brackets of $105$ pairs |
| $AAAA$ | $1$ | $g_{4}^{2}$ | $120$ symmetric pairs |
| $\bar\xi A\xi$ | $2$ | $g_{4}$ | one $\gamma^{\imath}$, $15$ generators, two blocks |
| $A\Xi\Xi$ | $3$ | $g_{4}$ | $15$ |
| $AA\Xi\Xi$ | $3$ | $g_{4}^{2}$ | $120$ symmetric pairs |
| $\Xi\Xi\Xi\Xi$ | $6$–$9$ | $6$ | four monomials |
| $\bar\xi\xi\Xi$ | $10$, $11$ | $8$ | two structures |

**The fourth column counts arrays and not couplings.** $80$ is not eighty couplings and $120$ is not a hundred and twenty. **The coupling is one number in each row, and the arrays are the components the group forces it into.**

**Row $1$ carries both gauge vertices, and the ratio of their strengths is fixed.** Expanding the curvature,

$$
\tfrac14\operatorname{tr}F_{\imath\jmath}F^{\imath\jmath}
=\underbrace{\tfrac14\operatorname{tr}(\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath})^{2}}_{\text{propagator}}
+\underbrace{\tfrac12g_{4}\operatorname{tr}\bigl(\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}\bigr)[A^{\imath},A^{\jmath}]}_{AAA}
+\underbrace{\tfrac14g_{4}^{2}\operatorname{tr}[A_{\imath},A_{\jmath}][A^{\imath},A^{\jmath}]}_{AAAA}.
$$

**The triple vertex is one Lorentz structure and the count of nonzero structure constants.** $\mathrm{SU}(4)$ has $\binom{15}{2}=105$ pairs and **eighty of them do not commute**; the other twenty-five do. **The quartic is the square of the commutator**, so it exists because the triple does and its strength is fixed once the triple's is. **A theory with no triple vertex has no quartic one**, which is why the abelian factor below $M_C$ has neither.

**Row $2$ carries one gamma structure, and hence one vertex shape.** At dimension four the fermion bilinear can carry $\gamma^{\imath}$ and nothing else; the Pauli term is dimension five and belongs to the tower the census cuts off. **So the vertex is $\bar\xi_{f}\gamma_{\imath}t_{a}\xi_{f}$ with $f$ summed and the copy index absent.**

**Row $3$ produces two mixed vertices, and their realisations carry one generator index and two.**

$$
\operatorname{tr}(D_{\imath}\Xi)^{\dagger}(D^{\imath}\Xi)
=\underbrace{\operatorname{tr}(\partial_{\imath}\Xi)^{\dagger}(\partial^{\imath}\Xi)}_{\text{propagator}}
+\underbrace{2g_{4}\operatorname{Re}\operatorname{tr}\bigl(\partial_{\imath}\Xi\bigr)^{\dagger}\bigl[-iA^{\imath},\Xi\bigr]}_{A\Xi\Xi:\ 15}
+\underbrace{g_{4}^{2}\operatorname{tr}\bigl[A_{\imath},\Xi\bigr]^{\dagger}\bigl[A^{\imath},\Xi\bigr]}_{AA\Xi\Xi:\ 120}.
$$

**A hundred and twenty and not two hundred and twenty-five**, because $\operatorname{tr}[A_{a},\Xi]^{\dagger}[A_{b},\Xi]$ is symmetric in the pair and the antisymmetric part is absent. **The count of ordered pairs would be $15^{2}$; the count here is the symmetric pairs, $15\cdot16/2$.**

**Rows $6$–$9$ are one shape with four monomials, and the four-point scalar vertex carries the sum.** No vertex separates $\lambda_{1}$ from $\lambda_{2}$: the amplitude is $\lambda_{1}\mathcal{O}_{1}+\dots+\lambda_{4}\mathcal{O}_{4}$ on the four external legs. **Four constants stand behind that vertex and not six**, because rows $4$ and $5$ are quadratic and a quadratic monomial has no fourth derivative: $\partial^{4}(\mu_{\Phi}^{2}\operatorname{tr}\Xi^{2})=0$ identically. **The sector carries six in all** — two masses on the two-point vertices and four quartics on the four-point one — and the six are what the census counts as one block.

**Rows $10$ and $11$ are two structures and one vertex type.** The traceless contraction and the trace contraction have the same external fields, **so they are one shape in the Feynman rules and two rows in the ledger.** That is why eleven rows give seven types and not eleven.

## The Last Line

**Nineteen candidates and nineteen rows, and they are two different nineteens.**

$$
\underbrace{11+6+1+1}_{\text{candidates}}=19
\qquad\text{against}\qquad
\underbrace{11+6+2}_{\text{rows}}=19 .
$$

**The left is the census's ladder**: eleven written, six declared zero, one removed by canonical normalisation, one removed as a total derivative. **The right is the row count**: the same eleven, the same six zeros, and the two gauge rows the group does not act on. **The normalisation term and the vacuum angle are on one side and the fixing and the ghosts on the other, and each pair cancels** — which is why the two nineteens are equal and not the same.

**The fixing and the ghosts carry one parameter between them, and it is not physical.** $\zeta$ cancels from every observable, and the ghost's interactions belong to $\zeta$'s row and not to the eleven.

**The broken phase's complete Lagrangian omits both, and is right to.** [That expression](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html) is written in unitary gauge, which exists there because the Goldstones are eaten and the physical field basis is available. **A phase with no vacuum has no such basis**, so an unbroken Lagrangian carries the fixing and its ghosts or it cannot be used; and this is the one line on which the two complete expressions differ.

**$\theta_{4}$ carries no row.** The structure it multiplies is a total derivative, **so the fourth condition removed it before the row count began**, and the angle survives as a parameter of the theory with no piece in the expression. [The census](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html) states the removal; this article states the consequence for the ledger.

**The ledger therefore has three kinds of entry.** Fifteen parameters in the eleven rows, one in the fixing, and one in no row at all: **seventeen, of which fifteen multiply a row of the expression above.**

## The Closure

**The ladder's four rungs are four kinds of absence, and the article has now named each.**

**The third term is $(\partial_{\imath}\operatorname{tr}\Xi)^{2}$**, which the four conditions admit and canonical normalisation removes. **The fourth is $\theta_{4}$**, which the fourth condition removes. **Neither is a zero coefficient, and that is why the ladder has four rungs and not two.** The six zeros between them are [the boundary](the-boundary-of-the-list-above-m-c-the-bare-mass-the-cubics-and-theta-four.html)'s warrant, and they are a decline, a forced zero, one symmetry and one separate declaration rather than six decisions.

**The audit closes in both directions.** Every constant reaches a vertex and every vertex traces to a row.

$$
\{g_{4}\}\cup\{\mu_{\Phi}^{2},\mu_{2}^{2}\}\cup\{\lambda_{1},\dots,\lambda_{4}\}\cup\{y,y'\}=15 .
$$

**A count of appearances would give twenty-one** — [the audit](the-audit-above-m-c-every-constant-against-every-piece.html) does the sum — because one constant can reach several types. **The union gives fifteen, and fifteen is the number of constants the theory has.**

**Two controls.** $\theta_{4}$ reaches no vertex, **which is correct and not a failure**: its structure is a total derivative and carries no interaction. The ghost reaches a vertex that belongs to $\zeta$'s row and not to the eleven, **which is also correct**: a gauge choice produces its own interactions.

**What the closure cannot check.** It cannot check a value, a sign, or whether a structure nobody wrote exists. **It checks presence, row and power**, and it says so.

## What Is Not in It

**No term above dimension four.** No $F^{3}$, no Pauli term, no four-fermion term. **The cut is the census rule's and the tower above it is infinite**; [the boundary](the-boundary-of-the-list-above-m-c-the-bare-mass-the-cubics-and-theta-four.html) prices the first three.

**No bare fermion mass.** It is invariant and admissible, and it is declared zero; **the condensate is the one source of fermion mass the ledger holds.** That declaration is the model's most consequential and its most contestable, and the boundary states the trade.

**No vector mass.** It is forbidden and not declined: **a mass term for a connection in the adjoint of a simple group is not invariant.** The fifteen stay massless until a vacuum picks a direction, which is the restructuring's work and not this phase's.

**No scale.** $\mu_{\Phi}$ is a mass and not a vacuum expectation. **$M_C$ enters the expression nowhere**; it is the scale at which the Lagrangian above stops being the right description.

## Summary

**Eleven rows, seven interaction types, fifteen constants, and two gauge rows the group does not act on.** One coupling reaches five of the seven types because the covariant derivative sits in all three kinetic terms; the quartics and the Yukawa matrices are the reverse, four and eight constants behind one shape each, with the two masses on the two-point vertices and not on the four-point one.

**The closure is nineteen candidates against nineteen rows** — $11+6+1+1$ against $11+6+2$ — **and the audit is a union.** The controls are $\theta_{4}$, which reaches no vertex because its structure is a total derivative, and the ghost, which reaches a vertex that belongs to the gauge-fixing row.

**The expression is complete at dimension four and silent above it.** What it does not contain — the electroweak sector, the strong sector, flavour mixing beyond the two Yukawa structures, and every scale — is what the phase would have to acquire, and the article that lists those absences is the category's last.

## Summary of Notation

| symbol | meaning |
|---|---|
| $F_{a,\imath\jmath}$ | the curvature of generator $a$; $F_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a}$ |
| $t_{a}$ | the fifteen generators, $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $g_{4}$ | the one coupling, in rows $1$, $2$, $3$ |
| $\Xi$, $\Xi_{0}$ | the Hermitian $4\times4$ scalar and its traceless part |
| $\xi_{f}$ | the sixteen Weyl fields; $\alpha$ the copy index |
| $y$, $y'$ | the traceless and trace Yukawa matrices |
| $\zeta$ | the gauge parameter of $\mathcal{L}_{\mathrm{gf}}$ |
| $\theta_{4}$ | the vacuum angle, a parameter with no row |
| type | a distinct interaction shape |
| realisation | a distinct array carrying one type |

## Further Reading

- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html). The ladder that produces the eleven, and the row numbering used here.
- [The Audit Above $M_C$](the-audit-above-m-c-every-constant-against-every-piece.html). The same closure read by rows, with the failure modes.
- [The Gauge Self-Couplings Above $M_C$](the-gauge-self-couplings-above-m-c-aaa-aaaa-and-the-eighty-brackets.html). Row $1$ expanded, and the eighty brackets.
- [The Covariant Derivative Pieces Above $M_C$](the-covariant-derivative-pieces-above-m-c-fifteen-a-xi-xi-and-one-hundred-and-twenty-aa-xi-xi.html). Row $3$ expanded, and the $120$.
- [The Fermion–Connection Pieces Above $M_C$](the-fermion-connection-pieces-above-m-c-one-lorentz-structure-two-blocks-and-one-untouched-index.html). Row $2$, the two blocks and the inert copy index.
- [The Free Parts Above $M_C$](the-free-parts-above-m-c-three-kinetic-terms-one-derivative-and-one-coupling.html). Rows $1$, $2$ and $3$ as propagators, and the three coefficients that are not parameters.
- [The Two Masses Above $M_C$](the-two-masses-above-m-c-one-traceless-block-one-trace-and-no-third.html). Rows $4$ and $5$, the $\sqrt2$ of the trace mode, and the two masses that are absent.
- [The Boundary of the List Above $M_C$](the-boundary-of-the-list-above-m-c-the-bare-mass-the-cubics-and-theta-four.html). What the list leaves out, and which omission is a theorem.
