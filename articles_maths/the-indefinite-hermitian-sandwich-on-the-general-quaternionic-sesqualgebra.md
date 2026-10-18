# __The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries two general plain sesquilinear forms of different type. The first is the **definite** form of the dagger, $(\tilde Q,\tilde W) = \mathrm{Sc}(\tilde Q^{*}\tilde W)$, positive definite of signature $(4,0)$, on which the whole definite operator theory is built (*Two-Sided Operators on the General Plain Sesqualgebra*). The second is the **general quaternionic sesquilinear form** $\langle\tilde W,\tilde Q\rangle_{\natural*} = \mathrm{Sc}(\tilde Q^{\natural*}\tilde W)$ of signature $(1,3)$, whose fundamental symmetry is the involution $J={}^{\natural}$ and whose automorphism group is $\mathrm{U}(1,3)$ (*The Krein Gram Matrix and the Restrictions of the Form*, *The Fundamental Symmetry of the Biquaternioid Algebra*, *The Krein Isometry Group and Its J-Contractions*). On a Krein space the sandwich by an operator $A$ — the operator's letter, the bare glyph $Q$ staying with the element of $\mathbb{B}$ — is formed with the **indefinite adjoint** $A^{\dagger} = JA^{*}J$ rather than with $A^{*}$,

$$
H_{A}(T) = A\,T\,A^{\dagger} ,
$$

and this operator is the subject of the article. It is the biquaternion instance of *The Hermitian Sandwich on a Krein Space*, and the indefinite counterpart of the dagger sandwich $\Theta_{\tilde Q}(\tilde Q_1) = \tilde Q\tilde Q_1\tilde Q^{*}$ of *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*.

The two sandwiches must not be confused, and the algebra makes the difference visible in coordinates. With the definite adjoint the sandwich is always an operator of the algebra's own family $\{\Theta_{\tilde Q}\}$ and the operator is quadratic in the parameter; with the indefinite adjoint the sandwich of a $J$-unitary parameter is an **inner automorphism of the operator algebra**, and the parameter families that are $J$-unitary are exactly the ones computed in *The Krein Isometry Group and Its J-Contractions*. The article determines the sandwich laws, the preservation of the indefinite form, of $J$-self-adjointness and of $J$-positivity, the transport of the kernel and the image, the parameters coming from the algebra, and the contrast with the definite case.

The forms and the algebra are *The Biquaternioid as a Vector Space over $\mathbb{C}$*; the definite form and the dagger sandwich are *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* and *Two-Sided Operators on the General Plain Sesqualgebra*; the indefinite form, its symmetry and its adjoint are *The Krein Gram Matrix and the Restrictions of the Form*, *The Fundamental Symmetry of the Biquaternioid Algebra* and *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*; the positive cone of the indefinite order is *Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*; the group of $J$-unitary parameters is *The Krein Isometry Group and Its J-Contractions*; and the general operator is *The Hermitian Sandwich on a Krein Space*.

**Conventions.** The algebra is read in the coefficient basis $e_t,\vec e_x,\vec e_y,\vec e_z$, so that $\tilde Q = \sum_\mu Q_\mu e_\mu$ is a vector of coefficients; the definite form is $(\tilde Q,\tilde W) = \sum_\mu\overline{Q_\mu}W_\mu$ and the general quaternionic sesquilinear form is $\langle\tilde W,\tilde Q\rangle_{\natural*} = \sum_\mu\varepsilon_\mu\overline{Q_\mu}W_\mu$ with $\varepsilon = (1,-1,-1,-1)$. The fundamental symmetry is $J={}^{\natural}$, the operator $\tilde Q\mapsto \tilde Q^{\natural}$ of matrix $E = \mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis, and

$$
\langle\tilde W,\tilde Q\rangle_{\natural*} = (J\tilde Q,\tilde W) , \qquad J^{2} = \mathrm{id}, \qquad E^{2} = \mathrm{I}_4 .
$$

The Krein adjoint of a $\mathbb{C}$-linear operator is $A^{\dagger} = JA^{*}J$, where $A^{*}$ is its adjoint for the definite form. Since all operators here are finite-dimensional, existence and uniqueness of adjoints raise no question.

## The Coefficient Model of the Form

