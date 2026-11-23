# __The Hilbert–Schmidt Form at $n=4$__

## Introduction

**The form $\langle A,B\rangle=\operatorname{tr}(A^{\ast}B)$ is a positive definite Hermitian form on the sixteen-dimensional complex space, whose real part is an inner product on the thirty-two-dimensional real space; the matrix units are orthonormal for it, the sixteen axis-free elements divided by two are a second orthonormal basis, and the two bases are related by a unitary change of coordinates.**

The article proves the definiteness and the Hermitian symmetry, exhibits the two orthonormal bases and the coefficient formula, proves the Cauchy–Schwarz inequality and the two norm comparisons at order four, identifies the form as the unique up-to-scale inner product invariant under $U(4)$, and reads it as the trace form composed with the conjugate transpose.

It assumes *The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$* for the indefinite companion and *The Axis-Free Representation of $M_4(\mathbb{C})$* for the basis $T_{\mu\nu}$. The case $n=2$ is *The Hilbert–Schmidt Form at $n=2$*; the operator use is *The Adjoints and the Polar Decomposition of an Operator at $n=4$*.

## The Form and Its Definiteness

**Definition.** $\langle A,B\rangle=\operatorname{tr}(A^{\ast}B)$, where $A^{\ast}=\bar A^{\mathsf T}$.

**Proposition.** The form is sesquilinear, Hermitian and positive definite: $\langle B,A\rangle=\overline{\langle A,B\rangle}$, and $\langle A,A\rangle=\sum_{ij}|a_{ij}|^{2}>0$ for $A\neq0$.

**Proof.** $\operatorname{tr}(B^{\ast}A)=\overline{\operatorname{tr}(A^{\ast}B)}$ because the trace of the conjugate transpose is the conjugate of the trace; and $\operatorname{tr}(A^{\ast}A)=\sum_{i}(A^{\ast}A)_{ii}=\sum_{i}\sum_{j}\bar a_{ji}a_{ji}=\sum_{ij}|a_{ij}|^{2}$.

**Corollary.** $\langle\cdot,\cdot\rangle$ is an inner product on the complex space of dimension $16$, and its real part is an inner product on the real space of dimension $32$.

**Proof.** A positive definite Hermitian form is an inner product; the real part of a Hermitian form is a real inner product of twice the dimension.

**Definition.** $\lVert A\rVert_F=\sqrt{\langle A,A\rangle}=\bigl(\sum_{ij}|a_{ij}|^{2}\bigr)^{1/2}$ is the Frobenius norm.

**Proof.** The computation above.

**The imaginary part.** $\operatorname{Im}\langle A,B\rangle$ is a real symplectic form on the thirty-two-dimensional real space, and it is non-degenerate.

**Proof.** The imaginary part of a positive definite Hermitian form is a symplectic form, and it is non-degenerate because the real part is definite.

## The Two Orthonormal Bases

**Proposition.** The sixteen matrix units are orthonormal: $\langle E_{ij},E_{kl}\rangle=\delta_{ik}\delta_{jl}$.

**Proof.** $E_{ij}^{\ast}=E_{ji}$ and $\operatorname{tr}(E_{ji}E_{kl})=\delta_{ik}\delta_{jl}$.

**Theorem.** The sixteen elements $T_{\mu\nu}/2$ are orthonormal: $\langle T_{\mu\nu},T_{\rho\sigma}\rangle=4\delta_{\mu\rho}\delta_{\nu\sigma}$, so $\langle T_{\mu\nu}/2,T_{\rho\sigma}/2\rangle=\delta_{\mu\rho}\delta_{\nu\sigma}$.

**Proof.** Each $T_{\mu\nu}$ is a signed permutation matrix, so $T_{\mu\nu}^{\ast}=T_{\mu\nu}^{\mathsf T}=T_{\mu\nu}^{-1}$, and the product $T_{\mu\nu}^{\mathsf T}T_{\rho\sigma}$ has trace $4$ when the two coincide and $0$ otherwise; this is the verified identity $\operatorname{tr}(T_{\mu\nu}^{\dagger}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$.

**Corollary.** Both sets are orthonormal bases of the same sixteen-dimensional space, and the change of basis between them is unitary.

**Proof.** Two orthonormal bases of one inner product space are related by a unitary matrix.

**The coordinates.** For $A=\sum_{\mu\nu}c_{\mu\nu}T_{\mu\nu}$ one has $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}A)=\tfrac14\langle T_{\mu\nu},A\rangle$.

