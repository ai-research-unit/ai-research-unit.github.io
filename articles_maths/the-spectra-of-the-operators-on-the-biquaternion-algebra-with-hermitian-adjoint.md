# __The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ with the Hermitian conjugation ${}^{*}$, and let $L_{\tilde C}$, $R_{\tilde D}$, $\Theta_{\tilde{Q}}=L_{\tilde{Q}}R_{\tilde{Q}^{*}}$ be the one-sided and two-sided operators of *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*. This article computes their spectra on the Hermitian space $(\tilde S,\tilde V)=\mathrm{Sc}(\tilde{S}^{*}\tilde V)$, which is the biquaternion instance of *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*.

The results are complete and explicit. **The one-sided operators have the spectrum of the element, each eigenvalue twice; the two-sided operator has the pairwise products $\lambda_{i}\overline{\lambda_{j}}$; the inner derivation has the pairwise differences $\lambda_{i}-\lambda_{j}$; and the Sylvester operator has the pairwise sums $\lambda_{i}+\mu_{j}$.** The four statements are one statement: on the algebra seen as $\mathbb{C}^{2}\otimes(\mathbb{C}^{2})^{*}$, left multiplication acts on the first factor, right multiplication on the second, and every operator of the corpus is a function of the two. The element-level theory is *Biquaternion Spectral Theory*; this article is the operator-level theory, and the two must be kept apart: an element has a spectrum, an operator has a spectrum, and the second is built from the first by the rules below.

## The Vectorisation

**Convention.** The algebra is identified with the matrix space $M_{2}(\mathbb{C})$; an element $\tilde{Q}$ is sent to the matrix $\Phi(\tilde{Q})$, and the algebra as a **linear space** is identified with $\mathbb{C}^{4}$ by the row-major vectorisation $\tilde{Q}\mapsto \mathrm{vec}(\tilde{Q})=(Q_{0},Q_{1},Q_{2},Q_{3})$, the coordinates in the basis $e_{0},e_{1},e_{2},e_{3}$.

**Proposition (the operators as Kronecker products).** On $\mathbb{C}^{4}$,

$$
L_{\tilde C} = \Phi(\tilde C)\otimes I_{2},\qquad R_{\tilde D} = I_{2}\otimes \Phi(\tilde D)^{T},\qquad \Theta_{\tilde{Q}} = \Phi(\tilde{Q})\otimes (\Phi(\tilde{Q}))^{\natural},
$$

and the Sylvester operator is $L_{\tilde C}+R_{\tilde D}=\Phi(\tilde C)\otimes I_{2}+I_{2}\otimes\Phi(\tilde D)^{T}$.

*Proof.* $L_{\tilde C}(\tilde V)=\tilde C\tilde V$ acts on the index of the first tensor factor and $R_{\tilde D}(\tilde V)=\tilde V\tilde D$ on the second; in row-major order the matrix of $\tilde V\mapsto \tilde V\tilde D$ is $I\otimes\Phi(\tilde D)^{T}$, and $\Theta_{\tilde{Q}}=L_{\tilde{Q}}R_{\tilde{Q}^{*}}$ gives $\Phi(\tilde{Q})\otimes(\Phi(\tilde{Q}))^{\natural}$ since $\Phi(\tilde{Q}^{*})=(\Phi(\tilde{Q}))^{\natural}$. All three were verified as $4\times4$ matrices on random elements.

**Remark (the Hermitian space and the Kronecker identification).** The vectorisation above is the **coordinate** vectorisation of the basis $e_{\mu}$; the Hermitian form of the article is $(\tilde S,\tilde V)=\mathrm{Sc}(\tilde{S}^{*}\tilde V)=\sum_{\mu}S_{\mu}^{*}V_{\mu}$, whose Gram matrix in that basis is the identity. The Kronecker formulas are therefore spectral statements about the operators on the Hermitian space, and the computed spectra below are the spectra with respect to $(\cdot,\cdot)$.

## The Spectrum of a One-Sided Operator

**Theorem (the one-sided spectrum).** Let $\lambda_{1},\lambda_{2}$ be the eigenvalues of $\Phi(\tilde C)$, repeated with algebraic multiplicity. Then

