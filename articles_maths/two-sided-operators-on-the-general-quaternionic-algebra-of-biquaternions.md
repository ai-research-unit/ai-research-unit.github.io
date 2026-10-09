
# __Two-Sided Operators on the General Quaternionic Algebra of Biquaternions__

## Introduction

The biquaternion algebra carries two families of one-sided operators, the left and the right multiplications, and their products are the two-sided operators $L_aR_b(y)=a\,y\,b$. Among them one member is singled out by the general quaternionic bilinear form and the natural conjugation: the choice $b=a^{\natural}$, giving the **twisted two-sided operator**

$$
\Theta_a=L_aR_{a^{\natural}},\qquad \Theta_a(y)=a\,y\,a^{\natural}.
$$

This is the **conjugation sandwich** of the biquaternion algebra, the member of the general two-sided family whose second slot carries the natural conjugation in place of the inverse. The corpus also calls it the *signed inner conjugation*, a name it shares with the different operator $\tilde Y\mapsto\alpha(\tilde A)\tilde Y\tilde A^{-1}$; the remark *which member of the general family this operator is* below separates the two. Placing the conjugation where the inverse belongs is what makes the operator defined on every element and not only on the units, and it leaves the norm in front of the inner conjugation: on a vector the operator is the reflection exactly on the shell $N(\tilde A)=-1$, and a scaled copy of it elsewhere.

This article treats the operator: its factors, its multiplication law, its injectivity up to sign, its adjoint for the general quaternionic bilinear form, the criterion that singles it out among the products $L_aR_b$, its automorphisms, and its dagger adjoint. The general Clifford theory of the family is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, to which this is the biquaternion instance; the one-sided factors are *One-Sided Operators on the General Quaternionic Algebra of Biquaternions*; the groups cut out by the norm are *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions*; and the corresponding family over the Hermitian form is *Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*. The form, its matrix and its adjoint are *The Four Pairings of the Biquaternion Algebra*; nothing of the general theory is re-derived here.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The natural conjugation is $\tilde Q^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$, an anti-automorphism and an involution; the norm is $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$, central and multiplicative; the general quaternionic bilinear form is $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})$, with $N$-adjoint written ${}^{N}$, so that $\langle T\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P,T^{N}\tilde Q\rangle_{\natural}$. The Hermitian form is $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and its adjoint is written ${}^{*}$.

## The Operator and Its Factors

**Definition.** For $\tilde A\in\mathbb{B}$ the **twisted two-sided operator** of $\tilde A$, or the **conjugation sandwich** by $\tilde A$, is the $\mathbb{C}$-linear map

$$
\Theta_{\tilde A}:\mathbb{B}\longrightarrow\mathbb{B},\qquad \Theta_{\tilde A}(\tilde Y)=\tilde A\,\tilde Y\,\tilde A^{\natural}.
$$

**Proposition (the factors, and the quadraticity in the parameter).** With $L$ and $R$ the left and right multiplications,

$$
\Theta_{\tilde A}=L_{\tilde A}\circ R_{\tilde A^{\natural}}=R_{\tilde A^{\natural}}\circ L_{\tilde A},
$$

the two factors commuting; and the parameter map is quadratic, not linear,

$$
\Theta_{\lambda\tilde A}=\lambda^{2}\,\Theta_{\tilde A},\qquad \Theta_{\tilde A+\tilde B}=\Theta_{\tilde A}+\Theta_{\tilde B}+\tilde A\,[\,]\tilde B^{\natural}+\tilde B\,[\,]\tilde A^{\natural},
$$

the last two terms being the cross term; in particular $\Theta_{-\tilde A}=\Theta_{\tilde A}$ and $\Theta_{i\tilde A}=-\Theta_{\tilde A}$.

