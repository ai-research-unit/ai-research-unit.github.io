
# __Conventions in the Biquaternion Universe__

## Introduction

A framework built on a non-standard algebra, and on a non-standard choice of which part of it counts as "real", is a framework in which a reader will repeatedly find things that look wrong and are not. Two examples fix the idea. The series takes the **anti**-Hermitian subspace as the material sector, where the more familiar convention would take the Hermitian one. And the series' d'Alembertian carries a sign opposite to the one used in the article on Weyl spinors, so that two mass-term equations which look like sign errors are in fact the same equation. In both cases it is the "correction" that is the error.

This article collects the conventions of the series in one place, states each one, and gives the reason it was chosen. It is meant to be read before any other article is edited, and it has two readers in mind. The first is a reader who meets an equation in a companion article that looks wrong. The second is anyone writing or revising an article in the series, for whom the conventions are load-bearing: a change that looks local — a sign, an operator definition, a factor of $i$ — generally propagates into a dozen dependent articles.

The article is organised in two parts. The first gives the **algebraic** conventions: the algebra, its basis, its conjugations, the two sectors, the matrix representation, and the trace. The second gives the **spacetime and field-theoretic** conventions: the material coordinate, the metric, the d'Alembertian, the convention for the Dirac mass term, and the algebra's real structure.

One warning applies throughout. **A convention recorded here is not a claim that the alternative is wrong.** Several of these choices are freely made where either choice would be defensible; they are conventions, not theorems. What is not free is *consistency*: once a convention is fixed, the dependent articles inherit it, and a change to it is a change to all of them. Where a convention is instead forced — where the alternative leads to a demonstrable contradiction — the article says so explicitly, and that distinction is the difference between a convention and a result.

## The Algebraic Conventions

### The Algebra and Its Basis

The framework is set in the **biquaternion algebra**

$$
\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H},
$$

the complexification of the quaternions. Every element is written in the basis

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $e_0 = 1$ and $e_1, e_2, e_3$ are the quaternion units,

$$
e_1^2 = e_2^2 = e_3^2 = -e_0, \qquad e_1e_2 = -e_2e_1 = e_3,
$$

and the four coefficients $Q_\mu$ are **complex** numbers. The scalar imaginary, denoted $i$, is the complex unit of the complexification:

$$
i^2 = -1.
$$

One structural fact governs the whole series, so it is worth isolating. **The scalar unit $i$ is central**: it commutes with every element of $\mathbb{B}$, because it belongs to the $\mathbb{C}$ factor of the tensor product, while the quaternion units belong to the $\mathbb{H}$ factor. Multiplication by a *central* phase $e^{i\alpha}$ therefore commutes with every operator constructed from the algebra — in particular with the biquaternionic gradient $\tilde{\nabla}$ — and this is why the central phase is the algebra's natural continuous symmetry. The articles on Noether's theorem and the gauge principle rest on it.

As a complex algebra $\mathbb{B}$ is isomorphic to the full matrix algebra,

$$
\mathbb{B} \cong M_2(\mathbb{C}),
$$

and this identification is used constantly. It is fixed explicitly in *The Matrix Representation* below, which asserts the four basis images and shows that neither the factor $i$ nor the sign is a free choice. Its two **minimal left ideals** are the algebra's two chiralities. They are the reason the Dirac field is carried by the spinor module rather than by the whole algebra, and the reason the mass term has the shape it has, as discussed below.

### The Conjugations and the Real Subspaces

The algebra carries four natural involutions, all of them used in the series:

| Name | Notation | Definition |
|---|---|---|
| Quaternion conjugation | $\bar{\tilde{Q}}$ | $e_k \mapsto -e_k$, $i$ fixed |
| Complex conjugation | $\tilde{Q}^*$ | $i \mapsto -i$, $e_k$ fixed |
| Hermitian conjugation | $\tilde{Q}^\dagger$ | $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*}$ |
| Anti-Hermitian conjugation | $\tilde{Q}^\flat$ | $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ |

Their fixed-point sets are the distinguished real subspaces of $\mathbb{B}$. Three of these are four-dimensional, and each is given a name in the series:

- the **real-quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, the fixed points of complex conjugation, which is a subalgebra;
- the **anti-Hermitian subspace** $\mathbb{M}_-$, the fixed points of $\flat$;
- the **Hermitian subspace** $\mathbb{M}_+$, the fixed points of $\dagger$.

The fourth fixed space, that of quaternion conjugation, is the **complex subspace** $\mathbb{C}_{\mathbb{B}} = \{Q_0 e_0\}$, of real dimension two; it is the center of $\mathbb{B}$.