**Proposition (the coefficient model).** Under the $\mathbb{C}$-linear identification $\tilde Q\mapsto(Q_t,Q_x,Q_y,Q_z)$ of $\mathbb{B}$ with $\mathbb{C}^{4}$, the general quaternionic sesquilinear form is the standard form of signature $(1,3)$,

$$
\langle\tilde W,\tilde Q\rangle_{\natural*} = \overline{Q_t}W_t - \overline{Q_x}W_x - \overline{Q_y}W_y - \overline{Q_z}W_z ,
$$

and the fundamental symmetry is the diagonal operator $J = \mathrm{diag}(1,-1,-1,-1)$, self-adjoint for both forms, with $J^{2}=\mathrm{id}$ and with the twisted form $\langle\tilde W,\tilde Q\rangle_{\natural*} = (J\tilde Q,\tilde W)$.

*Proof.* Immediate from the definitions in the coefficient basis; the diagonal of the definite form is $\mathrm{I}_4$ and the diagonal of the general quaternionic sesquilinear form is $E$, so $\langle\tilde W,\tilde Q\rangle_{\natural*} = \tilde Q^{\mathsf T*}E\tilde W = (E\tilde Q,\tilde W) = (J\tilde Q,\tilde W)$.

**Remark (four forms, not one).** The quaternion norm $\langle\tilde Q,\tilde Q\rangle_{\natural} = \sum_\mu Q_\mu^{2}$ is a complex quadratic form, isotropic on the null cone of *Norm and Invertibility in the General Quaternionic Algebra*; the definite form $(\cdot,\cdot)$ is positive definite; the general quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$ is an indefinite Hermitian structure of signature $(1,3)$, split as $\mathbb{B} = \mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$ into the centre line and the vector subspace; and the general quaternionic bilinear form of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* is another object again. The four must not be interchanged, and it is the general quaternionic sesquilinear form that defines the adjoint of this article.

## The Dagger Sandwich

**Definition.** For operators $A,T\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ the **indefinite Hermitian sandwich**, or **dagger sandwich**, is

$$
H_{A}(T) = A\,T\,A^{\dagger} , \qquad A^{\dagger} = JA^{*}J .
$$

In the coefficient basis, where $A$ and $T$ are $4\times4$ complex matrices, this reads $H_{A}(T) = ATEA^{*}E$ with $E = \mathrm{diag}(1,-1,-1,-1)$.

**Proposition (the adjoint law).** For all operators $A,T$,

$$
H_{A}(T)^{\dagger} = H_{A}\bigl(T^{\dagger}\bigr) .
$$

*Proof.* $H_A(T)^{\dagger} = (ATA^{\dagger})^{\dagger} = A^{\dagger\dagger}T^{\dagger}A^{\dagger} = AT^{\dagger}A^{\dagger}$, because the operation $T\mapsto T^{\dagger}$ is an involution and an anti-involution: $J^{2}=\mathrm{id}$ gives $A^{\dagger\dagger}=A$. The right-hand side is $H_A(T^{\dagger})$ by definition.

**Proposition (composition and multiplicativity).** For all operators $A,S,T$,

$$
H_{A}\bigl(H_{S}(T)\bigr) = H_{AS}(T) , \qquad
H_{A}(ST) = H_{A}(S)\,H_{A}(T) \iff A^{\dagger}A = \mathrm{id} .
$$

*Proof.* The composition is associativity: $A(S\,T\,S^{\dagger})A^{\dagger} = (AS)T(AS)^{\dagger}$. For the second, $H_A(S)H_A(T) = ASA^{\dagger}ATA^{\dagger} = AS(A^{\dagger}A)TA^{\dagger}$, which equals $ASTA^{\dagger}=H_A(ST)$ identically exactly when $A^{\dagger}A=\mathrm{id}$.

**Proposition (the parameter rule).** For a complex scalar $\alpha$ and all $T$,

$$
H_{\alpha A}(T) = \lvert\alpha\rvert^{2}\,H_{A}(T) .
$$

*Proof.* $(\alpha A)^{\dagger} = J(\alpha A)^{*}J = \bar\alpha\,JA^{*}J = \bar\alpha\,A^{\dagger}$, so $(\alpha A)T(\bar\alpha A^{\dagger}) = \lvert\alpha\rvert^{2}ATA^{\dagger}$.

