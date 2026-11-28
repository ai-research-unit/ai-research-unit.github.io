# __The Free Parts Above $M_C$: Three Kinetic Terms, One Derivative and One Coupling__

## Introduction

**The question.** Rows $1$, $2$ and $3$ are the only rows of the eleven that carry no parameter. **What fixes their coefficients, and what does each of them propagate?**

**The answer.**

$$
\boxed{\;-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}\;\equiv\;-\tfrac12\operatorname{tr}F_{\imath\jmath}F^{\imath\jmath},\qquad
+\sum_{f=1}^{16}\bar\xi_{f}\,i\gamma_{\imath}D_{\imath}\xi_{f},\qquad
+\operatorname{tr}\bigl(D_{\imath}\Xi\bigr)^{\dagger}\bigl(D^{\imath}\Xi\bigr).\;}
$$

**Three coefficients, $\tfrac14$, $1$ and $1$, and none of them is a choice.** Each is fixed by the demand that one real component of one field propagate canonically, **and the three numbers differ because the three fields carry different multiplicities of the trace**: the curvature carries two generators, the fermion carries none, and the scalar carries one index of each kind.

**What "free" means here, and what it does not.** A free part is the quadratic piece of a row — the part that produces a propagator and no vertex. **Rows $1$ and $3$ are not free in that sense**: the same two rows produce the $AAA$, $AAAA$, $A\Xi\Xi$ and $AA\Xi\Xi$ vertices, which [the covariant-derivative article](the-covariant-derivative-pieces-above-m-c-fifteen-a-xi-xi-and-one-hundred-and-twenty-aa-xi-xi.html) and [the gauge article](the-gauge-self-couplings-above-m-c-aaa-aaaa-and-the-eighty-brackets.html) count. **This article reads only the quadratic part of each**, and the interactions are those articles' subject.

**The scope sentence.** Above $M_C$ there is no vacuum, so no field has a mass, and "free" therefore means *kinetic*. **A free part with a mass term in it is a broken-phase object**, and [the two masses](the-two-masses-above-m-c-one-traceless-block-one-trace-and-no-third.html) is where the three quadratic potentials of this phase are read.

## The Three Rows

| row | piece | coefficient | propagates | real components |
|---|---|---|---|---|
| $1$ | $-\tfrac14\sum_a F_a F_a$ | $\tfrac14$ | fifteen vectors | $30$ |
| $2$ | $+\sum_f\bar\xi_i\gamma D\xi$ | $1$ | sixteen Weyl fields | $32$ |
| $3$ | $+\operatorname{tr}(D\Xi)^{\dagger}(D\Xi)$ | $1$ | one Hermitian matrix | $16$ |

**One coupling sits in all three**, because the covariant derivative sits in rows $2$ and $3$ and the curvature is the derivative of the connection in row $1$. **So the free parts already contain every interaction of the category that carries a derivative**, and the table is the reason [the audit](the-audit-above-m-c-every-constant-against-every-piece.html) finds $g_{4}$ in five of the seven vertex types.

## Row 1: The Fourth, and the Factor of Two Between Two Bases

**The coefficient is $\tfrac14$ on the component sum and $\tfrac12$ on the trace, and the two statements are the same number.**

$$
\operatorname{tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr)
=\tfrac12\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath},
\qquad F_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a},
\qquad \operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}.
$$

**So $-\tfrac14\sum FF=-\tfrac12\operatorname{tr}FF$, and a display written $-\tfrac14\operatorname{tr}FF$ is half the canonical value.** The factor of two is the trace norm and not a convention of sign or of metric: **an article that writes $\tfrac14$ in front of a trace has either halved its fields or doubled its coupling**, and the only defence is to print the normalisation in the same display as the coefficient.

**Why $\tfrac14$ is canonical.** The quadratic part of the row is

$$
-\tfrac14\sum_{a,\mu,\nu}\bigl(\partial_{\mu}A_{a,\nu}-\partial_{\nu}A_{a,\mu}\bigr)^{2}
=-\tfrac12\sum_{a,\mu,\nu}\bigl(\partial_{\mu}A_{a,\nu}\bigr)^{2}
+\tfrac12\sum_{a}\bigl(\partial\cdot A_{a}\bigr)^{2}
+\text{total derivative},
$$

**which is $\tfrac12$ of $(\partial A)^{2}$ per real component and per Lorentz index — the canonical normalisation of a real vector, fifteen times over.** The $30$ real components are $15\times4$, and each of them is canonical once the coefficient is $\tfrac14$ on the sum. **Change the coefficient and the fifteen cease to be canonical together**, which is why the number is fixed by one requirement and not fifteen.

**The basis in which the same physics needs $\tfrac18$.** Written with the printed arrays $G_{a}$ instead of the normalised $t_{a}$, the trace norms are $2$ on the fifteen and $12$ on the vacuum direction, **so the coefficient is not $\tfrac14$ and not $\tfrac18$ uniformly**: the printed frame is not orthonormal, and a coefficient that works on the fifteen fails on the corner. **That is why every vertex of this category is read from $t_{a}$**, and why [the primordial action](the-lagrangian-and-the-primordial-force.html) fixes the passage from the printed arrays to $t_{a}$ once, in one rescaling and one rotation of the diagonal frame.