It is worth noticing that neither $\mathbb{M}_-$ nor $\mathbb{M}_+$ is a subalgebra of $\mathbb{B}$: for example $(ie_1)(ie_2) = -e_3$, a product of two elements of $\mathbb{M}_+$ that lies in $\mathbb{M}_-$. The sectors are therefore real vector spaces on which the algebra acts, not algebras in their own right.

### The Material and Informational Sectors

The two sectors are the four-dimensional fixed spaces of the two Hermitian conjugations:

$$
\mathbb{M}_- = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\flat = \tilde{Q}\}, \qquad
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\dagger = \tilde{Q}\}.
$$

A basis of $\mathbb{M}_-$ over $\mathbb{R}$ is $ie_0, e_1, e_2, e_3$: its scalar part is **purely imaginary** and its vector part **real**. A basis of $\mathbb{M}_+$ over $\mathbb{R}$ is $e_0, ie_1, ie_2, ie_3$: its scalar part is **real** and its vector part **purely imaginary**.

The naming convention is a deliberate choice and should be stated as such:

- $\mathbb{M}_-$ is called the **material** sector. It carries the spacetime coordinate and the four-vectors, and its norm form has signature $(3,1)$.
- $\mathbb{M}_+$ is called the **informational** sector. It carries Hermitian operators, states and observables, and its norm form has signature $(1,3)$.

**The choice of which subspace is "real".** The convention that has to be flagged is that $\mathbb{M}_-$ is the *anti*-Hermitian subspace, so that the framework's "real" part is the part built on $i$ times a Hermitian element. The more familiar convention takes the Hermitian part as real. The two differ only by the central factor $i$, and there is no mathematical error either way: an anti-Hermitian generator is the standard choice for the Lie algebra of a unitary group, and it is $\mathbb{M}_-$ that carries that role here. What is unusual is that the convention is applied to the **field** rather than to the generators. Once it is, $\mathbb{M}_-$ is fixed by $\flat$ and $\mathbb{M}_+$ is not, and that is what makes $\mathbb{M}_-$ the framework's material sector. A reader who "restores" the Hermitian convention will find the whole series inverted. Do not.

### The Matrix Representation

The identification $\mathbb{B} \cong M_2(\mathbb{C})$ is fixed by a single isomorphism, written $\Phi$, and it is worth writing out in full because every numerical check in the series is performed with it. The four basis elements are assigned the matrices

