# __Square Roots of a General Element in the Biquaternion Algebra: the Realisation__

## Introduction

Of the four general products of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, exactly one makes the biquaternion space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ an associative unital $\mathbb{C}$-algebra: the general plain bilinear product $\tilde Q_1\tilde Q_2$, the multiplication of the algebra, read throughout this article.

The article reads that product at a general radicand. The **square-root problem** is: given $\tilde Q\in\mathbb{B}$, find every $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi^2=\tilde Q ,
$$

the square being the multiplication of the algebra. The solution is the mathematics of *Square Roots of a General Element in the Biquaternion Algebra*: the vector–scalar split turns the equation into one vector equation and one scalar equation, and the scalar equation is a quadratic in the square of the scalar part of a root. It is cited and read here, not re-proved.

**The results.** For a radicand with non-vanishing vector part the roots come in opposite pairs $\pm\tilde\Xi$: generically **four**, **two** in the two degenerate rows, and **none** for the rootless row. For a complex scalar radicand the roots are two central scalars together with a **four-real-parameter continuum**, the pure elements of prescribed complex square. The classification is the table of §*The Classification*.

**The physical interpretation.** The content added here is a reading. A material quantity is read as an element $\tilde Q$ of the algebra, and the quantity is said to be **realised by the algebra** when $\tilde Q$ has a square root, so that it is the square of some other element. The classification supplies the criterion: an element is rootless exactly when it is a **nonzero nilpotent**; and since the material sector $\mathbb{M}_-$ contains no nonzero nilpotent, **every material four-vector is realised**. The second reading is that the **mass shell** is a slice of the **natural square**, the norm $\nu(\tilde\Xi)=\tilde\Xi\tilde\Xi^{\natural}=\langle\tilde\Xi\rangle_{\natural}e_t$: the mass shell is the fibre of that map over the scalar $-m^{2}c^{2}$. The ordinary square of the article and the natural square of the mass shell are two different squares, and keeping them apart is the point of §*The Mass Shell as a Slice*. The reading "the mass shell is the fibre of the ordinary square" is **false** and is not made.

The roots of $+1$ and the idempotents are *Square Roots of One and the Idempotents: the Hermitian Observables and the States*; the roots of $0$, the nilpotents and the light cone are *Square Roots of Zero and the Nilpotents: the Light Cone*. The product and the algebra are *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* and *Introduction to the Biquaternion Algebra*; the norm, the zero-divisor cone and the group of units are *Norm and Invertibility in the Biquaternion Algebra* and *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*; the natural square, the interval and the mass shell are *The Four Forms, the Four Algebraic Norms and the Change of Scalars*; the separation of the ordinary square from the sesquilinear one is *Mass, Rank and the Positivity of the Dagger*; and the material sector is *The Anti-Hermitian Subspace M₋ as the Material Sector*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=Q_te_t+\vec Q$ with $Q_t\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The general plain bilinear form of two vector parts is $(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k$, and the square of a pure element is $\vec Q^2=-(\vec Q,\vec Q)e_t$. The **complex square of the vector part** is $(\vec Q,\vec Q)=Q_x^2+Q_y^2+Q_z^2$ and the **conjugate scalar** is $n=Q_t^2+(\vec Q,\vec Q)$, the scalar of the identity $\tilde Q\tilde Q^{\natural}=n\,e_t$. The scalar $n$ is the **norm** $\langle\tilde Q\rangle_{\natural}$ of *Norm and Invertibility in the Biquaternion Algebra*, written $n$ here to match the mathematics companion; one scalar, two names. The sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), a nilpotent $\tilde\Upsilon$, and the generic element $\tilde Q$.

## The Reduction and the Reduced Quadratic

Write the root and the radicand in scalar and vector parts,

$$
\tilde\Xi=\Xi_te_t+\vec\Xi,\qquad \tilde Q=Q_te_t+\vec Q,
$$

with all coefficients in $\mathbb{C}$. The product formula gives the square of $\tilde\Xi$ as

$$
\tilde\Xi^2=\bigl(\Xi_t^2-(\vec\Xi,\vec\Xi)\bigr)e_t+2\Xi_t\vec\Xi ,
$$