**Remark (linear in the argument, quadratic in the parameter).** The assignment $T\mapsto H_A(T)$ is linear in the argument and homogeneous of degree two in the parameter, and it is blind to the phase of the parameter. This is the operator-level form of the rule that the two-sided operator $\Theta_{\tilde Q}$ is quadratic in $\tilde Q$ (*Two-Sided Operators on the General Plain Sesqualgebra*), and it is the reason the sandwich is a map of the projective parameter, not a representation of the algebra.

## Preservation of the Form and of J-Positivity

**Theorem (form preservation by $J$-unitary parameters).** Let $A$ be $J$-unitary, $A^{\dagger}A = AA^{\dagger} = \mathrm{id}$. Then for every operator $T$ and all $\tilde Q,\tilde W\in\mathbb{B}$,

$$
\langle H_{A}(T)\tilde W,H_{A}(T)\tilde Q\rangle_{\natural*} = \langle TA^{\dagger}\tilde W,TA^{\dagger}\tilde Q\rangle_{\natural*} , \qquad
\langle \tilde W,H_{A}(T)\tilde Q\rangle_{\natural*} = \langle A^{\dagger}\tilde W,TA^{\dagger}\tilde Q\rangle_{\natural*} ,
$$

the first identity being the second applied twice; and $H_{A}(T)$ is a $J$-unitary operator whenever $T$ is.

*Proof.* The one-argument identity is the reading of the elementary rule $\langle\tilde S,A\tilde T\rangle_{\natural*} = \langle A^{\dagger}\tilde S,\tilde T\rangle_{\natural*}$, which holds for every operator $A$ and follows from $\langle\tilde S,\tilde T\rangle_{\natural*}=(J\tilde T,\tilde S)$ and $(A\tilde T,\tilde S)=(\tilde T,A^{*}\tilde S)$. With $\tilde T = TA^{\dagger}\tilde Q$ it gives $\langle\tilde W,ATA^{\dagger}\tilde Q\rangle_{\natural*} = \langle A^{\dagger}\tilde W,TA^{\dagger}\tilde Q\rangle_{\natural*}$; replacing $\tilde W$ by $H_A(T)\tilde W = ATA^{\dagger}\tilde W$ and applying the rule once more gives the first identity. If $T$ is a $J$-unitary operator then $\langle TA^{\dagger}\tilde W,TA^{\dagger}\tilde Q\rangle_{\natural*}=\langle A^{\dagger}\tilde W,A^{\dagger}\tilde Q\rangle_{\natural*}$, and $A^{\dagger}$ is $J$-unitary with $A$, so this is $\langle\tilde W,\tilde Q\rangle_{\natural*}$.

**Remark (the correction of the general display).** The general article states the second identity with $T\tilde Q$ in place of $TA^{\dagger}\tilde Q$; that reading is not correct, as the elementary rule shows, and the version above is the one the general proof uses. In the biquaternion algebra the distinction is not cosmetic, because $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ for an algebra element and the parameter cannot be moved across $T$ freely.

**Proposition (preservation of $J$-self-adjointness, $J$-positivity and $J$-unitarity).** For every operator $A$ and every $\tilde Q$,

$$
\langle\tilde Q,H_{A}(T)\tilde Q\rangle_{\natural*} = \langle A^{\dagger}\tilde Q,T\,A^{\dagger}\tilde Q\rangle_{\natural*} .
$$

Consequently, if $A$ is $J$-unitary then $H_{A}$ maps $J$-self-adjoint operators to $J$-self-adjoint operators, the $J$-positive cone to itself, and $J$-unitary operators to $J$-unitary operators.

*Proof.* The displayed identity is the elementary rule with $\tilde T=TA^{\dagger}\tilde Q$ and $\tilde S=\tilde Q$, and it holds for every $A$. If $T$ is $J$-self-adjoint then $H_A(T)^{\dagger}=H_A(T^{\dagger})=H_A(T)$ by the adjoint law; if $T$ is $J$-positive the display gives $\langle\tilde Q,H_A(T)\tilde Q\rangle_{\natural*}=\langle A^{\dagger}\tilde Q,TA^{\dagger}\tilde Q\rangle_{\natural*}\geq0$; and if $T$ is $J$-unitary then the multiplicativity of the second proposition applies to $T^{*}$ too.