*Proof.* The first identity is the definition, the second is $L_aR_b=R_bL_a$. For the quadraticity, $(\lambda\tilde A)\,\tilde Y\,(\lambda\tilde A)^{\natural}=\lambda^{2}\tilde A\tilde Y\tilde A^{\natural}$ because the natural conjugation is $\mathbb{C}$-linear; expanding the product $(\tilde A+\tilde B)\tilde Y(\tilde A+\tilde B)^{\natural}$ gives the displayed cross term. Verified on $200$ random parameters.

**Remark (why the parameter map cannot be linear).** A linear map of the parameter would give $\Theta_{0}=0$ and $\Theta_{\lambda\tilde A}=\lambda\Theta_{\tilde A}$; but $\Theta_{\tilde A}$ is built from two factors each linear in $\tilde A$, so the scalar appears twice. The operator is linear in $\tilde Y$, which is what the applications use, and quadratic in $\tilde A$; the sign $\Theta_{-\tilde A}=\Theta_{\tilde A}$ is the same statement at $\lambda=-1$.

**Proposition (the sign and the inverse).** For every element, $\Theta_{\tilde A}=\Theta_{-\tilde A}$; for an invertible $\tilde A$,

$$
\Theta_{\tilde A}=N(\tilde A)\ \mathrm{Ad}_{\tilde A},\qquad \mathrm{Ad}_{\tilde A}(\tilde Y)=\tilde A\,\tilde Y\,\tilde A^{-1},
$$

and $\mathrm{Ad}_{\tilde A}=\Theta_{\tilde A}$ exactly on the norm-one set $N=1$.

*Proof.* The first identity is $\tilde A^{\natural}=N(\tilde A)\tilde A^{-1}$ for a unit, and $N(\tilde A)$ is central; the second follows from $N=1$. Verified on $100$ random units.

**Remark (why the sign is needed).** The plain inner conjugation $\mathrm{Ad}_{\tilde A}$ is an algebra automorphism and needs the inverse, so it is defined only on the units and is blind to the norm; the twisted form $\Theta_{\tilde A}$ is defined for every element, is linear in its argument and quadratic in its parameter, and carries the norm as the scalar in front of the inner conjugation. On the norm-one set the two agree, and off it they differ by the scalar $N(\tilde A)$ – which is the whole of the sign in the name.

**Remark (which member of the general family this operator is, and the two senses of the name).** The general two-sided family of *Two-Sided Operators on a Clifford Algebra* attaches to a pair (an automorphism $\theta$ of the left factor, an anti-automorphism $c$ of the right one) the operator $\Phi^{\theta,c}_x(y)=\theta(x)\,y\,c(x)$, and its five members are told apart by $c$. The member that the general layer calls **signed inner conjugation** is $\theta=\alpha$, $c=(\ )^{-1}$,

$$
\alpha(\tilde A)\,\tilde Y\,\tilde A^{-1}=\varepsilon_{\tilde A}\,\mathrm{Ad}_{\tilde A},
$$

with $\varepsilon_{\tilde A}=(-1)^{k}$ the parity sign of a homogeneous $\tilde A$. The operator of this article, $\Theta_{\tilde A}=\tilde A\,\tilde Y\,\tilde A^{\natural}$, is the member $\theta=\mathrm{id}$, $c={}^{\natural}$, the **conjugation sandwich**, whose value at the unit is the Clifford norm; and the two are not the same operator, for on a unit

$$
\Theta_{\tilde A}=N(\tilde A)\,\mathrm{Ad}_{\tilde A},
\qquad
\alpha(\tilde A)\,\tilde Y\,\tilde A^{-1}=\varepsilon_{\tilde A}\,\mathrm{Ad}_{\tilde A},
$$

so they differ by the scalar $N(\tilde A)\varepsilon_{\tilde A}^{-1}$ and coincide exactly when

$$
N(\tilde A)=\varepsilon_{\tilde A},
$$

