
# __Two-Sided Operators on the General Quaternionic Algebra__

## Introduction

The biquaternion algebra carries two families of one-sided operators, the left and the right multiplications, and their products are the two-sided operators $L_aR_b(y)=a\,y\,b$. Among them one member is singled out by the general quaternionic bilinear form and the natural conjugation: the choice $b=a^{\natural}$, giving the **twisted two-sided operator**

$$
\Theta_a=L_aR_{a^{\natural}},\qquad \Theta_a(y)=a\,y\,a^{\natural}.
$$

This is the **conjugation sandwich** of the biquaternion algebra, the member of the general two-sided family whose second slot carries the natural conjugation in place of the inverse. The corpus also calls it the *signed inner conjugation*, a name it shares with the different operator $\tilde Q_1\mapsto\alpha(\tilde A)\tilde Q_1\tilde A^{-1}$; the remark *which member of the general family this operator is* below separates the two. Placing the conjugation where the inverse belongs is what makes the operator defined on every element and not only on the units, and it leaves the norm in front of the inner conjugation: on a vector the operator is the reflection exactly on the shell $\langle\tilde A\rangle_{\natural}=-1$, and a scaled copy of it elsewhere.

This article treats the operator: its factors, its multiplication law, its injectivity up to sign, its adjoint for the general quaternionic bilinear form, the criterion that singles it out among the products $L_aR_b$, its automorphisms, and its dagger adjoint. The general Clifford theory of the family is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, to which this is the biquaternion instance; the one-sided factors are *One-Sided Operators on the General Quaternionic Algebra*; the groups cut out by the norm are *The Pin and Spin Groups of the General Quaternionic Algebra*; and the corresponding family over the Hermitian form is *Mixed Inner Conjugation on the General Plain Sesqualgebra*. The form, its matrix and its adjoint are *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; nothing of the general theory is re-derived here.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and central scalar imaginary $i$; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The natural conjugation is $\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$, an anti-automorphism and an involution; the norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$, central and multiplicative; the general quaternionic bilinear form is $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})$, with $\langle\cdot,\cdot\rangle_{\natural}$-adjoint written ${}^{N}$, so that $\langle T\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P,T^{N}\tilde Q\rangle_{\natural}$. The Hermitian form is $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and its adjoint is written ${}^{*}$.

## The Operator and Its Factors

**Definition.** For $\tilde A\in\mathbb{B}$ the **twisted two-sided operator** of $\tilde A$, or the **conjugation sandwich** by $\tilde A$, is the $\mathbb{C}$-linear map

$$
\Theta_{\tilde A}:\mathbb{B}\longrightarrow\mathbb{B},\qquad \Theta_{\tilde A}(\tilde Q_1)=\tilde A\,\tilde Q_1\,\tilde A^{\natural}.
$$

**Proposition (the factors, and the quadraticity in the parameter).** With $L$ and $R$ the left and right multiplications,

$$
\Theta_{\tilde A}=L_{\tilde A}\circ R_{\tilde A^{\natural}}=R_{\tilde A^{\natural}}\circ L_{\tilde A},
$$

the two factors commuting; and the parameter map is quadratic, not linear,

$$
\Theta_{\lambda\tilde A}=\lambda^{2}\,\Theta_{\tilde A},\qquad \Theta_{\tilde A+\tilde Q_2}=\Theta_{\tilde A}+\Theta_{\tilde Q_2}+\tilde A\,[\,]\tilde Q_2^{\natural}+\tilde Q_2\,[\,]\tilde A^{\natural},
$$

the last two terms being the cross term; in particular $\Theta_{-\tilde A}=\Theta_{\tilde A}$ and $\Theta_{i\tilde A}=-\Theta_{\tilde A}$.

*Proof.* The first identity is the definition, the second is $L_aR_b=R_bL_a$. For the quadraticity, $(\lambda\tilde A)\,\tilde Q_1\,(\lambda\tilde A)^{\natural}=\lambda^{2}\tilde A\tilde Q_1\tilde A^{\natural}$ because the natural conjugation is $\mathbb{C}$-linear; expanding the product $(\tilde A+\tilde Q_2)\tilde Q_1(\tilde A+\tilde Q_2)^{\natural}$ gives the displayed cross term.

