# __The Trace Form and Its Signature on the Two Halves__

## Introduction

**The form $\langle X,Y\rangle=\operatorname{tr}(XY)$ is symmetric, nondegenerate and invariant under conjugation, and its signature on $M_n(\mathbb{R})$ is $(n(n+1)/2,\,n(n-1)/2)$, split exactly along the two halves: positive definite on $\operatorname{Sym}_n$ and negative definite on $\operatorname{Skew}_n$.**

The article proves the invariance, computes the Gram matrix in the matrix units and its eigenvalues, derives the signature of the whole algebra, of each half, of the traceless part and of the complex algebra read over $\mathbb{R}$, and identifies the form as the real part of the Hermitian form that becomes the Hilbert–Schmidt form. It assumes *The Two Halves as Orthogonal Complements* for the orthogonality of the split and *The Jordan Algebra $\operatorname{Sym}_n$* for the positive definiteness on the symmetric half. It defers the Hermitian form itself to *The Hilbert–Schmidt Form* and the Killing form to *The Killing Form, Its Radical and the Triangular Case*.

## The Form and Its Invariance

**The trace form is symmetric and nondegenerate.** Put

$$
\langle X,Y\rangle=\operatorname{tr}(XY)\qquad(X,Y\in M_n(\mathbb{R})).
$$

It is bilinear and symmetric by the cyclicity of the trace. It is nondegenerate, since $\langle X,E_{ij}\rangle=X_{ji}$: if the form vanishes against every unit then every entry of $X$ is zero. So the form identifies the algebra with its dual, and it is the pairing used throughout the category.

**The form is invariant under conjugation by any invertible matrix.** For $P\in\mathrm{GL}_n(\mathbb{R})$,

$$
\langle PXP^{-1},PYP^{-1}\rangle=\operatorname{tr}(PXY P^{-1})=\operatorname{tr}(XY)=\langle X,Y\rangle .
$$

So $\mathrm{GL}_n(\mathbb{R})$ acts by isometries of the form, and the form is the invariant bilinear form of the algebra. The invariance is the reason the form is compatible with the derivation $\operatorname{ad}_A$, which is anti-self-adjoint for it by *The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form*.

**The invariance does not make the form definite, and that is the point of the indefinite signature.** An invariant form on a non-compact group cannot be definite, and $\mathrm{GL}_n(\mathbb{R})$ is non-compact; the signature computed below is the exact measure of the failure. The form is positive on the symmetric half precisely because the symmetric half is not a Lie subalgebra but a space of stretches.

**The form is the trace form of the algebra in the sense of the associative theory.** It satisfies $\langle XY,Z\rangle=\langle X,YZ\rangle$, which was verified on random triples at $n=2,3,4$, and that associativity is what makes the projections onto the two halves self-adjoint for it.

## The Signature on the Whole Algebra

**In the matrix units the Gram matrix is the transposition permutation.** Since

$$
\langle E_{ij},E_{kl}\rangle=\delta_{jk}\delta_{il},
$$

the Gram matrix in the $n^{2}$ units is the permutation matrix of the swap $(i,j)\leftrightarrow(j,i)$. That permutation has $n^{2}-n$ two-cycles and $n$ fixed points, so its eigenvalues are $+1$ with multiplicity

$$
n+\frac{n^{2}-n}{2}=\frac{n(n+1)}{2}
$$

and $-1$ with multiplicity $n(n-1)/2$. Hence the signature of the trace form on $M_n(\mathbb{R})$ is

$$
\big(\operatorname{sig}\big)=(n(n+1)/2,\ n(n-1)/2\big)= (3,1),\ (6,3),\ (10,6),\ (15,10)\quad(n=2,3,4,5),
$$

which was checked by the eigenvalues of the Gram matrix at those orders.

**An explicit orthonormal basis diagonalises the form.** The units $E_{ii}$ and the normalised sums $\tfrac{1}{\sqrt2}(E_{ij}+E_{ji})$ for $i<j$ are positive vectors, and the normalised differences $\tfrac{1}{\sqrt2}(E_{ij}-E_{ji})$ are negative vectors:

$$
\Big\langle \tfrac{E_{ij}+E_{ji}}{\sqrt2},\tfrac{E_{ij}+E_{ji}}{\sqrt2}\Big\rangle=1,\qquad
\Big\langle \tfrac{E_{ij}-E_{ji}}{\sqrt2},\tfrac{E_{ij}-E_{ji}}{\sqrt2}\Big\rangle=-1 .
$$

The two families are exactly the two halves in an orthonormal frame, which is the content of *The Two Halves as Orthogonal Complements* read with normalisations.

