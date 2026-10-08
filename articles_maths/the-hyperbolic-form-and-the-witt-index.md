# __The Hyperbolic Form and the Witt Index__

## Introduction

The forms of the layer are built from one indecomposable block: the **hyperbolic plane**, the two-dimensional form with a basis of two isotropic vectors paired to $1$. Every non-degenerate form is an orthogonal sum of hyperbolic planes and one **anisotropic** part, and the number of the planes is the **Witt index** of the form:

$$
h \cong \underbrace{\mathbb{H} \perp \dots \perp \mathbb{H}}_{m} \perp h_{\mathrm{an}}, \qquad m = \operatorname{ind}(h) .
$$

The decomposition is the **Witt decomposition**, the number $m$ is an invariant of the form by the cancellation theorem, and the pair (index, anisotropic part) classifies the form over a field. This article constructs the plane, proves that every isotropic vector lies in one, and states the decomposition and its consequences; the cancellation theorem and the general Witt theory are *Witt's Theorems*, the inertia over an ordered field is *The Indefinite Case and the Signature*, and the orthogonal complements and the isotropy that the construction uses are *Orthogonality, Isotropy and the Radical*.

The hyperbolic form is the extremal case of the layer: it is as far from definite as a form of the given dimension can be, its index is maximal, its totally isotropic subspaces are the largest possible, and its Clifford algebra is the algebra of the exterior algebra, the reading of *Clifford Algebras in Finite Dimensions* and of *The Exterior Algebra* and *Involutions of the Exterior Algebra*. Over $\mathbb{R}$ the index of a form of signature $(p,q)$ is $\min(p,q)$, so the hyperbolic form of dimension $2n$ is the form of signature $(n,n)$. Throughout, $k$ is a field with an involution $\varsigma$ and $2$ invertible, $h$ is a non-degenerate Hermitian form on a finite-dimensional $k$-space $V$, and the Witt index is the largest dimension of a totally isotropic subspace.

## The Hyperbolic Plane

**Definition.** The **hyperbolic plane** $\mathbb{H}$ is the two-dimensional space with basis $e, f$ and the form

$$
h(e,e) = 0, \qquad h(f,f) = 0, \qquad h(e,f) = 1, \qquad h(f,e) = \varsigma(1) = 1 .
$$

**Proposition.** The hyperbolic plane is non-degenerate, its Witt index is $1$, its matrix in the basis $(e,f)$ is $\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ of determinant $-1$, and its two coordinate lines are the totally isotropic subspaces of maximal dimension.

**Proof.** The matrix has determinant $-1$, so the form is non-degenerate; the vectors $e$ and $f$ are isotropic, and their lines are totally isotropic, so the index is at least $1$. A two-dimensional totally isotropic subspace would be the whole plane, whose form is non-zero, so the index is exactly $1$.

**Proposition.** Every non-zero isotropic vector $x$ of a non-degenerate form lies in a hyperbolic plane.

**Proof.** By non-degeneracy there is $y$ with $h(x,y) \neq 0$; replacing $y$ by $y - \frac{h(y,y)}{2h(x,y)}\,x$ makes it isotropic without changing $h(x,y)$, because $h(y - \lambda x, y - \lambda x) = h(y,y) - 2\lambda h(x,y)$ when $h(x,x) = 0$ and $2$ is invertible. The plane spanned by $x$ and the new $y$ has the matrix of the previous proposition in the basis $(x,y)$ up to a scalar, and it is a hyperbolic plane.

**Corollary.** The Witt index of a non-degenerate form is the largest number of pairwise orthogonal hyperbolic planes it contains, and it is zero exactly when the form is anisotropic.

## The Hyperbolic Form

**Definition.** A form is **hyperbolic** when it is an orthogonal sum of hyperbolic planes, $h \cong \mathbb{H}^{\perp m}$; the form is **split** when in addition $m = \dim V/2$.

**Proposition.** The hyperbolic form $\mathbb{H}^{\perp m}$ has dimension $2m$, Witt index $m$, and its maximal totally isotropic subspaces have dimension $m$; it is the form of signature $(m,m)$ over $\mathbb{R}$.

**Proof.** The basis of the $2m$ vectors $e_{1},f_{1},\dots,e_{m},f_{m}$ is orthonormal-mixed: $h(e_{i},f_{j}) = \delta_{ij}$ and the other pairings vanish. The span of the $e_{i}$ and the span of the $f_{i}$ are totally isotropic of dimension $m$, and no totally isotropic subspace has a larger dimension because the form on a $(m+1)$-dimensional subspace has a non-zero restriction by the rank bound $\dim W + \dim W^{\perp} = 2m$ with $W$ totally isotropic giving $W \subseteq W^{\perp}$ and hence $2\dim W \leq 2m$. Over $\mathbb{R}$ the diagonalisation of the form has $m$ positive and $m$ negative squares.

## The Witt Decomposition

**Theorem (Witt).** Every non-degenerate form decomposes as an orthogonal sum

$$
V = H \perp V_{\mathrm{an}}, \qquad H \cong \mathbb{H}^{\perp m}, \quad V_{\mathrm{an}} \text{ anisotropic},
$$

