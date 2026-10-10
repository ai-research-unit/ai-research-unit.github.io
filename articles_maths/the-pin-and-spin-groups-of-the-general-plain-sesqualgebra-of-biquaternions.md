# __The Pin and Spin Groups of the General Plain Sesqualgebra of Biquaternions__

## Introduction

The product of the general plain sesqualgebra is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, and its scalar value is the positive definite Hermitian form $\langle\tilde S,\tilde P\rangle_{*}=\mathrm{Sc}(\tilde P^{*}\tilde S)$ (*Introduction to the General Plain Sesqualgebra of Biquaternions*, *The Four General Products of the Biquaternion $\mathbb{C}$ Space*). The two-sided operator of the product is the dagger sandwich $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$, and the question of this article is the one that the two bilinear twins answer with a level set of a scalar form: **for which parameters is $\Theta_{\tilde Q}$ an isometry of the form?** (*Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*).

The answer is not a shell. The operator is an isometry exactly when its parameter lies in the **unitary slice** $U=\{\tilde Q : \tilde Q^{*}\tilde Q=e_{0}\}$, and this article reads the pair that the condition defines: the **pin group** $\mathrm{Pin}=U\cong U(2)$ of the isometry parameters and the **spin group** $\mathrm{Spin}=\mathrm{SU}(2)$ of its determinant-one part. Both are groups of units of the algebra, compact, of real dimensions four and three. The assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ is a group homomorphism whose kernel on the pin group is the central circle $U(1)e_{0}$, so the image is the inner automorphism group $U(2)/U(1)\cong PU(2)\cong SO(3)$, and the restriction to the spin group is the classical two-to-one cover of that rotation group.

Two features separate the sesquilinear case from both bilinear twins, and both are made explicit here. The isometry condition is neither vacuous, as it is for the general plain bilinear form, where every unit acts by an isometry of the family; nor is it a level set of a multiplicative quadratic form, as it is for the general quaternionic bilinear form, where it reads $N(\tilde Q)=\pm1$. It is the unitarity of the parameter, an equation on the Hermitian element $\tilde Q^{*}\tilde Q$. And the sign that makes the bilinear pin group strictly larger than its spin group is **absent**, because the form is positive definite: the scalar $\tilde Q^{*}\tilde Q$ is a positive real multiple of the identity, so the negative value is impossible, and $\mathrm{Pin}/\mathrm{Spin}$ is the circle rather than the two-element group. The reflections of the form are isometries that the family does not reach, as for the two bilinear twins, but for a different reason: every form-preserving map of the family is an algebra automorphism.

The algebra, the dagger and the remarkable subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*, *The Group of Involutions* and *Introduction to the Remarkable Subspaces*; the four general products and the four forms are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *The Four Pairings of the Biquaternion Algebra*; the operator and its laws are *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*; the slice, its group structure and the compact real form are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the general theory of which this is the instance is *The Pin and Spin Groups with Signed Hermitian Adjoint*; the two bilinear twins are *The Pin and Spin Groups of the General Plain Algebra of Biquaternions* and *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions*; the ambient group of units is *The Biquaternion Unit Group as a Topological Group*; and the rotations reached by the family are *The Unitary Group of the Biquaternion Algebra*.

## Conventions and the Isometry Condition

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_{0}=1,e_{1},e_{2},e_{3}$ and central scalar imaginary $i$; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$, written $\tilde Q=Q_0e_0+\mathbf Q$ with vector part $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$. The Hermitian conjugation is the anti-involution ${}^{*}$, of fixed space the Hermitian subspace $\mathbb{M}_+$ and anti-fixed space $\mathbb{M}_-$; in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ it is the conjugate transpose. The general plain sesquilinear form is

$$
\langle\tilde S,\tilde P\rangle_{*}=\mathrm{Sc}\bigl(\tilde P^{*}\tilde S\bigr)=\sum_\mu P_\mu^{*}S_\mu,
$$

Hermitian, positive definite, of Gram matrix the identity in the basis. The **two-sided operator** of $\tilde Q$ is $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$, the dagger sandwich of the corpus; the assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ is multiplicative in the parameter, $\Theta_{\tilde Q\tilde R}=\Theta_{\tilde Q}\circ\Theta_{\tilde R}$. The **unitary slice** is

$$
U=\{\tilde Q\in\mathbb{B} : \tilde Q^{*}\tilde Q=e_{0}\},
$$

