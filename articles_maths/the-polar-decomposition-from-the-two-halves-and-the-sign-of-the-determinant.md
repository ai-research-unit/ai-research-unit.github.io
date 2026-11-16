# __The Polar Decomposition from the Two Halves and the Sign of the Determinant__

## Introduction

**Every invertible real matrix is the product of a rotation and a stretch in exactly one way, and the rotation carries the whole sign of the determinant.** The decomposition reads the matrix through the involution $A\mapsto A^{\mathsf T}$: the symmetric half gives the stretch, and what remains is orthogonal.

The article proves existence from the positive square root of $A^{\mathsf T}A$, proves uniqueness from the uniqueness of that square root, shows that $\det P>0$ and hence that the sign of $\det A$ is the sign of $\det Q$, rewrites the decomposition in the second order and in the singular value form, and draws the topological consequence: the identity component of $\mathrm{GL}_n(\mathbb{R})$ is $\mathrm{SO}(n)\times\operatorname{Sym}_n$. It assumes *The Exponential of the Symmetric Part: Stretches and the Positive Cone* for the cone and its logarithm, and *The Involutions of the First Kind: Transpose and Symplectic* for the two halves.

## The Statement

**Theorem (polar decomposition).** Every $A\in\mathrm{GL}_n(\mathbb{R})$ is uniquely

$$
A=QP,
$$

with $Q\in\mathrm{O}(n)$ and $P\in\operatorname{Sym}_n^{>0}$.

**The two factors are of different kinds.** The orthogonal factor has all its eigenvalues on the unit circle and preserves all lengths; the symmetric positive factor has positive real eigenvalues and stretches along an orthonormal frame. The decomposition separates the two, and the theorem says the separation is unique.

**The name comes from the scalar case.** For $n=1$ a nonzero real number is $a=(\pm1)|a|$, the product of a sign and a positive number. The polar decomposition is that identity with the sign replaced by an orthogonal matrix and the modulus by a positive definite one.

**The complex analogue is the polar form of a number.** Over $\mathbb{C}$ the same theorem reads $z=\mathrm{e}^{\mathrm{i}\theta}r$ with $r>0$. Over $\mathbb{R}$ the unit circle is replaced by $\mathrm{O}(n)$, and the modulus by the cone; the whole content is that the replacement works in every dimension, and that the stretch is a function of $A^{\mathsf T}A$ alone, so it is forced by the matrix and not chosen.

## Existence

**Step one: $A^{\mathsf T}A$ is positive definite.** For $x\ne0$,

$$
x^{\mathsf T}A^{\mathsf T}Ax=\|Ax\|^{2}>0,
$$

because $A$ is invertible and $Ax\ne0$. The matrix $A^{\mathsf T}A$ is symmetric by construction, so it lies in $\operatorname{Sym}_n^{>0}$, and by the spectral theorem it has a unique positive definite square root

$$
P=(A^{\mathsf T}A)^{1/2},
$$

computed as $P=Q\operatorname{diag}(\sqrt{\mu_i})Q^{\mathsf T}$ from a spectral decomposition $A^{\mathsf T}A=Q\operatorname{diag}(\mu_i)Q^{\mathsf T}$ with $\mu_i>0$.

**Step two: define $Q=AP^{-1}$.** The matrix $P$ is invertible because it is positive definite, so $Q$ is defined, and $QP=A$ by construction.

**Step three: $Q$ is orthogonal.** Compute

$$
Q^{\mathsf T}Q=P^{-1}A^{\mathsf T}AP^{-1}=P^{-1}P^{2}P^{-1}=\mathrm{I},
$$

using $A^{\mathsf T}A=P^{2}$ and $P=P^{\mathsf T}$. A square matrix with $Q^{\mathsf T}Q=\mathrm{I}$ is invertible with inverse $Q^{\mathsf T}$, so $QQ^{\mathsf T}=\mathrm{I}$ as well and $Q\in\mathrm{O}(n)$.

**The square root is the only place where a choice could hide.** It does not hide there: the square root of a positive definite matrix is unique, as the next section shows.

## Uniqueness

**Lemma.** A matrix $P\in\operatorname{Sym}_n^{>0}$ has exactly one square root in $\operatorname{Sym}_n^{>0}$.

