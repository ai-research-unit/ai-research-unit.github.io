# __The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form__

## Introduction

**The map $\operatorname{ad}_A(X)=[A,X]$ is a derivation of $M_2(\mathbb{C})$ for every $A$, it is anti-self-adjoint for the trace form for every $A$, and it is anti-self-adjoint for the Hilbert–Schmidt form exactly when $A$ is antisymmetric.**

The article proves the Leibniz rule, the representation property $\operatorname{ad}_{[A,B]}=[\operatorname{ad}_A,\operatorname{ad}_B]$, the skewness of $\operatorname{ad}_A$ for the trace form, the formula $\operatorname{ad}_A^{\mathrm{HS}*}=\operatorname{ad}_{A^{\mathsf T}}$, the spectrum of $\operatorname{ad}_A$ as the two differences of the eigenvalues, the identification of the kernel with the centre and the dimension of the space of inner derivations, and the nilpotency of $\operatorname{ad}_A$ for a nilpotent $A$. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* and *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian*.

It defers the Killing form to *The Killing Form of $\mathfrak{sl}_2$ and Its Three Signatures*, the Hilbert–Schmidt form to *The Hilbert–Schmidt Form at $n=2$*, and the operator viewpoint to *The One-Sided Operators at $n=2$*.

## The Commutator Is a Derivation

**Theorem.** For every $A$ the map $\operatorname{ad}_A(X)=[A,X]$ satisfies the Leibniz rule

$$
[A,XY]=[A,X]\,Y+X\,[A,Y].
$$

**Proof.** Expand: $[A,XY]=AXY-XYA$ and the right side is $AXY-XAY+XAY-XYA$, which is the same.

**Corollary.** $\operatorname{ad}_A$ is a derivation of the associative algebra, and it is traceless as an operator on the algebra because its values lie in the traceless subspace.

**Proof.** The Leibniz rule is the derivation property; and $\operatorname{tr}([A,X])=0$ for every $X$, so every value of $\operatorname{ad}_A$ is traceless.

**Corollary.** $\operatorname{ad}_A$ annihilates the identity and preserves the traceless subspace $\mathfrak{sl}_2$.

**Proof.** $[A,I]=0$, and the traceless matrices are exactly the kernel of the trace, which $\operatorname{ad}_A$ respects since its images are traceless.

## The Adjoint Representation

**Theorem.** The map $A\mapsto\operatorname{ad}_A$ is a representation of the Lie algebra $\mathfrak{gl}_2$:

$$
\operatorname{ad}_{[A,B]}=[\operatorname{ad}_A,\operatorname{ad}_B].
$$

**Proof.** Both sides applied to $X$ give $[[A,B],X]$ and $[A,[B,X]]-[B,[A,X]]$, which are equal by the Jacobi identity.

**Corollary.** The map $\operatorname{ad}$ is a homomorphism of Lie algebras with kernel the centre $\mathbb{C}I$, so its image is a Lie algebra of dimension $3$ over $\mathbb{C}$.

**Proof.** $\operatorname{ad}_A=0$ iff $A$ commutes with the whole algebra iff $A$ is scalar; the domain has dimension $4$ and the kernel has dimension $1$.

**The kernel is the centre and nothing else.** At order two the central simple algebra has a one-dimensional centre, so the adjoint representation is faithful exactly on the traceless part.

**Proof.** The scalar matrices commute with everything and no other matrix does, since the algebra is simple.

## Skewness for the Trace Form

**Theorem.** For every $A$ and all $X,Y$,

$$
\operatorname{tr}\bigl([A,X]\,Y\bigr)+\operatorname{tr}\bigl(X\,[A,Y]\bigr)=0 .
$$

**Proof.** $\operatorname{tr}([A,X]Y)=\operatorname{tr}(AXY)-\operatorname{tr}(XAY)=\operatorname{tr}(A[XY])$ using cyclicity, and $\operatorname{tr}(X[A,Y])=\operatorname{tr}(XAY)-\operatorname{tr}(XYA)=-\operatorname{tr}(A[XY])$ by the same cyclicity; the sum vanishes.

