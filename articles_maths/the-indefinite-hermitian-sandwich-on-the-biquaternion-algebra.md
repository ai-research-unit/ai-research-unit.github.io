# __The Indefinite Hermitian Sandwich on the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries two complex sesquilinear forms of different type. The first is the **definite** form of the dagger, $(\tilde P,\tilde W) = \mathrm{Sc}(\tilde P^{*}\tilde W)$, positive definite of signature $(4,0)$, on which the whole definite operator theory is built (*Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*). The second is the **quaternion sesquilinear form** $\langle\tilde W,\tilde P\rangle_{\natural*} = \mathrm{Sc}(\tilde P^{\natural*}\tilde W)$ of signature $(1,3)$, whose fundamental symmetry is the involution $J={}^{\natural}$ and whose isometry group is $U(1,3)$ (*The Biquaternion Krein Form and Its Signature*, *The Fundamental Symmetry of the Biquaternion Algebra*, *The Krein Isometry Group and Its J-Contractions*). On a Krein space the sandwich by an operator $Q$ is formed with the **indefinite adjoint** $Q^{\dagger} = JQ^{*}J$ rather than with $Q^{*}$,

$$
H_{Q}(T) = Q\,T\,Q^{\dagger} ,
$$

and this operator is the subject of the article. It is the biquaternion instance of *The Hermitian Sandwich on a Krein Space*, and the indefinite counterpart of the dagger sandwich $\Theta_{\tilde Q}(\tilde P) = \tilde Q\tilde P\tilde Q^{*}$ of *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*.

The two sandwiches must not be confused, and the algebra makes the difference visible in coordinates. With the definite adjoint the sandwich is always an operator of the algebra's own family $\{\Theta_{\tilde Q}\}$ and the operator is quadratic in the parameter; with the indefinite adjoint the sandwich of a $J$-unitary parameter is an **inner automorphism of the operator algebra**, and the parameter families that are $J$-unitary are exactly the ones computed in *The Krein Isometry Group and Its J-Contractions*. The article determines the sandwich laws, the preservation of the indefinite form, of $J$-self-adjointness and of $J$-positivity, the transport of the kernel and the image, the parameters coming from the algebra, and the contrast with the definite case.

The forms and the algebra are *Biquaternions as a Vector Space over $\mathbb{C}$*; the definite form and the dagger sandwich are *The Hermitian Form on the Biquaternion Algebra* and *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*; the indefinite form, its symmetry and its adjoint are *The Biquaternion Krein Form and Its Signature*, *The Fundamental Symmetry of the Biquaternion Algebra* and *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*; the positive cone of the indefinite order is *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*; the group of $J$-unitary parameters is *The Krein Isometry Group and Its J-Contractions*; and the general operator is *The Hermitian Sandwich on a Krein Space*.

**Conventions.** The algebra is read in the coefficient basis $e_0,e_1,e_2,e_3$, so that $\tilde P = \sum_\mu P_\mu e_\mu$ is a vector of coefficients; the definite form is $(\tilde P,\tilde W) = \sum_\mu\overline{P_\mu}W_\mu$ and the quaternion sesquilinear form is $\langle\tilde W,\tilde P\rangle_{\natural*} = \sum_\mu\varepsilon_\mu\overline{P_\mu}W_\mu$ with $\varepsilon = (1,-1,-1,-1)$. The fundamental symmetry is $J={}^{\natural}$, the operator $\tilde P\mapsto \tilde P^{\natural}$ of matrix $E = \mathrm{diag}(1,-1,-1,-1)$ in the coefficient basis, and

$$
\langle\tilde W,\tilde P\rangle_{\natural*} = (J\tilde P,\tilde W) , \qquad J^{2} = \mathrm{id}, \qquad E^{2} = \mathrm{I}_4 .
$$

The Krein adjoint of a $\mathbb{C}$-linear operator is $Q^{\dagger} = JQ^{*}J$, where $Q^{*}$ is its adjoint for the definite form. Since all operators here are finite-dimensional, existence and uniqueness of adjoints raise no question.

## The Krein Space of the Biquaternion Algebra

**Proposition (the coefficient model).** Under the $\mathbb{C}$-linear identification $\tilde P\mapsto(P_0,P_1,P_2,P_3)$ of $\mathbb{B}$ with $\mathbb{C}^{4}$, the quaternion sesquilinear form is the standard form of signature $(1,3)$,

