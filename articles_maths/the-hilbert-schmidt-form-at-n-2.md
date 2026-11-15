# __The Hilbert–Schmidt Form at $n=2$__

## Introduction

**The Hilbert–Schmidt form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ is a Hermitian inner product on $M_2(\mathbb{C})$, positive definite of signature $(8,0)$ over the reals, and its real part gives the matrix space the structure of a real Euclidean space of dimension eight.**

The article defines the form, proves that it is positive definite, identifies its norm with the sum of the squares of the entries, exhibits the eight vectors of an orthonormal real basis, shows that the four corners are mutually orthogonal, that the Hermitian and anti-Hermitian halves are orthogonal, and that on the real symmetric matrices the form agrees with the trace form while on all real matrices it is the entrywise product. It assumes *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*, *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* and *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$*.

It defers the four forms with their norms to *The Four Forms and Their Algebraic Norms at $n=2$*, and the polar decomposition of an operator to *The Adjoints and the Polar Decomposition of an Operator at $n=2$*.

## The Definition

**Definition.** The **Hilbert–Schmidt form** is $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$, where $X^{*}$ is the conjugate transpose.

**Proposition.** The form is Hermitian: it is conjugate-symmetric and linear in the second slot.

**Proof.** $\overline{\operatorname{tr}(X^{*}Y)}=\operatorname{tr}(Y^{*}X)$ by taking the conjugate transpose of the number, and the linearity in the second slot is the linearity of the trace.

**Theorem.** The form is positive definite: $\operatorname{tr}(X^{*}X)\ge 0$, with equality only for $X=0$.

**Proof.** $\operatorname{tr}(X^{*}X)=\sum_{i,j}\lvert x_{ij}\rvert^{2}$, a sum of squares of moduli, which is zero exactly when every entry vanishes.

**Corollary.** The real part of the form is a real inner product on the eight-dimensional real space, of signature $(8,0)$.

**Proof.** The real part is real bilinear and its quadratic form is the sum of the squares of the eight real coordinates of the matrix.

## The Norm and the Entries

**Proposition.** The square of the Hilbert–Schmidt norm is the sum of the squares of the moduli of the entries:

$$
\lVert X\rVert^{2}=\operatorname{tr}(X^{*}X)=\lvert x_{11}\rvert^{2}+\lvert x_{12}\rvert^{2}+\lvert x_{21}\rvert^{2}+\lvert x_{22}\rvert^{2}.
$$

**Proof.** The diagonal entries of $X^{*}X$ are the squared lengths of the columns of $X$, and their sum is the display.

**Corollary.** The norm is the Euclidean norm of the matrix read as a vector of four complex numbers, or of eight real numbers.

**Proof.** The formula is the sum of the four moduli squared, and each modulus squared is the sum of two real squares.

**Corollary.** The unit ball is the ball of $\mathbb{R}^{8}$, and the unit sphere is the sphere $S^{7}$.

**Proof.** The norm is the Euclidean norm in the eight real coordinates, so its level sets are the usual spheres.

## The Orthonormal Bases

**Proposition.** The four matrix units $E_{11}$, $E_{12}$, $E_{21}$, $E_{22}$ are orthonormal for the complex form, and the eight matrices $E_{ij}$ and $iE_{ij}$ are orthonormal for the real part.

**Proof.** $\operatorname{tr}(E_{ij}^{*}E_{kl})=\delta_{ik}\delta_{jl}$, since the product has a single nonzero entry equal to one on the diagonal when the indices match and is zero otherwise.

**Corollary.** The real dimension is eight, and the Hilbert–Schmidt form makes $M_2(\mathbb{C})$ isometric to $\mathbb{R}^{8}$.

**Proof.** The eight listed vectors are orthonormal, so they form a real basis, and in that basis the Gram matrix is the identity.

**Corollary.** The four corners $A_{kl}=P_{k}M_2P_{l}$ are mutually orthogonal, each of real dimension two.

**Proof.** A corner is spanned by the single matrix unit $E_{kl}$ and its multiple by $i$, and distinct matrix units are orthogonal.

## The Two Halves over the Complex Numbers

**Proposition.** The Hermitian half and the anti-Hermitian half are orthogonal for the real part of the form.

**Proof.** For Hermitian $H$ and anti-Hermitian $K$ the number $\operatorname{tr}(H^{*}K)=\operatorname{tr}(HK)$ equals the negative of its own conjugate, so it is purely imaginary and its real part vanishes.

**Corollary.** The real part of the form splits the space as an orthogonal sum of two real spaces of dimension four, and the splitting is the one of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*.

**Proof.** Every matrix is the sum of its Hermitian and anti-Hermitian parts, the two parts are orthogonal, and each half has real dimension four.

**Corollary.** On the Hermitian half the form is real, $\operatorname{tr}(H_{1}H_{2})$, and it is positive definite there.

**Proof.** For Hermitian matrices $H^{*}=H$, so the form is $\operatorname{tr}(H_{1}H_{2})$, a real number, and the value at two equal arguments is the sum of squares.

