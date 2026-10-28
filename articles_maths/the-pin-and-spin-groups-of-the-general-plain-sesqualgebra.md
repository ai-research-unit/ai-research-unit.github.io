# __The Pin and Spin Groups of the General Plain Sesqualgebra__

## Introduction

The product of the general plain sesqualgebra is $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$, and its scalar value is the positive definite Hermitian form $\langle\tilde S,\tilde Q_1\rangle_{*}=\mathrm{Sc}(\tilde Q_1^{*}\tilde S)$ (*Introduction to the General Plain Sesqualgebra*, *The Four General Products and Their Relations over the Biquaternion Algebra*). The two-sided operator of the product is the dagger sandwich $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$, and the question of this article is the one that the two bilinear twins answer with a level set of a scalar form: **for which parameters is $\Theta_{\tilde Q}$ an isometry of the form?** (*Two-Sided Operators on the General Plain Sesqualgebra*).

The answer is not a shell. The operator is an isometry exactly when its parameter lies in the **$*$-unitary slice** $U=\{\tilde Q : \tilde Q^{*}\tilde Q=e_{t}\}$, and this article reads the pair that the condition defines: the **pin group** $\mathrm{Pin}=U\cong \mathrm{U}(2)$ of the isometry parameters and the **spin group** $\mathrm{Spin}=\mathrm{SU}(2)$ of its determinant-one part. Both are groups of units of the algebra, compact, of real dimensions four and three. The assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ is a group homomorphism whose kernel on the pin group is the central circle $\mathrm{U}(1)e_{t}$, so the image is the inner automorphism group $\mathrm{U}(2)/\mathrm{U}(1)\cong PU(2)\cong SO(3)$, and the restriction to the spin group is the classical two-to-one cover of that rotation group.

Two features separate the sesquilinear case from both bilinear twins, and both are made explicit here. The isometry condition is neither vacuous, as it is for the general plain bilinear form, where every unit acts by an isometry of the family; nor is it a level set of a multiplicative quadratic form, as it is for the general quaternionic bilinear form, where it reads $\langle\tilde Q\rangle_{\natural}=\pm1$. It is the unitarity of the parameter, an equation on the Hermitian element $\tilde Q^{*}\tilde Q$. And the sign that makes the bilinear pin group strictly larger than its spin group is **absent**, because the form is positive definite: the scalar $\tilde Q^{*}\tilde Q$ is a positive real multiple of the identity, so the negative value is impossible, and $\mathrm{Pin}/\mathrm{Spin}$ is the circle rather than the two-element group. The reflections of the form are isometries that the family does not reach, as for the two bilinear twins, but for a different reason: every form-preserving map of the family is an algebra automorphism.

The algebra, the dagger and the remarkable subspaces are *The Biquaternion Algebra*, *The Group of Involutions* and *The Six Subspaces*; the four general products and the four forms are *The Four General Products and Their Relations over the Biquaternion Algebra* and *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the operator and its laws are *Two-Sided Operators on the General Plain Sesqualgebra*; the slice, its group structure and the compact real form are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the general theory of which this is the instance is *The Pin and Spin Groups with Signed Hermitian Adjoint*; the two bilinear twins are *Two-Sided Operators on the Biquaternion Algebra*, §*The Isometry Group and the Absence of a Pin Group*, and *The Pin and Spin Groups of the General Quaternionic Algebra*; the ambient group of units is *The Biquaternion Unit Group as a Topological Group*; and the rotations reached by the family are *The Unitary Group of the Biquaternion Algebra*.

## Conventions and the Isometry Condition

$$
\langle\tilde S,\tilde Q_1\rangle_{*}=\mathrm{Sc}\bigl(\tilde Q_1^{*}\tilde S\bigr)=\sum_\mu Q_{1\mu}^{*}S_\mu,
$$

Hermitian, positive definite, of Gram matrix the identity in the basis. The **two-sided operator** of $\tilde Q$ is $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$, the dagger sandwich of the corpus; the assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ is multiplicative in the parameter, $\Theta_{\tilde Q\tilde{Q}_3}=\Theta_{\tilde Q}\circ\Theta_{\tilde{Q}_3}$. The **$*$-unitary slice** is

$$
U=\{\tilde Q\in\mathbb{B} : \tilde Q^{*}\tilde Q=e_{t}\},
$$

which in the matrix model is the $*$-unitary group $\mathrm{U}(2)$, compact, of real dimension four, with determinant-one part $\mathrm{SU}(2)$ of real dimension three (*The Unitary Slice and the Compact Real Form with Hermitian Adjoint*).