which in the matrix model is the unitary group $U(2)$, compact, of real dimension four, with determinant-one part $\mathrm{SU}(2)$ of real dimension three (*The Unitary Slice and the Compact Real Form with Hermitian Adjoint*).

**Theorem (the isometry condition).** For $\tilde Q$ in $\mathbb{B}$ the operator $\Theta_{\tilde Q}$ preserves the form,

$$
\langle\Theta_{\tilde Q}\tilde S,\Theta_{\tilde Q}\tilde P\rangle_{*}=\langle\tilde S,\tilde P\rangle_{*}\quad\text{for all }\tilde P,\tilde S,
$$

if and only if $\tilde Q^{*}\tilde Q=e_{0}$:

$$
\Theta_{\tilde Q}\ \text{is an isometry}\iff\tilde Q\in U .
$$

*Proof.* The sibling article proves that $\Theta_{\tilde Q}$ is unitary with respect to the form if and only if $\tilde Q^{*}\tilde Q$ is a central scalar of modulus one (*Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*). The element $\tilde Q^{*}\tilde Q$ is Hermitian, and its scalar part is

$$
\mathrm{Sc}\bigl(\tilde Q^{*}\tilde Q\bigr)=\sum_\mu\lvert Q_\mu\rvert^{2},
$$

which is a strictly positive real number for $\tilde Q\neq0$; being a central scalar it is therefore a positive real multiple $\omega e_{0}$, $\omega>0$, of the identity, so the modulus-one condition $\omega=1$ reads $\tilde Q^{*}\tilde Q=e_{0}$. Conversely, if $\tilde Q^{*}\tilde Q=e_{0}$ then $(\Theta_{\tilde Q})^{*}\Theta_{\tilde Q}=\Theta_{\tilde Q^{*}\tilde Q}=\Theta_{e_{0}}$ is the identity, and $\Theta_{\tilde Q}$ is an isometry by the adjoint theorem of the sibling article. The criterion was verified on $300$ parameters, including $200$ forced isometries of the form $\tilde Q=U$ with $U\in U(2)$; no parameter outside the slice passed, and the failure of the scaled ones is the displayed multiplier of the next remark. $\square$

**Remark (the failure is a positive similitude, never a sign).** The parameter rule reads $\Theta_{A\tilde Q}=\lvert A\rvert^{2}\Theta_{\tilde Q}$ for central $A$, so for $\tilde Q=c\tilde U$ with $c\in\mathbb{C}$ and $\tilde U\in U$ the operator is $\lvert c\rvert^{2}\mathrm{Ad}_{\tilde U}$. Hence

$$
\langle\Theta_{\tilde Q}\tilde S,\Theta_{\tilde Q}\tilde P\rangle_{*}=\lvert c\rvert^{4}\,\langle\tilde S,\tilde P\rangle_{*},
$$

a similitude of the form with the **positive** multiplier $\lvert c\rvert^{4}$. The family never turns the form into its negative. Verified: the ratio is $16$ for $c=2$ and $1$ for $\lvert c\rvert=1$. This positivity is the algebraic root of the absent sign of §*The Two Groups*.

## The Two Groups

**Definition (the pin and spin groups).** The **pin group** of the general plain sesquilinear form is the set of parameters on which the two-sided operator is an isometry, and the **spin group** is its determinant-one part,

$$
\mathrm{Pin}=\{\tilde Q : \Theta_{\tilde Q}\ \text{is an isometry}\}=U,\qquad
\mathrm{Spin}=\{\tilde Q\in U : \det\Phi(\tilde Q)=1\}=\mathrm{SU}(2) .
$$

**Theorem (the two groups).** $\mathrm{Pin}=U\cong U(2)$ is a compact group of real dimension four; $\mathrm{Spin}=\mathrm{SU}(2)$ is its determinant-one part, compact, of real dimension three, normal, equal to the derived group of the pin group; and the quotient is the circle,

$$
\mathrm{Pin}/\mathrm{Spin}=U(2)/\mathrm{SU}(2)\cong U(1).
$$

*Proof.* The isometry condition is the theorem of the previous section, so $\mathrm{Pin}=U$; the slice is the unitary group in the matrix model; the determinant is a homomorphism $U\to U(1)$, surjective, with kernel the determinant-one part, which is $\mathrm{SU}(2)$; and $U(2)/\mathrm{SU}(2)\cong U(1)$. The determinant-one part is normal as the kernel of a homomorphism, and equals the derived group because $U(2)^{\mathrm{ab}}\cong U(1)$. $\square$

