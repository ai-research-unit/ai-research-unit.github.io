# __Biquaternion Idempotents and Projections__

## Introduction

The algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations, its six distinguished subspaces and the coordinate dictionary. This article treats the **idempotents** of $\mathbb{B}$ — the elements satisfying $\tilde\Pi^2 = \tilde\Pi$ — and the projections and direct sum decompositions they carry.

Algebraically, idempotents do four jobs at once in this algebra:

1. they give the direct sum decompositions into left ideals, and in particular the two minimal left ideals;
2. they classify the non-pure zero divisors, every one of which is a complex multiple of an idempotent;
3. they are in bijection with the roots of $-1$, so the classification of the idempotents is exactly the classification of those roots;
4. they drive the Peirce decomposition and the matrix-unit model of the algebra.

Physically, those four jobs are one subject read four ways. An idempotent is a **projector**: the two minimal left ideals are the one-particle modules on which the states of the theory live, the classification of the projectors is the classification of the **pure states of a qubit** as a two-sphere, the non-pure zero divisors are the null elements organised by the projectors, and the Peirce decomposition is the block structure of the algebra. Two consequences of the classification are the ones physics uses constantly: a rank-one projector is a **zero divisor** and therefore sits on the light cone, and the projectors that are orthogonal with respect to the Hermitian form are exactly the Hermitian idempotents, the projections of the spectral theorem.

The material here was previously distributed over the articles on ideals, on zero divisors, on the roots of $-1$ and over worked examples; it is collected here because the four statements above are one subject. Its proofs use only the algebra and norm articles: the roots of $-1$ enter as a parameter set whose classification is quoted from *Biquaternion Square Roots of Minus One, Zero and Plus One*, and the relations to the zero divisors and to the ideals are forward pointers.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ and $e_1e_2 = e_3$, central scalar imaginary $i$, and $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The scalar part is $Q_0$; a pure element is written $\mathbf{B} = B_1e_1+B_2e_2+B_3e_3$, and on pure elements the bilinear form is $(\mathbf{A},\mathbf{B}) = \sum_{k=1}^{3}A_kB_k$, so that $\mathbf{B}^2 = -(\mathbf{B},\mathbf{B})e_0$. The biquaternion norm is $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ and decides invertibility; the material coordinate is $ict\,e_0+\mathbf{x}$ and the informational coordinate is $ct'\,e_0+i\mathbf{x}'$.

## 1. Idempotents in an Algebra

Let $A$ be an associative unital algebra. An element $\tilde\Pi\in A$ is an **idempotent** if $\tilde\Pi^2 = \tilde\Pi$. Idempotents encode direct summands:

$$
A = A\tilde\Pi\oplus A(e_0-\tilde\Pi) \ (\text{left}), \qquad A = \tilde\Pi A\oplus (e_0-\tilde\Pi)A \ (\text{right}),
$$

and every such decomposition of the regular module arises from an idempotent. Two idempotents $\tilde\Pi,\tilde\Pi'$ are **orthogonal** if $\tilde\Pi\tilde\Pi' = \tilde\Pi'\tilde\Pi = 0$, and then $\tilde\Pi+\tilde\Pi'$ is again idempotent. A family is pairwise orthogonal if $\tilde\Pi_i\tilde\Pi_j = 0$ for $i\neq j$, and **complete** if in addition $\sum_i\tilde\Pi_i = e_0$. A nonzero idempotent is **primitive** if it is not a sum of two nonzero orthogonal idempotents. For a semisimple algebra,

$$
\tilde\Pi \text{ primitive} \iff A\tilde\Pi \text{ is a minimal left ideal} \iff \tilde\Pi A\tilde\Pi \text{ is a division ring},
$$

and since $\mathbb{B}\cong M_2(\mathbb{C})$ is semisimple, the criterion applies. It is the reason the idempotent theory and the ideal theory are two views of one subject.

**Physical reading: idempotent versus projection.** An idempotent element of the algebra acts on a state by the sandwich $\tilde{\rho}\mapsto \tilde\Pi\tilde{\rho}\tilde\Pi$, followed by normalisation, which is a projective measurement. The name "projection" is also used for a map on the state space with $\Phi\circ\Phi = \Phi$; that is a statement about an **operation**, not about an element, and the two are not the same. The distinction is worked out in *Decoherence as Idempotent Projection*: decoherence at partial strength is not idempotent as a channel, while a pure state is idempotent as an element. This article is about the element.

## 2. The Standard Idempotents of $\mathbb{B}$