**Theorem (the isometry condition).** For $\tilde Q$ in $\mathbb{B}$ the operator $\Theta_{\tilde Q}$ preserves the form,

$$
\boxed{\; \langle\Theta_{\tilde Q}\tilde S,\Theta_{\tilde Q}\tilde Q_1\rangle_{*}=\langle\tilde S,\tilde Q_1\rangle_{*}\quad\text{for all }\tilde Q_1,\tilde S \;},
$$

if and only if $\tilde Q^{*}\tilde Q=e_{t}$:

$$
\Theta_{\tilde Q}\ \text{is an isometry}\iff\tilde Q\in U .
$$

*Proof.* The sibling article proves that $\Theta_{\tilde Q}$ is $*$-unitary with respect to the form if and only if $\tilde Q^{*}\tilde Q$ is a central scalar of modulus one (*Two-Sided Operators on the General Plain Sesqualgebra*). The element $\tilde Q^{*}\tilde Q$ is Hermitian, and its scalar part is

$$
\mathrm{Sc}\bigl(\tilde Q^{*}\tilde Q\bigr)=\sum_\mu\lvert Q_\mu\rvert^{2},
$$

which is a strictly positive real number for $\tilde Q\neq0$; being a central scalar it is therefore a positive real multiple $\omega e_{t}$, $\omega>0$, of the identity, so the modulus-one condition $\omega=1$ reads $\tilde Q^{*}\tilde Q=e_{t}$. Conversely, if $\tilde Q^{*}\tilde Q=e_{t}$ then $(\Theta_{\tilde Q})^{*}\Theta_{\tilde Q}=\Theta_{\tilde Q^{*}\tilde Q}=\Theta_{e_{t}}$ is the identity, and $\Theta_{\tilde Q}$ is an isometry by the adjoint theorem of the sibling article.

**Remark (the failure is a positive similitude, never a sign).** The parameter rule reads $\Theta_{A\tilde Q}=\lvert A\rvert^{2}\Theta_{\tilde Q}$ for central $A$, so for $\tilde Q=c\tilde Q$ with $c\in\mathbb{C}$ and $\tilde Q\in U$ the operator is $\lvert c\rvert^{2}\mathrm{Ad}_{\tilde Q}$. Hence

$$
\langle\Theta_{\tilde Q}\tilde S,\Theta_{\tilde Q}\tilde Q_1\rangle_{*}=\lvert c\rvert^{4}\,\langle\tilde S,\tilde Q_1\rangle_{*},
$$

a similitude of the form with the **positive** multiplier $\lvert c\rvert^{4}$. The family never turns the form into its negative. This positivity is the algebraic root of the absent sign of §*The Two Groups*.

## The Two Groups

**Definition (the pin and spin groups).** The **pin group** of the general plain sesquilinear form is the set of parameters on which the two-sided operator is an isometry, and the **spin group** is its determinant-one part,

$$
\mathrm{Pin}=\{\tilde Q : \Theta_{\tilde Q}\ \text{is an isometry}\}=U,\qquad
\mathrm{Spin}=\{\tilde Q\in U : \det\mathsf{M}_2(\tilde Q)=1\}=\mathrm{SU}(2) .
$$

**Theorem (the two groups).** $\mathrm{Pin}=U\cong \mathrm{U}(2)$ is a compact group of real dimension four; $\mathrm{Spin}=\mathrm{SU}(2)$ is its determinant-one part, compact, of real dimension three, normal, equal to the derived group of the pin group; and the quotient is the circle,

$$
\boxed{\; \mathrm{Pin}/\mathrm{Spin}=\mathrm{U}(2)/\mathrm{SU}(2)\cong \mathrm{U}(1) \;}.
$$

*Proof.* The isometry condition is the theorem of the previous section, so $\mathrm{Pin}=U$; the slice is the $*$-unitary group in the matrix model; the determinant is a homomorphism $U\to \mathrm{U}(1)$, surjective, with kernel the determinant-one part, which is $\mathrm{SU}(2)$; and $\mathrm{U}(2)/\mathrm{SU}(2)\cong \mathrm{U}(1)$. The determinant-one part is normal as the kernel of a homomorphism, and equals the derived group because $\mathrm{U}(2)^{\mathrm{ab}}\cong \mathrm{U}(1)$.

