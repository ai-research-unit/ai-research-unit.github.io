# __Square Roots of One and the Idempotents: the Hermitian Observables and the States__

## Introduction

Of the four general products of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, exactly one makes the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ an associative unital $\mathbb{C}$-algebra: the general plain bilinear product $\tilde Q_1\tilde Q_2$, the multiplication of the algebra, read throughout this article.

The article reads that product at the central value $+1$. The **roots of $+1$** are the elements $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi^2=e_t$; the **idempotents** are the elements $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$. The two subjects are one subject, because the **halving map**

$$
\tilde\Xi\longmapsto\tilde\Pi=\tfrac12(e_t+\tilde\Xi),\qquad \tilde\Xi^2=e_t,
$$

is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_t$. A root carries two idempotents and not one: with

$$
\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi),\qquad \tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi),
$$

the two are a complete orthogonal pair, $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$, the root is their difference, $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$, and multiplication by the root acts by $+1$ on $\tilde\Pi_+$ and by $-1$ on $\tilde\Pi_-$. The pair, not the single idempotent, is the spine of the article: a root is an operator of square one, and its pair is the two projections onto its eigenspaces.

The three families of roots, and the idempotents they carry, are the mathematics of *Square Roots of One and the Idempotents of the Biquaternion Algebra*: the trivial roots $\pm e_t$; the purely imaginary roots $\pm i\tilde\xi$ over the pure real quaternions $\tilde\xi$ with $\tilde\xi^2=-e_t$; and the non-trivial roots $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and two real conditions. That article owns them; they are cited and read here, not re-proved.

**The physical interpretation.** The content added here is a reading. The **Hermitian roots of $+1$** — the trivial $\pm e_t$ and the purely imaginary family $\pm i\tilde\xi$ — are read as **Hermitian observables**, and the idempotents they carry as **states**. A Hermitian root is a Hermitian element whose square is the identity, an observable whose only values are $\pm1$; its two idempotents $\tilde\Pi_\pm$ are its two spectral projections, and they are the two pure states of the observable, because the Hermitian idempotents of the algebra are exactly the pure states of the informational sector. The observable and its two states are the two faces of one root. The roots of $-1$, read off the roots of $+1$ by the central imaginary, are the framework's **local complex structures**, and are the closing section of the article.

The roots of $+1$ are the first of the three central values of the algebra; the roots of $0$ and the light cone are *Square Roots of Zero and the Nilpotents: the Light Cone*; the general quadratic is *Square Roots of a General Element in the Biquaternion Algebra: the Realisation*. The product and the algebra are *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* and *Introduction to the Biquaternion Algebra*; the informational sector is *The Hermitian Subspace M₊ as the Informational Sector*; the pure states and the Bloch ball are *The Bloch Ball as the Trace-One Slice of the Future Light Cone* and *The Ontology of the Quantum State under the Biquaternion Framework*; the observables and their composition are *Square Roots of One and the Idempotents: the Hermitian Observables and the States*; the state as an idempotent is *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*; the projection reading of decoherence is *Decoherence as Idempotent Projection*; and the local complex structure is *The Local Complex Structure and the Speed of Light*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=\sum_{k=1}^{3}Q_k\vec e_k$. The general plain bilinear form of two vector parts is

$$
(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k,
$$

and the square of a pure element is $\vec Q^2=-(\vec Q,\vec Q)e_t$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$ and the Hermitian conjugation is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$; the sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\Pi$ (§*The Idempotent Convention*), and the two members of a complete pair carry the signs, $\tilde\Pi_+$ and $\tilde\Pi_-$. Orthogonality of projections is read from the Hermitian form of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, which is named and not used.

## The Square and the Two Branches

The square of a biquaternion is the two-term expression

$$
\tilde Q^2=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)e_t+2Q_t\vec Q .
$$

For the equation $\tilde\Xi^2=e_t$, with $\tilde\Xi=\Xi_te_t+\vec\Xi$, the vector part and the scalar part separate:

$$
2\Xi_t\vec\Xi=0,\qquad \Xi_t^2-(\vec\Xi,\vec\Xi)=1 .
$$

Since $\mathbb{C}$ is a field, the vector equation holds exactly when $\Xi_t=0$ or $\vec\Xi=0$: a root of $+1$ is either a **complex scalar** or **pure**, and the two branches are disjoint and exhaustive. The scalar branch carries the two central roots and the pure branch the two families of pure roots; this is the whole of the classification.

