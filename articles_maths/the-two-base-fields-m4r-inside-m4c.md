# __The Two Base Fields: $M_4(\mathbb{R})$ inside $M_4(\mathbb{C})$__

## Introduction

**The real matrices are the fixed set of the entrywise conjugation of $M_4(\mathbb{C})$, a real form of real dimension $16$ inside $32$, and inside them sit the two ladders $\mathbb{R}\subset\mathbb{C}$ and $\mathbb{R}\subset\mathbb{H}$, the first with a central imaginary unit and the second with three anticommuting ones.**

The article proves that $M_4(\mathbb{R})$ is the fixed algebra of $\tau(A)=\bar A$, that $\mathbb{C}\otimes_{\mathbb{R}}M_4(\mathbb{R})\cong M_4(\mathbb{C})$, that the rank survives the change of field while every dimension doubles, and that in the axis-free basis the transpose is the quaternion conjugation. It closes with what fails over $\mathbb{R}$: the exponential is not onto, the group has two components, and the spectrum leaves the base field.

It assumes *The Matrix Algebra $M_4(\mathbb{C})$* for the product, the trace and the rank, and *$M_4(\mathbb{C})$ Axis-Free Representation* for the coefficient basis. The general theory of the pair $M_n(\mathbb{R})\subset M_n(\mathbb{C})$ is *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*, and the second real form of the complex algebra is *The Quaternionic Structure and the Real Forms of $M_4(\mathbb{C})$*.

## The Real Matrices as a Fixed Set

**Definition.** The **entrywise conjugation** of $M_4(\mathbb{C})$ is $\tau(A)=\bar A$, applied to the sixteen entries.

**Proposition.** The map $\tau$ is an involutive antilinear automorphism: it is additive, $\tau(\lambda A)=\bar\lambda\tau(A)$, multiplicative, $\tau(AB)=\tau(A)\tau(B)$, and $\tau^{2}=\mathrm{id}$.

**Proof.** Conjugation of complex numbers is additive, conjugate-linear and multiplicative, and the matrix product is a sum of products of entries; hence $\overline{AB}=\bar A\bar B$. Two conjugations return each entry.

**Theorem.** The fixed set of $\tau$ is $M_4(\mathbb{R})$, a real subalgebra of real dimension $16$.

**Proof.** An entry is fixed exactly when it is real. The real matrices are closed under sums, products and real scalars, so they form a real subalgebra; the real dimension is the count of the sixteen entries.

**The fixed set is not a complex subspace and not an ideal.** It is stable under real scalars only, since $i\mathrm I_4$ is not real, and the product $E_{11}(iE_{11})=iE_{11}$ leaves it. It is a real form, because $M_4(\mathbb{R})\cap iM_4(\mathbb{R})=0$ and the two sum to the algebra.

## The Complexification and the Doubling of Dimension

**Theorem.** $\mathbb{C}\otimes_{\mathbb{R}}M_4(\mathbb{R})\cong M_4(\mathbb{C})$ as $\mathbb{C}$-algebras.

**Proof.** The map $\lambda\otimes X\mapsto\lambda X$ is $\mathbb{C}$-bilinear and multiplicative, since $(\lambda\otimes X)(\mu\otimes Y)=\lambda\mu\otimes XY$. It is surjective because $A=X+iY$ with $X=\tfrac12(A+\bar A)$ and $Y=\tfrac1{2i}(A-\bar A)$ real, and the two sides have complex dimension $16$.

**Corollary (the real and imaginary parts).** Every matrix has a unique decomposition

$$
A=X+iY,\qquad X=\tfrac12(A+\bar A)\in M_4(\mathbb{R}),\quad Y=\tfrac1{2i}(A-\bar A)\in M_4(\mathbb{R}),
$$

and the product reads $AC=(XU-YV)+i(XV+YU)$ for $C=U+iV$ with $U,V$ real.

**The dimension count.** The real dimension of $M_4(\mathbb{C})$ is $32$; that of $M_4(\mathbb{R})$ is $16$. The groups follow: $\dim_{\mathbb{R}}\mathrm{GL}_4(\mathbb{C})=32$ and $\dim_{\mathbb{R}}\mathrm{GL}_4(\mathbb{R})=16$.

**Proposition (the rank survives).** For $X\in M_4(\mathbb{R})$ the rank over $\mathbb{R}$ equals the rank over $\mathbb{C}$.

**Proof.** The rank is the largest order of a nonvanishing minor, and a minor is a polynomial with integer coefficients in the entries. Its vanishing is a condition on the entries and not on the field in which they are read.

