# __The Hermitian Sylvester Equation__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ with the Hermitian conjugation ${}^{*}$, and let $L_{\tilde Q_3}$, $R_{\tilde Q_4}$ be the left and right multiplications. The **Sylvester equation** on the algebra is

$$
\tilde Q_3\tilde Q + \tilde Q\tilde Q_4 = c ,
$$

an equation on the element $\tilde Q$ for given $\tilde Q_3,\tilde Q_4,c$, and its operator form is

$$
(L_{\tilde Q_3}+R_{\tilde Q_4})(\tilde Q) = c .
$$

This article is the biquaternion instance of *The Hermitian Sylvester Equation with Hermitian Adjoint*. The theory is complete and explicit: the Sylvester operator has the pairwise-sum spectrum $\lambda_{i}+\mu_{j}$, it is invertible exactly when the spectra of $\tilde Q_3$ and of $-\tilde Q_4$ are disjoint, its adjoint is $L_{\tilde Q_3^{*}}+R_{\tilde Q_4^{*}}$, it is self-adjoint exactly when **both** parameters are Hermitian, and the Hermitian case is the case of the **anticommutator**; the general article writes the solution operator of the Hermitian case as $L_{\tilde Q_3}(\tilde Q)=\tilde Q_3^{*}\tilde Q+\tilde Q\tilde Q_3$, which is $S_{\tilde Q_3^{*},\tilde Q_3}$ here, its $L$ being the Sylvester operator and not the left multiplication $L_{\tilde Q_3}$ of this series. Its companion $L_{\tilde Q_3}-R_{\tilde Q_3}$ is the inner derivation $\mathrm{ad}_{\tilde Q_3}=[\tilde Q_3,\cdot\,]$, which is skew-adjoint for Hermitian $\tilde Q_3$ and carries the roots of the algebra. The two operators together split every element into the commutator and the anticommutator part, which is the reason the Sylvester equation sits at the centre of the operator theory of the algebra.

## The Sylvester Operator and the Equation

**Definition.** For $\tilde Q_3,\tilde Q_4\in\mathbb{B}$ the **Sylvester operator** is $S_{\tilde Q_3,\tilde Q_4}=L_{\tilde Q_3}+R_{\tilde Q_4}\in\mathrm{End}(\mathbb{B})$, acting by $S_{\tilde Q_3,\tilde Q_4}(\tilde Q)=\tilde Q_3\tilde Q+\tilde Q\tilde Q_4$. The **Sylvester equation** is $S_{\tilde Q_3,\tilde Q_4}(\tilde Q)=c$; the **homogeneous** equation is $\tilde Q_3\tilde Q+\tilde Q\tilde Q_4=0$.

**Proposition (the operator is a sum of the two one-sided families).** $S_{\tilde Q_3,\tilde Q_4}=L_{\tilde Q_3}+R_{\tilde Q_4}$, and $L_{\tilde Q_3},R_{\tilde Q_4}$ commute; $S_{\tilde Q_3,\tilde Q_4}$ is a linear bijection of the algebra precisely when it is injective, since the algebra is finite-dimensional.

**Example ($\tilde Q_4=-\tilde Q_3$: the commutator).** $S_{\tilde Q_3,-\tilde Q_3}=L_{\tilde Q_3}-R_{\tilde Q_3}=\mathrm{ad}_{\tilde Q_3}$, the **inner derivation** $\tilde Q\mapsto \tilde Q_3\tilde Q-\tilde Q\tilde Q_3=[\tilde Q_3,\tilde Q]$, whose kernel is the centraliser of $\tilde Q_3$ and whose image is the space of the "commutators with $\tilde Q_3$".

**Example ($\tilde Q_4=\tilde Q_3$: the anticommutator).** $S_{\tilde Q_3,\tilde Q_3}=L_{\tilde Q_3}+R_{\tilde Q_3}$, the **anticommutator** operator $\tilde Q\mapsto \tilde Q_3\tilde Q+\tilde Q\tilde Q_3=\{\tilde Q_3,\tilde Q\}$, whose kernel is the space of the elements **anti-commuting** with $\tilde Q_3$.

