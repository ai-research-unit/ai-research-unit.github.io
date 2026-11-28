# __Five Quartics and Three Cubics Above $M_C$: What a $4\times4$ Matrix Admits and a Doublet Does Not__

## Introduction

**The question.** The scalar potential is eleven monomials. **Where does eleven come from, which of the eleven are written, and why does a doublet's potential have only two?**

**The answer.**

$$
\text{degrees }1,2,3,4:\quad 1,2,3,5\ \text{monomials};\qquad 1+2+3+5=11 .
$$

**A Hermitian $4\times4$ has eleven invariants at degree four or below. A doublet has two.** That factor of five and a half is the whole reason this phase's census is not shorter than the broken phase's.

## The Partition Count

**The invariant monomials of a Hermitian matrix at degree $d$ are the partitions of $d$ into at most four parts.**

| degree | partitions into $\le4$ parts | count |
|---|---|---|
| $1$ | $1$ | $1$ |
| $2$ | $2$; $1+1$ | $2$ |
| $3$ | $3$; $2+1$; $1+1+1$ | $3$ |
| $4$ | $4$; $3+1$; $2+2$; $2+1+1$; $1+1+1+1$ | $5$ |

**Why partitions of $d$.** An invariant is a product of traces, $\operatorname{tr}(\Xi^{k_{1}})\cdots\operatorname{tr}(\Xi^{k_{r}})$ with $k_{1}+\dots+k_{r}=d$. **Cayley--Hamilton makes $\operatorname{tr}\Xi^{k}$ independent only for $k\le4$**, so each part is at most $4$; and since $d\le4$ here, no part exceeds $d$ anyway. **The monomials are the partitions of $d$ into parts of size at most four**, which for $d\le4$ is the same list as partitions into at most four parts, and the count is the table.

**The count is a theorem and not a choice.** It is the Hilbert series of the invariant ring of a $4\times4$ Hermitian matrix under $\mathrm{U}(4)$ conjugation, **and $1,2,3,5$ is its coefficient sequence up to degree four.**

## The Eleven, Named

| degree | monomials | coefficient |
|---|---|---|
| $1$ | $\operatorname{tr}\Xi$ | $c$ (declared zero) |
| $2$ | $\operatorname{tr}\Xi^{2}$; $(\operatorname{tr}\Xi)^{2}$ | $\mu_{\Phi}^{2}$; $\mu_{2}^{2}$ |
| $3$ | $\operatorname{tr}\Xi^{3}$; $\operatorname{tr}\Xi^{2}\operatorname{tr}\Xi$; $(\operatorname{tr}\Xi)^{3}$ | $c_{1},c_{2},c_{3}$ (declared zero) |
| $4$ | $\operatorname{tr}\Xi^{4}$; $\operatorname{tr}\Xi^{3}\operatorname{tr}\Xi$; $(\operatorname{tr}\Xi^{2})^{2}$; $\operatorname{tr}\Xi^{2}(\operatorname{tr}\Xi)^{2}$; $(\operatorname{tr}\Xi)^{4}$ | $\lambda_{1}$–$\lambda_{4}$ and $\lambda_{5}$ (the fifth declared zero) |

**Four are written and seven carry declared or forced zeros.** The four quartics are $\operatorname{tr}\Xi^{4}$, $(\operatorname{tr}\Xi^{2})^{2}$, $\operatorname{tr}\Xi^{2}(\operatorname{tr}\Xi)^{2}$ and $(\operatorname{tr}\Xi)^{4}$; **the fifth, $\operatorname{tr}\Xi^{3}\operatorname{tr}\Xi$, is row $17$ with a zero coefficient.**

**The linear term is forced to zero and not declared.** A symmetric vacuum at $\Xi=0$ requires the gradient to vanish there, **and $\partial_{\Xi}\operatorname{tr}\Xi=\mathbb1\neq0$**, so $c=0$ follows from the vacuum and not from a convention. **That is why the census lists row $13$'s warrant as "forced" and rows $14$–$17$'s as "declared".**

## Why the Cubics Are Declared Zero

**Three cubics and one fifth quartic, and the reason is evenness.**

$$
\Xi\to-\Xi:\qquad
\operatorname{tr}\Xi^{3}\to-\operatorname{tr}\Xi^{3},
\qquad
\operatorname{tr}\Xi^{3}\operatorname{tr}\Xi\to-\operatorname{tr}\Xi^{3}\operatorname{tr}\Xi .
$$