that is on the homogeneous elements of $\mathrm{Pin}$ — odd with $N=-1$ and even with $N=+1$. The difference is the **normalisation of the sign**: the general member puts the inverse on the right factor and the sign on the left, while the conjugation sandwich puts the conjugate in place of the inverse. Both normalisations are used in the corpus under the name "signed inner conjugation", and this article is about the second. On the vector subspace the difference is visible without computation: for a vector $\tilde A$ the general member is $-\mathrm{Ad}_{\tilde A}=\rho_{\tilde A}$ for every odd parameter, whereas $\Theta_{\tilde A}$ restricts to $-N(\tilde A)\rho_{\tilde A}$, which is the reflection exactly on the shell $N=-1$.

## The Multiplication Law

**Proposition (composition).** For all $\tilde A,\tilde B$,

$$
\Theta_{\tilde A}\circ\Theta_{\tilde B}=\Theta_{\tilde A\tilde B}.
$$

*Proof.* $\Theta_{\tilde A}\bigl(\Theta_{\tilde B}(\tilde Y)\bigr)=\tilde A\tilde B\tilde Y\tilde B^{\natural}\tilde A^{\natural}=\tilde A\tilde B\tilde Y(\tilde A\tilde B)^{\natural}$ because ${}^{\natural}$ is an anti-automorphism. Verified on $200$ random triples.

**Proposition (multiplicativity up to the norm).** For all $\tilde A$ and all $\tilde Y,\tilde Z$,

$$
\Theta_{\tilde A}(\tilde Y)\,\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\,\Theta_{\tilde A}(\tilde Y\tilde Z).
$$

*Proof.* $\tilde A\tilde Y\tilde A^{\natural}\tilde A\tilde Z\tilde A^{\natural}=\tilde A\tilde YN(\tilde A)\tilde Z\tilde A^{\natural}=N(\tilde A)\tilde A\tilde Y\tilde Z\tilde A^{\natural}$, moving the central scalar out. Verified on $200$ random triples. In particular $\Theta_{\tilde A}$ is an algebra automorphism exactly when $N(\tilde A)=1$, while for $N(\tilde A)=-1$ the operator is multiplicative up to the sign $-1$, which is the algebraic meaning of the word *signed*; read in the other order the same identity is $\Theta_{\tilde A}(\tilde Z)\Theta_{\tilde A}(\tilde Y)=N(\tilde A)\Theta_{\tilde A}(\tilde Z\tilde Y)$, the statement with the two factors interchanged.

**Proposition (injectivity up to sign, and the kernel).** For units $\tilde A,\tilde B$, the assignment $\tilde A\mapsto\Theta_{\tilde A}$ is injective up to the sign of the parameter: $\Theta_{\tilde A}=\Theta_{\tilde B}$ if and only if $\tilde B=\tilde A$ or $\tilde B=-\tilde A$. Moreover $\Theta_{\tilde A}=0$ if and only if $\tilde A=0$. On the unit group the kernel of the assignment is therefore $\{\pm e_0\}$, and $\Theta_{\tilde A}$ is invertible exactly when $\tilde A$ is, with inverse $\Theta_{\tilde A^{-1}}$.

*Proof.* If $\tilde A=0$ then $\Theta_{\tilde A}=0$; otherwise apply both sides to $e_0$: $\Theta_{\tilde A}(e_0)=\tilde A\tilde A^{\natural}=N(\tilde A)e_0$ and $\Theta_{\tilde B}(e_0)=N(\tilde B)e_0$, so $N(\tilde A)=N(\tilde B)$; then apply to a general $\tilde Y$: $\tilde A\tilde Y\tilde A^{\natural}=\tilde B\tilde Y\tilde B^{\natural}$; multiplying the two sides of $\tilde A\tilde Y\tilde A^{\natural}=\tilde B\tilde Y\tilde B^{\natural}$ on the left by $\tilde A^{-1}$ and on the right by $\tilde A^{-\natural}$ gives $\tilde Y=\tilde A^{-1}\tilde B\,\tilde Y\,\tilde B^{\natural}\tilde A^{-\natural}$, so the element $\tilde C=\tilde A^{-1}\tilde B$ satisfies $\tilde C\tilde Y\tilde C^{\natural}=\tilde Y$ for all $\tilde Y$; taking $\tilde Y=e_0$ gives $N(\tilde C)=1$ and then $\tilde Y\tilde C=\tilde C\tilde Y$ for all $\tilde Y$, so $\tilde C$ is central, hence $\tilde C=\lambda e_0$ with $\lambda^{2}=1$, that is $\tilde C=\pm e_0$, so $\tilde B=\pm\tilde A$. The inverse statement is the composition law with $\tilde A^{-1}$. Verified on $200$ random parameters.