## The Spectrum and the Solvability Theorem

**Theorem (the Sylvester spectrum).** Let $\lambda_{1},\lambda_{2}$ be the eigenvalues of $\mathsf{M}_2(\tilde Q_3)$ and $\mu_{1},\mu_{2}$ those of $\mathsf{M}_2(\tilde Q_4)$. Then

$$
\boxed{\; \mathrm{spec}(S_{\tilde Q_3,\tilde Q_4})=\{\lambda_{i}+\mu_{j}\},\qquad
\det(S_{\tilde Q_3,\tilde Q_4})=\prod_{i,j}(\lambda_{i}+\mu_{j}) \;}.
$$

*Proof.* $S_{\tilde Q_3,\tilde Q_4}=\mathsf{M}_2(\tilde Q_3)\otimes I+I\otimes\mathsf{M}_2(\tilde Q_4)^{T}$ in the vectorisation of *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*, and the spectrum of a Kronecker sum is the set of pairwise sums.

**Theorem (the solvability criterion).** The Sylvester equation $\tilde Q_3\tilde Q+\tilde Q\tilde Q_4=c$ has a **unique** solution for every $c$ if and only if no eigenvalue of $\mathsf{M}_2(\tilde Q_3)$ is the negative of an eigenvalue of $\mathsf{M}_2(\tilde Q_4)$. If the criterion fails, the equation is solvable exactly when $c$ is orthogonal to the kernel of the adjoint $L_{\tilde Q_3^{*}}+R_{\tilde Q_4^{*}}$, and the solution set is an affine subspace of dimension $\sum_{m}(\text{multiplicity of }0\text{ in the spectrum})$.

*Proof.* $S_{\tilde Q_3,\tilde Q_4}$ is invertible iff $0$ is not an eigenvalue, i.e. iff no $\lambda_{i}+\mu_{j}=0$; the remaining statements are the Fredholm alternative for a finite-dimensional operator.

**Remark (the Hermitian case).** When both parameters are **Hermitian**, the spectrum of $S_{\tilde Q_3,\tilde Q_4}$ is real and the criterion becomes: **no eigenvalue of $\tilde Q_3$ is the negative of an eigenvalue of $\tilde Q_4$**. For $\tilde Q_3=\tilde Q_4$ Hermitian the anticommutator $\tilde Q_3\tilde Q+\tilde Q\tilde Q_3=c$ is uniquely solvable exactly when $\tilde Q_3$ has no pair of **opposite** eigenvalues: this is the Hermitian Sylvester equation proper, and it fails exactly at $\tilde Q_3=\mathrm{diag}(1,-1)$ (for which $\tilde Q=\mathrm{diag}(0,0)$ is a nonzero solution of the homogeneous equation) and at the elements with a zero eigenvalue.

## The Adjoint and the Self-Adjoint Cases

**Theorem (the adjoint).** $(L_{\tilde Q_3}+R_{\tilde Q_4})^{*}=L_{\tilde Q_3^{*}}+R_{\tilde Q_4^{*}}$, that is $S_{\tilde Q_3,\tilde Q_4}^{*}=S_{\tilde Q_3^{*},\tilde Q_4^{*}}$.

*Proof.* From $(L_{\tilde Q_3})^{*}=L_{\tilde Q_3^{*}}$ and $(R_{\tilde Q_4})^{*}=R_{\tilde Q_4^{*}}$ of *One-Sided Operators on the General Plain Sesqualgebra*.

**Corollary (self-adjointness needs both parameters Hermitian).** $S_{\tilde Q_3,\tilde Q_4}$ is self-adjoint if and only if $\tilde Q_3$ and $\tilde Q_4$ are both Hermitian. In particular the Lyapunov operator $S_{\tilde Q_3,\tilde Q_3^{*}}=L_{\tilde Q_3}+R_{\tilde Q_3^{*}}$ is self-adjoint if and only if $\tilde Q_3$ is Hermitian; for general $\tilde Q_3$ it is not, and its adjoint is $L_{\tilde Q_3^{*}}+R_{\tilde Q_3}$. **The temptation to call $L_{\tilde Q_3}+R_{\tilde Q_3^{*}}$ self-adjoint for every $\tilde Q_3$ is the trap of this article.**