**A potential even under $\Xi\to-\Xi$ excludes all three cubics and the fifth quartic at once**, and the reason is not aesthetic: **a $\mathbb Z_{2}$ on the scalar is what keeps the symmetric point a minimum with no cubic instability**, and it is the same discrete symmetry that makes the model's scalar sector renormalisable in the sense of having no cubic counterterm.

**"A potential with only quartics" is therefore a potential with a discrete symmetry**, and the census says so rather than presenting the zeros as a minimality principle.

**The fifth quartic is a separate declaration.** Evenness does not remove $\operatorname{tr}\Xi^{3}\operatorname{tr}\Xi$ at leading order in the same way — **it is odd under $\Xi\to-\Xi$ because $\operatorname{tr}\Xi^{3}$ is, so it is removed** — but the corpus declares it zero separately, **because a reader might restore the even symmetry and keep it.**

## What a Doublet Admits and This Does Not

**A doublet's potential has two monomials at degree four or below: $\phi^{\dagger}\phi$ and $(\phi^{\dagger}\phi)^{2}$.**

| object | degree $2$ | degree $4$ | total to degree $4$ |
|---|---|---|---|
| doublet | $1$ | $1$ | $2$ |
| $4\times4$ Hermitian | $2$ | $5$ | $7$ (+$1$+$3$ at degrees $1$ and $3$) |

**The difference is the number of independent traces.** A doublet's invariant is one real number $\phi^{\dagger}\phi$; **a matrix's invariants are traces of powers, and there are as many as there are partitions.**

**This is why eleven of the nineteen candidates are scalar monomials.** The scalar is not a bigger version of a doublet; **it is a different kind of object with a richer invariant ring**, and the census's size follows from that and not from adding fields.

## The Boundedness Condition

**The potential must be bounded below, and that is two conditions at the quartic level.**

$$
\lambda_{1}+\lambda_{2}\ge0,
\qquad
\lambda_{1}+4\lambda_{2}\ge0,
$$

**from $\tfrac14x^{2}\le s_{2}\le x^{2}$**, where $s_{2}=\operatorname{tr}\Xi^{2}$ and $x=\operatorname{tr}\Xi$. **The two binding directions are the identity and a single entry**, and [the boundedness article](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html) derives both.

**Boundedness is not a condition on admissibility.** A structure is admissible whether or not its coefficient keeps the potential bounded; **boundedness is a condition on the values, and it is checked on the values.**

## Checks

1. The partition count. $1,2,3,5$ at degrees $1$–$4$, so $11$.
2. The written quartics. Four, with the fifth declared zero.
3. The forced linear term. $\partial_{\Xi}\operatorname{tr}\Xi=\mathbb1\neq0$, so $c=0$ at a symmetric vacuum.
4. The evenness. $\Xi\to-\Xi$ removes three cubics and the fifth quartic.
5. The doublet comparison. Two monomials against eleven.
6. The boundedness. $\lambda_{1}+\lambda_{2}\ge0$ and $\lambda_{1}+4\lambda_{2}\ge0$.
7. The matrix split. $\operatorname{tr}\Xi^{2}=\operatorname{tr}\Xi_{0}^{2}+\tfrac14s^{2}$.

## Summary

**Eleven monomials because a Hermitian $4\times4$ has the invariant-ring counts $1,2,3,5$ at degrees one to four.** Four quartics are written, one is declared zero, three cubics are declared zero, and the linear term is forced to zero by the symmetric vacuum.

**A doublet admits two monomials and this matrix admits eleven**, which is why the unbroken phase's census is not shorter than the broken phase's despite having one force instead of four.

**Evenness under $\Xi\to-\Xi$ is the reason the cubics are absent**, and the article says so rather than presenting minimality as a principle.

## Summary of Notation

| symbol | meaning |
|---|---|
| $s$, $x$ | $\operatorname{tr}\Xi$ |
| $s_{2}$ | $\operatorname{tr}\Xi^{2}$ |
| $\lambda_{1}$–$\lambda_{4}$ | the four written quartic coefficients |
| $\lambda_{5}$, $c_{1}$–$c_{3}$, $c$ | the declared and forced zeros |

## Further Reading

- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The potential at working size.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html). The quartics in components and the boundedness cone.
- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html). The eleven potential rows.
- [The Coefficients Above $M_C$](the-coefficients-above-m-c-fifteen-constants-one-gauge-parameter-and-one-angle-without-a-row.html). The four quartics in the ledger.
- [The Canonical Basis Above $M_C$](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html). Why the zeros are basis statements.
