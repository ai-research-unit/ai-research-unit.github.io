# __J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra__

## Introduction

The fundamental symmetry $J={}^{\natural}$ equips the biquaternion algebra with a second adjoint operation: alongside the Hermitian adjoint ${}^{*}$ of *Two-Sided Operators on the General Plain Sesqualgebra* and *One-Sided Operators on the General Plain Sesqualgebra*, there is the adjoint for the general quaternionic sesquilinear form,

$$
T^{\dagger}=J\,T^{*}J,
$$

for which the operators of the algebra can be self-adjoint, skew-adjoint, unitary or normal. This article computes that adjoint on the three operator families of the corpus — the left multiplications $L_{\tilde{Q}}$, the right multiplications $R_{\tilde{Q}}$ and the sandwiches $\Theta_{\tilde{Q}}$ — and reads off the indefinite counterparts of the self-adjointness, skew-adjointness, unitarity and normality of the Hermitian case. The single structural surprise is that the indefinite adjoint of a left multiplication is a **right** multiplication: the form built from the trace of a product does not see the order, so $J$ exchanges the sides.

The general theory is *J-Self-Adjoint and J-Unitary Operators* and *Krein Spaces*; the form is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; its symmetry and the bridge are *The Fundamental Symmetry of the Form*; the definite counterpart is *Two-Sided Operators on the General Plain Sesqualgebra* and *One-Sided Operators on the General Plain Sesqualgebra*; the spectral consequences are in §*The Indefinite Spectral Data*.

## The $J$-Adjoint

**Proposition (characterisation and calculus).** $T^{\dagger}=JT^{*}J$ is the unique operator with

$$
\boxed{\; \langle\tilde{Q}_1,T\tilde{Q}_2\rangle_{\natural*}=\langle T^{\dagger}\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}\qquad\text{for all }\tilde{Q}_1,\tilde{Q}_2\in\mathbb{B} \;},
$$

it is involutive, $(T^{\dagger})^{\dagger}=T$, and antimultiplicative,

$$
(TS)^{\dagger}=S^{\dagger}T^{\dagger},\qquad (\alpha T+\beta S)^{\dagger}=\bar\alpha T^{\dagger}+\bar\beta S^{\dagger}.
$$

**Proof.** $\langle\tilde{Q}_1,T\tilde{Q}_2\rangle_{\natural*}=\langle JT\tilde{Q}_2,\tilde{Q}_1\rangle=\langle\tilde{Q}_2,T^{*}J\tilde{Q}_1\rangle=\langle J\tilde{Q}_2,J(JT^{*}J)\tilde{Q}_1\rangle=\langle T^{\dagger}\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}$; uniqueness is the non-degeneracy of the form; the calculus is that of ${}^{*}$ conjugated by the involutive $J$.

**Corollary (the definite–indefinite dictionary).** $T$ is $J$-self-adjoint iff $JT$ is self-adjoint for $\langle\cdot,\cdot\rangle$, and $J$-skew-adjoint iff $JT$ is skew-adjoint; so $T\mapsto JT$ is a bijection from the $J$-self-adjoint operators onto the Hermitian-self-adjoint ones. $T$ is $J$-unitary iff it preserves the general quaternionic sesquilinear form,

$$
\langle T\tilde{Q}_1,T\tilde{Q}_2\rangle_{\natural*}=\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*},\qquad\text{that is}\qquad T^{*}JT=J,
$$

and the $J$-unitary operators form the **indefinite unitary group**

$$
U_{J}(\mathbb{B})=\{T:T^{*}JT=J\}\cong \mathrm{U}(1,3),
$$

of real dimension $16$. Its unitary subgroup is $\mathrm{U}(1)\times \mathrm{U}(3)$, the automorphisms of the canonical fundamental decomposition.