**Remark (why the parameter map cannot be linear).** A linear map of the parameter would give $\Theta_{0}=0$ and $\Theta_{\lambda\tilde A}=\lambda\Theta_{\tilde A}$; but $\Theta_{\tilde A}$ is built from two factors each linear in $\tilde A$, so the scalar appears twice. The operator is linear in $\tilde Q_1$, which is what the applications use, and quadratic in $\tilde A$; the sign $\Theta_{-\tilde A}=\Theta_{\tilde A}$ is the same statement at $\lambda=-1$.

**Proposition (the sign and the inverse).** For every element, $\Theta_{\tilde A}=\Theta_{-\tilde A}$; for an invertible $\tilde A$,

$$
\Theta_{\tilde A}=\langle\tilde A\rangle_{\natural}\ \mathrm{Ad}_{\tilde A},\qquad \mathrm{Ad}_{\tilde A}(\tilde Q_1)=\tilde A\,\tilde Q_1\,\tilde A^{-1},
$$

and $\mathrm{Ad}_{\tilde A}=\Theta_{\tilde A}$ exactly on the norm-one set $\langle\cdot\rangle_{\natural}=1$.

*Proof.* The first identity is $\tilde A^{\natural}=\langle\tilde A\rangle_{\natural}\tilde A^{-1}$ for a unit, and $\langle\tilde A\rangle_{\natural}$ is central; the second follows from $\langle\cdot\rangle_{\natural}=1$.

**Remark (why the sign is needed).** The plain inner conjugation $\mathrm{Ad}_{\tilde A}$ is an algebra automorphism and needs the inverse, so it is defined only on the units and is blind to the norm; the twisted form $\Theta_{\tilde A}$ is defined for every element, is linear in its argument and quadratic in its parameter, and carries the norm as the scalar in front of the inner conjugation. On the norm-one set the two agree, and off it they differ by the scalar $\langle\tilde A\rangle_{\natural}$ – which is the whole of the sign in the name.

**Remark (which member of the general family this operator is, and the two senses of the name).** The general two-sided family of *Two-Sided Operators on a Clifford Algebra* attaches to a pair (an automorphism $\theta$ of the left factor, an anti-automorphism $c$ of the right one) the operator $\Phi^{\theta,c}_x(y)=\theta(x)\,y\,c(x)$, and its five members are told apart by $c$. The member that the general layer calls **signed inner conjugation** is $\theta=\alpha$, $c=(\ )^{-1}$,

$$
\alpha(\tilde A)\,\tilde Q_1\,\tilde A^{-1}=\varepsilon_{\tilde A}\,\mathrm{Ad}_{\tilde A},
$$

with $\varepsilon_{\tilde A}=(-1)^{k}$ the parity sign of a homogeneous $\tilde A$. The operator of this article, $\Theta_{\tilde A}=\tilde A\,\tilde Q_1\,\tilde A^{\natural}$, is the member $\theta=\mathrm{id}$, $c={}^{\natural}$, the **conjugation sandwich**, whose value at the unit is the Clifford norm; and the two are not the same operator, for on a unit

$$
\Theta_{\tilde A}=\langle\tilde A\rangle_{\natural}\,\mathrm{Ad}_{\tilde A},
\qquad
\alpha(\tilde A)\,\tilde Q_1\,\tilde A^{-1}=\varepsilon_{\tilde A}\,\mathrm{Ad}_{\tilde A},
$$

so they differ by the scalar $\langle\tilde A\rangle_{\natural}\varepsilon_{\tilde A}^{-1}$ and coincide exactly when

$$
\langle\tilde A\rangle_{\natural}=\varepsilon_{\tilde A},
$$

that is on the homogeneous elements of $\mathrm{Pin}$ — odd with $\langle\cdot\rangle_{\natural}=-1$ and even with $\langle\cdot\rangle_{\natural}=+1$. The difference is the **normalisation of the sign**: the general member puts the inverse on the right factor and the sign on the left, while the conjugation sandwich puts the conjugate in place of the inverse. Both normalisations are used in the corpus under the name "signed inner conjugation", and this article is about the second. On the vector subspace the difference is visible without computation: for a vector $\tilde A$ the general member is $-\mathrm{Ad}_{\tilde A}=\rho_{\tilde A}$ for every odd parameter, whereas $\Theta_{\tilde A}$ restricts to $-\langle\tilde A\rangle_{\natural}\rho_{\tilde A}$, which is the reflection exactly on the shell $\langle\cdot\rangle_{\natural}=-1$.

