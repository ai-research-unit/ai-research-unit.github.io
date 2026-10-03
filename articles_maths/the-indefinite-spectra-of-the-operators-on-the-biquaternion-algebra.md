# __The Indefinite Spectra of the Operators on the Biquaternion Algebra__

## Introduction

The spectral theory of the Hermitian adjoint on the biquaternion algebra gives the spectra of the left and right multiplications and of the sandwich, and reads self-adjointness, positivity and unitarity off the element spectrum (*The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*, *Biquaternion Spectral Theory*). This article does the same for the **Krein adjoint** $T^{\dagger}=J\,T^{*}J$ of *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*. Two facts govern the answer. First, the $J$-self-adjoint operators of the three families are very few: the left and right multiplications by real scalars, and the sandwiches with a parameter in the centre or in the vector subspace. Second, on those families the spectrum comes out **real with signs**: for the sandwich with a vector parameter the spectrum is the pair $\pm|N(\tilde{Q})|$ with multiplicity two each, so the operator has an **inertia** $(2,2)$, while a central parameter gives $(4,0)$; the case $N=0$ degenerates to a single nilpotent value. The general Krein theory allows a non-real spectrum, symmetric about the real axis, and the algebra exhibits it as soon as a mixed sum of a left and a right multiplication is admitted.

The general theory is *Spectral Theory on Krein Spaces* and *Definitizable Operators and the Krein–Naĭmark Theorem*; the definite counterpart is *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*; the operator classes are *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*; the element spectra that the operator spectra are read from are *Biquaternion Spectral Theory*; and the symmetry is *The Fundamental Symmetry of the Biquaternion Algebra*.

**Conventions.** $T^{\dagger}=JT^{*}J$ with $J={}^{\natural}$; $\Theta_{\tilde{Q}}(\tilde{X})=\tilde{Q}\tilde{X}\tilde{Q}^{\dagger}$, $L_{\tilde{Q}}$, $R_{\tilde{Q}}$; $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ is the matrix model, $N(\tilde{Q})=\det\Phi(\tilde{Q})$; and the spectra are those of the operators as complex-linear endomorphisms of the four-dimensional complex space $\mathbb{B}$. The Kronecker forms of the definite article are used: $L_{\tilde{Q}}\leftrightarrow\Phi(\tilde{Q})\otimes I$ and $R_{\tilde{R}}\leftrightarrow I\otimes\Phi(\tilde{R})^{\mathsf T}$.

## The Spectral Rules of the Definite Case

The following rules are quoted from the sibling article and are the input to everything below.

- $\mathrm{spec}(L_{\tilde{Q}})=\mathrm{spec}(\Phi(\tilde{Q}))$ with each eigenvalue of multiplicity two, and the same for $R_{\tilde{Q}}$.
- If $\Phi(\tilde{Q})$ is diagonalisable with eigenvalues $\lambda_1,\lambda_2$, then
$$
\mathrm{spec}\bigl(\Theta_{\tilde{Q}}\bigr)=\{\lambda_i\bar\lambda_j\}_{i,j=1}^{2}.
$$

**Proof.** These are the Kronecker forms $L_{\tilde{Q}}=\Phi(\tilde{Q})\otimes I$, $R_{\tilde{R}}=I\otimes\Phi(\tilde{R})^{\mathsf T}$ and $\Theta_{\tilde{Q}}=\Phi(\tilde{Q})\otimes\overline{\Phi(\tilde{Q})}$ of *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*, whose spectra are the sums and products of the spectra of the factors.

## The $J$-Self-Adjoint Left and Right Multiplications

**Theorem.** A left multiplication $L_{\tilde{Q}}$ is $J$-self-adjoint exactly for $\tilde{Q}\in\mathbb{R}e_0$, and then

$$
\mathrm{spec}\bigl(L_{te_0}\bigr)=\{t\}\ \text{with multiplicity }4,\qquad t\in\mathbb{R},
$$

so the spectrum is real and the operator is a real scalar.

**Proof.** The criterion is that of *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*, §*The $J$-Adjoint of the Three Families*; a scalar multiple of the identity has the single eigenvalue $t$ with multiplicity $\dim_{\mathbb{C}}\mathbb{B}=4$.

