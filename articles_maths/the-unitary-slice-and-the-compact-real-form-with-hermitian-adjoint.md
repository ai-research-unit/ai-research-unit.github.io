
# __The Unitary Slice and the Compact Real Form with Hermitian Adjoint__

## Introduction

The dagger is defined on every element of the algebra, but it is an inverse only on the elements that satisfy $x^{\dagger}x = 1$. Those elements are the **unitary slice** $U$, and the slice is where the involutive theory and the orthogonal theory meet: on it the Hermitian sandwich is the inner conjugation, the dagger is the inverse, and the operator family of *Two-Sided Operators on a Clifford Algebra* closes on itself. The slice is also the object that makes the involutive base visible in the group theory, because its shape records the signature: for the identity involution it is the Pin group, and for a definite form over $\mathbb{C}$ or $\mathbb{H}$ it is a compact unitary group.

This article treats the slice as a group, as the isometry group of the Hermitian form, as the image of the exponential of the skew part, and as a compact real form of the group of units. The two structural results are that $U$ is a compact subgroup whenever the dagger is a positive involution, because $x^{\dagger}x = 1$ forces the Euclidean norm to be $1$, so the slice lies in the unit sphere; and that the group of units is the product $U\cdot\exp(\mathrm{Herm})$ of the slice with the exponential of the self-adjoint part, which is the Cartan decomposition of the polar decomposition of the previous article.

The forms are *Hermitian Forms on a Hilbert Algebra with Hermitian Adjoint*; the scalar forms and the Euclidean norm are *The Blade Form and the Hilbert Structure with Hermitian Adjoint*; positivity and the cone are *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*; the operator on the algebra whose slice this is is *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*; the unitary group as a classical group is *The Unitary and Symplectic Groups*; the compactness of the group of units of a complex Clifford algebra is the case of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* in the definite real case; and the biquaternion example, where the slice is $U(2)$ with determinant-one part $\mathrm{Spin}(3)$, is *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*.

## The Unitary Slice

**Definition.** The **unitary slice** of the algebra is

$$
U = \{\, x \in \mathrm{Cl}(V,q) : x^{\dagger}x = 1 \,\}.
$$

**Theorem.** $U$ is a subgroup of the group of units, and on it the dagger is the inverse: for $x \in U$, $x^{-1} = x^{\dagger}$.

**Proof.** If $x \in U$ then $x$ is invertible with left inverse $x^{\dagger}$, and in a finite-dimensional algebra that is an inverse, so $x^{-1} = x^{\dagger}$ and $x\,x^{\dagger} = 1$. If $x, y \in U$ then

$$
(xy)^{\dagger}(xy) = y^{\dagger}x^{\dagger}x\,y = y^{\dagger}y = 1 ,
$$

so $U$ is closed under multiplication; it contains $1$; and if $x \in U$ then $(x^{\dagger})^{\dagger}x^{\dagger} = xx^{\dagger} = 1$, so $x^{\dagger} = x^{-1} \in U$.

**Corollary (the two theories meet).** On $U$ the Hermitian sandwich is the inner conjugation,

$$
x \in U \ \Longrightarrow \ \Theta_x(y) = x\,y\,x^{-1} = \mathrm{Ad}^{\alpha}_x(y) \text{ for even } x ,
$$

so the operator of *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint* restricts on the slice to the inverse sandwich of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

**Theorem (the slice is the isometry group).** $U$ is exactly the group of isometries of the Hermitian form $h_{\dagger}(x,y) = x^{\dagger}y$:

$$
\mathrm{Isom}(h_{\dagger}) = U .
$$

**Proof.** $h_{\dagger}(sx,sy) = (sx)^{\dagger}(sy) = x^{\dagger}s^{\dagger}s\,y$, which equals $h_{\dagger}(x,y) = x^{\dagger}y$ for all $x,y$ exactly when $s^{\dagger}s = 1$, the necessity by $x = y = 1$.

