# __The Finite-Dimensional Representations and Their Unitarity Defect__

## Introduction

The finite-dimensional representations of the Lorentz algebra are labelled $(\tfrac{j_1}{2},\tfrac{j_2}{2})$ with $j_1,j_2$ non-negative integers, and their dimension is $(j_1+1)(j_2+1)$. None of them except the trivial one is unitary. The failure is measured by a single number, the **unitarity defect**: the largest eigenvalue of a boost generator, which is $\tfrac12(j_1+j_2)$ and which grows without bound along any direction in the representation.

This article states the classification, gives the trace of the general representation, proves why unitarity fails, describes the Hermitian forms that do exist and their inertia, and defines the defect and its properties.

The article assumes *The Two Commuting Complex Triples* for the two $SU(2)$ factors, *The Isomorphisms and Their Dimensions* for the complexification, and *$P$, $T$ and the Representation Labels* for the physical labels. It feeds *The Principal Series and the Complementary Series*, where the infinite-dimensional unitary representations replace these, and *Wigner's Classification: Two Casimirs, Three Orbits*, which needs the little-group labels rather than the Lorentz labels.

## The Classification

### The Label

A finite-dimensional representation of $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ is a tensor product of one representation of each summand:

$$
(m,n)=\Bigl(\tfrac{j_1}{2},\tfrac{j_2}{2}\Bigr),
\qquad
m=\tfrac{j_1}{2},\quad n=\tfrac{j_2}{2},
$$

with $2m=j_1$ and $2n=j_2$ non-negative integers. The label is integral because a finite-dimensional representation of $\mathfrak{sl}_2$ has integral or half-integral highest weight and the two summands here are each $\mathfrak{sl}_2$; the pair $(2m,2n)$ of integers is the block's notation and it is the one the menu uses.

### The Dimension

$$
\dim(m,n)=(2m+1)(2n+1)=(j_1+1)(j_2+1).
$$

| $(j_1,j_2)$ | name | dimension |
|---|---|---|
| $(0,0)$ | scalar | $1$ |
| $(1,0)$ | self-dual spinor | $2$ |
| $(0,1)$ | anti-self-dual spinor | $2$ |
| $(2,0)$ | self-dual two-form | $3$ |
| $(1,1)$ | four-vector | $4$ |
| $(2,2)$ | symmetric traceless two-tensor | $9$ |

### The Trace

The trace of a representation is its **character**, and on the maximal torus — a rotation by $\theta_{\mathrm{axr}}$ about an axis and a boost of rapidity $\theta_{\mathrm{rpd}}$ along it — it factorises:

$$
\chi_{j_1,j_2}(\theta_{\mathrm{axr}},\theta_{\mathrm{rpd}})
=\frac{\sin\bigl((j_1+1)(\theta_{\mathrm{axr}}-i\theta_{\mathrm{rpd}})/2\bigr)}{\sin\bigl((\theta_{\mathrm{axr}}-i\theta_{\mathrm{rpd}})/2\bigr)}
\cdot
\frac{\sin\bigl((j_2+1)(\theta_{\mathrm{axr}}+i\theta_{\mathrm{rpd}})/2\bigr)}{\sin\bigl((\theta_{\mathrm{axr}}+i\theta_{\mathrm{rpd}})/2\bigr)} .
$$

The two factors are the same function of the two conjugate complex parameters $\theta_{\mathrm{axr}}\mp i\theta_{\mathrm{rpd}}$, one per $\mathfrak{sl}_2$ summand. At $\theta_{\mathrm{rpd}}=0$ both reduce to the $SU(2)$ character $\frac{\sin((j_i+1)\theta_{\mathrm{axr}}/2)}{\sin(\theta_{\mathrm{axr}}/2)}$, bounded and periodic; at $\theta_{\mathrm{axr}}=0$ both become hyperbolic, $\frac{\sinh((j_i+1)\theta_{\mathrm{rpd}}/2)}{\sinh(\theta_{\mathrm{rpd}}/2)}$, and **unbounded** in $\theta_{\mathrm{rpd}}$. That unboundedness is the whole content of the next two sections.