**The roots are units.** A root of $+1$ satisfies $\tilde\Xi\tilde\Xi=e_t$, so it is invertible with two-sided inverse $\tilde\Xi^{-1}=\tilde\Xi$, and a unit is never a zero divisor. The roots of $+1$ therefore lie outside the zero-divisor cone, in contrast to the roots of $0$ of the companion article.

## The Roots of One

**The roots of $+1$ are the two central scalars $\pm e_t$; the two-real-parameter family $\pm i\tilde\xi$ over the pure real quaternions $\tilde\xi$ with $\tilde\xi^2=-e_t$; and the four-real-parameter family $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions. There are no others.**

The classification is the one of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, recalled here in its three families.

### The Trivial Roots

The scalar branch gives $\tilde\Xi=\Xi_te_t$ with $\Xi_t^2=1$, hence the two **trivial roots** $\pm e_t$. They are the only roots in the centre $\mathbb{C}e_t$ and the only ones with a non-vanishing scalar part. They are Hermitian and central.

### The Purely Imaginary Roots

The pure branch of the form $\vec\Xi=i\tilde\xi$ with $\tilde\xi$ a pure real quaternion gives $(i\tilde\xi)^2=i^2\tilde\xi^2=-\tilde\xi^2$, so $i\tilde\xi$ is a root of $+1$ exactly when $\tilde\xi^2=-e_t$, that is when $\tilde\xi$ is a unit pure real quaternion. The roots are the **two-real-parameter family**

$$
\tilde\Xi=\pm i\tilde\xi,\qquad \tilde\xi=\xi_x\vec e_x+\xi_y\vec e_y+\xi_z\vec e_z,\ \xi_k\in\mathbb{R},\ \xi_x^2+\xi_y^2+\xi_z^2=1 .
$$

The two signs give the same set, since $-i\tilde\xi=i(-\tilde\xi)$ and $-\tilde\xi$ is again on the sphere; the family is one root for each point of the real unit sphere. Each member is **Hermitian**, $(i\tilde\xi)^{*}=i\tilde\xi$, because $i$ is central and $\tilde\xi$ is a real vector. These are the **Hermitian roots** of $+1$.

### The Non-Trivial Roots

The remaining pure roots have genuinely complex vector part, $\vec\Xi=\vec\xi+i\vec\xi'$ with $\vec\xi,\vec\xi'$ real pure. The single complex equation $(\vec\Xi,\vec\Xi)=-1$ is the two real conditions

$$
\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=-1,\qquad \xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0,
$$

equivalently $\vec\xi\vec\xi'+\vec\xi'\vec\xi=0$. The case $\vec\xi=0$ is the purely imaginary family; the case $\vec\xi\neq0$ is the **four-real-parameter family** of **non-trivial roots**. For such a root the imaginary part is automatically nonzero, so no real pure root of $+1$ exists: a real vector would need $(\vec q,\vec q)=\lvert\vec q\rvert^{2}=-1$. The non-trivial roots are not real and, in general, not Hermitian.

### A Table of the Roots

| family | elements | parameters | Hermitian |
|---|---|---|---|
| trivial | $\pm e_t$ | two isolated | yes, central |
| purely imaginary | $\pm i\tilde\xi$, $\tilde\xi$ real pure of square $-e_t$ | two real | yes |
| non-trivial | $\vec\xi+i\vec\xi'$, $\vec\xi\neq0$, two real conditions | four real | no |

## The Idempotents and the Halving Map

**Every idempotent of $\mathbb{B}$ is $0$, $e_t$, or of the form $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; the halving map is a bijection from the roots of $+1$ onto the idempotents; and each root carries the complete orthogonal pair $\tilde\Pi_\pm$.**

An **idempotent** is an element with $\tilde\Pi^2=\tilde\Pi$, the square being the multiplication of the algebra. The **halving map** $\tilde\Xi\mapsto\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_t$; the companion **pair map** $\tilde\Xi\mapsto(\tilde\Pi_+,\tilde\Pi_-)$ is a bijection from the roots onto the ordered complete orthogonal pairs of idempotents. Both computations are two lines: if $\tilde\Xi^2=e_t$ then $\tfrac14(e_t+\tilde\Xi)^2=\tfrac14(e_t+2\tilde\Xi+e_t)=\tfrac12(e_t+\tilde\Xi)$, and if $\tilde\Pi^2=\tilde\Pi$ then $(2\tilde\Pi-e_t)^2=4\tilde\Pi-4\tilde\Pi+e_t=e_t$.