**Proof.** $T^{\dagger}=T\iff JT^{*}J=T\iff (JT)^{*}=JT$, and replacing $T$ by $-T$ gives the skew case. For unitarity, $\langle T\tilde{Q}_1,T\tilde{Q}_2\rangle_{\natural*}=\langle JT\tilde{Q}_2,T\tilde{Q}_1\rangle=\langle\tilde{Q}_2,T^{*}JT\tilde{Q}_1\rangle$ while $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}=\langle J\tilde{Q}_2,\tilde{Q}_1\rangle=\langle\tilde{Q}_2,J\tilde{Q}_1\rangle$, so preservation is exactly $T^{*}JT=J$, which is $T^{\dagger}T=e_t$. In the coefficient basis $J$ has the matrix $E=\mathrm{diag}(1,-1,-1,-1)$ and $T^{*}$ is the conjugate transpose, so that equation reads $T^{*}ET=E$: it defines $\mathrm{U}(1,3)$, the automorphism group of an indefinite general plain sesquilinear form of signature $(1,3)$. The group has real dimension $16$, and the matrices that also preserve the two eigenspaces of $J$ are $\mathrm{U}(1)\times \mathrm{U}(3)$ (*The Krein Isometry Group and Its Cartan Decomposition*).

**Remark (what the dictionary does *not* say).** There is no reduction of $J$-unitarity to definite unitarity: $JTJ$ is not unitary for a general $J$-unitary $T$, and $U_{J}(\mathbb{B})$ is not isomorphic to the definite unitary group $\mathrm{U}(4)$. The definite unitary groups that do occur are the subgroups listed in the next sections.

**Example.** $J$ itself is $J$-unitary, $J^{\dagger}=JJ^{*}J=J$ and $J^{2}=\mathrm{id}$, though $J$ is not Hermitian-unitary (it is Hermitian-self-adjoint with spectrum $\{+1,-1\}$).

## The $J$-Adjoint of the Three Families

The natural conjugation exchanges the sides, and this propagates to the adjoints.

**Theorem (the adjoints).** For all $\tilde{Q},\tilde Q_3\in\mathbb{B}$,

$$
\boxed{\; \bigl(L_{\tilde{Q}}\bigr)^{\dagger}=R_{\bar{\tilde{Q}}},\qquad
\bigl(R_{\tilde Q_3}\bigr)^{\dagger}=L_{\bar{\tilde Q_3}},\qquad
\bigl(L_{\tilde{Q}}R_{\tilde Q_3}\bigr)^{\dagger}=L_{\bar{\tilde Q_3}}R_{\bar{\tilde{Q}}},\qquad
\bigl(\Theta_{\tilde{Q}}\bigr)^{\dagger}=\Theta_{{}^{\natural}\tilde{Q}} \;},
$$

where $\bar{\tilde{Q}}$ is the coefficient conjugate and ${}^{\natural}\tilde{Q}$ the natural conjugate of the parameter.

**Proof.** By the anti-automorphism property of ${}^{\natural}$, ${}^{\natural}L_{\tilde{Q}}{}^{\natural}=R_{\tilde{Q}^{\natural}}$ and ${}^{\natural}R_{\tilde Q_3}{}^{\natural}=L_{\tilde Q_3^{\natural}}$ (*The Biquaternion Algebra*, §*The Conjugations and the Classification*). Hence $L_{\tilde{Q}}^{\dagger}={}^{\natural}L_{\tilde{Q}}^{*}{}^{\natural}={}^{\natural}L_{\tilde{Q}^{*}}{}^{\natural}=R_{\tilde{Q}^{*\natural}}$, and $\tilde{Q}^{*\natural}=(\tilde{Q}^{*})^{\natural}=\overline{\tilde{Q}}$ because ${}^{*}$ and ${}^{\natural}$ commute; the second is the same with left and right interchanged. The third follows by antimultiplicativity, $(L_{\tilde{Q}}R_{\tilde Q_3})^{\dagger}=R_{\tilde Q_3}^{\dagger}L_{\tilde{Q}}^{\dagger}=L_{\bar{\tilde Q_3}}R_{\bar{\tilde{Q}}}$. For the sandwich, $\Theta_{\tilde{Q}}=L_{\tilde{Q}}R_{\tilde{Q}^{*}}$, so $\Theta_{\tilde{Q}}^{\dagger}=R_{\tilde{Q}^{*}}^{\dagger}L_{\tilde{Q}}^{\dagger}=L_{\overline{\tilde{Q}^{*}}}R_{\bar{\tilde{Q}}}=L_{{}^{\natural}\tilde{Q}}R_{\bar{\tilde{Q}}}=\Theta_{{}^{\natural}\tilde{Q}}$, using $\overline{\tilde{Q}^{*}}={}^{\natural}\tilde{Q}$ and $\Theta_{\tilde{S}}=L_{\tilde{S}}R_{\tilde{S}^{*}}$.

