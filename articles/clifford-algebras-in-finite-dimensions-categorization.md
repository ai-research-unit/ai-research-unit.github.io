
# __Clifford Algebras in Finite Dimensions categorization__

## Introduction

This article specializes the theory of finite-dimensional Clifford algebras to specific commutative rings. The treatment is introductory and purely mathematical.

The common properties of finite-dimensional Clifford algebras, over any commutative ring, are the subject of the preceding article. Here we treat the specialization to the fields $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, and to the commutative ring $\mathbb{D}$.

Throughout this article, the module is **free of finite rank** and the quadratic form is **non-degenerate**. We assume that 2 is invertible in the base ring, so that the polarization identity holds and the fundamental relation $uv + vu = 2B(u, v) \cdot 1$ is available.

A word on terminology. The first three rings are fields, so the classical theory of Clifford algebras over a field applies verbatim. The fourth ring $\mathbb{D}$ is not a field: it is a commutative ring with zero divisors. The theory of Clifford algebras over $\mathbb{D}$ is similar to the theory over a field, with the caveat that not every nonzero element is a unit, and that a division algebra over $\mathbb{D}$ is only possible in rank 1 (and even then only if the unique element is a unit). We indicate where this difference matters.

Throughout this article, we use **rank** rather than **dimension** when speaking of Clifford algebras over a general commutative ring, reserving **dimension** for the field case. When the ring is a field, the two notions coincide.

For each case, we state the rank of the module, the quadratic form, the resulting Clifford algebra, and the name of the classical number system when there is one. We also give the concrete presentation of the algebra in terms of generators and relations.

---

# Part I: The Field $\mathbb{Q}$

## 1. Classification over $\mathbb{Q}$

Over $\mathbb{Q}$, the situation is subtle. The signature is defined with respect to the usual order on $\mathbb{Q}$, but it is not the only invariant. The full classification of quadratic forms over $\mathbb{Q}$ requires arithmetic invariants beyond the signature, such as the Hasse–Minkowski theorem and the Hilbert symbol.

We do not develop this theory here. We state only the low-dimensional cases.

## 2. Rank 0

The module is $\{0\}$. There are no generators. The Clifford algebra is $\mathbb{Q}$ itself. This is the **rational numbers**.

## 3. Rank 1

The module is $\mathbb{Q}$, with basis vector $e$. The quadratic form is determined by the single value $Q(e)$. There are two cases up to isomorphism.

**$Q(e) = +1$.** The relation is $e^2 = +1$. The Clifford algebra is $\mathbb{Q} \oplus \mathbb{Q}$, the **split complex numbers over $\mathbb{Q}$**. It has rank $2$ over $\mathbb{Q}$.

**$Q(e) = -1$.** The relation is $e^2 = -1$. The Clifford algebra is $\mathbb{Q}[i]$, the **Gaussian rationals**, of rank $2$ over $\mathbb{Q}$.

## 4. Rank 2 and Beyond

In rank 2, the module is $\mathbb{Q}^2$, with basis $e_1, e_2$. The quadratic form is determined by the three values $Q(e_1)$, $Q(e_2)$, and $B(e_1, e_2)$. Over $\mathbb{Q}$, the classification depends on arithmetic invariants. For example, the forms $x^2 + y^2$ and $x^2 + 2y^2$ are not isomorphic over $\mathbb{Q}$, even though they have the same signature over $\mathbb{R}$.

The full classification requires the theory of quaternion algebras over $\mathbb{Q}$, which we do not develop here. Higher-rank Clifford algebras over $\mathbb{Q}$ are obtained from the tensor product decomposition.

---

# Part II: The Field $\mathbb{R}$

## 5. The Matrix of the Bilinear Form

Let $M$ be a free $\mathbb{R}$-module of finite rank with a symmetric bilinear form $B$. Choose a basis $f_1, \ldots, f_n$ of $M$. The **matrix of $B$** with respect to this basis is the $n \times n$ matrix $M$ with entries

$$
M_{ij} = B(f_i, f_j).
$$

Since $B$ is symmetric, the matrix $M$ is symmetric.