## The Multiplication Law

**Proposition (composition).** For all $\tilde A,\tilde Q_2$,

$$
\Theta_{\tilde A}\circ\Theta_{\tilde Q_2}=\Theta_{\tilde A\tilde Q_2}.
$$

*Proof.* $\Theta_{\tilde A}\bigl(\Theta_{\tilde Q_2}(\tilde Q_1)\bigr)=\tilde A\tilde Q_2\tilde Q_1\tilde Q_2^{\natural}\tilde A^{\natural}=\tilde A\tilde Q_2\tilde Q_1(\tilde A\tilde Q_2)^{\natural}$ because ${}^{\natural}$ is an anti-automorphism.

**Proposition (multiplicativity up to the norm).** For all $\tilde A$ and all $\tilde Q_1,\tilde Q_3$,

$$
\Theta_{\tilde A}(\tilde Q_1)\,\Theta_{\tilde A}(\tilde Q_3)=\langle\tilde A\rangle_{\natural}\,\Theta_{\tilde A}(\tilde Q_1\tilde Q_3).
$$

*Proof.* $\tilde A\tilde Q_1\tilde A^{\natural}\tilde A\tilde Q_3\tilde A^{\natural}=\tilde A\tilde YN(\tilde A)\tilde Q_3\tilde A^{\natural}=\langle\tilde A\rangle_{\natural}\tilde A\tilde Q_1\tilde Q_3\tilde A^{\natural}$, moving the central scalar out. In particular $\Theta_{\tilde A}$ is an algebra automorphism exactly when $\langle\tilde A\rangle_{\natural}=1$, while for $\langle\tilde A\rangle_{\natural}=-1$ the operator is multiplicative up to the sign $-1$, which is the algebraic meaning of the word *signed*; read in the other order the same identity is $\Theta_{\tilde A}(\tilde Q_3)\Theta_{\tilde A}(\tilde Q_1)=\langle\tilde A\rangle_{\natural}\Theta_{\tilde A}(\tilde Q_3\tilde Q_1)$, the statement with the two factors interchanged.

**Proposition (injectivity up to sign, and the kernel).** For units $\tilde A,\tilde Q_2$, the assignment $\tilde A\mapsto\Theta_{\tilde A}$ is injective up to the sign of the parameter: $\Theta_{\tilde A}=\Theta_{\tilde Q_2}$ if and only if $\tilde Q_2=\tilde A$ or $\tilde Q_2=-\tilde A$. Moreover $\Theta_{\tilde A}=0$ if and only if $\tilde A=0$. On the unit group the kernel of the assignment is therefore $\{\pm e_t\}$, and $\Theta_{\tilde A}$ is invertible exactly when $\tilde A$ is, with inverse $\Theta_{\tilde A^{-1}}$.

*Proof.* If $\tilde A=0$ then $\Theta_{\tilde A}=0$; otherwise apply both sides to $e_t$: $\Theta_{\tilde A}(e_t)=\tilde A\tilde A^{\natural}=\langle\tilde A\rangle_{\natural}e_t$ and $\Theta_{\tilde Q_2}(e_t)=\langle\tilde Q_2\rangle_{\natural}e_t$, so $\langle\tilde A\rangle_{\natural}=\langle\tilde Q_2\rangle_{\natural}$; then apply to a general $\tilde Q_1$: $\tilde A\tilde Q_1\tilde A^{\natural}=\tilde Q_2\tilde Q_1\tilde Q_2^{\natural}$; multiplying the two sides of $\tilde A\tilde Q_1\tilde A^{\natural}=\tilde Q_2\tilde Q_1\tilde Q_2^{\natural}$ on the left by $\tilde A^{-1}$ and on the right by $\tilde A^{-\natural}$ gives $\tilde Q_1=\tilde A^{-1}\tilde Q_2\,\tilde Q_1\,\tilde Q_2^{\natural}\tilde A^{-\natural}$, so the element $\tilde C=\tilde A^{-1}\tilde Q_2$ satisfies $\tilde C\tilde Q_1\tilde C^{\natural}=\tilde Q_1$ for all $\tilde Q_1$; taking $\tilde Q_1=e_t$ gives $\langle\tilde C\rangle_{\natural}=1$ and then $\tilde Q_1\tilde C=\tilde C\tilde Q_1$ for all $\tilde Q_1$, so $\tilde C$ is central, hence $\tilde C=\lambda e_t$ with $\lambda^{2}=1$, that is $\tilde C=\pm e_t$, so $\tilde Q_2=\pm\tilde A$. The inverse statement is the composition law with $\tilde A^{-1}$.