Writing the formula with a compact factor of argument $\theta_{\mathrm{axr}}$ and a hyperbolic factor of argument $\theta_{\mathrm{rpd}}$ — which is a common shortcut in the literature — is wrong for a mixed rotation-and-boost element: it gives the right answer only when one of the two angles vanishes.

## The General Representation

### The Construction

The representation $(m,n)$ is the tensor product of the spin-$m$ and spin-$n$ representations of the two $\mathfrak{sl}_2$ summands. The rotation generators act diagonally on the two factors, $J_\imath=J^{(m)}_\imath\otimes I+I\otimes J^{(n)}_\imath$, and the boost generators act with opposite signs, $K_\imath=J^{(m)}_\imath\otimes I-I\otimes J^{(n)}_\imath$: that sign is the reason the complexified algebra splits into two commuting triples while the real form does not.

### The Weights

On the Cartan, the weights are pairs $(w_1,w_2)$ with $w_1\in\{-m,\dots,m\}$ and $w_2\in\{-n,\dots,n\}$. The compact generator $J_z$ has eigenvalues $w_1+w_2$, which are imaginary; the non-compact generator $K_z$ has eigenvalues $w_1-w_2$, which are **real**. So the boost's eigenvalues are differences of the two weights, running over $\{-(m+n),\dots,m+n\}$.

### The Largest Boost Eigenvalue

$$
\max\operatorname{spec}K_z=m+n=\tfrac12(j_1+j_2).
$$

This single number is the defect defined below, and everything about the non-unitarity follows from it.

### The Verification

The statements are checked against explicit matrices. For $(1,1)$, the four-vector representation built as the congruence action on Hermitian matrices, the boost of rapidity $1.1$ has eigenvalues $e^{1.1}$, $e^{-1.1}$, $1$, $1$ and trace $2+2\cosh1.1=5.337037$, against the character formula's $5.337037$; with a rotation of $0.7$ about the same axis added, the trace is $2\cos0.7+2\cosh1.1=4.866721$, again matched to ten digits. For $(2,0)$, the symmetric square of the defining representation, the boost eigenvalues are $e^{1.1}$, $1$, $e^{-1.1}$ and the character is $1+2\cosh1.1=4.337037$, again exact. For $(1,0)$, the defining representation itself, the character is $2\cosh0.55=2.310203$. The rotation characters agree with $1+2\cos\theta_{\mathrm{axr}}$ and $2\cos(\theta_{\mathrm{axr}}/2)$ respectively.

## Why Unitarity Fails

### The Requirement

A representation is unitary when the module carries a positive-definite Hermitian form $\langle\cdot,\cdot\rangle$ with

$$
\langle\rho(\tilde U)u,\rho(\tilde U)v\rangle=\langle u,v\rangle
$$

for every $\tilde U$ in the group. For the Lie algebra that means every generator is anti-Hermitian with respect to the form, in the corpus's anti-Hermitian convention.

### The Theorem

**A finite-dimensional unitary representation of a non-compact semisimple group is trivial.** The Lorentz group is non-compact semisimple, so the only unitary finite-dimensional representation is the scalar.

### The Mechanism

Suppose a representation of dimension greater than one were unitary. Then for every real $\theta_{\mathrm{rpd}}$ the operator $\rho(\exp(\theta_{\mathrm{rpd}} K_z))$ would be unitary, hence of operator norm exactly one, and all its eigenvalues would have modulus one. But the eigenvalues are $e^{w\theta_{\mathrm{rpd}}}$ with $w$ running over the real differences of weights, and the extreme one is $e^{(m+n)\theta_{\mathrm{rpd}}}$, which has modulus $e^{(m+n)\theta_{\mathrm{rpd}}}$. For $\theta_{\mathrm{rpd}}\neq0$ and $m+n>0$ that is not one.

So the failure is not a technicality of the inner product's choice: the spectrum itself forbids it. A representation is unitarisable only if its boost eigenvalues are purely imaginary, and here they are real.

