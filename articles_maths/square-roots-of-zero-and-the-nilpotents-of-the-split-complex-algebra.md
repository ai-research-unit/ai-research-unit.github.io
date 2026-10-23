# __Square Roots of Zero and the Nilpotents of the Split-Complex Algebra__

## Introduction

Of the two products of *The Two Products of the Split-Complexoid Space*, exactly one makes the underlying real space of $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=+1$, an associative unital $\mathbb{R}$-algebra; the algebra is *Split-Complex Algebra*, and its multiplication is the general plain bilinear product of two split-complex numbers, $Q_1Q_2$. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\Xi\in\mathbb{D}$ with

$$
\Xi^{2}=0 .
$$

The second is the nilpotents of the algebra, the nonzero elements whose square vanishes. The two subjects are one: the roots of $0$ are the element $0$ together with the square-zero elements, and the nonzero square-zero elements are exactly the nilpotents. The roots of $+1$ and the idempotents are the companion article *Square Roots of One and the Idempotents of the Split-Complex Algebra*; the roots of the general quadratic $\Xi^{2}=Q$ are *Square Roots of a General Element in the Split-Complex Algebra*.

**The results.** The roots of $0$ are exactly the origin: the equation $\Xi^{2}=0$ forces both idempotent coordinates of $\Xi$ to vanish. There are **no nonzero nilpotents**. The nilpotent cone is the single point $\{0\}$, of real dimension $0$; the nilpotent set is empty; and the algebra is **reduced**. No element has index two or any higher index. No nilpotent is a zero divisor, because there are none; no nilpotent is an idempotent; the square-zero element $0$ is an idempotent and is not a nilpotent; the conjugation fixes the only square-zero element; and under the regular matrix model the square-zero elements are the zero matrix alone, in contrast with the nonzero nilpotent matrices of $M_2(\mathbb{R})$.

The article is algebraic. The zero-divisor set and its two families are *Zero Divisors of the Split-Complex Algebra*; the roots of $+1$ and the idempotents are *Square Roots of One and the Idempotents of the Split-Complex Algebra*; the ideals are *Ideals and Peirce Decomposition of the Split-Complex Algebra*; and the square-root problem for a general radicand is *Square Roots of a General Element in the Split-Complex Algebra*. The comparison with the dual numbers, where $\varepsilon^{2}=0$ has the nonzero root $\varepsilon$, is *The Specificities of the Split-Complex Algebra*.

The equations name a product, so the roots and the nilpotents are relative to it. The general definition of the power, the square, the root of a central value and the nilpotent, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other product of the space carries roots of $0$ and square-zero sets of its own, and they are *Relations and Comparison Between the Two Products of the Split-Complexoid Space*.

## The Roots of Zero

**The roots of $0$ are exactly the origin; the nonzero roots are the nilpotents, and there are none.**

A **root of $0$** is an element $\Xi\in\mathbb{D}$ with $\Xi^{2}=0$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in the idempotent coordinates,

$$
\Xi=\Xi_{+}\Pi_{+}+\Xi_{-}\Pi_{-},\qquad \Xi_{\pm}=x\pm x',
$$

with $x,x'\in\mathbb{R}$. The square is

$$
\Xi^{2}=\Xi_{+}^{2}\Pi_{+}+\Xi_{-}^{2}\Pi_{-},
$$

so the equation $\Xi^{2}=0$ is equivalent to the **pair of real equations**

$$
\Xi_{+}^{2}=0,\qquad \Xi_{-}^{2}=0.
$$

Over $\mathbb{R}$ each equation has the single solution $\Xi_{\pm}=0$, hence $\Xi=0$. There is no coupling and no room for a nonzero solution: the two coordinates must vanish separately.

**Remark (the scalar form).** In the basis $1,j$ the same equation reads

$$
x^{2}+x'^{2}=0,\qquad 2xx'=0,
$$