$$
\Phi(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\Phi(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\Phi(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\Phi(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$
<!-- CONVENTION — the matrix basis: the four basis images are asserted, with sigma_k = i Phi(e_k) = Phi(i e_k). Both the factor i and the sign are forced (e_k^2 = -e_0 and e_1 e_2 = e_3), so a reviewer must not "correct" them to Phi(e_k) = +i sigma_k, nor to real matrices, and must not treat the choice as free. -->

with the central scalar mapping to $\Phi(i) = iI_2$, and a general element to

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix},
\qquad
\det\Phi(\tilde{Q}) = N(\tilde{Q}) .
$$

Equivalently, the basis images are $i$ times the Pauli matrices, $\sigma_k = i\,\Phi(e_k) = \Phi(ie_k)$: the Pauli matrices are the images of the **Hermitian** units $ie_k$. In this realisation the four fixed spaces of the preceding subsections read off as follows.

| Subspace | Matrix image |
|---|---|
| Center $\mathbb{C}_{\mathbb{B}}$ | the scalar matrices $Q_0 I_2$ |
| Real quaternions $\mathbb{H}_{\mathbb{B}}$ | $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z} \end{pmatrix}$, $z, w \in \mathbb{C}$ |
| Hermitian $\mathbb{M}_+$ | the Hermitian matrices |
| Anti-Hermitian $\mathbb{M}_-$ | the anti-Hermitian matrices |

**The conjugations in matrix form.** The four involutions of the algebra become four matrix operations, with $M = \Phi(\tilde{Q})$:

| Involution | Matrix image |
|---|---|
| Quaternion conjugation $\bar{\tilde{Q}}$ | the adjugate $\epsilon M^{\mathsf T}\epsilon^{-1}$ |
| Complex conjugation $\tilde{Q}^*$ | $\epsilon\,\overline{M}\,\epsilon^{-1}$ |
| Hermitian conjugation $\tilde{Q}^\dagger$ | the conjugate transpose $M^\dagger$ |
| Anti-Hermitian conjugation $\tilde{Q}^\flat$ | $-M^\dagger$ |

Two of the four are dressed by the invariant antisymmetric form

$$
\epsilon = i\sigma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \Phi(-e_2),
$$
<!-- CONVENTION — the conjugation dictionary: quaternion conjugation is the adjugate epsilon M^T epsilon^-1 and complex conjugation is epsilon conj(M) epsilon^-1, while dagger and flat are undressed. A reviewer must not "simplify" complex conjugation to a plain entrywise conjugation of M: that operation is the image of no involution, sends e_1 and e_3 to minus themselves and leaves e_2 fixed, and so destroys the sector dictionary. -->

and the adjugate identity $\tilde{Q}\bar{\tilde{Q}} = N(\tilde{Q})e_0$ is the matrix identity $M\,\mathrm{adj}(M) = \det(M)I_2$.

**Entrywise conjugation is not in the list.** A reader who has the matrix $M$ in hand will be tempted to conjugate its entries and call the result $\Phi(\tilde{Q}^*)$. That operation is not the image of any involution of the algebra, and it does not preserve the sector dictionary: it sends $-i\sigma_1 \mapsto +i\sigma_1$ and $-i\sigma_3 \mapsto +i\sigma_3$, turning the images of $e_1$ and $e_3$ into the images of $-e_1$ and $-e_3$, while $\Phi(e_2)$ has real entries and is left untouched. Only the dressed form in the table is correct. The safe rule for the series is that $\bar{\phantom{Q}}$, ${}^*$, $\dagger$ and $\flat$ are evaluated through those four formulas and never by conjugating matrix entries on their own.

**The symbol $\Phi$.** A plain $\Phi$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde{\Phi} = \varphi\,e_0$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde{U}}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\Phi$ is not any of them.

**Why the form is fixed.** Three features of the assignment are consequences rather than choices, and they are worth recording because the identification $\mathbb{B} \cong M_2(\mathbb{C})$ is often written without them.

- *The factor $i$ is forced by $e_k^2 = -e_0$.* The matrices $\sigma_k$ square to $+I_2$, so a real assignment $e_k \mapsto \sigma_k$ would give $e_k^2 = +e_0$, the wrong sign. Both $\pm i\sigma_k$ repair it.
- *The sign is forced by $e_1e_2 = e_3$.* The opposite assignment, $\Phi(e_k) = +i\sigma_k$, reproduces $e_k^2 = -e_0$ but reverses every cross-relation: $(+i\sigma_1)(+i\sigma_2) = -\sigma_1\sigma_2 = -i\sigma_3$, whereas that assignment gives $e_3$ the image $+i\sigma_3$. The sign in the basis table above is therefore a consequence, not a convention.
- *The residual freedom is unitary, and no more.* Any other isomorphism has the form $\Phi' = S\Phi S^{-1}$ with $S$ invertible. Among these, the ones that preserve the sector table above — $\mathbb{M}_+$ to Hermitian, $\mathbb{M}_-$ to anti-Hermitian, $\mathbb{H}_{\mathbb{B}}$ to the form $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$ — are exactly those with $S$ a unitary matrix up to a nonzero complex scalar, and the scalar cancels in $S \cdot S^{-1}$. The representation is thus fixed up to a **unitary change of basis of $\mathbb{C}^2$**. An arbitrary invertible $S$ destroys the dictionary, and so does a genuine squeeze $S = UP$ with $U$ unitary and $P$ positive definite and $\neq I$; both cases were checked on four hundred random biquaternions each, and neither preserved a single entry of the table.

The matrix realisation is a convention of *presentation*, not of content: the algebra and the two sectors of level 2 are unchanged by it, and the articles of the series use the assignment above identically. It is recorded here because a mistake of translation between the algebra and its matrices is repaired **here**, by correcting the assignment or the explicit factors of $i$, and never by altering the norm form, the $ict$ assignment or the sector split.

### The Trace

The trace is taken in the $2 \times 2$ matrix representation afforded by $\Phi$, with the normalisation

$$
\mathrm{Tr}(e_0) = 2 .
$$

For an idempotent $\tilde{P}$ — a state — and a Hermitian element $\tilde{H}$ — an observable — both of which live in $\mathbb{M}_+$, the trace reduces to twice the scalar part:

$$
\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H}), \qquad \tilde{P} \in \mathbb{M}_+, \ \tilde{H} \in \mathbb{M}_+ .
$$

The restriction to $\mathbb{M}_+$ is not needed. As the article on the involution lattice records, the identity holds for arbitrary arguments, which is the form in which the operator articles use it:

$$
\mathrm{Tr}(\tilde{X}\tilde{Y}) = 2\,\mathrm{Sc}(\tilde{X}\tilde{Y}) \qquad \text{for all } \tilde{X}, \tilde{Y} \in \mathbb{B},
$$

