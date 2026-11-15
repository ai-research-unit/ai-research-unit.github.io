# __The One-Sided Operators at $n=2$__

## Introduction

**The left multiplication $L_{X}:Z\mapsto XZ$ is an operator of rank twice the rank of $X$, with the eigenvalues of $X$ each repeated twice, and its image is the set of matrices whose columns lie in the image of $X$; the right multiplications are the mirror image.**

The article studies the two one-sided families of operators on the matrix space, computes their rank, kernel, spectrum and adjoint, identifies the images of the rank-one elements as the minimal left ideals, and shows how the two families sit inside the endomorphism algebra. It assumes *$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation*, *The Minimal Left Ideals of the Biquaternion Algebra* and *The Hilbert–Schmidt Form at $n=2$*.

It follows the biquaternion article *The Endomorphisms of the Biquaternion Algebra* for the same operators on the eight real coordinates.

## The Left Regular Representation

**The map $X\mapsto L_{X}$ is an injective algebra homomorphism, so the matrix algebra acts on itself by left multiplication.**

**Proposition.** The map $X\mapsto L_{X}$ is a homomorphism of algebras and its kernel is zero, so the left multiplications form a copy of $M_2(\mathbb{C})$.

**Proof.** $L_{X}L_{X'}=L_{XX'}$ by associativity, and $L_{X}=0$ forces $X=L_{X}I=0$.

**Corollary.** The eight real dimensions of the matrix algebra sit inside the thirty-two real dimensions of the endomorphism algebra as the left multiplications.

**Proof.** The copy is a real subspace of dimension eight.

**Corollary.** The left multiplication by the identity is the identity operator, and the left multiplication by a scalar is the scalar operator.

**Proof.** Both statements are immediate from the definition.

## Rank and Kernel

**Theorem.** For a matrix $X$ of rank $r$ the operator $L_{X}$ has rank $2r$ over $\mathbb{C}$ and kernel of dimension $4-2r$.

**Proof.** The image of $L_{X}$ is the set of matrices $XZ$ with $Z$ arbitrary; the columns of $XZ$ are the images under $X$ of the columns of $Z$, so the image consists exactly of the matrices whose columns lie in $\operatorname{im}X$, a space of dimension $2r$. The rank-nullity theorem then gives the kernel dimension.

**Corollary.** The operator $L_{X}$ is invertible exactly when $X$ is invertible, and its kernel is the set of matrices whose columns lie in the kernel of $X$.

**Proof.** The rank is the full four exactly when $r=2$; and $XZ=0$ means that each column of $Z$ is annihilated by $X$.

**Corollary.** For a rank-one matrix the operator $L_{X}$ has rank two, so its image is a minimal left ideal of the algebra.

**Proof.** The image is a two-dimensional left ideal, and the minimal left ideals are exactly the two-dimensional left ideals.

## The Spectrum

**Proposition.** The eigenvalues of $L_{X}$ are the eigenvalues of $X$, each with multiplicity two; in particular the trace of $L_{X}$ is twice the trace of $X$.

**Proof.** The operator $L_{X}$ is the tensor product of $X$ with the identity on the two-dimensional column space, so every eigenvalue of $X$ occurs once for each basis vector of that space.

**Corollary.** The determinant of $L_{X}$ is the square of the determinant of $X$, and the operator is singular exactly when $X$ is.

**Proof.** The product of the eigenvalues with multiplicity is the square of the product of the eigenvalues of $X$.

**Corollary.** A left multiplication is diagonalisable exactly when $X$ is, and it is nilpotent exactly when $X$ is.

**Proof.** The Jordan form of a tensor product with the identity repeats the Jordan blocks of $X$.

## The Right Multiplications

**Proposition.** The right multiplication $R_{Y}$ has rank $2\operatorname{rank}Y$, kernel the matrices whose rows are annihilated by $Y$, and the eigenvalues of $Y$ each twice.

**Proof.** The image consists of the matrices $ZY$, whose rows are linear combinations of the rows of $Y$; the same computation as for the left family applies with the two factors interchanged.

**Corollary.** The right multiplication is the transpose of the left multiplication under the identification of a matrix with its transpose, so the two families have the same rank and spectrum.

**Proof.** $R_{Y}(Z)^{\mathsf T}=Y^{\mathsf T}Z^{\mathsf T}$, which is the left multiplication by $Y^{\mathsf T}$ applied to the transpose.

