# __The Two Halves as Orthogonal Complements at $n=4$__

## Introduction

**The symmetric and the antisymmetric matrices are orthogonal for the trace pairing, and they are exact orthogonal complements of one another; what separates them is not orthogonality but the sign of the form, positive on the ten symmetric directions and negative on the six antisymmetric ones over the reals.**

The article proves $\operatorname{tr}(SK)=0$, shows that the direct sum is orthogonal for the trace pairing and for the Hilbert–Schmidt form alike, explains why "orthogonal" and "definite" are different statements and that the trace pairing is indefinite on each half over $\mathbb{C}$ even while nondegenerate, and records that neither half is an ideal or a subalgebra.

It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$* for the definitions and the projections, and *The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$* for the inertia. The case $n=2$ is *The Two Halves as Orthogonal Complements at $n=2$*. The forms themselves are *The Hilbert–Schmidt Form at $n=4$*.

## The Orthogonality

**Theorem.** For $S\in\operatorname{Sym}_4$ and $K\in\operatorname{Skew}_4$, $\operatorname{tr}(SK)=0$.

**Proof.** The transpose of a scalar is itself, so $\operatorname{tr}(SK)=\operatorname{tr}\bigl((SK)^{\mathsf T}\bigr)=\operatorname{tr}(K^{\mathsf T}S^{\mathsf T})=\operatorname{tr}(-KS)=-\operatorname{tr}(SK)$. A number equal to its negative is zero.

**Corollary.** The two halves are orthogonal for $\beta(X,Y)=\operatorname{tr}(XY)$, and since $\dim\operatorname{Sym}_4+\dim\operatorname{Skew}_4=16=\dim M_4$, each is the orthogonal complement of the other for $\beta$.

**Proof.** Orthogonality is the theorem. For the complement statement one needs $\beta$ nondegenerate on the whole algebra: if $\operatorname{tr}(AY)=0$ for all $Y$ then $A=0$, by taking $Y=E_{ji}$ at a nonzero entry $A_{ij}$. A nondegenerate form with two orthogonal subspaces whose dimensions add to the total makes each the complement of the other.

**Corollary.** The same orthogonality holds for the Hilbert–Schmidt form $\langle A,B\rangle=\operatorname{tr}(A^{\ast}B)$.

**Proof.** For real $S$ and $K$ one has $\operatorname{tr}(S^{\mathsf T}K)=\operatorname{tr}(SK)=0$; for complex ones the conjugate does not change the vanishing, since $\operatorname{tr}(\bar S^{\mathsf T}K)$ is a sum of terms each of which is the conjugate of a term of $\operatorname{tr}(SK)$.

**The projections are orthogonal projections.** With respect to the Hilbert–Schmidt form the map $A\mapsto\tfrac12(A+A^{\mathsf T})$ is the orthogonal projection onto $\operatorname{Sym}_4$, because the kernel is $\operatorname{Skew}_4$ and it is orthogonal to the image.

**Proof.** The projection kills exactly the antisymmetric part, and the two halves are orthogonal, which is the characterisation of an orthogonal projection for a definite form.

## The Two Forms and What "Orthogonal" Does Not Say

**The two forms.** $\beta(X,Y)=\operatorname{tr}(XY)$ is symmetric and $\mathbb{C}$-bilinear; $\langle X,Y\rangle=\operatorname{tr}(X^{\ast}Y)$ is Hermitian and positive definite on the real $32$-dimensional space.

**Proposition.** On the symmetric half, $\beta(X,X)=\sum_{i,j}X_{ij}^{2}$; on the antisymmetric half, $\beta(K,K)=-2\sum_{i<j}K_{ij}^{2}$.

**Proof.** For symmetric $X$ one has $X_{ji}=X_{ij}$, so the diagonal of $X^{2}$ sums to $\sum_{i,j}X_{ij}^{2}$. For antisymmetric $K$ one has $K_{ji}=-K_{ij}$, so the same sum carries a minus sign and each unordered pair is counted twice.

**Corollary.** Over $\mathbb{R}$ the form $\beta$ is positive definite on $\operatorname{Sym}_4(\mathbb{R})$ and negative definite on $\operatorname{Skew}_4(\mathbb{R})$, hence of inertia $(10,6)$ on $M_4(\mathbb{R})$.

**Proof.** The two displays are sums of squares with a sign, and the halves are orthogonal.

**Corollary (the indefinite reading over $\mathbb{C}$).** Over $\mathbb{C}$ the form $\beta$ is nondegenerate on each half but definite on neither, and it has isotropic vectors.

**Proof.** Nondegeneracy: if $\beta(X,Y)=0$ for all symmetric $Y$ then taking $Y=E_{ii}$ and $Y=E_{ij}+E_{ji}$ kills every entry of $X$. Isotropy: the symmetric matrix $X=E_{11}+iE_{12}+iE_{21}-E_{22}$ has $\beta(X,X)=1+i^{2}+i^{2}+1=0$.

**What this shows.** Orthogonality is a statement about cross terms and holds over $\mathbb{C}$ as well; definiteness is a statement about signs and holds only on the real slice. Writing "the halves are orthogonal for the definite form but not for the indefinite one" is a confusion: they are orthogonal for both, and the indefinite form merely ceases to be definite on each half. The correct dichotomy is: orthogonal always, definite only over $\mathbb{R}$.

**The count of signs.** $10=\tfrac{4\cdot5}{2}$ is the number of entries on and above the diagonal, and $6=\tfrac{4\cdot3}{2}$ the number above it. These are also the dimensions of $\operatorname{Sym}^{2}\mathbb{C}^{4}$ and $\Lambda^{2}\mathbb{C}^{4}$.