where $\mathrm{Tr}(\tilde{X}\tilde{Y})$ is the trace of the product of the matrices, $\mathrm{Tr}(\Phi(\tilde{X})\Phi(\tilde{Y}))$. This follows from $\mathrm{Tr}\,\Phi(\tilde{Q}) = 2Q_0$, the $\mathbb{C}$-linearity of $\Phi$ and the multiplicativity of the trace; the $\mathbb{M}_+$ statement above is the case in which the pairing is real. This identity is used throughout the series to turn algebraic pairings into real numbers; in the quantum-information articles it is the Born rule, $p = \mathrm{Tr}(\tilde{P}\tilde{\rho})$. Its factor $2$ — not $1$ — is the convention, and it must not be dropped.

## The Spacetime Conventions

### The Material Coordinate

The spacetime point is an element of the material sector,

$$
\tilde{X} = ict\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 \in \mathbb{M}_- .
$$

Two conventions sit in this one line, and both matter.

First, the coefficient of $e_0$ is $ict$, not $ct$: the time coordinate is **imaginary**. This is the $ict$ convention, and it is chosen so that the Minkowski interval emerges as the algebra's own norm form rather than as an extra postulate.

Second, the spatial part is a pure-quaternion **vector**, written $\mathbf{x} = x e_1 + y e_2 + z e_3$, so that $\tilde{X} = ict\,e_0 + \mathbf{x}$.

The reason for the $ict$ choice is the norm form. On $\mathbb{M}_-$ it is real,

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = (iq_0)^2 + q_1^2 + q_2^2 + q_3^2 = -q_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

a quadratic form of signature $(3,1)$: three positive spatial directions and one negative temporal direction. **The Minkowski signature is thus a consequence of $i^2 = -1$**, not an independent input. It vanishes on the cone

$$
q_0^2 = q_1^2 + q_2^2 + q_3^2,
$$

whose nonzero elements are the algebra's **zero divisors**. The complement of the cone has three connected components: the spacelike region and the two time-like components, future and past.

The Lorentz group enters as the group of unit-norm elements,

$$
SL(2,\mathbb{C}) \cong \{\tilde{\Lambda} \in \mathbb{B} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\},
$$

acting on $\mathbb{M}_-$ by rotor conjugation, $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$. The four-element basis $e_0, e_1, e_2, e_3$ and the $ict$ assignment are the conventions on which all the relativistic articles depend.

### The Metric: Three Levels

The word "metric" appears at three distinct levels in the series, and most of the disagreements below are the result of the levels being conflated. They are separated here in order of priority, because the first is the convention of the framework and the third is only a convention of translation.

**Level 1 — the norm form on $\mathbb{B}$.** The algebra carries the complex-linear norm form

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2 ,
$$

and with all four coefficients $Q_\mu$ complex its Gram matrix is the **identity**:

$$
\mathrm{diag}(+1,+1,+1,+1).
$$

This is the metric of the biquaternion universe, and it is the framework's primary convention. It is a metric **on $\mathbb{C}$** — a complex bilinear form — and read that way every one of its four entries is positive: on $\mathbb{B}$ there is no minus sign in the form itself, and none is needed. That is precisely what the complex coefficients buy. A *real* direction has to be labelled positive or negative in advance, and that labelling becomes a convention that can be chosen wrongly; a complex coefficient carries its own sign in the coefficient, so all four directions can start out on an equal footing and no such commitment is required. Two cautions about reading it. It is not positive definite and it is not a norm in the analytic sense — it vanishes on the nonzero zero divisors, which is why $\mathbb{B}$ is not a normed division algebra. And the Hermitian form $\sum_\mu |Q_\mu|^2$ is a *different* object: real-valued, positive definite, and $\mathbb{C}$-antilinear in its first argument. It is used only where a positive-definite inner product on a complex vector space is needed, and it is not the norm form of the algebra.

**Level 2 — the real sectors.** A minus appears only once a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$. The two four-dimensional real sectors are exactly such choices, and the same level-1 form reads off differently on each:

| Sector | Basis | $N$ on the basis | Signature |
|---|---|---|---|
| $\mathbb{M}_-$ (material) | $ie_0,\ e_1,\ e_2,\ e_3$ | $-1,+1,+1,+1$ | $(-,+,+,+)$ |
| $\mathbb{M}_+$ (informational) | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $+1,-1,-1,-1$ | $(+,-,-,-)$ |

Read as a statement about **objects** rather than directions: an element of $\mathbb{M}_-$ carries the metric $(-,+,+,+)$, and an element of $\mathbb{M}_+$ carries $(+,-,-,-)$. This is not a separate choice made sector by sector — it is the one level-1 form read on two different real bases, and the two readings are mirror images of one another through the identity below.

The Minkowski interval is not postulated at this level either. It is the level-1 form read on the material sector with the time coordinate written $ict$: the four-position is $\tilde{X} = ict\,e_0 + \mathbf{x}$, whose scalar coefficient $ict$ is imaginary, and