**Corollary (self-adjointness and skew-adjointness).**

$$
L_{\tilde{Q}}\ \text{is }J\text{-self-adjoint} \iff \tilde{Q}\in\mathbb{R}e_t,
\qquad
R_{\tilde Q_3}\ \text{is }J\text{-self-adjoint} \iff \tilde Q_3\in\mathbb{R}e_t,
$$
$$
\Theta_{\tilde{Q}}\ \text{is }J\text{-self-adjoint} \iff \tilde{Q}\in\mathbb{C}_{\mathbb{B}}\cup\mathbb{V}_{\mathbb{B}},
$$
$$
L_{\tilde{Q}}\ \text{is }J\text{-skew-adjoint} \iff \tilde{Q}\in i\mathbb{R}e_t.
$$

**Proof.** A left and a right multiplication coincide, $L_{\tilde{Q}}=R_{\tilde Q_3}$, exactly when $\tilde{Q}=\tilde Q_3$ and $\tilde{Q}$ is central. Hence $L_{\tilde{Q}}$ is $J$-self-adjoint, $R_{\bar{\tilde{Q}}}=L_{\tilde{Q}}$, exactly when $\bar{\tilde{Q}}=\tilde{Q}$ and $\tilde{Q}$ is central, that is $\tilde{Q}\in\mathbb{R}e_t$; the case of $R$ is symmetric. For the sandwich, $\Theta_{\tilde{S}}=\Theta_{\tilde{Q}}$ exactly when $\tilde{S}=\lambda\tilde{Q}$ for a phase $\lambda$; hence $\Theta_{\tilde{Q}}$ is $J$-self-adjoint, $\Theta_{{}^{\natural}\tilde{Q}}=\Theta_{\tilde{Q}}$, exactly when ${}^{\natural}\tilde{Q}$ is a phase multiple of $\tilde{Q}$, and since ${}^{\natural}$ acts as $\pm1$ on the eigenspaces this means $\tilde{Q}\in\mathbb{C}_{\mathbb{B}}$ (fixed, phase $1$) or $\tilde{Q}\in\mathbb{V}_{\mathbb{B}}$ (negated, phase $-1$). For the skew case, $R_{\bar{\tilde{Q}}}=-L_{\tilde{Q}}=L_{-\tilde{Q}}$ gives $\bar{\tilde{Q}}=-\tilde{Q}$ and $\tilde{Q}$ central, that is $\tilde{Q}\in i\mathbb{R}e_t$.

**Remark (the contrast with the Hermitian case).** The definite sibling has $L_{\tilde{Q}}$ self-adjoint exactly on the Hermitian sector $\mathbb{M}_{+}$ and skew-adjoint exactly on the anti-Hermitian sector $\mathbb{M}_{-}$, a two-sector alternative, and a nonzero two-sided operator is never skew-adjoint. Indefinitely the split is different in kind: the $J$-self-adjoint left multiplications are only the real scalars, because the adjoint has crossed to the other side, and the sandwich is $J$-self-adjoint on the union of the two eigenspaces of ${}^{\natural}$, the centre and the vector subspace.

## The $J$-Unitary Operators

**Theorem (unitarity criteria).**

$$
\boxed{\; L_{\tilde{Q}}\ \text{is }J\text{-unitary}\iff\tilde{Q}\in S^{1}e_t,
\qquad
\Theta_{\tilde{Q}}\ \text{is }J\text{-unitary}\iff |\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|=1 \;}.
$$

