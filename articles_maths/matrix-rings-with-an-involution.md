
# __Matrix Rings with an Involution__

## Introduction

The matrix ring $M_n(R)$ carries three involutions that occur throughout the corpus: the **transpose** $X \mapsto X^{\mathrm t}$, which needs no commutativity and no coefficient structure; the **conjugate transpose** $X \mapsto (\sigma(x_{ji}))$, which needs a commutative ring of coefficients with an involution $\sigma$; and the **symplectic involution** $X \mapsto J^{-1}X^{\mathrm t}J$, which needs an element $J$ with $J^{\mathrm t} = -J$ and $J^2 = -1$ and therefore an even dimension. The three are not equivalent, and the classification of the involutions of $M_n(R)$ says that over a field, up to conjugation by a unit, there are no others of the first kind: an involution is of **transpose type** when it has $n$ orthogonal symmetric idempotents summing to the identity, and of **symplectic type** otherwise, the second occurring only in even dimension.

This article fixes the three involutions, computes their symmetric and skew matrices, and states the classification with the invariant that separates the transpose type from the symplectic type, the dimension of the symmetric part. It assumes *Involutive Rings* for the definition of an involution, its fixed set and its symmetric and skew elements, and *Rings* and *Modules over an Algebra* for the matrix ring and its units. The classification by the forms a matrix represents, the discriminant and the Clifford invariant of an involution, belong to *Hilbert Algebras* in Part II and are named here only as the boundary; the involutions of a general central simple algebra are *Involutions of a Central Simple Algebra*, in *Bilinear Algebras*, the algebra category that owns the central simple algebras. Nothing here is measured: a matrix is transposed, conjugated and multiplied, and no length or sign is read off a vector.

Throughout, $R$ is a ring with $1 \neq 0$, $F$ is a field, $n \geq 1$, and $M_n(R)$ is the ring of $n \times n$ matrices with entries in $R$ and the usual product; $e_{ij}$ are the matrix units, $X^{\mathrm t}$ is the transpose, $\operatorname{tr}(X)$ is the trace, $\sigma$ is an involution of $R$ when $R$ is commutative, and $J$ is a matrix with $J^{\mathrm t} = -J$, $J^2 = -1$. The **conjugate transpose** of $X = (x_{ij})$ is written $X^{*} = (\sigma(x_{ji}))$.

## The Three Involutions

### The Transpose

**Proposition.** The transpose $T(X) = X^{\mathrm t}$ is an involution of $M_n(R)$ for every ring $R$; it permutes the matrix units by $T(e_{ij}) = e_{ji}$, and its fixed set is the set of **symmetric** matrices $\{X : X^{\mathrm t} = X\}$.

**Proof.** $(X+Y)^{\mathrm t} = X^{\mathrm t}+Y^{\mathrm t}$, $(XY)^{\mathrm t} = Y^{\mathrm t}X^{\mathrm t}$ holds for matrices over any ring because the entry $(XY)^{\mathrm t}_{ij} = (XY)_{ji} = \sum_k x_{jk}y_{ki}$ equals $(Y^{\mathrm t}X^{\mathrm t})_{ij} = \sum_k (Y^{\mathrm t})_{ik}(X^{\mathrm t})_{kj} = \sum_k y_{ki}x_{jk}$, and the two sums coincide; $T^2 = \mathrm{id}$ and $I^{\mathrm t} = I$ are immediate. The fixed set is the symmetric matrices by definition.

**Remark.** The transpose is the only one of the three that requires no hypothesis on $R$: it is an anti-isomorphism of $M_n(R)$ with itself for the structure of a matrix ring alone, and the anti-multiplicativity $(XY)^{\mathrm t} = Y^{\mathrm t}X^{\mathrm t}$ is a computation in the entries.

### The Conjugate Transpose

**Definition.** Let $R$ be commutative with an involution $\sigma$. The **conjugate transpose** of $X = (x_{ij})$ is $X^{*} = (\sigma(x_{ji}))$; when $\sigma = \mathrm{id}$ it is the transpose.

**Proposition.** The conjugate transpose is an involution of $M_n(R)$; its fixed set is the set of **$\sigma$-Hermitian** matrices $\{X : X^{*} = X\}$, that is, $\sigma(x_{ji}) = x_{ij}$ for all $i, j$.

**Proof.** Additivity is entrywise. For the product, $((XY)^{*})_{ij} = \sigma((XY)_{ji}) = \sum_k \sigma(x_{jk}y_{ki}) = \sum_k \sigma(y_{ki})\sigma(x_{jk})$, and $(Y^{*}X^{*})_{ij} = \sum_k (Y^{*})_{ik}(X^{*})_{kj} = \sum_k \sigma(y_{ki})\sigma(x_{jk})$; the two agree, so $(XY)^{*} = Y^{*}X^{*}$. The order-two and unit conditions are immediate, and the fixed set is as stated.