**Proposition (the identity involution).** When $\sigma = \mathrm{id}$ the dagger is Clifford conjugation and

$$
U = \{\, x : N(x) = 1 \,\} = \mathrm{Pin}(V,q), \qquad N(x) = x\,\bar x ,
$$

so the unitary slice is the Pin group of the quadratic space, and in particular is the double cover of the orthogonal group in the definite real case.

**Proof.** If $\bar xx = 1$ then $N(x) = x\bar x = x(\bar xx)x^{-1} = 1$. Conversely if $x\bar x = 1$ then $\bar x = x^{-1}$, so $\bar xx = 1$.

**Remark.** For $\sigma = \mathrm{id}$ and an indefinite form the "slice" is still $\{N(x)=1\}$, but it contains null directions and is not compact; the compactness statement requires a definite form and is proved in the last section. This is the reason *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* uses the norm-two-condition restriction $N(x) = \pm1$ to get the two components.

## The Lie Algebra and the Exponential

**Theorem.** With the bracket $[u,v] = uv - vu$, the skew part

$$
\mathfrak{u} = \mathrm{Skew}(V,q) = \{\, u : u^{\dagger} = -u \,\}
$$

is a Lie algebra, $\mathfrak{u}$ is the Lie algebra of $U$, and the exponential maps it into the slice:

$$
u \in \mathfrak{u} \ \Longrightarrow \ \exp(u) \in U .
$$

**Proof.** The case $[\mathrm{Skew},\mathrm{Skew}] \subseteq \mathrm{Skew}$ of the Cartan decomposition of *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint* makes $\mathfrak{u}$ a Lie algebra. For the exponential, the dagger is an anti-automorphism, so $\dagger(\exp u) = \exp(u^{\dagger}) = \exp(-u)$, whence

$$
\exp(u)^{\dagger}\exp(u) = \exp(-u)\exp(u) = 1 .
$$

**Proposition.** The exponential maps the self-adjoint part into itself, $\exp(\mathrm{Herm}) \subseteq \mathrm{Herm}$, and the polar decomposition of an invertible element is the Cartan decomposition

$$
G = U\cdot\exp(\mathrm{Herm}(V,q)), \qquad x = u\,e^{h}, \quad u \in U, \ h = \log|x| \in \mathrm{Herm} ,
$$

of the group of units $G$, when the dagger is positive.

**Proof.** $\dagger(\exp h) = \exp(h^{\dagger}) = \exp(h)$ for $h$ self-adjoint. The factorisation is the polar decomposition $x = u|x|$ of *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*, with $|x| = \exp(\log|x|)$ and $\log|x|$ self-adjoint because $|x|$ is positive.

**Corollary.** The Lie algebra of the slice is the skew part, so the slice has the dimension of the skew part of the algebra, and the exponential is surjective onto the identity component of $U$ in the definite compact case; the Cartan involution $\theta$ of *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint* is exactly the involution $\mathrm{d}\theta = +1$ on $\mathfrak{u}$, $-1$ on $\mathrm{Herm}$, associated with this decomposition.

## The Compact Real Form

### Compactness

**Theorem.** Suppose the dagger is positive, that is $\mathrm{Sc}(x^{\dagger}x) > 0$ for $x \neq 0$, equivalently the Hermitian–Schmidt scalar form is positive definite. Then $U$ is a compact subgroup of the group of units, and it lies in the Euclidean unit sphere:

$$
x \in U \ \Longrightarrow \ \|x\|^{2} = (x,x) = \mathrm{Sc}(x^{\dagger}x) = \mathrm{Sc}(1) = 1 .
$$