The families of idempotents are the families of the roots read through the map.

- The trivial roots give the **trivial idempotents** $e_t$ and $0$.
- The purely imaginary roots give the **Hermitian idempotents** $\tilde\Pi_\pm(i\tilde\xi)=\tfrac12(e_t\pm i\tilde\xi)$, a two-real-parameter family lying in the informational sector $\mathbb{M}_+$.
- The non-trivial roots give a **four-real-parameter family** of idempotents lying in none of the four four-dimensional remarkable subspaces.

Every idempotent and its complement split the algebra,

$$
\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_t-\tilde\Pi)\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_t-\tilde\Pi),
$$

the algebraic form of a projection and its complementary projection; a Hermitian idempotent is an **orthogonal** projection for the Hermitian form. The components of the pair are orthogonal and complete, and the root is their difference, so the pair is the spectral decomposition of the root.

**Idempotents, zero divisors and ideals.** The trivial idempotents $0$ and $e_t$ are not zero divisors, $e_t$ being a unit; every non-trivial idempotent is one, since $\tilde\Pi(e_t-\tilde\Pi)=0$, and conversely every non-pure zero divisor is a complex multiple $2Q_t\tilde\Pi$ of a non-trivial idempotent. The two minimal left ideals the standard pair generates and the Peirce decomposition it drives are *Ideals and Peirce Decomposition of the Biquaternion Algebra*; the zero-divisor structure is *Zero Divisors of the Biquaternion Algebra*.

## The Hermitian Roots as Observables

**The Hermitian roots of $+1$ are the trivial roots $\pm e_t$ and the purely imaginary family $\pm i\tilde\xi$; a Hermitian root is a Hermitian element of square $e_t$, read as a Hermitian observable whose values are $\pm1$.**

The Hermitian roots are exactly the roots that lie in the informational sector $\mathbb{M}_+$. A Hermitian element of the algebra has the form $\tilde H=h_te_t+i\vec h$ with $h_t\in\mathbb{R}$ and $\vec h$ a real pure quaternion, and its square is

$$
(h_te_t+i\vec h)^2=(h_t^2+\lvert\vec h\rvert^{2})e_t+2h_ti\vec h .
$$

The vector part vanishes only when $h_t=0$ or $\vec h=0$, and the two cases give the purely imaginary family and the pair $\pm e_t$. So the Hermitian roots are the trivial roots and the family $\pm i\tilde\xi$, and no non-trivial root is Hermitian.

**The interpretation.** A Hermitian root $\tilde\Xi$ has $\tilde\Xi^{*}=\tilde\Xi$ and $\tilde\Xi^2=e_t$. It is read as a **Hermitian observable** of the informational sector, and specifically as an observable whose only values are $\pm1$: an involution of the state space, a parity or a sign. The two central roots $\pm e_t$ are the trivial observables, the constants $+1$ and $-1$; the family $i\tilde\xi$ is the family of non-trivial such observables, one for each direction $\tilde\xi$ of the real unit sphere. The family has two real parameters because a direction on the sphere does.

Three worked roots fix the reading. The element $i\vec e_z$ is a Hermitian root, $(i\vec e_z)^{*}=i\vec e_z$ and $(i\vec e_z)^2=e_t$, and it is the standard one; $i\vec e_x$ is another; and the non-trivial root $\vec e_x+i(\vec e_y+\vec e_z)$ is a root but is not Hermitian, hence not an observable. The distinction is the content of the table of §*The Roots of One*.

**What the reading says and does not say.** It says that **the Hermitian roots of $+1$ are the involutive observables**, the observables of square one. It does not say that every observable of the framework is a root of $+1$: a general observable is a Hermitian element of arbitrary square, and the roots of $+1$ are the special, involutive ones. The reading is a naming, not a derivation. The roots are the mathematics of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, and the observables are the framework's own, owned by *Square Roots of One and the Idempotents: the Hermitian Observables and the States*.

## The Idempotents as States