$$
N(\tilde{X}) = (ict)^2 + x^2 + y^2 + z^2 = -c^2t^2 + \mathbf{x}^2 ,
$$

with the minus arising from $i^2 = -1$ alone. Multiplication by $i$ exchanges the sectors, $i\mathbb{M}_+ = \mathbb{M}_-$, and reverses the sign of the form, $N(i\tilde{Q}) = -N(\tilde{Q})$; the mirror relation between the two signatures is that identity. The Lorentzian signature is therefore an *output* of the biquaternion conventions, not an input to them.

For contractions of four-vectors in the $ict$ coordinate the series writes this level-2 form as

$$
\eta = \mathrm{diag}(-1,+1,+1,+1),
$$

and at this level the series is uniform: the $ict$ metric is $(-,+,+,+)$ throughout. The two articles outside the relativistic core that carry a symbol $g = \mathrm{diag}(-1,+1,+1,+1)$ — the companion articles on the Higgs mechanism and on the Newman–Penrose formalism — mean **this** object, the $ict$-coordinate metric for index contractions, and not a Clifford metric, as their own notation tables state. They are not part of the level-3 disagreement below.

**Level 3 — the Clifford metric of the $\gamma^\mu$.** When the series writes gamma matrices it needs a further symbol $g$, defined by $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$. This is a property of the chosen generators and not of the biquaternion algebra, and it is best regarded as a **tool** rather than a convention: it can be used or not, depending on the situation, and where it is used it should not dictate any convention of the framework. The biquaternion formulation requires no gamma matrices; they are a translation into the language of the standard Dirac literature, convenient when comparing with that literature or borrowing a standard result, and dispensable otherwise. The freedom this level carries is exactly the freedom the framework treats as presentation: replacing every generator by $i\gamma^\mu$ takes $g$ to $-g$ and leaves the biquaternion algebra, the norm form, the sector split, the chirality operator and the whole of levels 1 and 2 invariant.

The value the series now uses is the standard **mostly-minus**

$$
g = \mathrm{diag}(+1,-1,-1,-1),
$$

so that $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$. Two reasons fix it. First, **it is the form of the objects the tool represents**: the Clifford vectors correspond to the *Hermitian* subspace $\mathbb{M}_+$ — the dictionary's own identification is $x_\mu\gamma^\mu = \gamma^0\Phi(w)$ with $w \in \mathbb{M}_+$ — and $(+,-,-,-)$ is the $\mathbb{M}_+$ form, so the square of a Clifford vector agrees with the norm form of the biquaternion it represents with **no relative sign**. Second, it is the standard particle-physics convention, so articles transcribing standard results inherit the standard sign without adjustment, and the name $\mathrm{Cl}_{1,3}$ is correct in the usual counting, $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$.

The opposite sign, $g = \mathrm{diag}(-1,+1,+1,+1)$, is **not in use**. It pairs the generators with the material sector, which is a real form they do not belong to; the price is a relative minus sign between the square of a Clifford vector and the norm form of the biquaternion it represents, a mixed sign pattern in the timelike bivectors, and a non-standard naming of the algebra. It is recorded here only because the series used it previously, in the article that defines the gamma matrices and the Dirac equation, in the Dirac-algebra dictionary, and in the mathematics article *Biquaternion Algebraic Representations*; those three have been aligned to the value above.

A difference at this level would **not** be an error at level 1 or level 2, and half the reason for separating the levels is to stop it being read as one: the norm form, the $ict$ metric and the sector structure are the same for either sign. The sign decides only which *real* Clifford form the generators generate — $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ for $(+,-,-,-)$, $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ for $(-,+,+,+)$ — and the even subalgebra, which is $\mathbb{B}$ itself, is the same for both, so no dictionary entry and no biquaternion identity depends on it.

The order of authority is therefore one-way. The algebra and its level-1 and level-2 conventions are the framework; the gamma matrices and their metric are a translation of it, adopted per article for whatever the article is doing. The tool serves the framework and not the reverse: a Clifford computation is never a reason to change a biquaternion convention, and where the two appear to disagree, the disagreement is in the translation and is resolved by adjusting the generators, the adjoint, or the explicit factors of $i$ — never by altering the norm form, the $ict$ assignment, or the sector split.

One consequence does reach the physics, and it is the only place where a level-3 choice is not free. The Dirac adjoint is $\bar{\psi} = \psi^\dagger\gamma^0$, so it carries $\gamma^0$ and changes with the convention. With the mostly-minus generators $\bar{\psi}\gamma^0\psi = +\psi^\dagger\psi$, the positive number density; with the mostly-plus generators the same expression gives $-\psi^\dagger\psi$. A spinor bilinear written as $\bar{\psi}\Gamma\psi$ therefore requires the adjoint to be defined consistently with the generators in use. No article in the series currently writes a spinor bilinear in the mostly-plus convention, so no statement in the series is in error on this count; the point is recorded so that one is not introduced. This sign is not part of the freedom that $\gamma^\mu \mapsto i\gamma^\mu$ leaves behind.

