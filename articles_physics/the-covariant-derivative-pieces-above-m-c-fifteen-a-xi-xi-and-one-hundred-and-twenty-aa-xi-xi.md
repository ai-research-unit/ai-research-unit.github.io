# __The Covariant Derivative Pieces Above $M_C$: Fifteen $A\Xi\Xi$ and One Hundred and Twenty $AA\Xi\Xi$__

## Introduction

**The question.** Row $3$ is $\operatorname{tr}(D_{\imath}\Xi)^{\dagger}(D^{\imath}\Xi)$. **It is the only row in which the scalar and the connection meet, and it produces both of the mixed vertices.** How many, and why those numbers?

**The answer.**

$$
\boxed{\;A\Xi\Xi:\ 15,\qquad AA\Xi\Xi:\ 120\ \text{symmetric pairs}.\;}
$$

**Fifteen and not a hundred and twenty, and the difference is the difference between one generator and two.** The first is the count of generators; the second is the count of symmetric pairs of generators.

## The Expansion

$$
\operatorname{tr}(D_{\imath}\Xi)^{\dagger}(D^{\imath}\Xi)
=\operatorname{tr}(\partial_{\imath}\Xi)^{\dagger}(\partial^{\imath}\Xi)
+2g_{4}\operatorname{Re}\operatorname{tr}\bigl(\partial_{\imath}\Xi\bigr)^{\dagger}\bigl[-iA^{\imath},\Xi\bigr]
+g_{4}^{2}\operatorname{tr}\bigl[A_{\imath},\Xi\bigr]^{\dagger}\bigl[A^{\imath},\Xi\bigr].
$$

**Three terms: the scalar's own kinetic term, the one-connection vertex, and the two-connection vertex.** The coupling appears as $g_{4}$ and $g_{4}^{2}$, **and both are row $1$'s number.**

**The commutator is the structure and it is not a choice.** The group acts as $\Xi\to U\Xi U^{\dagger}$, so the covariant derivative must be a commutator, **$D_{\imath}\Xi=\partial_{\imath}\Xi-ig_{4}[A_{\imath},\Xi]$**; there is no other invariant way to couple a connection to a matrix in the adjoint-plus-singlet.

## The One-Connection Vertex: Fifteen

$$
\mathcal{L}_{A\Xi\Xi}=-2ig_{4}\,\operatorname{tr}\bigl(\partial_{\imath}\Xi\bigr)^{\dagger}\bigl[A^{\imath},\Xi\bigr].
$$

**One generator at a time, so the count is the count of generators: fifteen.**

**The vertex has one Lorentz structure and no derivative ambiguity.** The derivative sits on one scalar leg and the connection carries the vector index, **so the vertex is a two-scalar-one-vector object with a momentum on one scalar leg**; that is the whole shape and it is fixed.

**Fifteen is a realisation count.** It is how many distinct arrays the vertex can carry — one per generator — **and the coupling is $g_{4}$, which is one number.**

## The Two-Connection Vertex: One Hundred and Twenty

$$
\mathcal{L}_{AA\Xi\Xi}=g_{4}^{2}\operatorname{tr}\bigl[A_{\imath},\Xi\bigr]^{\dagger}\bigl[A^{\imath},\Xi\bigr].
$$

**Two generators enter through two commutators, and the contraction is symmetric in the pair.**

$$
\bigl[A_{a}t_{a},\Xi\bigr]=\bigl[X_{a}\otimes t_{a}\bigr]\Xi,
\qquad
\text{pairs }(a,b)\ \text{counted symmetrically:}\ \frac{15\cdot16}{2}=120 .
$$

**A hundred and twenty and not two hundred and twenty-five.** The commutator's square is symmetric under $a\leftrightarrow b$ because $\operatorname{tr}[A_{a},\Xi]^{\dagger}[A_{b},\Xi]$ is symmetric, **so the antisymmetric part is not there** and the count is the symmetric pairs.

**This is the article's one arithmetic point and it is the one most often got wrong.** A count of ordered pairs gives $15^{2}=225$; **the correct count is $120$**, and the difference is the antisymmetric hundred and five, which would be the contraction with $f_{abc}$ and does not appear because the scalar's coupling is a commutator squared and not a commutator.

## Why the Scalar Couples by a Commutator

**Four reasons, and they are one reason stated four ways.**

**Invariance.** $\Xi\to U\Xi U^{\dagger}$ and $A_{\imath}\to UA_{\imath}U^{\dagger}+(i/g_{4})U\partial_{\imath}U^{\dagger}$; **the combination $\partial_{\imath}\Xi-ig_{4}[A_{\imath},\Xi]$ transforms as $\Xi$ does**, and no other combination does.