For any vectors $u = \sum_i u_i f_i$ and $v = \sum_j v_j f_j$, the bilinear form is

$$
B(u, v) = u^T M v.
$$

The associated quadratic form is

$$
Q(v) = B(v, v) = v^T M v.
$$

## 6. Non-Degeneracy

The bilinear form $B$ is **non-degenerate** if

$$
B(u, v) = 0 \text{ for all } v \in M \implies u = 0.
$$

Equivalently, $B$ is non-degenerate if and only if the matrix $M$ is invertible.

## 7. Change of Basis and Congruence

Let $\mathcal{B}$ and $\mathcal{B}'$ be two bases of $M$, and let $P$ be the change-of-basis matrix from $\mathcal{B}'$ to $\mathcal{B}$. Then the matrix of $B$ with respect to the new basis is

$$
M' = P^T M P.
$$

Two matrices related in this way are called **congruent**. The classification of bilinear forms up to change of basis is the classification of symmetric matrices up to congruence.

## 8. Diagonalization

A symmetric matrix $M$ can be diagonalized by a congruence transformation. There is an invertible matrix $P$ such that

$$
P^T M P = \mathrm{diag}(\lambda_1, \ldots, \lambda_n)
$$

for some real numbers $\lambda_1, \ldots, \lambda_n$. Equivalently, there is a basis $e_1, \ldots, e_n$ of $M$ in which

$$
B(e_i, e_j) = 0 \quad (i \neq j), \qquad B(e_i, e_i) = \lambda_i.
$$

In this basis,

$$
Q(x_1 e_1 + \cdots + x_n e_n) = \lambda_1 x_1^2 + \cdots + \lambda_n x_n^2.
$$

## 9. Sylvester's Law of Inertia

In a diagonalizing basis, we can arrange the basis so that the positive coefficients come first, then the negative coefficients, then the zero coefficients. In this basis, the matrix of the bilinear form is

$$
\eta = \begin{pmatrix}
I_p & 0 & 0 \\
0 & -I_q & 0 \\
0 & 0 & 0_r
\end{pmatrix},
$$

where $I_p$ is the $p \times p$ identity matrix, $I_q$ is the $q \times q$ identity matrix, and $0_r$ is the $r \times r$ zero matrix.

**Sylvester's Law of Inertia.** Let $Q$ be a quadratic form on a finite-rank free real module. In any diagonalizing basis, let $p$ be the number of positive coefficients, $q$ the number of negative coefficients, and $r$ the number of zero coefficients. Then the triple $(p, q, r)$ is independent of the choice of diagonalizing basis.

The triple $(p, q, r)$ is called the **signature** of $Q$. The form is **non-degenerate** if $r = 0$, in which case the signature is written $(p, q)$.

Two real quadratic forms are isomorphic if and only if they have the same signature.

## 10. The Clifford Algebras over $\mathbb{R}$

The Clifford algebra with signature $(p, q)$ is written $Cl_{p,q}(\mathbb{R})$. Its rank over $\mathbb{R}$ is $2^n$, where $n = p + q$.

## 11. Rank 0

The module is $\{0\}$. There are no generators. The Clifford algebra is $Cl_{0,0}(\mathbb{R}) \cong \mathbb{R}$. This is the **real numbers**.

## 12. Rank 1

The module is $\mathbb{R}$, with basis vector $e$. The quadratic form is determined by the single value $Q(e)$. There are two cases up to isomorphism.

**$Q(e) = +1$.** The relation is $e^2 = +1$. The Clifford algebra is $Cl_{1,0}(\mathbb{R}) \cong \mathbb{R} \oplus \mathbb{R}$, the **split complex numbers**, also called the **hyperbolic numbers**. It has rank $2$ over $\mathbb{R}$.

**$Q(e) = -1$.** The relation is $e^2 = -1$. The Clifford algebra is $Cl_{0,1}(\mathbb{R}) \cong \mathbb{C}$, the **complex numbers**. It has rank $2$ over $\mathbb{R}$.

## 13. Rank 2