## The Two Halves over the Real Numbers

**Proposition.** On the real symmetric matrices the Hilbert–Schmidt form and the trace form agree, both sending a pair to $\operatorname{tr}(SY)$.

**Proof.** For real symmetric $S$ one has $S^{*}=S^{\mathsf T}=S$, so the two forms have the same formula.

**Corollary.** On all real matrices the two forms differ: the Hilbert–Schmidt form is the entrywise product $\sum_{ij}x_{ij}y_{ij}$, while the trace form is $\sum_{ij}x_{ij}y_{ji}$.

**Proof.** $\operatorname{tr}(X^{\mathsf T}Y)=\sum_{ij}x_{ij}y_{ij}$, whereas $\operatorname{tr}(XY)=\sum_{ij}x_{ij}y_{ji}$; the two sums differ on a matrix that is not symmetric.

**Corollary.** On the real matrices the Hilbert–Schmidt form is positive definite of signature $(4,0)$, while the trace form has signature $(3,1)$.

**Proof.** The entrywise product is the Euclidean product of the four entries, and the trace form was computed with the signature $(3,1)$ in *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$*.

**The two forms answer different questions.** The Hilbert–Schmidt form measures the size of the entries, and the trace form measures the size in the sense of the algebra, with the antisymmetric direction counting negatively.

**Proof.** The first is the sum of the squares of the entries and the second is $\operatorname{tr}(X^{2})$, whose value at $J$ is $-2$.

## The Adjoints and the Inequality

**Proposition.** The adjoint of the operator $\operatorname{ad}_{A}$ for the Hilbert–Schmidt form is $\operatorname{ad}_{A^{*}}$.

**Proof.** $\operatorname{tr}((AX-XA)^{*}Y)=\operatorname{tr}(X^{*}(A^{*}Y-YA^{*}))$ after expanding and cycling the trace.

**Corollary.** The adjoint action of the Hermitian matrices is self-adjoint, and the adjoint action of the anti-Hermitian ones is anti-self-adjoint.

**Proof.** The formula of the proposition gives $\operatorname{ad}_{A}^{*}=\operatorname{ad}_{A}$ for Hermitian $A$ and $\operatorname{ad}_{A}^{*}=-\operatorname{ad}_{A}$ for anti-Hermitian $A$.

**Proposition.** The Hilbert–Schmidt norm is submultiplicative against the operator norm: $\lVert XY\rVert\le\lVert X\rVert_{\mathrm{op}}\lVert Y\rVert$.

**Proof.** $\operatorname{tr}(Y^{*}X^{*}XY)\le\lVert X\rVert_{\mathrm{op}}^{2}\operatorname{tr}(Y^{*}Y)$, since $X^{*}X\le\lVert X\rVert_{\mathrm{op}}^{2}I$ in the order of Hermitian matrices.

**Corollary.** The Hilbert–Schmidt norm is submultiplicative: $\lVert XY\rVert\le\lVert X\rVert\lVert Y\rVert$.

**Proof.** Combine the display with the inequality $\lVert X\rVert_{\mathrm{op}}\le\lVert X\rVert$, which holds because the operator norm is the largest singular value and the Hilbert–Schmidt norm is the Euclidean norm of the two singular values.

## Summary

The Hilbert–Schmidt form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ is a Hermitian inner product on $M_2(\mathbb{C})$ whose real part is positive definite of signature $(8,0)$; its norm is the Euclidean norm of the four complex entries, and the eight matrices $E_{ij}$ and $iE_{ij}$ are an orthonormal real basis.

The four corners are mutually orthogonal, the Hermitian and anti-Hermitian halves are orthogonal for the real part, and on the real matrices the form is the entrywise product, positive definite of signature $(4,0)$, which agrees with the trace form on the symmetric half and differs from it elsewhere. The adjoint of $\operatorname{ad}_{A}$ is $\operatorname{ad}_{A^{*}}$, and the norm is submultiplicative against the operator norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle$ | $\operatorname{tr}(X^{*}Y)$, the Hilbert–Schmidt form |
| $X^{*}$ | the conjugate transpose |
| $\lVert X\rVert$ | the Hilbert–Schmidt norm |
| $\lVert X\rVert_{\mathrm{op}}$ | the operator norm |
| $E_{ij}$ | the matrix unit, orthonormal for the form |
| $A_{kl}$ | the corner $P_{k}M_2P_{l}$ |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Hilbert–Schmidt norm, its inequalities and its comparison with the operator norm.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the entrywise and the trace products on matrix spaces.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$](the-two-halves-over-c-hermitian-and-anti-hermitian-at-n-2.html), for the two orthogonal halves.
- [The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$](the-trace-form-and-its-signature-on-the-two-halves-of-m2r.html), for the indefinite form that the Hilbert–Schmidt form replaces.
- [The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form](the-derivation-commutator-and-its-anti-self-adjointness-for-the-trace-form.html), for the adjoint action whose adjoint is computed here.
