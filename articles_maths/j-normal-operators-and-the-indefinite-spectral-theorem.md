# __J-Normal Operators and the Indefinite Spectral Theorem__

## Introduction

In a positive definite space the normal operators are the ones a spectral theorem can reach, and normality forces the spectrum into a symmetry: normal operators have no reason to be self-adjoint, but they are diagonalised by unitaries, and their spectra are conjugate-symmetric. This article asks what survives of that circle of ideas for the general quaternionic sesquilinear form. The answer is a partial one, and its partiality is the point: the $J$-normal operators are still those commuting with their $J$-adjoint, the algebra's three operator families are all $J$-normal, the $J$-self-adjoint operators with positive definite partner $JT$ still have real spectra and diagonalisations, and the spectral symmetries still hold — but $J$-normality no longer forces a real spectrum, a $J$-self-adjoint operator need not be diagonalisable, and the $J$-unitary group is not compact. The $J$-adjoint itself is *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*; the spectra of the algebra's operators are computed in *The Indefinite Spectra of the Operators on the Biquaternion Algebra*; and the group of $J$-unitaries is *The Krein Isometry Group and Its $J$-Contractions*.

**Conventions.** $\mathbb{B}$ is the biquaternion algebra with its general plain sesquilinear form $\langle\tilde{Q}',\tilde{Q}\rangle_{*}=\sum_{\mu}\bar Q_{\mu}Q'_{\mu}$ (positive definite, Gram matrix $\mathrm{I}_4$ in the coefficient basis), its general quaternionic sesquilinear form $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ (Gram matrix $E=\mathrm{diag}(1,-1,-1,-1)$), and its fundamental symmetry $J={}^{\natural}$. The **Krein adjoint** of a $\mathbb{C}$-linear operator $T$ is $T^{\dagger}=JT^{*}J$, characterised by $\langle\tilde{Q}',T\tilde{Q}\rangle_{\natural*}=\langle T^{\dagger}\tilde{Q}',\tilde{Q}\rangle_{\natural*}$, where $T^{*}$ is the adjoint for $\langle\cdot,\cdot\rangle_{*}$. The algebra's operators are $L_{\tilde{Q}}$, $R_{\tilde{Q}}$ and $\Theta_{\tilde{Q}}$, with $(\Theta_{\tilde{Q}})(\tilde{P})=\tilde{Q}\tilde{P}\tilde{Q}^{\dagger}$.

## J-Normality

**Definition.** A $\mathbb{C}$-linear operator $T$ is **$J$-normal** when

$$
T^{\dagger}T=TT^{\dagger},
$$

that is, when $T$ commutes with its Krein adjoint. It is $J$-self-adjoint when $T^{\dagger}=T$ and $J$-unitary when $T^{\dagger}T=TT^{\dagger}=\mathrm{id}$.

**Theorem (closure properties).** Every $J$-self-adjoint and every $J$-unitary operator is $J$-normal. The $J$-normal operators are closed under the Krein adjoint, under powers and inverses, and under $\mathbb{C}$-linear combinations of mutually commuting ones; the $J$-normal operators that are also $J$-self-adjoint form a real vector space, and those that are also $J$-unitary form a group.

**Proof.** For $J$-self-adjointness, $T^{\dagger}T=T^{2}=TT^{\dagger}$; for $J$-unitarity both products are the identity. The adjoint of $T^{\dagger}$ is $T$, and $T^{\dagger}$ trivially commutes with $T$ whenever $T$ does; powers of a $J$-normal operator commute with each other and with their adjoints by induction; inverses follow from $T^{\dagger}T=TT^{\dagger}$ by inversion; and commuting normal operators add, because every term in the expansion of $(S+T)^{\dagger}(S+T)$ and $(S+T)(S+T)^{\dagger}$ can be reordered to the same expression.

**Theorem (the definite model of $J$-normality).** In the coefficient basis, with $T^{*}$ the conjugate transpose and $E=\mathrm{diag}(1,-1,-1,-1)$, the operator $T$ is $J$-normal if and only if

$$
T^{*}\,E\,T\,E=E\,T\,E\,T^{*},
$$

equivalently if and only if $T^{*}$ commutes with $J TJ$.

**Proof.** $T^{\dagger}=ET^{*}E$, so $T^{\dagger}T=ET^{*}ET$ and $TT^{\dagger}=TET^{*}E$. Multiplying the equality $ET^{*}ET=TET^{*}E$ by $E$ on the left and on the right gives $T^{*}ETE=ETET^{*}$, which is $T^{*}(ETE)=(ETE)T^{*}$.

