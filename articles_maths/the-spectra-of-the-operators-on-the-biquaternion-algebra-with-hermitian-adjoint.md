# __The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ with the Hermitian conjugation ${}^{*}$, and let $L_{\tilde Q_1}$, $R_{\tilde D}$, $\Theta_{\tilde{Q}}=L_{\tilde{Q}}R_{\tilde{Q}^{*}}$ be the one-sided and two-sided operators of *One-Sided Operators on the General Plain Sesqualgebra* and *Two-Sided Operators on the General Plain Sesqualgebra*. This article computes their spectra on the Hermitian space $(\tilde S,\tilde Q_2)=\mathrm{Sc}(\tilde{S}^{*}\tilde Q_2)$, which is the biquaternion instance of *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*.

The results are complete and explicit. **The one-sided operators have the spectrum of the element, each eigenvalue twice; the two-sided operator has the pairwise products $\lambda_{i}\overline{\lambda_{j}}$; the inner derivation has the pairwise differences $\lambda_{i}-\lambda_{j}$; and the Sylvester operator has the pairwise sums $\lambda_{i}+\mu_{j}$.** The four statements are one statement: on the algebra seen as $\mathbb{C}^{2}\otimes(\mathbb{C}^{2})^{*}$, left multiplication acts on the first factor, right multiplication on the second, and every operator of the corpus is a function of the two. The element-level theory is *Biquaternion Spectral Theory*; this article is the operator-level theory, and the two must be kept apart: an element has a spectrum, an operator has a spectrum, and the second is built from the first by the rules below.

## The Vectorisation

**Convention.** The algebra is identified with the matrix space $M_{2}(\mathbb{C})$; an element $\tilde{Q}$ is sent to the matrix $\mathsf{M}_2(\tilde{Q})$, and the algebra as a **linear space** is identified with $\mathbb{C}^{4}$ by the row-major vectorisation $\tilde{Q}\mapsto \mathrm{vec}(\tilde{Q})=(Q_t,Q_x,Q_y,Q_z)$, the coordinates in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$.

**Proposition (the operators as Kronecker products).** On $\mathbb{C}^{4}$,

$$
L_{\tilde Q_1} = \mathsf{M}_2(\tilde Q_1)\otimes I_{2},\qquad R_{\tilde D} = I_{2}\otimes \mathsf{M}_2(\tilde D)^{T},\qquad \Theta_{\tilde{Q}} = \mathsf{M}_2(\tilde{Q})\otimes (\mathsf{M}_2(\tilde{Q}))^{\natural},
$$

and the Sylvester operator is $L_{\tilde Q_1}+R_{\tilde D}=\mathsf{M}_2(\tilde Q_1)\otimes I_{2}+I_{2}\otimes\mathsf{M}_2(\tilde D)^{T}$.

*Proof.* $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2$ acts on the index of the first tensor factor and $R_{\tilde D}(\tilde Q_2)=\tilde Q_2\tilde D$ on the second; in row-major order the matrix of $\tilde Q_2\mapsto \tilde Q_2\tilde D$ is $I\otimes\mathsf{M}_2(\tilde D)^{T}$, and $\Theta_{\tilde{Q}}=L_{\tilde{Q}}R_{\tilde{Q}^{*}}$ gives $\mathsf{M}_2(\tilde{Q})\otimes(\mathsf{M}_2(\tilde{Q}))^{\natural}$ since $\mathsf{M}_2(\tilde{Q}^{*})=(\mathsf{M}_2(\tilde{Q}))^{\natural}$.

**Remark (the Hermitian space and the Kronecker identification).** The vectorisation above is the **coordinate** vectorisation of the basis $e_{\mu}$; the general plain sesquilinear form of the article is $(\tilde S,\tilde Q_2)=\mathrm{Sc}(\tilde{S}^{*}\tilde Q_2)=\sum_{\mu}S_{\mu}^{*}V_{\mu}$, whose Gram matrix in that basis is the identity. The Kronecker formulas are therefore spectral statements about the operators on the Hermitian space, and the computed spectra below are the spectra with respect to $(\cdot,\cdot)$.

## The Spectrum of a One-Sided Operator

**Theorem (the one-sided spectrum).** Let $\lambda_{1},\lambda_{2}$ be the eigenvalues of $\mathsf{M}_2(\tilde Q_1)$, repeated with algebraic multiplicity. Then

