# __The Gauge Self-Couplings Above $M_C$: $AAA$, $AAAA$ and the Eighty Brackets__

## Introduction

**The question.** Row $1$ is one number, $\tfrac14\operatorname{tr}F_{\imath\jmath}F^{\imath\jmath}$. **What interactions does one number contain?** This article expands the row and counts them.

**The answer.** Two types and five structures.

$$
\boxed{\;\tfrac14\operatorname{tr}F^{2}\ \longrightarrow\ AAA\ \text{and}\ AAAA,\qquad
80\ \text{nonzero brackets of } 105\ \text{pairs}.\;}
$$

**One coupling, three-point and four-point vertices, and no free parameter anywhere in the expansion.** The vertex strengths are the structure constants, and **the structure constants are the group's and not the author's.**

## The Expansion

**The field strength is $F_{\imath\jmath}=\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}-ig_{4}[A_{\imath},A_{\jmath}]$, and squaring it gives three terms.**

$$
\tfrac14\operatorname{tr}F_{\imath\jmath}F^{\imath\jmath}
=\underbrace{\tfrac14\operatorname{tr}(\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath})^{2}}_{\text{kinetic}}
+\underbrace{\tfrac12g_{4}\operatorname{tr}\bigl(\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}\bigr)[A^{\imath},A^{\jmath}]}_{AAA}
+\underbrace{\tfrac14g_{4}^{2}\operatorname{tr}[A_{\imath},A_{\jmath}][A^{\imath},A^{\jmath}]}_{AAAA}.
$$

**The first term is the propagator and carries no coupling.** The second and third carry $g_{4}$ and $g_{4}^{2}$; **their ratio is fixed by the same number**, which is what "one coupling" means at the level of Feynman rules.