**Remark (why there is no non-real case here).** A real quaternion $\tilde{Q}=t+\sum_kq_ke_k$ has the two eigenvalues $\lambda=t+i|\mathbf{q}|$ and $\bar\lambda$ of $\Phi(\tilde{Q})$ (*Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*), so $\mathrm{spec}(L_{\tilde{Q}})=\{\lambda,\bar\lambda\}$ with multiplicity two each; but such an $L_{\tilde{Q}}$ is $J$-self-adjoint only when $\mathbf{q}=0$, in which case the pair collapses to the real double eigenvalue $t$. The non-real pair is a $J$-self-adjoint spectrum only for operators outside the left-multiplication family. The same statement holds for $R_{\tilde{R}}$.

**Proof.** The eigenvalues of a real quaternion are those of its $2\times2$ matrix, computed in *Biquaternion Spectral Theory*; the collapse is the criterion above.

## The $J$-Self-Adjoint Sandwiches

**Theorem (the two regimes).** Let $\Theta_{\tilde{Q}}$ be a sandwich with $\tilde{Q}$ in $\mathbb{C}_{\mathbb{B}}\cup\mathbb{V}_{\mathbb{B}}$ — the $J$-self-adjoint sandwiches of *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*.

- If $\tilde{Q}=\zeta e_0$ is central, then $\Theta_{\tilde{Q}}=|\zeta|^{2}\,\mathrm{id}$ and
$$
\mathrm{spec}\bigl(\Theta_{\tilde{Q}}\bigr)=\bigl\{|\zeta|^{2}\bigr\}\ \text{with multiplicity }4,\qquad\text{inertia }(4,0).
$$
- If $\tilde{Q}=\tilde V\in\mathbb{V}_{\mathbb{B}}$ is a pure vector with $N(\tilde V)\neq0$, then
$$
\mathrm{spec}\bigl(\Theta_{\tilde{V}}\bigr)=\bigl\{|N(\tilde V)|,\,|N(\tilde V)|,\,-|N(\tilde V)|,\,-|N(\tilde V)|\bigr\},\qquad\text{inertia }(2,2).
$$
- If $\tilde{Q}=\tilde V\in\mathbb{V}_{\mathbb{B}}$ has $N(\tilde V)=0$, then $\Theta_{\tilde{V}}$ is nilpotent of order two, $\Theta_{\tilde{V}}^{2}=0$, and
$$
\mathrm{spec}\bigl(\Theta_{\tilde{V}}\bigr)=\{0\}\ \text{with multiplicity }4.
$$

**Proof.** For a central parameter, $\Theta_{\zeta e_0}(\tilde{X})=\zeta\tilde{X}\bar\zeta=|\zeta|^{2}\tilde{X}$, which is the first line. For a vector parameter, $\tilde V^{2}=-N(\tilde V)e_0$ and $(\tilde V^{\dagger})^{2}=-\overline{N(\tilde V)}e_0$, because $\tilde V^{\dagger}=-\bar{\tilde V}$ and $\bar{\tilde V}{}^{2}=-N(\bar{\tilde V})e_0=-\overline{N(\tilde V)}e_0$; hence
$$
\Theta_{\tilde V}^{2}(\tilde{X})=\tilde V^{2}\tilde X(\tilde V^{\dagger})^{2}=|N(\tilde V)|^{2}\tilde X,
$$
so $\Theta_{\tilde V}^{2}=|N(\tilde V)|^{2}\mathrm{id}$. If $N(\tilde V)\neq0$ the matrix $\Phi(\tilde V)$ is traceless with $\Phi(\tilde V)^{2}=-N(\tilde V)I$, hence diagonalisable with the eigenvalues $\pm i\sqrt{N(\tilde V)}$, and the product rule gives $\{|N|,|N|,-|N|,-|N|\}$. If $N(\tilde V)=0$ then $\tilde V^{2}=0$ and $(\tilde V^{\dagger})^{2}=0$, so $\Theta_{\tilde V}^{2}=0$; the single eigenvalue is $0$ with multiplicity four.