**Corollary.** The rank strata meet $M_4(\mathbb{R})$ in real dimensions $0$, $7$, $12$, $15$ and $16$, since a rank-$k$ stratum has dimension $8k-k^{2}$ and the real slice has the same real dimension.

## The Two Ladders

**The complex ladder.** Inside $M_4(\mathbb{R})$ sits the scalar line $\mathbb{R}\mathrm I_4$; adjoining one matrix $J$ with $J^{2}=-\mathrm I_4$ gives a copy of $\mathbb{C}$, of real dimension $2$. The three levels are $\mathbb{R}\subset\mathbb{C}\subset M_4(\mathbb{R})$, of real dimensions $1,2,16$.

**The quaternionic ladder.** The real quaternions sit inside $M_4(\mathbb{R})$ as the left multiplication $q\mapsto L_{\mathrm{axf}}(q)$ with real coefficients,

$$
q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z,\qquad q_\mu\in\mathbb{R}.
$$

The four matrices $L_{\mathrm{axf},e_\mu}$ are the real signed permutations of *$M_4(\mathbb{C})$ Axis-Free Representation*. They obey $L_{\mathrm{axf},\vec e_x}^{2}=L_{\mathrm{axf},\vec e_y}^{2}=L_{\mathrm{axf},\vec e_z}^{2}=-\mathrm I_4$ and the cyclic product rule, so the image is a copy of $\mathbb{H}$ of real dimension $4$.

**Proposition.** The complex ladder sits inside the quaternionic one: $\mathbb{R}\subset\mathbb{C}\subset\mathbb{H}\subset M_4(\mathbb{R})$, of real dimensions $1,2,4,16$.

**Proof.** The scalars are $q=q_te_t$; the copy of $\mathbb{C}$ is spanned by $e_t$ and one vector unit, which squares to $-e_t$ and commutes with itself; the three vector units together span $\mathbb{H}$. The inclusions are strict by the dimensions.

**The two ladders differ in the centre.** In $\mathbb{C}$ the imaginary unit is central, and $i\mathrm I_4$ is central in $M_4(\mathbb{C})$; in $\mathbb{H}$ no vector unit is central, since $\vec e_x\vec e_y=\vec e_z=-\vec e_y\vec e_x$. The complex ladder is the scalar field of the algebra, the quaternionic ladder a division subalgebra of it: $\langle q\rangle_{\natural}=q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}$ is a sum of four real squares, so $\det L_{\mathrm{axf}}(q)=\langle q\rangle_{\natural}^{2}$ vanishes only at $q=0$.

## The Real Slice of the Axis-Free Frame

**The sixteen matrices are real.** Each $T_{\mu\nu}=L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ is a signed permutation matrix, hence real, and the sixteen are independent over $\mathbb{C}$. Their real span is a subspace of $M_4(\mathbb{R})$ of real dimension $16$, which is all of it.

**Proposition.** No proper real subspace contains the sixteen, and the expansion $A=\sum q_{\mu\nu}T_{\mu\nu}$ of a real matrix has real coefficients $q_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\mathsf T}A)$.

**Proof.** Sixteen independent real matrices in a real space of dimension sixteen span it, and each trace is real for real $A$; the formula is the orthogonality $\operatorname{tr}(T_{\mu\nu}^{\mathsf T}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$ read as a projection.

**The trace pairing on the slice.** In this basis the pairing is diagonal,

$$
\operatorname{tr}(T_{\mu\nu}T_{\rho\sigma})=\pm4\,\delta_{\mu\rho}\delta_{\nu\sigma},
$$

with $+4$ on the ten symmetric elements and $-4$ on the six antisymmetric ones. The signature $(10,6)$ is therefore a statement about the real algebra already, and the complex algebra inherits it in the same basis. The full account is *The Trace Form and Its Signature on the Two Halves of $M_4(\mathbb{C})$*.

**One count is not the other.** The slice of the algebra itself is four-dimensional, the image of $\mathbb{H}$; the sixteen is the dimension of the operator basis, in which elements of the algebra appear as vectors.

## The Transpose in the Real Slice

**The transpose is the quaternion conjugation.** In the axis-free frame,

$$
L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural}),\qquad
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z .
$$

On the real slice this is a real identity: the transpose of a real matrix is real, and it is the matrix of the element with the three vector coefficients negated.

**Proposition.** The identity holds on real coefficients, and the transpose is an antiautomorphism of the image $\mathbb{B}_L$.

**Proof.** Transposition reverses products, $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$, and the quaternion conjugation does the same, $(q_1q_2)^{\natural}=q_2^{\natural}q_1^{\natural}$. The identity on the four units extends by linearity.