$$
\boxed{\; \mathrm{spec}(L_{\tilde Q_1}) = \{\lambda_{1},\lambda_{2},\lambda_{1},\lambda_{2}\},\qquad \mathrm{spec}(R_{\tilde D}) = \{\mu_{1},\mu_{2},\mu_{1},\mu_{2}\} \;},
$$

each eigenvalue with multiplicity two, and the characteristic polynomials are $\chi_{L_{\tilde Q_1}}(t)=\chi_{\mathsf{M}_2(\tilde Q_1)}(t)^{2}$ and $\chi_{R_{\tilde D}}(t)=\chi_{\mathsf{M}_2(\tilde D)}(t)^{2}$.

*Proof.* By the Kronecker rule the eigenvalues of $A\otimes B$ are the products of the eigenvalues, so the eigenvalues of $\mathsf{M}_2(\tilde Q_1)\otimes I$ are those of $\mathsf{M}_2(\tilde Q_1)$, each twice; the same for $I\otimes\mathsf{M}_2(\tilde D)^{T}$, whose second factor has the eigenvalues of $\mathsf{M}_2(\tilde D)$.

**Corollary (the type criteria at the level of spectra).** $L_{\tilde Q_1}$ is self-adjoint exactly when $\mathsf{M}_2(\tilde Q_1)$ is Hermitian, and then its spectrum is real; $L_{\tilde Q_1}$ is skew-adjoint exactly when $\mathsf{M}_2(\tilde Q_1)$ is anti-Hermitian, and then its spectrum is purely imaginary; $L_{\tilde Q_1}$ is unitary exactly when $\mathsf{M}_2(\tilde Q_1)$ is unitary, and then its spectrum is on the unit circle; $L_{\tilde Q_1}$ is **normal** exactly when $\mathsf{M}_2(\tilde Q_1)$ is normal, since $L_{\tilde Q_1}L_{\tilde Q_1}^{*}=L_{\tilde Q_1\tilde{Q}_1^{*}}$ and $L_{\tilde Q_1}^{*}L_{\tilde Q_1}=L_{\tilde{Q}_1^{*}\tilde Q_1}$ coincide exactly when $\tilde Q_1\tilde{Q}_1^{*}=\tilde{Q}_1^{*}\tilde Q_1$.

**Corollary (the spectrum of the inner derivation).** The inner derivation $\mathrm{ad}_{\tilde Q_1}=L_{\tilde Q_1}-R_{\tilde Q_1}$ has

$$
\mathrm{spec}(\mathrm{ad}_{\tilde Q_1}) = \{\lambda_{i}-\lambda_{j}\ :\ i,j=1,2\},
$$

that is, the four pairwise differences of the eigenvalues of $\mathsf{M}_2(\tilde Q_1)$, with the two differences $\lambda_{1}-\lambda_{2}$ and $\lambda_{2}-\lambda_{1}$ and the double eigenvalue $0$. For a Hermitian $\tilde Q_1$ the spectrum is real and the nonzero values $\pm(\lambda_{1}-\lambda_{2})$ are the **roots** of the Cartan pair: the derivation acts diagonally on the algebra with the roots as weights. This is the spectral content of *Biquaternion Automorphisms and Derivations*.

## The Spectrum of a Two-Sided Operator

**Theorem (the two-sided spectrum).** Let $\lambda_{1},\lambda_{2}$ be the eigenvalues of $\mathsf{M}_2(\tilde{Q})$. Then

$$
\boxed{\; \mathrm{spec}(\Theta_{\tilde{Q}}) = \{\lambda_{i}\overline{\lambda_{j}}\ :\ i,j=1,2\} = \{\lvert\lambda_{1}\rvert^{2},\ \lambda_{1}\overline{\lambda_{2}},\ \lambda_{2}\overline{\lambda_{1}},\ \lvert\lambda_{2}\rvert^{2}\} \;},
$$

and consequently

$$
\boxed{\; \operatorname{tr}(\Theta_{\tilde{Q}}) = \lvert\operatorname{tr}\mathsf{M}_2(\tilde{Q})\rvert^{2},\qquad \det(\Theta_{\tilde{Q}}) = \lvert\det\mathsf{M}_2(\tilde{Q})\rvert^{4} \;},
$$