*Proof.* Let $P_1,P_2\in\operatorname{Sym}_n^{>0}$ with $P_1^{2}=P_2^{2}=R$. Since $P_1$ commutes with $P_1^{2}=R$, it preserves every eigenspace of $R$: if $Rv=\mu v$ then $R(P_1v)=P_1Rv=\mu P_1v$. On the eigenspace $E_\mu$ the matrix $P_1^{2}$ acts as $\mu\mathrm{I}$ with $\mu>0$, and a positive definite symmetric matrix whose square is $\mu\mathrm{I}$ is $\sqrt{\mu}\,\mathrm{I}$ there, because its eigenvalues are positive and square to $\mu$. So $P_1$ acts as $\sqrt{\mu}\,\mathrm{I}$ on each $E_\mu$, and so does $P_2$. Hence $P_1=P_2$.

**Theorem (uniqueness of the decomposition).** If $A=Q_1P_1=Q_2P_2$ with $Q_i\in\mathrm{O}(n)$ and $P_i\in\operatorname{Sym}_n^{>0}$, then $Q_1=Q_2$ and $P_1=P_2$.

*Proof.* From $A=Q_1P_1=Q_2P_2$ and $Q_i^{\mathsf T}Q_i=\mathrm{I}$,

$$
P_1^{2}=(Q_1P_1)^{\mathsf T}(Q_1P_1)=A^{\mathsf T}A=(Q_2P_2)^{\mathsf T}(Q_2P_2)=P_2^{2}.
$$

By the lemma $P_1=P_2$, and then $Q_1=Q_2$ because $P_1$ is invertible.

**Both factors must lie in the cone.** The lemma uses the positivity of both square roots. If $P_2$ is only symmetric, it may act as $-\sqrt{\mu}\,\mathrm{I}$ on an eigenspace of $R=P^{2}$, and then $P_2=-P$ on that eigenspace while $P_2^{2}=P^{2}$ still holds. So the cone is exactly what makes the decomposition unique: a symmetric factor outside it gives, for each eigenspace, a second choice of sign.

## The Sign of the Determinant

**Theorem.** For $A=QP$ one has $\det P=|\det A|$ and $\operatorname{sgn}\det A=\det Q$.

*Proof.* The determinant is multiplicative, so $\det A=\det Q\det P$, and $\det Q=\pm1$ because $Q$ is orthogonal. Further

$$
\det P=(\det P^{2})^{1/2}=(\det A^{\mathsf T}A)^{1/2}=|\det A|>0,
$$

using $\det A^{\mathsf T}=\det A$. Hence $\det A=\det Q\,|\det A|$ and the sign of $\det A$ is $\det Q$.

**Corollary.** $A\in\mathrm{GL}_n(\mathbb{R})^{+}$ if and only if the orthogonal factor lies in $\mathrm{SO}(n)$.

**The two components are read off from one factor.** The set $\mathrm{GL}_n(\mathbb{R})$ is the disjoint union of $\{\det>0\}$ and $\{\det<0\}$, each open and closed. The polar decomposition carries the first onto $\mathrm{SO}(n)\times\operatorname{Sym}_n$ and the second onto $\mathrm{O}^{-}(n)\times\operatorname{Sym}_n$, where $\mathrm{O}^{-}(n)=\{Q:Q^{\mathsf T}Q=\mathrm{I},\ \det Q=-1\}$, and both are diffeomorphisms. Each product is connected, being the product of two connected sets, so the two open sets are the two components, and they differ only in the orthogonal factor.

**The negative component is a copy of the positive one.** Left multiplication by any fixed $J\in\mathrm{O}^{-}(n)$, for instance $J=\operatorname{diag}(-1,1,\dots,1)$, is a diffeomorphism from $\mathrm{SO}(n)$ onto $\mathrm{O}^{-}(n)$, so both components are diffeomorphic to $\mathrm{SO}(n)\times\operatorname{Sym}_n$ and hence to each other.

## The Second Order

**Theorem.** Every $A\in\mathrm{GL}_n(\mathbb{R})$ is also uniquely $A=P'Q$ with $Q\in\mathrm{O}(n)$ and $P'\in\operatorname{Sym}_n^{>0}$, namely

$$
P'=AQ^{\mathsf T}=QPQ^{\mathsf T},
$$