**Theorem (kernel and image).** Let $A$ be invertible. Then for every $T$,

$$
\ker H_{A}(T) = \bigl(A^{\dagger}\bigr)^{-1}\bigl(\ker T\bigr) , \qquad \mathrm{im}\,H_{A}(T) = A\bigl(\mathrm{im}\,T\bigr) ,
$$

and for $J$-unitary $A$ these read $\ker H_{A}(T) = A\ker T$ and $\mathrm{im}\,H_{A}(T) = A\,\mathrm{im}\,T$.

*Proof.* $ATA^{\dagger}\tilde Q = 0$ iff $TA^{\dagger}\tilde Q=0$ because $A$ is invertible, so $\tilde Q\in\ker H_A(T)$ iff $A^{\dagger}\tilde Q\in\ker T$. The image statement is the same computation with the roles reversed, using the surjectivity of $A^{\dagger}$. For $J$-unitary $A$ one has $A^{\dagger}=A^{-1}$, hence $A\ker T$ and $A\,\mathrm{im}\,T$.

**Corollary (what the sandwich preserves).** For $J$-unitary $A$ the sandwich preserves the dimension of the kernel, the codimension and the dimension of the image, hence the rank of $T$; it preserves the $J$-orthogonal complement of the image and not the definite one.

*Proof.* $A$ is a bijective $J$-unitary operator, so it preserves dimensions and the indefinite orthogonality; it does not preserve $(\cdot,\cdot)$-orthogonality because a $J$-unitary operator need not be unitary, as the next sections show.

## The Parameters Coming from the Algebra

The parameters of the theory are the operators, and the algebra supplies three natural families of them: the left multiplications $L_{\tilde Q}$, the right multiplications $R_{\tilde Q}$ and the two-sided operators $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$. Their Krein adjoints and their $J$-unitarity are computed in *One-Sided Operators on the General Plain Sesqualgebra* and *The Krein Isometry Group and Its J-Contractions*; the results are collected here in the notation of the sandwich.

**Proposition (the Krein adjoints of the algebra families).** For every $\tilde Q\in\mathbb{B}$,

$$
\bigl(L_{\tilde Q}\bigr)^{\dagger} = R_{\bar{\tilde Q}} , \qquad
\bigl(R_{\tilde Q}\bigr)^{\dagger} = L_{\bar{\tilde Q}} ,
$$

with $\bar{\tilde Q} = \sum_\mu\overline{Q_\mu}e_\mu$ the coefficient conjugation.

*Proof.* In the coefficient basis $L_{\tilde Q}$ is left multiplication by $\tilde Q$ and the Krein adjoint is $E\,L_{\tilde Q}^{*}\,E$; the definite adjoint of $L_{\tilde Q}$ is $L_{\tilde Q^{*}}$ (*The Adjoint of the Left Multiplication on a Hermitian Algebra*), and conjugating it by $E$ replaces the Hermitian star by the coefficient conjugation, which is the natural involution composed with the star. The computation is the operator form of the identity $(L_{\tilde Q})^{\dagger} = R_{\bar{\tilde Q}}$ used throughout the indefinite theory of the algebra.

**Theorem ($J$-unitarity of the algebra parameters).** For $\tilde Q\in\mathbb{B}$,

$$
L_{\tilde Q}\ \text{is }J\text{-unitary} \iff \tilde Q\in S^{1}e_t , \qquad
R_{\tilde Q}\ \text{is }J\text{-unitary} \iff \tilde Q\in S^{1}e_t , \qquad
\Theta_{\tilde Q}\ \text{is }J\text{-unitary} \iff \lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert = 1 .
$$

*Proof.* This is the theorem of *The Krein Isometry Group and Its J-Contractions*, repeated because the sandwich needs it: $L_{\tilde Q}^{\dagger}L_{\tilde Q}$ is the operator $\tilde Q_1\mapsto\tilde Q\tilde Q_1\bar{\tilde Q}$, which is the identity only for central phases; and $\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q} = \Theta_{\langle\tilde Q,\tilde Q\rangle_{\natural}e_t} = \lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert^{2}\mathrm{id}$.