**Remark.** The conjugate transpose is the transpose of the *matrix* of conjugates: $X^{*} = (X^{\sigma})^{\mathrm t}$ with $X^{\sigma} = (\sigma(x_{ij}))$ the coefficientwise image. It is the involution of $M_n(R)$ induced by the involution of the coefficient ring, and it is the one used for Hermitian matrices over $\mathbb{C}$ in the applications of Part II.

### The Symplectic Involution

**Definition.** Let $J \in M_n(R)$ satisfy $J^{\mathrm t} = -J$ and $J^2 = -1$; necessarily $n$ is even and $-1$ is a square in the centre. The **symplectic involution** is

$$
X^{\tau} = J^{-1}X^{\mathrm t}J .
$$

**Proposition.** $X \mapsto X^{\tau}$ is an involution of $M_n(R)$, and $X^{\tau} = X$ if and only if $JX$ is skew-symmetric.

**Proof.** $\tau$ is additive and $\tau(1) = J^{-1}J = 1$; $\tau(XY) = J^{-1}Y^{\mathrm t}X^{\mathrm t}J = (J^{-1}Y^{\mathrm t}J)(J^{-1}X^{\mathrm t}J) = \tau(Y)\tau(X)$; and $\tau^2(X) = J^{-1}(J^{-1}X^{\mathrm t}J)^{\mathrm t}J = J^{-1}J^{\mathrm t}XJ^{-\mathrm t}J = J^{-1}(-J)X(-J)^{-1}J = X$, using $J^{\mathrm t} = -J$ and $J^{-1} = -J$. For the fixed set, $J^{-1}X^{\mathrm t}J = X$ is equivalent to $X^{\mathrm t}J = JX$; putting $Y = JX$, so that $X = -JY$, the condition becomes $(-JY)^{\mathrm t}J = Y$, that is $-Y^{\mathrm t}J^{\mathrm t}J = Y$, and $J^{\mathrm t}J = -J^2 = 1$, so $-Y^{\mathrm t} = Y$: $Y = JX$ is skew-symmetric.

**Remark.** The symplectic involution is the transpose twisted by $J$: since $J^{-1} = -J$ one has $X^{\tau} = -JX^{\mathrm t}J$. If $J'$ gives the same involution then $J'J^{-1}$ commutes with every $X^{\mathrm t}$ and is therefore a central scalar, and the conditions $J'^{\mathrm t} = -J'$, $J'^2 = -1$ force $J' = \pm J$; so $J$ is determined by the involution up to sign.

## Symmetric and Skew Matrices

**Proposition.** Let $2$ be invertible in $R$. Every matrix decomposes uniquely as the sum of a symmetric and a skew-symmetric matrix under the transpose,
$$
X = \tfrac12(X+X^{\mathrm t}) + \tfrac12(X-X^{\mathrm t}),
$$
and the same with $X^{\mathrm t}$ replaced by $X^{*}$ or $X^{\tau}$. In each case the symmetric and the skew matrices are the eigenspaces of the involution for $+1$ and $-1$, and the fixed set is the symmetric one.

**Proof.** This is the additive decomposition of *Involutive Rings* applied to the three involutions; the two summands are fixed or negated by the involution because it is additive of order two, and the decomposition is direct because the involution has no nonzero element on which it is both $\mathrm{id}$ and $-\mathrm{id}$ when $2$ is invertible.

**Example (the symmetric and skew sets of the transpose).** For $n = 2$ and $R$ a field with $2 \neq 0$, a symmetric matrix is $\begin{pmatrix} a & b \\ b & d\end{pmatrix}$ and a skew-symmetric matrix is $\begin{pmatrix} 0 & c \\ -c & 0\end{pmatrix}$, so $\dim \mathrm{Sym} = 3$ and $\dim \mathrm{Skew} = 1$, in agreement with $n(n+1)/2 = 3$ and $n(n-1)/2 = 1$.

**Example (Hermitian and skew-Hermitian).** Over $\mathbb{C}$ with the conjugation the $\sigma$-Hermitian matrices are the Hermitian ones, $X^{*} = X$, and the $\sigma$-skew-Hermitian matrices satisfy $X^{*} = -X$, so the skew-Hermitian matrices are $i$ times the Hermitian ones. The fixed set is not a complex subspace but a real one, because the involution is not complex-linear.

**Example (the symplectic symmetric matrices).** For $n = 2$ and $J = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$ the $\tau$-symmetric matrices are those with $JX$ skew-symmetric, that is, $X = \begin{pmatrix} a & b \\ c & -a\end{pmatrix}$, so $\dim \mathrm{Sym}$ is $3$, the same value as for the transpose in dimension $2$; the two involutions are nevertheless inequivalent, because in higher even dimension the dimensions $\tfrac12 n(n+1)$ and $\tfrac12 n(n-1)$ differ.