the conjugate of $P$ by $Q$.

*Proof.* With $A=QP$ put $P'=QPQ^{\mathsf T}$. It is symmetric and positive definite, since $x^{\mathsf T}P'x=(Q^{\mathsf T}x)^{\mathsf T}P(Q^{\mathsf T}x)>0$ for $x\ne0$, and $P'Q=QPQ^{\mathsf T}Q=QP=A$. Uniqueness follows from the same argument as before, applied to $A^{\mathsf T}A=QP'^{2}Q^{\mathsf T}$.

**The two orders give different symmetric factors.** $P$ is the square root of $A^{\mathsf T}A$, while $P'$ is the square root of $AA^{\mathsf T}$. The two have the same eigenvalues, since $AA^{\mathsf T}=Q(A^{\mathsf T}A)Q^{\mathsf T}$, and they differ by conjugation when $Q\ne\pm\mathrm{I}$.

**The first order is the one that reads the columns.** $A^{\mathsf T}A$ is the Gram matrix of the columns of $A$; its square root measures the stretch along the input frame. The second order measures the stretch along the output frame. The rotation factor is the same in both.

## The Singular Value Decomposition

**Theorem.** Every $A\in M_n(\mathbb{R})$ of rank $r$ is $A=U\Sigma V^{\mathsf T}$ with $U,V\in\mathrm{O}(n)$ and $\Sigma$ diagonal with $r$ positive entries and $n-r$ zeros. If $A$ is invertible, $A=QP$ gives $U=QV$, $\Sigma$ the diagonal matrix of the eigenvalues of $P$, and $V$ the orthogonal matrix of its eigenvectors.

*Proof.* Diagonalise the positive definite factor, $P=V\Sigma V^{\mathsf T}$ with $\Sigma=\operatorname{diag}(\sigma_1,\dots,\sigma_n)$ and $\sigma_i>0$. Then

$$
A=QP=QV\,\Sigma V^{\mathsf T}=U\Sigma V^{\mathsf T},\qquad U=QV .
$$

Both $U$ and $V$ are orthogonal, and $\Sigma$ carries the eigenvalues of $P$, which are the singular values of $A$. For a singular $A$ the same computation runs with $A^{\mathsf T}A$ positive semidefinite, and the zero eigenvalues give the zero block of $\Sigma$.

**The singular values are the eigenvalues of $P$.** They are $\sigma_i=\sqrt{\mu_i}$ where $\mu_i$ are the eigenvalues of $A^{\mathsf T}A$, so they are nonnegative and the number of positive ones is the rank.

**The polar decomposition is the SVD with the two orthogonal factors merged.** The SVD separates $U$ and $V$ and leaves the diagonal stretch between them; the polar decomposition merges $U$ and $V$ into $Q=UV^{\mathsf T}$ and keeps the stretch $P=V\Sigma V^{\mathsf T}$ in the input frame. The merge loses no information for invertible $A$: from $Q$ and $P$ one recovers $V$ and $\Sigma$ by diagonalising $P$.

**The signs.** If $A\in\mathrm{GL}_n(\mathbb{R})^{+}$ then $U$ and $V$ can be chosen in $\mathrm{SO}(n)$ with $\det U\det V=1$, because then $\det Q=1$. For $\det A<0$ exactly one of $U,V$ carries the negative sign.

## The Topology

**Corollary.** $\mathrm{GL}_n(\mathbb{R})^{+}$ is diffeomorphic to $\mathrm{SO}(n)\times\operatorname{Sym}_n$, and $\mathrm{GL}_n(\mathbb{R})$ is diffeomorphic to the disjoint union of two such products.

*Proof.* The map $(Q,S)\mapsto Q\exp(S)$ is a bijection by the polar decomposition and the bijection $\exp:\operatorname{Sym}_n\to\operatorname{Sym}_n^{>0}$, it is smooth, and its inverse $A\mapsto(Q,\log P)$ is smooth. A smooth bijection with a smooth inverse is a diffeomorphism.

**The count.** The dimensions are $n(n-1)/2$ for the orthogonal factor and $n(n+1)/2$ for the symmetric one, and

$$
\frac{n(n-1)}{2}+\frac{n(n+1)}{2}=n^{2}=\dim\mathrm{GL}_n(\mathbb{R}).
$$