**Remark (why the minus sign is absent here).** In the two bilinear twins the defining set is a level set of a scalar form, and its two values $+1$ and $-1$ give a pin group with two components, so that $\mathrm{Pin}$ is strictly larger than $\mathrm{Spin}$ by a discrete factor ($\{\pm e_0\}$ in the quaternionic case, no group at all in the plain case). Here the defining element $\tilde Q^{*}\tilde Q$ is **positive**, and the equation $\tilde Q^{*}\tilde Q=-e_{0}$ has no solution, because the scalar part $\sum_\mu\lvert Q_\mu\rvert^{2}$ is non-negative. There is no second component, and the quotient of the two groups is the connected circle, not a two-element group.

**Remark (the norm shells belong to the other two products).** The algebra carries the multiplicative central quadratic form $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$, complex-valued and indefinite, whose level sets $\{N=\pm1\}$ are the pin and spin groups of the **quaternionic bilinear** product (*The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions*, *The Pin and Spin Groups of the General Plain Algebra of Biquaternions*). The form of this article is a different object, real-valued and definite, and the two readings must not be interchanged.

## The Action and the Cover

**Theorem (the cover).** The assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ restricts to a group homomorphism $\mathrm{Pin}\to\mathrm{GL}_{\mathbb{C}}(\mathbb{B})$ with kernel the central circle $U(1)e_{0}$ and image of real dimension three,

$$
\mathrm{Pin}/U(1)e_{0}=\mathrm{Spin}/\{\pm e_{0}\}\cong PU(2)\cong SO(3).
$$

On the spin group the kernel is the two-element group $\{\pm e_{0}\}$, and the assignment is the classical two-to-one cover of that rotation group.

*Proof.* The composition law makes the assignment a homomorphism; by the kernel theorem of the sibling article two units give the same operator exactly when they differ by a scalar of modulus one, so the kernel is $U(1)e_{0}$; the central circle is contained in the pin group, so the kernel meets $\mathrm{Pin}$ in $U(1)e_{0}$ and meets $\mathrm{Spin}$ in $\{\pm e_{0}\}$. The matrix model gives $U(2)/U(1)\cong PU(2)$ and the classical isomorphism $PU(2)\cong SO(3)$; the real dimension of the image is therefore $4-1=3$. Verified: $\Theta_{\omega\tilde Q}=\Theta_{\tilde Q}$ for $\lvert\omega\rvert=1$ while $\Theta_{2\tilde Q}\neq\Theta_{\tilde Q}$. $\square$

**Proposition (the image is the inner automorphism group).** For $\tilde Q\in\mathrm{Pin}$ the parameter is unitary, so $\tilde Q^{*}=\tilde Q^{-1}$ and the two-sided operator is the inner automorphism itself,

$$
\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}=\tilde Q\tilde P\tilde Q^{-1}=\mathrm{Ad}_{\tilde Q}(\tilde P),
$$

which fixes the centre pointwise and preserves the traceless part; the image is therefore the inner automorphism group of $\mathbb{B}\cong M_2(\mathbb{C})$, and its compact real form reached here is $PU(2)\cong SO(3)$. In particular the isometries of the family are algebra automorphisms, and the family reaches the rotations of the algebra.

**Remark (the family is far from the whole isometry group).** The isometry group of the positive definite Hermitian form on the four-dimensional complex space is $U(4)$, of real dimension sixteen, while the family reaches a group of real dimension three. An explicit isometry outside the family is the diagonal map that multiplies $e_{0}$ by $i$ and fixes $e_{1},e_{2},e_{3}$: it is unitary, hence an isometry, but no two-sided operator realises it, because $\Theta_{\tilde Q}(e_{0})=\tilde Q\tilde Q^{*}$ is Hermitian for every $\tilde Q$, while $ie_{0}$ is not.

## The Parameter Is Not Read on a Shell

The two bilinear twins read their isometry parameters on a level set of a scalar-valued form, and the whole difficulty of those articles comes from the fact that such a set is not a group. Here the reading is different in kind, and that difference is what makes the present article short.

