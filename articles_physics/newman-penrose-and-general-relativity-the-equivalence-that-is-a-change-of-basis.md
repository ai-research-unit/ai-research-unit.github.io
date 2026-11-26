# __Newman–Penrose and General Relativity: The Equivalence That Is a Change of Basis__

## Introduction

The Newman–Penrose formalism is exactly equivalent to tensor general relativity. This is a change of basis and not a new theory: the same metric, the same Levi-Civita connection, the same Riemann, Ricci and Weyl tensors, resolved in a null tetrad instead of a holonomic or orthonormal frame. That equivalence is old — Newman and Penrose, 1962 — and uncontroversial.

The claim of this section is a different one, and the two are routinely confused. The section shows that the kinematic scaffolding of the formalism — the null tetrad, the dyad, the inner products, the interval, the boost weights, the classification as multiplicity theory — maps exactly onto structures native to $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. It does not show that the biquaternion algebra reproduces the dynamics of general relativity, and the articles of the section say so at each step.

This article separates the two. It states the equivalence with tensor general relativity and verifies its counting; it states the chain of two arrows that the section actually establishes; it distinguishes the three senses in which the word "equivalent" is used; and it says what the word "exact" in the section's headline does and does not cover.

## The Equivalence With Tensor General Relativity

In tensor general relativity the local geometry of a spacetime is carried by the metric $g_{\imath\jmath}$, its Levi-Civita connection, and the curvature tensors built from it: the Riemann tensor, its trace the Ricci tensor, its trace the curvature scalar, and the trace-free remainder the Weyl tensor. In the Newman–Penrose formalism the same objects are resolved in a null tetrad $(l,n,m,\bar m)$ rather than in a coordinate frame, and the same information is repackaged into three lists.

**The connection becomes twelve complex spin coefficients.** They are the components of the metric-compatible connection in the null basis: $\kappa,\sigma,\rho,\tau$ built on the gradient of $l$; $\pi,\varsigma_{\mathrm{nps}},\mu,\jmath$ on the gradient of $n$; and the four real $\varepsilon,\gamma,\beta,\alpha$ on the mixed components. They carry the same content as the twenty-four real Christoffel-type coefficients $\Gamma_{abc}$ of the frame.

**The Weyl tensor becomes five complex Weyl scalars.** $\tilde{Ξ}_{0},\dots,\tilde{Ξ}_{4}$ are the contractions of the Weyl tensor with the tetrad legs, one scalar per distinct pattern of legs. They carry the same content as the ten real components of the Weyl tensor.

**The Ricci tensor becomes four real and three complex scalars.** $\Phi_{00},\Phi_{11},\Phi_{22}$ and the curvature scalar $\Lambda$ are real; $\Phi_{01},\Phi_{02},\Phi_{12}$ are complex and their conjugates supply the remaining entries. Ten real numbers in total, the dimension of the Ricci tensor.

That is the whole of the formalism's apparatus. Nothing is added to general relativity, and nothing is taken away.

## The Two Bijections

The equivalences of the previous section are bijections, and the counting makes them checkable rather than rhetorical.

**The Weyl bijection, ten real to five complex.** A tensor with the Riemann symmetries has twenty independent components. Trace-freeness imposes ten conditions — one for each symmetric pair of indices — leaving ten. With the tetrad fixed, the five complex contractions $\tilde{Ξ}_{k}$ are five complex numbers, which is ten real numbers. The map was computed on the ten-dimensional space of trace-free tensors with the Riemann symmetries and found to have rank ten over $\mathbb{R}$, equivalently five over $\mathbb{C}$: the five scalars are the ten components reorganised, with no kernel and no image missing. In spinor language the same count reads: the self-dual Weyl tensor is a totally symmetric fourth-rank spinor, $\tilde{Ξ}_{ABCD}\in\mathrm{sym}^4 S$, and $\dim\mathrm{sym}^4 S=\binom{5}{4}=5$.

**The connection bijection, twenty-four real to twelve complex.** A metric-compatible connection in a frame has coefficients $\Gamma_{abc}=(\nabla_a e_b)\cdot e_c$ antisymmetric in the last two indices, so six real numbers per tetrad direction and $4\times6=24$ in all, which is twelve complex. The same count comes from the values: the connection is valued in the six-real-dimensional Lorentz algebra, and a 1-form on four dimensions has four components, so $6\times4=24$. Twenty-four real either way, twelve complex either way.

**The Ricci bijection, ten real to four real and three complex.** The Ricci tensor is symmetric, hence ten components. In the null basis these are $\Phi_{00},\Phi_{11},\Phi_{22},\Lambda$ real and $\Phi_{01},\Phi_{02},\Phi_{12}$ complex, which is $4+2\cdot3=10$.

The three counts exhaust the twenty independent components of the Riemann tensor: $10$ Weyl, $9$ trace-free Ricci, $1$ scalar. The bookkeeping closes, which is what a change of basis means.

## The Chain of Two Arrows

The logic of this section is two arrows in sequence, and almost every over-reading of it comes from running them together.

$$
\underbrace{\big(\mathcal{M},g\big)}_{\text{tensors on a metric}}\;\longleftrightarrow\;\underbrace{\text{null-tetrad components}}_{\text{Newman–Penrose}}\;\longleftrightarrow\;\underbrace{\mathbb{B},\ \text{zero divisors},\ S}_{\text{biquaternion kinematics}}
$$

**The first arrow is an equivalence of theories.** It is the bijection just counted, in either direction, at every point and for every metric. Whatever tensor general relativity says, the null-tetrad components say, and conversely.