**Remark (why the minus sign is absent here).** In the two bilinear twins the defining set is a level set of a scalar form, and its two values $+1$ and $-1$ give a pin group with two components, so that $\mathrm{Pin}$ is strictly larger than $\mathrm{Spin}$ by a discrete factor ($\{\pm e_t\}$ in the quaternionic case, no group at all in the plain case). Here the defining element $\tilde Q^{*}\tilde Q$ is **positive**, and the equation $\tilde Q^{*}\tilde Q=-e_{t}$ has no solution, because the scalar part $\sum_\mu\lvert Q_\mu\rvert^{2}$ is non-negative. There is no second component, and the quotient of the two groups is the connected circle, not a two-element group.

**Remark (the norm shells belong to the other two products).** The algebra carries the multiplicative central quadratic form $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$, complex-valued and indefinite, whose level sets $\{N=\pm1\}$ are the pin and spin groups of the **quaternionic bilinear** product (*The Pin and Spin Groups of the General Quaternionic Algebra*). The form of this article is a different object, real-valued and definite, and the two readings must not be interchanged.

## The Action and the Cover

**Theorem (the cover).** The assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ restricts to a group homomorphism $\mathrm{Pin}\to\mathrm{GL}_{\mathbb{C}}(\mathbb{B})$ with kernel the central circle $\mathrm{U}(1)e_{t}$ and image of real dimension three,

$$
\boxed{\; \mathrm{Pin}/\mathrm{U}(1)e_{t}=\mathrm{Spin}/\{\pm e_{t}\}\cong PU(2)\cong SO(3) \;}.
$$

On the spin group the kernel is the two-element group $\{\pm e_{t}\}$, and the assignment is the classical two-to-one cover of that rotation group.

*Proof.* The composition law makes the assignment a homomorphism; by the kernel theorem of the sibling article two units give the same operator exactly when they differ by a scalar of modulus one, so the kernel is $\mathrm{U}(1)e_{t}$; the central circle is contained in the pin group, so the kernel meets $\mathrm{Pin}$ in $\mathrm{U}(1)e_{t}$ and meets $\mathrm{Spin}$ in $\{\pm e_{t}\}$. The matrix model gives $\mathrm{U}(2)/\mathrm{U}(1)\cong PU(2)$ and the classical isomorphism $PU(2)\cong SO(3)$; the real dimension of the image is therefore $4-1=3$.

**Proposition (the image is the inner automorphism group).** For $\tilde Q\in\mathrm{Pin}$ the parameter is $*$-unitary, so $\tilde Q^{*}=\tilde Q^{-1}$ and the two-sided operator is the inner automorphism itself,

$$
\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}=\tilde Q\tilde Q_1\tilde Q^{-1}=\mathrm{Ad}_{\tilde Q}(\tilde Q_1),
$$

which fixes the centre pointwise and preserves the traceless part; the image is therefore the inner automorphism group of $\mathbb{B}\cong M_2(\mathbb{C})$, and its compact real form reached here is $PU(2)\cong SO(3)$. In particular the isometries of the family are algebra automorphisms, and the family reaches the rotations of the algebra.

**Remark (the family is far from the whole isometry group).** The isometry group of the positive definite Hermitian form on the four-dimensional complex space is $\mathrm{U}(4)$, of real dimension sixteen, while the family reaches a group of real dimension three. An explicit isometry outside the family is the diagonal map that multiplies $e_{t}$ by $i$ and fixes $\vec e_x,\vec e_y,\vec e_z$: it is $*$-unitary, hence an isometry, but no two-sided operator realises it, because $\Theta_{\tilde Q}(e_{t})=\tilde Q\tilde Q^{*}$ is Hermitian for every $\tilde Q$, while $ie_{t}$ is not.

## The Parameter Is Not Read on a Shell

The two bilinear twins read their isometry parameters on a level set of a scalar-valued form, and the whole difficulty of those articles comes from the fact that such a set is not a group. Here the reading is different in kind, and that difference is what makes the present article short.

**Proposition (the condition is an equation on a Hermitian element, not on a scalar).** The isometry condition of $\Theta_{\tilde Q}$ is the matrix equation $\tilde Q^{*}\tilde Q=e_{t}$; it is one $\mathbb{C}$-bilinear equation in the pair $(\tilde Q^{*},\tilde Q)$, equivalently the four statements $\sum_\mu\lvert Q_\mu\rvert^{2}=1$ and $\tilde Q^{*}\tilde Q$ central. The set it defines is a group, because the equation is the defining equation of the $*$-unitary slice, whereas the corresponding sets $\{q=\pm1\}$ and $\{N=\pm1\}$ of the bilinear twins are not groups.