*Proof.* $S_{\tilde Q_3,\tilde Q_4}^{*}=S_{\tilde Q_3^{*},\tilde Q_4^{*}}$ equals $S_{\tilde Q_3,\tilde Q_4}$ iff $\tilde Q_3^{*}=\tilde Q_3$ and $\tilde Q_4^{*}=\tilde Q_4$. The Lyapunov case: $S_{\tilde Q_3,\tilde Q_3^{*}}^{*}=S_{\tilde Q_3^{*},\tilde Q_3}$, which equals $S_{\tilde Q_3,\tilde Q_3^{*}}$ iff $\tilde Q_3=\tilde Q_3^{*}$.

**Corollary (the anticommutator spectrum in the Hermitian case).** For Hermitian $\tilde Q_3$ the operator $L_{\tilde Q_3}+R_{\tilde Q_3}$ is self-adjoint with the real spectrum $\{2\lambda_{1},\ \lambda_{1}+\lambda_{2},\ \lambda_{1}+\lambda_{2},\ 2\lambda_{2}\}$: the two **doubled** eigenvalues $2\lambda_{i}$ and the **sum** $\lambda_{1}+\lambda_{2}$ counted twice. Consequently: if $\tilde Q_3$ is definite the anticommutator operator is definite with the sign of $\tilde Q_3$; if $\tilde Q_3$ is indefinite it has eigenvalues of both signs and is never definite; and it is **singular** exactly when $\lambda_{1}+\lambda_{2}=0$, that is, exactly when the Hermitian and indefinite $\tilde Q_3$ has trace zero. The same computation for the sandwich gives the products $\lambda_{i}\lambda_{j}$ and the signature $(p^{2}+q^{2},2pq)$ of *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*: the anticommutator uses the **sums** and the sandwich the **products** of the eigenvalues, and the two patterns must not be interchanged.

## The Commutator, the Anticommutator and the Derivation

**Theorem (the commutator laws).** For all $\tilde Q_3,\tilde Q_4$,

$$
\boxed{\; [L_{\tilde Q_3},L_{\tilde Q_4}]=L_{[\tilde Q_3,\tilde Q_4]},\qquad [R_{\tilde Q_3},R_{\tilde Q_4}]=-R_{[\tilde Q_3,\tilde Q_4]},\qquad [L_{\tilde Q_3},R_{\tilde Q_4}]=0 \;}.
$$

*Proof.* $L_{\tilde Q_3}L_{\tilde Q_4}=L_{\tilde Q_3\tilde Q_4}$ and $R_{\tilde Q_3}R_{\tilde Q_4}=R_{\tilde Q_4\tilde Q_3}$ from the composition laws, and $L$ and $R$ commute because left and right multiplication commute.

**Corollary (the inner derivation is a Lie algebra homomorphism).** The map $\tilde Q_3\mapsto\mathrm{ad}_{\tilde Q_3}=L_{\tilde Q_3}-R_{\tilde Q_3}$ is a representation of the Lie algebra of $\mathbb{B}$ on $\mathbb{B}$,

$$
[\mathrm{ad}_{\tilde Q_3},\mathrm{ad}_{\tilde Q_4}]=\mathrm{ad}_{[\tilde Q_3,\tilde Q_4]},\qquad\text{that is}\qquad [L_{\tilde Q_3}-R_{\tilde Q_3},\ L_{\tilde Q_4}-R_{\tilde Q_4}]=L_{[\tilde Q_3,\tilde Q_4]}-R_{[\tilde Q_3,\tilde Q_4]},
$$

and $\mathrm{ad}_{\tilde Q_3}$ is a derivation of the associative algebra, $\mathrm{ad}_{\tilde Q_3}(\tilde Q_1\tilde Q_2)=\mathrm{ad}_{\tilde Q_3}(\tilde Q_1)\tilde Q_2+\tilde Q_1\,\mathrm{ad}_{\tilde Q_3}(\tilde Q_2)$. Its spectrum is the set of pairwise differences $\lambda_{i}-\lambda_{j}$: for Hermitian $\tilde Q_3$ these are the real **roots** and $\mathrm{ad}_{\tilde Q_3}$ is the infinitesimal generator of the inner automorphism group. This is the operator form of *Biquaternion Automorphisms and Derivations*.