Put

$$
\tilde\Pi_1 = \frac{e_0+ie_3}{2}, \qquad \tilde\Pi_2 = \frac{e_0-ie_3}{2}.
$$

Since $i$ is central and $(ie_3)^2 = i^2e_3^2 = (-1)(-1) = 1$, one has $\tilde\Pi_1^2 = \tilde\Pi_1$, $\tilde\Pi_2^2 = \tilde\Pi_2$ and

$$
\tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = \frac{e_0-(ie_3)^2}{4} = 0, \qquad \tilde\Pi_1+\tilde\Pi_2 = e_0 .
$$

So $\tilde\Pi_1$ and $\tilde\Pi_2$ are orthogonal idempotents summing to the unit. They are not central: $e_1$ anticommutes with $ie_3$ and hence does not commute with $\tilde\Pi_1$ or $\tilde\Pi_2$. Under $\mathbb{B}\cong M_2(\mathbb{C})$ they are the diagonal matrix units,

$$
\Phi(\tilde\Pi_1) = \tfrac{1}{2}(I_2+\sigma_3) = \mathrm{diag}(1,0) = E_{11}, \qquad \Phi(\tilde\Pi_2) = \tfrac{1}{2}(I_2-\sigma_3) = \mathrm{diag}(0,1) = E_{22},
$$

and each is primitive. Left multiplication by $e_3$ and by $e_2$ acts on them as

$$
e_3\tilde\Pi_1 = -i\tilde\Pi_1, \qquad e_3\tilde\Pi_2 = i\tilde\Pi_2, \qquad e_2\tilde\Pi_1 = ie_1\tilde\Pi_1,
$$

the first two because $e_3\tilde\Pi_1 = (e_3+i e_3^2)/2 = (e_3-i)/2 = -i\tilde\Pi_1$ and similarly for $\tilde\Pi_2$. The consequence used in Section 7 is that the four products $e_\mu \tilde\Pi_1$ reduce to $\tilde\Pi_1$ and $e_1\tilde\Pi_1$, so $\{\tilde\Pi_1,e_1\tilde\Pi_1\}$ is a basis of $\mathbb{B}\tilde\Pi_1$ over $\mathbb{C}$.

**Physical reading: the two projectors of a qubit mode.** The pair $\{\tilde\Pi_1,\tilde\Pi_2\}$ is the pair of orthogonal rank-one projectors of a single two-state system: $\tilde\Pi_1$ projects onto one state and $\tilde\Pi_2$ onto its orthogonal complement. In the quantum-mechanical articles the two are read as the state and its complement, for instance the vacuum projector $\tilde\Pi_1 = \tilde\Pi(e_3) = |0\rangle\langle 0|$ and its occupied counterpart $\tilde\Pi_2$, whose sum is the resolution of the identity. Their matrix traces are $\mathrm{Tr}\,\Phi(\tilde\Pi_1) = \mathrm{Tr}\,\Phi(\tilde\Pi_2) = 1$: they are rank-one projectors, and the trace of a rank-one projector is the normalisation that makes it a state. **Both are zero divisors**, $N(\tilde\Pi_1) = N(\tilde\Pi_2) = 0$ by the norm article's criterion, which is the algebra's statement that a rank-one projector is not invertible; a pure state is a null element of the algebra, and the choice of a pure state is the choice of a null direction.

## 3. The Classification of the Idempotents

**Theorem.** Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_0$) or of the form

$$
\tilde\Pi = \tfrac{1}{2}e_0 \pm \tfrac{1}{2}\xi i ,
$$

where $\xi \in \mathbb{B}$ is a root of $-1$, $\xi^2 = -1$. There are no other idempotents.

**Proof.** Write $\tilde\Pi = Ae_0+\mathbf{B}$ with $A\in\mathbb{C}$ and $\mathbf{B}$ pure. Then

$$
\tilde\Pi^2 = \left(A^2-(\mathbf{B},\mathbf{B})\right)e_0 + 2A\mathbf{B} .
$$

Equating to $\tilde\Pi = Ae_0+\mathbf{B}$ gives

$$
A^2-(\mathbf{B},\mathbf{B}) = A, \qquad 2A\mathbf{B} = \mathbf{B} .
$$

If $\mathbf{B} = 0$ then $A^2 = A$, so $A = 0$ or $A = 1$: the trivial idempotents. If $\mathbf{B}\neq0$ the second equation gives $A = 1/2$, and the first then gives $(\mathbf{B},\mathbf{B}) = -1/4$. Define $\xi = -2i\mathbf{B}$; then $\xi$ is pure and