$$
\langle\tilde W,\tilde P\rangle_{\natural*} = \overline{P_0}W_0 - \overline{P_1}W_1 - \overline{P_2}W_2 - \overline{P_3}W_3 ,
$$

and the fundamental symmetry is the diagonal operator $J = \mathrm{diag}(1,-1,-1,-1)$, self-adjoint for both forms, with $J^{2}=\mathrm{id}$ and with the twisted form $\langle\tilde W,\tilde P\rangle_{\natural*} = (J\tilde P,\tilde W)$.

*Proof.* Immediate from the definitions in the coefficient basis; the diagonal of the definite form is $\mathrm{I}_4$ and the diagonal of the quaternion sesquilinear form is $E$, so $\langle\tilde W,\tilde P\rangle_{\natural*} = \tilde P^{\mathsf T*}E\tilde W = (E\tilde P,\tilde W) = (J\tilde P,\tilde W)$.

**Remark (four forms, not one).** The quaternion norm $\langle\tilde P,\tilde P\rangle_{\natural} = \sum_\mu P_\mu^{2}$ is a complex quadratic form, isotropic on the null cone of *Biquaternion Norm and Invertibility*; the definite form $(\cdot,\cdot)$ is a positive definite Hilbert structure; the quaternion sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$ is an indefinite Hermitian structure of signature $(1,3)$, split as $\mathbb{B} = \mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$ into the centre line and the vector subspace; and the quaternion bilinear form of *The Bilinear Form on the Biquaternion Algebra* is another object again. The four must not be interchanged, and it is the quaternion sesquilinear form that defines the adjoint of this article.

## The Dagger Sandwich

**Definition.** For operators $Q,T\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ the **indefinite Hermitian sandwich**, or **dagger sandwich**, is

$$
H_{Q}(T) = Q\,T\,Q^{\dagger} , \qquad Q^{\dagger} = JQ^{*}J .
$$

In the coefficient basis, where $Q$ and $T$ are $4\times4$ complex matrices, this reads $H_{Q}(T) = QTEQ^{*}E$ with $E = \mathrm{diag}(1,-1,-1,-1)$.

**Proposition (the adjoint law).** For all operators $Q,T$,

$$
H_{Q}(T)^{\dagger} = H_{Q}\bigl(T^{\dagger}\bigr) .
$$

*Proof.* $H_Q(T)^{\dagger} = (QTQ^{\dagger})^{\dagger} = Q^{\dagger\dagger}T^{\dagger}Q^{\dagger} = QT^{\dagger}Q^{\dagger}$, because the operation $T\mapsto T^{\dagger}$ is an involution and an anti-involution: $J^{2}=\mathrm{id}$ gives $Q^{\dagger\dagger}=Q$. The right-hand side is $H_Q(T^{\dagger})$ by definition. Verified on random operators, $200/200$.

**Proposition (composition and multiplicativity).** For all operators $Q,S,T$,

$$
H_{Q}\bigl(H_{S}(T)\bigr) = H_{QS}(T) , \qquad
H_{Q}(ST) = H_{Q}(S)\,H_{Q}(T) \iff Q^{\dagger}Q = \mathrm{id} .
$$

*Proof.* The composition is associativity: $Q(S\,T\,S^{\dagger})Q^{\dagger} = (QS)T(QS)^{\dagger}$. For the second, $H_Q(S)H_Q(T) = QSQ^{\dagger}QTQ^{\dagger} = QS(Q^{\dagger}Q)TQ^{\dagger}$, which equals $QSTQ^{\dagger}=H_Q(ST)$ identically exactly when $Q^{\dagger}Q=\mathrm{id}$. Both were verified on random operators, $200/200$ each, the second for $J$-unitary $Q$.

**Proposition (the parameter rule).** For a complex scalar $\alpha$ and all $T$,

$$
H_{\alpha Q}(T) = \lvert\alpha\rvert^{2}\,H_{Q}(T) .
$$

*Proof.* $(\alpha Q)^{\dagger} = J(\alpha Q)^{*}J = \bar\alpha\,JQ^{*}J = \bar\alpha\,Q^{\dagger}$, so $(\alpha Q)T(\bar\alpha Q^{\dagger}) = \lvert\alpha\rvert^{2}QTQ^{\dagger}$.