so equating $\tilde\Xi^2$ to $\tilde Q$ splits the equation into the vector part and the scalar part,

$$
2\Xi_t\vec\Xi=\vec Q,\qquad \Xi_t^2-(\vec\Xi,\vec\Xi)=Q_t .
$$

The vector equation decides the shape of the answer. If $\vec Q\neq0$ then $\Xi_t\neq0$ and $\vec\Xi=\vec Q/(2\Xi_t)$: a root is fixed by its scalar part. If $\vec Q=0$ then $\tilde Q$ is a complex scalar and the root is either a complex scalar or pure.

**The reduced quadratic.** In the first case, substituting $\vec\Xi=\vec Q/(2\Xi_t)$ into the scalar equation and putting $x=\Xi_t^2$ gives

$$
4x^{2}-4Q_tx-(\vec Q,\vec Q)=0,
$$

of discriminant $16n$ and solutions $x_\pm=\tfrac12(Q_t\pm\sqrt n)$. Each nonzero solution contributes the pair $\pm(\sqrt x\,e_t+\vec Q/(2\sqrt x))$.

## The Classification

**Every radicand falls into exactly one row below: four roots generically, two in the two degenerate rows, none for the rootless row, and a four-real-parameter continuum for a complex scalar.**

| condition on $\tilde Q=Q_te_t+\vec Q$ | number of roots |
|---|---|
| $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$, $n\neq0$ | four |
| $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$, $n=0$ | two |
| $\vec Q\neq0$, $(\vec Q,\vec Q)=0$, $Q_t\neq0$ | two |
| $\vec Q\neq0$, $n=0$, $Q_t=0$ | none |
| $\vec Q=0$ | a four-parameter family |

The generic case is four roots. The complex square $(\vec Q,\vec Q)$ decides whether a solution is lost at $x=0$; the conjugate scalar $n$ decides whether the two solutions of the reduced quadratic are distinct; and the vector part $\vec Q$ decides which of the two cases applies.

## The Roots in Each Case

**The roots are read off the rows of the table: a single pair in the degenerate rows, two pairs in the generic row, the empty set in the rootless row, and a continuum for a complex scalar.**

- **Four roots** when $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$ and $n\neq0$: two pairs, one for each solution of the reduced quadratic, $\tilde\Xi=\pm\bigl(\sqrt{x_+}\,e_t+\vec Q/(2\sqrt{x_+})\bigr)$ and $\tilde\Xi=\pm\bigl(\sqrt{x_-}\,e_t+\vec Q/(2\sqrt{x_-})\bigr)$.
- **Two roots** when $\vec Q\neq0$ and either $(\vec Q,\vec Q)\neq0$, $n=0$ (with $x=Q_t/2$) or $(\vec Q,\vec Q)=0$, $Q_t\neq0$ (with $x=Q_t$): a single pair.
- **No roots** when $\vec Q\neq0$, $(\vec Q,\vec Q)=0$, $n=0$ and $Q_t=0$.
- **A four-real-parameter family** when $\tilde Q=Q_te_t$ is a complex scalar: the two elements $\pm\sqrt{Q_t}e_t$ together with the pure $\vec\Xi$ with $(\vec\Xi,\vec\Xi)=-Q_t$, of whose real equations there are two, hence four free real parameters.

The roots always come in $\pm$ pairs when they are finite, so the finite root set is symmetric about the origin.

## The Square-Root Criterion and the Material Corollary

**An element has no square root exactly when it is a nonzero nilpotent; and every element of the material sector has a square root.**

The rootless row is $\vec Q\neq0$, $(\vec Q,\vec Q)=0$, $n=0$, $Q_t=0$, which is exactly the defining condition of a **nonzero nilpotent** of *Square Roots of Zero and the Nilpotents: the Light Cone*: pure, with isotropic vector part. Hence:

**Criterion.** The equation $\tilde\Xi^2=\tilde Q$ has no solution if and only if $\tilde Q$ is a nonzero nilpotent.