because $\Xi^{2}=(x^{2}+x'^{2})+2xx'j$. The first equation forces $x=x'=0$ over $\mathbb{R}$, since both squares are non-negative; the second is then automatic. The scalar form shows the same result without the idempotent basis.

### The Zero Element

The **zero element** $\Xi=0$ is a root of $0$: $0^{2}=0$. It is the only root. It is not a zero divisor under the convention that both factors be nonzero, even though it annihilates every element; it is an idempotent, because $0^{2}=0$; and it is not a nilpotent under the corpus convention, which reserves the word for a nonzero element.

### The Nilpotent Cone

The **nilpotent cone** of the algebra is the set

$$
\mathcal{N}_{0}=\{\Xi:\Xi^{2}=0\}.
$$

The reduction gives

$$
\boxed{\;\mathcal{N}_{0}=\{0\}\;},
$$

a single point, of real dimension $0$. There is no nonzero cone and no isotropic direction: the only square-zero element is the origin. The contrast with the dual numbers is sharp: there the equation $\varepsilon^{2}=0$ has the nonzero solution $\varepsilon$, and the nilpotent cone is the whole imaginary line. The contrast with the biquaternion algebra is equally sharp: there the nilpotent cone is a four-real-parameter cone inside the pure subspace. Here it collapses to a point because the two idempotent coordinates are real and their squares cannot cancel.

### Statement of the Theorem

**Theorem (the roots of $0$).** The equation $\Xi^{2}=0$ has exactly one solution in $\mathbb{D}$, the element $\Xi=0$.

**Proof.** The reduction gives $\Xi_{+}^{2}=0$ and $\Xi_{-}^{2}=0$; over $\mathbb{R}$ this gives $\Xi_{+}=\Xi_{-}=0$, hence $\Xi=0$. The element $0$ satisfies $0^{2}=0$.

### Verification

The verification is immediate: $0^{2}=0$. The content of the theorem is the converse, that no nonzero element squares to zero; it is the reduction and the positivity of the real squares.

### The Roots of Zero and the Nilpotents

The roots of $0$ are the origin together with the square-zero elements; since there are no nonzero square-zero elements, the two sets are

$$
\boxed{\;\{\Xi:\Xi^{2}=0\}=\{0\},\qquad \{\text{nilpotents}\}=\varnothing\;}.
$$

The word **nilpotent** is defined for a nonzero element in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, so the nilpotent set is empty and the root set is the singleton $\{0\}$. The article keeps the two notions separate: $0$ is a root of $0$ and is not a nilpotent.

## The Nilpotents

**There are no nonzero nilpotents in the split-complex algebra; the algebra is reduced.**

### The Definition

An element $\Upsilon\in\mathbb{D}$ is **nilpotent** when $\Upsilon\neq0$ and there is an integer $n\ge1$ with

$$
\Upsilon^{n}=0 .
$$

The smallest such $n$ is the **index of nilpotency** of $\Upsilon$. A **square-zero element** is an element $\Xi$ with $\Xi^{2}=0$; the nonzero square-zero elements are exactly the nilpotents of index two.

### The Criterion

**Theorem (the criterion).** There is **no** nilpotent in $\mathbb{D}$, and the only square-zero element is $0$.

**Proof.** If $\Upsilon^{n}=0$ for some $n\ge1$, write $\Upsilon=\Upsilon_{+}\Pi_{+}+\Upsilon_{-}\Pi_{-}$; then $\Upsilon^{n}=\Upsilon_{+}^{n}\Pi_{+}+\Upsilon_{-}^{n}\Pi_{-}$, so $\Upsilon_{+}^{n}=0$ and $\Upsilon_{-}^{n}=0$. Over $\mathbb{R}$ this gives $\Upsilon_{+}=\Upsilon_{-}=0$, hence $\Upsilon=0$, contrary to the definition of a nilpotent. So there is no nilpotent. If $\Upsilon^{2}=0$ the same computation with $n=2$ gives $\Upsilon=0$.

**Corollary (the algebra is reduced).** The plain algebra has no nonzero nilpotent element.

### The Nilpotent Cone

The nilpotent cone is the set of square-zero elements,

$$
\mathcal{N}_{0}=\{\Upsilon:\Upsilon^{2}=0\}=\{0\},
$$

of real dimension $0$. It is not a cone in the usual sense: it is the origin, the apex alone, with no ray. The **nonzero nilpotent cone** is empty. In the classification of the elements by the algebraic norm, the origin is the only element of norm $0$ that is not a zero divisor; the zero divisors are the other elements of the null cone, and the nilpotent cone lies at the apex of that null cone.

### Index Two

**Proposition (index).** There is no element of index two or higher: $\Upsilon^{2}=0$ already forces $\Upsilon=0$.

**Proof.** The computation of the criterion with $n=2$ gives $\Upsilon=0$. If one assigns index $1$ to the zero element, then $0$ is the only element with a finite index; no nonzero element has an index.

The statement is the sharp form of the absence: the usual hierarchy of nilpotents of index $2,3,\dots$ is empty at the first step.

### The Nilpotents and the Zero Divisors

**No nilpotent is a zero divisor, because there are no nilpotents; the nilpotent set and the zero-divisor set are disjoint, the first empty and the second the null cone minus the origin.**

The zero divisors are the nonzero elements of the null cone, $\mathcal{Z}=\mathcal{N}\setminus\{0\}$, and the nilpotent set is empty. The two sets do not meet. The origin, which is in the nilpotent cone, is not a zero divisor and is not a nilpotent; it is the apex of the null cone and belongs to the zero-divisor set only after the origin is removed.

**Remark.** The disjointness is not an accident of the split-complex case: in any reduced commutative ring there are no nonzero nilpotents, and the zero divisors can be plentiful. The split-complex algebra is the smallest reduced algebra with zero divisors, and it exhibits the separation in its purest form.

### The Nilpotents and the Idempotents

**No nilpotent is an idempotent, vacuously; the nilpotent set is empty, and the only square-zero idempotent is the origin, which is not a nilpotent.**

If $\Upsilon$ were both nilpotent and idempotent, then $\Upsilon^{2}=\Upsilon$ and $\Upsilon^{n}=0$ would give $\Upsilon=\Upsilon^{2}=\cdots=\Upsilon^{n}=0$, contradicting $\Upsilon\neq0$. In $\mathbb{D}$ the idempotents are $0,1,\Pi_{+},\Pi_{-}$, and the nilpotent set is empty, so the intersection is empty; the origin is the only element that is a square-zero element and an idempotent, and it is not a nilpotent.

### The Conjugation

The conjugation is an automorphism and fixes the only square-zero element: $\overline{0}=0$. It therefore maps the nilpotent cone to itself. The statement is vacuous for the nonzero nilpotents, but it is the statement that the nilpotent set is invariant under the involution, as it must be for any set defined by a polynomial equation with real coefficients.

### The Matrix Model

In the regular matrix model

$$
Q\longmapsto\mathsf{M}(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix},
$$

the square-zero elements are the matrices with $\mathsf{M}(Q)^{2}=0$. The matrix is symmetric, with eigenvalues $Q_{+}=q+q'$ and $Q_{-}=q-q'$; a symmetric matrix is nilpotent exactly when it is zero, because it is diagonalisable over $\mathbb{R}$ and its eigenvalues must vanish. The square-zero elements of the model are therefore the zero matrix alone, in contrast with the full matrix algebra $M_2(\mathbb{R})$, which has the nonzero square-zero matrix $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. The model is a commutative subalgebra and does not contain that matrix; the absence of nilpotents is the absence of the off-diagonal directions.

### The Nilpotents and the Ideals

**There is no nonzero nilpotent ideal, and the radical of the algebra is zero.**

A nilpotent ideal is an ideal $I$ with $I^{n}=0$ for some $n$; since every nonzero element of $I$ would then be nilpotent, and there are no nonzero nilpotents, the only nilpotent ideal is $0$. The Jacobson radical of the artinian algebra $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ is the intersection of its maximal ideals, which is $0$; the algebra is semisimple and reduced. The ideal theory is *Ideals and Peirce Decomposition of the Split-Complex Algebra*.

### The Nilpotents and the Distinguished Subspaces

**Every distinguished subspace contains $0$ and no nonzero nilpotent.**

The real line $\mathbb{R}_{\mathbb{D}}$, the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, the two idempotent lines $\mathbb{R}\Pi_{\pm}$, and the whole algebra all have the same square-zero set, $\{0\}$. On the real line, $q^{2}=0$ forces $q=0$; on the imaginary line, $-q'^{2}=0$ forces $q'=0$; on an idempotent line, $(\lambda\Pi_{\pm})^{2}=\lambda^{2}\Pi_{\pm}$, which is zero only at $\lambda=0$. The distribution is the simplest possible: the origin in every subspace and nothing else.

## Summary

The roots of $0$ in the split-complex algebra are exactly the origin: $\Xi^{2}=0$ forces both idempotent coordinates to vanish, and the only square-zero element is $0$. There are **no nonzero nilpotents**, so the nilpotent set is empty, the nilpotent cone is the single point $\{0\}$ of real dimension $0$, and the algebra is reduced. No element has index two or any higher index; no nilpotent is a zero divisor; no nilpotent is an idempotent; the square-zero element $0$ is an idempotent and not a nilpotent; the conjugation fixes the only square-zero element; the regular matrix model has the zero matrix alone as its square-zero element; and there is no nonzero nilpotent ideal, the radical being zero.

The result is the sharp contrast with the dual numbers, where $\varepsilon^{2}=0$ has the nonzero root $\varepsilon$, and with the biquaternion algebra, where the nilpotent cone is a four-real-parameter cone. In the split-complex algebra the two idempotent coordinates are real and their squares cannot cancel, so the cone collapses to its apex; the zero divisors are the null cone minus that apex, and the two classes of element are disjoint.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $\Xi$ | A root of $0$, or a square-zero element |
| $\Upsilon$ | A nilpotent |
| $\mathcal{N}_{0}=\{\Xi:\Xi^{2}=0\}=\{0\}$ | The nilpotent cone |
| $\{\text{nilpotents}\}=\varnothing$ | The nilpotent set |
| $\mathcal{Z}=\mathcal{N}\setminus\{0\}$ | The zero-divisor set, disjoint from the nilpotents |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The idempotents, none nilpotent |
| $\mathsf{M}(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$ | Regular matrix model, square-zero only at $Q=0$ |

## Further Reading

- [Square Roots of One and the Idempotents of the Split-Complex Algebra](square-roots-of-one-and-the-idempotents-of-the-split-complex-algebra.html), for the companion central value $+1$ and the four idempotents.
- [Square Roots of a General Element in the Split-Complex Algebra](square-roots-of-a-general-element-in-the-split-complex-algebra.html), for the roots of $\Xi^{2}=Q$.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the null cone, which contains the nilpotent cone as its apex.
- [Norm and Invertibility in the Split-Complex Algebra](norm-and-invertibility-in-the-split-complex-algebra.html), for the plain algebraic norm, whose vanishing set is also the origin.
- [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), for the radical and the semisimplicity of the algebra.
- [The Specificities of the Split-Complex Algebra](the-specificities-of-the-split-complex-algebra.html), for the comparison with the dual numbers.