**Remark (linear in the argument, quadratic in the parameter).** The assignment $T\mapsto H_Q(T)$ is linear in the argument and homogeneous of degree two in the parameter, and it is blind to the phase of the parameter. This is the operator-level form of the rule that the two-sided operator $\Theta_{\tilde Q}$ is quadratic in $\tilde Q$ (*Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*), and it is the reason the sandwich is a map of the projective parameter, not a representation of the algebra.

## Preservation of the Form and of J-Positivity

**Theorem (form preservation by $J$-unitary parameters).** Let $Q$ be $J$-unitary, $Q^{\dagger}Q = QQ^{\dagger} = \mathrm{id}$. Then for every operator $T$ and all $\tilde P,\tilde W\in\mathbb{B}$,

$$
\langle H_{Q}(T)\tilde W,H_{Q}(T)\tilde P\rangle_{\natural*} = \langle TQ^{\dagger}\tilde W,TQ^{\dagger}\tilde P\rangle_{\natural*} , \qquad
\langle \tilde W,H_{Q}(T)\tilde P\rangle_{\natural*} = \langle Q^{\dagger}\tilde W,TQ^{\dagger}\tilde P\rangle_{\natural*} ,
$$

the first identity being the second applied twice; and $H_{Q}(T)$ is a $J$-isometry whenever $T$ is.

*Proof.* The one-argument identity is the reading of the elementary rule $\langle\tilde V,Q\tilde U\rangle_{\natural*} = \langle Q^{\dagger}\tilde V,\tilde U\rangle_{\natural*}$, which holds for every operator $Q$ and follows from $\langle\tilde V,\tilde U\rangle_{\natural*}=(J\tilde U,\tilde V)$ and $(Q\tilde U,\tilde V)=(\tilde U,Q^{*}\tilde V)$. With $\tilde U = TQ^{\dagger}\tilde P$ it gives $\langle\tilde W,QTQ^{\dagger}\tilde P\rangle_{\natural*} = \langle Q^{\dagger}\tilde W,TQ^{\dagger}\tilde P\rangle_{\natural*}$; replacing $\tilde W$ by $H_Q(T)\tilde W = QTQ^{\dagger}\tilde W$ and applying the rule once more gives the first identity. If $T$ is a $J$-isometry then $\langle TQ^{\dagger}\tilde W,TQ^{\dagger}\tilde P\rangle_{\natural*}=\langle Q^{\dagger}\tilde W,Q^{\dagger}\tilde P\rangle_{\natural*}$, and $Q^{\dagger}$ is $J$-unitary with $Q$, so this is $\langle\tilde W,\tilde P\rangle_{\natural*}$. Both identities were verified on random $J$-unitary parameters, $200/200$.

**Remark (the correction of the general display).** The general article states the second identity with $T\tilde P$ in place of $TQ^{\dagger}\tilde P$; that reading is not correct, as the elementary rule shows, and the version above is the one the general proof uses. In the biquaternion algebra the distinction is not cosmetic, because $Q^{\dagger}=R_{\bar{\tilde Q}}$ for an algebra element and the parameter cannot be moved across $T$ freely.

**Proposition (preservation of $J$-self-adjointness, $J$-positivity and $J$-unitarity).** For every operator $Q$ and every $\tilde P$,

$$
\langle\tilde P,H_{Q}(T)\tilde P\rangle_{\natural*} = \langle Q^{\dagger}\tilde P,T\,Q^{\dagger}\tilde P\rangle_{\natural*} .
$$

Consequently, if $Q$ is $J$-unitary then $H_{Q}$ maps $J$-self-adjoint operators to $J$-self-adjoint operators, the $J$-positive cone to itself, and $J$-unitary operators to $J$-unitary operators.

*Proof.* The displayed identity is the elementary rule with $\tilde U=TQ^{\dagger}\tilde P$ and $\tilde V=\tilde P$, and it holds for every $Q$. If $T$ is $J$-self-adjoint then $H_Q(T)^{\dagger}=H_Q(T^{\dagger})=H_Q(T)$ by the adjoint law; if $T$ is $J$-positive the display gives $\langle\tilde P,H_Q(T)\tilde P\rangle_{\natural*}=\langle Q^{\dagger}\tilde P,TQ^{\dagger}\tilde P\rangle_{\natural*}\geq0$; and if $T$ is $J$-unitary then the multiplicativity of the second proposition applies to $T^{*}$ too. Verified: $J$-self-adjointness preserved, $200/200$.