The module is $\mathbb{R}^2$, with basis $e_1, e_2$. In an orthogonal basis, the quadratic form is determined by the two values $Q(e_1)$ and $Q(e_2)$, with $B(e_1, e_2) = 0$. There are three cases up to isomorphism.

**$Q(e_1) = +1$, $Q(e_2) = +1$.** The relations are

$$
e_1^2 = +1, \qquad e_2^2 = +1, \qquad e_1 e_2 = -e_2 e_1.
$$

The Clifford algebra is $Cl_{2,0}(\mathbb{R}) \cong M_2(\mathbb{R})$, the algebra of $2 \times 2$ real matrices, of rank $4$.

**$Q(e_1) = +1$, $Q(e_2) = -1$.** The relations are

$$
e_1^2 = +1, \qquad e_2^2 = -1, \qquad e_1 e_2 = -e_2 e_1.
$$

The Clifford algebra is $Cl_{1,1}(\mathbb{R}) \cong M_2(\mathbb{R})$, the same algebra of $2 \times 2$ real matrices. It is also called the **split quaternions** or **coquaternions**.

**$Q(e_1) = -1$, $Q(e_2) = -1$.** The relations are

$$
e_1^2 = -1, \qquad e_2^2 = -1, \qquad e_1 e_2 = -e_2 e_1.
$$

The Clifford algebra is $Cl_{0,2}(\mathbb{R}) \cong \mathbb{H}$, the **quaternions**, of rank $4$.

Let me prove the last case. The algebra is generated by $1, e_1, e_2$. The product $e_1 e_2$ is a new element. Its square is

$$
(e_1 e_2)^2 = e_1 e_2 e_1 e_2 = -e_1 e_1 e_2 e_2 = -(e_1^2)(e_2^2) = -(-1)(-1) = -1.
$$

So the algebra is spanned by $1, e_1, e_2, e_1 e_2$, and the three elements $e_1, e_2, e_1 e_2$ all square to $-1$ and anticommute. This is exactly the quaternion algebra, with $e_1, e_2, e_1 e_2$ playing the roles of the three imaginary units.

## 14. Rank 3

The module is $\mathbb{R}^3$, with basis $e_1, e_2, e_3$. In an orthogonal basis, the quadratic form is determined by the three values $Q(e_1)$, $Q(e_2)$, $Q(e_3)$. Up to isomorphism, there are four cases, and the Clifford algebras fall into three isomorphism classes.

**Case with an odd number of positive squares.** The Clifford algebra is $Cl_{3,0}(\mathbb{R}) \cong Cl_{1,2}(\mathbb{R}) \cong M_2(\mathbb{C})$, the algebra of $2 \times 2$ complex matrices, of rank $8$.

**Case with two positive squares.** The Clifford algebra is $Cl_{2,1}(\mathbb{R}) \cong M_2(\mathbb{R}) \oplus M_2(\mathbb{R})$, a sum of two copies of the algebra of $2 \times 2$ real matrices, of rank $8$. Its center is $\mathbb{R} \oplus \mathbb{R}$, spanned by the unit and the volume element, so it is a product of two simple algebras rather than a simple algebra.

**Case with no positive squares.** The Clifford algebra is $Cl_{0,3}(\mathbb{R}) \cong \mathbb{H} \oplus \mathbb{H}$, the **split biquaternion algebra**, of rank $8$.

## 15. Rank 4 and Beyond

The pattern continues, with the graded tensor product of the preceding article in the first line:

$$
Cl_{0,4}(\mathbb{R}) \cong \mathbb{H} \hat{\otimes} \mathbb{H} \cong M_2(\mathbb{H}),
$$

$$
Cl_{1,3}(\mathbb{R}) \cong M_2(\mathbb{H}),
$$

$$
Cl_{2,2}(\mathbb{R}) \cong M_4(\mathbb{R}),
$$

$$
Cl_{3,1}(\mathbb{R}) \cong M_4(\mathbb{R}),
$$

$$
Cl_{4,0}(\mathbb{R}) \cong M_2(\mathbb{H}).
$$