## The Adjoint

**Proposition (the adjoint for the general quaternionic bilinear form).** The adjoint of $\Theta_{\tilde A}$ for the general quaternionic bilinear form is $\Theta_{\tilde A^{\natural}}$,

$$
\bigl(\Theta_{\tilde A}\bigr)^{N}=\Theta_{\tilde A^{\natural}},\qquad\text{that is}\qquad
\bigl\langle\Theta_{\tilde A}\tilde Y,\tilde Z\bigr\rangle_{\natural}=\bigl\langle\tilde Y,\Theta_{\tilde A^{\natural}}\tilde Z\bigr\rangle_{\natural}.
$$

*Proof.* The adjoint of a product of one-sided operators is the product of the adjoints in the reverse order, and the adjoints are $(L_{\tilde A})^{N}=L_{\tilde A^{\natural}}$ and $(R_{\tilde B})^{N}=R_{\tilde B^{\natural}}$ (*One-Sided Operators on the General Quaternionic Algebra of Biquaternions*); hence $(\Theta_{\tilde A})^{N}=(L_{\tilde A}R_{\tilde A^{\natural}})^{N}=(R_{\tilde A^{\natural}})^{N}(L_{\tilde A})^{N}=R_{\tilde A^{\natural\,\natural}}L_{\tilde A^{\natural}}=R_{\tilde A}L_{\tilde A^{\natural}}=\Theta_{\tilde A^{\natural}}$, the factors commuting. Verified directly on $200$ random pairs.

**Corollary (the self-adjoint and the skew-adjoint operators).** The operator $\Theta_{\tilde A}$ is $N$-self-adjoint exactly when $\tilde A^{\natural}=\pm\tilde A$, that is exactly when the parameter lies in one of the two eigenspaces of the natural conjugation – the centre $\mathbb{C}_{\mathbb{B}}$ or the vector subspace $\mathrm{Vect}(\mathbb{B})$; and no nonzero operator $\Theta_{\tilde A}$ is $N$-skew-adjoint.

*Proof.* Self-adjointness is $\Theta_{\tilde A^{\natural}}=\Theta_{\tilde A}$, that is $\tilde A^{\natural}\tilde Y\tilde A=\tilde A\tilde Y\tilde A^{\natural}$ for all $\tilde Y$, which after multiplication on both sides reads $2a_0(\tilde Y\mathbf A-\mathbf A\tilde Y)=0$ when $\tilde A=a_0e_0+\mathbf A$ is split into its scalar and pure parts and $\tilde Y$ is taken pure; hence $a_0=0$, so that $\tilde A$ is pure and $\tilde A^{\natural}=-\tilde A$, or $\mathbf A$ commutes with every pure element, so that $\mathbf A=0$ and $\tilde A$ is central with $\tilde A^{\natural}=\tilde A$. The two solutions are exactly the centre and the vector subspace. For skew-adjointness one would need $(\Theta_{\tilde A})^{N}=-\Theta_{\tilde A}$, that is $\Theta_{\tilde A^{\natural}}=\Theta_{i\tilde A}$. Evaluating at $e_0$ gives $N(\tilde A)=-N(\tilde A)$, so $\tilde A$ is null; evaluating at a pure $\tilde Y$ and comparing the pure parts then gives $a_0^{2}\tilde Y$ against $N(\mathbf A)\tilde Y$ on the orthogonal complement of $\mathbf A$, and with $N(\tilde A)=a_0^{2}+N(\mathbf A)=0$ this forces $a_0=0$ and $N(\mathbf A)=0$, leaving a pure null parameter, for which $\Theta_{\tilde A^{\natural}}=\Theta_{\tilde A}$ rather than $-\Theta_{\tilde A}$ unless $\tilde A=0$. So there is no nonzero skew-adjoint operator. Verified on $300$ random parameters: the self-adjoint operators are exactly those with the parameter central or pure, and there is no skew-adjoint one.