**Remark (why the definite case is not recovered).** For the Hermitian adjoint the condition is $T^{*}T=TT^{*}$; here the conjugation by $E$ intervenes on both sides, so $J$-normality is *not* the normality of $T$ for $\langle\cdot,\cdot\rangle_{*}$ and *not* the normality of $JT$. The two notions coincide only on the operators that commute with $E$ in the appropriate sense.

## The Spectral Theorem for J-Self-Adjoint Operators

**Theorem (the dictionary).** The map $T\mapsto JT$ is a bijection from the $J$-self-adjoint operators onto the self-adjoint operators for $\langle\cdot,\cdot\rangle_{*}$, with inverse $S\mapsto JS$; consequently every $J$-self-adjoint operator is $J$ times a Hermitian operator, and its spectrum is the spectrum of that Hermitian operator read through $J$.

**Proof.** $T^{\dagger}=T\iff ET^{*}E=T\iff (ET)^{*}=ET$, and $S=ET$ is Hermitian exactly when $S^{*}=S$; the map is its own inverse up to the involutions $E$.

**Theorem (the definite-spectrum case).** Let $T$ be $J$-self-adjoint and suppose that $JT$ is positive definite for $\langle\cdot,\cdot\rangle_{*}$. Then $T$ has real spectrum and is diagonalisable over $\mathbb{C}$.

**Proof.** Write $S=JT$, positive definite and self-adjoint. Then $T=ES$ and

$$
S^{1/2}\,T\,S^{-1/2}=S^{1/2}ES^{1/2},
$$

an operator that is self-adjoint for $\langle\cdot,\cdot\rangle_{*}$, since $S^{1/2}$ and $E$ are; it is therefore diagonalisable with real eigenvalues (*Self-Adjoint Elements and the Positive Cone*), and $T$, being similar to it, is diagonalisable with the same real spectrum.

**Remark (the semidefinite case fails the conclusion).** The hypothesis of positive definiteness cannot be weakened to positive semidefiniteness. With $E=\mathrm{diag}(1,-1,-1,-1)$ and $S=|\tilde{Q}\rangle\langle\tilde{Q}|$ the rank-one operator of the isotropic element $\tilde{Q}=e_0+e_1$, the operator $T=ES$ is $J$-self-adjoint and lies in the $J$-positive cone, while

$$
T^{2}=0,\qquad T\neq0 ,
$$

so $T$ is nilpotent, has spectrum $\{0\}$, and is not diagonalisable. Thus a $J$-self-adjoint, $J$-nonnegative operator of the algebra need not have a $J$-orthonormal eigenbasis.

## The Spectral Symmetries

**Theorem (the symmetry of the $J$-self-adjoint spectrum).** If $T$ is $J$-self-adjoint then $T$ and $T^{*}$ have the same characteristic polynomial, so the spectrum of $T$, with multiplicities, is invariant under conjugation:

$$
\lambda\in\mathrm{spec}(T)\iff\bar\lambda\in\mathrm{spec}(T).
$$

**Proof.** $T=ES$ with $S$ self-adjoint, so $T^{*}=(ES)^{*}=SE$; the matrices $ES$ and $SE$ have the same characteristic polynomial, because $AB$ and $BA$ do for square matrices. Since $T^{*}$ is the conjugate transpose of $T$, its spectrum is the conjugate of the spectrum of $T$.

**Theorem (the symmetry of the $J$-unitary spectrum).** If $T$ is $J$-unitary then its spectrum is invariant under inversion in the unit circle,

$$
\lambda\in\mathrm{spec}(T)\iff\frac{1}{\bar\lambda}\in\mathrm{spec}(T),
$$

with the same multiplicity; in particular an eigenvalue on the unit circle has its conjugate present as well, but the spectrum is in general not contained in the unit circle.

**Proof.** $T$ is $J$-unitary exactly when $T^{*}ET=E$, that is $T^{*}=ET^{-1}E$; so $T^{*}$ is similar to $T^{-1}$, whence the characteristic polynomials of $T^{*}$ and $T^{-1}$ agree, and $\mathrm{spec}(T^{-1})=\{\lambda^{-1}:\lambda\in\mathrm{spec}(T)\}$ while $\mathrm{spec}(T^{*})=\overline{\mathrm{spec}(T)}$. The last clause is the hyperbolic boost of the next sections, with eigenvalues $e^{\pm t}$.