**Corollary (the two regimes of the sandwich).** For a central phase $\tilde Q = ce_t$, $\lvert c\rvert=1$, the parameter $L_{\tilde Q}=c\,\mathrm{id}$ gives the trivial sandwich $H_{L_{\tilde Q}}(T)=\lvert c\rvert^{2}T=T$, so the only sandwich coming from a left or right multiplication by a $J$-unitary element is the identity. The interesting sandwiches come from the **norm-one slice**: for $\lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert=1$ the operator $\Theta_{\tilde Q}$ is $J$-unitary, the sandwich

$$
H_{\Theta_{\tilde Q}}(T) = \Theta_{\tilde Q}\circ T\circ\Theta_{\tilde Q}^{\dagger}
$$

is an automorphism of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ preserving the indefinite form, and

$$
\bigl(\Theta_{\tilde Q}\bigr)^{\dagger} = \Theta_{\tilde Q^{-1}} .
$$

*Proof.* The triviality of the central-phase sandwich is the parameter rule with $\lvert c\rvert=1$. For the second, the theorem makes $\Theta_{\tilde Q}$ $J$-unitary on the norm-one slice, so $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}$, the last equality by the composition law $\Theta_{\tilde Q}\Theta_{\tilde Q^{-1}}=\Theta_{e_t}=\mathrm{id}$ of *Two-Sided Operators on the General Plain Sesqualgebra*.

**Remark (the kernel of the sandwich map).** The sandwich map $A\mapsto H_A$ is a homomorphism from the $J$-unitary group into the automorphism group of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ whose kernel is the circle of scalars of modulus one: $H_A(T)=T$ for all $T$ forces $A$ central, and the $J$-unitary central operators are the phases. The algebra's own parameters generate inside the $J$-unitary group the subgroup $\mathrm{U}(1)\times PU(2)\cong \mathrm{U}(1)\times SO(3)$ of *The Krein Isometry Group and Its J-Contractions*, and the sandwich restricts to the automorphisms $\Theta_{\tilde Q}$ themselves, which are inner and depend only on the class of $\tilde Q$ in $PU(2)$.

*Proof.* Multiplicativity and the kernel statement are the propositions of the first section; the subgroup statement is the corollary of the cited article, and the inner reading is the composition law, since $H_{\Theta_{\tilde Q}}(\Theta_{\tilde Q_1}) = \Theta_{\tilde Q}\Theta_{\tilde Q_1}\Theta_{\tilde Q}^{\dagger}$ is conjugation in the group of $J$-unitary operators.

## Contrast with the Definite Sandwich

**Remark (two adjoints, two sandwiches).** The definite sandwich $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ of *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint* uses the adjoint $Q^{*}$ of the definite form $(\cdot,\cdot)$ and is multiplicative in its argument exactly when $\tilde Q^{*}\tilde Q=e_t$, that is on the unitary slice $\mathrm{U}(2)$; the indefinite sandwich $H_A(T)=ATA^{\dagger}$ uses the adjoint of the general quaternionic sesquilinear form and is multiplicative exactly when $A^{\dagger}A=\mathrm{id}$, that is on the Krein-unitary group $\mathrm{U}(1,3)$. The identity that separates them is that the adjoint of a left multiplication for the general quaternionic sesquilinear form changes sides, $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, whereas for the definite form it stays, $(L_{\tilde Q})^{*}=L_{\tilde Q^{*}}$.

**Theorem (the failures of the indefinite sandwich).** For a $J$-unitary $A$ that is not unitary, the sandwich $H_A$ does not preserve the norm of the definite form, its orthogonal complements, its positive cone or its spectrum. It preserves the general quaternionic sesquilinear form, $J$-self-adjointness, $J$-positivity, $J$-unitarity, and the kernel and the image of every operator.

*Proof.* A $J$-unitary $A$ satisfies $A^{*}JA=J$ and is unitary only if additionally $A^{*}A=\mathrm{id}$. When it is not, $H_A$ changes the norm of operators, and their spectrum is not preserved, while all the indefinite statements are the theorems of the previous sections.