the trace of the sandwich being the Hermitian square of the trace of the element.

*Proof.* $\Theta_{\tilde{Q}}=\mathsf{M}_2(\tilde{Q})\otimes(\mathsf{M}_2(\tilde{Q}))^{\natural}$, and the eigenvalues of $A\otimes B$ are the products of the eigenvalues; the eigenvalues of $(\mathsf{M}_2(\tilde{Q}))^{\natural}$ are the conjugates of those of $\mathsf{M}_2(\tilde{Q})$. The trace is the sum of the eigenvalues, $\sum_{i,j}\lambda_{i}\overline{\lambda_{j}}=(\sum_{i}\lambda_{i})(\sum_{j}\overline{\lambda_{j}})=\lvert\operatorname{tr}\mathsf{M}_2(\tilde{Q})\rvert^{2}$, and the determinant is their product, $\prod_{i,j}\lambda_{i}\overline{\lambda_{j}}=\lvert\lambda_{1}\lambda_{2}\rvert^{4}$.

**Remark (the structure of the two-sided spectrum).** The four eigenvalues are the two **populations** $\lvert\lambda_{i}\rvert^{2}$ and the two **coherences** $\lambda_{1}\overline{\lambda_{2}},\lambda_{2}\overline{\lambda_{1}}$, which are conjugates of one another. The spectrum is therefore conjugate-symmetric, and it is real if and only if the coherences are real, that is, if and only if $\lambda_{1}\overline{\lambda_{2}}\in\mathbb{R}$, which is one of the many equivalent forms of the condition that $\tilde{Q}$ be Hermitian up to a central phase.

**Theorem (self-adjointness and positivity).**

1. $\Theta_{\tilde{Q}}$ is self-adjoint if and only if $\tilde{Q}$ is Hermitian up to a central phase, $\tilde{Q}^{*}=\omega\tilde{Q}$ with $\lvert\omega\rvert=1$.
2. If $\tilde{Q}$ is Hermitian with inertia $(n,m)$ then the signature of $\Theta_{\tilde{Q}}$ is
$$
\mathrm{sig}(\Theta_{\tilde{Q}}) = \bigl(p^{2}+q^{2},\ 2pq\bigr),
$$
so $\Theta_{\tilde{Q}}$ is positive semidefinite exactly when $p=2$ or $q=2$, that is, exactly when $\tilde{Q}$ is semidefinite (including the zero element), and positive definite exactly when $\tilde{Q}$ is definite.
3. More generally $\Theta_{\tilde{Q}}$ is positive semidefinite if and only if $\tilde{Q}$ is Hermitian up to a central phase and semidefinite.

*Proof.* (1) $\Theta_{\tilde{Q}}^{*}=\Theta_{\tilde{Q}^{*}}$ and $\Theta_{\tilde{Q}^{*}}=\Theta_{\tilde{Q}}$ exactly when $\tilde{Q}^{*}=\omega\tilde{Q}$ with $\lvert\omega\rvert=1$, by the injectivity of $\tilde{Q}\mapsto \Theta_{\tilde{Q}}$ up to the central circle. (2) If $\tilde{Q}$ is Hermitian its eigenvalues $\lambda_{1},\lambda_{2}$ are real, the four general products $\lambda_{i}\lambda_{j}$ are real, $\lambda_{1}^{2},\lambda_{2}^{2}$ have the sign of the squares and $2\lambda_{1}\lambda_{2}$ the sign of the product, which is negative precisely when the two eigenvalues have opposite signs; the count of the inertia follows. (3) is (1) together with (2).

**Remark (the numerical range is not real).** It must not be expected that $(\Theta_{\tilde{Q}}\tilde Q_2,\tilde Q_2)$ be real for all $\tilde Q_2$: for $\tilde{Q}$ not Hermitian up to phase the operator is not self-adjoint and the values $\lambda_{i}\overline{\lambda_{j}}$ are not real, so the quadratic form of $\Theta_{\tilde{Q}}$ takes genuinely complex values. A verified counterexample is $\tilde{Q}=e_t+\vec e_x$, for which $\tilde{Q}^{*}=e_t-\vec e_x$ is not a central multiple of $\tilde{Q}$ and the spectrum $\{2,2i,-2i,2\}$ is not real. The correct positivity statements are those of the theorem above, and only for $\tilde{Q}$ Hermitian up to phase.