The algebras $M_2(\mathbb{H})$ and $M_4(\mathbb{R})$ are both $16$-dimensional central simple algebras over $\mathbb{R}$, but they are **not** isomorphic: $M_4(\mathbb{R})$ is split while $M_2(\mathbb{H})$ is not, the two lying in different classes of the Brauer group $\mathrm{Br}(\mathbb{R}) = \mathbb{Z}/2$. Their centers are both $\mathbb{R}$, so the center does not distinguish them.

## 16. Bott Periodicity

The classification over $\mathbb{R}$ is periodic with period 8:

$$
Cl_{p+8,q}(\mathbb{R}) \cong Cl_{p,q}(\mathbb{R}) \otimes M_{16}(\mathbb{R}).
$$

## 17. The Even Subalgebra over $\mathbb{R}$

The even subalgebra satisfies

$$
Cl_{p,q}^+(\mathbb{R}) \cong Cl_{q,p-1}(\mathbb{R})
$$

for $p \geq 1$. The formula requires a positive direction to stand on; for $p = 0$ the companion formula reads $Cl_{0,q}^+(\mathbb{R}) \cong Cl_{0,q-1}(\mathbb{R})$.

## 18. The Center over $\mathbb{R}$

The center of $Cl_{p,q}(\mathbb{R})$ is either $\mathbb{R}$ or $\mathbb{R} \oplus \mathbb{R} g_1 g_2 \cdots g_n$, depending on whether $n = p + q$ is even or odd.

## 19. The Dual Quaternions

The **dual quaternion algebra** is $\mathbb{H}[\epsilon]/(\epsilon^2)$, the quaternions with a nilpotent element $\epsilon$ adjoined, satisfying $\epsilon^2 = 0$.

The dual quaternions are not a Clifford algebra in the strict sense. They are a **degenerate** Clifford algebra, obtained by allowing one of the generators to be nilpotent rather than square to $\pm 1$.

---

# Part III: The Field $\mathbb{C}$

## 20. Classification over $\mathbb{C}$

Over $\mathbb{C}$, every non-degenerate quadratic form of rank $n$ is isomorphic to the standard form

$$
Q(z_1, \ldots, z_n) = z_1^2 + \cdots + z_n^2.
$$

The reason is that over $\mathbb{C}$, we can rescale a basis vector by a complex scalar to change the sign of its coefficient. If a coefficient is $\lambda \neq 0$, we can write $\lambda = \mu^2$ for some $\mu \in \mathbb{C}^\times$, and then rescale the basis vector by $1/\mu$ to make the coefficient $1$.

So over $\mathbb{C}$, there is only one isomorphism class of non-degenerate quadratic forms in each rank. There is no signature.

## 21. The Complex Clifford Algebras

The complex Clifford algebra of rank $n$ is written $\mathbb{C}l_n$. The classification is:

$$
\mathbb{C}l_{2k} \cong M_{2^k}(\mathbb{C}), \qquad \mathbb{C}l_{2k+1} \cong M_{2^k}(\mathbb{C}) \oplus M_{2^k}(\mathbb{C}).
$$

## 22. Rank 0

The module is $\{0\}$. There are no generators. The Clifford algebra is $\mathbb{C}l_0 \cong \mathbb{C}$. This is the **complex numbers**.

## 23. Rank 1

The module is $\mathbb{C}$, with basis vector $e$. The quadratic form is determined by the single value $Q(e)$. Up to isomorphism, there is only one case.

Take $Q(e) = +1$. The relation is $e^2 = +1$. The algebra generated by $1$ and $e$ with $e^2 = +1$ is two-dimensional over $\mathbb{C}$. It splits as a direct sum of two copies of $\mathbb{C}$, spanned by the idempotents $(1 + e)/2$ and $(1 - e)/2$. So the Clifford algebra is

$$
\mathbb{C}l_1 \cong \mathbb{C} \oplus \mathbb{C}.
$$

This is the **split complex numbers over $\mathbb{C}$**.