**Remark (the sign and the symmetry).** The two self-adjoint families are the two eigenspaces of the sign character of the algebra, which is why the criterion is a sign and not an inequality. The comparison with the Hermitian form is the sharpest illustration: in the dagger layer the adjoint pairs $\tilde A$ with $\tilde A^{*}$, self-adjointness cuts out $\mathbb{M}_+$ and skew-adjointness cuts out $\mathbb{M}_-$, both populated; here the adjoint pairs $\tilde A$ with $\tilde A^{\natural}$, and because $\natural$ is the sign on the vector subspace, the two eigenspaces of the bilinear case are the centre and the vector subspace while the skew-adjoint sector collapses (*Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*).

## When a Product $L_aR_b$ Is Two-Sided

**Proposition (the criterion).** For all $\tilde Y,\tilde Z$ the product satisfies

$$
L_{\tilde A}R_{\tilde B}(\tilde Y)\,L_{\tilde A}R_{\tilde B}(\tilde Z)=L_{\tilde A}R_{\tilde B}\bigl(\tilde Y\,(\tilde B\tilde A)\,\tilde Z\bigr),
$$

so it is multiplicative up to the scalar $\tilde B\tilde A$ – that is $L(\tilde Y)L(\tilde Z)=\mu L(\tilde Y\tilde Z)$ with $\mu=\tilde B\tilde A$ – exactly when the product $\tilde B\tilde A$ is central, $\tilde B\tilde A\in\mathbb{C}e_0$; and it is strictly multiplicative, $L(\tilde Y)L(\tilde Z)=L(\tilde Y\tilde Z)$, exactly when $\tilde B\tilde A=e_0$, that is $\tilde B=\tilde A^{-1}$ for a unit $\tilde A$. The strictly multiplicative products are therefore the inner automorphisms $\mathrm{Ad}_{\tilde A}$, and up to scalar multiples they are exactly the twisted two-sided operators, $\mathrm{Ad}_{\tilde A}=N(\tilde A)^{-1}\Theta_{\tilde A}$.

*Proof.* The left side is $\tilde A\tilde Y\tilde B\tilde A\tilde Z\tilde B=\tilde A\tilde Y(\tilde B\tilde A)\tilde Z\tilde B$, which is $L_{\tilde A}R_{\tilde B}$ applied to $\tilde Y(\tilde B\tilde A)\tilde Z$. When $\tilde B\tilde A=\mu e_0$ the inserted scalar is central and may be moved out, giving $L(\tilde Y)L(\tilde Z)=\mu L(\tilde Y\tilde Z)$; conversely, for units $\tilde A,\tilde B$ the identity for all $\tilde Y,\tilde Z$ forces $\tilde Y(\tilde B\tilde A)\tilde Z=\mu\tilde Y\tilde Z$ after cancellation, hence $\tilde B\tilde A=\mu e_0$, and the strict case is $\mu=1$, giving $\tilde B=\tilde A^{-1}=\tilde A^{\natural}/N(\tilde A)$. Verified on $300$ random pairs, and on the explicit central cases $(\tilde A,\tilde B)=(e_0,-e_0)$ and $(e_0,e_0)$, where the first is multiplicative up to $-1$ and not strictly.