*Proof.* The equation is the theorem of §*Conventions and the Isometry Condition*; that the slice is a group is the closure of the $*$-unitary group under multiplication and inversion, $\tilde Q,\tilde{Q}_3\in U\Rightarrow(\tilde Q\tilde{Q}_3)^{*}(\tilde Q\tilde{Q}_3)=\tilde{Q}_3^{*}\tilde Q^{*}\tilde Q\tilde{Q}_3=e_{t}$. The failure of the bilinear shells is the theorem of the twin articles.

**Remark (the phase is invisible).** Because $\Theta_{A\tilde Q}=\lvert A\rvert^{2}\Theta_{\tilde Q}$, the pin group and the circle act on the same operators: every parameter and its $*$-unitary multiples give one isometry, and the information carried by the parameter is only its class modulo the kernel $\mathrm{U}(1)e_{t}$. This is the reason the image of the cover has real dimension three although the pin group has real dimension four.

## The Reflections the Algebra Does Not Reach

**Proposition (the reflections of the form).** Let $\tilde Q_3\in\mathbb{B}$ with $\tilde Q_3\neq0$, and put

$$
r_{\tilde Q_3}(\tilde Q_1)=\tilde Q_1-2\,\frac{\langle\tilde Q_1,\tilde Q_3\rangle_{*}}{\langle\tilde Q_3,\tilde Q_3\rangle_{*}}\,\tilde Q_3 .
$$

Then $r_{\tilde Q_3}$ is an isometry of the general plain sesquilinear form, but it is not the two-sided operator of any parameter.

*Proof.* The denominator is the positive number $\sum_\mu\lvert V_\mu\rvert^{2}$, so the map is defined, and the standard identity $\langle r_{\tilde Q_3}\tilde Q_1,r_{\tilde Q_3}\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ is a direct substitution; verified on random pairs. Suppose now that $r_{\tilde Q_3}=\Theta_{\tilde Q}$ for some $\tilde Q$. Then $\Theta_{\tilde Q}$ is an isometry, so $\tilde Q\in U$ by the isometry theorem, and on the slice the operator is the inner automorphism $\mathrm{Ad}_{\tilde Q}$, which is multiplicative: $\Theta_{\tilde Q}(\tilde Q_1\tilde Q_2)=\Theta_{\tilde Q}(\tilde Q_1)\Theta_{\tilde Q}(\tilde Q_2)$ for all $\tilde Q_1,\tilde Q_2$. But the reflection is not multiplicative: taking $\tilde Q_1=\tilde Q_2=\tilde Q_3$ gives $r_{\tilde Q_3}(\tilde Q_3^{2})=\tilde Q_3^{2}-2\langle\tilde Q_3^{2},\tilde Q_3\rangle_{*}\langle\tilde Q_3,\tilde Q_3\rangle_{*}^{-1}\tilde Q_3$ while $r_{\tilde Q_3}(\tilde Q_3)^{2}=\tilde Q_3^{2}$, and the two differ whenever $\langle\tilde Q_3^{2},\tilde Q_3\rangle_{*}\neq0$; moreover $r_{\tilde Q_3}(e_{t})=e_{t}-2\mathrm{Sc}(\tilde Q_3^{*})\langle\tilde Q_3,\tilde Q_3\rangle_{*}^{-1}\tilde Q_3$ does not fix the centre unless $\mathrm{Sc}(\tilde Q_3^{*})=0$, whereas every inner automorphism fixes the centre.

**Corollary (the family generates the automorphisms, not the isometries).** Every isometry of the form generated by reflections of the algebra lies outside the two-sided family, since no reflection is a two-sided operator; the family generates only the inner automorphisms, that is, the rotations of §*The Action and the Cover*. This is the conclusion of the plain bilinear twin as well, and the reason is different: there the family was too large only by the sign coset, here it is exactly the automorphism group.

## Comparison with the Two Bilinear Twins

The three pin-and-spin articles of the corpus read the same question on three forms, and the answers differ on every row.