**The factor $\tfrac14$ is not arbitrary.** It is $\tfrac14$ because $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ and the field strength carries two generators: **$\tfrac14\cdot\tfrac12\cdot2=\tfrac14$ for the canonical normalisation**, and [the kinetic terms' article](the-lagrangian-and-the-primordial-force.html) derives it rather than positing it.

## The Triple Vertex

**Written with the structure constants showing.**

$$
\mathcal{L}_{AAA}=g_{4}f_{abc}\,\bigl(\partial_{\imath}A_{a,\jmath}\bigr)A_{b}^{\imath}A_{c}^{\jmath},
$$

**one Lorentz structure and fifteen generators.** The vertex is antisymmetric in all three legs, because $f_{abc}$ is totally antisymmetric and the derivative sits on one leg only.

**The count is the count of nonzero structure constants.** $\mathrm{SU}(4)$ has fifteen generators and $\binom{15}{2}=105$ pairs; **eighty of those pairs have a nonzero commutator and twenty-five commute.** The eighty are the triple vertices' content, **and the twenty-five are the Cartan directions plus the pairs whose commutator vanishes.**

**Eighty is a realisation count and not an operator count.** It is the number of distinct arrays the vertex can carry; **it is one Lorentz structure with eighty group components**, and a reader who read it as eighty independent couplings would be counting the group's dimension as the theory's freedom.

## The Quartic Vertex

**One Lorentz structure, and the count is pairs of generators.**

$$
\mathcal{L}_{AAAA}=\tfrac14g_{4}^{2}f_{abe}f_{cde}\,A_{a}^{\imath}A_{b}^{\jmath}A_{c,\imath}A_{d,\jmath},
$$

**with $f_{abe}f_{cde}$ symmetric under the exchange of the two pairs.** The number of distinct such contractions is the number of symmetric pairs,

$$
\frac{15\cdot16}{2}=120 .
$$

**One hundred and twenty is again a realisation count.** It is the component count in the expansion, **and it is not a hundred and twenty quartic couplings**; the coupling is $g_{4}^{2}$ and there is one of it.

**The quartic is the triple vertex squared, and that is the group's statement.** In a non-abelian theory the four-point vertex exists because the three-point one does: **$[A,A]^{2}$ is the square of $[A,A]$**, and its strength is fixed once the triple's is. **An abelian theory has neither**, which is why QED's photon has no self-coupling and this connection does.

## What Is Not There

**No $d_{abc}$ term at dimension four.** A symmetric structure constant $d_{abc}$ could in principle appear, **but in $\mathrm{SU}(4)$ the totally symmetric invariant at dimension four is not available for the cubic**, and the trace $\operatorname{tr}\{t_{a},t_{b}\}t_{c}$ vanishes for $\mathrm{SU}(N)$ with $N\ge3$ in the fundamental.

**No $F^{3}$ and no Pauli term.** Both are dimension five or six and **the census stops at four**; [the boundary article](the-boundary-of-the-list-above-m-c-the-bare-mass-the-cubics-and-theta-four.html) prices them.

**No photon and no gluon.** Above $M_C$ there is one connection and no residual subgroup; **the eight gluons and the photon are what the restructuring leaves behind**, and [the force content](the-force-content-of-the-su4-model-one-connection-a-nine-dimensional-kernel-and-rank-five.html) says which kernel produces which.

## The Vertex Count in One Place

| structure | type | count | coupling |
|---|---|---|---|
| $\operatorname{tr}(\partial A)^{2}$ | propagator | $1$ | none |
| $f_{abc}\,\partial A\,A\,A$ | $AAA$ | $80$ components | $g_{4}$ |
| $f_{abe}f_{cde}\,A^{4}$ | $AAAA$ | $120$ pairs | $g_{4}^{2}$ |

**Three structures, two vertices, one coupling.** The row that carries them is row $1$, **and it is the row with the largest downstream vertex content in the whole census**: five of the seven vertex types in [the tally](the-audit-above-m-c-every-constant-against-every-piece.html) trace to $g_{4}$.

## Why This Is One Force

**The triple and quartic vertices are not two interactions.** They are the two orders at which one field strength's square is nonlinear, **and their strengths are related by the same $g_{4}$**: the quartic is $g_{4}^{2}$ because the cubic is $g_{4}$ and the square of a bracket carries the square of the coupling.

**The relation is testable and is the theory's signature.** A model with independent triple and quartic couplings would have two numbers where this has one; **measuring their ratio tests whether the connection is a connection** — that is, whether it is a gauge field at all.

**And the eighty is a property of $\mathrm{SU}(4)$.** A different group would give a different bracket count with the same structure, **so the eighty is the group's fingerprint at the triple vertex**, and [the counts article](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html) collects it with the others.

## Checks

1. The expansion. Three terms: kinetic, $AAA$, $AAAA$.
2. The coupling powers. $g_{4}^{0}$, $g_{4}^{1}$, $g_{4}^{2}$.
3. The brackets. $\binom{15}{2}=105$ pairs, $80$ nonzero, $25$ commuting.
4. The quartic. $\binom{16}{2}=120$ symmetric pairs.
5. The factor. $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$, giving $\tfrac14$ on $\operatorname{tr}F^{2}$.
6. The absence. No $d_{abc}$ cubic for $\mathrm{SU}(N)$, $N\ge3$, in the fundamental.
7. The ratio. Quartic over cubic squared is fixed: one coupling, not two.

## Summary

**One row, $\tfrac14\operatorname{tr}F^{2}$, contains a propagator, a triple vertex and a quartic vertex, with couplings $1$, $g_{4}$ and $g_{4}^{2}$.** The triple vertex carries the eighty nonzero structure constants of a hundred and five pairs; **the quartic carries a hundred and twenty symmetric pairs.**

**Both counts are realisation counts and neither is a count of couplings.** There is one coupling, **and the quartic's strength is the cube's squared** — which is what makes the connection a gauge field rather than three unrelated interactions.

**The eighty is $\mathrm{SU}(4)$'s fingerprint, and the absence of a photon and a gluon above $M_C$ is the statement that no residual subgroup has formed yet.**

## Summary of Notation

| symbol | meaning |
|---|---|
| $F_{\imath\jmath}$ | the field strength, $\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}-ig_{4}[A_{\imath},A_{\jmath}]$ |
| $f_{abc}$ | the totally antisymmetric structure constants of $\mathrm{SU}(4)$ |
| $d_{abc}$ | the symmetric invariant; absent at dimension four for $\mathrm{SU}(4)$ |
| realisation count | distinct arrays a vertex carries; not a count of couplings |

## Further Reading

- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html). Row $1$ in the eleven.
- [The Feynman Rules of the $\mathrm{SU}(4)$ Model](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The vertices as rules.
- [The Counts of the Fifteen](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html). The generator arithmetic.
- [The Force Content of the $\mathrm{SU}(4)$ Model](the-force-content-of-the-su4-model-one-connection-a-nine-dimensional-kernel-and-rank-five.html). Where the residual groups come from.
- [The Audit Above $M_C$](the-audit-above-m-c-every-constant-against-every-piece.html). $g_{4}$'s five doors.