So the product fills the group exactly, with no room to spare, and the two components are the two copies.

**A consequence for the fundamental group.** The symmetric factor is contractible, since it is the image of the linear space $\operatorname{Sym}_n$ under a homeomorphism. So the homotopy type of $\mathrm{GL}_n(\mathbb{R})^{+}$ is that of $\mathrm{SO}(n)$, and $\pi_1\big(\mathrm{GL}_n(\mathbb{R})^{+}\big)=\mathbb{Z}/2$ for $n\ge3$.

**What the decomposition does not say.** It does not say the group is a direct product of groups: the symmetric factor is not closed under multiplication. The statement is about manifolds and about the group law only through the formula $A=QP$.

## The Numerical Check

**The reconstruction.** At $n=3$ a random invertible matrix is decomposed as $P=(A^{\mathsf T}A)^{1/2}$ and $Q=AP^{-1}$. The residual $\|A-QP\|$ is $4\times10^{-16}$, the orthogonality defect $\|Q^{\mathsf T}Q-\mathrm{I}\|$ is $7\times10^{-16}$, and $P$ is positive definite to $10^{-16}$.

**The sign.** For a random $A$ with $\det A<0$ the computed $\det Q$ is $-1$ to $10^{-15}$, and $\det P=|\det A|$ to the same accuracy. For $A$ with $\det A>0$, $\det Q=+1$.

**The second order.** With $P'=AQ^{\mathsf T}$ the symmetry defect is $0$, the residual $\|A-P'Q\|$ is $2\times10^{-15}$, and $P'$ is positive definite. The eigenvalues of $P$ and $P'$ agree to machine precision.

**The split of the positive part.** Writing a random $A$ with positive determinant as $Q\exp(S)$ with $S=\tfrac12\log(A^{\mathsf T}A)$ gives $Q\in\mathrm{SO}(n)$ and reconstruction residual $2\times10^{-16}$ at $n=3$.

## Summary

Every invertible real matrix is uniquely $A=QP$ with $Q$ orthogonal and $P$ symmetric positive definite; $P$ is the positive square root of $A^{\mathsf T}A$, $Q=AP^{-1}$, and uniqueness follows from the uniqueness of the positive square root. Because $\det P=|\det A|>0$ and $\det Q=\pm1$, the sign of $\det A$ is the sign of $\det Q$: the two components of $\mathrm{GL}_n(\mathbb{R})$ are read off from the orthogonal factor alone, and $\mathrm{GL}_n(\mathbb{R})^{+}$ is diffeomorphic to $\mathrm{SO}(n)\times\operatorname{Sym}_n$, of dimension $n(n-1)/2+n(n+1)/2=n^{2}$. The second order $A=P'Q$ with $P'=QPQ^{\mathsf T}$ gives the stretch of the output frame, and the singular value decomposition is the polar decomposition with the orthogonal factor split into two. The sign of the determinant, the two components, and the product structure of each, are therefore three readings of one theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=QP$ | The polar decomposition, rotation times stretch |
| $P$ | The positive definite factor, $(A^{\mathsf T}A)^{1/2}$ |
| $Q$ | The orthogonal factor, $AP^{-1}$ |
| $P'=QPQ^{\mathsf T}$ | The symmetric factor of the order $P'Q$ |
| $A^{\mathsf T}A$ | The Gram matrix of the columns |
| $\mu_i,\sigma_i=\sqrt{\mu_i}$ | The eigenvalues of $A^{\mathsf T}A$ and the singular values |
| $\Sigma$ | The diagonal matrix of singular values |
| $\mathrm{O}^{-}(n)$ | The orthogonal matrices of determinant $-1$ |
| $\mathrm{GL}_n(\mathbb{R})^{+}$ | The matrices of positive determinant |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the polar decomposition, its uniqueness and the singular value decomposition.
- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the cone and the square root.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone](the-exponential-of-the-symmetric-part-stretches-and-the-positive-cone.html), for the cone, the logarithm and the stretch factor $\exp(S)$.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the determinant and the two components of the group of invertibles.
- [The Involutions of the First Kind: Transpose and Symplectic](the-involutions-of-the-first-kind-transpose-and-symplectic.html), for the symmetric and antisymmetric halves.