| | Plain bilinear (GPA) | Quaternionic bilinear (GQA) | Plain sesquilinear (GPS) |
|---|---|---|---|
| Form | $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, symmetric bilinear | $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$, symmetric bilinear | $\mathrm{Sc}(\tilde Q_1^{*}\tilde S)$, Hermitian positive definite |
| Isometry condition of $\Theta$ | vacuous (every unit) | $\langle\tilde Q\rangle_{\natural}=\pm1$ | $\tilde Q^{*}\tilde Q=e_{t}$ |
| Pin group | none (the level set is not a group) | $\{N=\pm1\}$ | $U\cong \mathrm{U}(2)$ |
| Spin group | — | $\{N=1\}\cong SL_2(\mathbb{C})$ | $\mathrm{SU}(2)$ |
| Kernel of the assignment | $\mathbb{C}^{\times}e_{t}$ | $\{\pm e_{t}\}$ | $\mathrm{U}(1)e_{t}$ (and $\{\pm e_{t}\}$ on $\mathrm{Spin}$) |
| Image | $SO_3(\mathbb{C})$ | $SO_3(\mathbb{C})$ | $PU(2)\cong SO(3)$ |
| Reflections reached | no | carried by vectors, up to sign | no |

The pattern is the following. The plain bilinear form has no level set that is a group, and its family is an isometry for every unit, so the pin group does not exist and the cover has the full centre as kernel. The quaternionic bilinear form has a multiplicative norm, its level set $\langle\cdot\rangle_{\natural}=\pm1$ is a group, and the sign supplies a genuine second component. The plain sesquilinear form has a definite form, its isometry condition is the unitarity of the parameter, and definiteness removes the sign entirely, leaving the $*$-unitary group and its determinant-one part.

## Worked Examples

**A $*$-unitary parameter.** Let $\tilde Q\in \mathrm{U}(2)$, so $\tilde Q^{*}\tilde Q=e_{t}$. Then $\Theta_{\tilde Q}$ is an isometry by the theorem, and it is the inner automorphism $\mathrm{Ad}_{\tilde Q}$ since $\tilde Q^{*}=\tilde Q^{-1}$.

**A non-central $*$-unitary in the basis.** Take $\tilde Q=i\vec e_x$. Then $\tilde Q^{*}=i\vec e_x$ and

$$
\tilde Q^{*}\tilde Q=(i\vec e_x)(i\vec e_x)=i^{2}\vec e_x^{2}=(-1)(-e_{t})=e_{t},
$$

so $i\vec e_x$ lies in the pin group and $\Theta_{i\vec e_x}$ is an isometry; its determinant is the determinant of the matrix $\mathsf{M}_2(i\vec e_x)$, so it lies in the spin group exactly when that determinant is one.

**A scaled $*$-unitary fails.** Take $\tilde Q=\sqrt2\,\tilde Q_1$ with $\tilde Q_1\in U$. Then $\tilde Q$ is not in the slice, and the operator is the similitude of multiplier $4$: on random pairs $\langle\Theta_{\tilde Q}\tilde S,\Theta_{\tilde Q}\tilde Q_1\rangle_{*}=4\langle\tilde S,\tilde Q_1\rangle_{*}$ and the operator is not an isometry of the form.

**The central phase is invisible.** Take $\tilde Q=\omega e_{t}$ with $\lvert\omega\rvert=1$, a central $*$-unitary. Then $\tilde Q^{*}\tilde Q=e_{t}$, so $\omega e_{t}$ lies in the pin group, and $\Theta_{\omega e_{t}}=\Theta_{e_{t}}$ is the identity: the whole central circle is the kernel of the assignment and produces one and the same operator.

**A reflection.** Take $\tilde Q_3=e_{t}$. Then $\langle\tilde Q_3,\tilde Q_3\rangle_{*}=1$ and

$$
r_{e_{t}}(\tilde Q_1)=\tilde Q_1-2\,\mathrm{Sc}(\tilde Q_1)\,e_{t},
$$

which is an isometry of the form by the proposition and which no two-sided operator equals: it is not multiplicative, and it changes the central part, while every two-sided operator of the pin group fixes it.

## Summary