$$
(\xi,\xi) = \sum_{k=1}^{3}(-2iB_k)^2 = -4\sum_{k=1}^{3}B_k^2 = -4(\mathbf{B},\mathbf{B}) = 1 ,
$$

so $\xi^2 = -(\xi,\xi) = -1$ and $\mathbf{B} = \xi\cdot(i/2)$, giving $\tilde\Pi = \tfrac{1}{2}e_0+\tfrac{1}{2}\xi i$. The sign choice arises from replacing $\xi$ by $-\xi$, itself a root of $-1$.

The trivial idempotents correspond to the degenerate roots $\xi = \pm i$: with $\xi = i$, $\tilde\Pi_1 = \tfrac12 e_0+\tfrac12 i\cdot i = 0$; with $\xi = -i$, $\tilde\Pi_1 = \tfrac12 e_0-\tfrac12 i\cdot i = e_0$.

The classification is a classification only because the roots of $-1$ are classified, which is the subject of *Biquaternion Square Roots of Minus One, Zero and Plus One*. The three families it produces — the trivial roots $\pm i$, the real roots $\pm\mu$ over unit pure real quaternions $\mu$, and the non-trivial roots $b\mu+d\nu i$ — give the three families of idempotents of Section 4.

**Physical reading.** The theorem says that a projector in this algebra has no free parameter beyond **one direction**: an idempotent is a unit plus a direction $\xi$, halved. That is why the set of projectors is a sphere and not a larger manifold, and why a measurement in the framework is specified by a direction.

## 4. The Bijection With the Roots of Minus One

**Theorem.** The map

$$
\xi \longmapsto \tilde\Pi(\xi), \qquad \tilde\Pi(\xi) = \tfrac{1}{2}(e_0+\xi i),
$$

is a **bijection** from the set of roots of $-1$ onto the set of idempotents of $\mathbb{B}$.

**Proof.** *Well defined:* if $\xi^2 = -1$ then

$$
\tilde\Pi(\xi)^2 = \tfrac14(e_0+\xi i)^2 = \tfrac14\left(e_0+2\xi i+\xi^2i^2\right) = \tfrac14(e_0+2\xi i+1) = \tilde\Pi(\xi).
$$

*Injective:* $\tilde\Pi(\xi) = \tilde\Pi(\xi')$ gives $\xi i = \xi' i$, hence $\xi = \xi'$. *Surjective:* the classification says every idempotent is $\tfrac12e_0\pm\tfrac12\xi i$, and $\tilde\Pi(-\xi) = \tfrac12(e_0-\xi i)$ with $-\xi$ again a root.

Consequently the **complementary pairs** $\{\tilde\Pi, e_0-\tilde\Pi\}$ are in bijection with the roots modulo the sign identification $\xi\sim-\xi$, since $\tilde\Pi(-\xi) = e_0-\tilde\Pi(\xi)$: the two members of a pair correspond to the class $\{\xi,-\xi\}$.

Substituting the three families of roots:

- **Trivial roots** $\xi = \pm i$: $\tilde\Pi = 0$ or $\tilde\Pi = e_0$, the trivial idempotents. Physically these are the degenerate projectors: no state and everything.
- **Real roots** $\xi = \pm\mu$ with $\mu$ a unit pure real quaternion: $\tilde\Pi = \tfrac12e_0\pm\tfrac12\mu i$. Since $\mu i$ is Hermitian when $\mu$ is, $(\mu i)^{*} = \mu i$, these are the **Hermitian idempotents**. They lie in the informational sector $\mathbb{M}_+$ and are the **rank-one projectors**: the pure states of a qubit, and the one-mode vacua. The family is parametrised by the unit sphere of pure real quaternions, that is by $\hat{\boldsymbol\mu}\in S^2$,
$$
  \tilde\Pi(\hat{\boldsymbol\mu}) = \tfrac{1}{2}\left(e_0+i\hat{\boldsymbol\mu}\right),
$$
  which is the **Bloch sphere** of the state space, and the orbit of one vacuum under the rotations is the vacuum manifold. See *The Biquaternion Vacuum as a Minimal Idempotent* and *Quantum Physics in Biquaternionic Form*.
- **Non-trivial roots** $\xi = b\mu+d\nu i$: $\tilde\Pi = \tfrac12e_0\pm\tfrac12(b\mu i-d\nu)$, idempotents combining a real scalar part, a real vector part in the direction of $\nu$ and an imaginary vector part in the direction of $\mu$. Their vector part mixes a real and an imaginary direction, so they lie in none of the four four-dimensional subspaces, and they are **not** Hermitian: they are idempotents of the algebra but not orthogonal projections, hence not pure states in the sense the quantum articles use. They are the projectors that appear in the Peirce decomposition.

**A note on the null property.** Every idempotent of the classification has $N(\tilde\Pi) = 0$: for $\tilde\Pi = \tfrac12(e_0+\xi i)$,

$$
N(\tilde\Pi) = \tfrac14\left(1+\xi^2i^2+2\xi i\right)\Big|_{\text{scalar}} = \tfrac14(1 - 1) = 0 ,
$$

and the same for the other sign. So **every nontrivial idempotent is a zero divisor**, and, by the norm article's criterion, a projector is never invertible. Physically: a pure state is a null element, and the two facts "the vacuum is idempotent" and "the vacuum lies on the zero-divisor cone" are one fact.

## 5. Idempotents as Projections

An idempotent $\tilde\Pi$ satisfies $\tilde\Pi^2 = \tilde\Pi$; its **complement** $e_0-\tilde\Pi$ is also idempotent, and $\tilde\Pi(e_0-\tilde\Pi) = \tilde\Pi-\tilde\Pi^2 = 0$, so the pair gives a direct sum decomposition of the underlying $\mathbb{C}$-module,

$$
\mathbb{B} = \tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B}, \qquad \text{and equally} \qquad \mathbb{B} = \mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_0-\tilde\Pi) .
$$

