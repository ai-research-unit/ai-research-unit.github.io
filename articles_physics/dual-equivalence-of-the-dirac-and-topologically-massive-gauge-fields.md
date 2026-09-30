# __Dual Equivalence of the Dirac and Topologically Massive Gauge Fields__

## Introduction

A massive spin-1 field can acquire its mass in more than one way. The **Proca** term gives the field a second-order kinetic operator and a mass by hand. A **topological** mass term gives the field a first-order, Levi-Civita-weighted term and a mass that comes from the antisymmetric structure of spacetime rather than from a scalar coupling; in $2+1$ dimensions this is the Chern–Simons mass of Deser, Jackiw and Templeton, and in four dimensions the analogous term is the $\varepsilon FF$- or BF-type term. Liu Yu-Fen's thesis is that a single *first-order* (parent) action carries both descriptions: eliminating one field gives the Dirac Lagrangian of a massive spin-$\frac{1}{2}$ field, and eliminating the other gives the Lagrangian of a topologically massive spin-1 field. The two theories are then **dual** — two descriptions of the same propagating degrees of freedom.

This article records that equivalence and the machinery it uses. It is the physics companion of *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form* and of *Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form*: the parent action is written in the s-vector variables, and the two eliminations pass through the self-dual field strength and the cubic (order-three ding) form of those articles.

**Scope and honesty.** The construction is Liu's. What this article does is state the equivalence, its mechanism, and the role of the corpus's verified identities in it; it does **not** claim to have independently recomputed the variational eliminations. Where a statement is the source's and rests on an elimination this pass did not perform, the article says so, both here and in the companion `.context` file. The algebraic identities that the equivalence *uses* — the normed condition, the associativity, the bilinear dictionary, the anti-self-duality of $H^{\mu\nu}$, and the Chern–Pontryagin density being a total derivative — are verified in the companion articles.

The conventions are those of the companion articles: four-vector indices $\mu = 0,1,2,3$ carry the generator metric $g_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$; $\varepsilon^{\mu\nu\lambda\rho}$ is totally antisymmetric with $\varepsilon^{0123} = 1$; and the structure constants $c^{\mu\nu\lambda}$ and $\check c^{\mu\nu\lambda}$ are those of the s-vector article.

## The Parent Action

### The Idea

A dual equivalence between two second-order theories is usually exhibited by a **first-order** action, linear in the field strength, with an auxiliary field that can be eliminated in two ways. The prototypical example is the equivalence between the Maxwell action $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ and its first-order form $\tfrac12 B^{\mu\nu}(\partial_\mu A_\nu - \partial_\nu A_\mu) - \tfrac18 B_{\mu\nu}B^{\mu\nu}$, whose elimination of $B$ gives Maxwell and whose elimination of $A$ gives the dual (magnetic) Maxwell theory. Liu's construction is the same move with the s-vector as the basic field, and the auxiliary field being the antisymmetric part of the biquaternion:

$$
S_{\text{parent}}[G, A] = \int \tfrac12\Bigl[G^*_\nu\, i\check c^{\nu\mu\lambda}\,\tilde\nabla_\mu G_\lambda - \bigl(\tilde\nabla_\mu G_\nu\bigr)^* i\check c^{\nu\mu\lambda} G_\lambda\Bigr] + S_{\text{aux}}[G, A],
$$

the first two terms being the bosonic kinetic form of the s-vector article and $S_{\text{aux}}$ the term that carries the antisymmetric (field-strength) field. The essential property is that the *same* $\check c$ that defines the kinetic operator also defines the auxiliary field's transformation, so the two eliminations are the two ways of inverting one linear system.

### The Two Eliminations

Eliminating the auxiliary field leaves the **Dirac Lagrangian** in the vector representation,

$$
\mathcal{L}_D = \tfrac12\Bigl[\bigl(\tilde\nabla_\mu G_\nu\bigr)^* i\check c^{\nu\mu\lambda} G_\lambda - G^*_\nu\, i\check c^{\nu\mu\lambda}\, \tilde\nabla_\mu G_\lambda + m\bigl(G^{*}_\nu G^{*\nu} + G_\nu G^\nu\bigr)\Bigr],
$$

whose mass term $m(G^*G^* + GG)$ couples $G$ to $G^*$ — the chirality-off-diagonal mass, and the reason the s-vector is not simply a pair of independent complex vectors. Eliminating $G$ instead leaves a **second-order gauge Lagrangian** for the field $A_\mu$, with a mass term built from the antisymmetric symbol,

$$
\mathcal{L}_G = -\tfrac14 F_{\mu\nu}F^{\mu\nu} + \tfrac{m}{4}\,\varepsilon^{\mu\nu\lambda\rho}F_{\mu\nu}A_\lambda,
$$

the second term being the topological (Chern–Simons-type / BF-type) mass. The two Lagrangians describe the same propagating modes.

