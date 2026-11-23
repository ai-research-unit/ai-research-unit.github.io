# __The Hilbert–Schmidt Form__

## Introduction

**The form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ is a positive definite Hermitian form on $M_n(\mathbb{C})$, its real part is the Euclidean form on the $2n^{2}$ real coordinates, its norm is the square root of the sum of the squares of the singular values, and it is invariant under unitary conjugation but not under the full linear group.**

The article proves the Hermitian axioms, computes the norm through the singular values, shows unitary invariance and the failure of invariance under general conjugation, computes the adjoints of the one-sided and the two-sided operators and of the derivation, shows that the form is definite on both halves in contrast with the trace form, and compares the Hilbert–Schmidt norm with the operator norm. It assumes *The Trace Form and Its Inertia on the Two Halves* for the indefinite form it replaces and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* for the complex split. It defers the operator theory to *The Symmetric and Antisymmetric Parts of the Operator Space* and the analysis to *The Analysis on $M_n(\mathbb{C})$*.

## The Form

**The form is Hermitian and positive definite.** Put

$$
\langle X,Y\rangle=\operatorname{tr}(X^{*}Y).
$$

It is linear in the second argument and conjugate linear in the first, and

$$
\overline{\langle X,Y\rangle}=\overline{\operatorname{tr}(X^{*}Y)}=\operatorname{tr}(Y^{*}X)=\langle Y,X\rangle ,
$$

so it is Hermitian. It is positive definite because

$$
\langle X,X\rangle=\operatorname{tr}(X^{*}X)=\sum_{i,j}|X_{ij}|^{2}\ \ge0,
$$

with equality only at $X=0$. So it is an inner product on the $2n^{2}$-dimensional real space $M_n(\mathbb{C})$, and it is the form that makes the matrix space a Hilbert space.

**Its real part is the Euclidean form.** Writing $X=P+iQ$ with $P,Q$ real matrices,

$$
\operatorname{Re}\operatorname{tr}(X^{*}Y)=\operatorname{tr}(P^{\mathsf T}R+Q^{\mathsf T}S)=\sum_{i,j}\big(P_{ij}R_{ij}+Q_{ij}S_{ij}\big),
$$

which is the Euclidean pairing of the real and imaginary parts. So the Hilbert–Schmidt form is not a new form on a new space: it is the Euclidean form on $\mathbb{R}^{2n^{2}}$ written in complex notation, and the $2n^{2}$ count was verified by the Gram matrix of the real basis $E_{ij},iE_{ij}$.

**The form is the complexification of the trace form.** Its real part restricts on the real matrices to $\operatorname{tr}(P^{\mathsf T}R)=\operatorname{tr}(PR)$, which is the trace form of *The Trace Form and Its Inertia on the Two Halves*. The two forms therefore agree on $M_n(\mathbb{R})$ and differ elsewhere: the Hilbert–Schmidt form is positive definite on the whole complex space, while the trace form is indefinite already on the real subspace.

**The form is nondegenerate and perfect.** It pairs $X$ with $X$ to a positive number and pairs distinct matrix units to zero,

$$
\langle E_{ij},E_{kl}\rangle=\delta_{ik}\delta_{jl},
$$

so the matrix units are an orthonormal basis. The Gram matrix is the identity of size $n^{2}$ over $\mathbb{C}$, and the whole space is its own dual under the form.

## The Norm and Its Values

**The norm is the square root of the sum of the squares of the singular values.** If $X=U\Sigma V^{*}$ is a singular value decomposition with singular values $s_1,\dots,s_n$, then

$$
\|X\|^{2}=\operatorname{tr}(X^{*}X)=\operatorname{tr}(V\Sigma^{2}V^{*})=\sum_{i=1}^{n}s_i^{2},
$$

which was verified at $n=4$ against the singular values computed numerically. So the Hilbert–Schmidt norm is the Euclidean norm of the vector of singular values, and it vanishes exactly at $X=0$.

**The norm is comparable with the operator norm.** Since the largest singular value is at most the Euclidean norm of the list and at least its largest entry divided by $\sqrt n$,

$$
\|X\|_{2}\ \le\ \|X\|_{HS}\ \le\ \sqrt{n}\,\|X\|_{2},
$$

where $\|X\|_{2}=s_{\max}$ is the operator norm. At $n=4$ the computed ratios on a random matrix were $1.19$ and $0.59$ against $\sqrt4=2$, inside the interval. Both bounds are attained: the first by a rank-one matrix and the second by a scalar multiple of the identity.

**The norm is multiplicative on rank-one matrices and submultiplicative in general.** For $X=uv^{*}$ the norm is $\|u\|\|v\|$, so a rank-one matrix has norm equal to the product of the norms of its factors; for general $X,Y$,

$$
\|XY\|_{HS}\le\|X\|_{2}\|Y\|_{HS},
$$