If instead we take $Q(e) = -1$, we get the relation $e^2 = -1$. The resulting algebra is isomorphic to $\mathbb{C} \oplus \mathbb{C}$, via the substitution $e \mapsto i e'$, where $e'$ is the generator with $(e')^2 = +1$. So the two cases are isomorphic.

## 24. Rank 2

The module is $\mathbb{C}^2$, with basis $e_1, e_2$. Up to isomorphism, there is only one case.

Take $Q(e_1) = -1$ and $Q(e_2) = -1$. The relations are

$$
e_1^2 = -1, \qquad e_2^2 = -1, \qquad e_1 e_2 = -e_2 e_1.
$$

The algebra is generated by $1, e_1, e_2$, with the product $e_1 e_2$. A basis is

$$
1, \quad e_1, \quad e_2, \quad e_1 e_2.
$$

So the algebra is four-dimensional over $\mathbb{C}$. It is the quaternion algebra with complex coefficients, which is the **biquaternions**:

$$
\mathbb{C}l_2 \cong \mathbb{H} \otimes \mathbb{C} \cong M_2(\mathbb{C}).
$$

If instead we take $Q(e_1) = +1$ and $Q(e_2) = +1$, the relations are

$$
f_1^2 = +1, \qquad f_2^2 = +1, \qquad f_1 f_2 = -f_2 f_1.
$$

This algebra is isomorphic to the biquaternions, via the rescaling $e_1 = i f_1$, $e_2 = i f_2$. So the two choices of sign give isomorphic algebras.

In all cases, the Clifford algebra in rank 2 over $\mathbb{C}$ is isomorphic to $M_2(\mathbb{C})$, the algebra of $2 \times 2$ complex matrices, which is also the biquaternions.

## 25. Rank 3

The module is $\mathbb{C}^3$. Up to isomorphism, there is only one case. The Clifford algebra is

$$
\mathbb{C}l_3 \cong M_2(\mathbb{C}) \oplus M_2(\mathbb{C}),
$$

the direct sum of two copies of the biquaternions, of rank $8$ over $\mathbb{C}$.

## 26. Periodicity over $\mathbb{C}$

The complex Clifford algebras are periodic with period 2:

$$
\mathbb{C}l_{n+2} \cong \mathbb{C}l_n \otimes M_2(\mathbb{C}).
$$

## 27. The Even Subalgebra over $\mathbb{C}$

The even subalgebra satisfies

$$
\mathbb{C}l_n^+ \cong \mathbb{C}l_{n-1}
$$

for all $n \geq 1$ except $n = 2$.

## 28. The Center over $\mathbb{C}$

The center of $\mathbb{C}l_n$ is $\mathbb{C}$ if $n$ is even, and $\mathbb{C} \oplus \mathbb{C}$ if $n$ is odd.

---

# Part IV: The Commutative Ring $\mathbb{D}$

## 29. A Caveat

The split complex numbers $\mathbb{D}$ are not a field in the strict sense: they form a commutative ring with zero divisors. Writing $j$ for the split complex unit, with $j^2 = +1$ as in the split complex algebra article, the simplest example is $(1 + j)(1 - j) = 0$, and the element $1 + j$ has no inverse.

Despite this, much of the theory carries over. A module over $\mathbb{D}$ is a module over the ring $\mathbb{D}$. The determinant is defined, but the theorem "invertible if and only if determinant is nonzero" becomes "invertible if and only if determinant is a unit of $\mathbb{D}$".

## 30. Classification over $\mathbb{D}$

A quadratic form over $\mathbb{D}$ can be diagonalized, and the coefficients take values in $\mathbb{D}$. The classification is by the values of the coefficients, up to multiplication by squares in $\mathbb{D}$.

## 31. Rank 0

The module is $\{0\}$. There are no generators. The Clifford algebra is $\mathbb{D}$ itself. This is the **split complex numbers**.

## 32. Rank 1

The module is $\mathbb{D}$, with basis vector $e$. The quadratic form is determined by the single value $Q(e)$. There are two cases, since $+1$ and $-1$ are not related by multiplication by a square in $\mathbb{D}$.

**$Q(e) = +1$.** The relation is $e^2 = +1$. The Clifford algebra is $\mathbb{D} \oplus \mathbb{D}$, the direct sum of two copies of the split complex numbers.

**$Q(e) = -1$.** The relation is $e^2 = -1$. Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, the algebra is $\mathbb{D}[e]/(e^2+1) \cong \mathbb{C} \oplus \mathbb{C}$, the direct sum of two copies of the complex numbers. It is not the algebra of dual numbers over $\mathbb{D}$: the element $1 + e$ is not nilpotent, since $(1+e)^2 = 1 + 2e + e^2 = 2e \neq 0$.

## 33. Rank 2

The module is $\mathbb{D}^2$, with basis $e_1, e_2$. In an orthogonal basis, the quadratic form is determined by $Q(e_1)$ and $Q(e_2)$. Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, the Clifford algebra of the form with sign pattern $(p,q)$ is $Cl_{p,q}(\mathbb{R}) \otimes_{\mathbb{R}} \mathbb{D}$, so the classification over $\mathbb{D}$ is that over $\mathbb{R}$ tensored with $\mathbb{D}$. There are therefore two outcomes, not one.

If at most one of the two values is negative, the Clifford algebra is

$$
M_2(\mathbb{D}),
$$

the algebra of $2 \times 2$ matrices with entries in $\mathbb{D}$.

For $Q(e_1) = -1$, $Q(e_2) = -1$, the relations are

$$
e_1^2 = -1, \qquad e_2^2 = -1, \qquad e_1 e_2 = -e_2 e_1.
$$

This is the analogue of the biquaternions over $\mathbb{D}$, and it is also called the **split biquaternions**: the algebra is $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{D}$, not $M_2(\mathbb{D})$.

## 34. Rank 3

The module is $\mathbb{D}^3$. As in rank 2, the Clifford algebra is $Cl_{p,q}(\mathbb{R}) \otimes_{\mathbb{R}} \mathbb{D}$ for the sign pattern $(p,q)$, so it depends on that pattern rather than being the same for every form. For $Q = (+1, +1, -1)$ it is

$$
M_2(\mathbb{D}) \oplus M_2(\mathbb{D}),
$$

the direct sum of two copies of $M_2(\mathbb{D})$; for $Q = (+1,+1,+1)$ it is $M_2(\mathbb{C}) \otimes_{\mathbb{R}} \mathbb{D}$, and for $Q = (-1,-1,-1)$ it is $(\mathbb{H} \oplus \mathbb{H}) \otimes_{\mathbb{R}} \mathbb{D}$, a sum of four copies of $\mathbb{H}$.

## 35. The Split Biquaternions

The **split biquaternions** are the algebra $\mathbb{H} \otimes \mathbb{D}$, the quaternions tensored with the split complex numbers. As an algebra over $\mathbb{D}$, the split biquaternions are four-dimensional, with basis $\{1, e_1, e_2, e_3\}$ and the same relations as the quaternions, with coefficients in $\mathbb{D}$.

The split biquaternions are not a division algebra over $\mathbb{D}$, because $\mathbb{D}$ has zero divisors.

---

# Part V: Summary

## Over $\mathbb{Q}$

| Rank | Quadratic form | Clifford algebra | Name |
|---|---|---|---|
| 0 | — | $\mathbb{Q}$ | rational numbers |
| 1 | $Q(e) = +1$ | $\mathbb{Q} \oplus \mathbb{Q}$ | split complex over $\mathbb{Q}$ |
| 1 | $Q(e) = -1$ | $\mathbb{Q}[i]$ | Gaussian rationals |

Higher ranks require arithmetic invariants.

## Over $\mathbb{R}$

| Rank | Signature | Quadratic form | Clifford algebra | Name |
|---|---|---|---|---|
| 0 | $(0,0)$ | — | $\mathbb{R}$ | real numbers |
| 1 | $(1,0)$ | $Q(e) = +1$ | $\mathbb{R} \oplus \mathbb{R}$ | split complex numbers |
| 1 | $(0,1)$ | $Q(e) = -1$ | $\mathbb{C}$ | complex numbers |
| 2 | $(2,0)$ | $Q(e_1) = +1$, $Q(e_2) = +1$ | $M_2(\mathbb{R})$ | $2 \times 2$ real matrices |
| 2 | $(1,1)$ | $Q(e_1) = +1$, $Q(e_2) = -1$ | $M_2(\mathbb{R})$ | split quaternions |
| 2 | $(0,2)$ | $Q(e_1) = -1$, $Q(e_2) = -1$ | $\mathbb{H}$ | quaternions |
| 3 | $(3,0)$ | all $+1$ | $M_2(\mathbb{C})$ | $2 \times 2$ complex matrices |
| 3 | $(2,1)$ | two $+1$, one $-1$ | $M_2(\mathbb{R}) \oplus M_2(\mathbb{R})$ | sum of two copies |
| 3 | $(1,2)$ | one $+1$, two $-1$ | $M_2(\mathbb{C})$ | $2 \times 2$ complex matrices |
| 3 | $(0,3)$ | all $-1$ | $\mathbb{H} \oplus \mathbb{H}$ | split biquaternions |
| 4 | $(4,0)$ | all $+1$ | $M_2(\mathbb{H})$ | $2 \times 2$ quaternionic matrices |
| 4 | $(3,1)$ | three $+1$, one $-1$ | $M_4(\mathbb{R})$ | $4 \times 4$ real matrices |
| 4 | $(2,2)$ | two $+1$, two $-1$ | $M_4(\mathbb{R})$ | $4 \times 4$ real matrices |
| 4 | $(1,3)$ | one $+1$, three $-1$ | $M_2(\mathbb{H})$ | $2 \times 2$ quaternionic matrices |
| 4 | $(0,4)$ | all $-1$ | $M_2(\mathbb{H})$ | $2 \times 2$ quaternionic matrices |

## Over $\mathbb{C}$

| Rank | Quadratic form | Clifford algebra | Name |
|---|---|---|---|
| 0 | — | $\mathbb{C}$ | complex numbers |
| 1 | $Q(e) = +1$ or $-1$ | $\mathbb{C} \oplus \mathbb{C}$ | split complex over $\mathbb{C}$ |
| 2 | $Q(e_1) = -1$, $Q(e_2) = -1$ | $\mathbb{H} \otimes \mathbb{C} \cong M_2(\mathbb{C})$ | biquaternions |
| 2 | $Q(e_1) = +1$, $Q(e_2) = +1$ | $\mathbb{H} \otimes \mathbb{C} \cong M_2(\mathbb{C})$ | biquaternions (isomorphic) |
| 3 | any | $M_2(\mathbb{C}) \oplus M_2(\mathbb{C})$ | sum of two copies |

## Over $\mathbb{D}$

| Rank | Quadratic form | Clifford algebra | Name |
|---|---|---|---|
| 0 | — | $\mathbb{D}$ | split complex numbers |
| 1 | $Q(e) = +1$ | $\mathbb{D} \oplus \mathbb{D}$ | sum of two copies of $\mathbb{D}$ |
| 1 | $Q(e) = -1$ | $\mathbb{C} \oplus \mathbb{C}$ | sum of two copies of $\mathbb{C}$ |
| 2 | at most one negative | $M_2(\mathbb{D})$ | $2 \times 2$ matrices over $\mathbb{D}$ |
| 2 | $Q(e_1) = Q(e_2) = -1$ | $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{D}$ | split biquaternions |
| 3 | $(2,1)$ | $M_2(\mathbb{D}) \oplus M_2(\mathbb{D})$ | sum of two copies |
| 3 | $(3,0)$ or $(1,2)$ | $M_2(\mathbb{C}) \otimes_{\mathbb{R}} \mathbb{D}$ | — |
| 3 | $(0,3)$ | $(\mathbb{H} \oplus \mathbb{H}) \otimes_{\mathbb{R}} \mathbb{D}$ | — |

---

## Further Reading

- I. R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001).
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
- Klaus Gürlebeck and Wolfgang Sprössig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997).
- David Hestenes and Garret Sobczyk, *Clifford Algebra to Geometric Calculus* (Reidel, 1984).
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991).
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005).