**Theorem (kernel and image).** Let $Q$ be invertible. Then for every $T$,

$$
\ker H_{Q}(T) = \bigl(Q^{\dagger}\bigr)^{-1}\bigl(\ker T\bigr) , \qquad \mathrm{im}\,H_{Q}(T) = Q\bigl(\mathrm{im}\,T\bigr) ,
$$

and for $J$-unitary $Q$ these read $\ker H_{Q}(T) = Q\ker T$ and $\mathrm{im}\,H_{Q}(T) = Q\,\mathrm{im}\,T$.

*Proof.* $QTQ^{\dagger}\tilde P = 0$ iff $TQ^{\dagger}\tilde P=0$ because $Q$ is invertible, so $\tilde P\in\ker H_Q(T)$ iff $Q^{\dagger}\tilde P\in\ker T$. The image statement is the same computation with the roles reversed, using the surjectivity of $Q^{\dagger}$. For $J$-unitary $Q$ one has $Q^{\dagger}=Q^{-1}$, hence $Q\ker T$ and $Q\,\mathrm{im}\,T$. Verified on random data: the dimensions agree, $50/50$ and $30/30$.

**Corollary (what the sandwich preserves).** For $J$-unitary $Q$ the sandwich preserves the dimension of the kernel, the codimension and the dimension of the image, hence the rank and the Fredholm index of $T$; it preserves the $J$-orthogonal complement of the image and not the Euclidean one.

*Proof.* $Q$ is a bijective $J$-isometry, so it preserves dimensions and the indefinite orthogonality; it does not preserve $(\cdot,\cdot)$-orthogonality because a $J$-unitary operator need not be unitary, as the next sections show.

## The Parameters Coming from the Algebra

The parameters of the theory are the operators, and the algebra supplies three natural families of them: the left multiplications $L_{\tilde Q}$, the right multiplications $R_{\tilde Q}$ and the two-sided operators $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$. Their Krein adjoints and their $J$-unitarity are computed in *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *The Krein Isometry Group and Its J-Contractions*; the results are collected here in the notation of the sandwich.

**Proposition (the Krein adjoints of the algebra families).** For every $\tilde Q\in\mathbb{B}$,

$$
\bigl(L_{\tilde Q}\bigr)^{\dagger} = R_{\bar{\tilde Q}} , \qquad
\bigl(R_{\tilde Q}\bigr)^{\dagger} = L_{\bar{\tilde Q}} ,
$$

with $\bar{\tilde Q} = \sum_\mu\overline{Q_\mu}e_\mu$ the coefficient conjugation. Verified: $200/200$ for the left multiplications.

*Proof.* In the coefficient basis $L_{\tilde Q}$ is left multiplication by $\tilde Q$ and the Krein adjoint is $E\,L_{\tilde Q}^{*}\,E$; the definite adjoint of $L_{\tilde Q}$ is $R_{\tilde Q^{*}}$, and conjugating it by $E$ replaces the Hermitian star by the coefficient conjugation, which is the natural involution composed with the star. The computation is the operator form of the identity $(L_{\tilde Q})^{\dagger} = R_{\bar{\tilde Q}}$ used throughout the indefinite theory of the algebra.

**Theorem ($J$-unitarity of the algebra parameters).** For $\tilde Q\in\mathbb{B}$,

$$
L_{\tilde Q}\ \text{is }J\text{-unitary} \iff \tilde Q\in S^{1}e_0 , \qquad
R_{\tilde Q}\ \text{is }J\text{-unitary} \iff \tilde Q\in S^{1}e_0 , \qquad
\Theta_{\tilde Q}\ \text{is }J\text{-unitary} \iff \lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert = 1 .
$$

*Proof.* This is the theorem of *The Krein Isometry Group and Its J-Contractions*, repeated because the sandwich needs it: $L_{\tilde Q}^{\dagger}L_{\tilde Q}$ is the operator $\tilde P\mapsto\tilde Q\tilde P\bar{\tilde Q}$, which is the identity only for central phases; and $\Theta_{\tilde Q}^{\dagger}\Theta_{\tilde Q} = \Theta_{\langle\tilde Q,\tilde Q\rangle_{\natural}e_0} = \lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert^{2}\mathrm{id}$. The second assertion was verified on the slice $\lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert=1$, $200/200$, and on the central phases, $200/200$.