### The d'Alembertian, and a Known Sign Collision

The series' d'Alembertian is defined through the biquaternionic gradient:

$$
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2 ,
$$

the **series convention**, used by the Klein–Gordon article, the Dirac article, and the great majority of the series.

The article *Exercise: Chirality and the Weyl Spinors* uses a different one:

$$
\Box_{\text{Weyl}} = \partial_0^2 - \nabla^2 ,
$$

in natural units with the standard quantum-field-theory metric $(+,-,-,-)$. The two are related by

$$
\Box_{\text{Weyl}} = -\,\Box_{\text{series}} .
$$

Since an overall factor $-1$ does not change the kernel, the two mass-term equations

$$
(\Box + m^2)\psi = 0 \quad \text{(the Weyl-spinor exercise)}, \qquad \left(\Box - \frac{m^2c^2}{\hbar^2}\right)\psi = 0 \quad \text{(the series)}
$$

have the **same solution set**. They are the same equation written in two sign conventions.

This is the single most likely place for a spurious "correction" in the whole series. The rule is: **check the local definition of $\Box$ before touching a mass-term sign.** Reciprocal markers sit at both articles recording this, so that neither is "aligned" to the other in isolation.

## The Dirac Mass Term: the Linear, Chirality-Off-Diagonal Convention

### The Convention

The biquaternionic Dirac equation for a **massless** field is

$$
\tilde{\nabla}\tilde{\Psi} = 0 ,
$$

which is identical in form to the source-free biquaternion Maxwell equation. For a field of mass $m$ the equation is **linear** in the field and **off-diagonal between the chiralities**. Writing $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$, the massive equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

the **canonical form** of the series. Its massless limit is $\tilde{\nabla}\tilde{\Psi} = 0$.

Two features of this convention are load-bearing, and both are stated as standing rules.

**(i) The mass term is linear.** Because it is linear in the field, the continuous central phase passes through it: the vector $U(1)$ symmetry is **exact for the massive field**,

$$
\partial_\mu j^\mu = 0 \quad \text{on shell, for all } m,
$$

and what the mass breaks is not the vector symmetry but the **axial** one,

$$
\partial_\mu j_5^\mu = 2im\,\bar{\Psi}\gamma_5\Psi ,
$$

which vanishes only at $m = 0$. A single plane wave cannot exhibit this breaking: its bilinears are $x$-independent, so both divergences vanish identically and the distinction is invisible. The breaking is visible on a **superposition**, which is how it should be checked.

**(ii) The mass term is off-diagonal between the chiralities.** It relates $\tilde{\Psi}_L$ to $\tilde{\Psi}_R$; it never pairs a field with its own conjugate.

### Why Linear and Off-Diagonal

The off-diagonal form is **forced**, not chosen, and the argument is purely algebraic.

Left multiplication by an element of $\mathbb{B}$ *preserves* each minimal left ideal. Since those ideals are the two chiralities, no combination of the form $a\tilde{\Psi}_L + b\tilde{\Psi}_R$ can relate one chirality to the other: left multiplication maps each into itself. A mass term that couples the chiralities therefore has to act as a **right** multiplication, which is exactly what the pair above does. Equivalently, restricted to the strict spinor module — a single minimal left ideal — the mass is simply linear.

This is the structural reason why the **spinor module**, and not the whole algebra, is the natural carrier of the Dirac field. On that module the pair is the matrix equation $(\not\partial - m)\psi = 0$ with $\psi = (\psi_L, \psi_R)$ the pair of Weyl spinors, and the off-diagonal structure is the statement that the mass couples the two Weyl spinors.

### What Is Not the Mass Term

The series previously wrote the massive equation as a single **antilinear** equation in one field,

$$
\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat , \qquad \tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger ,
$$

using the algebra's anti-Hermitian conjugation. **This is not the mass term, and it must not be restored as one.** The reason is not that it is antilinear — a Majorana mass is also antilinear and is perfectly physical. The reason is its dispersion relation.

For that equation, the central-phase plane waves do **not** sit on the physical mass shell. Solving the two-frequency system for a single-mode field gives nullity $0$ on the timelike shell $k_0^2 = k^2 + m^2$ but nullity $4$ on the **spacelike** shell $k^2 = k_0^2 + m^2$. Its solutions therefore lie on the spacelike locus. An equation whose central-phase solutions are spacelike is not the Dirac equation, and it contradicts the four-momentum kinematics the rest of the series uses. The spacelike dispersion is a property of that equation, not a typographical error, and re-deriving it by hand (pure real arithmetic suffices) reproduces the nullities. It is exactly why the equation was retired as the mass term.