**The Hermitian idempotents are the pure states of the informational sector; a Hermitian root carries its two eigenstates $\tilde\Pi_\pm$, the spectral projections of the observable; and the observable is the difference of its two states.**

A **Hermitian idempotent** is an idempotent with $\tilde\Pi^{*}=\tilde\Pi$. It is an orthogonal projection of the algebra, and it is a **pure state** of the informational sector: the family is the two-real-parameter family

$$
\tilde\Pi_\pm(i\tilde\xi)=\tfrac12(e_t\pm i\tilde\xi),\qquad \tilde\xi\in S^{2},
$$

the Bloch sphere of the pure states, the trivial projections $e_t$ and $0$ being the degenerate cases. The trace of a state is the central part, $\operatorname{Tr}\tilde\Pi=2\operatorname{Sc}\tilde\Pi=1$, and the pairing of a state with an observable is the Hermitian form of *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*.

**The spectral resolution.** For the Hermitian root $\tilde\Xi=i\tilde\xi$ the two idempotents are the spectral projections of the observable:

$$
\tilde\Xi\tilde\Pi_+=\tilde\Pi_+\tilde\Xi=\tilde\Pi_+,\qquad \tilde\Xi\tilde\Pi_-=\tilde\Pi_-\tilde\Xi=-\tilde\Pi_-,
$$

whence $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$, and the pair splits the algebra into the two eigenspaces. The observable and its two states are therefore one datum: the root gives the observable, the halving map gives its two states, and the difference returns the observable. This is the algebraic content of the reading that **the idempotents are the states of the observable**.

**The general idempotents are not states.** The non-trivial idempotents of the four-real-parameter family lie in no remarkable subspace and are not Hermitian; they are not states in the orthogonal-projection sense. The identification of idempotents with states is confined to the Hermitian ones, that is to the informational sector, and the trivial pair $e_t,0$ is the degenerate case. The mixed states, which are not idempotent, are the interior of the Bloch ball of *The Bloch Ball as the Trace-One Slice of the Future Light Cone*; the reading of the state as an idempotent of the algebra is that of *The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*, and the projection reading of decoherence is *Decoherence as Idempotent Projection*.

## The Roots of Minus One and the Local Complex Structure

**The central imaginary $i$ turns the roots of $+1$ into the roots of $-1$: the map $\tilde\Xi\mapsto i\tilde\Xi$ is a bijection. Read physically, a root of $-1$ is a local complex structure, a choice of what is called $i$ in a patch; the distinguished global choice is the central $i$ itself.**

If $\tilde\Xi^2=e_t$ then $(i\tilde\Xi)^2=i^2\tilde\Xi^2=-e_t$, because $i$ is central, and since $i$ is invertible the map is a bijection. The three families of the roots of $+1$ are carried to the three families of the roots of $-1$: the two central scalars $\pm i$; the family $\pm\tilde\xi$ over the pure real unit quaternions, the two-sphere $S^{2}$ of unit imaginary quaternions; and the family $-\vec\xi'+i\vec\xi$ with the same two real conditions. This is the closing remark of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, quoted here for the reading it carries.

**The interpretation.** A root of $-1$ is read as a **local complex structure**, a choice of which element plays the role of $i$ in a local patch. The central root $i$ is the distinguished choice, the one that commutes with every element and makes the algebra an algebra over $\mathbb{C}$; the remaining roots are local, each defining its own complex structure, and passing from one to another is a change of what plays the role of $i$. The physical interpretation — the local complex structure fixing the propagation of the fields and the speed of light of the patch — is owned by *The Local Complex Structure and the Speed of Light*.

**The two sectors.** The root of $-1$ is anti-Hermitian when its root of $+1$ is Hermitian: $i$ is anti-Hermitian, $i^{*}=-i$, so $(i\tilde\Xi)^{*}=\tilde\Xi^{*}i^{*}=-i\,\tilde\Xi^{*}$ for central $i$, and a Hermitian root of $+1$ is carried to an anti-Hermitian root of $-1$. The observables of the article therefore lie in the informational sector $\mathbb{M}_+$, and the local complex structures read off them lie in the material sector $\mathbb{M}_-$. The sign of the radicand separates the sector.

## The Interpretation

The two readings of the article are one: **a Hermitian root of $+1$ is an observable and its two idempotents are its states.**