This is the algebraic content of the statement that idempotents are projections: the idempotent is the projection, its complement the complementary projection, and the algebra splits into their images.

A **Hermitian idempotent**, $\tilde\Pi^{*} = \tilde\Pi$, is an **orthogonal** projection with respect to the Hermitian form, and it is the kind that occurs in the spectral decomposition of a Hermitian element. Since $\tilde\Pi^{*} = \tilde\Pi$, the Hermitian idempotents are exactly the second family of Section 4 and lie in $\mathbb{M}_+$.

**Physical reading: the projection, the state and the measurement.** The Hermitian idempotents of $\mathbb{M}_+$ are the pure states, and the pairing of one with an observable gives the Born probability through the trace; the spectral decomposition of an observable is a sum of orthogonal Hermitian idempotents. The two objects called "projection" must be kept apart here as well: the **idempotent element** $\tilde\Pi$ is a state, and the **sandwich** $\tilde{\rho}\mapsto\tilde\Pi\tilde{\rho}\tilde\Pi$ is the measurement operation; the operation squares to itself only in the idealised case, while the state is idempotent by definition. The passage from a pure state (idempotent) to a mixed state (not idempotent) is the subject of *Decoherence as Idempotent Projection*, and the pairing with the Born rule is in *Quantum Physics in Biquaternionic Form*.

## 6. Idempotents and the Non-Pure Zero Divisors

A nontrivial idempotent is a zero divisor, since $\tilde\Pi(e_0-\tilde\Pi) = 0$ with both factors nonzero unless $\tilde\Pi$ is $0$ or $e_0$. Conversely, every **non-pure** zero divisor — every zero divisor with $Q_0\neq0$ — is a complex multiple of a nontrivial idempotent,

$$
\tilde{Q} = 2Q_0\tilde\Pi, \qquad \tilde\Pi = \frac{\tilde{Q}}{2Q_0} .
$$

The derivation, from the square relation $\tilde{Q}^2 = 2Q_0\tilde{Q}$ that the non-pure family satisfies, together with the structure of the two families, is the subject of *Biquaternion Zero Divisors*.

**Physical reading.** The non-pure null elements of the material sector — the null four-vectors with nonvanishing time component, to which the light cone belongs — are parametrised by the projectors, so the light cone is organised by the same sphere that carries the pure states. That coincidence is what makes a null direction and a state direction the same kind of datum in this framework.

## 7. Idempotents and the Minimal Left Ideals

**Proposition.** The left ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ satisfy $\mathbb{B} = \mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$ as left $\mathbb{B}$-modules, and each has dimension 2 over $\mathbb{C}$ and 4 over $\mathbb{R}$ and is a minimal left ideal.