**The diagnosis is the dispersion, not the antilinearity.** This distinction matters, because the antilinear structure itself is retained — it is the algebra's real structure, and it has genuine uses, as the next section records.

### What Dependent Articles Inherit

The three consequences below propagate into every article that touches the Dirac equation. They are the reason this convention cannot be changed locally.

1. **The vector $U(1)$ is conserved for the massive field.** The old claim that the mass breaks the phase symmetry belonged to the retired antilinear equation. In the linear form, the central phase passes through the mass term and commutes with $\tilde{\nabla}$, so the vector current is conserved on shell at all $m$.
2. **The axial current is what the mass breaks**, with $\partial_\mu j_5^\mu = 2im\bar{\Psi}\gamma_5\Psi$, and it is checked on a superposition.
3. **The mass is the off-diagonal coupling between the two central ideals** of $\mathbb{B} \cong M_2(\mathbb{C})$ — the two chiralities, that is, the algebra's central splitting. It breaks exactly the symmetry that rotates those two ideals, and *not* the central $U(1)$ the algebra canonically carries.

## The Real Structure $\flat$

### What $\flat$ Is

The map

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger = -\bar{\tilde{\Psi}}^{\,*}
$$

is the **anti-Hermitian conjugation**. It is not merely a sign variant of $\dagger$; it has its own algebraic character:

- it is a $\mathbb{C}$-**antilinear** involution, $(\alpha\tilde{A} + \beta\tilde{B})^\flat = \alpha^*\tilde{A}^\flat + \beta^*\tilde{B}^\flat$;
- it is **order-reversing with a twist**, $(\tilde{A}\tilde{B})^\flat = -\tilde{B}^\flat\tilde{A}^\flat$, the sign being the only difference from an ordinary anti-automorphism;
- it acts by a **sign on the two sectors**,
$$
\tilde{\Psi}^\flat = +\tilde{\Psi}\ \ (\tilde{\Psi} \in \mathbb{M}_-), \qquad
\tilde{\Psi}^\flat = -\tilde{\Psi}\ \ (\tilde{\Psi} \in \mathbb{M}_+);
$$
- consequently its **fixed space is the anti-Hermitian sector $\mathbb{M}_-$**.

The map $\flat$ is the algebra's **real structure**, and its shape is that of a charge-conjugation (Majorana) pairing: it relates a field to its own conjugate. The sign convention on the two sectors is what makes $\mathbb{M}_-$ the fixed space, and hence what makes $\mathbb{M}_-$ the material sector — the two conventions are the same convention seen twice.

### What $\flat$ Is For

$\flat$ is retained in the framework for what it is genuinely for:

- conjugation, and the definition of the $\mathbb{M}_\pm$ split itself;
- the trace and the bilinear pairings;
- the real-form question of Dirac versus Majorana fermions, which the companion articles on chirality, the neutrino and the CPT theorem develop.

In every case the coupling built on $\flat$ pairs $\tilde{\Psi}$ with $\tilde{\Psi}^\flat$. Because $\flat$ is antilinear, such a coupling is **not invariant under the continuous central phase** — which is precisely the difference between a Majorana-type pairing and an ordinary Dirac mass, and precisely why $\flat$ cannot serve as the mass term of the Dirac equation.

### What $\flat$ Is Not

$\flat$ is **not** the mass. The two roles were conflated in the retired form $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$, and separating them is the content of the mass-term convention above. A reader who finds $\flat$ in an article should expect conjugation, a Majorana pairing, a bilinear, or the sector split — never a Dirac mass.

## Summary

The conventions of the series fall into two groups.

**Algebraic.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, over complex coefficients. The scalar unit $i$ is central, which is what makes the central phase the algebra's continuous symmetry. The conjugations give four distinguished real subspaces, three of them four-dimensional and named: $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$, $\mathbb{M}_+$. With complex coefficients the norm form $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ is the identity matrix on $\mathbb{B}$; its Minkowski signature appears only on the real sectors, and the $i$ is what supplies the minus. The matrix representation $\Phi$ is fixed by its four basis images, with $\sigma_k = i\,\Phi(e_k) = \Phi(ie_k)$; the residual freedom is a unitary change of basis of $\mathbb{C}^2$ and nothing further, so the sector dictionary cannot be altered by re-choosing it.