- The Hermitian roots $\pm e_t$ and $\pm i\tilde\xi$ are the Hermitian observables of square one, the involutive observables of the informational sector; the non-Hermitian non-trivial roots are not observables.
- The Hermitian idempotents $\tilde\Pi_\pm$ are the pure states of the informational sector, the Bloch sphere; the non-Hermitian idempotents are not states.
- The root and its pair are the observable and its two eigenstates, related by the halving map and its inverse, the root being the difference of the pair; the eigenvalues of the observable are the two signs, carried by the two idempotents.

The roots of $-1$ carry the complementary reading: they are the local complex structures, the local choices of $i$, and they lie in the material sector. The classification is the mathematics of *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the readings are proposals about naming.

**What the framework does not claim.** The framework does not claim that every observable is a square root of $+1$, that every idempotent is a state, that quantum mechanics or the Born rule is derived here, or that one direction $\tilde\xi$ or one state is preferred. The identification of the Hermitian roots with observables and of the Hermitian idempotents with states is a reading of a classification, and the classification is the result.

## Summary

The general plain bilinear product of the biquaternion space is the multiplication of the algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$. The square roots of $+1$ in that product are the two central scalars $\pm e_t$, the two-real-parameter family $\pm i\tilde\xi$ over the pure real quaternions of square $-e_t$, and the four-real-parameter family $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions. All roots except the trivial ones are pure, every root is a unit with inverse itself, and no real pure root exists.

The idempotents are the trivial ones $0$ and $e_t$ and the elements $\tilde\Pi=\tfrac12(e_t\pm\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$. The halving map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_t$, and each root carries the complete orthogonal pair $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_t\pm\tilde\Xi)$, whose sum is $e_t$, whose product is $0$, and whose difference is the root; multiplication by the root acts by $+1$ on $\tilde\Pi_+$ and by $-1$ on $\tilde\Pi_-$. The three families of roots give the trivial idempotents, the Hermitian idempotents of $\mathbb{M}_+$ (a two-real-parameter family, the Bloch sphere of the pure states), and the non-trivial idempotents (a four-real-parameter family, lying in no remarkable subspace).

The readings are these. The **Hermitian roots of $+1$** are the **Hermitian observables** of square one, the involutive observables of the informational sector, the trivial roots being the constants $\pm1$ and the family $i\tilde\xi$ one observable per direction of the real unit sphere; the non-trivial roots are not observables. The **Hermitian idempotents** are the **pure states** of the informational sector; the two idempotents of a root are the two eigenstates of the observable, its spectral projections, and the observable is their difference. The **roots of $-1$**, read off the roots of $+1$ by the central imaginary, are the **local complex structures**, the local choices of $i$; they lie in the material sector and are owned by *The Local Complex Structure and the Speed of Light*. The readings are proposals about naming, labelled as such; the root sets, the halving map, the pair and the sector computation are results.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, the general plain algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\tilde\Xi$ | A root of $+1$, $\tilde\Xi^2=e_t$ |
| $\tilde\Xi=\Xi_te_t+\vec\Xi$, $\vec\Xi=\vec\xi+i\vec\xi'$ | Scalar and vector parts of a root; $\vec\xi,\vec\xi'$ real pure |
| $(\vec P,\vec Q)=\sum_kP_kQ_k$ | General plain bilinear form of two vector parts |
| $\tilde\Pi$ | An idempotent, $\tilde\Pi^2=\tilde\Pi$ |
| $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_t\pm\tilde\Xi)$ | The complete orthogonal pair of a root; $\tilde\Pi_+-\tilde\Pi_-=\tilde\Xi$ |
| $i\tilde\xi$, $\tilde\xi\in S^{2}$ | The purely imaginary roots; the Hermitian observables of square one |
| $\tilde\Pi_\pm(i\tilde\xi)$ | The Hermitian idempotents; the pure states of $\mathbb{M}_+$ |
| $i\tilde\Xi$ | A root of $-1$; a local complex structure |
| $\mathbb{M}_\pm$ | Informational and material sectors |
| $S^{2}$ | Real unit sphere, $S^{2}$ of unit imaginary quaternions |

## Further Reading

- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the two-sphere of roots of $-1$ in the complexified quaternions.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the idempotents of the algebra beside the nilpotents.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the idempotents, the isotropic cone and the structure of the complexified quaternions.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for idempotents, complete orthogonal sets and the structure of matrix algebras.