## The Classification of the Involutions of M_n(R)

### First and Second Kind

**Definition.** An involution $\sigma$ of an $F$-algebra $A$ is of the **first kind** when it fixes the centre elementwise, $\sigma(z) = z$ for all $z \in Z(A)$, and of the **second kind** (or of the **second kind, unitary**) when it acts on the centre by a nontrivial automorphism of order two. For $A = M_n(F)$ with $F$ a field, the centre is $F$ and the first-kind involutions are those fixing $F$; a second-kind involution exists only when $F$ has an automorphism $\sigma_0$ of order two, and is then the composition of a first-kind involution with the coefficientwise $\sigma_0$.

**Proposition.** The transpose and the symplectic involution of $M_n(F)$ are of the first kind; the conjugate transpose of $M_n(F)$ for a nontrivial $\sigma$ of $F$ is of the second kind. The fixed set of a second-kind involution is a vector space over the fixed field $F^{\sigma}$, and $F$ is a quadratic extension of it.

**Proof.** The centre of $M_n(F)$ is $F I$, and the transpose and the symplectic involution fix every scalar matrix; the conjugate transpose sends the scalar matrix $zI$ to $\sigma(z)I$, which is $zI$ only for $z \in F^\sigma$. The last statement is the quadratic-extension theorem of *Involutive Rings*.

### The Two Types of the First Kind

**Theorem (the classification of the first kind).** Let $F$ be a field and let $\sigma$ be an involution of the first kind of $M_n(F)$. Then $\sigma$ is of **transpose type** if there are $n$ orthogonal symmetric idempotents with sum $1$, and of **symplectic type** otherwise; the transpose type occurs for every $n$, the symplectic type only for even $n$, and the two types are inequivalent.

**Proof.** The transpose has the $n$ matrix units $e_{ii}$ as orthogonal symmetric idempotents summing to $1$. The symplectic involution fixes no such family: its symmetric idempotents have even rank, because for a $\tau$-symmetric idempotent $E$ the matrix $JE$ is skew-symmetric and $JE = J E^2 = (JE)E$, forcing $\operatorname{tr}(JE) = 0$ and hence $\operatorname{rank} E$ even; so a sum of orthogonal symmetric idempotents equal to $1$ would have even trace $n$, which excludes odd $n$ and, for even $n$, would need $n$ summands of even rank at least $2$, which is impossible. The two types are inequivalent by the dimension of the symmetric part (next paragraph).

**Theorem (the separating invariant).** The dimension of the symmetric part of a first-kind involution of $M_n(F)$ is

$$
\dim_F \mathrm{Sym}(M_n(F),\sigma) =
\begin{cases}
\tfrac12 n(n+1) & \text{transpose type},\\[2pt]
\tfrac12 n(n-1) & \text{symplectic type}.
\end{cases}
$$

Hence the transpose and the symplectic involutions are inequivalent for $n \geq 2$, and the type is determined by this dimension.

**Proof.** For the transpose the symmetric matrices are free on the $\tfrac12 n(n+1)$ positions on and above the diagonal, hence of dimension $\tfrac12 n(n+1)$; the skew-symmetric matrices are free on the $\tfrac12 n(n-1)$ positions above the diagonal, giving the second value for the symplectic involution because its symmetric part is the image of the skew-symmetric matrices under $X \mapsto J^{-1}X$, which is an isomorphism of vector spaces.

**Remark (uniqueness within a type).** Two first-kind involutions of $M_n(F)$ are equivalent, that is, conjugate by an automorphism of $M_n(F)$, exactly when they have the same kind and type; since every automorphism of $M_n(F)$ is inner by *Involutions of a Central Simple Algebra*, the conjugating automorphism is conjugation by a unit, and the classification is the classification of the involutions up to conjugation. The full statement, with the arithmetic invariants that distinguish two algebras of the same type, is the Albert classification of involutions of central simple algebras, and it is deferred to *Involutions of a Central Simple Algebra* and to the forms of Part II.

## Examples

**(a) The transpose over $\mathbb{Z}$.** On $M_2(\mathbb{Z})$ the transpose is an involution whose symmetric matrices are $\begin{pmatrix} a & b \\ b & d\end{pmatrix}$ and whose skew-symmetric matrices are $\begin{pmatrix} 0 & c \\ -c & 0\end{pmatrix}$; the fixed ring is not a subring, since $\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\1&1\end{pmatrix} = \begin{pmatrix}1&2\\0&1\end{pmatrix}$ is not symmetric, as in *Involutive Rings*.