**Corollary.** The two families have the same singular values, and the same minimal left and right ideals up to transposition.

**Proof.** Transposition is an isometry for the Hilbert–Schmidt form and exchanges left and right.

## The Adjoints

**Proposition.** The adjoint of $L_{X}$ for the Hilbert–Schmidt form is $L_{X^{*}}$, and the adjoint of $R_{Y}$ is $R_{Y^{*}}$.

**Proof.** $\langle L_{X}Z,W\rangle=\operatorname{tr}((XZ)^{*}W)=\operatorname{tr}(Z^{*}X^{*}W)=\langle Z,L_{X^{*}}W\rangle$.

**Corollary.** A left multiplication is self-adjoint exactly when $X$ is Hermitian, and unitary exactly when $X$ is unitary.

**Proof.** The adjoint is the left multiplication by the conjugate transpose, and the identity of the two operators is the identity of the parameters.

**Corollary.** The Hilbert–Schmidt norm of $L_{X}$ is $\sqrt2$ times the Hilbert–Schmidt norm of $X$.

**Proof.** The squared norm of $L_{X}$ is the sum of the squared norms of the images of the four matrix units, and the image of a matrix unit is the corresponding column of $X$, so each column is counted twice.

**Corollary.** The left multiplications by Hermitian matrices form a real subspace of dimension four inside the self-adjoint operators, and the left multiplications by skew-Hermitian matrices form the corresponding skew subspace.

**Proof.** The four real dimensions of the Hermitian half carry over to the four real dimensions of the subspace of self-adjoint one-sided operators.

## Where the Two Families Meet

**Proposition.** The left multiplication by $X$ equals the right multiplication by $X$ exactly when $X$ is a scalar.

**Proof.** The identity $XZ=ZX$ for every $Z$ is the statement that $X$ is in the centre, and the centre of the algebra is the scalars.

**Corollary.** The intersection of the two copies is the two real dimensions of the scalars, and the sum of the two copies has real dimension fourteen.

**Proof.** The intersection is the scalars, and the dimensions add with the intersection subtracted: eight plus eight minus two.

**Corollary.** The product $L_{X}R_{Y}$ is the operator $Z\mapsto XZY$, and its rank is at most twice the smaller of the two ranks.

**Proof.** The image is contained in the set of matrices whose columns lie in the image of $X$, which has dimension at most $2\operatorname{rank}X$; and symmetrically for the rows and $Y$.

## The One-Sided Ideals

**Proposition.** The image of $L_{X}$ is a left ideal of the algebra, and it is the left ideal generated by the columns of $X$.

**Proof.** For any $A$ the matrix $A(XZ)=(AX)Z$ is again in the image, so the image is closed under left multiplication by the algebra.

**Corollary.** The images of the rank-one elements are exactly the minimal left ideals, and they are parametrised by the lines of the plane.

**Proof.** The image of a rank-one element is the set of matrices with columns in a fixed line, which is a minimal left ideal, and the line is the parameter.

**Corollary.** The algebra is the direct sum of any two minimal left ideals carried by independent lines, so the four complex dimensions split into two halves of dimension two.

**Proof.** Choosing two independent lines gives two minimal left ideals whose intersection is zero, and their dimensions add to four.

## Summary

The left multiplication by $X$ is an operator of rank twice the rank of $X$, with the eigenvalues of $X$ repeated twice, kernel the matrices whose columns lie in the kernel of $X$, and image the matrices whose columns lie in the image of $X$. Its adjoint for the Hilbert–Schmidt form is the left multiplication by $X^{*}$.

The right multiplications are the transposed mirror of the left ones, with the same rank, spectrum and singular values. The images of the rank-one elements are the minimal left ideals, parametrised by the lines of the plane, and two independent lines split the algebra into two halves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{X}$ | the left multiplication $Z\mapsto XZ$ |
| $R_{Y}$ | the right multiplication $Z\mapsto ZY$ |
| $\operatorname{rank}X$ | the rank of the matrix |
| $X^{*}$ | the conjugate transpose |
| $\langle,\rangle$ | the Hilbert–Schmidt form |

## Further Reading

- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for one-sided multiplication operators.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for ranks and spectra of tensor products.
- [$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m2c-as-an-algebra-the-regular-representation.html), for the ambient algebra of the operators.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the ideals that appear as images.
- [The Hilbert–Schmidt Form at $n=2$](the-hilbert-schmidt-form-at-n-2.html), for the form used to take adjoints.