The material sector makes the criterion disappear. A material element is $\tilde Q=i a_0e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ with $a_0\in\mathbb{R}$, $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ a real vector; it satisfies $Q_t=ia_0$ and $(\vec Q,\vec Q)=\lvert x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\rvert^{2}$, so $n=-a_0^2+\lvert x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\rvert^{2}$. The rootless row needs $(\vec Q,\vec Q)=0$, which forces $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z=0$ and then $Q_t=0$, that is $\tilde Q=0$; so no nonzero material element is rootless.

**Corollary.** The material sector $\mathbb{M}_-$ contains no nonzero nilpotent, hence every material four-vector has a square root.

## The Mass Shell as a Slice

**The mass shell is a slice of the natural square $\nu(\tilde\Xi)=\tilde\Xi\tilde\Xi^{\natural}=\langle\tilde\Xi\rangle_{\natural}e_t$, not of the ordinary square; the natural square always lands in the centre, and the mass shell is its fibre over the scalar $-m^{2}c^{2}$.**

The article's square is the **ordinary** square $\sigma(\tilde\Xi)=\tilde\Xi\tilde\Xi$ of the plain product; the mass shell uses a different square, the **natural** square

$$
\nu(\tilde\Xi)=\tilde\Xi\tilde\Xi^{\natural}=\langle\tilde\Xi\rangle_{\natural}e_t,
$$

which is $\mathbb{C}$-valued and always lands in the centre. The two must be kept apart, and the separation is the one of *Mass, Rank and the Positivity of the Dagger*.

**The natural square and the interval.** On a material four-momentum $\tilde P=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ the natural square is the interval,

$$
\langle\tilde P\rangle_{\natural}=-c^{2}t^{2}+\lvert x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\rvert^{2},
$$

of signature $(-,+,+,+)$; its zero set cut by $\mathbb{M}_-$ is the light cone, and its level set $\langle\tilde P\rangle_{\natural}=-m^{2}c^{2}$ is the **mass shell**, developed in *The Four Forms, the Four Algebraic Norms and the Change of Scalars*. The mass is the label of the slice, and the mass shell is the **fibre** of the natural square map over that scalar. That the natural square is a scalar is automatic; what the mass-shell condition adds is the **value**.

**The scalar slice of the ordinary square.** For completeness, the ordinary square $\sigma$ lands in the centre exactly when $2\Xi_t\vec\Xi=0$, that is when the element is central ($\vec\Xi=0$) or pure ($\Xi_t=0$). The scalar slice of the ordinary square is therefore the union of the centre and the vector subspace, on which the square takes the values $\Xi_t^{2}$ and $-(\vec\Xi,\vec\Xi)$. This slice is **larger than the mass shell and is not the mass shell**; it is recorded because it is the set on which the ordinary square, like the natural one, is scalar, and it is the reason the two squares are easily confused. **The mass shell is not $\tilde P^{2}=-m^{2}c^{2}$ in the ordinary square.**

## The Reading: Realisation by the Algebra

**A material quantity is realised by the algebra exactly when its element has a square root; the unrealisable locus is the nonzero nilpotents; and the material sector carries no refusal.**

The reading is the following. A material quantity is read as an element $\tilde Q$ of the algebra, and it is said to be **realised by the algebra** when $\tilde Q$ is the square of some element. The criterion then reads as an existence condition on the quantity.

- A quantity whose element is **off the nilpotent locus** is realised: it has a square root, and the root is the element of which it is the square.
- A quantity whose element is a **nonzero nilpotent** is not realised: there is no element whose square it is, and the algebra refuses it.
- The **material sector carries no refusal**: by the corollary every material four-vector is realised.

**The non-uniqueness of the root.** The root is not unique: a generic element has four roots, a complex scalar a continuum. The reading has therefore no preferred root until an extra principle selects one, and this is its standing weakness. Read as structure rather than defect, the non-uniqueness says that **the roots of a quantity are the frames it can be referred to**, and choosing one is a choice of representative. Read the same way, the **mass shell** is the slice of the natural square on which the square takes the prescribed value $-m^{2}c^{2}$, and the mass is the label of the slice.

**What the framework does not claim.** The identification of the square-root criterion with a physical existence condition is a **proposal and not a result**. The framework does not claim that the nilpotent locus is unphysical, that every material quantity is a square in the physical sense, or that the mass shell is derived from the square map; it does not fix a mass spectrum, and it does not say which roots are physical. The root sets, the criterion and the material corollary are results; the words "realised", "refusal", "frame" and "mass as the label of the slice" are the reading.