## The Adjoint

**Proposition (the adjoint for the general quaternionic bilinear form).** The adjoint of $\Theta_{\tilde A}$ for the general quaternionic bilinear form is $\Theta_{\tilde A^{\natural}}$,

$$
\bigl(\Theta_{\tilde A}\bigr)^{N}=\Theta_{\tilde A^{\natural}},\qquad\text{that is}\qquad
\bigl\langle\Theta_{\tilde A}\tilde Q_1,\tilde Q_3\bigr\rangle_{\natural}=\bigl\langle\tilde Q_1,\Theta_{\tilde A^{\natural}}\tilde Q_3\bigr\rangle_{\natural}.
$$

*Proof.* The adjoint of a product of one-sided operators is the product of the adjoints in the reverse order, and the adjoints are $(L_{\tilde A})^{N}=L_{\tilde A^{\natural}}$ and $(R_{\tilde Q_2})^{N}=R_{\tilde Q_2^{\natural}}$ (*One-Sided Operators on the General Quaternionic Algebra*); hence $(\Theta_{\tilde A})^{N}=(L_{\tilde A}R_{\tilde A^{\natural}})^{N}=(R_{\tilde A^{\natural}})^{N}(L_{\tilde A})^{N}=R_{\tilde A^{\natural\,\natural}}L_{\tilde A^{\natural}}=R_{\tilde A}L_{\tilde A^{\natural}}=\Theta_{\tilde A^{\natural}}$, the factors commuting.

**Corollary (the self-adjoint and the skew-adjoint operators).** The operator $\Theta_{\tilde A}$ is $\langle\cdot\rangle_{\natural}$-self-adjoint exactly when $\tilde A^{\natural}=\pm\tilde A$, that is exactly when the parameter lies in one of the two eigenspaces of the natural conjugation – the centre $\mathbb{C}_{\mathbb{B}}$ or the vector subspace $\mathrm{Vect}(\mathbb{B})$; and no nonzero operator $\Theta_{\tilde A}$ is $\langle\cdot\rangle_{\natural}$-skew-adjoint.

*Proof.* Self-adjointness is $\Theta_{\tilde A^{\natural}}=\Theta_{\tilde A}$, that is $\tilde A^{\natural}\tilde Q_1\tilde A=\tilde A\tilde Q_1\tilde A^{\natural}$ for all $\tilde Q_1$, which after multiplication on both sides reads $2a_0(\tilde Q_1\vec A-\vec A\tilde Q_1)=0$ when $\tilde A=a_0e_t+\vec A$ is split into its scalar and pure parts and $\tilde Q_1$ is taken pure; hence $a_0=0$, so that $\tilde A$ is pure and $\tilde A^{\natural}=-\tilde A$, or $\vec A$ commutes with every pure element, so that $\vec A=0$ and $\tilde A$ is central with $\tilde A^{\natural}=\tilde A$. The two solutions are exactly the centre and the vector subspace. For skew-adjointness one would need $(\Theta_{\tilde A})^{N}=-\Theta_{\tilde A}$, that is $\Theta_{\tilde A^{\natural}}=\Theta_{i\tilde A}$. Evaluating at $e_t$ gives $\langle\tilde A\rangle_{\natural}=-\langle\tilde A\rangle_{\natural}$, so $\tilde A$ is null; evaluating at a pure $\tilde Q_1$ and comparing the pure parts then gives $a_0^{2}\tilde Q_1$ against $\langle \vec A\rangle_{\natural}\tilde Q_1$ on the orthogonal complement of $\vec A$, and with $\langle\tilde A\rangle_{\natural}=a_0^{2}+\langle \vec A\rangle_{\natural}=0$ this forces $a_0=0$ and $\langle \vec A\rangle_{\natural}=0$, leaving a pure null parameter, for which $\Theta_{\tilde A^{\natural}}=\Theta_{\tilde A}$ rather than $-\Theta_{\tilde A}$ unless $\tilde A=0$. So there is no nonzero skew-adjoint operator.