**Hermiticity.** $\Xi$ is Hermitian, so $[A_{\imath},\Xi]$ is anti-Hermitian for Hermitian $A$, **and $\operatorname{tr}[A,\Xi]^{\dagger}[A,\Xi]$ is positive** — which is what makes the kinetic term a kinetic term.

**The trace.** The singlet in $\mathbf{15}\otimes\mathbf{15}$ is the trace, **so the only invariant contraction of two adjoint objects is $\operatorname{tr}(\cdot\,\cdot)$**, and the commutator's square is that contraction.

**The absence of a second coupling.** A term $\operatorname{tr}A_{\imath}\Xi A^{\imath}\Xi$ would be a different contraction of the same objects, **but it reduces to the commutator's square plus a total derivative**, so it is not independent.

## What Is Not Produced

**No $A\Xi$ vertex.** A single connection and a single scalar would need an invariant linear in $\Xi$ and in $A$, **and $\operatorname{tr}A_{\imath}\Xi$ vanishes because $\Xi$ contains a singlet and $A$ is traceless.** The linear-in-$\Xi$ term is row $13$, **declared zero and not produced by the covariant derivative.**

**No $\Xi\Xi\Xi$ from this row.** Three scalars and no connection come from the potential, **not from the derivative**, and the cubic is row $14$ with a zero coefficient.

**No derivative on the connection.** The vertex $A\Xi\Xi$ has its momentum on a scalar leg; **the $A\Xi\partial\Xi$ and $\partial A\Xi\Xi$ forms are the same vertex up to integration by parts**, and the census counts it once.

## The Vertex Count in One Place

| structure | type | count | coupling |
|---|---|---|---|
| $\operatorname{tr}(\partial\Xi)^{\dagger}(\partial\Xi)$ | propagator | $1$ | none |
| $\operatorname{tr}(\partial\Xi)^{\dagger}[A,\Xi]$ | $A\Xi\Xi$ | $15$ | $g_{4}$ |
| $\operatorname{tr}[A,\Xi]^{\dagger}[A,\Xi]$ | $AA\Xi\Xi$ | $120$ | $g_{4}^{2}$ |

**Two vertices from one row, and both carry row $1$'s coupling.** With the gauge self-couplings, **$g_{4}$ now reaches five vertex types** — the statement [the audit](the-audit-above-m-c-every-constant-against-every-piece.html) makes: **one number, five doors.**

## Checks

1. The expansion. Three terms: kinetic, $A\Xi\Xi$, $AA\Xi\Xi$.
2. The one-connection count. Fifteen, one per generator.
3. The two-connection count. $\binom{16}{2}=120$ symmetric pairs, not $225$.
4. The symmetry. $\operatorname{tr}[A_{a},\Xi]^{\dagger}[A_{b},\Xi]$ is symmetric in $a,b$.
5. The commutator. $D_{\imath}\Xi=\partial_{\imath}\Xi-ig_{4}[A_{\imath},\Xi]$, unique by invariance.
6. The absent terms. No $A\Xi$, no cubic, no independent $\operatorname{tr}A\Xi A\Xi$.
7. The coupling. $g_{4}$ and $g_{4}^{2}$, both row $1$'s.

## Summary

**Row $3$ produces two vertices: fifteen $A\Xi\Xi$ and a hundred and twenty $AA\Xi\Xi$.** The first is the count of generators; **the second is the count of symmetric pairs, and it is not two hundred and twenty-five because the commutator's square is symmetric.**

**The commutator coupling is forced, not chosen**: invariance, Hermiticity, the trace and the absence of a second independent contraction all point the same way.

**Both vertices carry row $1$'s coupling**, which is why $g_{4}$ reaches five of the seven vertex types and why one number is one force.

## Summary of Notation

| symbol | meaning |
|---|---|
| $D_{\imath}\Xi$ | $\partial_{\imath}\Xi-ig_{4}[A_{\imath},\Xi]$ |
| $a,b$ | generator indices, $1,\dots,15$ |
| symmetric pairs | $(a,b)$ with $a\le b$; $\binom{16}{2}=120$ |

## Further Reading

- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html). Row $3$ and the scalar kinetic pair.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html). The scalar sector in components.
- [The Gauge Self-Couplings Above $M_C$](the-gauge-self-couplings-above-m-c-aaa-aaaa-and-the-eighty-brackets.html). The other two $g_{4}$ vertices.
- [The Audit Above $M_C$](the-audit-above-m-c-every-constant-against-every-piece.html). $g_{4}$'s five doors.
- [The Canonical Basis Above $M_C$](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html). The trace split of this same row.