**(b) The conjugate transpose over $\mathbb{C}$.** On $M_n(\mathbb{C})$ with the conjugation the involution is of the second kind, its fixed field is $\mathbb{R}$, and the Hermitian and skew-Hermitian matrices are the two eigenspaces; the unitary matrices are the units fixed by the anti-automorphism $X \mapsto (X^{*})^{-1}$, that is, those with $U^{*} = U^{-1}$.

**(c) The symplectic involution in dimension two.** On $M_2(F)$ with $J = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$ the involution $X \mapsto -JX^{\mathrm t}J$ has symmetric part $\{\begin{pmatrix}a&b\\c&-a\end{pmatrix}\}$, of dimension $3$; since $\tfrac12 n(n+1) = 3$ and $\tfrac12 n(n-1) = 1$ for $n = 2$, and the symplectic symmetric part has dimension $3$, the dimension invariant alone does not separate the two types in dimension two. It does in dimension four, where the two values $10$ and $6$ differ, and the two types are inequivalent for every $n \geq 2$ by the theorem above.

**(d) Quaternion matrices.** For the quaternion algebra $\mathbb{H}$ over $\mathbb{R}$ and its conjugate involution, $M_n(\mathbb{H})$ carries the conjugate transpose, of the second kind relative to the centre $\mathbb{R}$; the fixed set is the set of Hermitian quaternion matrices, and the units with $U^{*} = U^{-1}$ form the quaternion unitary group, met again among the matrix groups later in the corpus.

## Summary

The matrix ring $M_n(R)$ carries the **transpose** $X \mapsto X^{\mathrm t}$, an involution for every ring $R$ with symmetric fixed set and permutation $e_{ij} \leftrightarrow e_{ji}$; the **conjugate transpose** $X \mapsto (\sigma(x_{ji}))$ for a commutative coefficient ring with an involution $\sigma$, whose fixed matrices are the $\sigma$-Hermitian ones; and the **symplectic involution** $X \mapsto J^{-1}X^{\mathrm t}J$ for $J^{\mathrm t} = -J$, $J^2 = -1$, whose fixed matrices are those with $JX$ skew-symmetric, and which needs even dimension. Each has a symmetric-plus-skew decomposition when $2$ is invertible, with the symmetric and skew matrices the eigenspaces.

An involution is of the **first kind** when it fixes the centre and of the **second kind** when it acts on the centre by a nontrivial automorphism; the transpose and the symplectic involutions are of the first kind, the conjugate transpose of the second kind. The first-kind involutions of $M_n(F)$, up to conjugation, are the **transpose type**, occurring for every $n$ and characterised by $n$ orthogonal symmetric idempotents summing to $1$, and the **symplectic type**, occurring only for even $n$; the separating invariant is the dimension of the symmetric part, $\tfrac12 n(n+1)$ in the transpose type and $\tfrac12 n(n-1)$ in the symplectic type, so the two are inequivalent in dimension at least two. The arithmetic invariant that distinguishes two algebras of the same type is the business of the central simple algebra and of the forms of Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_n(R)$ | Matrix ring over a ring $R$, units $M_n(R)^\times$ |
| $e_{ij}$ | Matrix units |
| $X^{\mathrm t}$, $\operatorname{tr}(X)$ | Transpose and trace |
| $T(X) = X^{\mathrm t}$ | Involution of transpose type; fixed set the symmetric matrices |
| $\sigma$ | Involution of the commutative coefficient ring |
| $X^{*} = (\sigma(x_{ji}))$ | Conjugate transpose; fixed set the $\sigma$-Hermitian matrices |
| $\tau(X) = X^{\tau} = J^{-1}X^{\mathrm t}J$ | Symplectic involution |
| $J$, with $J^{\mathrm t} = -J$, $J^2 = -1$ | The matrix twisting the symplectic involution; even $n$ |
| $JX$ skew-symmetric | Equivalent form of $\tau$-symmetry |
| $\mathrm{Sym}$, $\mathrm{Skew}$ | Symmetric and skew matrices, the eigenspaces |
| $\tfrac12 n(n+1)$, $\tfrac12 n(n-1)$ | Dimensions of the symmetric part in the two types |
| $U^{*}U = 1$ | Unitary matrices, the units fixed by the twisted action |
| first kind, second kind | Involution fixing the centre, or acting on it by a nontrivial order-two automorphism |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and skew matrices, the two types of the first kind and the idempotent criterion.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the classification of the involutions of a matrix ring and the symplectic type.
- Albert Adrian Albert, *Structure of Algebras*, American Mathematical Society Colloquium Publications 24 (1939), for the classification of involutions of central simple algebras, which begins with the matrix case.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2nd ed. 2013), for symmetric, Hermitian, skew-symmetric and skew-Hermitian matrices and their decompositions.