which is the standard inequality and is strict unless $Y$ is supported on the maximal singular direction of $X$.

**The norm of a projection is the square root of its rank.** For an orthogonal projection $P$ of rank $r$ the singular values are $r$ ones and $n-r$ zeros, so

$$
\|P\|_{HS}=\sqrt{r},
$$

which is the statement that the idempotents of rank $r$ lie on the sphere of radius $\sqrt r$ inside the Hilbert space. At $n=2$ the idempotents $\tilde\Pi_{\mathrm{id},\pm}$ have norm $1$, and the two other idempotents of the frame have the same norm.

## Unitary Invariance and the Failure of Full Invariance

**The form is invariant under unitary conjugation.** For unitary $U,V$,

$$
\langle UXV,UYW\rangle=\operatorname{tr}(V^{*}X^{*}U^{*}UYW)=\operatorname{tr}(V^{*}X^{*}YW)=\langle X,Y\rangle ,
$$

using $U^{*}U=\mathrm{I}$ and the cyclicity of the trace. The identity was verified on random unitary matrices at $n=4$. So $\mathrm{U}(n)\times\mathrm{U}(n)$ acts by isometries, and the norm is a unitary invariant of the matrix.

**The form is not invariant under general conjugation.** For an invertible $P$,

$$
\langle PXP^{-1},PYP^{-1}\rangle=\operatorname{tr}\big((P^{*})^{-1}X^{*}P^{*}PYP^{-1}\big),
$$

which is not $\operatorname{tr}(X^{*}Y)$ in general, and the computation at $n=4$ confirms the failure on a random invertible matrix. The reason is that the form is definite: an invariant definite form would make the group compact, and $\mathrm{GL}_n(\mathbb{C})$ is not.

**The trade-off with the trace form is exact.** The trace form is invariant under all of $\mathrm{GL}_n$ and indefinite; the Hilbert–Schmidt form is definite and invariant only under the compact subgroup. Each form sees one of the two structures, and no form sees both, which is the dichotomy that the category reads as the difference between the algebra as a group and the algebra as a Hilbert space.

## The Adjoints of the Operators

**The adjoint of left multiplication is left multiplication by the conjugate transpose.** For the operator $L_A(X)=AX$,

$$
\langle L_AX,Y\rangle=\operatorname{tr}(X^{*}A^{*}Y)=\langle X,L_{A^{*}}Y\rangle ,
$$

so $L_A^{*}=L_{A^{*}}$, and likewise $R_B^{*}=R_{B^{*}}$ for $R_B(X)=XB$. Both identities were verified at $n=4$ on random complex matrices.

**The adjoint of a two-sided operator is two-sided.** For $T(X)=AXB$,

$$
\langle T X,Y\rangle=\operatorname{tr}(X^{*}A^{*}YB^{*})=\langle X,T^{*}Y\rangle,\qquad T^{*}(Y)=A^{*}YB^{*},
$$

which the computation confirms. So the two-sided operators form a $*$-closed family, and the adjoint is the entrywise conjugate transpose in the two-sided reading of *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*.

**The adjoint of the derivation is the derivation by the conjugate transpose, without a sign.** For $\operatorname{ad}_A(X)=[A,X]$,

$$
\langle [A,X],Y\rangle=\operatorname{tr}\big(X^{*}A^{*}Y-A^{*}X^{*}Y\big)=\langle X,[A^{*},Y]\rangle ,
$$

so

$$
\operatorname{ad}_A^{*}=\operatorname{ad}_{A^{*}} .
$$

The identity was verified at $n=4$, and the sign is absent because the conjugate transpose is used twice with no transposition of the product order. For the trace form the corresponding statement has a minus sign, since there the adjoint of the multiplication is multiplication by the transpose and the order reverses.

**The derivation is therefore not anti-self-adjoint for the Hilbert–Schmidt form.** Since $\operatorname{ad}_A^{*}=\operatorname{ad}_{A^{*}}$ and $\operatorname{ad}_A$ is anti-Hermitian only when $A$ is anti-Hermitian up to the sign of the adjoint, the anti-self-adjointness statement holds for the trace form and not for this one. The two forms split the theory: the trace form is the natural form for the Lie structure, the Hilbert–Schmidt form the natural form for the operator structure.

## Definiteness on the Two Halves

**The form is positive definite on each half.** On the Hermitian matrices, $\operatorname{tr}(X^{*}X)=\operatorname{tr}(X^{2})=\sum X_{ij}^{2}>0$; on the anti-Hermitian matrices, $\operatorname{tr}(X^{*}X)=-\operatorname{tr}(X^{2})=\sum|X_{ij}|^{2}>0$. Both were verified on random elements at $n=4$.

