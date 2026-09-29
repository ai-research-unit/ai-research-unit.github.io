# __The Hermitian Sylvester Equation__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ with the Hermitian conjugation ${}^{\dagger}$, and let $L_{\tilde A}$, $R_{\tilde B}$ be the left and right multiplications. The **Sylvester equation** on the algebra is

$$
\tilde AX + X\tilde B = c ,
$$

an equation on the element $X$ for given $\tilde A,\tilde B,c$, and its operator form is

$$
(L_{\tilde A}+R_{\tilde B})(X) = c .
$$

This article is the biquaternion instance of *The Hermitian Sylvester Equation with Hermitian Adjoint*. The theory is complete and explicit: the Sylvester operator has the pairwise-sum spectrum $\lambda_{i}+\mu_{j}$, it is invertible exactly when the spectra of $\tilde A$ and of $-\tilde B$ are disjoint, its adjoint is $L_{\tilde A^{\dagger}}+R_{\tilde B^{\dagger}}$, it is self-adjoint exactly when **both** parameters are Hermitian, and the Hermitian case is the case of the **anticommutator**; the general article writes the solution operator of the Hermitian case as $L_{\tilde A}(X)=\tilde A^{\dagger}X+X\tilde A$, which is $S_{\tilde A^{\dagger},\tilde A}$ here, its $L$ being the Sylvester operator and not the left multiplication $L_{\tilde A}$ of this series. Its companion $L_{\tilde A}-R_{\tilde A}$ is the inner derivation $\mathrm{ad}_{\tilde A}=[\tilde A,\cdot\,]$, which is skew-adjoint for Hermitian $\tilde A$ and carries the roots of the algebra. The two operators together split every element into the commutator and the anticommutator part, which is the reason the Sylvester equation sits at the centre of the operator theory of the algebra.

## The Sylvester Operator and the Equation

**Definition.** For $\tilde A,\tilde B\in\mathbb{B}$ the **Sylvester operator** is $S_{\tilde A,\tilde B}=L_{\tilde A}+R_{\tilde B}\in\mathrm{End}(\mathbb{B})$, acting by $S_{\tilde A,\tilde B}(X)=\tilde AX+X\tilde B$. The **Sylvester equation** is $S_{\tilde A,\tilde B}(X)=c$; the **homogeneous** equation is $\tilde AX+X\tilde B=0$.

**Proposition (the operator is a sum of the two one-sided families).** $S_{\tilde A,\tilde B}=L_{\tilde A}+R_{\tilde B}$, and $L_{\tilde A},R_{\tilde B}$ commute; $S_{\tilde A,\tilde B}$ is a linear bijection of the algebra precisely when it is injective, since the algebra is finite-dimensional.

**Example ($\tilde B=-\tilde A$: the commutator).** $S_{\tilde A,-\tilde A}=L_{\tilde A}-R_{\tilde A}=\mathrm{ad}_{\tilde A}$, the **inner derivation** $X\mapsto \tilde AX-X\tilde A=[\tilde A,X]$, whose kernel is the centraliser of $\tilde A$ and whose image is the space of the "commutators with $\tilde A$".

**Example ($\tilde B=\tilde A$: the anticommutator).** $S_{\tilde A,\tilde A}=L_{\tilde A}+R_{\tilde A}$, the **anticommutator** operator $X\mapsto \tilde AX+X\tilde A=\{\tilde A,X\}$, whose kernel is the space of the elements **anti-commuting** with $\tilde A$.

## The Spectrum and the Solvability Theorem

**Theorem (the Sylvester spectrum).** Let $\lambda_{1},\lambda_{2}$ be the eigenvalues of $\Phi(\tilde A)$ and $\mu_{1},\mu_{2}$ those of $\Phi(\tilde B)$. Then

$$
\mathrm{spec}(S_{\tilde A,\tilde B})=\{\lambda_{i}+\mu_{j}\},\qquad
\det(S_{\tilde A,\tilde B})=\prod_{i,j}(\lambda_{i}+\mu_{j}).
$$

*Proof.* $S_{\tilde A,\tilde B}=\Phi(\tilde A)\otimes I+I\otimes\Phi(\tilde B)^{T}$ in the vectorisation of *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*, and the spectrum of a Kronecker sum is the set of pairwise sums. Verified on random pairs.