### The Compact Contrast

Restricted to $SU(2)$, every finite-dimensional representation is unitary, because the rotation eigenvalues are $e^{i(\cdot)}$ and therefore on the unit circle. The defect is exactly the measure of how far the boost is from that situation: the boost's spectrum sits on the real axis where the rotation's sits on the circle.

### What the Defect Is Not

It is not the failure of an invariant bilinear form to exist. Invariant bilinear forms exist for many of these representations, and the Minkowski form on the four-vector is one. It is the failure of a *positive-definite* one to exist, which is a statement about the signs in the inertia and not about existence.

## The Hermitian Form

### What Would Be Needed

An invariant Hermitian form on $(m,n)$ is a $G$-equivariant antilinear map from the module to its dual. Since conjugation of the representation exchanges the two labels,

$$
\overline{(m,n)}\cong(n,m),
$$

such a form exists exactly when the representation is **self-conjugate**, that is when $m=n$.

### When It Exists

| representation | self-conjugate? | invariant Hermitian form |
|---|---|---|
| $(m,m)$ | yes | exists, indefinite for $m>0$ |
| $(m,n)$, $m\neq n$ | no | does not exist |

So $(1,1)$, the four-vector, carries the Minkowski form, of inertia $(1,3)$ or $(3,1)$; $(1,0)$ carries none, and its invariant bilinear form is the antisymmetric $\epsilon$ on its two components.

### Its Inertia

For a self-conjugate representation the form is indefinite whenever the representation is nontrivial — because a positive-definite invariant form would make the representation unitary, and no such representation exists beyond the scalar. So the inertia is the obstruction, and the number of negative signs is a property of the representation.

The four-vector is the cleanest case: the invariant form is the Minkowski interval, with one sign different from the other three, and that one sign is why the representation is not unitary and why the group acting on it is the Lorentz group rather than a rotation group.

### The Reading

The indefinite form is not a defect of the formalism. It is the geometry: the representation $(1,1)$ *is* spacetime, and spacetime's invariant form has a sign. A unitary structure on it would force the time direction to behave like the space directions, which is precisely what the Lorentz group does not do.

## The Defect

### The Definition

$$
d(m,n):=\max\operatorname{spec}\bigl(\rho(K_z)\bigr)=m+n=\tfrac12(j_1+j_2).
$$

It is the growth rate of the representation under a boost:

$$
\bigl\lVert\rho\bigl(\exp(\theta_{\mathrm{rpd}} K_z)\bigr)\bigr\rVert\sim e^{d\theta_{\mathrm{rpd}}},\qquad \theta_{\mathrm{rpd}}\to\infty.
$$

### The Values

| $(j_1,j_2)$ | $d$ | growth of the norm |
|---|---|---|
| $(0,0)$ | $0$ | bounded |
| $(1,0)$, $(0,1)$ | $\tfrac12$ | $e^{\theta_{\mathrm{rpd}}/2}$ |
| $(1,1)$ | $1$ | $e^{\theta_{\mathrm{rpd}}}$ |
| $(2,0)$ | $1$ | $e^{\theta_{\mathrm{rpd}}}$ |
| $(2,2)$ | $2$ | $e^{2\theta_{\mathrm{rpd}}}$ |

### The Two Properties

- **It vanishes only for the trivial representation.** $d=0$ requires $m=n=0$, which is the scalar. So "the defect" separates the scalar from everything else, exactly as unitarity does.
- **It is additive under tensor products.** $(m_1,n_1)\otimes(m_2,n_2)$ decomposes into labels with $m\le m_1+m_2$ and $n\le n_1+n_2$, so the maximum defect in the product is $d_1+d_2$. So the defect is a grading, and a theory built from these representations has a defect equal to the sum of its constituents'.

### Why the Name

The defect is the size of the "unphysical" part of the boost: it is the number that has to be removed, by passing to an infinite-dimensional representation, before a positive-definite form can exist. In the principal series the boost's spectrum becomes continuous and purely imaginary, and the defect is replaced by a continuous parameter — which is the subject of *The Principal Series and the Complementary Series*.