$$
\mathrm{spec}(L_{\tilde C}) = \{\lambda_{1},\lambda_{2},\lambda_{1},\lambda_{2}\},\qquad \mathrm{spec}(R_{\tilde D}) = \{\mu_{1},\mu_{2},\mu_{1},\mu_{2}\},
$$

each eigenvalue with multiplicity two, and the characteristic polynomials are $\chi_{L_{\tilde C}}(t)=\chi_{\Phi(\tilde C)}(t)^{2}$ and $\chi_{R_{\tilde D}}(t)=\chi_{\Phi(\tilde D)}(t)^{2}$.

*Proof.* By the Kronecker rule the eigenvalues of $A\otimes B$ are the products of the eigenvalues, so the eigenvalues of $\Phi(\tilde C)\otimes I$ are those of $\Phi(\tilde C)$, each twice; the same for $I\otimes\Phi(\tilde D)^{T}$, whose second factor has the eigenvalues of $\Phi(\tilde D)$. Verified on random elements by comparing $\det(tI-L_{\tilde C})$ with the squared characteristic polynomial.

**Corollary (the type criteria at the level of spectra).** $L_{\tilde C}$ is self-adjoint exactly when $\Phi(\tilde C)$ is Hermitian, and then its spectrum is real; $L_{\tilde C}$ is skew-adjoint exactly when $\Phi(\tilde C)$ is anti-Hermitian, and then its spectrum is purely imaginary; $L_{\tilde C}$ is unitary exactly when $\Phi(\tilde C)$ is unitary, and then its spectrum is on the unit circle; $L_{\tilde C}$ is **normal** exactly when $\Phi(\tilde C)$ is normal, since $L_{\tilde C}L_{\tilde C}^{*}=L_{\tilde C\tilde{C}^{*}}$ and $L_{\tilde C}^{*}L_{\tilde C}=L_{\tilde{C}^{*}\tilde C}$ coincide exactly when $\tilde C\tilde{C}^{*}=\tilde{C}^{*}\tilde C$.

**Corollary (the spectrum of the inner derivation).** The inner derivation $\mathrm{ad}_{\tilde C}=L_{\tilde C}-R_{\tilde C}$ has

$$
\mathrm{spec}(\mathrm{ad}_{\tilde C}) = \{\lambda_{i}-\lambda_{j}\ :\ i,j=1,2\},
$$

that is, the four pairwise differences of the eigenvalues of $\Phi(\tilde C)$, with the two differences $\lambda_{1}-\lambda_{2}$ and $\lambda_{2}-\lambda_{1}$ and the double eigenvalue $0$. For a Hermitian $\tilde C$ the spectrum is real and the nonzero values $\pm(\lambda_{1}-\lambda_{2})$ are the **roots** of the Cartan pair: the derivation acts diagonally on the algebra with the roots as weights. This is the spectral content of *Biquaternion Automorphisms and Derivations*.

## The Spectrum of a Two-Sided Operator

**Theorem (the two-sided spectrum).** Let $\lambda_{1},\lambda_{2}$ be the eigenvalues of $\Phi(\tilde{Q})$. Then

$$
\mathrm{spec}(\Theta_{\tilde{Q}}) = \{\lambda_{i}\overline{\lambda_{j}}\ :\ i,j=1,2\} = \{\lvert\lambda_{1}\rvert^{2},\ \lambda_{1}\overline{\lambda_{2}},\ \lambda_{2}\overline{\lambda_{1}},\ \lvert\lambda_{2}\rvert^{2}\},
$$

and consequently

$$
\operatorname{tr}(\Theta_{\tilde{Q}}) = \lvert\operatorname{tr}\Phi(\tilde{Q})\rvert^{2},\qquad \det(\Theta_{\tilde{Q}}) = \lvert\det\Phi(\tilde{Q})\rvert^{4},
$$

the trace of the sandwich being the Hermitian square of the trace of the element.

