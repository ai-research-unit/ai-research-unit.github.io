# __The Adjoints and the Polar Decomposition of an Operator at $n=2$__

## Introduction

**The endomorphism algebra of the matrix space is a Hilbert space of real dimension thirty-two, each operator has an adjoint, and every invertible operator is the product of a unitary operator with a positive operator, by the same theorem that gives the polar decomposition of a matrix.**

The article computes adjoints of operators, identifies the self-adjoint, the unitary and the positive operators, proves the polar decomposition inside the endomorphism algebra, applies it to the one-sided and the two-sided families, and computes the positive part of a two-sided operator in terms of its two parameters. It assumes *The Length and the Two Ranks at $n=2$*, *The Polar Decomposition from the Two Halves at $n=2$* and *The Hilbert–Schmidt Form at $n=2$*.

It follows the biquaternion article *The Endomorphisms of the Biquaternion Algebra* for the same adjoints on the eight real coordinates.

## The Adjoint of an Operator

**The Hilbert–Schmidt form gives every operator an adjoint, and the adjoint is the conjugate transpose in the basis of matrix units.**

**Definition.** The adjoint $T^{*}$ of an operator $T$ is the unique operator with $\langle TZ,W\rangle=\langle Z,T^{*}W\rangle$ for all $Z,W$.

**Proposition.** The adjoint is conjugate-linear, involutive and reversing: $(T^{*})^{*}=T$ and $(TS)^{*}=S^{*}T^{*}$.

**Proof.** The form is linear in the second argument and conjugate-linear in the first, and the two identities are checked by moving the form from one side to the other twice.

**Corollary.** In the basis of matrix units the adjoint of an operator is the conjugate transpose of its matrix.

**Proof.** The Hilbert–Schmidt form is the standard Hermitian form on the four complex coordinates, whose adjoint is the conjugate transpose.

**Corollary.** The trace of an operator is the trace of its adjoint up to conjugation, and the length of an operator equals the length of its adjoint.

**Proof.** The trace of $T^{*}$ is the conjugate of the trace of $T$, and the squared lengths of the two agree.

## The Adjoints of the Two Families

**Proposition.** The adjoint of $L_{X}$ is $L_{X^{*}}$ and the adjoint of $T_{X,Y}$ is $T_{X^{*},Y^{*}}$.

**Proof.** The first was computed in *The One-Sided Operators at $n=2$*; for the second, $\langle XZY,W\rangle=\operatorname{tr}(Y^{*}Z^{*}X^{*}W)=\langle Z,X^{*}WY^{*}\rangle$.

**Corollary.** A two-sided operator is self-adjoint exactly when both parameters are Hermitian.

**Proof.** The adjoint is the two-sided operator with the conjugate transposed parameters, and the two operators agree exactly when both parameters are Hermitian.

**Corollary.** A two-sided operator is unitary exactly when both of its parameters are unitary.

**Proof.** The composition $T_{X,Y}^{*}T_{X,Y}=T_{X^{*}X,YY^{*}}$ is the identity exactly when both of its parameters are the identity, since a two-sided operator is the identity exactly when both parameters are.

## The Special Operators

**Proposition.** The self-adjoint operators of the matrix space form a real subspace of dimension sixteen, the unitary operators form a group of real dimension sixteen, and the positive operators form a cone inside the self-adjoint space.

**Proof.** The self-adjoint operators are the Hermitian matrices of the four-dimensional complex space, a real space of dimension sixteen; the unitary operators are the unitary matrices of that space, a group of real dimension sixteen; and the positive operators are the positive definite Hermitian matrices of the same space, an open cone.

**Corollary.** The self-adjoint operators of the one-sided family are exactly the left multiplications by Hermitian matrices, a subspace of real dimension four.

**Proof.** The left multiplication is self-adjoint exactly when its parameter is Hermitian, and the Hermitian half has dimension four.

**Corollary.** The unitary operators of the one-sided family are exactly the left multiplications by unitary matrices, and they form a group of real dimension four.

**Proof.** The left multiplication is unitary exactly when its parameter is unitary, and the unitary group at order two has real dimension four.

## The Polar Decomposition of an Operator