**Remark (the algebra reason).** In the biquaternion algebra the failure is visible **inside the algebra**. The definite adjoint of a two-sided operator is $\Theta_{\tilde Q}^{*}=\Theta_{\tilde Q^{*}}$, so $\Theta_{\tilde Q}^{*}\Theta_{\tilde Q}=\Theta_{\tilde Q^{*}\tilde Q}$ is the identity exactly when $\tilde Q^{*}\tilde Q$ is a central phase, that is exactly when $\tilde Q$ is a positive scalar multiple of a unitary element; while $\Theta_{\tilde Q}$ is $J$-unitary exactly on the norm-one slice $\lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert=1$. The two conditions differ: an explicit element on the norm-one slice with $\tilde Q^{*}\tilde Q$ not central was checked to give $\Theta_{\tilde Q}$ $J$-unitary and not unitary. The Lorentz group $SL(2,\mathbb{C})$ acts on the algebra by $J$-unitary operators and changes the definite structure: no positive definite form is invariant under it.

## Worked Examples

### The Fundamental Symmetry
For $A = J$ one has $J^{\dagger}=J$ and

$$
H_{J}(T) = JTJ , \qquad \bigl(H_{J}(T)\bigr)^{*} = J\,T^{*}J = H_{J}(T^{*}) ,
$$

so $H_{J}(T)$ is self-adjoint for the definite form exactly when $T$ is, and $\langle H_{J}(T)\tilde Q,\tilde Q\rangle = \langle T(J\tilde Q),J\tilde Q\rangle$ shows that $H_{J}(T)\geq0$ for the definite form exactly when $T\geq0$. The link with the indefinite data is the dictionary of *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*: $T$ is $J$-self-adjoint exactly when $JT$ is self-adjoint for the definite form, and in that case $H_{J}(T)=T^{*}$.

### The Boost
On the two-dimensional sub-block spanned by $e_t,\vec e_x$ let

$$
\mathsf{B}_{t} = \begin{pmatrix}\cosh t & \sinh t\\ \sinh t & \cosh t\end{pmatrix} , \qquad t\in\mathbb{R},
$$

extended by the identity on $\vec e_y,\vec e_z$. Then $\mathsf{B}_{t}$ is $J$-unitary, $\mathsf{B}_{t}^{\dagger}=\mathsf{B}_{t}^{-1}=\mathsf{B}_{-t}$, and $\mathsf{B}_t$ is not unitary, since $\mathsf{B}_t^{*}\mathsf{B}_t = \mathsf{B}_t^{2} = \mathsf{B}_{2t}$. For $\tilde Q = e_t$ one has $\mathsf{B}_te_t = \cosh t\,e_t + \sinh t\,\vec e_x$ and

$$
\langle \mathsf{B}_te_t,\mathsf{B}_te_t\rangle_{\natural*} = 1 = \langle e_t,e_t\rangle_{\natural*} , \qquad (\mathsf{B}_te_t,\mathsf{B}_te_t) = \cosh^{2}t + \sinh^{2}t = \cosh 2t .
$$

So the sandwich preserves the general quaternionic sesquilinear form and changes the norm of the definite form, by the factor $\cosh 2t$ per unit of the parameter; the boost is the model of the failure theorem, and it is the reason the indefinite sandwich preserves the indefinite form only.

### The Phase Parameters
For $\tilde Q = ce_t$ with $\lvert c\rvert=1$ the left multiplication is $L_{\tilde Q}=c\,\mathrm{id}$, $J$-unitary and central, and $H_{L_{\tilde Q}}(T)=\lvert c\rvert^{2}T=T$ by the parameter rule. The sandwich therefore sees the projective class of the parameter, and the circle $S^{1}e_t$ is exactly the kernel of $A\mapsto H_A$, as the kernel computation of the previous section asserts.

## Summary