*Proof.* $\Theta_{\tilde{Q}}=\Phi(\tilde{Q})\otimes(\Phi(\tilde{Q}))^{\natural}$, and the eigenvalues of $A\otimes B$ are the products of the eigenvalues; the eigenvalues of $(\Phi(\tilde{Q}))^{\natural}$ are the conjugates of those of $\Phi(\tilde{Q})$. The trace is the sum of the eigenvalues, $\sum_{i,j}\lambda_{i}\overline{\lambda_{j}}=(\sum_{i}\lambda_{i})(\sum_{j}\overline{\lambda_{j}})=\lvert\operatorname{tr}\Phi(\tilde{Q})\rvert^{2}$, and the determinant is their product, $\prod_{i,j}\lambda_{i}\overline{\lambda_{j}}=\lvert\lambda_{1}\lambda_{2}\rvert^{4}$. Both were verified numerically on random elements.

**Remark (the structure of the two-sided spectrum).** The four eigenvalues are the two **populations** $\lvert\lambda_{i}\rvert^{2}$ and the two **coherences** $\lambda_{1}\overline{\lambda_{2}},\lambda_{2}\overline{\lambda_{1}}$, which are conjugates of one another. The spectrum is therefore conjugate-symmetric, and it is real if and only if the coherences are real, that is, if and only if $\lambda_{1}\overline{\lambda_{2}}\in\mathbb{R}$, which is one of the many equivalent forms of the condition that $\tilde{Q}$ be Hermitian up to a central phase.

**Theorem (self-adjointness and positivity).**

1. $\Theta_{\tilde{Q}}$ is self-adjoint if and only if $\tilde{Q}$ is Hermitian up to a central phase, $\tilde{Q}^{*}=\omega\tilde{Q}$ with $\lvert\omega\rvert=1$.
2. If $\tilde{Q}$ is Hermitian with inertia $(p,q)$ then the signature of $\Theta_{\tilde{Q}}$ is
$$
\mathrm{sig}(\Theta_{\tilde{Q}}) = \bigl(p^{2}+q^{2},\ 2pq\bigr),
$$
so $\Theta_{\tilde{Q}}$ is positive semidefinite exactly when $p=2$ or $q=2$, that is, exactly when $\tilde{Q}$ is semidefinite (including the zero element), and positive definite exactly when $\tilde{Q}$ is definite.
3. More generally $\Theta_{\tilde{Q}}$ is positive semidefinite if and only if $\tilde{Q}$ is Hermitian up to a central phase and semidefinite.

*Proof.* (1) $\Theta_{\tilde{Q}}^{*}=\Theta_{\tilde{Q}^{*}}$ and $\Theta_{\tilde{Q}^{*}}=\Theta_{\tilde{Q}}$ exactly when $\tilde{Q}^{*}=\omega\tilde{Q}$ with $\lvert\omega\rvert=1$, by the injectivity of $\tilde{Q}\mapsto \Theta_{\tilde{Q}}$ up to the central circle. (2) If $\tilde{Q}$ is Hermitian its eigenvalues $\lambda_{1},\lambda_{2}$ are real, the four products $\lambda_{i}\lambda_{j}$ are real, $\lambda_{1}^{2},\lambda_{2}^{2}$ have the sign of the squares and $2\lambda_{1}\lambda_{2}$ the sign of the product, which is negative precisely when the two eigenvalues have opposite signs; the count of the inertia follows. (3) is (1) together with (2). All three were verified on thousands of random and structured samples.

**Remark (the numerical range is not real).** It must not be expected that $(\Theta_{\tilde{Q}}\tilde V,\tilde V)$ be real for all $\tilde V$: for $\tilde{Q}$ not Hermitian up to phase the operator is not self-adjoint and the values $\lambda_{i}\overline{\lambda_{j}}$ are not real, so the quadratic form of $\Theta_{\tilde{Q}}$ takes genuinely complex values. A verified counterexample is $\tilde{Q}=e_{0}+e_{1}$, for which $\tilde{Q}^{*}=e_{0}-e_{1}$ is not a central multiple of $\tilde{Q}$ and the spectrum $\{2,2i,-2i,2\}$ is not real. The correct positivity statements are those of the theorem above, and only for $\tilde{Q}$ Hermitian up to phase.