**What the row does not carry.** No mass: a term $\operatorname{tr}A_{\mu}A^{\mu}$ is invariant under a global transformation and **not under a local one**, since $A_{\mu}\mapsto UA_{\mu}U^{\dagger}+\tfrac{i}{g}U\partial_{\mu}U^{\dagger}$ turns the quadratic form into something else. **No cubic $F^{3}$**: the curvature carries dimension two, so the cube carries six. **No derivative of the curvature**: dimension five. **And no $\theta_{4}$**: the topological density is a total derivative and the fourth condition excluded it, which is why [the complete Lagrangian](the-complete-lagrangian-above-m-c-eleven-structures-seven-vertex-types-and-fifteen-constants.html) prints it on the last line and not among the eleven.

## Row 2: The Fermion, and Why There Is No Half

**A fermion has no $\tfrac12$ because it has no real component to halve.** A real scalar needs $\tfrac12(\partial\phi)^{2}$ so that its conjugate momentum is $\dot\phi$; **a Grassmann field's kinetic term already carries the right coefficient at $1$**, and the two-component form makes the point in one line:

$$
+\sum_{f=1}^{16}\xi_{f}^{\dagger}\,i\bar\sigma^{\imath}D_{\imath}\,\xi_{f},
\qquad
D_{\imath}\xi_{f}=\partial_{\imath}\xi_{f}-ig_{4}A_{a,\imath}\bigl(t_{a}\otimes\mathbb 1_{2}\bigr)\xi_{f}.
$$

**The coefficient is one and the field is complex, and the two facts belong together**: a complex field has two real components and a first-order equation, so the $\tfrac12$ that a real second-order field needs has nowhere to go.

**The sixteen are $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$, and the covariant derivative is block-diagonal on that split.** The quartet half carries $t_{a}\otimes\mathbb 1_{2}$ and the conjugate half carries $-t_{a}^{T}\otimes\mathbb 1_{2}$; **the minus is not a convention** — a $\bar{\mathbf4}$ transforms with the transpose-inverse, and a vertex that forgot it would give the $\mathrm{SU}(4)^{3}$ index $+4$ instead of $0$. **The copy index is untouched by every generator**, which is the one structural statement the row makes: the algebra acts on the quartet index alone, and the commutant of that action is where the family lives.

**What the row does not carry.** No mass, no chirality projection, no second structure of any kind. **A mass is $m\bar\xi\xi$, it is invariant because the content is vector-like, and it is row $12$ with a zero coefficient** — [the boundary](the-boundary-of-the-list-above-m-c-the-bare-mass-the-cubics-and-theta-four.html) prices the decline. **A kinetic term is not allowed to supply what a mass supplies**, and a reader who expects the free parts to fix the fermion masses will find them in the Yukawa block instead, one scale later.

## Row 3: The Scalar, and the Half the Trace Supplies

**The coefficient is $1$ and the fifteen components are canonical because the trace supplies the $\tfrac12$.** Writing $\Xi=\chi_{a}t_{a}+\tfrac14 s\,\mathbb 1$ with $s\equiv\operatorname{tr}\Xi$,

$$
\operatorname{tr}\bigl(\partial_{\imath}\Xi\bigr)^{2}
=\tfrac12\sum_{a}\bigl(\partial_{\imath}\chi_{a}\bigr)^{2}
+\tfrac14\bigl(\partial_{\imath}s\bigr)^{2},
$$

**and the cross term is absent because $\operatorname{tr}t_{a}=0$** — the traceless part and the trace are orthogonal under the trace form, which is the same statement as the decomposition being canonical.

**The fifteen are canonical at coefficient $1$, and the trace is not.** $\tfrac14(\partial s)^{2}$ is $\tfrac12(\partial\tau)^{2}$ for $\tau\equiv s/\sqrt2$, **so the canonical trace field is $\operatorname{tr}\Xi/\sqrt2$ and not $\operatorname{tr}\Xi$.** The distinction is worth a display because it is where a factor of two goes missing:

$$
\tfrac14\bigl(\partial\operatorname{tr}\Xi\bigr)^{2}=\tfrac12\Bigl(\partial\tfrac{\operatorname{tr}\Xi}{\sqrt2}\Bigr)^{2}.
$$

**So "the scalar carries no $\tfrac12$" is a true sentence about the fifteen and an incomplete one about the trace**: the fifteen are canonical at coefficient $1$ because $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$, and the trace mode needs the $\sqrt2$ before it can be compared with anything. [The two masses](the-two-masses-above-m-c-one-traceless-block-one-trace-and-no-third.html) uses the canonical $\tau$ when it quotes $\mu_{\Phi}^{2}+4\mu_{2}^{2}$ on the trace; **in the $s$ coordinate the same mass reads $2(\mu_{\Phi}^{2}/4+\mu_{2}^{2})$**, and the two numbers differ by exactly the $\sqrt2$ printed above.