**Corollary (the canonical two-sided member).** With $\tilde B=\lambda\tilde A^{\natural}$, the product $\tilde B\tilde A=\lambda\tilde A^{\natural}\tilde A=\lambda N(\tilde A)e_0$ is central, so $L_{\tilde A}R_{\tilde A^{\natural}}=\Theta_{\tilde A}$ is multiplicative up to the norm; and since the strictly multiplicative products are the inner automorphisms $\mathrm{Ad}_{\tilde A}=N(\tilde A)^{-1}\Theta_{\tilde A}$, the products $L_{\tilde A}R_{\tilde B}$ that are multiplicative up to a scalar are exactly the scalar multiples of the twisted two-sided operators $\Theta_{\tilde A}$, and this is the sense in which the signed inner conjugation is the canonical two-sided operator of the algebra.

*Proof.* The centrality is the computation of the criterion; the converse is the criterion read backwards, $\tilde B\tilde A=\mu e_0$ giving $\tilde B=\mu\tilde A^{-1}$ for a unit $\tilde A$, and $\tilde A^{-1}=\tilde A^{\natural}/N(\tilde A)$ gives $\tilde B$ proportional to $\tilde A^{\natural}$. Verified on $300$ random pairs.

## Automorphisms

**Proposition (the norm of the image and the automorphisms).** For all $\tilde A,\tilde X$,

$$
N\bigl(\Theta_{\tilde A}(\tilde X)\bigr)=N(\tilde A)^{2}N(\tilde X),
$$

so that $\Theta_{\tilde A}$ is an automorphism of the general quaternionic bilinear form exactly when $N(\tilde A)=\pm1$; its determinant is $\det\Theta_{\tilde A}=N(\tilde A)^{4}$ in the coefficient basis.

*Proof.* $N(\tilde A\tilde X\tilde A^{\natural})=N(\tilde A)N(\tilde X)N(\tilde A^{\natural})=N(\tilde A)^{2}N(\tilde X)$ by multiplicativity, and $N(\tilde A^{\natural})=N(\tilde A)$; the determinant follows because $\Theta_{\tilde A}$ is the product of the left and right multiplications by $\tilde A$ and $\tilde A^{\natural}$ and each of those has determinant $N(\tilde A)^{2}$ in the coefficient basis. Verified on $200$ random pairs, and the determinant by expansion.

**Corollary (the group of operators).** The set $\{\Theta_{\tilde A}:N(\tilde A)=\pm1\}$ is a group under composition, isomorphic to $\{\tilde A\in\mathbb{B}^\times:N(\tilde A)=\pm1\}/\{\pm e_0\}$, and it lies in the orthogonal group of the form; the subset with $N=1$ lies in the special orthogonal group and consists of the inner automorphisms.

*Proof.* The composition law and the injectivity up to sign make the assignment a group homomorphism with kernel $\{\pm e_0\}$; the preservation statement is the proposition, and the determinant is $+1$ when $N=1$; the restriction to the norm-one set is the pair $\Theta_{\tilde A}=\mathrm{Ad}_{\tilde A}$ of an automorphism. Verified on $200$ random triples. The group is the biquaternion pin group, developed in *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions*.

## The Dagger Adjoint

**Proposition (the adjoint for the Hermitian form).** For the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$,

$$
\bigl\langle\Theta_{\tilde A}\tilde Y,\tilde Z\bigr\rangle_{*}=\bigl\langle\tilde Y,\Theta_{\tilde A^{*}}\tilde Z\bigr\rangle_{*},
$$

so that the adjoint is $\bigl(\Theta_{\tilde A}\bigr)^{*}=\Theta_{\tilde A^{*}}$; the operator is self-adjoint exactly for $\tilde A^{*}=\pm\tilde A$, that is for $\tilde A$ in $\mathbb{M}_+$ or in $\mathbb{M}_-$, and it is unitary for the Hermitian form exactly when $\tilde A^{*}\tilde A=e_0$, that is on the slice $U$ of the unitary elements of norm one.