**Proof.** Every $\tilde{Q}$ satisfies $\tilde{Q} = \tilde{Q}(\tilde\Pi_1+\tilde\Pi_2) = \tilde{Q}\tilde\Pi_1+\tilde{Q}\tilde\Pi_2$, and the intersection is zero because $\tilde\Pi_1\tilde\Pi_2 = 0$: if $\tilde{Q}\tilde\Pi_1 = \tilde\Pi\tilde\Pi_2$ then multiplying on the right by $\tilde\Pi_1$ gives $\tilde{Q}\tilde\Pi_1 = 0$. For the dimension, the relations $e_3\tilde\Pi_1 = -i\tilde\Pi_1$ and $e_2\tilde\Pi_1 = ie_1\tilde\Pi_1$ reduce the products $e_\mu \tilde\Pi_1$ to $\tilde\Pi_1$ and $e_1\tilde\Pi_1$, which are independent over $\mathbb{C}$, so $\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde\Pi_1\oplus\mathbb{C}e_1\tilde\Pi_1$ has $\mathbb{C}$-dimension 2 and $\mathbb{R}$-dimension 4; the two ideals then span $4+4 = 8 = \dim_{\mathbb{R}}\mathbb{B}$. Minimality is read in the matrix model: $\Phi(\tilde\Pi_1) = E_{11}$ and $\Phi(\tilde\Pi_2) = E_{22}$, so $\mathbb{B}\tilde\Pi_1$ corresponds to the matrices whose only nonzero column is the first, a minimal left ideal of $M_2(\mathbb{C})$.

**Proposition.** The minimal left ideal $\mathbb{B}\tilde\Pi_1$ is isomorphic to $\mathbb{C}^2$ as a left $\mathbb{B}$-module, and the central element $i$ acts on it as multiplication by $i$.

**Proof.** Every element of $\mathbb{B}\tilde\Pi_1$ is uniquely $\alpha \tilde\Pi_1+\beta e_1\tilde\Pi_1$ with $\alpha,\beta\in\mathbb{C}$, so $\alpha \tilde\Pi_1+\beta e_1\tilde\Pi_1\mapsto(\alpha,\beta)$ is a bijection onto $\mathbb{C}^2$; left multiplication by $\tilde{Q}'$ sends $\tilde{Q}\tilde\Pi_1$ to $(\tilde{Q}'\tilde{Q})\tilde\Pi_1$, again in $\mathbb{B}\tilde\Pi_1$ and linear in the coordinates, so the assignment is an isomorphism of left $\mathbb{B}$-modules; and since $i$ is central, $i(\alpha \tilde\Pi_1+\beta e_1\tilde\Pi_1) = (i\alpha)\tilde\Pi_1+(i\beta)e_1\tilde\Pi_1$.

**Corollary.** $\mathbb{B}$ is a free left module of rank one over itself, $\mathbb{B} = \mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$; each summand is a simple left $\mathbb{B}$-module isomorphic to $\mathbb{C}^2$, and since $M_2(\mathbb{C})$ is simple the two summands are isomorphic and correspond to the two columns.

**Physical reading: the one-particle modules.** The summands are the modules on which the states of the theory live; they are the two-complex-dimensional one-particle (spinor) spaces. Both summands are copies of the **same** defining module, since $M_2(\mathbb{C})$ has a single simple module up to isomorphism, and this is the point at which a common misreading has to be blocked: the ideal decomposition $\mathbb{B} = \mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$ is **not** a chirality decomposition. The spinor module's chiral decomposition is a different decomposition of a different object. Three decompositions of the framework are in play and must not be conflated:

- the **ideal (Peirce) decomposition**, $\mathbb{B} = \mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$, by the primitive idempotents, acting on the **algebra** by right multiplication, with two summands that are *both* copies of the defining module;
- the **sector decomposition**, by Hermitian conjugation ${}^{*}$, splitting the **algebra** into $\mathbb{M}_-$ and $\mathbb{M}_+$, with projectors $\tilde{Q}\mapsto\tfrac12(\tilde{Q}\mp\tilde{Q}^{*})$;
- the **chiral decomposition**, by $\gamma_5$, splitting the **spinor module** $\Delta$ into $S\oplus\bar{S}$, with projectors $\tilde\Pi_L, \tilde\Pi_R$.

The three share no projector: $\tilde\Pi_L$ is not $\tilde\Pi_1$ or $\tilde\Pi_2$, and the sector split is not the chirality split; the comparison is made in full in *Chiral Fermions in the Biquaternion Framework*. The module itself — its dual, its conjugate and the reality conditions on it — is developed in *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and *The Native Qubit and the Defining Module of the Biquaternion Algebra*.

## 8. The Dimension of the Set of Idempotents