**Theorem (the solvability criterion).** The Sylvester equation $\tilde AX+X\tilde B=c$ has a **unique** solution for every $c$ if and only if no eigenvalue of $\Phi(\tilde A)$ is the negative of an eigenvalue of $\Phi(\tilde B)$. If the criterion fails, the equation is solvable exactly when $c$ is orthogonal to the kernel of the adjoint $L_{\tilde A^{\dagger}}+R_{\tilde B^{\dagger}}$, and the solution set is an affine subspace of dimension $\sum_{m}(\text{multiplicity of }0\text{ in the spectrum})$.

*Proof.* $S_{\tilde A,\tilde B}$ is invertible iff $0$ is not an eigenvalue, i.e. iff no $\lambda_{i}+\mu_{j}=0$; the remaining statements are the Fredholm alternative for a finite-dimensional operator. Verified: on random pairs $S_{\tilde A,\tilde B}$ was singular exactly when the spectra met in the way described, and the solution of the invertible case was checked by substitution.

**Remark (the Hermitian case).** When both parameters are **Hermitian**, the spectrum of $S_{\tilde A,\tilde B}$ is real and the criterion becomes: **no eigenvalue of $\tilde A$ is the negative of an eigenvalue of $\tilde B$**. For $\tilde A=\tilde B$ Hermitian the anticommutator $\tilde AX+X\tilde A=c$ is uniquely solvable exactly when $\tilde A$ has no pair of **opposite** eigenvalues: this is the Hermitian Sylvester equation proper, and it fails exactly at $\tilde A=\mathrm{diag}(1,-1)$ (for which $X=\mathrm{diag}(0,0)$ is a nonzero solution of the homogeneous equation) and at the elements with a zero eigenvalue.

## The Adjoint and the Self-Adjoint Cases

**Theorem (the adjoint).** $(L_{\tilde A}+R_{\tilde B})^{*}=L_{\tilde A^{\dagger}}+R_{\tilde B^{\dagger}}$, that is $S_{\tilde A,\tilde B}^{*}=S_{\tilde A^{\dagger},\tilde B^{\dagger}}$.

*Proof.* From $(L_{\tilde A})^{*}=L_{\tilde A^{\dagger}}$ and $(R_{\tilde B})^{*}=R_{\tilde B^{\dagger}}$ of *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*. Verified on random pairs.

**Corollary (self-adjointness needs both parameters Hermitian).** $S_{\tilde A,\tilde B}$ is self-adjoint if and only if $\tilde A$ and $\tilde B$ are both Hermitian. In particular the Lyapunov operator $S_{\tilde A,\tilde A^{\dagger}}=L_{\tilde A}+R_{\tilde A^{\dagger}}$ is self-adjoint if and only if $\tilde A$ is Hermitian; for general $\tilde A$ it is not, and its adjoint is $L_{\tilde A^{\dagger}}+R_{\tilde A}$. **The temptation to call $L_{\tilde A}+R_{\tilde A^{\dagger}}$ self-adjoint for every $\tilde A$ is the trap of this article.**

*Proof.* $S_{\tilde A,\tilde B}^{*}=S_{\tilde A^{\dagger},\tilde B^{\dagger}}$ equals $S_{\tilde A,\tilde B}$ iff $\tilde A^{\dagger}=\tilde A$ and $\tilde B^{\dagger}=\tilde B$. The Lyapunov case: $S_{\tilde A,\tilde A^{\dagger}}^{*}=S_{\tilde A^{\dagger},\tilde A}$, which equals $S_{\tilde A,\tilde A^{\dagger}}$ iff $\tilde A=\tilde A^{\dagger}$. Verified on random, Hermitian and anti-Hermitian samples.

**Corollary (the anticommutator spectrum in the Hermitian case).** For Hermitian $\tilde A$ the operator $L_{\tilde A}+R_{\tilde A}$ is self-adjoint with the real spectrum $\{2\lambda_{1},\ \lambda_{1}+\lambda_{2},\ \lambda_{1}+\lambda_{2},\ 2\lambda_{2}\}$: the two **doubled** eigenvalues $2\lambda_{i}$ and the **sum** $\lambda_{1}+\lambda_{2}$ counted twice. Consequently: if $\tilde A$ is definite the anticommutator operator is definite with the sign of $\tilde A$; if $\tilde A$ is indefinite it has eigenvalues of both signs and is never definite; and it is **singular** exactly when $\lambda_{1}+\lambda_{2}=0$, that is, exactly when the Hermitian and indefinite $\tilde A$ has trace zero. Verified numerically. The same computation for the sandwich gives the products $\lambda_{i}\lambda_{j}$ and the signature $(p^{2}+q^{2},2pq)$ of *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*: the anticommutator uses the **sums** and the sandwich the **products** of the eigenvalues, and the two patterns must not be interchanged.