**Proof.** $L_{\tilde{Q}}^{\dagger}L_{\tilde{Q}}=R_{\bar{\tilde{Q}}}L_{\tilde{Q}}$, and $R_{\bar{\tilde{Q}}}L_{\tilde{Q}}(\tilde Q_2)=\bar{\tilde{Q}}\tilde Q_2\tilde{Q}$; this is the identity exactly when $\tilde{Q}$ is central and $\bar{\tilde{Q}}\tilde{Q}=e_t$, that is $\tilde{Q}\in S^{1}e_t$. For the sandwich, $\Theta_{\tilde{Q}}^{\dagger}\Theta_{\tilde{Q}}=\Theta_{{}^{\natural}\tilde{Q}}\Theta_{\tilde{Q}}=\Theta_{{}^{\natural}\tilde{Q}\cdot\tilde{Q}}=\Theta_{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}e_t}$, since ${}^{\natural}\tilde{Q}\cdot\tilde{Q}=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}e_t$ — the identity $\mathrm{adj}(M)M=\det(M)I$ in the matrix model; and $\Theta_{\tilde{Q}}=\mathrm{id}$ exactly when $\tilde{Q}\in \mathrm{U}(1)e_t$, so the condition is $|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|=1$.

**Corollary (the $J$-unitary operators of the three families).** Among the left multiplications the $J$-unitary ones are exactly the central phases, $\tilde{Q}\in S^{1}e_t$; among the sandwiches they are exactly those with $|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|=1$, and those act as the inner automorphisms by the unitaries of $\mathrm{U}(\mathbb{B})$. Together they form the subgroup

$$
\mathrm{U}(1)\times PU(2)\cong \mathrm{U}(1)\times SO(3)
$$

of $U_{J}(\mathbb{B})$, of real dimension $4$ — far smaller than the whole group, which is the indefinite $\mathrm{U}(1,3)$ of real dimension $16$ and contains the indefinite elements (*The Krein Isometry Group and Its Cartan Decomposition*).

**Proof.** The two criteria are those of §*The $J$-Unitary Operators*. For the sandwich, $\Theta_{\tilde{Q}}$ with $|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|=1$ depends only on the class of $\tilde{Q}$ in $\mathrm{U}(\mathbb{B})/\mathrm{U}(1)$, and $\Theta$ is the conjugation $X\mapsto\tilde{Q}X\tilde{Q}^{*}$; the resulting class of maps is $PU(2)\cong SO(3)$. The central phases commute with every sandwich and with each other, so the generated subgroup is the direct product. The dimension count is $1+3$, against $\dim_{\mathbb{R}}\mathrm{U}(1,3)=16$.

## Notes on the Indefinite Polar Decomposition

The general indefinite polar decomposition replaces the positive definite root of the Hermitian case by a $J$-positive root and holds only under a spectrum condition that the algebra's operators need not meet; the general statement is *J-Self-Adjoint and J-Unitary Operators*, §*The J-Positive Cone*, and *Krein Spaces*. The algebra always carries the Hermitian polar data, $\tilde{Q}_4=\tilde{U}\tilde Q_5$ of *The Unitary Group of the Biquaternion Algebra*, and its $J$-conjugate; the indefinite spectral consequences are in §*The Indefinite Spectral Data*. No new polar decomposition is claimed here.

## The Indefinite Spectral Data

**Definition.** The **$J$-spectrum** of an operator $T$ is its spectrum as a complex-linear operator; the structure that matters is that $T$ is $J$-self-adjoint exactly when $JT$ is self-adjoint, so a $J$-self-adjoint operator is similar to its own adjoint, $JTJ=T^{*}$, and its spectrum is symmetric with respect to the real axis.

**Proposition.** For every $J$-self-adjoint $T$ the spectrum is symmetric under conjugation, $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$, and the multiplicities of $\lambda$ and $\bar\lambda$ agree.

**Proof.** $T^{*}=JTJ$ is similar to $T$, so the spectra coincide; but $\mathrm{spec}(T^{*})=\overline{\mathrm{spec}(T)}$ for every operator, and this is the symmetry; multiplicities agree because the algebraic multiplicities are invariant under similarity.

**Theorem (the spectra of the three families).** On the three families the $J$-self-adjoint operators and their spectra are the following.