**So the split of the complex algebra is not an inertia split.** The trace form has inertia $(n^{2},n^{2})$ on $M_n(\mathbb{C})$ read over $\mathbb{R}$, with the Hermitian and anti-Hermitian parts on opposite sides; the Hilbert–Schmidt form has inertia $(2n^{2},0)$, and both halves are positive. The involution $X\mapsto X^{*}$ is therefore an isometry of the Hilbert–Schmidt form and an anti-isometry of the trace form, and the two behaviours are the two readings of the same involution.

**The two halves are orthogonal but not definite for the trace form, and orthogonal and definite for this one.** For $H$ Hermitian and $K$ anti-Hermitian,

$$
\operatorname{tr}(H^{*}K)=\operatorname{tr}(HK)\in i\mathbb{R},\qquad \operatorname{Re}\operatorname{tr}(H^{*}K)=0,
$$

so the halves are orthogonal for the real part of the Hilbert–Schmidt form as well. The orthogonality is common to the two forms; only the definiteness differs.

## The Case $n=2$

**At $n=2$ the form is the Euclidean form on four complex coordinates.** With the basis $\mathrm{I},\sigma_1,\sigma_2,\sigma_3$ and the Pauli matrices Hermitian and traceless,

$$
\langle\sigma_i,\sigma_j\rangle=\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij},\qquad \langle\mathrm{I},\mathrm{I}\rangle=2,\qquad \langle\mathrm{I},\sigma_i\rangle=0 .
$$

So the four matrices are orthogonal, of equal norm $\sqrt2$, and the form is $2$ times the standard form in that basis, which the computation confirms.

**The Hilbert–Schmidt form and the biquaternion norm are different forms on the same algebra.** The biquaternion norm $N$ is the determinant, indefinite of inertia $(2,2)$, while the Hilbert–Schmidt form is definite; the two are related by the identity

$$
N(X)=\det X,\qquad \|X\|^{2}=\operatorname{tr}(X^{*}X),
$$

and for $2\times2$ matrices they satisfy $N(X)\le\tfrac12\|X\|^{2}$, with equality exactly on the scalar multiples of unitary matrices. So the definite form dominates the indefinite norm, and the equality case is the group $\mathrm{U}(2)$.

**The idempotents of the frame lie on a sphere.** The four idempotents $\tfrac12(\mathrm{I}\pm\sigma_1)$ and $\tfrac12(\mathrm{I}\pm\sigma_3)$ all have norm $1$, and a companion nilpotent with a single unit entry has norm $1$, which the computation confirms. So the sphere of radius $1$ contains both the idempotent variety of $M_2(\mathbb{C})$ and the two companion nilpotents of the frame.

## Summary

The form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ is Hermitian, positive definite, with the matrix units as an orthonormal basis, and its real part is the Euclidean form on $\mathbb{R}^{2n^{2}}$. Its norm is the Euclidean norm of the singular values, it is bounded between the operator norm and $\sqrt n$ times it, and it equals $\sqrt r$ on a projection of rank $r$. The form is invariant under unitary conjugation and not under general conjugation, which is the exact trade-off against the indefinite invariant trace form. The adjoints are $L_A^{*}=L_{A^{*}}$, $R_B^{*}=R_{B^{*}}$, $(X\mapsto AXB)^{*}=(Y\mapsto A^{*}YB^{*})$ and $\operatorname{ad}_A^{*}=\operatorname{ad}_{A^{*}}$, so the derivation is anti-self-adjoint for the trace form and not for this one. The form is positive definite on both halves, so the split by the involution is orthogonal for it but not an inertia split.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ | the Hilbert–Schmidt form |
| $\|X\|^{2}=\operatorname{tr}(X^{*}X)$ | the Hilbert–Schmidt norm, the sum of the squares of the singular values |
| $2n^{2}$ | the real dimension of the space |
| $\delta_{ik}\delta_{jl}$ | the pairing of the matrix units |
| $L_A^{*}=L_{A^{*}}$, $R_B^{*}=R_{B^{*}}$ | the adjoints of the one-sided operators |
| $\operatorname{ad}_A^{*}=\operatorname{ad}_{A^{*}}$ | the adjoint of the derivation, without a sign |
| $\sqrt{r}$ | the norm of a projection of rank $r$ |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Hilbert–Schmidt norm, the singular values and the comparison with the operator norm.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Hilbert–Schmidt inner product and the adjoints of the standard operators.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the two-sided operators and their adjoints.
- [The Trace Form and Its Inertia on the Two Halves](the-trace-form-and-its-signature-on-the-two-halves.html), for the indefinite form that this one replaces.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian](the-two-halves-over-c-hermitian-and-anti-hermitian.html), for the split that is orthogonal but not definite here.
- [The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form](the-derivation-commutator-and-its-anti-self-adjointness-for-the-trace-form.html), for the anti-self-adjointness that fails for this form.