with $m = \operatorname{ind}(h)$; the decomposition is unique in the sense that the index and the isometry class of the anisotropic part are invariants of the form.

**Proof.** The construction is by induction on the index: if the form is anisotropic the decomposition is trivial, and otherwise an isotropic vector spans a hyperbolic plane by the previous proposition, whose orthogonal complement is non-degenerate by *Orthogonality, Isotropy and the Radical* and has index one less. The uniqueness is Witt's cancellation theorem, which states that $h_{1} \perp h \cong h_{2} \perp h$ implies $h_{1} \cong h_{2}$ for non-degenerate forms; the theorem and its proof are *Witt's Theorems*.

**Corollary (the classification).** Two non-degenerate forms over a field with an involution and $2$ invertible are isometric exactly when they have the same Witt index and isometric anisotropic parts; the classification of the forms reduces to the classification of the anisotropic forms, and the classes form the Witt group of the layer, *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Corollary (the order relations).** A form has index at least $m$ exactly when it contains $\mathbb{H}^{\perp m}$ as an orthogonal summand; adding a hyperbolic plane increases the index by one and leaves the anisotropic part unchanged; the index is monotone under the orthogonal inclusion of non-degenerate forms.

## The Hyperbolic Form and the Algebra

**Proposition.** The Clifford algebra of the hyperbolic plane over a field of characteristic not two is the full matrix algebra $M_{2}(k)$, and the Clifford algebra of $\mathbb{H}^{\perp m}$ is $M_{2^{m}}(k)$; over $\mathbb{R}$ the hyperbolic form of dimension $2m$ has the Clifford algebra $M_{2^{m}}(\mathbb{R})$.

**Proof.** The Clifford algebra of a hyperbolic plane has a basis $\{1, e, f, ef\}$ with $e^{2} = f^{2} = 0$ and $ef + fe = -2$, which is the algebra of the two matrices $\begin{pmatrix}0&0\\ -2&0\end{pmatrix}$ and $\begin{pmatrix}0&1\\0&0\end{pmatrix}$; the identification is the matrix realisation of the exterior algebra, and the product statement follows by the tensor product of the Clifford algebras of the orthogonal summands.

**Corollary.** The hyperbolic form is the form whose Clifford algebra is the matrix algebra; the split cases of the classification of the Clifford algebras are the hyperbolic ones, and the periodicity and the classification are *The Low-Dimensional Classification*, *Bott Periodicity and the Classification* and *The Brauer–Wall Group and the Eightfold Way*. The exterior-algebra reading is *The Exterior Algebra* and *Involutions of the Exterior Algebra*.

## Examples

### The Plane and the Lorentz Form

The hyperbolic plane is the form of signature $(1,1)$ over $\mathbb{R}$; the Lorentz form of signature $(1,n-1)$ has index $1$ and anisotropic part of dimension $n-2$, its unique hyperbolic plane being the light plane of the two null directions of the physics articles.

### The Split Form

The hyperbolic form $\mathbb{H}^{\perp n}$ is the split form of dimension $2n$ and signature $(n,n)$; it is the form of the maximum index and of the maximum totally isotropic dimension $n$, and it is the form of the split groups of *The Indefinite Case and the Signature*.

### The Biquaternion Algebra

On $\mathbb{B}$ with the form $\operatorname{Sc}(\bar{\tilde Q}\tilde Q')$ of signature $(2,6)$ the index is $2$, the anisotropic part has dimension $4$, and the decomposition into two hyperbolic planes is the Lorentzian reading of *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## Summary

- The **hyperbolic plane** $\mathbb{H}$ has an isotropic basis $(e,f)$ with $h(e,f) = 1$; it is non-degenerate, its index is $1$, and its matrix has determinant $-1$.
- Every non-zero isotropic vector of a non-degenerate form lies in a hyperbolic plane.
- A **hyperbolic form** is an orthogonal sum of hyperbolic planes; $\mathbb{H}^{\perp m}$ has dimension $2m$, index $m$, and signature $(m,m)$ over $\mathbb{R}$.
- The **Witt decomposition** writes every non-degenerate form as $H \perp V_{\mathrm{an}}$ with $H$ hyperbolic and $V_{\mathrm{an}}$ anisotropic; the index and the anisotropic part are invariants by Witt's cancellation.
- The classification of the forms is by the Witt index together with the anisotropic part, and the classes form the Witt group.
- The Clifford algebra of a hyperbolic form is a full matrix algebra, the exterior-algebra realisation of the split case.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the hyperbolic plane with basis $e, f$ |
| $\mathbb{H}^{\perp m}$ | the orthogonal sum of $m$ hyperbolic planes |
| $h_{\mathrm{an}}$ | the anisotropic part of a Witt decomposition |
| $\operatorname{ind}(h)$ | the Witt index of a non-degenerate form |
| $(m,m)$ | the signature of the hyperbolic form over $\mathbb{R}$ |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the hyperbolic plane, the Witt decomposition and the cancellation theorem.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the Witt index, the anisotropic forms and the classification over a field.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the hyperbolic forms over a ring with an involution and the Witt group.