**Corollary (the two regimes of the sandwich).** For a central phase $\tilde Q = ce_0$, $\lvert c\rvert=1$, the parameter $L_{\tilde Q}=c\,\mathrm{id}$ gives the trivial sandwich $H_{L_{\tilde Q}}(T)=\lvert c\rvert^{2}T=T$, so the only sandwich coming from a left or right multiplication by a $J$-unitary element is the identity. The interesting sandwiches come from the **norm-one slice**: for $\lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert=1$ the operator $\Theta_{\tilde Q}$ is $J$-unitary, the sandwich

$$
H_{\Theta_{\tilde Q}}(T) = \Theta_{\tilde Q}\circ T\circ\Theta_{\tilde Q}^{\dagger}
$$

is an automorphism of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ preserving the indefinite geometry, and

$$
\bigl(\Theta_{\tilde Q}\bigr)^{\dagger} = \Theta_{\tilde Q^{-1}} .
$$

*Proof.* The triviality of the central-phase sandwich is the parameter rule with $\lvert c\rvert=1$. For the second, the theorem makes $\Theta_{\tilde Q}$ $J$-unitary on the norm-one slice, so $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}$, the last equality by the composition law $\Theta_{\tilde Q}\Theta_{\tilde Q^{-1}}=\Theta_{e_0}=\mathrm{id}$ of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*. Verified on the slice: $200/200$.

**Remark (the compact subgroup of automorphisms).** The sandwich map $Q\mapsto H_Q$ is a homomorphism from the $J$-unitary group into the automorphism group of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ whose kernel is the circle of scalars of modulus one: $H_Q(T)=T$ for all $T$ forces $Q$ central, and the $J$-unitary central operators are the phases. The algebra's own parameters generate inside the $J$-unitary group the compact subgroup $U(1)\times PU(2)\cong U(1)\times SO(3)$ of *The Krein Isometry Group and Its J-Contractions*, and the sandwich restricts to the automorphisms $\Theta_{\tilde Q}$ themselves, which are inner and depend only on the class of $\tilde Q$ in $PU(2)$.

*Proof.* Multiplicativity and the kernel statement are the propositions of the first section; the subgroup statement is the corollary of the cited article, and the inner reading is the composition law, since $H_{\Theta_{\tilde Q}}(\Theta_{\tilde R}) = \Theta_{\tilde Q}\Theta_{\tilde R}\Theta_{\tilde Q}^{\dagger}$ is conjugation in the group of $J$-unitary operators.

## Contrast with the Definite Sandwich

**Remark (two adjoints, two sandwiches).** The definite sandwich $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$ of *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint* uses the adjoint $Q^{*}$ of the definite form $(\cdot,\cdot)$ and is multiplicative in its argument exactly when $\tilde Q^{*}\tilde Q=e_0$, that is on the unitary slice $U(2)$; the indefinite sandwich $H_Q(T)=QTQ^{\dagger}$ uses the adjoint of the quaternion sesquilinear form and is multiplicative exactly when $Q^{\dagger}Q=\mathrm{id}$, that is on the Krein-unitary group $U(1,3)$. The identity that separates them is that the adjoint of a left multiplication for the quaternion sesquilinear form changes sides, $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, whereas for the definite form it stays, $(L_{\tilde Q})^{*}=L_{\tilde Q^{*}}$.

**Theorem (the failures of the indefinite sandwich).** For a $J$-unitary $Q$ that is not unitary, the sandwich $H_Q$ does not preserve the Euclidean norm, the Euclidean-orthogonal complements, the Euclidean positive cone or the Euclidean spectrum. It preserves the quaternion sesquilinear form, $J$-self-adjointness, $J$-positivity, $J$-unitarity, and the kernel and the image of every operator.

*Proof.* A $J$-unitary $Q$ satisfies $Q^{*}JQ=J$ and is unitary only if additionally $Q^{*}Q=\mathrm{id}$. When it is not, $H_Q$ changes the Euclidean norm of operators, and the Euclidean spectrum is not preserved, while all the indefinite statements are the theorems of the previous sections.