**A second kinetic term exists and is not written.** $c\,(\partial\operatorname{tr}\Xi)^{2}$ is invariant, dimension four, and admissible; **the census counts it at the rung below** and [the canonical basis](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html) removes it with one rescaling of the trace mode. **The coefficient $1$ in row $3$ is therefore a choice of basis and not a group-theoretic fact**: it is the basis in which $c=0$, and the price is that four potential coefficients and one Yukawa matrix move when the basis changes.

**What the row does not carry.** No mass, no quartic, no derivative of $s$ alone. **And no potential**: rows $4$–$9$ are affine in $V(\Xi)$ and carry no derivative at all, which is why they produce masses and vertices and never a propagator's momentum dependence.

## What the Free Parts Do Not Carry

**No mass, for any field.** The fifteen vectors cannot have one and the sixteen fermions decline one; the scalar's two masses are rows $4$ and $5$, and they are potential terms.

**No ghost kinetic term among the eleven.** $-\partial\bar c Dc$ exists and is the ghost's, and it belongs to the gauge-fixing row that [the complete Lagrangian](the-complete-lagrangian-above-m-c-eleven-structures-seven-vertex-types-and-fifteen-constants.html) prints on its last line. **A free part is a row of the eleven, and the ghost is not one.**

**No $\tfrac12$ that is not a trace, and no $2$ that is not a $\mathrm{U}(1)$.** The three coefficients are $\tfrac14$, $1$, $1$; a display with $\tfrac12$ on the fermion, or with $\tfrac12$ on the scalar's trace mode, **has moved a normalisation into a coefficient**, and the count of parameters will not show it.

## The Three Propagators

**What each free part buys, in the covariant gauge of the last line.**

| field | quadratic part | propagator |
|---|---|---|
| $A_{a,\mu}$, fifteen | $-\tfrac14(\partial_{\mu}A_{a,\nu}-\partial_{\nu}A_{a,\mu})^{2}$ | $-i\delta_{\mu\nu}/k^{2}$ at $\zeta=1$ |
| $\xi_{f}$, sixteen | $i\xi^{\dagger}\bar\sigma^{\imath}\partial_{\imath}\xi$ | $i\bar\sigma\cdot k/k^{2}$ |
| $\chi_{a}$, fifteen | $\tfrac12(\partial\chi_{a})^{2}$ | $i/k^{2}$ |
| $\tau=\operatorname{tr}\Xi/\sqrt2$ | $\tfrac12(\partial\tau)^{2}$ | $i/k^{2}$ |

**Four propagators from three rows, and the fourth is the trace mode that row $3$ contains without naming it.** The scalar counts as sixteen real fields and not as fifteen, which is the same count the census makes when it says the content is fifteen connections, sixteen Weyl fields and one Hermitian scalar.

## Summary

**Three rows, three coefficients, one coupling, and no parameter of their own.** $\tfrac14$ on the component sum is $\tfrac12$ on the trace and is fixed by the canonical normalisation of fifteen real vectors; $1$ on the fermion is fixed by the Grassmann field being complex; $1$ on the scalar is fixed by $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$, which supplies the $\tfrac12$ for the fifteen and leaves the trace mode a $\sqrt2$ short of canonical.

**Two facts about these rows are choices and the rest are not.** The coefficient $1$ in row $3$ is the basis in which the second kinetic term $(\partial\operatorname{tr}\Xi)^{2}$ is absent, and that basis is [the census](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html)'s rung. **Everything else is a trace norm.**

## Summary of Notation

| symbol | meaning |
|---|---|
| $F_{a,\imath\jmath}$ | curvature of generator $a$; $F_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a}$ |
| $t_{a}$ | the fifteen generators, $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |
| $G_{a}$ | the printed arrays, trace norms $2$ and $12$; not orthonormal |
| $\chi_{a}$ | the fifteen coordinates of $\Xi_{0}$ on $t_{a}$ |
| $s$, $\tau$ | $s=\operatorname{tr}\Xi$; $\tau=s/\sqrt2$, the canonical trace field |
| $\xi_{f}$ | the sixteen Weyl fields, quartet index slow and copy index fast |
| $\zeta$ | the gauge parameter of the fixing row, absent from the eleven |

## Further Reading

- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html). The eleven rows and the rungs that produce them.
- [The Content Above $M_C$](the-content-above-m-c-fifteen-connections-sixteen-weyl-fields-and-one-hermitian-scalar.html). The fields these rows propagate.
- [The Canonical Basis](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html). The rescaling that removes the second kinetic term and the four costs.
- [The Gauge Self-Couplings](the-gauge-self-couplings-above-m-c-aaa-aaaa-and-the-eighty-brackets.html). What row $1$ contains beyond its propagator.
- [The Two Masses](the-two-masses-above-m-c-one-traceless-block-one-trace-and-no-third.html). The quadratic potential, which is where the $\sqrt2$ pays off.
- [The Complete Lagrangian](the-complete-lagrangian-above-m-c-eleven-structures-seven-vertex-types-and-fifteen-constants.html). The three rows in place.