**The form is the real part of a Hermitian form.** On $M_n(\mathbb{C})$ the form $\operatorname{tr}(X^{*}Y)$ is Hermitian and positive definite, and its real part restricts on the real matrices to $\operatorname{tr}(X^{\mathsf T}Y)=\operatorname{tr}(XY)$. So the trace form is the real part of the Hilbert–Schmidt form, and its indefiniteness is the statement that the real structure is not the one the Hermitian form prefers.

## The Two Halves

**The symmetric half is positive definite.** For $X\in\operatorname{Sym}_n$,

$$
\langle X,X\rangle=\operatorname{tr}(X^{2})=\sum_{i,j}X_{ij}^{2}>0\qquad(X\neq0),
$$

so the form restricts to an inner product on the half, of rank $n(n+1)/2$. The positive part of the signature is therefore carried entirely by $\operatorname{Sym}_n$, and the computation of the Gram matrix on the basis $E_{ii}$, $\tfrac{1}{\sqrt2}(E_{ij}+E_{ji})$ gives the identity matrix of that size.

**The antisymmetric half is negative definite.** For $K\in\operatorname{Skew}_n$,

$$
\langle K,K\rangle=\operatorname{tr}(K^{2})=-\operatorname{tr}(KK^{\mathsf T})=-\sum_{i,j}K_{ij}^{2}<0\qquad(K\neq0),
$$

so the form is negative definite there, of rank $n(n-1)/2$. The negative part of the signature is carried entirely by $\operatorname{Skew}_n$.

**The two halves are orthogonal, so the signature is the sum of the two.** For $S$ symmetric and $K$ antisymmetric,

$$
\langle S,K\rangle=\operatorname{tr}(SK)=0,
$$

which was verified on random elements at $n=2,3,4$. So the orthogonal decomposition

$$
M_n(\mathbb{R})=\operatorname{Sym}_n\perp\operatorname{Skew}_n
$$

is a decomposition into a positive definite and a negative definite subspace, and the signature theorem for a direct orthogonal sum gives

$$
\operatorname{sig}\big(M_n(\mathbb{R})\big)=\Big(\frac{n(n+1)}{2},0\Big)+\Big(0,\frac{n(n-1)}{2}\Big).
$$

**The form is therefore the model of an indefinite form split by an involution.** Any involution $\theta$ preserving a form with $\theta^{2}=1$ splits the space into the fixed and the anti-fixed parts, and the form is definite on each; the trace form with the transpose is the matrix case, and the general statement is the lemma of *The Two Halves as Orthogonal Complements*.

## The Traceless Part

**On the traceless subspace the signature loses one positive direction.** The line $\mathbb{R}\mathrm{I}$ is positive and orthogonal to $\mathfrak{sl}_n(\mathbb{R})$, since $\langle \mathrm{I},X\rangle=\operatorname{tr}(X)=0$. Hence

$$
\operatorname{sig}\big(\mathfrak{sl}_n(\mathbb{R})\big)=\Big(\frac{n(n+1)}{2}-1,\ \frac{n(n-1)}{2}\Big)=(2,1),\ (5,3),\ (9,6)\quad(n=2,3,4),
$$

which was checked from the Gram matrix in the basis $E_{ij}-\tfrac1n\delta_{ij}\mathrm{I}$.

**The traceless part splits as symmetric traceless plus antisymmetric.** The traceless symmetric matrices have dimension $n(n+1)/2-1$ and the antisymmetric ones $n(n-1)/2$, and they add to $n^{2}-1$. So the same split occurs inside the traceless part, and the form is the direct sum of a positive definite inner product on the traceless symmetric matrices and a negative definite form on the antisymmetric ones.

**The form is definite on each half of the traceless part and indefinite on the whole.** The two statements are consistent because the split is orthogonal: indefiniteness on a sum of two definite pieces of opposite signs is automatic, and the signature counts the two signs separately.

## The Complex Case and the Hermitian Form

**Read over $\mathbb{R}$, the complex algebra has signature $(n^{2},n^{2})$.** With $\operatorname{Re}\operatorname{tr}(XY)$ and the real basis $E_{ij},iE_{ij}$, the Gram matrix has eigenvalues

$$
+1,\ +1,\ -1,\ -1\ \text{per pair }(i,j),
$$

so the positive and negative multiplicities are equal, $n^{2}$ each, and the signature is $(n^{2},n^{2})=(4,4),(9,9)$ at $n=2,3$, which was checked from the Gram matrix.