**Proof.** For $x \in U$ we have $x^{\dagger}x = 1$, so $\mathrm{Sc}(x^{\dagger}x) = 1$; when the dagger is positive, $\mathrm{Sc}(x^{\dagger}x) = \|x\|^{2}$ by *The Blade Form and the Hilbert Structure with Hermitian Adjoint*, whence $\|x\| = 1$. Thus $U$ is a closed subset of the unit sphere of a finite-dimensional Euclidean space, and it is bounded and closed, hence compact; it is a group by the theorem above, and a closed subgroup of the group of units, hence a compact Lie group.

**Corollary (the positive cases).** The dagger is positive and $U$ is compact for the Clifford algebras of a negative definite real form, $\mathrm{Cl}_{0,n}$ over $\mathbb{R}$, where $U = \mathrm{Pin}(0,n)$; for the complexified algebras with coefficient conjugation; and for the quaternionic cases. In each of them the slice is a compact real Lie group whose Lie algebra is the skew part, and the exponential is surjective onto its identity component.

### The Slice as a Compact Real Form

**Theorem (the complex case).** Let $A = \mathbb{C}$ with $\sigma$ the complex conjugation, and suppose the dagger is positive. Then the group of units $G = \mathrm{Cl}(V,q)^{\times}$ is a complex Lie group, $U$ is a compact real form of it, and the Cartan decomposition $G = U\exp(\mathfrak{p})$ with $\mathfrak{p}$ the self-adjoint part is the polar decomposition. The real Lie algebra of $U$ complexifies to the Lie algebra of $G$.

**Proof.** The complexification of $\mathfrak{u}$ is $\mathfrak{u}\oplus i\mathfrak{u} = \mathfrak{u}\oplus\mathfrak{p} = \mathrm{Lie}(G)$, since every element of the algebra is the sum of its skew and self-adjoint parts after multiplying by $i$; the rest is the theory of compact real forms.

**Example (the one-dimensional complex case, computed exactly).** Let $\mathrm{Cl}_1(\mathbb{C})$ be the algebra with a single generator $e^{2} = -1$, so $\mathrm{Cl}_1(\mathbb{C})\cong\mathbb{C}\oplus\mathbb{C}$ and the group of units is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$. Write $x = a + be$ with $a, b \in \mathbb{C}$, so that $x^{\dagger} = \bar a - \bar b e$ and

$$
x^{\dagger}x = |a|^{2} + |b|^{2} + (\bar ab - \bar ba)e .
$$

The condition $x^{\dagger}x = 1$ is therefore the pair

$$
|a|^{2} + |b|^{2} = 1, \qquad \bar ab \in \mathbb{R},
$$

which defines a compact real surface in $\mathbb{C}^{2}$; the algebra is commutative, so $U$ is an abelian compact connected Lie group of dimension two, that is $U \cong U(1)\times U(1)$, the compact real form of $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$. In the identification with $\mathbb{C}\oplus\mathbb{C}$ the dagger is $(z,w)^{\dagger} = (\bar z,\bar w)$ and $U = \{(z,w) : |z| = |w| = 1\}$, which is the same torus.

**Remark (the general complex case).** In dimension $n$ the slice $U$ is the unitary group of the Hermitian form $h_{\dagger}$ restricted to the spinor module; the biquaternion algebra $\mathbb{B}\cong\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ gives $U(2)$ and its determinant-one part $SU(2)\cong\mathrm{Spin}(3)$, the example carried through in *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*. The identification of $U$ with a classical unitary group in each signature is the subject of *The Unitary and Symplectic Groups*, and this article only fixes the slice, the compactness and the Cartan structure.

### The Orthogonal and the Unitary Geometry

**Proposition.** If $x \in U \cap \Gamma(V,q)$ then $x^{\dagger} = x^{-1}$, and comparing with the Clifford-group identity $x^{\dagger} = \sigma(N(x))\sigma(x)^{-1}$ gives

$$
\sigma(x) = \sigma\bigl(N(x)\bigr)\, x ,
$$