**Remark (the sign and the symmetry).** The two self-adjoint families are the two eigenspaces of the sign character of the algebra, which is why the criterion is a sign and not an inequality. The comparison with the Hermitian form is the sharpest illustration: in the dagger layer the adjoint pairs $\tilde A$ with $\tilde A^{*}$, self-adjointness cuts out $\mathbb{M}_+$ and skew-adjointness cuts out $\mathbb{M}_-$, both populated; here the adjoint pairs $\tilde A$ with $\tilde A^{\natural}$, and because $\natural$ is the sign on the vector subspace, the two eigenspaces of the bilinear case are the centre and the vector subspace while the skew-adjoint sector collapses (*Mixed Inner Conjugation on the General Plain Sesqualgebra*).

## When a Product $L_aR_b$ Is Two-Sided

**Proposition (the criterion).** For all $\tilde Q_1,\tilde Q_3$ the product satisfies

$$
L_{\tilde A}R_{\tilde Q_2}(\tilde Q_1)\,L_{\tilde A}R_{\tilde Q_2}(\tilde Q_3)=L_{\tilde A}R_{\tilde Q_2}\bigl(\tilde Q_1\,(\tilde Q_2\tilde A)\,\tilde Q_3\bigr),
$$

so it is multiplicative up to the scalar $\tilde Q_2\tilde A$ – that is $L(\tilde Q_1)L(\tilde Q_3)=\mu L(\tilde Q_1\tilde Q_3)$ with $\mu=\tilde Q_2\tilde A$ – exactly when the product $\tilde Q_2\tilde A$ is central, $\tilde Q_2\tilde A\in\mathbb{C}e_t$; and it is strictly multiplicative, $L(\tilde Q_1)L(\tilde Q_3)=L(\tilde Q_1\tilde Q_3)$, exactly when $\tilde Q_2\tilde A=e_t$, that is $\tilde Q_2=\tilde A^{-1}$ for a unit $\tilde A$. The strictly multiplicative products are therefore the inner automorphisms $\mathrm{Ad}_{\tilde A}$, and up to scalar multiples they are exactly the twisted two-sided operators, $\mathrm{Ad}_{\tilde A}=\langle\tilde A\rangle_{\natural}^{-1}\Theta_{\tilde A}$.

*Proof.* The left side is $\tilde A\tilde Q_1\tilde Q_2\tilde A\tilde Q_3\tilde Q_2=\tilde A\tilde Q_1(\tilde Q_2\tilde A)\tilde Q_3\tilde Q_2$, which is $L_{\tilde A}R_{\tilde Q_2}$ applied to $\tilde Q_1(\tilde Q_2\tilde A)\tilde Q_3$. When $\tilde Q_2\tilde A=\mu e_t$ the inserted scalar is central and may be moved out, giving $L(\tilde Q_1)L(\tilde Q_3)=\mu L(\tilde Q_1\tilde Q_3)$; conversely, for units $\tilde A,\tilde Q_2$ the identity for all $\tilde Q_1,\tilde Q_3$ forces $\tilde Q_1(\tilde Q_2\tilde A)\tilde Q_3=\mu\tilde Q_1\tilde Q_3$ after cancellation, hence $\tilde Q_2\tilde A=\mu e_t$, and the strict case is $\mu=1$, giving $\tilde Q_2=\tilde A^{-1}=\tilde A^{\natural}/\langle\tilde A\rangle_{\natural}$.

**Corollary (the canonical two-sided member).** With $\tilde Q_2=\lambda\tilde A^{\natural}$, the product $\tilde Q_2\tilde A=\lambda\tilde A^{\natural}\tilde A=\lambda \langle\tilde A\rangle_{\natural}e_t$ is central, so $L_{\tilde A}R_{\tilde A^{\natural}}=\Theta_{\tilde A}$ is multiplicative up to the norm; and since the strictly multiplicative products are the inner automorphisms $\mathrm{Ad}_{\tilde A}=\langle\tilde A\rangle_{\natural}^{-1}\Theta_{\tilde A}$, the products $L_{\tilde A}R_{\tilde Q_2}$ that are multiplicative up to a scalar are exactly the scalar multiples of the twisted two-sided operators $\Theta_{\tilde A}$, and this is the sense in which the signed inner conjugation is the canonical two-sided operator of the algebra.

