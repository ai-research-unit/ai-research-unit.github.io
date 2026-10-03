# __J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra__

## Introduction

The fundamental symmetry $J={}^{\natural}$ equips the biquaternion algebra with a second adjoint operation: alongside the Hermitian adjoint ${}^{*}$ of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, there is the adjoint for the Krein form,

$$
T^{\dagger}=J\,T^{*}J,
$$

for which the operators of the algebra can be self-adjoint, skew-adjoint, unitary or normal. This article computes that adjoint on the three operator families of the corpus — the left multiplications $L_{\tilde{Q}}$, the right multiplications $R_{\tilde{Q}}$ and the sandwiches $\Theta_{\tilde{Q}}$ — and reads off the indefinite counterparts of the self-adjointness, skew-adjointness, unitarity and normality of the Hermitian case. The single structural surprise is that the indefinite adjoint of a left multiplication is a **right** multiplication: the form built from the trace of a product does not see the order, so $J$ exchanges the sides.

The general theory is *J-Self-Adjoint and J-Unitary Operators* and *Krein Spaces*; the symmetry and the bridge are *The Fundamental Symmetry of the Biquaternion Algebra*; the form is *The Biquaternion Krein Form and Its Signature*; the definite counterpart is *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*; the spectral consequences are *The Indefinite Spectra of the Operators on the Biquaternion Algebra*.

**Conventions.** Operators act on $\mathbb{B}$; $\Theta_{\tilde{Q}}(\tilde{V})=\tilde{Q}\tilde{V}\tilde{Q}^{\dagger}$ is the dagger sandwich, $L_{\tilde{Q}}(\tilde{V})=\tilde{Q}\tilde{V}$, $R_{\tilde{Q}}(\tilde{V})=\tilde{V}\tilde{Q}$; ${}^{*}$ is the adjoint for the Hermitian form $\langle\cdot,\cdot\rangle$, so that $L_{\tilde{Q}}^{*}=L_{\tilde{Q}^{\dagger}}$ and $R_{\tilde{Q}}^{*}=R_{\tilde{Q}^{\dagger}}$ (*One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*); $J={}^{\natural}$, and $\bar{\tilde{Q}}$ denotes the coefficient (complex) conjugation. The **$J$-adjoint** is $T^{\dagger}=JT^{*}J$; convergence is automatic, $\mathbb{B}$ being finite-dimensional.

## The $J$-Adjoint

**Proposition (characterisation and calculus).** $T^{\dagger}=JT^{*}J$ is the unique operator with

$$
[T\tilde{Q},\tilde{Q}']=[\tilde{Q},T^{\dagger}\tilde{Q}']\qquad\text{for all }\tilde{Q},\tilde{Q}'\in\mathbb{B},
$$

it is involutive, $(T^{\dagger})^{\dagger}=T$, and antimultiplicative,

$$
(TS)^{\dagger}=S^{\dagger}T^{\dagger},\qquad (\alpha T+\beta S)^{\dagger}=\bar\alpha T^{\dagger}+\bar\beta S^{\dagger}.
$$