## Summary

For a general $\tilde Q\in\mathbb{B}$ the square roots in the general plain product are found from the vector–scalar split $\tilde Q=Q_te_t+\vec Q$, $\tilde\Xi=\Xi_te_t+\vec\Xi$, which turns $\tilde\Xi^2=\tilde Q$ into the vector equation $2\Xi_t\vec\Xi=\vec Q$ and the scalar equation $\Xi_t^2-(\vec\Xi,\vec\Xi)=Q_t$. When $\vec Q\neq0$ a root has $\Xi_t\neq0$, $\vec\Xi=\vec Q/(2\Xi_t)$ and $x=\Xi_t^{2}$ solving the reduced quadratic $4x^{2}-4Q_tx-(\vec Q,\vec Q)=0$, of discriminant $16n$; each nonzero solution contributes the pair $\pm(\sqrt x\,e_t+\vec Q/(2\sqrt x))$. When $\vec Q=0$ the radicand is a complex scalar and the roots are the two elements $\pm\sqrt{Q_t}e_t$ and the four-real-parameter family of pure $\vec\Xi$ with $(\vec\Xi,\vec\Xi)=-Q_t$.

The number of roots is **four** generically, **two** in the two degenerate rows, **none** for the rootless row, and the **four-parameter family** for a complex scalar; the rootless row is exactly the condition that $\tilde Q$ be a **nonzero nilpotent**, and since the material sector contains no nonzero nilpotent every material four-vector has a square root.

The readings are these. A material quantity is **realised by the algebra** exactly when it has a square root; the **unrealisable locus** is the nonzero nilpotents; the **material sector carries no refusal**; and the **mass shell** is the fibre of the **natural square** $\nu(\tilde\Xi)=\tilde\Xi\tilde\Xi^{\natural}=\langle\tilde\Xi\rangle_{\natural}e_t$ over the scalar $-m^{2}c^{2}$, on the material sector the level set of the interval $-c^{2}t^{2}+\lvert x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\rvert^{2}$. The ordinary square and the natural square are distinct, and the scalar slice of the ordinary square is the centre together with the vector subspace, which is not the mass shell. The readings are proposals about naming, labelled as such; the classification, the criterion, the corollary and the nesting of the two squares are results. The standing weakness is the non-uniqueness of the root.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, the general plain algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\tilde Q=Q_te_t+\vec Q$ | Radicand; scalar and vector parts |
| $\tilde\Xi=\Xi_te_t+\vec\Xi$ | A square root of $\tilde Q$ |
| $(\vec Q,\vec Q)=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | Complex square of the vector part |
| $n=Q_t^{2}+(\vec Q,\vec Q)$ | Conjugate scalar, the scalar of $\tilde Q\tilde Q^{\natural}$ |
| $x=\Xi_t^{2}$, $x_\pm=\tfrac12(Q_t\pm\sqrt n)$ | Square of a root's scalar part; the reduced quadratic |
| four / two / none / continuum | The root count, row by row |
| nonzero nilpotent | $\tilde Q\neq0$, $\tilde Q^{2}=0$; the rootless locus |
| $\mathbb{M}_-$ | Material sector; no nonzero nilpotent, so no refusal |
| $\sigma(\tilde\Xi)=\tilde\Xi\tilde\Xi$ | The ordinary square, the article's square |
| $\nu(\tilde\Xi)=\tilde\Xi\tilde\Xi^{\natural}=\langle\tilde\Xi\rangle_{\natural}e_t$ | The natural square; always scalar |
| $N=-c^{2}t^{2}+\lvert x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\rvert^{2}$ | The interval on $\mathbb{M}_-$ |
| $N=-m^{2}c^{2}$ | The mass shell, fibre of the natural square |

## Further Reading

- A. Dargys and A. Acus, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square-root problem of the complexified quaternions.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the zero divisors and the nilpotents, the rootless locus of the general problem.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the square roots and the isotropic cone in the complexified quaternions.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the idempotents and the structure of matrix algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the square of an element and the factorization of the wave operator.