**Proof.** Take the inner product with $T_{\rho\sigma}$ and use orthogonality.

**Corollary.** $\lVert A\rVert_F^{2}=4\sum_{\mu\nu}|c_{\mu\nu}|^{2}$, so the Frobenius norm is, up to the factor $4$, the Euclidean norm of the axis-free coordinates.

**Proof.** Expand $\langle A,A\rangle$ in the orthogonal basis and use $\langle T,T\rangle=4$.

**The contrast with the matrix units.** In the matrix-unit coordinates the Frobenius norm is the Euclidean norm with no factor; in the axis-free coordinates it is the Euclidean norm with the factor $4$. Each basis is orthonormal up to a scale, and the two scales are $1$ and $2$.

**Proof.** $\langle E,E\rangle=1$ and $\langle T,T\rangle=4$, so the normalised elements are $E_{ij}$ and $T_{\mu\nu}/2$ respectively.

## The Norms and the Inequalities

**Theorem (Cauchy–Schwarz).** $|\langle A,B\rangle|\le\lVert A\rVert_F\lVert B\rVert_F$, with equality exactly when $A$ and $B$ are linearly dependent over $\mathbb{C}$.

**Proof.** The standard argument: for every $t\in\mathbb{C}$ the expression $\lVert A+tB\rVert_F^{2}$ is non-negative, and minimising over $t$ gives the inequality; equality forces $A+tB=0$.

**Definition.** The operator norm is $\lVert A\rVert_2=\sup\{\lVert Av\rVert:\lVert v\rVert=1\}$, the largest singular value.

**Theorem.** $\lVert A\rVert_2\le\lVert A\rVert_F\le2\lVert A\rVert_2$ at order four.

**Proof.** Let $s_1\ge s_2\ge s_3\ge s_4\ge0$ be the singular values. Then $\lVert A\rVert_2=s_1$ and $\lVert A\rVert_F^{2}=s_1^{2}+s_2^{2}+s_3^{2}+s_4^{2}$, so the left inequality is $s_1^{2}\le\sum s_k^{2}$ and the right is $\sum s_k^{2}\le4s_1^{2}$.

**Corollary.** The two inequalities are both attained: equality on the left for a matrix of rank one, equality on the right for a scalar multiple of a unitary matrix.

**Proof.** A rank-one matrix has one nonzero singular value; a unitary matrix has four equal ones.

**The constant $2$.** The upper constant is $\sqrt n=2$ at order four, and it grows with the order; it is the square root of the number of singular values.

**Proof.** The comparison $\sum_{k=1}^{n}s_k^{2}\le n s_1^{2}$ has the constant $n$ under the square root.

## Invariance and Uniqueness

**Proposition.** The form is invariant under the conjugation action of the unitary group: $\langle UAU^{\ast},UBU^{\ast}\rangle=\langle A,B\rangle$ for $U\in U(4)$.

**Proof.** $(UAU^{\ast})^{\ast}UBU^{\ast}=UA^{\ast}U^{\ast}UBU^{\ast}=UA^{\ast}BU^{\ast}$, whose trace is $\operatorname{tr}(A^{\ast}B)$.

**Theorem.** Every inner product on $M_4(\mathbb{C})$ invariant under the conjugation action of $U(4)$ is a positive multiple of $\langle\cdot,\cdot\rangle$.

**Proof.** The action of $U(4)$ on $M_4$ by conjugation is irreducible over the reals on the traceless part and acts on the scalars by the trivial character, and the invariants are computed by the double centraliser theorem: the commutant of the action is spanned by the identity operator, so the invariant inner products form a one-dimensional space. The form $\langle\cdot,\cdot\rangle$ is invariant and positive, so it spans that space.