**Theorem (adjointness of the commutator and the anticommutator).** For $\tilde Q_3\in\mathbb{B}$:

1. $(\mathrm{ad}_{\tilde Q_3})^{*}=\mathrm{ad}_{\tilde Q_3^{*}}$; hence the inner derivation $\mathrm{ad}_{\tilde Q_3}=L_{\tilde Q_3}-R_{\tilde Q_3}$ is **self-adjoint** exactly when $\tilde Q_3$ is Hermitian and **skew-adjoint** exactly when $\tilde Q_3$ is anti-Hermitian;
2. the anticommutator operator $L_{\tilde Q_3}+R_{\tilde Q_3}$ is **self-adjoint** exactly when $\tilde Q_3$ is Hermitian.

*Proof.* $(L_{\tilde Q_3}+R_{\tilde Q_3})^{*}=L_{\tilde Q_3^{*}}+R_{\tilde Q_3^{*}}$, which equals $L_{\tilde Q_3}+R_{\tilde Q_3}$ iff $\tilde Q_3^{*}=\tilde Q_3$ for (2); the same computation with the relative sign gives $(\mathrm{ad}_{\tilde Q_3})^{*}=\mathrm{ad}_{\tilde Q_3^{*}}$ for (1).

**Remark (the sector reading).** The two statements are the sector decomposition at the operator level: the **anticommutator** is the self-adjoint operator of the **Hermitian** elements, and the **commutator** is the skew-adjoint operator of the **anti-Hermitian** elements. Since $e_{k}\in\mathbb{M}_-$ for $k=1,2,3$, the derivations $\mathrm{ad}_{e_{k}}$ are skew-adjoint with purely imaginary spectra, and $\exp(\mathrm{ad}_{e_{k}})$ are rotations, of period $\pi$ because the elementary rotation is at half-angle: this is the operator form of the compact internal group of *One-Sided Operators on the General Plain Sesqualgebra*.

## The Solution

**Theorem (the Kronecker solution).** When $S_{\tilde Q_3,\tilde Q_4}$ is invertible, the solution of $\tilde Q_3\tilde Q+\tilde Q\tilde Q_4=c$ is $\tilde Q=\mathrm{vec}^{-1}\bigl((\mathsf{M}_2(\tilde Q_3)\otimes I+I\otimes\mathsf{M}_2(\tilde Q_4)^{T})^{-1}\,\mathrm{vec}(c)\bigr)$, and in a basis diagonalising both parameters simultaneously (when they commute and are separately diagonalisable) it is the entrywise formula

$$
Q_{ij} = \frac{c_{ij}}{\lambda_{i}+\mu_{j}} .
$$

*Proof.* The vectorised equation is a linear system with matrix $\mathsf{M}_2(\tilde Q_3)\otimes I+I\otimes\mathsf{M}_2(\tilde Q_4)^{T}$; the diagonal case is the $2\times2$ instance of it.

**Theorem (the integral representation).** Let $\tilde Q_3,\tilde Q_4$ have spectra in the open right half-plane (so that $\exp(-t\tilde Q_3)$ and $\exp(-t\tilde Q_4)$ decay). Then

$$
\boxed{\; \tilde Q = \int_{0}^{\infty} \exp(-t\tilde Q_3)\,c\,\exp(-t\tilde Q_4)\,dt \;}
$$

is the solution of $\tilde Q_3\tilde Q+\tilde Q\tilde Q_4=c$.

*Proof.* Differentiate: $\tilde Q_3\tilde Q+\tilde Q\tilde Q_4=\int_{0}^{\infty}\bigl(\tilde Q_3 \exp(-t\tilde Q_3)c\exp(-t\tilde Q_4)+\exp(-t\tilde Q_3)c\exp(-t\tilde Q_4)\tilde Q_4\bigr)dt=-\int_{0}^{\infty}\frac{d}{dt}\bigl(\exp(-t\tilde Q_3)c\exp(-t\tilde Q_4)\bigr)dt=\exp(0)ce^{0}=c$.