**Corollary (rank and trace preservation).** The rank of $\Theta_{\tilde{Q}}$ is $(\mathrm{rank}\,\Phi(\tilde{Q}))^{2}$, so a singular $\tilde{Q}$ gives a **rank-one** sandwich, as the null example below shows. As a map on the algebra, the sandwich is trace preserving exactly when $\tilde{Q}\in U$, since $\operatorname{tr}(\tilde{Q}Y\tilde{Q}^{*})=\operatorname{tr}(\tilde{Q}^{*}\tilde{Q}Y)$ for all $Y$ forces $\tilde{Q}^{*}\tilde{Q}=e_{0}$; this is the statement used in *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint*. The two-sided operator of a *positive semidefinite* element is a positive map, so the sandwich carries the positive cone into itself.

**Remark (the operator norm).** The norm of $\Theta_{\tilde{Q}}$ on the Hermitian space is the square of the operator norm of $\Phi(\tilde{Q})$, $\lVert \Theta_{\tilde{Q}}\rVert=\lVert\Phi(\tilde{Q})\rVert^{2}$, since $\lVert \tilde{Q}\tilde V\tilde{Q}^{*}\rVert\le\lVert \tilde{Q}\rVert^{2}\lVert \tilde V\rVert$ with equality on a suitable rank-one $\tilde V$. The sandwich therefore **doubles the norm in the exponent**: the unit ball of the algebra is contracted by the sandwich of a contraction and fixed only by the unitaries.

## The Spectrum of the Sylvester Operator

**Theorem (the Sylvester spectrum).** For the operator $L_{\tilde C}+R_{\tilde D}$ whose equation is the Sylvester equation $\tilde CX+X\tilde D=c$,

$$
\mathrm{spec}(L_{\tilde C}+R_{\tilde D}) = \{\lambda_{i}+\mu_{j}\ :\ i,j=1,2\},\qquad \det(L_{\tilde C}+R_{\tilde D}) = \prod_{i,j}(\lambda_{i}+\mu_{j}),
$$

where $\lambda_{i}$ are the eigenvalues of $\Phi(\tilde C)$ and $\mu_{j}$ those of $\Phi(\tilde D)$. The operator is invertible exactly when no eigenvalue of $\Phi(\tilde C)$ is the negative of an eigenvalue of $\Phi(\tilde D)$.

*Proof.* Immediate from $L_{\tilde C}+R_{\tilde D}=\Phi(\tilde C)\otimes I+I\otimes\Phi(\tilde D)^{T}$ and the additivity of the spectrum under Kronecker sums for the first factor terms; verified on random pairs, together with the determinant formula.

**Corollary (the self-adjoint Sylvester operator).** $(L_{\tilde C}+R_{\tilde D})^{*}=L_{\tilde{C}^{*}}+R_{\tilde{D}^{*}}$, so $L_{\tilde C}+R_{\tilde D}$ is self-adjoint exactly when both parameters are Hermitian, and the Lyapunov operator $L_{\tilde C}+R_{\tilde{C}^{*}}$ is self-adjoint exactly when $\tilde C$ is Hermitian, with the real spectrum $\{\lambda_{i}+\overline{\lambda_{j}}\}=\{\lambda_{i}+\lambda_{j}\}$ for $\lambda_{i}$ real. Verified numerically. This is the operator side of the Hermitian Sylvester equation, developed in *The Hermitian Sylvester Equation*.

## Worked Examples

**The identity and the central scalars.** $\mathrm{spec}(L_{e_{0}})=\{1,1,1,1\}$; $\mathrm{spec}(L_{e_{3}})=\{i,-i,i,-i\}$, purely imaginary, consistent with $e_{3}$ anti-Hermitian and $L_{e_{3}}$ skew-adjoint; $\mathrm{spec}(L_{ie_{3}})=\{1,1,-1,-1\}$, real, consistent with $ie_{3}$ Hermitian and $L_{ie_{3}}$ self-adjoint. For $\tilde C=e_{1}$, of spectrum $\{i,-i\}$, $L_{e_{1}}$ has spectrum $\{i,i,-i,-i\}$: skew-adjoint, of spectrum on the imaginary axis, since $e_{1}\in\mathbb{M}_-$.