**Remark (no unit-circle confinement).** The symmetry is inversion, not confinement: the boost $T$ with $e_0\mapsto\cosh t\,e_0+\sinh t\,e_1$, $e_1\mapsto\sinh t\,e_0+\cosh t\,e_1$ and $e_2,e_3$ fixed is $J$-unitary with eigenvalues $e^{t},e^{-t},1,1$, so a $J$-unitary operator leaves the unit circle as soon as it moves the Minkowski slice (*The Krein Isometry Group and Its $J$-Contractions*).

## The Normality of the Algebra's Operators

**Theorem (the three families are $J$-normal).** For every biquaternion $\tilde{Q}$ the left multiplication $L_{\tilde{Q}}$, the right multiplication $R_{\tilde{Q}}$ and the sandwich $\Theta_{\tilde{Q}}$ are $J$-normal. Precisely,

$$
(L_{\tilde{Q}})^{\dagger}=R_{\bar{\tilde{Q}}},\qquad
(R_{\tilde{Q}})^{\dagger}=L_{\bar{\tilde{Q}}},\qquad
(\Theta_{\tilde{Q}})^{\dagger}=\Theta_{{}^{\natural}\tilde{Q}},
$$

and in each case the two factors of $T^{\dagger}T$ commute.

**Proof.** $[L_{\tilde{Q}}\tilde{P},\tilde{U}]=\langle R_{\bar{\tilde{Q}}}\tilde{U},\tilde{P}\rangle_{\natural*}$ was computed in *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*; then $L_{\tilde{Q}}^{\dagger}L_{\tilde{Q}}=R_{\bar{\tilde{Q}}}L_{\tilde{Q}}$ and $L_{\tilde{Q}}L_{\tilde{Q}}^{\dagger}=L_{\tilde{Q}}R_{\bar{\tilde{Q}}}$, equal because left and right multiplications commute. The right case is the same. For the sandwich, $\Theta_{\tilde{Q}}^{\dagger}\Theta_{\tilde{Q}}=\Theta_{{}^{\natural}\tilde{Q}}\Theta_{\tilde{Q}}=\Theta_{{}^{\natural}\tilde{Q}\,\tilde{Q}}=\Theta_{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}e_0}$, and $\Theta_{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}e_0}=|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|^{2}\mathrm{id}$; the same value is obtained in the other order, because $\tilde{Q}$ and ${}^{\natural}\tilde{Q}$ have the same norm.

**Remark (a product of a left and a right multiplication need not be normal).** The composite $L_{\tilde{Q}}R_{\tilde{R}}$ has Krein adjoint $L_{\bar{\tilde{R}}}R_{\bar{\tilde{Q}}}$, and the normality condition is the commutation of the two parameters; it fails for general $\tilde{Q},\tilde{R}$, so the $J$-normal operators are not the whole of the algebra's operator span.

## The Limits of the Analogy

**Theorem (normality does not force a real spectrum).** A $J$-normal operator of the algebra can have a non-real spectrum. For $\tilde{Q}=e_1$ the operator $L_{e_1}$ is $J$-normal with

$$
\mathrm{spec}(L_{e_1})=\{i,-i\},
$$

each eigenvalue of multiplicity two.

**Proof.** $L_{e_1}$ is $J$-normal by the theorem above. As a $\mathbb{C}$-linear operator on $\mathbb{B}\cong\mathbb{C}^{4}$ it is the left multiplication of the matrix $\Phi(e_1)$, whose eigenvalues are $i$ and $-i$; and the left regular representation of the algebra is the direct sum of two copies of the defining representation, so each eigenvalue occurs twice (*The Indefinite Spectra of the Operators on the Biquaternion Algebra*).

**Corollary (contrast with the definite theory).** In a positive definite space a normal operator with real eigenvalues is self-adjoint and a normal operator with non-real eigenvalues is not; here $L_{e_1}$ is $J$-normal, is not $J$-self-adjoint, and its spectrum is imaginary. Normality, self-adjointness and reality of the spectrum are three independent conditions in the indefinite case, whereas in the definite case normality and reality together imply diagonalisability by unitaries.

## Worked Examples

**$J$ itself.** $J={}^{\natural}$ is $J$-self-adjoint and $J$-unitary, hence $J$-normal; its spectrum is $\{+1,-1\}$, real, and the multiplicities $(2,6)$ are the inertia of the form.