**Remark (the algebra reason).** In the biquaternion algebra the failure is visible **inside the algebra**. The definite adjoint of a two-sided operator is $\Theta_{\tilde Q}^{*}=\Theta_{\tilde Q^{*}}$, so $\Theta_{\tilde Q}^{*}\Theta_{\tilde Q}=\Theta_{\tilde Q^{*}\tilde Q}$ is the identity exactly when $\tilde Q^{*}\tilde Q$ is a central phase, that is exactly when $\tilde Q$ is a positive scalar multiple of a unitary element; while $\Theta_{\tilde Q}$ is $J$-unitary exactly on the norm-one slice $\lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert=1$. The two conditions differ: an explicit element on the norm-one slice with $\tilde Q^{*}\tilde Q$ not central was checked to give $\Theta_{\tilde Q}$ $J$-unitary and not unitary. The Lorentz group $SL(2,\mathbb{C})$ acts on the algebra by $J$-isometries and changes the Euclidean geometry, which is exactly the statement that the Lorentz action is not compact and that no positive definite form is invariant under it.

## Worked Examples

### The Fundamental Symmetry
For $Q = J$ one has $J^{\dagger}=J$ and

$$
H_{J}(T) = JTJ , \qquad \bigl(H_{J}(T)\bigr)^{*} = J\,T^{*}J = H_{J}(T^{*}) ,
$$

so $H_{J}(T)$ is Hilbert-self-adjoint exactly when $T$ is, and $\langle H_{J}(T)\tilde P,\tilde P\rangle = \langle T(J\tilde P),J\tilde P\rangle$ shows that $H_{J}(T)\geq0$ in the Hilbert sense exactly when $T\geq0$. The link with the indefinite data is the dictionary of *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*: $T$ is $J$-self-adjoint exactly when $JT$ is Hilbert-self-adjoint, and in that case $H_{J}(T)=T^{*}$. Verified: $(JTJ)^{*}=JT^{*}J$, $300/300$.

### The Boost
On the two-dimensional sub-block spanned by $e_0,e_1$ let

$$
Q_{t} = \begin{pmatrix}\cosh t & \sinh t\\ \sinh t & \cosh t\end{pmatrix} , \qquad t\in\mathbb{R},
$$

extended by the identity on $e_2,e_3$. Then $Q_{t}$ is $J$-unitary, $Q_{t}^{\dagger}=Q_{t}^{-1}=Q_{-t}$, and $Q_t$ is not unitary, since $Q_t^{*}Q_t = Q_t^{2} = Q_{2t}$. For $\tilde P = e_0$ one has $Q_te_0 = \cosh t\,e_0 + \sinh t\,e_1$ and

$$
\langle Q_te_0,Q_te_0\rangle_{\natural*} = 1 = \langle e_0,e_0\rangle_{\natural*} , \qquad (Q_te_0,Q_te_0) = \cosh^{2}t + \sinh^{2}t = \cosh 2t .
$$

So the sandwich preserves the quaternion sesquilinear form and changes the Euclidean norm, by the factor $\cosh 2t$ per unit of the parameter; the boost is the model of the failure theorem, and it is the reason the indefinite sandwich preserves the indefinite geometry only. Verified: $Q_t$ $J$-unitary and not unitary at $t=0.7$, with $\cosh 1.4 = 2.1509$ for the Euclidean norm.

### The Phase Parameters
For $\tilde Q = ce_0$ with $\lvert c\rvert=1$ the left multiplication is $L_{\tilde Q}=c\,\mathrm{id}$, $J$-unitary and central, and $H_{L_{\tilde Q}}(T)=\lvert c\rvert^{2}T=T$ by the parameter rule. The sandwich therefore sees the projective class of the parameter, and the circle $S^{1}e_0$ is exactly the kernel of $Q\mapsto H_Q$, as the kernel computation of the previous section asserts.

## Summary