1. A left or right multiplication is $J$-self-adjoint exactly for a real scalar parameter: $L_{te_t}$ and $R_{te_t}$ with $t\in\mathbb{R}$ have the spectrum $\{t\}$ with multiplicity four.
2. A sandwich with a nonzero central parameter $\tilde{Q}=\zeta e_t$ is $J$-self-adjoint with $\Theta_{\zeta e_t}=|\zeta|^{2}\mathrm{id}$, spectrum $\{|\zeta|^{2}\}$ with multiplicity four, and inertia $(4,0)$.
3. A sandwich with a vector parameter $\tilde{S}$ of nonzero norm is $J$-self-adjoint, with inertia $(2,2)$ and
    $$
    \mathrm{spec}(\Theta_{\tilde{S}})=\bigl\{|\langle\tilde{S},\tilde{S}\rangle_{\natural}|,\ |\langle\tilde{S},\tilde{S}\rangle_{\natural}|,\ -|\langle\tilde{S},\tilde{S}\rangle_{\natural}|,\ -|\langle\tilde{S},\tilde{S}\rangle_{\natural}|\bigr\}.
    $$
4. A sandwich with a null vector parameter, $\langle\tilde{S},\tilde{S}\rangle_{\natural}=0$, is nilpotent, $\Theta_{\tilde{S}}^{2}=0$, with spectrum $\{0\}$ of multiplicity four.

*Proof.* The criteria are those of §*The $J$-Adjoint of the Three Families*: the $J$-self-adjoint left multiplications are the real scalars, and the $J$-self-adjoint sandwiches have a parameter in the centre or in the vector subspace. For a central parameter, $\Theta_{\zeta e_t}(\tilde{Q}_2)=\zeta\tilde{Q}_2\bar\zeta=|\zeta|^{2}\tilde{Q}_2$. For a vector parameter, $\tilde{S}^{2}=-\langle\tilde{S},\tilde{S}\rangle_{\natural}e_t$ and $(\tilde{S}^{*})^{2}=-\overline{\langle\tilde{S},\tilde{S}\rangle_{\natural}}e_t$, hence
$$
\Theta_{\tilde{S}}^{2}(\tilde{Q}_2)=\tilde{S}^{2}\tilde{Q}_2(\tilde{S}^{*})^{2}=|\langle\tilde{S},\tilde{S}\rangle_{\natural}|^{2}\tilde{Q}_2,
$$
so $\Theta_{\tilde{S}}^{2}=|\langle\tilde{S},\tilde{S}\rangle_{\natural}|^{2}\mathrm{id}$. If the norm is nonzero, $\mathsf{M}_2(\tilde{S})$ is traceless with square $-\langle\tilde{S},\tilde{S}\rangle_{\natural}I$, hence diagonalisable with eigenvalues $\pm i\sqrt{\langle\tilde{S},\tilde{S}\rangle_{\natural}}$, and the product rule for the spectrum of the sandwich gives two positive and two negative eigenvalues. If the norm vanishes, $\tilde{S}^{2}=0$ and $(\tilde{S}^{*})^{2}=0$, so $\Theta_{\tilde{S}}^{2}=0$ and the only eigenvalue is $0$, with multiplicity four.

**Remark.** Unlike the Hermitian case, the spectrum of a $J$-self-adjoint operator is in general **not real**. The three families above are real with signs, but a mixed sum is not: $L_{\vec e_x}+R_{\vec e_x}$ is $J$-self-adjoint with the spectrum $\{2i,-2i,0,0\}$, symmetric about the real axis and not real. Away from the null case the spectrum of a $J$-self-adjoint sandwich has inertia $(4,0)$ for a central parameter and $(2,2)$ for a vector parameter; the null case is the one in which the operator is nilpotent and has no eigenbasis.

## J-Normality and the Definite-Spectrum Criterion

**Definition.** A $\mathbb{C}$-linear operator $T$ is **$J$-normal** when $T^{\dagger}T=TT^{\dagger}$.

**Theorem (closure).** Every $J$-self-adjoint and every $J$-unitary operator is $J$-normal. The $J$-normal operators are closed under the $J$-adjoint, under powers and inverses, and under $\mathbb{C}$-linear combinations of mutually commuting ones; those that are also $J$-self-adjoint form a real vector space, and those that are also $J$-unitary form a group.

*Proof.* For a $J$-self-adjoint operator $T^{\dagger}T=T^{2}=TT^{\dagger}$; for a $J$-unitary one both products are the identity. The adjoint of $T^{\dagger}$ is $T$, and $T^{\dagger}$ commutes with $T$ whenever $T$ does; powers and inverses follow by induction and by inversion of $T^{\dagger}T=TT^{\dagger}$; and for commuting $S,T$ every term in the expansion of $(S+T)^{\dagger}(S+T)$ and $(S+T)(S+T)^{\dagger}$ can be reordered to the same expression.