**Corollary (the sandwich is definitizable except at the null elements).** A $J$-self-adjoint sandwich is diagonalisable, with real spectrum, exactly when it is not the sandwich of a null vector $\tilde V$ with $N(\tilde V)=0$; in that case its spectrum is the real pair $\pm|N(\tilde Q)|$ with the inertia $(4,0)$ or $(2,2)$, and the operator is definitizable in the sense of *Definitizable Operators and the Krein–Naĭmark Theorem*.

**Proof.** The theorem gives the two diagonalisable regimes; the nilpotent case has no basis of eigenvectors.

**Remark (the sign structure).** The signs are the content of the indefinite theory: the sandwich of a vector parameter of nonzero norm has exactly two positive and two negative eigenvalues, whereas the definite sibling's sandwich of a Hermitian element is positive and has non-negative spectrum. The two regimes $(4,0)$ and $(2,2)$ are the two possible inertias of a $J$-self-adjoint sandwich on a space of complex dimension four, and they are the "signature of the sandwich operator" alluded to in the sibling article.

## The Symmetry of the Spectrum

**Theorem.** For every $J$-self-adjoint operator $T$ on $\mathbb{B}$ the spectrum is symmetric under conjugation, $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$, and the algebraic multiplicities of $\lambda$ and $\bar\lambda$ coincide.

**Proof.** $T^{\dagger}=T$ gives $T^{*}=JTJ$, so $T$ is similar to its adjoint; a matrix is similar to its adjoint only... precisely, $\mathrm{spec}(T^{*})=\overline{\mathrm{spec}(T)}$ for every operator and $\mathrm{spec}(JTJ)=\mathrm{spec}(T)$, so $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$; the multiplicities agree because similarity preserves the characteristic polynomial up to conjugation.

**Corollary (the symmetry is visible in the two regimes).** In the regime $(4,0)$ the symmetry is vacuous (a real multiple of the identity); in the regime $(2,2)$ it pairs $|N|$ with itself and $-|N|$ with itself; and it constrains any non-real $J$-self-adjoint spectrum of the algebra to consist of conjugate pairs.

**Proof.** Immediate from the theorem and the spectra computed above.

## The Mixed Sums and the Non-Real Spectrum

The symmetry is a constraint, not a triviality: away from the three families the algebra has $J$-self-adjoint operators with genuinely non-real spectrum.

**Theorem.** The operator

$$
T=L_{e_1}+R_{e_1}
$$

is $J$-self-adjoint, and

$$
\mathrm{spec}(T)=\{2i,\,-2i,\,0,\,0\}.
$$

**Proof.** $J$-self-adjointness is $(L_{\tilde{Q}})^{\dagger}+(R_{\tilde{Q}})^{\dagger}=R_{\bar{\tilde{Q}}}+L_{\bar{\tilde{Q}}}$, which for $\tilde{Q}=e_1$ (real coefficients) returns $L_{e_1}+R_{e_1}$; the sum is a "Sylvester" operator, and the rule $\mathrm{spec}(L_{\tilde{Q}}+R_{\tilde{Q}})=\{\lambda_i+\lambda_j\}$ for the eigenvalues $\lambda_i$ of $\Phi(\tilde{Q})$ (*The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*, §*The Spectrum of the Sylvester Operator*) applied to $\Phi(e_1)=i\sigma_1$ with eigenvalues $\pm i$ gives $\{i+i,i-i,-i+i,-i-i\}=\{2i,0,0,-2i\}$.

**Remark.** The spectrum is non-real and symmetric about the real axis, exactly as the general theory of *Spectral Theory on Krein Spaces* predicts, and the operator is $J$-self-adjoint but not definitizable; it is therefore a $J$-self-adjoint operator of the algebra to which the Krein–Naĭmark theory does not apply, in contrast with the sandwiches of §*The $J$-Self-Adjoint Sandwiches*.

## Worked Examples

**A central scalar.** $\tilde{Q}=t e_0$, $t\in\mathbb{R}$: $L_{\tilde{Q}}$ is $J$-self-adjoint with spectrum $\{t\}$ of multiplicity four.