## The Commutator, the Anticommutator and the Derivation

**Theorem (the commutator laws).** For all $\tilde A,\tilde B$,

$$
[L_{\tilde A},L_{\tilde B}]=L_{[\tilde A,\tilde B]},\qquad [R_{\tilde A},R_{\tilde B}]=-R_{[\tilde A,\tilde B]},\qquad [L_{\tilde A},R_{\tilde B}]=0 .
$$

*Proof.* $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ and $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$ from the composition laws, and $L$ and $R$ commute because left and right multiplication commute. Verified as matrices.

**Corollary (the inner derivation is a Lie algebra homomorphism).** The map $\tilde A\mapsto\mathrm{ad}_{\tilde A}=L_{\tilde A}-R_{\tilde A}$ is a representation of the Lie algebra of $\mathbb{B}$ on $\mathbb{B}$,

$$
[\mathrm{ad}_{\tilde A},\mathrm{ad}_{\tilde B}]=\mathrm{ad}_{[\tilde A,\tilde B]},\qquad\text{that is}\qquad [L_{\tilde A}-R_{\tilde A},\ L_{\tilde B}-R_{\tilde B}]=L_{[\tilde A,\tilde B]}-R_{[\tilde A,\tilde B]},
$$

and $\mathrm{ad}_{\tilde A}$ is a derivation of the associative algebra, $\mathrm{ad}_{\tilde A}(XY)=\mathrm{ad}_{\tilde A}(X)Y+X\,\mathrm{ad}_{\tilde A}(Y)$. Its spectrum is the set of pairwise differences $\lambda_{i}-\lambda_{j}$: for Hermitian $\tilde A$ these are the real **roots** and $\mathrm{ad}_{\tilde A}$ is the infinitesimal generator of the inner automorphism group. Both statements verified numerically. This is the operator form of *Biquaternion Automorphisms and Derivations*.

**Theorem (adjointness of the commutator and the anticommutator).** For $\tilde A\in\mathbb{B}$:

1. $(\mathrm{ad}_{\tilde A})^{*}=\mathrm{ad}_{\tilde A^{\dagger}}$; hence the inner derivation $\mathrm{ad}_{\tilde A}=L_{\tilde A}-R_{\tilde A}$ is **self-adjoint** exactly when $\tilde A$ is Hermitian and **skew-adjoint** exactly when $\tilde A$ is anti-Hermitian;
2. the anticommutator operator $L_{\tilde A}+R_{\tilde A}$ is **self-adjoint** exactly when $\tilde A$ is Hermitian.

*Proof.* $(L_{\tilde A}+R_{\tilde A})^{*}=L_{\tilde A^{\dagger}}+R_{\tilde A^{\dagger}}$, which equals $L_{\tilde A}+R_{\tilde A}$ iff $\tilde A^{\dagger}=\tilde A$ for (2); the same computation with the relative sign gives $(\mathrm{ad}_{\tilde A})^{*}=\mathrm{ad}_{\tilde A^{\dagger}}$ for (1). Both verified numerically on random, Hermitian and anti-Hermitian samples.

**Remark (the sector reading).** The two statements are the sector decomposition at the operator level: the **anticommutator** is the self-adjoint operator of the **Hermitian** elements, and the **commutator** is the skew-adjoint operator of the **anti-Hermitian** elements. Since $e_{k}\in\mathbb{M}_-$ for $k=1,2,3$, the derivations $\mathrm{ad}_{e_{k}}$ are skew-adjoint with purely imaginary spectra, and $\exp(\mathrm{ad}_{e_{k}})$ are rotations, of period $\pi$ because the elementary rotation is at half-angle: this is the operator form of the compact internal group of *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*.

## The Solution

**Theorem (the Kronecker solution).** When $S_{\tilde A,\tilde B}$ is invertible, the solution of $\tilde AX+X\tilde B=c$ is $X=\mathrm{vec}^{-1}\bigl((\Phi(\tilde A)\otimes I+I\otimes\Phi(\tilde B)^{T})^{-1}\,\mathrm{vec}(c)\bigr)$, and in a basis diagonalising both parameters simultaneously (when they commute and are separately diagonalisable) it is the entrywise formula