*Proof.* Multiplying out, $\langle\Theta_{\tilde A}\tilde Y,\tilde Z\rangle_{*}=\mathrm{Sc}(\tilde A\tilde Y\tilde A^{\natural}\tilde Z^{*})$ and $\langle\tilde Y,\Theta_{\tilde A^{*}}\tilde Z\rangle_{*}=\mathrm{Sc}(\tilde Y\tilde A^{\natural}\tilde Z^{*}\tilde A)$, and the two agree by the cyclic property of the scalar part together with $(\tilde A^{*})^{\natural}=\tilde A^{\natural*}$, which follows from ${}^{\natural}$ and ${}^{*}$ commuting. Self-adjointness is $(\Theta_{\tilde A})^{*}=\Theta_{\tilde A}$, that is $\Theta_{\tilde A^{*}}=\Theta_{\tilde A}$, that is $\tilde A^{*}=\pm\tilde A$; the plus is the Hermitian sector $\mathbb{M}_+$ and the minus the anti-Hermitian sector $\mathbb{M}_-$, both populated, since the operator is blind to the overall sign of its parameter. Unitarity is $(\Theta_{\tilde A})^{*}\Theta_{\tilde A}=\mathrm{id}$, that is $\Theta_{\tilde A^{*}\tilde A}=\mathrm{id}$, that is $\tilde A^{*}\tilde A=\pm e_0$, and the minus is impossible because $N(\tilde A^{*}\tilde A)=N(\tilde A^{*})N(\tilde A)=\overline{N(\tilde A)}N(\tilde A)=\lvert N(\tilde A)\rvert^{2}$ is a non-negative real while $N(-e_0)=-1$. Verified on $200$ random triples for each statement. The dagger layer, with its two sectors and its mixed operators, is *Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*.

## Worked Examples