so the involution $\sigma$ acts on such an $x$ as the scalar $\sigma(N(x))$, and $x$ is $\sigma$-real exactly when its norm is one. Conversely an element of $\Gamma$ with $\sigma(x) = \sigma(N(x))x$ lies in $U$.

**Corollary (the orthogonal part of the slice).** For $\sigma = \mathrm{id}$ the condition is $N(x) = 1$ and the whole slice is the Pin group; its elements act on $V$ by the orthogonal transformations of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. For a nontrivial $\sigma$ the slice meets $\Gamma$ only in the elements on which $\sigma$ is a scalar, so the slice is **not** an enlargement of Pin inside the Clifford group; the elements of $U$ outside $\Gamma$ do not act on $V$ at all. In either case the unitary slice adds a compact group of **operators** on the algebra and on its Clifford modules and adds no isometry of the quadratic space, which is the precise division of labour between the orthogonal and the unitary geometry.

## Summary

The **unitary slice** $U = \{x : x^{\dagger}x = 1\}$ is a subgroup of the group of units on which the dagger is the inverse, and it is exactly the isometry group of the Hermitian form $h_{\dagger}(x,y) = x^{\dagger}y$. On it the Hermitian sandwich is the inner conjugation, so the Hermitian and the inverse sandwich agree on the slice and the two theories meet there. For the identity involution $U = \{x : N(x) = 1\} = \mathrm{Pin}(V,q)$, so the slice recovers the classical spin group; for a nontrivial involution it is larger and acts as a group of operators on the algebra and its modules without adding isometries of the quadratic space.

The **skew part** $\mathfrak{u} = \{u : u^{\dagger} = -u\}$ is a Lie algebra and is the Lie algebra of $U$; the exponential maps $\mathfrak{u}$ into $U$ and the self-adjoint part into itself, and the group of units is the Cartan product $G = U\exp(\mathrm{Herm})$ when the dagger is positive, which is the polar decomposition of an invertible element. When the dagger is positive the slice is **compact**, because $x^{\dagger}x = 1$ forces $\|x\|^{2} = \mathrm{Sc}(x^{\dagger}x) = 1$, so $U$ is a closed subset of the unit sphere; in the complex case it is a compact real form of the complex group of units, the one-dimensional exactly computed example being $\mathrm{Cl}_1(\mathbb{C})\cong\mathbb{C}\oplus\mathbb{C}$ with $U\cong U(1)\times U(1)$ and the biquaternion example being $U(2)$ with determinant-one part $\mathrm{Spin}(3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U = \{x : x^{\dagger}x=1\}$ | Unitary slice |
| $h_{\dagger}(x,y) = x^{\dagger}y$ | Hermitian form whose isometry group is $U$ |
| $\mathfrak{u} = \mathrm{Skew}(V,q)$ | Skew part, the Lie algebra of $U$ |
| $\mathrm{Herm}(V,q)$ | Self-adjoint part, the tangent space of the symmetric space |
| $\theta$ | Cartan involution, $\mathrm{d}\theta = +1$ on $\mathfrak{u}$, $-1$ on $\mathrm{Herm}$ |
| $G = U\exp(\mathrm{Herm})$ | Cartan decomposition of the group of units |
| $\mathrm{Pin}(V,q) = \{x : N(x)=1\}$ | Slice for $\sigma = \mathrm{id}$ |
| $\|x\|^{2} = \mathrm{Sc}(x^{\dagger}x)$ | Euclidean norm when the dagger is positive |

## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques*, Ergebnisse der Mathematik 5 (Springer, 3rd ed. 1971), for the unitary group of a form over a ring with involution and its isometry group.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Pin and Spin groups, the norm condition and the compact forms.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for compact real forms, the Cartan decomposition and the exponential.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics II*, Texts and Monographs in Physics (Springer, 2nd ed. 1997), for the Clifford algebra of a Hilbert space, its unitary group and the completion.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the unitary group of a Hermitian form over a ring with involution.