**Attribution.** The specific form of $S_{\text{aux}}$, the precise field content of the gauge sector, and the dimension in which the topological mass lives are the source's; the display above is the structure the equivalence has, and the reader should take the two Lagrangian *shapes* — a Dirac kinetic-plus-chirality-off-diagonal-mass form, and a Maxwell-plus-topological-mass form — as the content, not the exact coefficients of $S_{\text{aux}}$. The coefficient $m/4$ and the sign of the topological term are recorded from the source.

## The Machinery the Equivalence Uses

### The Self-Dual Field Strength

The equivalence passes through the antisymmetric part of the biquaternion, which is the field strength of the s-vector. In the companion article the two-form

$$
H^{\mu\nu} = G^*_\lambda\, \check c^{\lambda\mu\nu}
$$

is shown to be anti-self-dual, $H^{\mu\nu} = -\tfrac{i}{2}\varepsilon^{\mu\nu\lambda\rho}H_{\lambda\rho}$. The self-duality means that the auxiliary field carries only the three complex independent components of its antisymmetric part: a biquaternion has four complex components (scalar, three-vector), the symmetric part of $H$ is proportional to the metric, and the antisymmetric part is anti-self-dual. The parent action's elimination is therefore an elimination of a self-dual two-form, which is exactly the structure a topological mass term needs.

### The Chern–Pontryagin Density as a Total Derivative

The second ingredient is that the next-to-topological density is a total derivative. In the s-vector variables,

$$
\tfrac14\bigl[G_{\mu\nu}\varepsilon^{\mu\nu\lambda\rho}G_{\lambda\rho} + G^*_{\mu\nu}\varepsilon^{\mu\nu\lambda\rho}G^*_{\lambda\rho}\bigr]
= 2\partial_\mu\Bigl[\varepsilon^{\mu\nu\lambda\rho}\bigl(B_\nu\partial_\lambda B_\rho - N_\nu\partial_\lambda N_\rho + 2mB_\nu N_\lambda j_\rho\bigr)\Bigr],
$$

where $B$ and $N$ are the two real four-vectors of the semi-spinors (the real and imaginary parts of $G$). The right-hand side is the divergence of a Chern–Simons-type current. A total derivative may be added to a Lagrangian without changing the equations of motion, and it is this freedom that lets the parent action carry the topological mass into the gauge reduction and out of the Dirac reduction. The identity is transcribed from the source; the corresponding *algebraic* statements that would establish it — the self-duality of $H$ and the structure of the cubic form — are verified in the companion articles, but the divergence identity itself was not recomputed in this pass.

### The Mass as a Non-Integrable Phase

The third ingredient is the reading of the mass. In the vector representation the mass term is

$$
m\,\bar\Psi\Psi = \tfrac{m}{2}\bigl(N_\nu N^\nu - B_\nu B^\nu\bigr) = \bar\Psi\, K_\mu\gamma^\mu\Psi
$$

for a unit complex vector $K^\mu$ built from the field. The mass is a unit vector, hence a **phase**, and the phase is *non-integrable*: it cannot be removed by a gauge transformation of the s-vector. The topological mass of the gauge field and the non-integrable mass of the Dirac field are read as the same object in the two reductions — a mass that is a phase rather than a scalar. This reading is the source's and is recorded, with the companion article *The Dirac Equation in Biquaternionic Form* carrying the same element.

## What the Equivalence Is and Is Not

**It is** a *strong–weak* or *electric–magnetic*-type duality: two Lagrangians, one first-order reduction each, same spectrum. The mechanism is standard, and the corpus already uses it for the Maxwell duality in *Electromagnetism in Media* and for the Chern–Simons–Maxwell duality in *Anyons and Braid Statistics in Biquaternionic Form*.

**It is not** a new solution of either theory. The duality relates the *descriptions*, not the dynamics: a solution of the Dirac equation maps to a solution of the gauge equation, and conversely, and no new physics follows. What the duality supplies is a *dictionary*: the Dirac mass corresponds to a topological gauge mass, the Dirac current to the gauge field strength, and the Dirac chirality to the gauge dual pair.

**It is not** established by this article. The corpus's standard for a verified claim is recomputation, and the parent action's two eliminations were not recomputed here: they are a variational computation on a field content that the source does not specify in enough detail in the available text to set up unambiguously. The article therefore records the equivalence as the source's claim, supported by the verified algebraic identities it uses, and flags the elimination itself as the first thing to complete against the published paper.

## Open Questions

1. **The dimension of the gauge sector.** The topological mass term $\varepsilon^{\mu\nu\lambda\rho}F_{\mu\nu}A_\lambda$ is the four-dimensional (BF / Cremmer–Scherk) mass; the $2+1$-dimensional Chern–Simons mass is a different term. Which one the source's gauge Lagrangian carries, and whether the gauge sector lives in the same four dimensions as the Dirac field or in a reduced three, is the first question to settle.