**Theorem (the definite model).** In the coefficient basis, with $T^{*}$ the conjugate transpose and $E=\operatorname{diag}(1,-1,-1,-1)$, the operator $T$ is $J$-normal if and only if
$$
T^{*}ETE=ETET^{*},
$$
equivalently if and only if $T^{*}$ commutes with $JTJ$.

*Proof.* $T^{\dagger}=ET^{*}E$, so $T^{\dagger}T=ET^{*}ET$ and $TT^{\dagger}=TET^{*}E$; multiplying $ET^{*}ET=TET^{*}E$ by $E$ on both sides gives $T^{*}ETE=ETET^{*}$, which is $T^{*}(ETE)=(ETE)T^{*}$.

**Theorem (the definite-spectrum case).** Let $T$ be $J$-self-adjoint and suppose that $JT$ is positive definite for $\langle\cdot,\cdot\rangle_{*}$. Then $T$ has real spectrum and is diagonalisable over $\mathbb{C}$.

*Proof.* Write $S=JT$, positive definite and self-adjoint. Then $T=ES$ and
$$
S^{1/2}\,T\,S^{-1/2}=S^{1/2}ES^{1/2},
$$
an operator that is self-adjoint for $\langle\cdot,\cdot\rangle_{*}$, since $S^{1/2}$ and $E$ are; it is therefore diagonalisable with real eigenvalues, and $T$, being similar to it, is diagonalisable with the same real spectrum.

**Remark (the semidefinite case fails the conclusion).** The hypothesis cannot be weakened to positive semidefiniteness. With $E=\operatorname{diag}(1,-1,-1,-1)$ and $S=|\tilde{Q}\rangle\langle\tilde{Q}|$ the rank-one operator of the isotropic element $\tilde{Q}=e_t+\vec e_x$, the operator $T=ES$ is $J$-self-adjoint and lies in the $J$-positive cone, while $T^{2}=0$ and $T\neq0$: it is nilpotent, has spectrum $\{0\}$, and is not diagonalisable.

**Theorem (the $J$-unitary spectrum).** If $T$ is $J$-unitary then
$$
\lambda\in\mathrm{spec}(T)\iff\frac{1}{\bar\lambda}\in\mathrm{spec}(T),
$$
with the same multiplicity; in particular an eigenvalue on the unit circle has its conjugate present as well, but the spectrum is in general not contained in the unit circle.

*Proof.* $T$ is $J$-unitary exactly when $T^{*}ET=E$, that is $T^{*}=ET^{-1}E$; so $T^{*}$ is similar to $T^{-1}$, whence the characteristic polynomials of $T^{*}$ and $T^{-1}$ agree, and $\mathrm{spec}(T^{-1})=\{\lambda^{-1}:\lambda\in\mathrm{spec}(T)\}$ while $\mathrm{spec}(T^{*})=\overline{\mathrm{spec}(T)}$. The boost $e_t\mapsto\cosh t\,e_t+\sinh t\,\vec e_x$, $\vec e_x\mapsto\sinh t\,e_t+\cosh t\,\vec e_x$, with $\vec e_y,\vec e_z$ fixed, is $J$-unitary with eigenvalues $e^{t},e^{-t},1,1$, so the spectrum leaves the unit circle as soon as the operator moves the Lorentzian slice.

**Theorem (the three families are $J$-normal).** For every biquaternion $\tilde{Q}$ the operators $L_{\tilde{Q}}$, $R_{\tilde{Q}}$ and $\Theta_{\tilde{Q}}$ are $J$-normal: their $J$-adjoints are $R_{\bar{\tilde{Q}}}$, $L_{\bar{\tilde{Q}}}$ and $\Theta_{{}^{\natural}\tilde{Q}}$, and in each case the two factors of $T^{\dagger}T$ commute.