**Theorem.** Every invertible operator $T$ of the matrix space is uniquely $T=UP$ with $U$ unitary and $P$ positive definite self-adjoint.

**Proof.** This is *The Polar Decomposition from the Two Halves at $n=2$* applied to the four-dimensional complex space of matrices, with the Hilbert–Schmidt form as the Hermitian form.

**Corollary.** The endomorphism algebra is the product of its unitary group with its positive cone, and the product map is a diffeomorphism.

**Proof.** The decomposition is unique and continuous in both directions.

**Corollary.** The positive part is the square root of $T^{*}T$ and its eigenvalues are the singular values of $T$.

**Proof.** The construction of the matrix case applies verbatim, and the singular values of an operator are the eigenvalues of its positive part.

## The Positive Part of a Two-Sided Operator

**Proposition.** For a two-sided operator with invertible parameters the operator $T^{*}T$ is the two-sided operator $T_{X^{*}X,Y Y^{*}}$.

**Proof.** The adjoint of $T_{X,Y}$ is $T_{X^{*},Y^{*}}$, and the composition gives the two-sided operator with the two products on the two sides.

**Corollary.** The positive part of an invertible two-sided operator is $T_{|X|,|Y^{*}|}$, with $|X|=(X^{*}X)^{1/2}$ and $|Y^{*}|=(YY^{*})^{1/2}$.

**Proof.** The square root of a two-sided operator with one parameter on each side is computed on each side, and the square roots of $X^{*}X$ and of $YY^{*}$ are the two absolute values.

**Corollary.** The unitary part of an invertible two-sided operator is $T_{X|X|^{-1},\,|Y^{*}|^{-1}Y}$, whose two parameters are the unitary factors of the polar decompositions of $X$ and of $Y$.

**Proof.** Multiplying the operator by the inverse of its positive part gives the stated two-sided operator, and each parameter of that operator is unitary because it is the unitary factor of a polar decomposition.

## The Geometry of the Decomposition

**Proposition.** The polar decomposition of an operator separates the rotation of the matrix space from its stretching, and the stretching is measured on the four singular values.

**Proof.** The unitary factor preserves the length of every matrix, and the positive factor multiplies the length along four orthogonal directions by the four singular values.

**Corollary.** The volume distortion of an operator is the product of its four singular values, which is the absolute value of its determinant.

**Proof.** The determinant is the product of the eigenvalues, and the absolute value of the determinant is the product of the singular values.

**Corollary.** An operator preserves the Hilbert–Schmidt length exactly when its positive part is the identity, which is the case of the unitary operators.

**Proof.** The positive part is the identity exactly when all the singular values are one.

**Corollary.** The condition number of an operator is the ratio of its largest to its smallest singular value, and it is one exactly for the unitary operators up to a scalar.

**Proof.** The ratio is computed from the eigenvalues of the positive part, and it equals one exactly when they are all equal; the positive part is then a scalar multiple of the identity, and the operator is a scalar multiple of a unitary one.

## Summary

Every operator of the matrix space has an adjoint, which is the conjugate transpose in the basis of matrix units and is computed on the two parameters of a two-sided operator by conjugating and transposing each of them. The self-adjoint operators form a real space of dimension sixteen, the unitary group has real dimension sixteen, and the positive operators form a cone inside the self-adjoint space.

Every invertible operator is uniquely the product of a unitary operator with a positive operator, and the positive part is the square root of $T^{*}T$ with the singular values on its diagonal. For a two-sided operator the positive part is read from the two products $X^{*}X$ and $YY^{*}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{*}$ | the adjoint for the Hilbert–Schmidt form |
| $T=UP$ | the polar decomposition of an operator |
| $P=(T^{*}T)^{1/2}$ | the positive part |
| $U$ | the unitary part |
| $|X|$ | the positive square root of $X^{*}X$ |

## Further Reading

- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for adjoints and polar decompositions of operators.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the polar decomposition and singular values.
- [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html), for the length used to take adjoints.
- [The Polar Decomposition from the Two Halves at $n=2$](the-polar-decomposition-from-the-two-halves-at-n-2.html), for the matrix theorem applied here.
- [The Hilbert–Schmidt Form at $n=2$](the-hilbert-schmidt-form-at-n-2.html), for the form that defines the adjoint.