2. **The field content of the parent action.** The parent action's auxiliary field is a self-dual two-form (the antisymmetric part of the biquaternion), but whether it is also a one-form (a gauge field) and how many independent fields the parent action couples is not fixed by the display above. The published paper's parent action will settle it.

3. **The role of the triality.** The parent action is written in the s-vector variables, and the s-vector carries the triality (order-three ding) structure. Does the dual equivalence commute with the triality map $A \mapsto B \mapsto N \mapsto A$? If it does, the equivalence is triality-covariant, which would be a strong structural statement; if it does not, the triality breaks at the duality.

4. **The quantised equivalence.** A classical dual equivalence need not survive quantisation. Do the two reductions give the same anomaly, the same $\beta$ function, the same $S$-matrix? The corpus's *Anomalies and Anomaly Cancellation in Biquaternionic Form* is the natural place to test it.

5. **The relation to the corpus's Proca article.** *The Proca Equation: Massive Spin 1 in Biquaternionic Form* treats the ordinary (second-order) mass. Is the topological mass of this article a distinct biquaternionic object, and does the Proca article's mass term correspond to the *integrals* of the non-integrable phase?

These questions are open.

## Summary

Liu Yu-Fen's thesis is that the massive Dirac field and a topologically massive gauge field are **dual**: a single first-order parent action in the s-vector variables reduces, on one elimination, to the Dirac Lagrangian in the vector representation — kinetic term with the $\check c$ structure constants and the chirality-off-diagonal mass $m(G^*G^* + GG)$ — and, on the other elimination, to a gauge Lagrangian with a Maxwell kinetic term and a topological (Chern–Simons-type / BF-type) mass term $\tfrac{m}{4}\varepsilon^{\mu\nu\lambda\rho}F_{\mu\nu}A_\lambda$. The two describe the same propagating modes.

The mechanism is the standard first-order duality. The ingredients are three: the anti-self-duality $H^{\mu\nu} = -\tfrac{i}{2}\varepsilon^{\mu\nu\lambda\rho}H_{\lambda\rho}$ of the biquaternion's antisymmetric part, the identity that the next-to-topological density is the divergence of a Chern–Simons-type current, and the reading of the mass as a non-integrable phase carried by a unit complex vector $K^\mu$. The first is verified in the companion article; the second and third are the source's. The parent action's two eliminations were not recomputed in this pass, and the article records the equivalence as the source's claim, supported by the verified identities it uses.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G^\mu$ | s-Vector (complex four-vector), the Dirac field in the vector representation |
| $B^\mu, N^\mu$ | Real four-vectors of the two semi-spinors, $G = B + iN$ |
| $\check c^{\mu\nu\lambda} = (t^{\mu\nu\lambda\rho}-i\varepsilon^{\mu\nu\lambda\rho})j_\rho$ | Structure constants built on the neutral vector $j$ |
| $\bar\Psi\Psi$ | Dirac bilinear, $= \tfrac12(N^2 - B^2)$ |
| $H^{\mu\nu} = G^*_\lambda\check c^{\lambda\mu\nu}$ | Anti-self-dual two-form (the antisymmetric part) |
| $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ | Gauge field strength |
| $A_\mu$ | Gauge four-potential |
| $K^\mu$ | Unit complex vector; the mass as a phase |
| $\varepsilon^{\mu\nu\lambda\rho}$ | Totally antisymmetric symbol, $\varepsilon^{0123} = 1$ |
| $m$ | Fermion mass, equated to the topological gauge mass |
| $S_{\text{parent}}$ | The first-order action with the two reductions |
| $\mathcal{L}_D$, $\mathcal{L}_G$ | The Dirac and gauge Lagrangians |

## Further Reading

- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the parent action and its two eliminations, the topological (Chern–Simons-type) mass term, the self-dual field strength, the Chern–Pontryagin total derivative, and the non-integrable-phase reading of the mass. **This article's transcription of the parent action is from the source's summary; the eliminations are recorded as claims.**
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the s-vector representation, the bosonic Dirac Lagrangian, the self-dual form of the massive equation, and the bilinear dictionary on which the parent action is built.
- S. Deser, R. Jackiw and S. Templeton, "Topologically massive gauge theories," *Annals of Physics* **140** (1982) 372–411, for the original topologically massive gauge theory in $2+1$ dimensions and its Chern–Simons mass.
- E. Cremmer and J. Scherk, "Spontaneous dynamical breaking of gauge symmetry in dual models," *Nuclear Physics B* **72** (1974) 117–134, for the four-dimensional analogue, the $\varepsilon FF$-type mass of an antisymmetric tensor.
- M. Kalb and P. Ramond, "Classical direct interstring action," *Physical Review D* **9** (1974) 2273–2284, for the antisymmetric-tensor (B-field) formulation of the same mass, and for the dual equivalence of the massive vector and the antisymmetric tensor.
- The companion corpus articles: *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*, *Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form*, *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, *Anyons and Braid Statistics in Biquaternionic Form*, and *Anomalies and Anomaly Cancellation in Biquaternionic Form*.