*Proof.* The centrality is the computation of the criterion; the converse is the criterion read backwards, $\tilde Q_2\tilde A=\mu e_t$ giving $\tilde Q_2=\mu\tilde A^{-1}$ for a unit $\tilde A$, and $\tilde A^{-1}=\tilde A^{\natural}/\langle\tilde A\rangle_{\natural}$ gives $\tilde Q_2$ proportional to $\tilde A^{\natural}$.

## Automorphisms

**Proposition (the norm of the image and the automorphisms).** For all $\tilde A,\tilde Q_4$,

$$
N\bigl(\Theta_{\tilde A}(\tilde Q_4)\bigr)=\langle\tilde A\rangle_{\natural}^{2}\langle\tilde Q_4\rangle_{\natural},
$$

so that $\Theta_{\tilde A}$ is an automorphism of the general quaternionic bilinear form exactly when $\langle\tilde A\rangle_{\natural}=\pm1$; its determinant is $\det\Theta_{\tilde A}=\langle\tilde A\rangle_{\natural}^{4}$ in the coefficient basis.

*Proof.* $\langle\tilde A\tilde Q_4\tilde A^{\natural}\rangle_{\natural}=\langle\tilde A\rangle_{\natural}\langle\tilde Q_4\rangle_{\natural}\langle\tilde A^{\natural}\rangle_{\natural}=\langle\tilde A\rangle_{\natural}^{2}\langle\tilde Q_4\rangle_{\natural}$ by multiplicativity, and $\langle\tilde A^{\natural}\rangle_{\natural}=\langle\tilde A\rangle_{\natural}$; the determinant follows because $\Theta_{\tilde A}$ is the product of the left and right multiplications by $\tilde A$ and $\tilde A^{\natural}$ and each of those has determinant $\langle\tilde A\rangle_{\natural}^{2}$ in the coefficient basis.

**Corollary (the group of operators).** The set $\{\Theta_{\tilde A}:\langle\tilde A\rangle_{\natural}=\pm1\}$ is a group under composition, isomorphic to $\{\tilde A\in\mathbb{B}^\times:\langle\tilde A\rangle_{\natural}=\pm1\}/\{\pm e_t\}$, and it lies in the orthogonal group of the form; the subset with $\langle\cdot,\cdot\rangle_{\natural}=1$ lies in the special orthogonal group and consists of the inner automorphisms.

*Proof.* The composition law and the injectivity up to sign make the assignment a group homomorphism with kernel $\{\pm e_t\}$; the preservation statement is the proposition, and the determinant is $+1$ when $\langle\cdot\rangle_{\natural}=1$; the restriction to the norm-one set is the pair $\Theta_{\tilde A}=\mathrm{Ad}_{\tilde A}$ of an automorphism. The group is the biquaternion pin group, developed in *The Pin and Spin Groups of the General Quaternionic Algebra*.

## The Dagger Adjoint

**Proposition (the adjoint for the Hermitian form).** For the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$,

$$
\bigl\langle\Theta_{\tilde A}\tilde Q_1,\tilde Q_3\bigr\rangle_{*}=\bigl\langle\tilde Q_1,\Theta_{\tilde A^{*}}\tilde Q_3\bigr\rangle_{*},
$$

so that the adjoint is $\bigl(\Theta_{\tilde A}\bigr)^{*}=\Theta_{\tilde A^{*}}$; the operator is self-adjoint exactly for $\tilde A^{*}=\pm\tilde A$, that is for $\tilde A$ in $\mathbb{M}_+$ or in $\mathbb{M}_-$, and it is unitary for the Hermitian form exactly when $\tilde A^{*}\tilde A=e_t$, that is on the slice $U$ of the unitary elements of norm one.