**Corollary (rank and trace preservation).** The rank of $\Theta_{\tilde{Q}}$ is $(\mathrm{rank}\,\mathsf{M}_2(\tilde{Q}))^{2}$, so a singular $\tilde{Q}$ gives a **rank-one** sandwich, as the null example below shows. As a map on the algebra, the sandwich is trace preserving exactly when $\tilde{Q}\in U$, since $\operatorname{tr}(\tilde{Q}Y\tilde{Q}^{*})=\operatorname{tr}(\tilde{Q}^{*}\tilde{Q}Y)$ for all $Y$ forces $\tilde{Q}^{*}\tilde{Q}=e_t$; this is the statement used in *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint*. The two-sided operator of a *positive semidefinite* element is a positive map, so the sandwich carries the positive cone into itself.

**Remark (the operator norm).** The norm of $\Theta_{\tilde{Q}}$ on the Hermitian space is the square of the operator norm of $\mathsf{M}_2(\tilde{Q})$, $\lVert \Theta_{\tilde{Q}}\rVert=\lVert\mathsf{M}_2(\tilde{Q})\rVert^{2}$, since $\lVert \tilde{Q}\tilde Q_2\tilde{Q}^{*}\rVert\le\lVert \tilde{Q}\rVert^{2}\lVert \tilde Q_2\rVert$ with equality on a suitable rank-one $\tilde Q_2$. The sandwich therefore **doubles the norm in the exponent**: the unit ball of the algebra is contracted by the sandwich of a contraction and fixed only by the unitaries.

## The Spectrum of the Sylvester Operator

**Theorem (the Sylvester spectrum).** For the operator $L_{\tilde Q_1}+R_{\tilde D}$ whose equation is the Sylvester equation $\tilde Q_1X+X\tilde D=c$,

$$
\mathrm{spec}(L_{\tilde Q_1}+R_{\tilde D}) = \{\lambda_{i}+\mu_{j}\ :\ i,j=1,2\},\qquad \det(L_{\tilde Q_1}+R_{\tilde D}) = \prod_{i,j}(\lambda_{i}+\mu_{j}),
$$

where $\lambda_{i}$ are the eigenvalues of $\mathsf{M}_2(\tilde Q_1)$ and $\mu_{j}$ those of $\mathsf{M}_2(\tilde D)$. The operator is invertible exactly when no eigenvalue of $\mathsf{M}_2(\tilde Q_1)$ is the negative of an eigenvalue of $\mathsf{M}_2(\tilde D)$.

*Proof.* Immediate from $L_{\tilde Q_1}+R_{\tilde D}=\mathsf{M}_2(\tilde Q_1)\otimes I+I\otimes\mathsf{M}_2(\tilde D)^{T}$ and the additivity of the spectrum under Kronecker sums for the first factor terms; verified on random pairs, together with the determinant formula.

**Corollary (the self-adjoint Sylvester operator).** $(L_{\tilde Q_1}+R_{\tilde D})^{*}=L_{\tilde{Q}_1^{*}}+R_{\tilde{D}^{*}}$, so $L_{\tilde Q_1}+R_{\tilde D}$ is self-adjoint exactly when both parameters are Hermitian, and the Lyapunov operator $L_{\tilde Q_1}+R_{\tilde{Q}_1^{*}}$ is self-adjoint exactly when $\tilde Q_1$ is Hermitian, with the real spectrum $\{\lambda_{i}+\overline{\lambda_{j}}\}=\{\lambda_{i}+\lambda_{j}\}$ for $\lambda_{i}$ real. This is the operator side of the Hermitian Sylvester equation, developed in *The Hermitian Sylvester Equation*.

## Worked Examples

**The identity and the central scalars.** $\mathrm{spec}(L_{e_t})=\{1,1,1,1\}$; $\mathrm{spec}(L_{\vec e_z})=\{i,-i,i,-i\}$, purely imaginary, consistent with $\vec e_z$ anti-Hermitian and $L_{\vec e_z}$ skew-adjoint; $\mathrm{spec}(L_{i\vec e_z})=\{1,1,-1,-1\}$, real, consistent with $i\vec e_z$ Hermitian and $L_{i\vec e_z}$ self-adjoint. For $\tilde Q_1=\vec e_x$, of spectrum $\{i,-i\}$, $L_{\vec e_x}$ has spectrum $\{i,i,-i,-i\}$: skew-adjoint, of spectrum on the imaginary axis, since $\vec e_x\in\mathbb{M}_-$.