**Corollary.** The Hilbert–Schmidt form is the canonical inner product of the algebra as a unitary representation, and every other invariant inner product is a rescaling.

**Proof.** The theorem and the positivity.

**What invariance fails for the trace form.** The trace pairing $\operatorname{tr}(AB)$ is invariant under the larger group $\mathrm{GL}_4$ acting by conjugation, and it is indefinite; the Hilbert–Schmidt form is invariant only under the smaller group $U(4)$, and it is definite.

**Proof.** $\operatorname{tr}(PAP^{-1}PBP^{-1})=\operatorname{tr}(AB)$ for all invertible $P$, and the form is indefinite; the unitary invariance was computed above and the smaller group is forced by the dagger.

## Relation to the Trace Form

**Theorem.** $\langle A,B\rangle=\beta(A^{\ast},B)$, where $\beta(X,Y)=\operatorname{tr}(XY)$.

**Proof.** Substitute $X=A^{\ast}$.

**Corollary.** The Hilbert–Schmidt form is the trace form composed with the involution, so the two forms carry the same information and differ by the choice of which factor is conjugated.

**Proof.** The identity above, read in both directions.

**Corollary.** $\beta$ is recovered from $\langle\cdot,\cdot\rangle$ by $\beta(A,B)=\langle A^{\ast},B\rangle$, and the indefiniteness of $\beta$ is the statement that the involution does not preserve the positive definite form.

**Proof.** Substitute $A^{\ast}$ for $A$ in the theorem and use $(A^{\ast})^{\ast}=A$; indefiniteness follows from $\beta(K,K)<0$ for a nonzero antisymmetric $K$ while $\langle K,K\rangle>0$.

**The two real forms.** On the real algebra the Hilbert–Schmidt form and the trace form coincide on the symmetric half and are opposite on the antisymmetric half, since $S^{\ast}=S$ and $K^{\ast}=-K$ there.

**Proof.** $\beta(S,B)=\langle S,B\rangle$ for symmetric $S$, and $\beta(K,B)=-\langle K,B\rangle$ for antisymmetric $K$.

**Corollary.** The inertia $(10,6)$ of the trace form and the positive definiteness of the Hilbert–Schmidt form are the same computation with the involution inserted.

**Proof.** The sign change on the six antisymmetric directions is exactly the difference between the two inertias.

## Summary

The Hilbert–Schmidt form is a positive definite Hermitian form, whose real part is an inner product on the real algebra of dimension $32$ and whose imaginary part is a symplectic form. The matrix units are orthonormal for it and the sixteen axis-free elements divided by two are a second orthonormal basis, related to the first by a unitary change of coordinates.

The Cauchy–Schwarz inequality holds, and the operator and Frobenius norms satisfy $\lVert A\rVert_2\le\lVert A\rVert_F\le2\lVert A\rVert_2$ at order four, with both bounds attained and with the constant $2$ equal to the square root of the order.

The form is invariant under conjugation by $U(4)$ and is the unique invariant inner product up to scale. It equals the trace form composed with the conjugate transpose, so the two forms differ by the involution and not by any independent choice: the positive definiteness of one and the inertia $(10,6)$ of the other are one computation read twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle A,B\rangle=\operatorname{tr}(A^{\ast}B)$ | the Hilbert–Schmidt form |
| $\lVert A\rVert_F$ | the Frobenius norm |
| $\lVert A\rVert_2$ | the operator norm, the largest singular value |
| $E_{ij}$, $T_{\mu\nu}/2$ | the two orthonormal bases |
| $\beta(A,B)=\operatorname{tr}(AB)$ | the trace form |
| $U(4)$ | the invariance group of the form |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Frobenius and operator norms and their comparison.
- [The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m4c.html), for the indefinite companion.
- [The Axis-Free Representation of $M_4(\mathbb{C})$](m4c-axis-free-representation.html), for the orthonormal basis $T_{\mu\nu}/2$.
- [The Adjoints and the Polar Decomposition of an Operator at $n=4$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-4.html), for the adjoint computed with this form.
- [The Hilbert–Schmidt Form at $n=2$](the-hilbert-schmidt-form-at-n-2.html), for the same form at order two.