*Proof.* Multiplying out, $\langle\Theta_{\tilde A}\tilde Q_1,\tilde Q_3\rangle_{*}=\mathrm{Sc}(\tilde A\tilde Q_1\tilde A^{\natural}\tilde Q_3^{*})$ and $\langle\tilde Q_1,\Theta_{\tilde A^{*}}\tilde Q_3\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde A^{\natural}\tilde Q_3^{*}\tilde A)$, and the two agree by the cyclic property of the scalar part together with $(\tilde A^{*})^{\natural}=\tilde A^{\natural*}$, which follows from ${}^{\natural}$ and ${}^{*}$ commuting. Self-adjointness is $(\Theta_{\tilde A})^{*}=\Theta_{\tilde A}$, that is $\Theta_{\tilde A^{*}}=\Theta_{\tilde A}$, that is $\tilde A^{*}=\pm\tilde A$; the plus is the Hermitian sector $\mathbb{M}_+$ and the minus the anti-Hermitian sector $\mathbb{M}_-$, both populated, since the operator is blind to the overall sign of its parameter. Unitarity is $(\Theta_{\tilde A})^{*}\Theta_{\tilde A}=\mathrm{id}$, that is $\Theta_{\tilde A^{*}\tilde A}=\mathrm{id}$, that is $\tilde A^{*}\tilde A=\pm e_t$, and the minus is impossible because $\langle\tilde A^{*}\tilde A\rangle_{\natural}=\langle\tilde A^{*}\rangle_{\natural}\langle\tilde A\rangle_{\natural}=\overline{\langle\tilde A\rangle_{\natural}}\langle\tilde A\rangle_{\natural}=\lvert \langle\tilde A\rangle_{\natural}\rvert^{2}$ is a non-negative real while $\langle -e_t\rangle_{\natural}=-1$. The dagger layer, with its two sectors and its mixed operators, is *Mixed Inner Conjugation on the General Plain Sesqualgebra*.

## Worked Examples

**A unit of norm one.** For $\tilde A=e_t+\vec e_x$, $\langle\tilde A\rangle_{\natural}=2$, so $\Theta_{\tilde A}=2\,\mathrm{Ad}_{\tilde A}$; the operator preserves the form up to $\langle\tilde A\rangle_{\natural}^{2}=4$ and is not a form-preserving map. Scaling to $\tilde A_2=(e_t+\vec e_x)/\sqrt2$ gives $\langle\cdot,\cdot\rangle_{\natural}=1$ and $\Theta_{\tilde A_2}=\mathrm{Ad}_{\tilde A_2}$, an inner automorphism and a form-preserving map.

**A null parameter.** For $\tilde A=\vec e_x+i\vec e_y$, $\langle\tilde A\rangle_{\natural}=0$ and $\Theta_{\tilde A}(\tilde Q_1)=\tilde A\tilde Q_1\tilde A^{\natural}$; the operator is nonzero but has $\Theta_{\tilde A}(e_t)=0$ and is not invertible, in agreement with the criterion that $\Theta$ is invertible exactly on the units.

**A vector parameter.** For $\tilde R=\vec e_x$ one has $\tilde R^{\natural}=-\vec e_x$, so $\Theta_{\tilde R}(\tilde Q_1)=-\vec e_x\tilde Q_1 \vec e_x$, with $\langle\tilde R\rangle_{\natural}=1$: the operator is a form-preserving map, $\Theta_{\tilde R}(e_t)=e_t$ and $\Theta_{\tilde R}(\vec e_y)=-\vec e_y$. Its restriction to the vector subspace is the reflection, up to sign, described in *The Pin and Spin Groups of the General Quaternionic Algebra*.

**A parameter of norm minus one.** For $\tilde A=ie_t$, $\langle\tilde A\rangle_{\natural}=-1$ and $\tilde A^{\natural}=ie_t$, so $\Theta_{\tilde A}(\tilde Q_1)=-\tilde Q_1$: the operator is a scalar, of norm $\pm1$ and orthogonal, of determinant $+1$; the kernel $\{\pm e_t\}$ of the assignment contains both $\tilde A$ and $-\tilde A$, and the two give the same operator.

## Summary