## Neither Half Is an Ideal and Neither Is Closed

**Proposition.** Neither half is a two-sided ideal, and neither is closed under multiplication.

**Proof.** $E_{11}$ is symmetric and $E_{12}$ is neither, and $E_{11}E_{12}=E_{12}$ leaves the symmetric half; multiplying a symmetric matrix on the left by $E_{21}$ turns a symmetric entry into an antisymmetric one. For closure, $S=E_{12}+E_{21}$ and $S'=E_{11}$ are symmetric with the product $E_{21}$, which is antisymmetric.

**Corollary.** The decomposition $M_4=\operatorname{Sym}_4\oplus\operatorname{Skew}_4$ is a decomposition of the algebra as a vector space, not as a direct sum of ideals.

**Proof.** A direct sum of ideals would make every product stay in its summand, which the proposition denies.

**The structure that does survive.** $\operatorname{Sym}_4$ is closed under the anticommutator and is a Jordan algebra with the unit $\mathrm I_4$; $\operatorname{Skew}_4$ is closed under the commutator and is a Lie algebra isomorphic to $\mathfrak{so}(4)$. The two halves are the two products of the same space, and the pair is *The Jordan Algebra $\operatorname{Sym}_4$* and *The Lie Algebra $\operatorname{Skew}_4$ and $\mathfrak{so}(4)$*.

**The dimension checks.** $\dim\operatorname{Sym}_4=10$ is the dimension of the Jordan algebra and also of $UT_4$; $\dim\operatorname{Skew}_4=6$ is the dimension of $\mathfrak{so}(4)$ and of $\Lambda^{2}\mathbb{C}^{4}$. The coincidence of numbers is not a coincidence of spaces, which is the point of *$UT_4$ as the Complement of the Antisymmetric Part*.

## The Coordinate Subspaces of a Single Basis

**In the axis-free basis the split is a coordinate split.** The pairing is diagonal,

$$
\operatorname{tr}(T_{\mu\nu}T_{\rho\sigma})=\pm4\,\delta_{\mu\rho}\delta_{\nu\sigma},
$$

with $+4$ on the ten symmetric elements and $-4$ on the six antisymmetric ones. Hence $\operatorname{Sym}_4$ is the span of the ten and $\operatorname{Skew}_4$ the span of the six.

**Proof.** Each half is the eigenspace of the transpose for its eigenvalue, and the sixteen elements are sorted into the two eigenspaces by comparing each with its transpose; a coordinate subspace spanned by basis vectors of one eigenspace is that eigenspace.

**Corollary.** In this basis the orthogonal complement of a half is read off by setting the other coordinates to zero, and the pairing has no cross terms to compute.

**Proof.** A diagonal form pairs coordinate subspaces dually, so the annihilator of the six coordinates is the span of the ten.

**The contrast with the matrix units.** In the basis $\{E_{ij}\}$ the pairing is not diagonal: $\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}$, a permutation matrix on the $16$ coordinates, and the symmetric and antisymmetric halves are not coordinate subspaces. The matrix units are canonical and define the product; the axis-free sixteen are the basis in which the two halves and the pairing are visible at once.

**The same statement in coordinates.** Writing $A=\sum c_{\mu\nu}T_{\mu\nu}$, orthogonality reads: the six coefficients $c_{tx},c_{ty},c_{tz},c_{xt},c_{yt},c_{zt}$ and the other ten never pair. This is the coordinate form of $\operatorname{tr}(SK)=0$, and it needs no transpose because the transpose is already built into the basis.

## Summary

For symmetric $S$ and antisymmetric $K$ the trace $\operatorname{tr}(SK)$ equals its own negative, so the two halves are orthogonal for the trace pairing and for the Hilbert–Schmidt form, and each is the other's orthogonal complement because the algebra is $10+6=16$ and the trace pairing is nondegenerate.

On the symmetric half the trace form is the sum of the squares of the entries, on the antisymmetric half minus twice the sum over the upper triangle; over $\mathbb{R}$ that makes the form positive definite on one half and negative definite on the other, of inertia $(10,6)$, and over $\mathbb{C}$ it makes the form nondegenerate but isotropic on each half. Orthogonality is field-independent; definiteness is not.

Neither half is an ideal and neither is closed under the product; the symmetric half is a Jordan algebra and the antisymmetric half a Lie algebra. In the axis-free basis the split is a split of coordinates with a sign of $4$ attached to each element, and the orthogonality is the vanishing of every cross pairing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\beta(X,Y)=\operatorname{tr}(XY)$ | the trace pairing, symmetric and indefinite |
| $\langle X,Y\rangle=\operatorname{tr}(X^{\ast}Y)$ | the Hilbert–Schmidt form, positive definite |
| $\operatorname{Sym}_4$, $\operatorname{Skew}_4$ | the two halves, dimensions $10$ and $6$ |
| $\tfrac12(A\pm A^{\mathsf T})$ | the orthogonal projections |
| $T_{\mu\nu}$ | the axis-free basis, diagonalising $\beta$ |
| $c_{\mu\nu}$ | coordinates in that basis |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for orthogonal projections and the trace inner product.
- [The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m4c.html), for the inertia computed in the axis-free basis.
- [The Hilbert–Schmidt Form at $n=4$](the-hilbert-schmidt-form-at-n-4.html), for the definite form and its two orthonormal bases.
- [The Jordan Algebra $\operatorname{Sym}_4$](the-jordan-algebra-sym-4.html), for the product that the symmetric half does support.
- [The Two Halves as Orthogonal Complements at $n=2$](the-two-halves-as-orthogonal-complements-at-n-2.html), for the same argument at order two.