**Remark (why the Hermitian case is the interesting one).** For Hermitian $\tilde Q_3,\tilde Q_4$ the operator is self-adjoint and the equation is the **operator form of the Hermitian condition**: it is the equation satisfied by the fixed point of the linear relaxation $\tilde Q\mapsto c-\tilde Q_3\tilde Q-\tilde Q\tilde Q_4$, by the correction term of any perturbative expansion, and by the solution of the Lyapunov problem of linear systems theory. The integral representation is the statement that the solution is a **time-ordered average** of the two exponential factors, and it is the reason the solution of a stable equation is written with two decaying exponentials rather than one.

## Worked Examples

**The identity.** $\tilde Q_3=\tilde Q_4=e_t$: $S(\tilde Q)=2\tilde Q$, invertible, solution $\tilde Q=c/2$. The spectrum is $\{2,2,2,2\}$ and $\det(S)=16$, as the formula gives.

**The singular Hermitian case.** For the Hermitian element $i\vec e_z$ (the matrix $\sigma_{3}$, eigenvalues $\{1,-1\}$ and inertia $(1,1)$): the anticommutator operator $L_{i\vec e_z}+R_{i\vec e_z}$ is self-adjoint with the real spectrum $\{2,0,0,-2\}$ and it is **singular**, because the two opposite eigenvalues $1$ and $-1$ give the vanishing sum. The homogeneous equation $i\vec e_z\tilde Q+\tilde Qi\vec e_z=0$ has the two-dimensional solution space spanned by the off-diagonal matrix units $E_{12}$ and $E_{21}$: the anticommutator is not invertible exactly for the indefinite Hermitian elements with opposite eigenvalues, which is the exact algebraic statement of the failure of the Hermitian Sylvester equation in that case.

**The Lyapunov operator of an anti-Hermitian element.** For $\tilde Q_3=\vec e_z$ (anti-Hermitian, $\vec e_z^{\dagger}=-\vec e_z$) the operator $L_{\tilde Q_3}+R_{\tilde Q_3^{*}}=L_{\vec e_z}-R_{\vec e_z}=\mathrm{ad}_{\vec e_z}$ is the inner derivation, and it is **not** self-adjoint but skew-adjoint, with the purely imaginary spectrum $\{0,2i,-2i,0\}$. This is the trap of the article in its sharpest form: $L_{\tilde Q_3}+R_{\tilde Q_3^{*}}$ looks symmetric in its two factors and is skew-adjoint for an anti-Hermitian $\tilde Q_3$.

**The derivation of the internal rotation.** $\mathrm{ad}_{\vec e_z}$ has the spectrum $\{0,2i,-2i,0\}$, the pairwise differences of the eigenvalues $\{i,-i\}$ of $\mathsf{M}_2(\vec e_z)$: the two roots $\pm2i$ are the weights of the derivation on the off-diagonal entries and the two zeros are the diagonal weights. Since $\vec e_z\in\mathbb{M}_-$ the derivation is skew-adjoint and $\exp(\mathrm{ad}_{\vec e_z})$ is a rotation of period $\pi$, the internal rotation group generated by $\vec e_z$ at half-angle.

**The commutator with $e_t$.** $\mathrm{ad}_{e_t}=L_{e_t}-R_{e_t}=0$: the identity generates no inner derivation, and consistently the central elements have zero pairwise differences. More generally $\mathrm{ad}_{\tilde Q_3}=0$ exactly for the central $\tilde Q_3$.

## Summary