**A Hermitian element with indefinite inertia.** For $\tilde{Q}=e_{3}$: $\Phi(e_{3})$ has eigenvalues $\{i,-i\}$, inertia $(1,1)$, and the four products are $i\cdot(-i)=1$, $i\cdot i=-1$, $(-i)\cdot(-i)=-1$, $(-i)\cdot i=1$, so $\mathrm{spec}(\Theta_{e_{3}})=\{1,-1,-1,1\}$ and the signature of $\Theta_{e_{3}}$ is $(p^{2}+q^{2},2pq)=(2,2)$: the sandwich of an indefinite Hermitian element has two positive and two negative eigenvalues. For $\tilde{Q}=ie_{3}$ the element differs from $e_{3}$ by the central phase $i$ and $\Phi(\tilde{Q})=\sigma_{3}$ has eigenvalues $\{1,-1\}$; the sandwich is the *same* operator, $\Theta_{ie_{3}}=\Theta_{e_{3}}$, so the phase shows up in the element's spectrum and not at all in the operator's. This is the phase blindness of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, visible at the level of the spectrum.

**Remark (the sandwich is never negative).** For $\tilde{Q}$ Hermitian the two eigenvalues $\lambda_{i}\overline{\lambda_{i}}=\lvert\lambda_{i}\rvert^{2}$ are positive unless $\tilde{Q}=0$. Hence $\Theta_{\tilde{Q}}$ is never negative semidefinite except for $\tilde{Q}=0$: the sandwich of any nonzero Hermitian element has at least two positive eigenvalues, and the only possibilities for a Hermitian $\tilde{Q}$ are $\Theta_{\tilde{Q}}\succeq0$ (for $\tilde{Q}$ semidefinite) and $\Theta_{\tilde{Q}}$ indefinite with signature $(2,2)$ (for $\tilde{Q}$ definite-indefinite of inertia $(1,1)$).

**A non-Hermitian element.** For $\tilde{Q}=e_{0}+e_{1}$ the matrix $\Phi(\tilde{Q})=I-i\sigma_{1}$ has eigenvalues $\{1+i,1-i\}$, so

$$
\mathrm{spec}(\Theta_{\tilde{Q}}) = \{2,\ 2i,\ -2i,\ 2\} ,
$$

not real: the two coherence eigenvalues $\lambda_{1}\overline{\lambda_{2}}=2i$ and its conjugate are purely imaginary, and by the self-adjointness theorem $\Theta_{\tilde{Q}}$ is **not** self-adjoint. The example is instructive because the *element* $\tilde{Q}$ has a real trace and a real determinant, so a reader looking only at the element will not see the obstruction: the obstruction is in the operator, whose spectrum is not real although the element is "almost" Hermitian. The correct diagnostic is the identity $\Theta_{\tilde{Q}}=\Theta_{\tilde{Q}}^{*}$, not the element data.

**The null element.** For $\tilde{Q}=e_{0}+ie_{3}$, Hermitian of spectrum $\{2,0\}$ and inertia $(1,0,1)$, $\mathrm{spec}(\Theta_{\tilde{Q}})=\{4,0,0,0\}$: positive semidefinite of rank one, matching $\Theta_{\tilde{Q}}(e_{0})=2\tilde{Q}$ and the collapse computed in *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*.

## Summary