**Corollary.** Every $\operatorname{ad}_A$ is anti-self-adjoint for the trace form, so the image of $\operatorname{ad}$ lies in the Lie algebra of the orthogonal group of the trace form, which is $\mathfrak{so}(3,1)$.

**Proof.** The skewness is the theorem, and the Lie algebra of the orthogonal group of a form of signature $(3,1)$ is the set of anti-self-adjoint endomorphisms.

**The trace form cannot detect the skewness condition.** Here the freedom is total: no hypothesis on $A$ is needed, because the trace is invariant under the cyclic permutation of three factors, and the invariance is what produces the skewness.

**Proof.** The proof above uses only cyclicity, with no symmetry of $A$.

## Skewness for the Hilbert–Schmidt Form

**Theorem.** For the Hilbert–Schmidt form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ the adjoint of $\operatorname{ad}_A$ is $\operatorname{ad}_{A^{\mathsf T}}$.

**Proof.** $\langle[A,X],Y\rangle=\operatorname{tr}((AX-XA)^{*}Y)=\operatorname{tr}(X^{*}A^{*}Y)-\operatorname{tr}(A^{*}X^{*}Y)$ and $\langle X,[A^{\mathsf T},Y]\rangle=\operatorname{tr}(X^{*}A^{\mathsf T}Y)-\operatorname{tr}(X^{*}YA^{\mathsf T})$; the two agree after cyclicity.

**Corollary.** $\operatorname{ad}_A$ is anti-self-adjoint for the Hilbert–Schmidt form exactly when $A$ is antisymmetric, and it is self-adjoint exactly when $A$ is symmetric.

**Proof.** $\operatorname{ad}_{A^{\mathsf T}}=-\operatorname{ad}_A$ iff $A^{\mathsf T}=-A$, since $\operatorname{ad}$ is injective on the traceless part and the antisymmetric matrices are traceless.

**The two forms divide the algebra.** The trace form sees every derivation as antisymmetric, while the Hilbert–Schmidt form separates the symmetric directions, where the derivation is self-adjoint, from the antisymmetric direction, where it is antisymmetric.

## The Spectrum of $\operatorname{ad}_A$

**Theorem.** If $A$ has eigenvalues $\lambda_{1},\lambda_{2}$ then $\operatorname{ad}_A$ has eigenvalues $0,0,\lambda_{1}-\lambda_{2},\lambda_{2}-\lambda_{1}$, with the two zeros on the eigen-directions $E_{11}$ and $E_{22}$.

**Proof.** In the basis of matrix units, $\operatorname{ad}_A(E_{ij})=(\lambda_{i}-\lambda_{j})E_{ij}$, so the four eigenvalues are the four differences, two of which vanish on the diagonal units.

**Corollary.** The trace of $\operatorname{ad}_A$ is zero and the determinant of $\operatorname{ad}_A$ is zero, and the rank of $\operatorname{ad}_A$ is $2$ when the two eigenvalues differ and $0$ when they coincide.

**Proof.** The four eigenvalues sum to zero and contain two zeros; the rank is the number of nonzero eigenvalues.

**Corollary.** The spectrum of $\operatorname{ad}_A$ is real for every complex matrix $A$ whose eigenvalues are real, and it is purely imaginary for an anti-Hermitian $A$ with imaginary eigenvalues.

**Proof.** The differences of two real numbers are real, and the differences of two purely imaginary numbers are purely imaginary.

## The Kernel and the Inner Derivations

**Theorem.** Every derivation of $M_2(\mathbb{C})$ is inner, and the space of derivations is $\mathfrak{sl}_2(\mathbb{C})$, of dimension $3$.

**Proof.** The algebra is central simple, so every derivation is of the form $\operatorname{ad}_A$; the kernel of $\operatorname{ad}$ is the centre, so the space of derivations is the quotient by the scalars, which is $\mathfrak{sl}_2$.