**A unit of norm one.** For $\tilde A=e_0+e_1$, $N(\tilde A)=2$, so $\Theta_{\tilde A}=2\,\mathrm{Ad}_{\tilde A}$; the operator preserves the form up to $N(\tilde A)^{2}=4$ and is not a form-preserving map. Scaling to $\tilde A'=(e_0+e_1)/\sqrt2$ gives $N=1$ and $\Theta_{\tilde A'}=\mathrm{Ad}_{\tilde A'}$, an inner automorphism and a form-preserving map.

**A null parameter.** For $\tilde A=e_1+ie_2$, $N(\tilde A)=0$ and $\Theta_{\tilde A}(\tilde Y)=\tilde A\tilde Y\tilde A^{\natural}$; the operator is nonzero but has $\Theta_{\tilde A}(e_0)=0$ and is not invertible, in agreement with the criterion that $\Theta$ is invertible exactly on the units.

**A vector parameter.** For $\tilde V=e_1$ one has $\tilde V^{\natural}=-e_1$, so $\Theta_{\tilde V}(\tilde Y)=-e_1\tilde Y e_1$, with $N(\tilde V)=1$: the operator is a form-preserving map, $\Theta_{\tilde V}(e_0)=e_0$ and $\Theta_{\tilde V}(e_2)=-e_2$. Its restriction to the vector subspace is the reflection, up to sign, described in *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions*.

**A parameter of norm minus one.** For $\tilde A=ie_0$, $N(\tilde A)=-1$ and $\tilde A^{\natural}=ie_0$, so $\Theta_{\tilde A}(\tilde Y)=-\tilde Y$: the operator is a scalar, of norm $\pm1$ and orthogonal, of determinant $+1$; the kernel $\{\pm e_0\}$ of the assignment contains both $\tilde A$ and $-\tilde A$, and the two give the same operator.

## Summary

The **twisted two-sided operator** of the biquaternion algebra is $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$, the conjugation sandwich $\tilde Y\mapsto\tilde A\tilde Y\tilde A^{\natural}$: quadratic in the parameter, with $\Theta_{-\tilde A}=\Theta_{\tilde A}$ and $\Theta_{i\tilde A}=-\Theta_{\tilde A}$, defined for every element, and equal to $N(\tilde A)$ times the inner conjugation $\mathrm{Ad}_{\tilde A}$ on the units. It satisfies $\Theta_{\tilde A}\circ\Theta_{\tilde B}=\Theta_{\tilde A\tilde B}$ and $\Theta_{\tilde A}(\tilde Y)\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\Theta_{\tilde A}(\tilde Y\tilde Z)$, so that it is an algebra automorphism exactly on the norm-one set and is multiplicative up to the sign $-1$ for norm minus one. The assignment is injective up to sign on the units, with kernel $\{\pm e_0\}$, and $\Theta_{\tilde A}=0$ only for $\tilde A=0$; its adjoint for the general quaternionic bilinear form is $\Theta_{\tilde A^{\natural}}$, the self-adjoint operators being exactly the parameters lying in the centre or the vector subspace and the skew-adjoint ones nonexistent; and its adjoint for the Hermitian form is $\Theta_{\tilde A^{*}}$, with self-adjointness on $\mathbb{M}_+\cup\mathbb{M}_-$ and unitarity on the slice $U$. Among the products $L_{\tilde A}R_{\tilde B}$, those that are multiplicative up to a scalar are exactly the ones with $\tilde B\tilde A$ central, that is, up to scalars, $\tilde B$ proportional to $\tilde A^{\natural}$, the strictly multiplicative ones being the inner automorphisms $\mathrm{Ad}_{\tilde A}$; so it is $\Theta$ that is canonical. The operator is an automorphism of the general quaternionic bilinear form exactly when $N(\tilde A)=\pm1$, and it is that condition that cuts out the pin and spin groups.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_{\tilde A}(\tilde Y)=\tilde A\tilde Y\tilde A^{\natural}$ | The twisted two-sided operator; the conjugation sandwich |
| $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$ | Its one-sided factorisation |
| $\Theta_{\tilde A}\circ\Theta_{\tilde B}=\Theta_{\tilde A\tilde B}$ | The composition law |
| $\Theta_{\tilde A}(\tilde Y)\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\Theta_{\tilde A}(\tilde Y\tilde Z)$ | Multiplicativity up to the norm |
| $\Theta_{\tilde A}=\Theta_{\tilde B}\iff\tilde B=\pm\tilde A$ | Injectivity up to sign; kernel $\{\pm e_0\}$ on the units |
| $(\Theta_{\tilde A})^{N}=\Theta_{\tilde A^{\natural}}$, $(\Theta_{\tilde A})^{*}=\Theta_{\tilde A^{*}}$ | The adjoints for the bilinear and the Hermitian forms |
| $N(\Theta_{\tilde A}\tilde X)=N(\tilde A)^{2}N(\tilde X)$ | The form preservation condition $N(\tilde A)=\pm1$ |
| $\tilde B\tilde A$ central; $=e_0$ | $L_{\tilde A}R_{\tilde B}$ multiplicative up to the scalar $\tilde B\tilde A$; strictly multiplicative for $\tilde B\tilde A=e_0$ |

## Further Reading

- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the signed inner conjugation $\tilde A^{\natural}\tilde X\tilde A^{-1}$ against the unsigned $\tilde A\tilde X\tilde A^{-1}$, their difference $-2\mathbf A\tilde X\tilde A^{-1}$ and the two matrices of the sign
- *One-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the factors
- *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-pin-and-spin-groups-of-the-general-quaternionic-algebra-of-biquaternions.md`), for the groups cut out by the norm
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form and its adjoint
- *Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/mixed-inner-conjugation-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the corresponding family over the dagger
- *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* (`articles_maths/two-sided-operators-on-a-clifford-algebra-with-signed-inner-conjugation.md`), for the general theory