The idempotents correspond bijectively to the roots of $-1$ and inherit the size of that set. The roots form a stratified space of real dimension 4 — the non-trivial family $b\mu+d\nu i$ — with a two-dimensional boundary stratum (the real roots, $S^2$) and two isolated points (the trivial roots $\pm i$).

The trivial roots map to $0$ and $e_0$, which are excluded, so among the **nontrivial** idempotents there are no isolated points: they form a set of real dimension 4 with a two-dimensional boundary stratum inherited from the real roots. The nontrivial idempotents sit inside the six-real-dimensional zero divisor set of $\mathbb{B}$, and the trivial ones outside it.

**Physical reading.** The two-dimensional stratum is exactly the set of physical projectors: the Hermitian idempotents $\tilde\Pi(\hat{\boldsymbol\mu})$, $\hat{\boldsymbol\mu}\in S^2$, the Bloch sphere of pure states and the vacuum manifold. The four-dimensional family is the non-Hermitian idempotents, which are algebraically legitimate and are used by the Peirce decomposition, but are **not** orthogonal projections and so are not states. The dimension statements for the roots themselves are in *Biquaternion Square Roots of Minus One, Zero and Plus One*.

## Summary

An idempotent of $\mathbb{B}$ is an element with $\tilde\Pi^2 = \tilde\Pi$. The standard orthogonal idempotents are

$$
\tilde\Pi_1 = \tfrac12(e_0+ie_3), \qquad \tilde\Pi_2 = \tfrac12(e_0-ie_3), \qquad \tilde\Pi_1\tilde\Pi_2 = 0, \qquad \tilde\Pi_1+\tilde\Pi_2 = e_0,
$$

corresponding to the diagonal matrix units and giving $\mathbb{B} = \mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$, two minimal left ideals each isomorphic to $\mathbb{C}^2$ as a left $\mathbb{B}$-module — the one-particle modules. Every idempotent is trivial or of the form $\tfrac12e_0\pm\tfrac12\xi i$ with $\xi^2 = -1$, and $\xi\mapsto\tfrac12(e_0+\xi i)$ is a bijection from the roots of $-1$ onto the idempotents, under which complementary pairs correspond to the classes $\{\xi,-\xi\}$. The three root families give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$ and the idempotents lying in none of the four four-dimensional subspaces.

Physically, the Hermitian idempotents are the pure states: the rank-one projectors of a qubit, parametrised by the Bloch sphere $S^2$, with the one-mode vacuum among them, and the orbit of one vacuum under rotations is the vacuum manifold. Every nontrivial idempotent is a zero divisor, so a pure state is a null element of the algebra and a projector is never invertible. The non-pure zero divisors are the complex multiples of the idempotents, so the light cone is organised by the projectors. The idempotents and their complements split the algebra, which is the algebraic form of a projection and its complementary projection; and the Peirce, sector and chiral projectors are three distinct notions acting on the algebra and on the module respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi, \tilde\Pi', \tilde\Pi_1, \tilde\Pi_2$ | Idempotents, $\tilde\Pi^2 = \tilde\Pi$ |
| $\tilde\Pi_1 = \tfrac12(e_0+ie_3)$, $\tilde\Pi_2 = \tfrac12(e_0-ie_3)$ | The standard orthogonal idempotents, $\tilde\Pi_1+\tilde\Pi_2 = e_0$ |
| $\xi$ | A root of $-1$, $\xi^2 = -1$ |
| $\tilde\Pi(\xi) = \tfrac12(e_0+\xi i)$ | The idempotent of $\xi$; $\xi\mapsto \tilde\Pi(\xi)$ is a bijection |
| $\tilde\Pi(\hat{\boldsymbol\mu}) = \tfrac12(e_0+i\hat{\boldsymbol\mu})$ | Hermitian idempotent; pure state; Bloch sphere; vacuum |
| $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The two minimal left ideals, each $\cong\mathbb{C}^2$; the one-particle modules |
| $(\mathbf{A},\mathbf{B}) = \sum_kA_kB_k$ | Bilinear form on the pure part, $\mathbf{B}^2 = -(\mathbf{B},\mathbf{B})e_0$ |
| $\mathbb{M}_+$ | Informational sector, containing the Hermitian idempotents |
| $\mathbb{M}_-$ | Material sector |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm; $N(\tilde\Pi) = 0$ for every nontrivial idempotent |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the idempotents of the biquaternion algebra and its matrix model.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the idempotent structure in the applied setting.