The **twisted two-sided operator** of the biquaternion algebra is $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$, the conjugation sandwich $\tilde Q_1\mapsto\tilde A\tilde Q_1\tilde A^{\natural}$: quadratic in the parameter, with $\Theta_{-\tilde A}=\Theta_{\tilde A}$ and $\Theta_{i\tilde A}=-\Theta_{\tilde A}$, defined for every element, and equal to $\langle\tilde A\rangle_{\natural}$ times the inner conjugation $\mathrm{Ad}_{\tilde A}$ on the units. It satisfies $\Theta_{\tilde A}\circ\Theta_{\tilde Q_2}=\Theta_{\tilde A\tilde Q_2}$ and $\Theta_{\tilde A}(\tilde Q_1)\Theta_{\tilde A}(\tilde Q_3)=\langle\tilde A\rangle_{\natural}\Theta_{\tilde A}(\tilde Q_1\tilde Q_3)$, so that it is an algebra automorphism exactly on the norm-one set and is multiplicative up to the sign $-1$ for norm minus one. The assignment is injective up to sign on the units, with kernel $\{\pm e_t\}$, and $\Theta_{\tilde A}=0$ only for $\tilde A=0$; its adjoint for the general quaternionic bilinear form is $\Theta_{\tilde A^{\natural}}$, the self-adjoint operators being exactly the parameters lying in the centre or the vector subspace and the skew-adjoint ones nonexistent; and its adjoint for the Hermitian form is $\Theta_{\tilde A^{*}}$, with self-adjointness on $\mathbb{M}_+\cup\mathbb{M}_-$ and unitarity on the slice $U$. Among the products $L_{\tilde A}R_{\tilde Q_2}$, those that are multiplicative up to a scalar are exactly the ones with $\tilde Q_2\tilde A$ central, that is, up to scalars, $\tilde Q_2$ proportional to $\tilde A^{\natural}$, the strictly multiplicative ones being the inner automorphisms $\mathrm{Ad}_{\tilde A}$; so it is $\Theta$ that is canonical. The operator is an automorphism of the general quaternionic bilinear form exactly when $\langle\tilde A\rangle_{\natural}=\pm1$, and it is that condition that cuts out the pin and spin groups.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_{\tilde A}(\tilde Q_1)=\tilde A\tilde Q_1\tilde A^{\natural}$ | The twisted two-sided operator; the conjugation sandwich |
| $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$ | Its one-sided factorisation |
| $\Theta_{\tilde A}\circ\Theta_{\tilde Q_2}=\Theta_{\tilde A\tilde Q_2}$ | The composition law |
| $\Theta_{\tilde A}(\tilde Q_1)\Theta_{\tilde A}(\tilde Q_3)=\langle\tilde A\rangle_{\natural}\Theta_{\tilde A}(\tilde Q_1\tilde Q_3)$ | Multiplicativity up to the norm |
| $\Theta_{\tilde A}=\Theta_{\tilde Q_2}\iff\tilde Q_2=\pm\tilde A$ | Injectivity up to sign; kernel $\{\pm e_t\}$ on the units |
| $(\Theta_{\tilde A})^{N}=\Theta_{\tilde A^{\natural}}$, $(\Theta_{\tilde A})^{*}=\Theta_{\tilde A^{*}}$ | The adjoints for the bilinear and the Hermitian forms |
| $\langle\Theta_{\tilde A}\tilde Q_4\rangle_{\natural}=\langle\tilde A\rangle_{\natural}^{2}\langle\tilde Q_4\rangle_{\natural}$ | The form preservation condition $\langle\tilde A\rangle_{\natural}=\pm1$ |
| $\tilde Q_2\tilde A$ central; $=e_t$ | $L_{\tilde A}R_{\tilde Q_2}$ multiplicative up to the scalar $\tilde Q_2\tilde A$; strictly multiplicative for $\tilde Q_2\tilde A=e_t$ |

## Further Reading

- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the signed inner conjugation $\tilde A^{\natural}\tilde Q_4\tilde A^{-1}$ against the unsigned $\tilde A\tilde Q_4\tilde A^{-1}$, their difference $-2\vec A\tilde Q_4\tilde A^{-1}$ and the two matrices of the sign
- *One-Sided Operators on the General Quaternionic Algebra* (`articles_maths/one-sided-operators-on-the-general-quaternionic-algebra.md`), for the factors
- *The Pin and Spin Groups of the General Quaternionic Algebra* (`articles_maths/the-pin-and-spin-groups-of-the-general-quaternionic-algebra.md`), for the groups cut out by the norm
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the general quaternionic bilinear form and its Gram matrix
- *Mixed Inner Conjugation on the General Plain Sesqualgebra* (`articles_maths/mixed-inner-conjugation-on-the-general-plain-sesqualgebra.md`), for the corresponding family over the dagger
- *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* (`articles_maths/two-sided-operators-on-a-clifford-algebra-with-signed-inner-conjugation.md`), for the general theory