**A real quaternion.** $\tilde{Q}=\tfrac12+\tfrac{\sqrt3}{2}e_1$: $N(\tilde{Q})=1$ and the eigenvalues of $\Phi(\tilde{Q})$ are $e^{\pm i\pi/3}$; $L_{\tilde{Q}}$ is a unit-norm element, but it is **not** $J$-self-adjoint, and its spectrum $\{e^{\pm i\pi/3}\}$ is not the $J$-self-adjoint spectrum. It is $J$-unitary as a sandwich, by $|N|=1$.

**A vector sandwich of nonzero norm.** $\tilde{Q}=e_1$: $\mathrm{spec}(\Theta_{e_1})=\{1,1,-1,-1\}$, inertia $(2,2)$; the operator is $J$-self-adjoint and $J$-unitary.

**A vector sandwich of zero norm.** $\tilde{Q}=e_1+ie_2$: $N=0$, so $\Theta_{\tilde{Q}}^{2}=0$ and the spectrum is $\{0\}$; the sandwich of a null vector is nilpotent.

**A central phase.** $\tilde{Q}=e^{i\theta}e_0$: $\Theta_{\tilde{Q}}=\mathrm{id}$, spectrum $\{1\}$ of multiplicity four, inertia $(4,0)$.

**The non-real example.** $T=L_{e_1}+R_{e_1}$: spectrum $\{2i,-2i,0\}$, non-real, symmetric, not definitizable.

## Summary

For the Krein adjoint $T^{\dagger}=JT^{*}J$ the $J$-self-adjoint operators of the three families are few and their spectra are real with signs. A left or right multiplication is $J$-self-adjoint exactly for a real scalar parameter, and then the spectrum is that scalar with multiplicity four. A sandwich is $J$-self-adjoint exactly for a parameter in the centre or in the vector subspace, and there are two regimes: a central parameter gives $|\zeta|^{2}$ with multiplicity four and inertia $(4,0)$, while a vector parameter of nonzero norm gives the real pair $\pm|N(\tilde{Q})|$ with multiplicity two each and inertia $(2,2)$; a null vector parameter gives the nilpotent operator $\Theta_{\tilde{Q}}^{2}=0$ with the single spectrum $\{0\}$. Every $J$-self-adjoint operator has a spectrum symmetric under conjugation with matching multiplicities, and this is the only general constraint: away from the three families the algebra carries $J$-self-adjoint operators with non-real spectrum, the simplest being $L_{e_1}+R_{e_1}$ with $\{2i,-2i,0\}$, which is not definitizable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\dagger}=JT^{*}J$ | The Krein adjoint |
| $\mathrm{spec}(L_{\tilde{Q}})=\mathrm{spec}(\Phi(\tilde{Q}))$ (twice) | Rule for the left multiplication |
| $L_{\tilde{Q}}$ $J$-self-adjoint $\iff\tilde{Q}\in\mathbb{R}e_0$, spectrum $\{t\}$ (mult. 4) | The left-multiplication case |
| $\mathrm{spec}(\Theta_{\zeta e_0})=\{\lvert\zeta\rvert^{2}\}$ (mult. 4), inertia $(4,0)$ | The central regime |
| $\mathrm{spec}(\Theta_{\tilde V})=\{\pm\lvert N(\tilde V)\rvert\}$ (mult. 2), inertia $(2,2)$ | The vector regime |
| $\Theta_{\tilde V}^{2}=0$, $\mathrm{spec}=\{0\}$ | The null-vector regime |
| $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$ | The general symmetry |
| $\mathrm{spec}(L_{e_1}+R_{e_1})=\{2i,-2i,0\}$ | A non-real, non-definitizable spectrum |

## Further Reading

- *Spectral Theory on Krein Spaces* (`articles_maths/spectral-theory-on-krein-spaces.md`) and *Definitizable Operators and the Krein–Naĭmark Theorem* (`articles_maths/definitizable-operators-and-the-krein-naimark-theorem.md`), for the indefinite spectral theory and definitizability
- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the definite spectral rules quoted here
- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the $J$-self-adjointness criteria
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for $J$ and its eigenspaces
- *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* (`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.md`), for the indefinite cone and the $J$-Cartan involution
- *Biquaternion Spectral Theory* (`articles_maths/biquaternion-spectral-theory.md`), for the element spectra and the Cayley–Hamilton functionals
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the spectra, the inertias and the normal forms of indefinite operators