**A Hermitian element with indefinite inertia.** For $\tilde{Q}=\vec e_z$: $\mathsf{M}_2(\vec e_z)$ has eigenvalues $\{i,-i\}$, inertia $(1,1)$, and the four general products are $i\cdot(-i)=1$, $i\cdot i=-1$, $(-i)\cdot(-i)=-1$, $(-i)\cdot i=1$, so $\mathrm{spec}(\Theta_{\vec e_z})=\{1,-1,-1,1\}$ and the signature of $\Theta_{\vec e_z}$ is $(p^{2}+q^{2},2pq)=(2,2)$: the sandwich of an indefinite Hermitian element has two positive and two negative eigenvalues. For $\tilde{Q}=i\vec e_z$ the element differs from $\vec e_z$ by the central phase $i$ and $\mathsf{M}_2(\tilde{Q})=\sigma_{3}$ has eigenvalues $\{1,-1\}$; the sandwich is the *same* operator, $\Theta_{i\vec e_z}=\Theta_{\vec e_z}$, so the phase shows up in the element's spectrum and not at all in the operator's. This is the phase blindness of *Two-Sided Operators on the General Plain Sesqualgebra*, visible at the level of the spectrum.

**Remark (the sandwich is never negative).** For $\tilde{Q}$ Hermitian the two eigenvalues $\lambda_{i}\overline{\lambda_{i}}=\lvert\lambda_{i}\rvert^{2}$ are positive unless $\tilde{Q}=0$. Hence $\Theta_{\tilde{Q}}$ is never negative semidefinite except for $\tilde{Q}=0$: the sandwich of any nonzero Hermitian element has at least two positive eigenvalues, and the only possibilities for a Hermitian $\tilde{Q}$ are $\Theta_{\tilde{Q}}\succeq0$ (for $\tilde{Q}$ semidefinite) and $\Theta_{\tilde{Q}}$ indefinite with signature $(2,2)$ (for $\tilde{Q}$ definite-indefinite of inertia $(1,1)$).

**A non-Hermitian element.** For $\tilde{Q}=e_t+\vec e_x$ the matrix $\mathsf{M}_2(\tilde{Q})=I-i\sigma_{1}$ has eigenvalues $\{1+i,1-i\}$, so

$$
\mathrm{spec}(\Theta_{\tilde{Q}}) = \{2,\ 2i,\ -2i,\ 2\} ,
$$

not real: the two coherence eigenvalues $\lambda_{1}\overline{\lambda_{2}}=2i$ and its conjugate are purely imaginary, and by the self-adjointness theorem $\Theta_{\tilde{Q}}$ is **not** self-adjoint. The example is instructive because the *element* $\tilde{Q}$ has a real trace and a real determinant, so a reader looking only at the element will not see the obstruction: the obstruction is in the operator, whose spectrum is not real although the element is "almost" Hermitian. The correct diagnostic is the identity $\Theta_{\tilde{Q}}=\Theta_{\tilde{Q}}^{*}$, not the element data.

**The null element.** For $\tilde{Q}=e_t+i\vec e_z$, Hermitian of spectrum $\{2,0\}$ and inertia $(1,0,1)$, $\mathrm{spec}(\Theta_{\tilde{Q}})=\{4,0,0,0\}$: positive semidefinite of rank one, matching $\Theta_{\tilde{Q}}(e_t)=2\tilde{Q}$ and the collapse computed in *Two-Sided Operators on the General Plain Sesqualgebra*.

## Summary