**Proof.** $[T\tilde{Q},\tilde{Q}']=\langle JT\tilde{Q},\tilde{Q}'\rangle=\langle\tilde{Q},T^{*}J\tilde{Q}'\rangle=\langle J\tilde{Q},J(JT^{*}J)\tilde{Q}'\rangle=[\tilde{Q},T^{\dagger}\tilde{Q}']$; uniqueness is the non-degeneracy of the form; the calculus is that of ${}^{*}$ conjugated by the involutive $J$.

**Corollary (the definite–indefinite dictionary).** $T$ is $J$-self-adjoint iff $JT$ is self-adjoint for $\langle\cdot,\cdot\rangle$, and $J$-skew-adjoint iff $JT$ is skew-adjoint; so $T\mapsto JT$ is a bijection from the $J$-self-adjoint operators onto the Hermitian-self-adjoint ones. $T$ is $J$-unitary iff it preserves the Krein form,

$$
[T\tilde{Q},T\tilde{Q}']=[\tilde{Q},\tilde{Q}'],\qquad\text{that is}\qquad T^{*}JT=J,
$$

and the $J$-unitary operators form the **indefinite unitary group**

$$
U_{J}(\mathbb{B})=\{T:T^{*}JT=J\}\cong U(1,3),
$$

of real dimension $16$, non-compact. Its maximal compact subgroup is $U(1)\times U(3)$, the isometries of the canonical fundamental decomposition.

**Proof.** $T^{\dagger}=T\iff JT^{*}J=T\iff (JT)^{*}=JT$, and replacing $T$ by $-T$ gives the skew case. For unitarity, $[T\tilde{Q},T\tilde{Q}']=\langle JT\tilde{Q},T\tilde{Q}'\rangle=\langle\tilde{Q},T^{*}JT\tilde{Q}'\rangle$ while $[\tilde{Q},\tilde{Q}']=\langle J\tilde{Q},\tilde{Q}'\rangle=\langle\tilde{Q},J\tilde{Q}'\rangle$, so preservation is exactly $T^{*}JT=J$, which is $T^{\dagger}T=e_0$. In the coefficient basis $J$ has the matrix $E=\mathrm{diag}(1,-1,-1,-1)$ and $T^{*}$ is the conjugate transpose, so that equation reads $T^{*}ET=E$: it defines $U(1,3)$, the isometry group of an indefinite Hermitian form of signature $(1,3)$. The group is non-compact with real dimension $16$, and the matrices that also preserve the two eigenspaces of $J$ are $U(1)\times U(3)$ (*The Krein Isometry Group and Its $J$-Contractions*).

**Remark (what the dictionary does *not* say).** There is no reduction of $J$-unitarity to definite unitarity: $JTJ$ is not unitary for a general $J$-unitary $T$, and $U_{J}(\mathbb{B})$ is not isomorphic to a compact group. The compact groups that do occur are the subgroups listed in the next sections.

**Example.** $J$ itself is $J$-unitary, $J^{\dagger}=JJ^{*}J=J$ and $J^{2}=\mathrm{id}$, though $J$ is not Hermitian-unitary (it is Hermitian-self-adjoint with spectrum $\{+1,-1\}$).

## The $J$-Adjoint of the Three Families

The natural conjugation exchanges the sides, and this propagates to the adjoints.

**Theorem (the adjoints).** For all $\tilde{Q},\tilde{R}\in\mathbb{B}$,

$$
\bigl(L_{\tilde{Q}}\bigr)^{\dagger}=R_{\bar{\tilde{Q}}},\qquad
\bigl(R_{\tilde{R}}\bigr)^{\dagger}=L_{\bar{\tilde{R}}},\qquad
\bigl(L_{\tilde{Q}}R_{\tilde{R}}\bigr)^{\dagger}=L_{\bar{\tilde{R}}}R_{\bar{\tilde{Q}}},\qquad
\bigl(\Theta_{\tilde{Q}}\bigr)^{\dagger}=\Theta_{{}^{\natural}\tilde{Q}},
$$

where $\bar{\tilde{Q}}$ is the coefficient conjugate and ${}^{\natural}\tilde{Q}$ the natural conjugate of the parameter.

**Proof.** By the anti-automorphism property of ${}^{\natural}$, ${}^{\natural}L_{\tilde{Q}}{}^{\natural}=R_{\tilde{Q}^{\natural}}$ and ${}^{\natural}R_{\tilde{R}}{}^{\natural}=L_{\tilde{R}^{\natural}}$ (*The Fundamental Symmetry of the Biquaternion Algebra*). Hence $L_{\tilde{Q}}^{\dagger}={}^{\natural}L_{\tilde{Q}}^{*}{}^{\natural}={}^{\natural}L_{\tilde{Q}^{\dagger}}{}^{\natural}=R_{\tilde{Q}^{\dagger\natural}}$, and $\tilde{Q}^{\dagger\natural}=(\tilde{Q}^{\dagger})^{\natural}=\overline{\tilde{Q}}$ because $\dagger$ and $\natural$ commute; the second is the same with left and right interchanged. The third follows by antimultiplicativity, $(L_{\tilde{Q}}R_{\tilde{R}})^{\dagger}=R_{\tilde{R}}^{\dagger}L_{\tilde{Q}}^{\dagger}=L_{\bar{\tilde{R}}}R_{\bar{\tilde{Q}}}$. For the sandwich, $\Theta_{\tilde{Q}}=L_{\tilde{Q}}R_{\tilde{Q}^{\dagger}}$, so $\Theta_{\tilde{Q}}^{\dagger}=R_{\tilde{Q}^{\dagger}}^{\dagger}L_{\tilde{Q}}^{\dagger}=L_{\overline{\tilde{Q}^{\dagger}}}R_{\bar{\tilde{Q}}}=L_{{}^{\natural}\tilde{Q}}R_{\bar{\tilde{Q}}}=\Theta_{{}^{\natural}\tilde{Q}}$, using $\overline{\tilde{Q}^{\dagger}}={}^{\natural}\tilde{Q}$ and $\Theta_{\tilde{S}}=L_{\tilde{S}}R_{\tilde{S}^{\dagger}}$.

**Corollary (self-adjointness and skew-adjointness).**

$$
L_{\tilde{Q}}\ \text{is }J\text{-self-adjoint} \iff \tilde{Q}\in\mathbb{R}e_0,
\qquad
R_{\tilde{R}}\ \text{is }J\text{-self-adjoint} \iff \tilde{R}\in\mathbb{R}e_0,
$$
$$
\Theta_{\tilde{Q}}\ \text{is }J\text{-self-adjoint} \iff \tilde{Q}\in\mathbb{C}_{\mathbb{B}}\cup\mathbb{V}_{\mathbb{B}},
$$
$$
L_{\tilde{Q}}\ \text{is }J\text{-skew-adjoint} \iff \tilde{Q}\in i\mathbb{R}e_0.
$$

**Proof.** A left and a right multiplication coincide, $L_{\tilde{Q}}=R_{\tilde{R}}$, exactly when $\tilde{Q}=\tilde{R}$ and $\tilde{Q}$ is central. Hence $L_{\tilde{Q}}$ is $J$-self-adjoint, $R_{\bar{\tilde{Q}}}=L_{\tilde{Q}}$, exactly when $\bar{\tilde{Q}}=\tilde{Q}$ and $\tilde{Q}$ is central, that is $\tilde{Q}\in\mathbb{R}e_0$; the case of $R$ is symmetric. For the sandwich, $\Theta_{\tilde{S}}=\Theta_{\tilde{Q}}$ exactly when $\tilde{S}=\lambda\tilde{Q}$ for a phase $\lambda$; hence $\Theta_{\tilde{Q}}$ is $J$-self-adjoint, $\Theta_{{}^{\natural}\tilde{Q}}=\Theta_{\tilde{Q}}$, exactly when ${}^{\natural}\tilde{Q}$ is a phase multiple of $\tilde{Q}$, and since ${}^{\natural}$ acts as $\pm1$ on the eigenspaces this means $\tilde{Q}\in\mathbb{C}_{\mathbb{B}}$ (fixed, phase $1$) or $\tilde{Q}\in\mathbb{V}_{\mathbb{B}}$ (negated, phase $-1$). For the skew case, $R_{\bar{\tilde{Q}}}=-L_{\tilde{Q}}=L_{-\tilde{Q}}$ gives $\bar{\tilde{Q}}=-\tilde{Q}$ and $\tilde{Q}$ central, that is $\tilde{Q}\in i\mathbb{R}e_0$.

**Remark (the contrast with the Hermitian case).** The definite sibling has $L_{\tilde{Q}}$ self-adjoint exactly on the Hermitian sector $\mathbb{M}_{+}$ and skew-adjoint exactly on the anti-Hermitian sector $\mathbb{M}_{-}$, a two-sector alternative, and a nonzero two-sided operator is never skew-adjoint. Indefinitely the split is different in kind: the $J$-self-adjoint left multiplications are only the real scalars, because the adjoint has crossed to the other side, and the sandwich is $J$-self-adjoint on the union of the two eigenspaces of ${}^{\natural}$, the centre and the vector subspace.

## The $J$-Unitary Operators

**Theorem (unitarity criteria).**

$$
L_{\tilde{Q}}\ \text{is }J\text{-unitary}\iff\tilde{Q}\in S^{1}e_0,
\qquad
\Theta_{\tilde{Q}}\ \text{is }J\text{-unitary}\iff |N(\tilde{Q})|=1.
$$

**Proof.** $L_{\tilde{Q}}^{\dagger}L_{\tilde{Q}}=R_{\bar{\tilde{Q}}}L_{\tilde{Q}}$, and $R_{\bar{\tilde{Q}}}L_{\tilde{Q}}(\tilde{V})=\bar{\tilde{Q}}\tilde{V}\tilde{Q}$; this is the identity exactly when $\tilde{Q}$ is central and $\bar{\tilde{Q}}\tilde{Q}=e_0$, that is $\tilde{Q}\in S^{1}e_0$. For the sandwich, $\Theta_{\tilde{Q}}^{\dagger}\Theta_{\tilde{Q}}=\Theta_{{}^{\natural}\tilde{Q}}\Theta_{\tilde{Q}}=\Theta_{{}^{\natural}\tilde{Q}\cdot\tilde{Q}}=\Theta_{N(\tilde{Q})e_0}$, since ${}^{\natural}\tilde{Q}\cdot\tilde{Q}=N(\tilde{Q})e_0$ — the identity $\mathrm{adj}(M)M=\det(M)I$ in the matrix model; and $\Theta_{\tilde{W}}=\mathrm{id}$ exactly when $\tilde{W}\in U(1)e_0$, so the condition is $|N(\tilde{Q})|=1$.

**Corollary (the $J$-unitary operators of the three families).** Among the left multiplications the $J$-unitary ones are exactly the central phases, $\tilde{Q}\in S^{1}e_0$; among the sandwiches they are exactly those with $|N(\tilde{Q})|=1$, and those act as the inner automorphisms by the unitaries of $U(\mathbb{B})$. Together they form the compact subgroup

$$
U(1)\times PU(2)\cong U(1)\times SO(3)
$$

of $U_{J}(\mathbb{B})$, of real dimension $4$ — far smaller than the whole group, which is the non-compact $U(1,3)$ of real dimension $16$ and contains the indefinite elements (*The Krein Isometry Group and Its $J$-Contractions*).

**Proof.** The two criteria are those of §*The $J$-Unitary Operators*. For the sandwich, $\Theta_{\tilde{Q}}$ with $|N(\tilde{Q})|=1$ depends only on the class of $\tilde{Q}$ in $U(\mathbb{B})/U(1)$, and $\Theta$ is the conjugation $X\mapsto\tilde{Q}X\tilde{Q}^{\dagger}$; the resulting class of maps is $PU(2)\cong SO(3)$. The central phases commute with every sandwich and with each other, so the generated subgroup is the direct product. The dimension count is $1+3$, against $\dim_{\mathbb{R}}U(1,3)=16$.

## Notes on the Indefinite Polar Decomposition

The general indefinite polar decomposition replaces the positive definite root of the Hermitian case by a $J$-positive root and holds only under a spectrum condition that the algebra's operators need not meet; the general statement is *J-Self-Adjoint and J-Unitary Operators*, §*The J-Positive Cone*, and *Krein Spaces*. The algebra always carries the Hermitian polar data, $\tilde{A}=\tilde{U}\tilde{P}$ of *The Unitary Group of the Biquaternion Algebra*, and its $J$-conjugate; the indefinite spectral consequences are *The Indefinite Spectra of the Operators on the Biquaternion Algebra*. No new polar decomposition is claimed here.

## The Indefinite Spectral Data

**Definition.** The **$J$-spectrum** of an operator $T$ is its spectrum as a complex-linear operator; the structure that matters is that $T$ is $J$-self-adjoint exactly when $JT$ is self-adjoint, so a $J$-self-adjoint operator is similar to its own adjoint, $JTJ=T^{*}$, and its spectrum is symmetric with respect to the real axis.

**Proposition.** For every $J$-self-adjoint $T$ the spectrum is symmetric under conjugation, $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$, and the multiplicities of $\lambda$ and $\bar\lambda$ agree.

**Proof.** $T^{*}=JTJ$ is similar to $T$, so the spectra coincide; but $\mathrm{spec}(T^{*})=\overline{\mathrm{spec}(T)}$ for every operator, and this is the symmetry; multiplicities agree because the algebraic multiplicities are invariant under similarity.

**Remark.** Unlike the Hermitian case, the spectrum of a $J$-self-adjoint operator is in general **not real**: the left multiplication $L_{e_1}$ is not $J$-self-adjoint, but the sandwich $\Theta_{e_1}$ is, and its spectrum is not real. The exact spectra of the three families under the $J$-adjoint are computed in *The Indefinite Spectra of the Operators on the Biquaternion Algebra*.

## Worked Examples

**The identity and the symmetry.** $L_{e_0}=\mathrm{id}$ is $J$-self-adjoint and $J$-unitary; $J={}^{\natural}$ is $J$-unitary with spectrum $\{+1,-1\}$.

**A real scalar.** $\tilde{Q}=te_0$, $t\in\mathbb{R}$: $L_{\tilde{Q}}$ is $J$-self-adjoint, and $J$-unitary only for $t=\pm1$; for $t\in i\mathbb{R}$ it is $J$-skew-adjoint.

**A vector element.** $\tilde{Q}=e_1$: $\Theta_{e_1}$ is $J$-self-adjoint (the parameter lies in $\mathbb{V}_{\mathbb{B}}$) and $J$-unitary (with $|N|=1$); $L_{e_1}$ is neither, its $J$-adjoint being $R_{e_1}\neq L_{e_1}$.

**A mixed element.** $\tilde{Q}=e_0+e_1$: $N(\tilde{Q})=2$, so $\Theta_{\tilde{Q}}$ is not $J$-unitary, and since $e_0+e_1$ lies in neither eigenspace of ${}^{\natural}$ the sandwich is not $J$-self-adjoint either.

**A central phase.** $\tilde{Q}=e^{i\theta}e_0$: $L_{\tilde{Q}}$ and $R_{\tilde{Q}}$ are $J$-unitary for every $\theta$, and $|\Theta_{\tilde{Q}}|=1$ as well, so the circle $S^{1}e_0$ is a common unitary subgroup in both senses.

## Summary

The **$J$-adjoint** $T^{\dagger}=JT^{*}J$ is the adjoint for the Krein form, characterised by $[T\tilde{Q},\tilde{Q}']=[\tilde{Q},T^{\dagger}\tilde{Q}']$, involutive and antimultiplicative. The dictionary with the definite case is $T$ is $J$-self-adjoint iff $JT$ is self-adjoint, and $T$ is $J$-unitary iff it preserves the Krein form, $T^{*}JT=J$; the $J$-unitary group is the indefinite unitary group $U_{J}(\mathbb{B})\cong U(1,3)$, of real dimension $16$ and non-compact, whose intersection with the algebra's three families is only the compact $U(1)\times SO(3)$. On the three families, $(L_{\tilde{Q}})^{\dagger}=R_{\bar{\tilde{Q}}}$, $(R_{\tilde{R}})^{\dagger}=L_{\bar{\tilde{R}}}$, $(L_{\tilde{Q}}R_{\tilde{R}})^{\dagger}=L_{\bar{\tilde{R}}}R_{\bar{\tilde{Q}}}$ and $(\Theta_{\tilde{Q}})^{\dagger}=\Theta_{{}^{\natural}\tilde{Q}}$: the indefinite adjoint of a left multiplication is a right multiplication. Hence $L_{\tilde{Q}}$ is $J$-self-adjoint exactly for $\tilde{Q}\in\mathbb{R}e_0$ and $J$-skew-adjoint exactly for $\tilde{Q}\in i\mathbb{R}e_0$; $L_{\tilde{Q}}$ is $J$-unitary exactly for $\tilde{Q}\in S^{1}e_0$; and $\Theta_{\tilde{Q}}$ is $J$-self-adjoint exactly for $\tilde{Q}$ in the centre or the vector subspace and $J$-unitary exactly when $|N(\tilde{Q})|=1$. Every $J$-self-adjoint operator has a spectrum symmetric about the real axis, but in general not real.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\dagger}=JT^{*}J$ | The $J$-adjoint; $[T\tilde{Q},\tilde{Q}']=[\tilde{Q},T^{\dagger}\tilde{Q}']$ |
| $U_{J}(\mathbb{B})=\{T:T^{*}JT=J\}$ | The $J$-unitary group, $\cong U(1,3)$; real dimension $16$ |
| $U(1)\times SO(3)$ | The $J$-unitaries among the left and two-sided multiplications |
| $T$ $J$-unitary $\iff T^{*}JT=J$ | Preservation of the Krein form |
| $(L_{\tilde{Q}})^{\dagger}=R_{\bar{\tilde{Q}}}$, $(R_{\tilde{R}})^{\dagger}=L_{\bar{\tilde{R}}}$ | The adjoints exchange the sides |
| $(\Theta_{\tilde{Q}})^{\dagger}=\Theta_{{}^{\natural}\tilde{Q}}$ | The $J$-adjoint of a sandwich |
| $L_{\tilde{Q}}$ $J$-self-adjoint $\iff\tilde{Q}\in\mathbb{R}e_0$ | Self-adjointness criterion |
| $L_{\tilde{Q}}$ $J$-unitary $\iff\tilde{Q}\in S^{1}e_0$ | Unitarity criterion |
| $\Theta_{\tilde{Q}}$ $J$-self-adjoint $\iff\tilde{Q}\in\mathbb{C}_{\mathbb{B}}\cup\mathbb{V}_{\mathbb{B}}$ | Self-adjointness of the sandwich |
| $\Theta_{\tilde{Q}}$ $J$-unitary $\iff\lvert N(\tilde{Q})\rvert=1$ | Unitarity of the sandwich |
| $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$ | Symmetry of the spectrum of a $J$-self-adjoint operator |

## Further Reading

- *J-Self-Adjoint and J-Unitary Operators* (`articles_maths/j-self-adjoint-and-j-unitary-operators.md`), for the general theory of the indefinite adjoint and the $J$-positive cone
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the symmetry $J={}^{\natural}$ and the bridge identity
- *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the form whose adjoint this is
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`, `articles_maths/one-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the definite counterparts
- *The Krein Isometry Group and Its $J$-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`), for the indefinite unitary group $U(1,3)$ and its maximal compact part
- *The Indefinite Spectra of the Operators on the Biquaternion Algebra* (`articles_maths/the-indefinite-spectra-of-the-operators-on-the-biquaternion-algebra.md`), for the spectral computations
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the indefinite adjoint and its normal forms