**The second arrow is the section's contribution, and it is not an equivalence of theories.** It is an embedding of the formalism's kinematic data into the algebra: the four legs are the four zero divisors, the tetrad is the matrix-unit basis up to the common factor $\sqrt2\,i$, the inner products follow from the pairing, the dyad is the factorisation of the matrix units, and the weights are the weights of $\mathrm{sym}^4 S$. Each of these is verified by computation in the companion articles.

The second arrow is exact at the level of the **frame**. It is not exact at the level of the **theory**, and it was never claimed to be. The dynamical content of general relativity — the connection as a solution-dependent object, the Weyl tensor as a functional of a metric, the field equations that tie the two — sits outside the algebra, which hosts the index spaces in which those objects are written and does not generate the objects.

## Three Senses of the Word Equivalent

Three different statements share one word, and keeping them apart is most of the work of this article.

| sense | statement | holds here? |
| --- | --- | --- |
| theory-level | two formulations have the same solutions and the same predictions | Newman–Penrose and tensor general relativity: yes, trivially |
| frame-level | two descriptions of the same data differ by a choice of basis | the null tetrad and the matrix-unit basis: yes, up to $\sqrt2\,i$ |
| representation-level | two structures live on the same vector space with different forms | $\mathbb{C}^4$ carrying the conformal group's Hermitian form of inertia $(2,2)$, and $\mathbb{C}^4$ as the algebra with its symmetric bilinear norm: yes, and the two forms differ |

The first row is the equivalence of the formalism with general relativity. The second is what the section proves. The third is a fact about vector spaces that the section uses and does not need.

No row of the table says that the biquaternion algebra is a theory of gravity. A theory needs field equations, and the algebra has none.

## What "Exact" Means Here

The section's headline is that the null tetrad is the algebra's matrix-unit basis up to $\sqrt2\,i$. That is a statement about **one object** — the null frame — and it is exact in the sense that it was verified directly: the four legs were written out, their images under the matrix realization computed, and the identity confirmed with the two real legs equal to the two primitive idempotents and the complex pair to the two nilpotents.

The identity is then used rather than admired, and the uses are where its content shows. The multiplication table of the four legs follows and gives a physical reading to $ln=nl=0$ — the two real null directions annihilate each other — and to $m\bar m=\sigma l$ — the nilpotent pair multiplies into the idempotent. The block-antidiagonal pairing on the Peirce corners explains why the algebra's own basis is null and an orthonormal one is the thing that is not native. The trace $\mathrm{tr}\,\tilde\Pi_{\mathrm{id}}=1$ against $\mathrm{tr}\,\vec\Pi_{\mathrm{nil}}=0$ shows that four arbitrary null directions are not a Peirce basis. The interval is rebuilt from the tetrad with no other input.

What the word does not cover is everything downstream of the frame. The connection is not selected by the algebra; the Weyl tensor is not determined by it; the field equations are absent from it. A reader who takes "exact" to mean "biquaternions are general relativity" has read the adjective across the boundary the section draws, and the ledger article is the corrective.

## The Residual Frame Choice

Even at the frame level the identification carries a qualification, and the section states it rather than burying it.

A Peirce basis has three parameters; a null tetrad has six. The identification therefore holds in a representative, and the representative is the **unit-boost frame**, in which the two real legs share one normalisation $\sigma=\sqrt2\,i$. Under a boost along the axis, $l\mapsto A l$ and $n\mapsto A^{-1}n$ with real $A$, each leg remains a scaled idempotent but the common factor is destroyed: $l$ becomes $(A\sigma)\tilde\Pi_{\mathrm{id},1}$ and $n$ becomes $(A^{-1}\sigma)\tilde\Pi_{\mathrm{id},2}$. The tetrad is then the Peirce basis rescaled leg by leg, which is still a statement about the algebra, but no longer a statement about a single $\sigma$.

So "exact" means exact after fixing the representative, and the boost that destroys the common factor is itself an automorphism of the bilinear form. This is a small point and it is the kind of small point that decides whether a claim is true.

## What the Stronger Claim Would Require

For the algebra to be a theory of gravity rather than a home for a frame, three things would have to hold, and none of them does.

**The algebra would have to select a connection.** It supplies the six-real-dimensional bivector subspace in which a connection takes its values, and it supplies the tetrad in which the connection is read; it does not single out one connection among the many metric-compatible ones.

**The algebra would have to determine the curvature.** It hosts $\mathrm{sym}^4 S$, the space in which the self-dual Weyl spinor lives, but it says nothing about which element of that space a given solution produces. That is the gap named in the companion article on the scalars.

**The algebra would have to impose the field equations.** There are no field equations in the algebra, so the twelve coefficients and the five scalars are not tied to one another by any identity the algebra supplies.

A future derivation of any one of these would change the status of the claim, and the section would then have to be rewritten rather than extended. Until then the claim stands where it is: the algebra contains the frame, and the frame is not the theory.

## Verdict

Newman–Penrose is general relativity in a null basis, and the equivalence is trivial in the sense that it is a change of basis — the same tensors, the same equations, a different frame. The section establishes a second and different statement: the null frame, with its dyad, its pairing, its weights and its classification, is native to the biquaternion algebra, and the identification is exact at the frame level, verified by computation, and holds in the unit-boost representative.

Two equivalences, then, and only the first is an equivalence of theories. The second is an embedding of a frame into an algebra. The section never claims more, and the ledger article states, item by item, exactly how much less it is.