$$
X_{ij} = \frac{c_{ij}}{\lambda_{i}+\mu_{j}} .
$$

*Proof.* The vectorised equation is a linear system with matrix $\Phi(\tilde A)\otimes I+I\otimes\Phi(\tilde B)^{T}$; the diagonal case is the $2\times2$ instance of it. Verified by solving the system and substituting.

**Theorem (the integral representation).** Let $\tilde A,\tilde B$ have spectra in the open right half-plane (so that $\exp(-t\tilde A)$ and $\exp(-t\tilde B)$ decay). Then

$$
X = \int_{0}^{\infty} e^{-t\tilde A}\,c\,e^{-t\tilde B}\,dt
$$

is the solution of $\tilde AX+X\tilde B=c$.

*Proof.* Differentiate: $\tilde AX+X\tilde B=\int_{0}^{\infty}\bigl(\tilde A e^{-t\tilde A}ce^{-t\tilde B}+e^{-t\tilde A}ce^{-t\tilde B}\tilde B\bigr)dt=-\int_{0}^{\infty}\frac{d}{dt}\bigl(e^{-t\tilde A}ce^{-t\tilde B}\bigr)dt=e^{0}ce^{0}=c$. The diagonal positive case was verified numerically, and the invertible case by substitution.

**Remark (why the Hermitian case is the interesting one).** For Hermitian $\tilde A,\tilde B$ the operator is self-adjoint and the equation is the **operator form of the Hermitian condition**: it is the equation satisfied by the fixed point of the linear relaxation $X\mapsto c-\tilde AX-X\tilde B$, by the correction term of any perturbative expansion, and by the solution of the Lyapunov problem of linear systems theory. The integral representation is the statement that the solution is a **time-ordered average** of the two exponential factors, and it is the reason the solution of a stable equation is written with two decaying exponentials rather than one.

## Worked Examples

**The identity.** $\tilde A=\tilde B=e_{0}$: $S=X+X=2X$, invertible, solution $X=c/2$. The spectrum is $\{2,2,2,2\}$ and $\det(S)=16$, as the formula gives.

**The singular Hermitian case.** For the Hermitian element $ie_{3}$ (the matrix $\sigma_{3}$, eigenvalues $\{1,-1\}$ and inertia $(1,1)$): the anticommutator operator $L_{ie_{3}}+R_{ie_{3}}$ is self-adjoint with the real spectrum $\{2,0,0,-2\}$ and it is **singular**, because the two opposite eigenvalues $1$ and $-1$ give the vanishing sum. The homogeneous equation $ie_{3}X+Xie_{3}=0$ has the two-dimensional solution space spanned by the off-diagonal matrix units $E_{12}$ and $E_{21}$: the anticommutator is not invertible exactly for the indefinite Hermitian elements with opposite eigenvalues, which is the exact algebraic statement of the failure of the Hermitian Sylvester equation in that case.

**The Lyapunov operator of an anti-Hermitian element.** For $\tilde A=e_{3}$ (anti-Hermitian, $e_{3}^{\dagger}=-e_{3}$) the operator $L_{\tilde A}+R_{\tilde A^{\dagger}}=L_{e_{3}}-R_{e_{3}}=\mathrm{ad}_{e_{3}}$ is the inner derivation, and it is **not** self-adjoint but skew-adjoint, with the purely imaginary spectrum $\{0,2i,-2i,0\}$. This is the trap of the article in its sharpest form: $L_{\tilde A}+R_{\tilde A^{\dagger}}$ looks symmetric in its two factors and is skew-adjoint for an anti-Hermitian $\tilde A$.

**The derivation of the internal rotation.** $\mathrm{ad}_{e_{3}}$ has the spectrum $\{0,2i,-2i,0\}$, the pairwise differences of the eigenvalues $\{i,-i\}$ of $\Phi(e_{3})$: the two roots $\pm2i$ are the weights of the derivation on the off-diagonal entries and the two zeros are the diagonal weights. Since $e_{3}\in\mathbb{M}_-$ the derivation is skew-adjoint and $\exp(\mathrm{ad}_{e_{3}})$ is a rotation of period $\pi$, the internal rotation group generated by $e_{3}$ at half-angle.

**The commutator with $e_{0}$.** $\mathrm{ad}_{e_{0}}=L_{e_{0}}-R_{e_{0}}=0$: the identity generates no inner derivation, and consistently the central elements have zero pairwise differences. More generally $\mathrm{ad}_{\tilde A}=0$ exactly for the central $\tilde A$.