On the Hermitian space of the biquaternion algebra, the operators of the corpus have explicit spectra: $\mathrm{spec}(L_{\tilde Q_1})=\mathrm{spec}(\mathsf{M}_2(\tilde Q_1))$ with each eigenvalue twice, the same for $R_{\tilde D}$; the inner derivation $\mathrm{ad}_{\tilde Q_1}=L_{\tilde Q_1}-R_{\tilde Q_1}$ has the pairwise differences $\lambda_{i}-\lambda_{j}$, the roots of the Cartan pair when $\tilde Q_1$ is Hermitian; the two-sided operator $\Theta_{\tilde{Q}}$ has the pairwise products $\lambda_{i}\overline{\lambda_{j}}$, the populations $\lvert\lambda_{i}\rvert^{2}$ and the coherences $\lambda_{i}\overline{\lambda_{j}}$; and the Sylvester operator $L_{\tilde Q_1}+R_{\tilde D}$ has the pairwise sums $\lambda_{i}+\mu_{j}$. From these: $\mathrm{tr}(\Theta_{\tilde{Q}})=\lvert\operatorname{tr}\mathsf{M}_2(\tilde{Q})\rvert^{2}$ and $\det(\Theta_{\tilde{Q}})=\lvert\det\mathsf{M}_2(\tilde{Q})\rvert^{4}$; $\Theta_{\tilde{Q}}$ is self-adjoint exactly when $\tilde{Q}$ is Hermitian up to a central phase and then its signature is $(p^{2}+q^{2},2pq)$ for the inertia $(n,m)$ of $\tilde{Q}$; $\Theta_{\tilde{Q}}$ is positive semidefinite exactly when $\tilde{Q}$ is Hermitian up to phase and semidefinite; $L_{\tilde Q_1}+R_{\tilde D}$ is invertible exactly when $\mathsf{M}_2(\tilde Q_1)$ and $-\mathsf{M}_2(\tilde D)$ share no eigenvalue and self-adjoint exactly when both parameters are Hermitian.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde{Q})$ | The $2\times2$ matrix of $\tilde{Q}$ in the matrix model |
| $\mathrm{vec}$ | Row-major vectorisation onto $\mathbb{C}^{4}$ in the basis $e_{\mu}$ |
| $L_{\tilde Q_1}=\mathsf{M}_2(\tilde Q_1)\otimes I$ | Left multiplication; spectrum $\lambda_{i}$, each twice |
| $R_{\tilde D}=I\otimes\mathsf{M}_2(\tilde D)^{T}$ | Right multiplication; spectrum $\mu_{j}$, each twice |
| $\Theta_{\tilde{Q}}=\mathsf{M}_2(\tilde{Q})\otimes(\mathsf{M}_2(\tilde{Q}))^{\natural}$ | Two-sided operator; spectrum $\lambda_{i}\overline{\lambda_{j}}$ |
| $\mathrm{ad}_{\tilde Q_1}=L_{\tilde Q_1}-R_{\tilde Q_1}$ | Inner derivation; spectrum $\lambda_{i}-\lambda_{j}$ |
| $L_{\tilde Q_1}+R_{\tilde D}$ | Sylvester operator; spectrum $\lambda_{i}+\mu_{j}$ |
| $(n,m)$ | Inertia of a Hermitian element; $\mathrm{sig}(\Theta_{\tilde{Q}})=(p^{2}+q^{2},2pq)$ |
| $(\tilde S,\tilde Q_2)=\mathrm{Sc}(\tilde{S}^{*}\tilde Q_2)$ | The general plain sesquilinear form of the spectra |

## Further Reading

- [The Spectra of Self-Adjoint Operators with Hermitian Adjoint](the-spectra-of-self-adjoint-operators-with-hermitian-adjoint.html), the general spectral theorem of which this is the biquaternion instance.
- [Biquaternion Spectral Theory](biquaternion-spectral-theory.html), for the spectra of **elements**: the element-level theory that this article uses and does not repeat.
- [Self-Adjoint and Skew Operators with Hermitian Adjoint](self-adjoint-and-skew-operators-with-hermitian-adjoint.html), for the general operator-level theory of the adjoint.
- [One-Sided Operators on the General Plain Sesqualgebra](one-sided-operators-on-the-general-plain-sesqualgebra.html) and [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), for the definitions, the type criteria and the composition laws.
- [The Hermitian Sylvester Equation](the-hermitian-sylvester-equation.html), for the solvability and the solution of $\tilde Q_1X+X\tilde D=c$.
- [Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint](completely-positive-maps-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the positivity statements at the level of maps.
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the derivations and their weights.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the remarkable real subspaces