**A central scalar.** $\tilde{Q}=te_0$, $t\in\mathbb{R}$: $L_{\tilde{Q}}=t\,\mathrm{id}$ is $J$-self-adjoint with spectrum $\{t\}$ of multiplicity four, the positive definite case of the spectral theorem with $JT=tJ$ definite exactly for $t\neq0$ up to sign.

**A vector element.** $L_{e_1}$: $J$-normal and not $J$-self-adjoint, with the imaginary spectrum $\{i,-i\}$.

**A sandwich.** $\Theta_{e_1}$: $J$-normal, $J$-self-adjoint and $J$-unitary at once, since $e_1$ lies in the vector subspace and $|\langle e_1,e_1\rangle_{\natural}|=1$; its spectrum is $\{+1,-1\}$, each of multiplicity two.

**A $J$-positive nilpotent.** $T=ES$ with $S=|\tilde{Q}\rangle\langle\tilde{Q}|$ and $\tilde{Q}=e_0+e_1$: $J$-self-adjoint, in the $J$-positive cone, with $T^{2}=0$ and spectrum $\{0\}$; not diagonalisable.

**A $J$-unitary with non-real spectrum.** $L_{e^{i\theta}e_0}$: $J$-unitary with spectrum $\{e^{i\theta}\}$ on the circle, showing that confinement to the circle takes place exactly for the scalar phases.

## Summary

A $\mathbb{C}$-linear operator is $J$-normal when it commutes with its Krein adjoint $T^{\dagger}=JT^{*}J$; in the coefficient basis this is $T^{*}ETE=ETET^{*}$. The $J$-self-adjoint and the $J$-unitary operators are $J$-normal, and so are all three families of the algebra, $L_{\tilde{Q}}$, $R_{\tilde{Q}}$ and $\Theta_{\tilde{Q}}$, because the Krein adjoint of a left multiplication is a right one and the two commute. The map $T\mapsto JT$ puts the $J$-self-adjoint operators in bijection with the Hermitian ones, and when $JT$ is positive definite the operator is diagonalisable with real spectrum; positive semidefiniteness is not enough, since $T=J|\tilde{Q}\rangle\langle\tilde{Q}|$ with $\tilde{Q}$ isotropic is $J$-self-adjoint, $J$-nonnegative and nilpotent. The spectra carry two symmetries: conjugation for $J$-self-adjoint operators and inversion $\lambda\mapsto1/\bar\lambda$ for $J$-unitary ones, without confinement to the unit circle. The analogy with the definite theory stops at normality: $L_{e_1}$ is $J$-normal with the non-real spectrum $\{i,-i\}$, so normality, self-adjointness and reality of the spectrum are independent conditions here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\dagger}=JT^{*}J$ | The Krein adjoint |
| $T^{\dagger}T=TT^{\dagger}$ | $J$-normality |
| $T^{*}ETE=ETET^{*}$, or $\langle JTJ,T^{*}\rangle_{\natural*}=0$ | $J$-normality in the coefficient basis |
| $T\mapsto JT$ | The bijection with the Hermitian operators |
| $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$ | The symmetry for $J$-self-adjoint $T$ |
| $\lambda\leftrightarrow1/\bar\lambda$ | The symmetry for $J$-unitary $T$ |
| $L_{\tilde{Q}}$, $R_{\tilde{Q}}$, $\Theta_{\tilde{Q}}$ | The three $J$-normal families |
| $J\lvert\tilde{Q}\rangle\langle\tilde{Q}\rvert$ with $\tilde{Q}=e_0+e_1$ | $J$-self-adjoint, $J$-nonnegative, nilpotent |

## Further Reading

- *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the Krein adjoint and its criteria
- *The Indefinite Spectra of the Operators on the Biquaternion Algebra* (`articles_maths/the-indefinite-spectra-of-the-operators-on-the-biquaternion-algebra.md`), for the explicit spectra used here
- *The Krein Isometry Group and Its J-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`), for the $J$-unitary group $U(1,3)$ and the boosts
- *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* (`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.md`), for the $J$-positive cone containing the nilpotent example
- *The Krein Cartan Decomposition of the Operator Algebra* (`articles_maths/the-krein-cartan-decomposition-of-the-operator-algebra.md`), for the operator algebra the family statements live in
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for indefinite normality, the definite-spectrum criterion and the symmetries of the spectra