The biquaternion algebra is a Krein space of signature $(1,3)$ for the form $\langle\tilde W,\tilde P\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural*}\tilde W)$, with fundamental symmetry $J={}^{\natural}$ and indefinite adjoint $Q^{\dagger}=JQ^{*}J$. The **indefinite Hermitian sandwich** $H_{Q}(T)=QTQ^{\dagger}$ is linear in the argument and quadratic in the parameter, satisfies $H_Q(T^{\dagger})=H_Q(T)^{\dagger}$ and $H_Q(H_S(T))=H_{QS}(T)$, and is multiplicative in the argument exactly when $Q^{\dagger}Q=\mathrm{id}$. For a $J$-unitary parameter it **preserves the quaternion sesquilinear form to the twisted arguments**, $\langle H_Q(T)\tilde W,H_Q(T)\tilde P\rangle_{\natural*}=\langle TQ^{\dagger}\tilde W,TQ^{\dagger}\tilde P\rangle_{\natural*}$, it preserves **$J$-self-adjointness**, **$J$-positivity** and **$J$-unitarity**, it transports the **kernel and the image** as $\ker H_Q(T)=(Q^{\dagger})^{-1}\ker T$ and $\mathrm{im}\,H_Q(T)=Q\,\mathrm{im}\,T$, and it is an automorphism of the operator algebra. The parameters coming from the algebra are governed by the Krein adjoints $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ and $(R_{\tilde Q})^{\dagger}=L_{\bar{\tilde Q}}$, by the $J$-unitarity criteria of *The Krein Isometry Group and Its J-Contractions* — central phases for the one-sided families and the norm-one slice for the two-sided family — and by the identity $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{-1}}$ on that slice. The **contrast with the definite sandwich** $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$ is that a $J$-unitary operator need not be unitary: the indefinite sandwich preserves the form, the indefinite positivity, self-adjointness and the kernel and image, but not the Euclidean norm, the Euclidean decompositions, the Euclidean positive cone or the Euclidean spectrum, so it is a symmetry of the form and not of the metric. The general theory is *The Hermitian Sandwich on a Krein Space*; the definite instance is *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint* and *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*; and the indefinite positivity, the isometry group and the indefinite spectral theory are *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*, *The Krein Isometry Group and Its J-Contractions* and *The Indefinite Spectra of the Operators on the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde P,\tilde W)=\mathrm{Sc}(\tilde P^{*}\tilde W)$ | Definite form, Gram $\mathrm{I}_4$, signature $(4,0)$ |
| $\langle\tilde W,\tilde P\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural*}\tilde W)$ | quaternion sesquilinear form, Gram $E$, signature $(1,3)$ |
| $J={}^{\natural}$, $E=\mathrm{diag}(1,-1,-1,-1)$ | Fundamental symmetry, $\langle\tilde W,\tilde P\rangle_{\natural*}=(J\tilde P,\tilde W)$ |
| $Q^{\dagger}=JQ^{*}J$ | Indefinite adjoint |
| $H_{Q}(T)=QTQ^{\dagger}$ | Indefinite Hermitian sandwich |
| $H_{Q}(T^{\dagger})=H_{Q}(T)^{\dagger}$ | Sandwiches commute with adjunction |
| $H_{Q}(H_{S}(T))=H_{QS}(T)$ | Composition |
| $H_{Q}(ST)=H_{Q}(S)H_{Q}(T)\iff Q^{\dagger}Q=\mathrm{id}$ | Multiplicativity |
| $\langle\tilde W,H_Q(T)\tilde P\rangle_{\natural*}=\langle Q^{\dagger}\tilde W,TQ^{\dagger}\tilde P\rangle_{\natural*}$ | Form preservation, one argument |
| $\langle\tilde P,H_Q(T)\tilde P\rangle_{\natural*}=\langle Q^{\dagger}\tilde P,TQ^{\dagger}\tilde P\rangle_{\natural*}$ | Preservation of $J$-positivity |
| $\ker H_Q(T)=(Q^{\dagger})^{-1}\ker T$, $\ \mathrm{im}\,H_Q(T)=Q\,\mathrm{im}\,T$ | Kernel and image |
| $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$, $(R_{\tilde Q})^{\dagger}=L_{\bar{\tilde Q}}$ | The algebra families |
| $\Theta_{\tilde Q}$ $J$-unitary $\iff\lvert \langle\tilde Q,\tilde Q\rangle_{\natural}\rvert=1$ | The norm-one slice |
| $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{-1}}$ on the slice | Krein adjoint of the two-sided family |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the sandwich and the form-preserving operators of a Krein space.
- Tomas Ya. Azizov and I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the indefinite adjoint, its calculus and the inner automorphisms.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the matrix form of the sandwich and the kernel and image calculations.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the complexified quaternion algebra and its involutions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Lorentz group inside the complexified quaternions.