The general plain sesquilinear form $\langle\tilde S,\tilde Q_1\rangle_{*}=\mathrm{Sc}(\tilde Q_1^{*}\tilde S)$ of the biquaternion algebra, positive definite of Gram matrix the identity, has for its two-sided operators $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ exactly the isometries with parameter in the **$*$-unitary slice** $\tilde Q^{*}\tilde Q=e_{t}$: the isometry condition is neither vacuous, as for the general plain bilinear form, nor a level set of a scalar form, as for the general quaternionic bilinear form, but the unitarity of the parameter. The **pin group** is therefore the $*$-unitary group $\mathrm{Pin}=U\cong \mathrm{U}(2)$, compact of real dimension four, and the **spin group** is its determinant-one part $\mathrm{Spin}=\mathrm{SU}(2)$, compact of real dimension three, normal and of derived group equal to itself, with quotient $\mathrm{Pin}/\mathrm{Spin}\cong \mathrm{U}(1)$. Because the defining element $\tilde Q^{*}\tilde Q$ is positive, the value $-1$ is impossible, so there is no second component and no discrete sign: the quotient of pin by spin is the connected circle. The assignment $\tilde Q\mapsto\Theta_{\tilde Q}$ is a group homomorphism with kernel the central circle $\mathrm{U}(1)e_{t}$ on the pin group and the two-element group $\{\pm e_{t}\}$ on the spin group, so it is the classical two-to-one cover of the rotation group $PU(2)\cong SO(3)$, of real dimension three; on the pin group the operator is an algebra automorphism, indeed the inner automorphism $\mathrm{Ad}_{\tilde Q}$, and the family reaches only these rotations inside the full isometry group $\mathrm{U}(4)$ of real dimension sixteen. The reflections of the form are isometries and are not two-sided operators, because they are not multiplicative and do not fix the centre, so the family generates the automorphisms and not the isometries. A scaled $*$-unitary is a similitude of positive multiplier $\lvert c\rvert^{4}$, never a sign; the central phase is invisible to the operator; and the shells of the multiplicative norm belong to the two bilinear products, not to this one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde S,\tilde Q_1\rangle_{*}=\mathrm{Sc}(\tilde Q_1^{*}\tilde S)$ | The general plain sesquilinear form; positive definite, Gram matrix the identity |
| $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ | The two-sided operator of $\tilde Q$; the dagger sandwich |
| $\Theta_{\tilde Q\tilde{Q}_3}=\Theta_{\tilde Q}\circ\Theta_{\tilde{Q}_3}$ | Composition law; the assignment is multiplicative in the parameter |
| $\Theta_{A\tilde Q}=\lvert A\rvert^{2}\Theta_{\tilde Q}$ | Parameter rule for central $A$; the phase is invisible |
| $U=\{\tilde Q^{*}\tilde Q=e_{t}\}=\mathrm{U}(2)$ | The $*$-unitary slice; real dimension four |
| $\mathrm{Pin}=U\cong \mathrm{U}(2)$ | The pin group; the isometry parameters of the form |
| $\mathrm{Spin}=\mathrm{SU}(2)=\ker\det$ | The spin group; real dimension three, normal in $\mathrm{Pin}$ |
| $\mathrm{Pin}/\mathrm{Spin}\cong \mathrm{U}(1)$ | The quotient; the circle, not a two-element group |
| $\mathrm{U}(1)e_{t}$ | Kernel of the assignment on the pin group; the central circle |
| $\{\pm e_{t}\}$ | Kernel of the assignment on the spin group; the two-to-one cover |
| $\mathrm{Pin}/\mathrm{U}(1)e_{t}\cong PU(2)\cong SO(3)$ | The image; the inner automorphisms reached, real dimension three |
| $r_{\tilde Q_3}(\tilde Q_1)=\tilde Q_1-2\langle\tilde Q_1,\tilde Q_3\rangle_{*}\langle\tilde Q_3,\tilde Q_3\rangle_{*}^{-1}\tilde Q_3$ | The reflection of the form; an isometry outside the family |

## Further Reading

- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), for the operator, its composition and parameter rules, the adjoint, the $*$-unitary criterion and the kernel.
- [The Unitary Slice and the Compact Real Form with Hermitian Adjoint](the-unitary-slice-and-the-compact-real-form-with-hermitian-adjoint.html), for the slice, the group $\mathrm{U}(2)$ and its determinant-one part.
- [The Pin and Spin Groups of the General Quaternionic Algebra](the-pin-and-spin-groups-of-the-general-quaternionic-algebra.html), the bilinear twin whose isometry condition is the norm level set $\langle\cdot\rangle_{\natural}=\pm1$.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), §*The Isometry Group and the Absence of a Pin Group*, the bilinear twin whose isometry condition is vacuous and whose level set is not a group.
- [The Pin and Spin Groups with Signed Hermitian Adjoint](the-pin-and-spin-groups-with-signed-hermitian-adjoint.html), for the general theory of the pin and spin groups with a Hermitian adjoint, of which this is the biquaternion instance.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, the four conjugations and the scalar form.
- [The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint](the-hermitian-sandwich-in-the-biquaternion-algebra-with-hermitian-adjoint.html), for the same operator in coordinates, the forms, positivity and the slice.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms of the algebra side by side.