*Proof.* The adjoint formulas are those of §*The $J$-Adjoint of the Three Families*; a left multiplication commutes with every right multiplication, so $R_{\bar{\tilde Q}}L_{\tilde Q}=L_{\tilde Q}R_{\bar{\tilde Q}}$ and $L_{\bar{\tilde Q}}R_{\tilde Q}=R_{\tilde Q}L_{\bar{\tilde Q}}$. For the sandwich, $\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q}=\Theta_{\tilde Q^{\natural}}\Theta_{\tilde Q}=\Theta_{\tilde Q^{\natural}\tilde Q}$ and $\Theta_{\tilde Q}\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q\tilde Q^{\natural}}$, and $\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}$; the two products agree.

**Example (normality without reality).** $L_{\vec e_x}$ is $J$-normal, is not $J$-self-adjoint, and has the imaginary spectrum $\{i,-i\}$, each eigenvalue twice. In a positive definite space normality and a real spectrum together give self-adjointness; here normality, self-adjointness and reality of the spectrum are three independent conditions.

## Worked Examples

**The identity and the symmetry.** $L_{e_t}=\mathrm{id}$ is $J$-self-adjoint and $J$-unitary; $J={}^{\natural}$ is $J$-unitary with spectrum $\{+1,-1\}$.

**A real scalar.** $\tilde{Q}=te_t$, $t\in\mathbb{R}$: $L_{\tilde{Q}}$ is $J$-self-adjoint, and $J$-unitary only for $t=\pm1$; for $t\in i\mathbb{R}$ it is $J$-skew-adjoint.

**A vector element.** $\tilde{Q}=\vec e_x$: $\Theta_{\vec e_x}$ is $J$-self-adjoint (the parameter lies in $\mathbb{V}_{\mathbb{B}}$) and $J$-unitary (with $|N|=1$); $L_{\vec e_x}$ is neither, its $J$-adjoint being $R_{\vec e_x}\neq L_{\vec e_x}$.

**A mixed element.** $\tilde{Q}=e_t+\vec e_x$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=2$, so $\Theta_{\tilde{Q}}$ is not $J$-unitary, and since $e_t+\vec e_x$ lies in neither eigenspace of ${}^{\natural}$ the sandwich is not $J$-self-adjoint either.

**A central phase.** $\tilde{Q}=\exp(i\theta)e_t$: $L_{\tilde{Q}}$ and $R_{\tilde{Q}}$ are $J$-unitary for every $\theta$, and $|\Theta_{\tilde{Q}}|=1$ as well, so the circle $S^{1}e_t$ is a common unitary subgroup in both senses.

## Summary