## Summary

The Sylvester equation $\tilde AX+X\tilde B=c$ on the biquaternion algebra is the equation of the operator $S_{\tilde A,\tilde B}=L_{\tilde A}+R_{\tilde B}$, whose spectrum is the set of pairwise sums $\lambda_{i}+\mu_{j}$ and whose determinant is their product; it is uniquely solvable exactly when no eigenvalue of $\tilde A$ is the negative of an eigenvalue of $\tilde B$, and in the Hermitian case exactly when the two Hermitian parameters have no opposite eigenvalues. The adjoint is $S_{\tilde A,\tilde B}^{*}=L_{\tilde A^{\dagger}}+R_{\tilde B^{\dagger}}$, so $S_{\tilde A,\tilde B}$ is self-adjoint exactly when **both** parameters are Hermitian — in particular the Lyapunov operator $L_{\tilde A}+R_{\tilde A^{\dagger}}$ is self-adjoint only for Hermitian $\tilde A$, which is the trap of the article. The companion operator $L_{\tilde A}-R_{\tilde A}$ is the inner derivation $\mathrm{ad}_{\tilde A}=[\tilde A,\cdot\,]$, with spectrum the pairwise differences $\lambda_{i}-\lambda_{j}$, skew-adjoint exactly for the anti-Hermitian parameters, and a Lie algebra homomorphism $\tilde A\mapsto\mathrm{ad}_{\tilde A}$; the anticommutator is self-adjoint exactly for the Hermitian parameters. The solution is given by the Kronecker inverse, by the entrywise formula $X_{ij}=c_{ij}/(\lambda_{i}+\mu_{j})$ in the diagonalisable case, and by the time-ordered integral $\int_{0}^{\infty}e^{-t\tilde A}ce^{-t\tilde B}dt$ in the stable case. All statements were verified to machine precision.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{\tilde A,\tilde B}=L_{\tilde A}+R_{\tilde B}$ | Sylvester operator; $X\mapsto \tilde AX+X\tilde B$ |
| $\mathrm{spec}(S_{\tilde A,\tilde B})=\{\lambda_{i}+\mu_{j}\}$ | Pairwise sums of the spectra |
| $\det(S_{\tilde A,\tilde B})=\prod_{i,j}(\lambda_{i}+\mu_{j})$ | Product of the pairwise sums |
| $S_{\tilde A,\tilde B}^{*}=S_{\tilde A^{\dagger},\tilde B^{\dagger}}$ | The adjoint; self-adjoint iff $\tilde A,\tilde B$ both Hermitian |
| $\mathrm{ad}_{\tilde A}=L_{\tilde A}-R_{\tilde A}$ | Inner derivation; spectrum $\lambda_{i}-\lambda_{j}$ |
| $\{\tilde A,\cdot\}=L_{\tilde A}+R_{\tilde A}$ | Anticommutator operator; self-adjoint iff $\tilde A$ Hermitian |
| $[L_{\tilde A},L_{\tilde B}]=L_{[\tilde A,\tilde B]}$ | Commutator law of the left multiplications |
| $X_{ij}=c_{ij}/(\lambda_{i}+\mu_{j})$ | The solution in the diagonalisable case |
| $\int_{0}^{\infty}e^{-t\tilde A}ce^{-t\tilde B}dt$ | The solution in the stable case |

## Further Reading

- *The Hermitian Sylvester Equation with Hermitian Adjoint* (`articles_maths/the-hermitian-sylvester-equation-with-hermitian-adjoint.md`), the general theory of which this is the biquaternion instance.
- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the spectral rules used throughout.
- *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/one-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the adjoints $(L_{\tilde A})^{*}=L_{\tilde A^{\dagger}}$ and the composition laws.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the sandwich, its invariants and the congruence.
- *Biquaternion Automorphisms and Derivations* (`articles_maths/biquaternion-automorphisms-and-derivations.md`), for the derivations, the roots and the exponential.
- *Self-Adjoint and Skew Operators with Hermitian Adjoint* (`articles_maths/self-adjoint-and-skew-operators-with-hermitian-adjoint.md`), for the general theory of the adjoint on an operator algebra.
- *Biquaternion Lie Algebra* (`articles_maths/biquaternion-lie-algebra.md`), for the commutator, the roots and the Lie structure of the algebra.