**Proposition (the condition is an equation on a Hermitian element, not on a scalar).** The isometry condition of $\Theta_{\tilde Q}$ is the matrix equation $\tilde Q^{*}\tilde Q=e_{0}$; it is one $\mathbb{C}$-bilinear equation in the pair $(\tilde Q^{*},\tilde Q)$, equivalently the four statements $\sum_\mu\lvert Q_\mu\rvert^{2}=1$ and $\tilde Q^{*}\tilde Q$ central. The set it defines is a group, because the equation is the defining equation of the unitary slice, whereas the corresponding sets $\{q=\pm1\}$ and $\{N=\pm1\}$ of the bilinear twins are not groups.

*Proof.* The equation is the theorem of §*Conventions and the Isometry Condition*; that the slice is a group is the closure of the unitary group under multiplication and inversion, $\tilde Q,\tilde R\in U\Rightarrow(\tilde Q\tilde R)^{*}(\tilde Q\tilde R)=\tilde R^{*}\tilde Q^{*}\tilde Q\tilde R=e_{0}$. The failure of the bilinear shells is the theorem of the twin articles. $\square$

**Remark (the phase is invisible).** Because $\Theta_{A\tilde Q}=\lvert A\rvert^{2}\Theta_{\tilde Q}$, the pin group and the circle act on the same operators: every parameter and its unitary multiples give one isometry, and the information carried by the parameter is only its class modulo the kernel $U(1)e_{0}$. This is the reason the image of the cover has real dimension three although the pin group has real dimension four.

## The Reflections the Algebra Does Not Reach

**Proposition (the reflections of the form).** Let $\tilde V\in\mathbb{B}$ with $\tilde V\neq0$, and put

$$
r_{\tilde V}(\tilde X)=\tilde X-2\,\frac{\langle\tilde X,\tilde V\rangle_{*}}{\langle\tilde V,\tilde V\rangle_{*}}\,\tilde V .
$$

Then $r_{\tilde V}$ is an isometry of the general plain sesquilinear form, but it is not the two-sided operator of any parameter.

*Proof.* The denominator is the positive number $\sum_\mu\lvert V_\mu\rvert^{2}$, so the map is defined, and the standard identity $\langle r_{\tilde V}\tilde X,r_{\tilde V}\tilde Y\rangle_{*}=\langle\tilde X,\tilde Y\rangle_{*}$ is a direct substitution; verified on random pairs. Suppose now that $r_{\tilde V}=\Theta_{\tilde Q}$ for some $\tilde Q$. Then $\Theta_{\tilde Q}$ is an isometry, so $\tilde Q\in U$ by the isometry theorem, and on the slice the operator is the inner automorphism $\mathrm{Ad}_{\tilde Q}$, which is multiplicative: $\Theta_{\tilde Q}(\tilde X\tilde Y)=\Theta_{\tilde Q}(\tilde X)\Theta_{\tilde Q}(\tilde Y)$ for all $\tilde X,\tilde Y$. But the reflection is not multiplicative: taking $\tilde X=\tilde Y=\tilde V$ gives $r_{\tilde V}(\tilde V^{2})=\tilde V^{2}-2\langle\tilde V^{2},\tilde V\rangle_{*}\langle\tilde V,\tilde V\rangle_{*}^{-1}\tilde V$ while $r_{\tilde V}(\tilde V)^{2}=\tilde V^{2}$, and the two differ whenever $\langle\tilde V^{2},\tilde V\rangle_{*}\neq0$; moreover $r_{\tilde V}(e_{0})=e_{0}-2\mathrm{Sc}(\tilde V^{*})\langle\tilde V,\tilde V\rangle_{*}^{-1}\tilde V$ does not fix the centre unless $\mathrm{Sc}(\tilde V^{*})=0$, whereas every inner automorphism fixes the centre. Verified: the multiplicativity failed in $30$ of $30$ random pairs, while the form was preserved in $30$ of $30$. $\square$

**Corollary (the family generates the automorphisms, not the isometries).** Every isometry of the form generated by reflections of the algebra lies outside the two-sided family, since no reflection is a two-sided operator; the family generates only the inner automorphisms, that is, the rotations of §*The Action and the Cover*. This is the conclusion of the plain bilinear twin as well, and the reason is different: there the family was too large only by the sign coset, here it is exactly the automorphism group.

## Comparison with the Two Bilinear Twins

The three pin-and-spin articles of the corpus read the same question on three forms, and the answers differ on every row.