The **$J$-adjoint** $T^{\dagger}=JT^{*}J$ is the adjoint for the general quaternionic sesquilinear form, characterised by $\langle\tilde{Q}_1,T\tilde{Q}_2\rangle_{\natural*}=\langle T^{\dagger}\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}$, involutive and antimultiplicative. The dictionary with the definite case is $T$ is $J$-self-adjoint iff $JT$ is self-adjoint, and $T$ is $J$-unitary iff it preserves the general quaternionic sesquilinear form, $T^{*}JT=J$; the $J$-unitary group is the indefinite unitary group $U_{J}(\mathbb{B})\cong \mathrm{U}(1,3)$, of real dimension $16$, whose intersection with the algebra's three families is only the definite unitary group $\mathrm{U}(1)\times SO(3)$. On the three families, $(L_{\tilde{Q}})^{\dagger}=R_{\bar{\tilde{Q}}}$, $(R_{\tilde Q_3})^{\dagger}=L_{\bar{\tilde Q_3}}$, $(L_{\tilde{Q}}R_{\tilde Q_3})^{\dagger}=L_{\bar{\tilde Q_3}}R_{\bar{\tilde{Q}}}$ and $(\Theta_{\tilde{Q}})^{\dagger}=\Theta_{{}^{\natural}\tilde{Q}}$: the indefinite adjoint of a left multiplication is a right multiplication. Hence $L_{\tilde{Q}}$ is $J$-self-adjoint exactly for $\tilde{Q}\in\mathbb{R}e_t$ and $J$-skew-adjoint exactly for $\tilde{Q}\in i\mathbb{R}e_t$; $L_{\tilde{Q}}$ is $J$-unitary exactly for $\tilde{Q}\in S^{1}e_t$; and $\Theta_{\tilde{Q}}$ is $J$-self-adjoint exactly for $\tilde{Q}$ in the centre or the vector subspace and $J$-unitary exactly when $|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|=1$. Every $J$-self-adjoint operator has a spectrum symmetric about the real axis, but in general not real. On the three families the spectra are real: the $J$-self-adjoint left and right multiplications are the real scalars, with spectrum that scalar of multiplicity four; a sandwich with a nonzero central parameter has spectrum $\{|\zeta|^{2}\}$ and inertia $(4,0)$; a sandwich with a vector parameter of nonzero norm has the pair $\pm|\langle\tilde{S},\tilde{S}\rangle_{\natural}|$, each twice, and inertia $(2,2)$; and a sandwich with a null vector parameter is nilpotent, with spectrum $\{0\}$ of multiplicity four. A **$J$-normal** operator is one commuting with its $J$-adjoint; the three families are $J$-normal, but normality does not force a real spectrum, and the definite-spectrum criterion — $J$-self-adjoint with $JT$ positive definite — restores real spectra and diagonalisability.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\dagger}=JT^{*}J$ | The $J$-adjoint; $\langle\tilde{Q}_1,T\tilde{Q}_2\rangle_{\natural*}=\langle T^{\dagger}\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}$ |
| $U_{J}(\mathbb{B})=\{T:T^{*}JT=J\}$ | The $J$-unitary group, $\cong \mathrm{U}(1,3)$; real dimension $16$ |
| $\mathrm{U}(1)\times SO(3)$ | The $J$-unitaries among the left and two-sided multiplications |
| $T$ $J$-unitary $\iff T^{*}JT=J$ | Preservation of the general quaternionic sesquilinear form |
| $(L_{\tilde{Q}})^{\dagger}=R_{\bar{\tilde{Q}}}$, $(R_{\tilde Q_3})^{\dagger}=L_{\bar{\tilde Q_3}}$ | The adjoints exchange the sides |
| $(\Theta_{\tilde{Q}})^{\dagger}=\Theta_{{}^{\natural}\tilde{Q}}$ | The $J$-adjoint of a sandwich |
| $T^{\dagger}T=TT^{\dagger}$ | $J$-normality |
| $T^{*}ETE=ETET^{*}$, or $[JTJ,T^{*}]=0$ | $J$-normality in the coefficient basis |
| $JT$ positive definite | The definite-spectrum criterion: real spectrum and diagonalisability |
| $L_{\tilde{Q}}$ $J$-self-adjoint $\iff\tilde{Q}\in\mathbb{R}e_t$ | Self-adjointness criterion |
| $L_{\tilde{Q}}$ $J$-unitary $\iff\tilde{Q}\in S^{1}e_t$ | Unitarity criterion |
| $\Theta_{\tilde{Q}}$ $J$-self-adjoint $\iff\tilde{Q}\in\mathbb{C}_{\mathbb{B}}\cup\mathbb{V}_{\mathbb{B}}$ | Self-adjointness of the sandwich |
| $\Theta_{\tilde{Q}}$ $J$-unitary $\iff\lvert \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\rvert=1$ | Unitarity of the sandwich |
| $\mathrm{spec}(T)=\overline{\mathrm{spec}(T)}$ | Symmetry of the spectrum of a $J$-self-adjoint operator |
| $\lambda\in\mathrm{spec}(T)\iff1/\bar\lambda\in\mathrm{spec}(T)$ | Symmetry of the spectrum of a $J$-unitary operator |

## Further Reading

- [J-Self-Adjoint and J-Unitary Operators](j-self-adjoint-and-j-unitary-operators.html), for the general theory of the indefinite adjoint, the $J$-positive cone, $J$-normality and the definite-spectrum criterion
- [The Fundamental Symmetry of the Form](the-fundamental-symmetry-of-the-form.html), for the symmetry $J={}^{\natural}$, the fundamental decomposition and the bridge identity.
- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html) and [One-Sided Operators on the General Plain Sesqualgebra](one-sided-operators-on-the-general-plain-sesqualgebra.html), for the definite counterparts
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the indefinite unitary group $\mathrm{U}(1,3)$ and its maximal compact part
- [The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion](two-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), §*The Spectrum of the Sandwich*, for the definite spectra against which the indefinite signs are read
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the indefinite adjoint and its normal forms