## The Exceptional Cases

### The Trivial Representation

$(0,0)$ has $d=0$, its invariant form is positive definite, and it is the only unitary finite-dimensional representation. A theory that demanded unitarity and finite dimension would have only scalars.

### The Self-Conjugate Nontrivial Cases

$(m,m)$ with $m>0$ has an invariant Hermitian form and it is indefinite. These are the representations whose form has an inertia, and the four-vector is the physically important one. The pattern is that the form's inertia is fixed by the representation and cannot be adjusted by a choice of basis.

### The Conjugate Pairs

$(m,n)$ with $m\neq n$ has no invariant Hermitian form and its conjugate is $(n,m)$. So a real theory must use both members of the pair, which is why the self-dual and anti-self-dual two-forms come together in a real field strength — the point made algebraically in *The Two Commuting Complex Triples*.

### The Two-Valued and Single-Valued Labels

The centre $\{\pm I\}$ of the double cover acts on $(m,n)$ as $(-1)^{j_1+j_2}$. So the parity of $j_1+j_2$ decides whether the representation is single-valued on the Lorentz group or only on its double cover: $(1,1)$, the four-vector, is single-valued, and $(1,0)$, the self-dual spinor, is two-valued. The defect does not distinguish the two cases — $(1,0)$ and $(1,1)$ differ by a factor two in dimension and by a factor two in defect — so unitarity and single-valuedness are independent obstructions.

## Summary

The finite-dimensional representations of the Lorentz algebra are labelled $(\tfrac{j_1}{2},\tfrac{j_2}{2})$, of dimension $(j_1+1)(j_2+1)$, with character $\chi=\frac{\sin((j_1+1)(\theta_{\mathrm{axr}}-i\theta_{\mathrm{rpd}})/2)}{\sin((\theta_{\mathrm{axr}}-i\theta_{\mathrm{rpd}})/2)}\frac{\sin((j_2+1)(\theta_{\mathrm{axr}}+i\theta_{\mathrm{rpd}})/2)}{\sin((\theta_{\mathrm{axr}}+i\theta_{\mathrm{rpd}})/2)}$ on the torus. The boost's eigenvalues are the differences of the two weights and the largest is $\tfrac12(j_1+j_2)$, so under a boost the representation's norm grows like $e^{\frac12(j_1+j_2)\theta_{\mathrm{rpd}}}$. That growth is the unitarity defect, and it forbids a positive-definite invariant form for every representation except the scalar. Invariant Hermitian forms exist exactly for the self-conjugate labels $m=n$, and they are indefinite whenever nontrivial; the four-vector's is the Minkowski form, whose single negative sign is the geometry of spacetime rather than a flaw.

## Summary of Notation

| symbol | meaning |
|---|---|
| $(\tfrac{j_1}{2},\tfrac{j_2}{2})$, $(m,n)$ | the finite-dimensional labels |
| $\chi_{j_1,j_2}$ | the character, the trace of the representation |
| $\theta_{\mathrm{axr}}$ | the rotation angle of the torus element |
| $\theta_{\mathrm{rpd}}$ | the boost rapidity of the torus element |
| $d=\tfrac12(j_1+j_2)$ | the unitarity defect |
| self-conjugate | $m=n$, so that $\overline{(m,n)}\cong(m,n)$ |
| inertia | the number of positive and negative signs of an invariant form |

## Further Reading

- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer, 1991 — the finite-dimensional representations of $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ and the character formulas.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015 — the theorem that a non-compact semisimple group has no nontrivial finite-dimensional unitary representation, with the spectral proof.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §5.6 — the $(\tfrac{j_1}{2},\tfrac{j_2}{2})$ labels, the non-unitarity and the passage to infinite-dimensional representations.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984 — the self-dual and anti-self-dual two-forms as a conjugate pair.
- *The Two Commuting Complex Triples* — the split whose two factors are these labels.
- *The Principal Series and the Complementary Series* — the infinite-dimensional representations that are unitary.