**Corollary.** The commutator subspace of $M_2(\mathbb{C})$ is $\mathfrak{sl}_2(\mathbb{C})$, of dimension $3$, and the commutator of two matrix units is another matrix unit or zero.

**Proof.** The commutators span the traceless part, and $[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj}$.

**The derivations of the two halves.** A derivation that preserves the symmetric half is the restriction of some $\operatorname{ad}_A$ with $A$ antisymmetric, and at order two that space is one-dimensional.

**Proof.** The antisymmetric matrices form the line $\mathbb{R}J$, and $\operatorname{ad}_J$ is the single derivation of the symmetric half into itself up to scale.

## The Nilpotent Case

**Theorem.** If $A$ is nilpotent then $\operatorname{ad}_A$ is nilpotent, and at order two its index is $3$.

**Proof.** For $A=E_{12}$ the eigenvalues of $A$ coincide, so all four eigenvalues of $\operatorname{ad}_A$ vanish; a direct computation gives $\operatorname{ad}_{E_{12}}^{2}\neq0$ and $\operatorname{ad}_{E_{12}}^{3}=0$.

**Corollary.** The derivation attached to a nilpotent element lies in the nilpotent cone of $\mathfrak{gl}(\mathfrak{gl}_2)$, and its powers cut the algebra into the filtration of the associated graded space.

**Proof.** The vanishing of the cube is the statement, and the filtration by the kernels of the powers is the standard one.

**The matrix of $\operatorname{ad}_{E_{12}}$.** In the basis $I,\sigma_{3},\sigma_{1},J$ the operator is

$$
\operatorname{ad}_{E_{12}}=\begin{pmatrix}0&0&0&0\\ 0&0&1&-1\\ 0&-1&0&0\\ 0&-1&0&0\end{pmatrix}.
$$

**Proof.** The columns are the coordinates of the images of the four basis elements, computed with $E_{12}I-IE_{12}=E_{12}$ and $E_{12}J-JE_{12}=-\sigma_{3}$.

**Corollary.** The image of $\operatorname{ad}_{E_{12}}$ is two-dimensional, spanned by $\sigma_{3}$ and $\sigma_{1}+J$, and its kernel is the same span together with $I$.

**Proof.** Read the column space and the null space of the displayed matrix.

## Summary

$\operatorname{ad}_A(X)=[A,X]$ is a derivation for every $A$, the map $A\mapsto\operatorname{ad}_A$ is a representation of $\mathfrak{gl}_2$ with kernel the scalars, and every derivation of $M_2(\mathbb{C})$ is inner, so the derivations form $\mathfrak{sl}_2(\mathbb{C})$ of dimension $3$.

For the trace form every $\operatorname{ad}_A$ is anti-Hermitian, with no condition on $A$, while for the Hilbert–Schmidt form the adjoint is $\operatorname{ad}_{A^{\mathsf T}}$, which makes the derivation anti-self-adjoint for antisymmetric $A$ and self-adjoint for symmetric $A$. The spectrum of $\operatorname{ad}_A$ is $0,0,\pm(\lambda_{1}-\lambda_{2})$, and for a nilpotent element the derivation is nilpotent of index $3$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_A$ | the derivation $X\mapsto[A,X]$ |
| $[A,B]$ | the commutator $AB-BA$ |
| $\operatorname{tr}(X^{*}Y)$ | the Hilbert–Schmidt form |
| $\operatorname{ad}_A^{\mathrm{HS}*}$ | the adjoint for the Hilbert–Schmidt form |
| $\mathfrak{sl}_2$ | the traceless matrices, the space of derivations |
| $E_{ij}$ | the matrix units |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for inner derivations of central simple algebras and the Jacobi identity.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the adjoint representation and the Killing form.
- [The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian](the-lie-algebra-skew-2-one-dimension-hence-abelian.html), for the antisymmetric line on which the derivation is antisymmetric.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the splitting that the two forms detect.
- [The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$](the-four-multiplication-tables-ss-sk-ks-kk-at-n-2.html), for the products used in the computation of the matrix of $\operatorname{ad}_{E_{12}}$.