**The isotropic directions are the complex structures.** Every complex matrix $X$ gives an isotropic pair $X$ and $iX$, since $\operatorname{Re}\operatorname{tr}(X\cdot iX)=0$ and both are isotropic when $X$ is nilpotent in the appropriate sense. So the real form on the complex algebra has a large isotropic subspace, of dimension $n^{2}$, and the real structure of $\mathbb{C}$ is what produces it.

**The Hermitian form is definite, and it is the form that the two halves split into Hermitian and anti-Hermitian.** The positive definite form $\operatorname{tr}(X^{*}Y)$ has no negative direction, and the involution $X\mapsto X^{*}$ splits the complex algebra into the Hermitian and the anti-Hermitian parts, on which the form is respectively positive and negative. So the two pictures agree: the real case of the trace form is the real part of the Hermitian case, and the split by the involution is the same split in both.

## The Case $n=2$

**At $n=2$ the signature is $(3,1)$ and the form is the Lorentz form of the biquaternion algebra.** In the basis $\mathrm{I},\sigma_1,\sigma_3,J$,

$$
\langle\mathrm{I},\mathrm{I}\rangle=\langle\sigma_1,\sigma_1\rangle=\langle\sigma_3,\sigma_3\rangle=2,\qquad \langle J,J\rangle=-2,
$$

and all other pairings vanish, so the Gram matrix is $2$ times the Lorentz form $\operatorname{diag}(1,1,1,-1)$. The computation confirms the diagonal form and the value $-2$ on $J$.

**The signature $(3,1)$ and the biquaternion norm are two readings of one form.** The biquaternion norm $N$ is indefinite of signature $(2,2)$ over $\mathbb{R}$ on the four real coordinates of $\mathbb{B}$, and the trace form on the same four coordinates has signature $(3,1)$; the two differ by the choice of real structure, since the norm is the determinant and the trace form is the trace of the product. On the symmetric half the trace form is positive definite of signature $(3,0)$, and the negative direction is the whole of the antisymmetric half.

**The two halves at $n=2$ are a time direction and a space direction.** The symmetric half is the three-dimensional positive space and the antisymmetric half the line of negative type, so the split is the split of Minkowski space into space and time. The idempotents $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ are positive vectors of norm $1$, since $\operatorname{tr}(\tilde\Pi_\pm^{2})=\operatorname{tr}(\tilde\Pi_\pm)=1$, and the rotation direction $J$ is the negative vector, which is the Lorentz picture of *Coda: $n=2$ and the Biquaternion Algebra*.

## Summary

The form $\langle X,Y\rangle=\operatorname{tr}(XY)$ is symmetric, nondegenerate and invariant under conjugation, with $\langle E_{ij},E_{kl}\rangle=\delta_{jk}\delta_{il}$, so its Gram matrix is the transposition permutation. Its signature on $M_n(\mathbb{R})$ is $(n(n+1)/2,n(n-1)/2)$, positive definite on the symmetric half and negative definite on the antisymmetric half, with the two halves orthogonal. On the traceless part the signature is $(n(n+1)/2-1,n(n-1)/2)$, and on the complex algebra read over $\mathbb{R}$ it is $(n^{2},n^{2})$. At $n=2$ the form is the Lorentz form of signature $(3,1)$, which is the trace-form shadow of the indefinite biquaternion norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace form |
| $\delta_{jk}\delta_{il}$ | the value on the matrix units, giving the transposition permutation as Gram matrix |
| $(n(n+1)/2,\,n(n-1)/2)$ | the signature on $M_n(\mathbb{R})$ |
| $\operatorname{sig}(\operatorname{Sym}_n)=(n(n+1)/2,0)$ | positive definiteness on the symmetric half |
| $\operatorname{sig}(\operatorname{Skew}_n)=(0,n(n-1)/2)$ | negative definiteness on the antisymmetric half |
| $(n^{2},n^{2})$ | the signature of $\operatorname{Re}\operatorname{tr}(XY)$ on $M_n(\mathbb{C})$ over $\mathbb{R}$ |
| $\operatorname{diag}(1,1,1,-1)$ | the Lorentz form at $n=2$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the trace form, the matrix units and the inertia of a symmetric form.
- Werner Greub, *Linear Algebra* (Springer, 1975), for the signature of a symmetric bilinear form and orthogonal direct sums.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the associative trace form and its nondegeneracy.
- [The Two Halves as Orthogonal Complements](the-two-halves-as-orthogonal-complements.html), for the orthogonality of the split that the signature follows.
- [The Jordan Algebra $\operatorname{Sym}_n$](the-jordan-algebra-sym-n.html), for the positive definiteness on the symmetric half.
- [The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form](the-derivation-commutator-and-its-anti-self-adjointness-for-the-trace-form.html), for the invariance that makes every derivation anti-Hermitian.