The Sylvester equation $\tilde Q_3\tilde Q+\tilde Q\tilde Q_4=c$ on the biquaternion algebra is the equation of the operator $S_{\tilde Q_3,\tilde Q_4}=L_{\tilde Q_3}+R_{\tilde Q_4}$, whose spectrum is the set of pairwise sums $\lambda_{i}+\mu_{j}$ and whose determinant is their product; it is uniquely solvable exactly when no eigenvalue of $\tilde Q_3$ is the negative of an eigenvalue of $\tilde Q_4$, and in the Hermitian case exactly when the two Hermitian parameters have no opposite eigenvalues. The adjoint is $S_{\tilde Q_3,\tilde Q_4}^{*}=L_{\tilde Q_3^{*}}+R_{\tilde Q_4^{*}}$, so $S_{\tilde Q_3,\tilde Q_4}$ is self-adjoint exactly when **both** parameters are Hermitian — in particular the Lyapunov operator $L_{\tilde Q_3}+R_{\tilde Q_3^{*}}$ is self-adjoint only for Hermitian $\tilde Q_3$, which is the trap of the article. The companion operator $L_{\tilde Q_3}-R_{\tilde Q_3}$ is the inner derivation $\mathrm{ad}_{\tilde Q_3}=[\tilde Q_3,\cdot\,]$, with spectrum the pairwise differences $\lambda_{i}-\lambda_{j}$, skew-adjoint exactly for the anti-Hermitian parameters, and a Lie algebra homomorphism $\tilde Q_3\mapsto\mathrm{ad}_{\tilde Q_3}$; the anticommutator is self-adjoint exactly for the Hermitian parameters. The solution is given by the Kronecker inverse, by the entrywise formula $Q_{ij}=c_{ij}/(\lambda_{i}+\mu_{j})$ in the diagonalisable case, and by the time-ordered integral $\int_{0}^{\infty}\exp(-t\tilde Q_3)c\exp(-t\tilde Q_4)dt$ in the stable case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{\tilde Q_3,\tilde Q_4}=L_{\tilde Q_3}+R_{\tilde Q_4}$ | Sylvester operator; $\tilde Q\mapsto \tilde Q_3\tilde Q+\tilde Q\tilde Q_4$ |
| $\mathrm{spec}(S_{\tilde Q_3,\tilde Q_4})=\{\lambda_{i}+\mu_{j}\}$ | Pairwise sums of the spectra |
| $\det(S_{\tilde Q_3,\tilde Q_4})=\prod_{i,j}(\lambda_{i}+\mu_{j})$ | Product of the pairwise sums |
| $S_{\tilde Q_3,\tilde Q_4}^{*}=S_{\tilde Q_3^{*},\tilde Q_4^{*}}$ | The adjoint; self-adjoint iff $\tilde Q_3,\tilde Q_4$ both Hermitian |
| $\mathrm{ad}_{\tilde Q_3}=L_{\tilde Q_3}-R_{\tilde Q_3}$ | Inner derivation; spectrum $\lambda_{i}-\lambda_{j}$ |
| $\{\tilde Q_3,\cdot\}=L_{\tilde Q_3}+R_{\tilde Q_3}$ | Anticommutator operator; self-adjoint iff $\tilde Q_3$ Hermitian |
| $[L_{\tilde Q_3},L_{\tilde Q_4}]=L_{[\tilde Q_3,\tilde Q_4]}$ | Commutator law of the left multiplications |
| $Q_{ij}=c_{ij}/(\lambda_{i}+\mu_{j})$ | The solution in the diagonalisable case |
| $\int_{0}^{\infty}\exp(-t\tilde Q_3)c\exp(-t\tilde Q_4)dt$ | The solution in the stable case |

## Further Reading

- [The Hermitian Sylvester Equation with Hermitian Adjoint](the-hermitian-sylvester-equation-with-hermitian-adjoint.html), the general theory of which this is the biquaternion instance.
- [The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint](the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.html), for the spectral rules used throughout.
- [One-Sided Operators on the General Plain Sesqualgebra](one-sided-operators-on-the-general-plain-sesqualgebra.html), for the adjoints $(L_{\tilde Q_3})^{*}=L_{\tilde Q_3^{*}}$ and the composition laws.
- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), for the sandwich, its invariants and the congruence.
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the derivations, the roots and the exponential.
- [Self-Adjoint and Skew Operators with Hermitian Adjoint](self-adjoint-and-skew-operators-with-hermitian-adjoint.html), for the general theory of the adjoint on an operator algebra.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the commutator, the roots and the Lie structure of the algebra.