On the biquaternion algebra the general quaternionic sesquilinear form $\langle\tilde W,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde Q^{\natural*}\tilde W)$ has signature $(1,3)$, with fundamental symmetry $J={}^{\natural}$ and indefinite adjoint $A^{\dagger}=JA^{*}J$. The **indefinite Hermitian sandwich** $H_{A}(T)=ATA^{\dagger}$ is linear in the argument and quadratic in the parameter, satisfies $H_A(T^{\dagger})=H_A(T)^{\dagger}$ and $H_A(H_S(T))=H_{AS}(T)$, and is multiplicative in the argument exactly when $A^{\dagger}A=\mathrm{id}$. For a $J$-unitary parameter it **preserves the general quaternionic sesquilinear form to the twisted arguments**, $\langle H_A(T)\tilde W,H_A(T)\tilde Q\rangle_{\natural*}=\langle TA^{\dagger}\tilde W,TA^{\dagger}\tilde Q\rangle_{\natural*}$, it preserves **$J$-self-adjointness**, **$J$-positivity** and **$J$-unitarity**, it transports the **kernel and the image** as $\ker H_A(T)=(A^{\dagger})^{-1}\ker T$ and $\mathrm{im}\,H_A(T)=A\,\mathrm{im}\,T$, and it is an automorphism of the operator algebra. The parameters coming from the algebra are governed by the Krein adjoints $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ and $(R_{\tilde Q})^{\dagger}=L_{\bar{\tilde Q}}$, by the $J$-unitarity criteria of *The Krein Isometry Group and Its J-Contractions* — central phases for the one-sided families and the norm-one slice for the two-sided family — and by the identity $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{-1}}$ on that slice. The **contrast with the definite sandwich** $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ is that a $J$-unitary operator need not be unitary: the indefinite sandwich preserves the form, the indefinite positivity, self-adjointness and the kernel and image, but not the norm of the definite form, its decompositions, its positive cone or its spectrum, so it is a symmetry of the indefinite form and not of the definite one. The general theory is *The Hermitian Sandwich on a Krein Space*; the definite instance is *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint* and *Two-Sided Operators on the General Plain Sesqualgebra*; and the indefinite positivity, the $J$-unitary group and the indefinite spectral theory are *Indefinite Positivity and the Krein Cone of the Biquaternioid Algebra*, *The Krein Isometry Group and Its J-Contractions* and *The Indefinite Spectra of the Operators on the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde Q,\tilde W)=\mathrm{Sc}(\tilde Q^{*}\tilde W)$ | Definite form, Gram $\mathrm{I}_4$, signature $(4,0)$ |
| $\langle\tilde W,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde Q^{\natural*}\tilde W)$ | general quaternionic sesquilinear form, Gram $E$, signature $(1,3)$ |
| $J={}^{\natural}$, $E=\mathrm{diag}(1,-1,-1,-1)$ | Fundamental symmetry, $\langle\tilde W,\tilde Q\rangle_{\natural*}=(J\tilde Q,\tilde W)$ |
| $A^{\dagger}=JA^{*}J$ | Indefinite adjoint |
| $H_{A}(T)=ATA^{\dagger}$ | Indefinite Hermitian sandwich |
| $H_{A}(T^{\dagger})=H_{A}(T)^{\dagger}$ | Sandwiches commute with adjunction |
| $H_{A}(H_{S}(T))=H_{AS}(T)$ | Composition |
| $H_{A}(ST)=H_{A}(S)H_{A}(T)\iff A^{\dagger}A=\mathrm{id}$ | Multiplicativity |
| $\langle\tilde W,H_A(T)\tilde Q\rangle_{\natural*}=\langle A^{\dagger}\tilde W,TA^{\dagger}\tilde Q\rangle_{\natural*}$ | Form preservation, one argument |
| $\langle\tilde Q,H_A(T)\tilde Q\rangle_{\natural*}=\langle A^{\dagger}\tilde Q,TA^{\dagger}\tilde Q\rangle_{\natural*}$ | Preservation of $J$-positivity |
| $\ker H_A(T)=(A^{\dagger})^{-1}\ker T$, $\ \mathrm{im}\,H_A(T)=A\,\mathrm{im}\,T$ | Kernel and image |
| $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, $(R_{\tilde Q})^{\dagger}=L_{\bar{\tilde Q}}$ | The algebra families |
| $\Theta_{\tilde Q}$ $J$-unitary $\iff\lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert=1$ | The norm-one slice |
| $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{-1}}$ on the slice | Krein adjoint of the two-sided family |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the sandwich and the form-preserving operators of a Krein space.
- Tomas Ya. Azizov and I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the indefinite adjoint, its calculus and the inner automorphisms.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the matrix form of the sandwich and the kernel and image calculations.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the complexified quaternion algebra and its involutions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Lorentz group inside the complexified quaternions.