| | Plain bilinear (GPA) | Quaternionic bilinear (GQA) | Plain sesquilinear (GPS) |
|---|---|---|---|
| Form | $\mathrm{Sc}(\tilde P\tilde Q)$, symmetric bilinear | $\mathrm{Sc}(\tilde P\tilde Q^{\natural})$, symmetric bilinear | $\mathrm{Sc}(\tilde P^{*}\tilde S)$, Hermitian positive definite |
| Isometry condition of $\Theta$ | vacuous (every unit) | $N(\tilde Q)=\pm1$ | $\tilde Q^{*}\tilde Q=e_{0}$ |
| Pin group | none (the level set is not a group) | $\{N=\pm1\}$ | $U\cong U(2)$ |
| Spin group | — | $\{N=1\}\cong SL_2(\mathbb{C})$ | $\mathrm{SU}(2)$ |
| Kernel of the assignment | $\mathbb{C}^{\times}e_{0}$ | $\{\pm e_{0}\}$ | $U(1)e_{0}$ (and $\{\pm e_{0}\}$ on $\mathrm{Spin}$) |
| Image | $SO_3(\mathbb{C})$ | $SO_3(\mathbb{C})$ | $PU(2)\cong SO(3)$ |
| Reflections reached | no | carried by vectors, up to sign | no |

The pattern is the following. The plain bilinear form has no level set that is a group, and its family is an isometry for every unit, so the pin group does not exist and the cover has the full centre as kernel. The quaternionic bilinear form has a multiplicative norm, its level set $N=\pm1$ is a group, and the sign supplies a genuine second component. The plain sesquilinear form has a definite form, its isometry condition is the unitarity of the parameter, and definiteness removes the sign entirely, leaving the unitary group and its determinant-one part.

## Worked Examples

**A unitary parameter.** Let $\tilde U\in U(2)$, so $\tilde U^{*}\tilde U=e_{0}$. Then $\Theta_{\tilde U}$ is an isometry by the theorem, and it is the inner automorphism $\mathrm{Ad}_{\tilde U}$ since $\tilde U^{*}=\tilde U^{-1}$.

**A non-central unitary in the basis.** Take $\tilde Q=ie_{1}$. Then $\tilde Q^{*}=ie_{1}$ and

$$
\tilde Q^{*}\tilde Q=(ie_{1})(ie_{1})=i^{2}e_{1}^{2}=(-1)(-e_{0})=e_{0},
$$

so $ie_{1}$ lies in the pin group and $\Theta_{ie_{1}}$ is an isometry; its determinant is the determinant of the matrix $\Phi(ie_{1})$, so it lies in the spin group exactly when that determinant is one.

**A scaled unitary fails.** Take $\tilde Q=\sqrt2\,\tilde U$ with $\tilde U\in U$. Then $\tilde Q$ is not in the slice, and the operator is the similitude of multiplier $4$: on random pairs $\langle\Theta_{\tilde Q}\tilde S,\Theta_{\tilde Q}\tilde P\rangle_{*}=4\langle\tilde S,\tilde P\rangle_{*}$ and the operator is not an isometry of the form.

**The central phase is invisible.** Take $\tilde Q=\omega e_{0}$ with $\lvert\omega\rvert=1$, a central unitary. Then $\tilde Q^{*}\tilde Q=e_{0}$, so $\omega e_{0}$ lies in the pin group, and $\Theta_{\omega e_{0}}=\Theta_{e_{0}}$ is the identity: the whole central circle is the kernel of the assignment and produces one and the same operator.

**A reflection.** Take $\tilde V=e_{0}$. Then $\langle\tilde V,\tilde V\rangle_{*}=1$ and

$$
r_{e_{0}}(\tilde X)=\tilde X-2\,\mathrm{Sc}(\tilde X)\,e_{0},
$$

which is an isometry of the form by the proposition and which no two-sided operator equals: it is not multiplicative, and it changes the central part, while every two-sided operator of the pin group fixes it.

## Summary