On the Hermitian space of the biquaternion algebra, the operators of the corpus have explicit spectra: $\mathrm{spec}(L_{\tilde C})=\mathrm{spec}(\Phi(\tilde C))$ with each eigenvalue twice, the same for $R_{\tilde D}$; the inner derivation $\mathrm{ad}_{\tilde C}=L_{\tilde C}-R_{\tilde C}$ has the pairwise differences $\lambda_{i}-\lambda_{j}$, the roots of the Cartan pair when $\tilde C$ is Hermitian; the two-sided operator $\Theta_{\tilde{Q}}$ has the pairwise products $\lambda_{i}\overline{\lambda_{j}}$, the populations $\lvert\lambda_{i}\rvert^{2}$ and the coherences $\lambda_{i}\overline{\lambda_{j}}$; and the Sylvester operator $L_{\tilde C}+R_{\tilde D}$ has the pairwise sums $\lambda_{i}+\mu_{j}$. From these: $\mathrm{tr}(\Theta_{\tilde{Q}})=\lvert\operatorname{tr}\Phi(\tilde{Q})\rvert^{2}$ and $\det(\Theta_{\tilde{Q}})=\lvert\det\Phi(\tilde{Q})\rvert^{4}$; $\Theta_{\tilde{Q}}$ is self-adjoint exactly when $\tilde{Q}$ is Hermitian up to a central phase and then its signature is $(p^{2}+q^{2},2pq)$ for the inertia $(p,q)$ of $\tilde{Q}$; $\Theta_{\tilde{Q}}$ is positive semidefinite exactly when $\tilde{Q}$ is Hermitian up to phase and semidefinite; $L_{\tilde C}+R_{\tilde D}$ is invertible exactly when $\Phi(\tilde C)$ and $-\Phi(\tilde D)$ share no eigenvalue and self-adjoint exactly when both parameters are Hermitian. All statements were verified to machine precision in the matrix model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(\tilde{Q})$ | The $2\times2$ matrix of $\tilde{Q}$ in the matrix model |
| $\mathrm{vec}$ | Row-major vectorisation onto $\mathbb{C}^{4}$ in the basis $e_{\mu}$ |
| $L_{\tilde C}=\Phi(\tilde C)\otimes I$ | Left multiplication; spectrum $\lambda_{i}$, each twice |
| $R_{\tilde D}=I\otimes\Phi(\tilde D)^{T}$ | Right multiplication; spectrum $\mu_{j}$, each twice |
| $\Theta_{\tilde{Q}}=\Phi(\tilde{Q})\otimes(\Phi(\tilde{Q}))^{\natural}$ | Two-sided operator; spectrum $\lambda_{i}\overline{\lambda_{j}}$ |
| $\mathrm{ad}_{\tilde C}=L_{\tilde C}-R_{\tilde C}$ | Inner derivation; spectrum $\lambda_{i}-\lambda_{j}$ |
| $L_{\tilde C}+R_{\tilde D}$ | Sylvester operator; spectrum $\lambda_{i}+\mu_{j}$ |
| $(p,q)$ | Inertia of a Hermitian element; $\mathrm{sig}(\Theta_{\tilde{Q}})=(p^{2}+q^{2},2pq)$ |
| $(\tilde S,\tilde V)=\mathrm{Sc}(\tilde{S}^{*}\tilde V)$ | The Hermitian form of the spectra |

## Further Reading

- *The Spectra of Self-Adjoint Operators with Hermitian Adjoint* (`articles_maths/the-spectra-of-self-adjoint-operators-with-hermitian-adjoint.md`), the general spectral theorem of which this is the biquaternion instance.
- *Biquaternion Spectral Theory* (`articles_maths/biquaternion-spectral-theory.md`), for the spectra of **elements**: the element-level theory that this article uses and does not repeat.
- *Self-Adjoint and Skew Operators with Hermitian Adjoint* (`articles_maths/self-adjoint-and-skew-operators-with-hermitian-adjoint.md`), for the general operator-level theory of the adjoint.
- *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/one-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`) and *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the definitions, the type criteria and the composition laws.
- *The Hermitian Sylvester Equation* (`articles_maths/the-hermitian-sylvester-equation.md`), for the solvability and the solution of $\tilde CX+X\tilde D=c$.
- *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/completely-positive-maps-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positivity statements at the level of maps.
- *Biquaternion Automorphisms and Derivations* (`articles_maths/biquaternion-automorphisms-and-derivations.md`), for the derivations and their weights.
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`) and *Biquaternion Spectral Theory* (`articles_maths/biquaternion-spectral-theory.md`), for the inertia, the cone and the element spectra.