**The dagger on the slice.** The conjugate transpose of a real matrix is its transpose, so ${}^{\ast}$ restricts to ${}^{\mathsf T}$ on $M_4(\mathbb{R})$. Hence $\operatorname{Herm}_4\cap M_4(\mathbb{R})=\operatorname{Sym}_4(\mathbb{R})$, of real dimension $10$, and $\mathfrak{u}(4)\cap M_4(\mathbb{R})=\operatorname{Skew}_4(\mathbb{R})$, of real dimension $6$: the complex decomposition of dimensions $16+16$ meets the real slice in the decomposition $10+6$.

## What Fails over $\mathbb{R}$

**The exponential is not onto.** Over $\mathbb{C}$ the exponential is surjective onto $\mathrm{GL}_4(\mathbb{C})$, by the Jordan form and a logarithm chosen on each eigenvalue. Over $\mathbb{R}$ it is not. If $e^{X}=A$ with $X$ real, the eigenvalues of $X$ are logarithms of those of $A$; at a one-dimensional block with the eigenvalue $-2$ the only logarithm is $\log2+i\pi$, and a real $X$ would need $\log2-i\pi$ as well, which is a logarithm of no eigenvalue of $A$. Hence $\operatorname{diag}(-1,-1,-2,-3)$ has no real logarithm.

**The group has two components.** $\mathrm{GL}_4(\mathbb{R})$ has two connected components, separated by the sign of the determinant, while $\mathrm{GL}_4(\mathbb{C})$ is connected. The exponential lands in the component of positive determinant, and even there not onto it.

**The spectrum leaves the base field.** A real matrix has a characteristic polynomial with real coefficients, so its nonreal eigenvalues occur in conjugate pairs and its Jordan form carries $2\times2$ rotation blocks. The block of angle $\theta$ has the eigenvalues $e^{\pm i\theta}$ and no real eigenvector unless $\theta\in\pi\mathbb{Z}$.

**The quaternionic norm becomes Euclidean.** Over $\mathbb{C}$ the form $\langle\tilde Q\rangle_{\natural}$ is isotropic: the element with $Q_t=1$ and $Q_x=i$ has norm $1-1=0$, and its left matrix is a nonzero zero divisor. On the real slice the same form is a sum of four real squares, and its zero set collapses to the origin. One formula, a Lorentzian form in one reading and a Euclidean norm in the other.

## Summary

$M_4(\mathbb{R})$ is the fixed algebra of the entrywise conjugation of $M_4(\mathbb{C})$, of real dimension $16$ against $32$, and $\mathbb{C}\otimes_{\mathbb{R}}M_4(\mathbb{R})\cong M_4(\mathbb{C})$. Every matrix is $X+iY$ with $X,Y$ real and unique, the rank is a condition on minors and survives the change of field, and the rank strata have real dimensions $0,7,12,15,16$.

Two ladders sit inside the real matrices: $\mathbb{R}\subset\mathbb{C}\subset M_4(\mathbb{R})$ with a central imaginary unit, and $\mathbb{R}\subset\mathbb{C}\subset\mathbb{H}\subset M_4(\mathbb{R})$ with three anticommuting ones. The second is a division algebra of real dimension $4$, and it is the real slice of the biquaternion algebra under the left regular representation.

The axis-free basis is real, so its sixteen matrices are a coordinate frame of $M_4(\mathbb{R})$ and the trace pairing is diagonal there with ten signs $+4$ and six signs $-4$. On the real slice the transpose is the quaternion conjugation, and the dagger restricts to the transpose. What fails over $\mathbb{R}$ is the surjectivity of the exponential, the connectedness of the group, and the closedness of the spectrum; and the quaternionic norm turns from a Lorentzian form into a Euclidean one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(A)=\bar A$ | the entrywise conjugation, an antilinear involution |
| $M_4(\mathbb{R})$ | the fixed set of $\tau$, of real dimension $16$ |
| $X,Y$ | the real and imaginary parts of $A=X+iY$ |
| $L_{\mathrm{axf}}$ | the left regular representation, real on real coefficients |
| $T_{\mu\nu}$ | the sixteen two-sided basis matrices, all real |
| $q_{\mu\nu}$ | the real coordinates of a real matrix in that basis |
| $\natural$ | the quaternion conjugation, equal to the transpose in this frame |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the real and complex readings of one matrix and the reality of the spectrum.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the product, the trace, the determinant and the rank of the complex algebra.
- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the coefficient basis, the four left matrices and the transpose identity.
- [The Quaternionic Structure and the Real Forms of $M_4(\mathbb{C})$](the-quaternionic-structure-and-the-real-forms-of-m4c.html), for the second real form and its classification.
- [The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$](the-two-base-fields-m2r-inside-m2c.html), for the same pair at order two.