**Spacetime and fields.** The material coordinate is $\tilde{X} = ict\,e_0 + \mathbf{x}$, using the $ict$ convention so that the Minkowski interval is the norm form, of signature $(3,1)$, vanishing on the zero-divisor cone. The $ict$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The series d'Alembertian is $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$; the Weyl-spinor exercise uses the opposite sign, $\Box = \partial_0^2 - \nabla^2$, and the two mass-term signs are the same equation. The Clifford metric $g$ is a level-3 tool rather than a convention, adopted where an article translates into gamma matrices, and its value is the standard mostly-minus $\mathrm{diag}(+1,-1,-1,-1)$ throughout the series — the $\mathbb{M}_+$ form, since the Clifford vectors correspond to the Hermitian subspace, so that the square of a Clifford vector agrees with the norm form of the biquaternion it represents with no relative sign. The opposite sign is not in use. Either way the norm form, the $ict$ metric and the sector structure are unchanged, and the tool never dictates them. The Dirac mass term is **linear and chirality-off-diagonal**, $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$; it conserves the vector $U(1)$ and breaks the axial symmetry. The retired antilinear form $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ was retired for its spacelike dispersion, and $\flat = -\dagger$ is retained as the algebra's real structure.

The theme is single. In a framework whose algebra and sector assignment are non-standard, the most likely error is a correction of something that is deliberate. The conventions recorded above are the places where that is most likely to happen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\bar{\tilde{Q}}, \tilde{Q}^*, \tilde{Q}^\dagger, \tilde{Q}^\flat$ | Quaternion, complex, Hermitian and anti-Hermitian conjugation |
| $\bar{\tilde{Q}} \mapsto \epsilon M^{\mathsf T}\epsilon^{-1}$, $\tilde{Q}^* \mapsto \epsilon\overline{M}\epsilon^{-1}$ | The two conjugations dressed by the antisymmetric form; $\epsilon = i\sigma_2 = \Phi(-e_2)$ |
| $\tilde{Q}^\dagger \mapsto M^\dagger$, $\tilde{Q}^\flat \mapsto -M^\dagger$ | The two undressed ones. Entrywise conjugation of $M$ alone is not the image of any involution |
| $\flat = -\dagger$ | The anti-Hermitian conjugation, the algebra's real structure |
| $\mathbb{M}_- = \{ \tilde{Q} : \tilde{Q}^\flat = \tilde{Q} \}$ | Anti-Hermitian subspace, the material sector; basis $ie_0, e_1, e_2, e_3$ |
| $\mathbb{M}_+ = \{ \tilde{Q} : \tilde{Q}^\dagger = \tilde{Q} \}$ | Hermitian subspace, the informational sector; basis $e_0, ie_1, ie_2, ie_3$ |
| $\mathbb{C}_{\mathbb{B}} = \{Q_0 e_0\}$ | Complex subspace, fixed points of quaternion conjugation; the center of $\mathbb{B}$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, fixed points of complex conjugation; a subalgebra |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | The material coordinate, $\mathbf{x} = x e_1 + y e_2 + z e_3$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form; identity matrix $\mathrm{diag}(+1,+1,+1,+1)$ as a metric on $\mathbb{C}$ (level 1), signature $(3,1)$ on $\mathbb{M}_-$ (level 2) |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric, signature $(-,+,+,+)$ (level 2) |
| $g$ | Clifford metric of the $\gamma^\mu$ (level 3); an optional tool, not a framework convention. $\mathrm{diag}(+1,-1,-1,-1)$ throughout — the $\mathbb{M}_+$ form, matching the objects the tool represents |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}$ | Biquaternionic gradient and its conjugate |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$ | d'Alembertian, series convention |
| $\Box_{\text{Weyl}} = -\Box$ | d'Alembertian of the Weyl-spinor exercise, opposite sign |
| $\mathrm{Tr}(\tilde{X}\tilde{Y}) = 2\,\mathrm{Sc}(\tilde{X}\tilde{Y})$ | Trace pairing, unrestricted; the case $\tilde{P}\in\mathbb{M}_+$, $\tilde{H}\in\mathbb{M}_+$ is the real one. $\mathrm{Tr}(e_0) = 2$ |
| $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ | The matrix representation, with $\Phi(e_0) = I_2$ and $\sigma_k = i\,\Phi(e_k) = \Phi(ie_k)$. Fixed up to a unitary change of basis, and no further |
| $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$ | Chiral decomposition of the Dirac field |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$ | The linear, chirality-off-diagonal mass term (canonical form) |
| $SL(2,\mathbb{C})$ | Unit-norm biquaternions, the Lorentz group on $\mathbb{M}_-$ |

## Further Reading

- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the original quaternion algebra and its units.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and its mass term.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard treatment of spinors and the chiral structure of the Dirac field.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard particle-physics metric and gamma-matrix conventions.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the metric and normalisation conventions of quantum field theory, and the consequences of changing them.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents, minimal left ideals, and the conjugations of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for real structures and real forms on Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Dirac equation and its mass term.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in geometric algebra.