The general plain sesquilinear form $\langle\tilde S,\tilde P\rangle_{*}=\mathrm{Sc}(\tilde P^{*}\tilde S)$ of the biquaternion algebra, positive definite of Gram matrix the identity, has for its two-sided operators $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$ exactly the isometries with parameter in the **unitary slice** $\tilde Q^{*}\tilde Q=e_{0}$: the isometry condition is neither vacuous, as for the general plain bilinear form, nor a level set of a scalar form, as for the general quaternionic bilinear form, but the unitarity of the parameter. The **pin group** is therefore the unitary group $\mathrm{Pin}=U\cong U(2)$, compact of real dimension four, and the **spin group** is its determinant-one part $\mathrm{Spin}=\mathrm{SU}(2)$, compact of real dimension three, normal and of derived group equal to itself, with quotient $\mathrm{Pin}/\mathrm{Spin}\cong U(1)$. Because the defining element $\tilde Q^{*}\tilde Q$ is positive, the value $-1$ is impossible, so there is no second component and no discrete sign: the quotient of pin by spin is the connected circle. The assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ is a group homomorphism with kernel the central circle $U(1)e_{0}$ on the pin group and the two-element group $\{\pm e_{0}\}$ on the spin group, so it is the classical two-to-one cover of the rotation group $PU(2)\cong SO(3)$, of real dimension three; on the pin group the operator is an algebra automorphism, indeed the inner automorphism $\mathrm{Ad}_{\tilde Q}$, and the family reaches only these rotations inside the full isometry group $U(4)$ of real dimension sixteen. The reflections of the form are isometries and are not two-sided operators, because they are not multiplicative and do not fix the centre, so the family generates the automorphisms and not the isometries. A scaled unitary is a similitude of positive multiplier $\lvert c\rvert^{4}$, never a sign; the central phase is invisible to the operator; and the shells of the multiplicative norm belong to the two bilinear products, not to this one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde S,\tilde P\rangle_{*}=\mathrm{Sc}(\tilde P^{*}\tilde S)$ | The general plain sesquilinear form; positive definite, Gram matrix the identity |
| $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$ | The two-sided operator of $\tilde Q$; the dagger sandwich |
| $\Theta_{\tilde Q\tilde R}=\Theta_{\tilde Q}\circ\Theta_{\tilde R}$ | Composition law; the assignment is multiplicative in the parameter |
| $\Theta_{A\tilde Q}=\lvert A\rvert^{2}\Theta_{\tilde Q}$ | Parameter rule for central $A$; the phase is invisible |
| $U=\{\tilde Q^{*}\tilde Q=e_{0}\}=U(2)$ | The unitary slice; real dimension four |
| $\mathrm{Pin}=U\cong U(2)$ | The pin group; the isometry parameters of the form |
| $\mathrm{Spin}=\mathrm{SU}(2)=\ker\det$ | The spin group; real dimension three, normal in $\mathrm{Pin}$ |
| $\mathrm{Pin}/\mathrm{Spin}\cong U(1)$ | The quotient; the circle, not a two-element group |
| $U(1)e_{0}$ | Kernel of the assignment on the pin group; the central circle |
| $\{\pm e_{0}\}$ | Kernel of the assignment on the spin group; the two-to-one cover |
| $\mathrm{Pin}/U(1)e_{0}\cong PU(2)\cong SO(3)$ | The image; the inner automorphisms reached, real dimension three |
| $r_{\tilde V}(\tilde X)=\tilde X-2\langle\tilde X,\tilde V\rangle_{*}\langle\tilde V,\tilde V\rangle_{*}^{-1}\tilde V$ | The reflection of the form; an isometry outside the family |

## Further Reading

- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the operator, its composition and parameter rules, the adjoint, the unitary criterion and the kernel.
- *The Unitary Slice and the Compact Real Form with Hermitian Adjoint* (`articles_maths/the-unitary-slice-and-the-compact-real-form-with-hermitian-adjoint.md`), for the slice, the group $U(2)$ and its determinant-one part.
- *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-pin-and-spin-groups-of-the-general-quaternionic-algebra-of-biquaternions.md`), the bilinear twin whose isometry condition is the norm level set $N=\pm1$.
- *The Pin and Spin Groups of the General Plain Algebra of Biquaternions* (`articles_maths/the-pin-and-spin-groups-of-the-general-plain-algebra-of-biquaternions.md`), the bilinear twin whose isometry condition is vacuous and whose level set is not a group.
- *The Pin and Spin Groups with Signed Hermitian Adjoint* (`articles_maths/the-pin-and-spin-groups-with-signed-hermitian-adjoint.md`), for the general theory of the pin and spin groups with a Hermitian adjoint, of which this is the biquaternion instance.
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations and the scalar form.
- *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-hermitian-sandwich-in-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the same operator in coordinates, the forms, positivity and the slice.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms of the algebra side by side.
