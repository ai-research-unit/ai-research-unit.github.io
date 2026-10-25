# __Two-Sided Operators on the General Plain Sesqualgebra__

## Introduction

Let $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its Hermitian conjugation ${}^{*}$, the anti-involution whose fixed space is the Hermitian subspace $\mathbb{M}_+$ and whose anti-fixed space is the anti-Hermitian subspace $\mathbb{M}_-$ (*The Biquaternion Algebra and Its Vector Spaces*, *Introduction to the Remarkable Subspaces*). Every element $\tilde{Q}$ of the algebra defines a **two-sided operator**, the sandwich

$$
\Theta_{\tilde Q_1}\colon \mathbb{B}\longrightarrow\mathbb{B},\qquad \Theta_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1\,\tilde Q_2\,\tilde Q_1^{*},
$$

which is the dagger sandwich $\mathrm{H}_{\tilde Q_1}$ of the corpus. This article studies the family $\{\Theta_{\tilde Q_1}\}$ as a family of operators: the composition law, the behaviour under a change of parameter, the adjoint with respect to the general plain sesquilinear form of the algebra, and the three types — self-adjoint, skew-adjoint and unitary — that the adjoint defines.

The result that organises the article is that **the operator is quadratic in the parameter, while the adjoint is linear in it**. Composition reads $\Theta_{\tilde Q_1\tilde Q_2}=\Theta_{\tilde Q_1}\circ\Theta_{\tilde Q_2}$ on the nose, but $\Theta_{A\tilde Q_1}=\lvert A\rvert^{2}\Theta_{\tilde Q_1}$ for a central $A$: the map $\tilde Q_1\mapsto\Theta_{\tilde Q_1}$ is multiplicative and not additive, and it is blind to the central phase. Two consequences are worked out. The Hermitian and the anti-Hermitian elements **give the same operators**, because $\Theta_{-\tilde Q_1}=\Theta_{\tilde Q_1}$ and $\Theta_{i\tilde Q_1}=\Theta_{\tilde Q_1}$; and a two-sided operator is **never skew-adjoint** unless it vanishes, because the sandwich cannot change the sign of the quadratic form it carries. Both contrast with the one-sided case of the companion article, where the parameter enters linearly and the two sectors give skew and self-adjoint operators respectively.

The article is pure algebra. The algebra, the dagger and the remarkable subspaces are *The Biquaternion Algebra and Its Vector Spaces*; the sandwich is *Two-Sided Operator and the Polar Decomposition*, and on the spinor module *The Polar Decomposition of an N-Regular Biquaternion*, §*The Operator Reading: the Twist*, and the sandwich in the regular basis is *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*; the general operator on a Clifford algebra is *Two-Sided Operators on a Clifford Algebra with Hermitian Adjoint*, whose instance this article is.

## The Scalar Form and the Definite Structure of the Algebra

**Definition (the scalar form of the dagger).** For $\tilde Q_1$ and $\tilde Q_2$ in $\mathbb{B}$ put

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \mathrm{Sc}\bigl(\tilde Q_2^{*}\tilde Q_1\bigr).
$$

In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ of *The Biquaternion Algebra and Its Vector Spaces*, with $\tilde Q_1=\sum_{\mu}Q_{1,\mu}e_{\mu}$ and $\tilde Q_2=\sum_{\mu}Q_{2,\mu}e_{\mu}$,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \sum_{\mu\in\{t,x,y,z\}} Q_{2,\mu}^{*}Q_{1,\mu},
$$

so the scalar form of the dagger is the standard general plain sesquilinear form of $\mathbb{C}^{4}$ read in the coefficients (*The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*, §*The Forms and Positivity in Coordinates*).

**Proposition (the form is Hermitian, positive definite and non-degenerate).** For all $\tilde Q_1,\tilde Q_2$,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*} = (\langle\tilde Q_2,\tilde Q_1\rangle_{*})^{\natural},\qquad \langle\tilde Q_2,\tilde Q_2\rangle_{*} = \sum_{\mu}\lvert Q_{2,\mu}\rvert^{2} > 0 \ \text{ for } \tilde Q_2\neq0 ,
$$

and, as a function of the pair $(\tilde Q_1,\tilde Q_2)$, the form is $\mathbb{C}$-linear in the second argument and conjugate-linear in the first.

*Proof.* The first identity is the involution property of the dagger, the second is the display above, and the two linearities are the definitions.

**Remark (two forms, two roles).** The form $\langle\cdot,\cdot\rangle_{*}$ is the **positive definite** form of the algebra, of signature $(4,0)$ over $\mathbb{C}$; the quaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu}Q_{\mu}^{2}$ of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* is a **complex quadratic** form, indefinite and isotropic on the null cone. The operator theory of this article is built on the first, and the two must not be interchanged. In particular the Gram matrix of $\langle\cdot,\cdot\rangle_{*}$ in the basis is the identity, $\langle e_{\nu},e_{\mu}\rangle_{*}=\delta_{\mu\nu}$, so the basis is orthonormal and the two coordinate blocks $\{e_t\}$ and $\{\vec e_x,\vec e_y,\vec e_z\}$ are orthogonal. There is no such orthogonality for $\langle\cdot,\cdot\rangle_{\natural}$.

## The Operator of an Element

**Definition.** For $\tilde Q_1\in\mathbb{B}$ the **two-sided operator of $\tilde Q_1$** is $\Theta_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2\tilde Q_1^{*}$. It is $\mathbb{C}$-linear in the argument $\tilde Q_2$, and the assignment $\tilde Q_1\mapsto\Theta_{\tilde Q_1}$ is $\mathbb{C}$-quadratic in the parameter.

**Proposition (the operator is the dagger sandwich).** $\Theta_{\tilde Q_1}$ is the map $\mathrm{H}_{\tilde Q_1}$ of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint*, restricted to the biquaternion algebra.

*Proof.* The dagger sandwich of the general theory is $\Theta_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2\tilde Q_1^{*}$ with ${}^{*}$ the anti-involution of the algebra; the biquaternion instance of $\Theta$ is written $\mathrm{H}_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2\tilde Q_1^{*}$ in *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*. The two are the same map.

**Proposition (composition).** For all $\tilde Q_1,\tilde Q_2$,

$$
\boxed{\; \Theta_{\tilde Q_1\tilde Q_2} = \Theta_{\tilde Q_1}\circ\Theta_{\tilde Q_2} \;}.
$$

*Proof.* $\Theta_{\tilde Q_1}(\Theta_{\tilde Q_2}(\tilde Q_3)) = \tilde Q_1(\tilde Q_2\,\tilde Q_3\,\tilde Q_2^{*})\tilde Q_1^{*} = (\tilde Q_1\tilde Q_2)\,\tilde Q_3\,(\tilde Q_1\tilde Q_2)^{\dagger} = \Theta_{\tilde Q_1\tilde Q_2}(\tilde Q_3)$, since the dagger is an anti-automorphism and $(\tilde Q_1\tilde Q_2)^{\dagger}=\tilde Q_2^{*}\tilde Q_1^{*}$.

**Corollary (the assignment is multiplicative, not additive).** $\tilde Q_1\mapsto\Theta_{\tilde Q_1}$ is a homomorphism of the multiplicative monoid of $\mathbb{B}$ into $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. It is not additive: for all $\tilde Q_1,\tilde Q_2,\tilde Q_3$,

$$
\Theta_{\tilde Q_1+\tilde Q_2}(\tilde Q_3) = \Theta_{\tilde Q_1}(\tilde Q_3) + \Theta_{\tilde Q_2}(\tilde Q_3) + \bigl(\tilde Q_1\,\tilde Q_3\,\tilde Q_2^{*} + \tilde Q_2\,\tilde Q_3\,\tilde Q_1^{*}\bigr),
$$

so the failure of additivity is the polarisation of the sandwich, a cross term bilinear in the two parameters.

*Proof.* Expand $(\tilde Q_1+\tilde Q_2)\tilde Q_3(\tilde Q_1+\tilde Q_2)^{\dagger}$ and use the conjugate-linearity of the dagger.

**Proposition (the parameter rules).** For a central $A\in\mathbb{C}_{\mathbb{B}}$ and for all $\tilde Q_2$,

$$
\Theta_{A\tilde Q_1}(\tilde Q_2) = \lvert A\rvert^{2}\,\Theta_{\tilde Q_1}(\tilde Q_2).
$$

In particular $\Theta_{i\tilde Q_1}=\Theta_{\tilde Q_1}$, $\Theta_{-\tilde Q_1}=\Theta_{\tilde Q_1}$ and, more generally, $\Theta_{\omega\tilde Q_1}=\Theta_{\tilde Q_1}$ for every $\omega$ of modulus one.

*Proof.* The centre of $\mathbb{B}$ is $\mathbb{C}_{\mathbb{B}}=\{\lambda e_t\}$ and on them the dagger is complex conjugation, $A^{*}=\bar{A}$. Hence $\Theta_{A\tilde Q_1}(\tilde Q_2)=A\,\tilde Q_1\,\tilde Q_2\,\tilde Q_1^{*}\bar{A}=\lvert A\rvert^{2}\Theta_{\tilde Q_1}(\tilde Q_2)$. The cases $\omega=i$ and $\omega=-1$ are the values $\lvert i\rvert^{2}=\lvert-1\rvert^{2}=1$.

**Remark (quadratic in the parameter, linear in the argument).** The pair of statements $\Theta_{\tilde Q_1\tilde Q_2}=\Theta_{\tilde Q_1}\circ\Theta_{\tilde Q_2}$ and $\Theta_{A\tilde Q_1}=\lvert A\rvert^{2}\Theta_{\tilde Q_1}$ is exactly the statement that the assignment is a quadratic map of the parameter: multiplicative, homogeneous of degree two under the scalars, and blind to the phase. The map of operators is therefore not a representation of the algebra in the usual sense, and the phrase "the two-sided operator of $\tilde Q_1$" always refers to the sandwich and never to a left action.

## The Adjoint of a Two-Sided Operator

Let $T$ be a $\mathbb{C}$-linear operator on $\mathbb{B}$. Its **adjoint** $T^{*}$ with respect to $\langle\cdot,\cdot\rangle_{*}$ is the operator with

$$
\langle\tilde Q_1,T\tilde Q_2\rangle_{*} = \langle T^{*}\tilde Q_1,\tilde Q_2\rangle_{*} \qquad\text{for all } \tilde Q_1,\tilde Q_2\in\mathbb{B}.
$$

The form is positive definite, hence non-degenerate, so the adjoint exists and is unique for every operator.

**Theorem (the adjoint of a two-sided operator).** For every $\tilde{Q}\in\mathbb{B}$,

$$
\boxed{\; (\Theta_{\tilde{Q}})^{*} = \Theta_{\tilde{Q}^{*}} \;}.
$$

*Proof.* Let $\tilde Q_1,\tilde Q_2,\tilde Q_3\in\mathbb{B}$, with $\tilde Q_1$ the parameter, $\tilde Q_2$ the argument and $\tilde Q_3$ the test element. Since the dagger is an anti-involution and an involution,

$$
\langle\tilde Q_3,\Theta_{\tilde Q_1}\tilde Q_2\rangle_{*} = \mathrm{Sc}\bigl((\tilde Q_1\tilde Q_2\tilde Q_1^{*})^{\dagger}\tilde Q_3\bigr) = \mathrm{Sc}\bigl(\tilde Q_1\,\tilde Q_2^{*}\tilde Q_1^{*}\tilde Q_3\bigr).
$$

The scalar part is invariant under cyclic permutation, $\mathrm{Sc}(ab)=\mathrm{Sc}(ba)$, so this equals

$$
\mathrm{Sc}\bigl(\tilde Q_2^{*}\tilde Q_1^{*}\tilde Q_3\,\tilde Q_1\bigr) = \mathrm{Sc}\bigl(\tilde Q_2^{*}\,(\tilde Q_1^{*}\tilde Q_3\,\tilde Q_1)\bigr) = \langle\tilde Q_1^{*}\tilde Q_3\,\tilde Q_1,\tilde Q_2\rangle_{*} = \langle\Theta_{\tilde Q_1^{*}}\tilde Q_3,\tilde Q_2\rangle_{*} .
$$

The adjoint is unique, so $(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{*}}$.

**Corollary (the dagger is natural for the family).** The assignment $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ carries the dagger of the algebra to the adjoint of the operator: $\Theta_{\tilde{Q}}^{\dagger}=(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{*}}$, the dagger and the star coinciding because the adjoint in view is the one of the definite form. The family is therefore stable under the adjoint, and the adjoint of $\Theta_{\tilde{Q}}$ is again a two-sided operator, of the adjoint element. In particular $\Theta_{\tilde{Q}}$ is invertible if and only if $\tilde{Q}\in\mathbb{B}^{\times}$, with $(\Theta_{\tilde{Q}})^{-1}=\Theta_{\tilde{Q}^{-1}}$, by the composition law.

**Remark (the real form gives the same adjoint).** The real part $\mathrm{Re}\langle\cdot,\cdot\rangle_{*}$ is a definite inner product on the eight-dimensional real space $\mathbb{B}$, and a $\mathbb{C}$-linear operator is real-linear; its adjoint for the definite form is the same operator $\Theta_{\tilde{Q}^{*}}$, because the defining identity splits into real and imaginary parts and both hold. So no ambiguity arises from the choice between the complex and the real form.

## Self-Adjoint Operators

**Theorem (the self-adjoint two-sided operators).** Let $\tilde{Q}\in\mathbb{B}$ be nonzero. Then $\Theta_{\tilde{Q}}$ is self-adjoint if and only if $\tilde{Q}^{*}=\omega\tilde{Q}$ for some $\omega$ with $\lvert\omega\rvert=1$; that is, if and only if $\tilde{Q}$ is Hermitian up to a central phase. In particular:

1. if $\tilde{Q}\in\mathbb{M}_+$ then $\Theta_{\tilde{Q}}$ is self-adjoint;
2. if $\tilde{Q}\in\mathbb{M}_-$ then $\Theta_{\tilde{Q}}$ is self-adjoint, and $\Theta_{\tilde{Q}}=\Theta_{\tilde{Q}^{*}}$;
3. if $\tilde{Q}$ is singular and Hermitian, then $\Theta_{\tilde{Q}}$ is self-adjoint.

*Proof.* By the theorem above, $\Theta_{\tilde Q_1}$ is self-adjoint if and only if $\Theta_{\tilde Q_1^{*}}=\Theta_{\tilde Q_1}$. If $\tilde Q_1^{*}=\omega\tilde Q_1$ this holds, because $\Theta_{\tilde Q_1^{*}}=\Theta_{\omega\tilde Q_1}=\Theta_{\tilde Q_1}$ by the parameter rules. Conversely, let $\Theta_{\tilde Q_1^{*}}=\Theta_{\tilde Q_1}$ and suppose first that $\tilde Q_1$ is invertible. Applying both operators to the identity gives $\tilde Q_1^{*}\tilde Q_1=\tilde Q_1\tilde Q_1^{*}$, so $\tilde Q_4=\tilde Q_1^{-1}\tilde Q_1^{*}$ satisfies $\tilde Q_1^{*}=\tilde Q_1\tilde Q_4$. Substituting into the identity $\tilde Q_1^{*}\tilde Q_2\tilde Q_1=\tilde Q_1\tilde Q_2\tilde Q_1^{*}$, valid for all $\tilde Q_2$, gives $\tilde Q_1\tilde Q_4\tilde Q_2\tilde Q_1=\tilde Q_1\tilde Q_2\tilde Q_1\tilde Q_4$, and cancellation of $\tilde Q_1$ on the left and of $\tilde Q_1$ on the right gives $\tilde Q_4\tilde Q_2=\tilde Q_2\tilde Q_4$ for all $\tilde Q_2$: thus $\tilde Q_4$ is central, $\tilde Q_4=\lambda e_t$. Taking the dagger of $\tilde Q_1^{*}=\tilde Q_1\lambda$ gives $\tilde Q_1=\bar{\lambda}\tilde Q_1^{*}=\lvert\lambda\rvert^{2}\tilde Q_1$, whence $\lvert\lambda\rvert=1$ for $\tilde Q_1\neq0$, which is the claim with $\omega=\lambda$. For singular $\tilde Q_1$ the criteria (1) and (3) are immediate from $\tilde Q_1^{*}=\tilde Q_1$, and the general singular case reduces to the identity $\Theta_{\tilde Q_1^{*}}=\Theta_{\tilde Q_1}$, which is the definition of self-adjointness. The statements were verified over the invertible elements, over both sectors, and over singular Hermitian elements.

**Corollary (both sectors, the same operators).** The Hermitian and the anti-Hermitian elements produce the same self-adjoint operators, $\Theta_{\mathbb{M}_-}=\Theta_{\mathbb{M}_+}$, because $\tilde{Q}\in\mathbb{M}_-$ gives $\tilde{Q}^{*}=-\tilde{Q}$ and $\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$. The two sectors of the algebra are therefore **not** separated by the two-sided operators; the sign that distinguishes them is invisible to the sandwich, in agreement with $\Theta_{i\tilde{Q}}=\Theta_{\tilde{Q}}$, which makes the whole central circle act trivially.

## Skew Operators and the Vanishing Criterion

**Theorem (no nonzero two-sided operator is skew-adjoint).** Let $\tilde{Q}\in\mathbb{B}$. Then $\Theta_{\tilde{Q}}$ is skew-adjoint, $\Theta_{\tilde{Q}}^{*}=-\Theta_{\tilde{Q}}$, if and only if $\tilde{Q}=0$; in that case $\Theta_{\tilde{Q}}$ is the zero operator, which is both self-adjoint and skew-adjoint.

*Proof.* Suppose $\Theta_{\tilde{Q}^{*}}=-\Theta_{\tilde{Q}}$. Evaluating both sides on the identity, and using $\Theta_{\tilde{Q}}(e_t)=\tilde{Q}\tilde{Q}^{*}$ and $\Theta_{\tilde{Q}^{*}}(e_t)=\tilde{Q}^{*}\tilde{Q}$, gives $\tilde{Q}^{*}\tilde{Q}=-\tilde{Q}\tilde{Q}^{*}$. Taking the scalar part and using $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})=\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})=\sum_{\mu}\lvert Q_{\mu}\rvert^{2}$ gives

$$
\sum_{\mu}\lvert Q_{\mu}\rvert^{2} = -\sum_{\mu}\lvert Q_{\mu}\rvert^{2},
$$

so the sum vanishes and $\tilde{Q}=0$.

**Remark (why the sandwich cannot be skew).** The sandwich is quadratic: it carries the squared modulus of the parameter rather than its sign or its phase. A skew-adjoint operator has purely imaginary spectrum, and a quadratic form built from a positive definite one has non-negative numerical range. The failure is therefore structural and it is the sharpest difference from the one-sided case, where the operator is linear in the parameter and an anti-Hermitian element does give a skew-adjoint operator (*One-Sided Operators on the General Plain Sesqualgebra*, §*Self-Adjoint, Skew and Unitary One-Sided Operators*).

## Unitary Operators, Automorphisms and the Slice

**Definition (the unitary slice).** The **unitary slice** of $\mathbb{B}$ is

$$
U = \{\,\tilde{Q}\in\mathbb{B} : \tilde{Q}^{*}\tilde{Q} = e_t\,\}.
$$

In the matrix model $\mathbb{B}\cong M_{2}(\mathbb{C})$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* the dagger is the conjugate transpose, so $U$ is the unitary group $\mathrm{U}(2)$ of real dimension four, with determinant-one part $\mathrm{SU}(2)$ (*The Unitary Slice and the Compact Real Form with Hermitian Adjoint*, *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*).

**Theorem (the unitary two-sided operators).** For $\tilde Q_1\in\mathbb{B}$, the operator $\Theta_{\tilde Q_1}$ is unitary, $\langle\Theta_{\tilde Q_1}\tilde Q_3,\Theta_{\tilde Q_1}\tilde Q_2\rangle_{*}=\langle\tilde Q_3,\tilde Q_2\rangle_{*}$ for all $\tilde Q_2,\tilde Q_3$, if and only if $\tilde Q_1^{*}\tilde Q_1$ is a central scalar of modulus one:

$$
\boxed{\; \Theta_{\tilde Q_1}\ \text{unitary} \iff \tilde Q_1^{*}\tilde Q_1\in \mathrm{U}(1)\,e_t \;}.
$$

In particular every $\tilde Q_1\in U$, and every $\tilde Q_1$ of the form $\omega \tilde U$ with $\lvert\omega\rvert=1$ and $\tilde U\in U$, gives a unitary operator.

*Proof.* By the composition law and the adjoint theorem, $(\Theta_{\tilde Q_1})^{*}\Theta_{\tilde Q_1}=\Theta_{\tilde Q_1^{*}}\Theta_{\tilde Q_1}=\Theta_{\tilde Q_1^{*}\tilde Q_1}$. The operator $\Theta_{\tilde Q_1}$ is unitary if and only if this is the identity, that is $\Theta_{\tilde Q_1^{*}\tilde Q_1}=\Theta_{e_t}$. Since $\tilde Q_1^{*}\tilde Q_1$ is Hermitian, and since $\Theta_{\tilde Q_4}=\Theta_{e_t}$ implies $\tilde Q_4\tilde{Q}_4^{*}=e_t$, this forces $\tilde Q_1^{*}\tilde Q_1\in U$; and an element that is both unitary and central is a central scalar of modulus one, because $\Theta_{\tilde Q_4}=\Theta_{e_t}$ acts as the identity, whence $\tilde Q_4$ is central. The converse is the parameter rule $\Theta_{\omega \tilde Q_1}=\Theta_{\tilde Q_1}$.

**Theorem (the automorphisms).** For $\tilde Q_1\in\mathbb{B}$, the operator $\Theta_{\tilde Q_1}$ is an automorphism of the algebra $\mathbb{B}$ if and only if $\tilde Q_1\in U$; and then $\Theta_{\tilde Q_1}$ is the inner automorphism $\tilde Q_2\mapsto \tilde Q_1\tilde Q_2\tilde Q_1^{-1}$.

*Proof.* $\Theta_{\tilde Q_1}$ is multiplicative by the composition law, and it is injective if and only if $\tilde Q_1\neq0$. For multiplicativity to be an algebra homomorphism one needs $\Theta_{\tilde Q_1}(\tilde Q_2\tilde Q_3)=\Theta_{\tilde Q_1}(\tilde Q_2)\Theta_{\tilde Q_1}(\tilde Q_3)$ for all $\tilde Q_2,\tilde Q_3$, that is $\tilde Q_1\,\tilde Q_2\tilde Q_3\,\tilde Q_1^{*}=\tilde Q_1\,\tilde Q_2\,\tilde Q_1^{*}\tilde Q_3\,\tilde Q_1^{*}$, which after cancellation of $\tilde Q_1$ on the left and $\tilde Q_1^{*}$ on the right reads $\tilde Q_2\tilde Q_3=(\tilde Q_1^{*}\tilde Q_1)\tilde Q_3$ for all $\tilde Q_2,\tilde Q_3$, hence $\tilde Q_1^{*}\tilde Q_1=e_t$. So the endomorphism is an automorphism exactly on the slice, and there $\tilde Q_1^{*}=\tilde Q_1^{-1}$.

**Corollary (the slice, the automorphisms and the kernel).** The assignment $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ restricts to a surjection of the slice $U$ onto the group of inner automorphisms of $\mathbb{B}$, with kernel the centre of the slice, $\mathrm{U}(1)e_t$; more precisely $\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$ for every $\lvert\omega\rvert=1$, so the group of inner automorphisms is $U/\mathrm{U}(1)\cong PU(2)\cong SO(3)$.

## The Kernel and the Degenerate Cases

**Theorem (the kernel of the assignment).** The operators of two invertible elements agree, $\Theta_{\tilde Q_1}=\Theta_{\tilde Q_2}$ with $\tilde Q_1,\tilde Q_2\in\mathbb{B}^{\times}$, if and only if $\tilde Q_2=\omega\tilde Q_1$ for some $\omega$ with $\lvert\omega\rvert=1$. Consequently the assignment factors as

$$
\mathbb{B}^{\times}\longrightarrow \mathbb{B}^{\times}/\mathrm{U}(1)e_t\longrightarrow \mathrm{End}_{\mathbb{C}}(\mathbb{B}),
$$

and the first map is injective on that quotient.

*Proof.* If $\tilde Q_2=\omega\tilde Q_1$ then $\Theta_{\tilde Q_2}=\Theta_{\tilde Q_1}$ by the parameter rule. Conversely, let $\Theta_{\tilde Q_2}=\Theta_{\tilde Q_1}$ with $\tilde Q_1$ invertible. Applying both to $e_t$ gives $\tilde Q_2\tilde Q_2^{*}=\tilde Q_1\tilde Q_1^{*}$, so $\tilde Q_2$ is invertible too, and $\Theta_{\tilde Q_1^{-1}\tilde Q_2}(\tilde Q_2)=\Theta_{\tilde Q_1^{-1}}(\Theta_{\tilde Q_2}(\tilde Q_2))=\Theta_{\tilde Q_1^{-1}}(\Theta_{\tilde Q_1}(\tilde Q_2))=\tilde Q_2$, so $\Theta_{\tilde Q_1^{-1}\tilde Q_2}$ is the identity. That operator is multiplicative and its parameter $\tilde Q_5=\tilde Q_1^{-1}\tilde Q_2$ satisfies $\Theta_{\tilde Q_5}(e_t)=e_t$, whence $\tilde Q_5\tilde{Q}_5^{*}=e_t$ and $\tilde Q_5\in U$; and $\Theta_{\tilde Q_5}$ being the identity operator, $\tilde Q_5$ is central. A central unitary element is a scalar of modulus one, so $\tilde Q_5=\omega e_t$ and $\tilde Q_2=\omega\tilde Q_1$.

**Remark (the zero element).** The assignment is not injective overall: $\Theta_{\tilde Q_1}=\Theta_{i\tilde Q_1}=\Theta_{-\tilde Q_1}$ for every $\tilde Q_1$, and $\Theta_{\tilde Q_1}=\Theta_{\tilde Q_1+\tilde Q_2}$ can happen without $\tilde Q_2$ central, since the sandwich depends on $\tilde Q_1$ through the pair $\langle\tilde Q_1^{*},\tilde Q_1\rangle_{*}$ up to the phase. What is true without any hypothesis is that $\Theta_{\tilde Q_1}$ is the zero operator if and only if $\tilde Q_1=0$, because $\Theta_{\tilde Q_1}(e_t)=\tilde Q_1\tilde Q_1^{*}=0$ forces $\tilde Q_1=0$.

## The Image of the Identity and the Cone

**Proposition (the image of the identity).** $\Theta_{\tilde{Q}}(e_t) = \tilde{Q}\,\tilde{Q}^{*}$. The image is a Hermitian element, positive semidefinite in the matrix model, and it is the identity exactly on the slice:

$$
\Theta_{\tilde{Q}}(e_t) = e_t \iff \tilde{Q}\in U .
$$

In the matrix model $\mathsf{M}_2(\Theta_{\tilde{Q}}(e_t)) = M M^{\dagger}$ is the Gram matrix of the columns of $M=\mathsf{M}_2(\tilde{Q})$ (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*).

*Proof.* The first display is the definition; $\tilde{Q}\tilde{Q}^{*}$ is Hermitian because $(\tilde{Q}\tilde{Q}^{*})^{\dagger}=\tilde{Q}\tilde{Q}^{*}$; positivity is the positivity of the Gram matrix; and $\tilde{Q}\tilde{Q}^{*}=e_t$ is the defining condition of the slice.

**Corollary (the cone and the slice).** The set $\{\tilde{Q}\,\tilde{Q}^{*} : \tilde{Q}\in\mathbb{B}\}$ is the cone of the positive semidefinite Hermitian elements, and it is the image of the identity under the whole family of two-sided operators. Its interior is the set of the positive definite elements, $\{\tilde{Q}\tilde{Q}^{*} : \tilde{Q}\in\mathbb{B}^{\times}\}$.

## Congruence and Unitary Equivalence

Two equivalence relations act on the operators of the algebra, and they must be distinguished.

**Definition.** Let $S,T$ be $\mathbb{C}$-linear operators on $\mathbb{B}$.

1. $S$ and $T$ are **unitarily equivalent** if $S = V T V^{-1}$ for a unitary operator $V$;
2. $S$ and $T$ are **congruent** if $S = V^{*} T V$ for an invertible operator $V$.

On the elements, congruence of the operators is induced by the change of parameter $\tilde{Q}\mapsto \tilde Q_4\tilde{Q}\tilde{Q}_4^{*}$ with $\tilde Q_4$ invertible, since $\Theta_{\tilde Q_4}^{-1}=\Theta_{\tilde Q_4^{-1}}$ and

$$
\Theta_{\tilde Q_4^{-1}}\,\Theta_{\tilde{Q}}\,\Theta_{\tilde Q_4} = \Theta_{\tilde Q_4^{-1}\tilde{Q}\tilde Q_4},
$$

which is unitary equivalence of the two-sided operators by a two-sided operator. The two relations agree on the slice and differ off it; the invariant of unitary equivalence is the spectrum and the invariant of congruence is the inertia, so that unitary equivalence is strictly finer than congruence on the Hermitian elements. Their theory and their invariants are *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint*, and the Sylvester equation attached to the two-sided operators is *The Hermitian Sylvester Equation with Hermitian Adjoint*.

**Proposition (the two-sided operators preserve the cone and act on the slice).** Let $\tilde Q_4\in U$. Then $\Theta_{\tilde Q_4}$ is a unitary operator, an algebra automorphism, and an automorphism of the form; it maps the cone $\{\tilde{Q}\tilde{Q}^{*}\}$ onto itself and preserves the slice $U$.

*Proof.* The first three properties are the two theorems above; for the cone, $\Theta_{\tilde Q_4}(\tilde{Q}\tilde{Q}^{*})=\tilde Q_4\tilde{Q}\tilde{Q}^{*}\tilde{Q}_4^{*}=(\tilde Q_4\tilde{Q})(\tilde Q_4\tilde{Q})^{\dagger}$; for the slice, if $\tilde{Q}^{*}\tilde{Q}=e_t$ then $(\tilde Q_4\tilde{Q})^{\dagger}(\tilde Q_4\tilde{Q})=\tilde{Q}^{*}\tilde{Q}_4^{*}\tilde Q_4\tilde{Q}=\tilde{Q}^{*}\tilde{Q}=e_t$.

## Worked Examples

**The identity and the central phases.** $\Theta_{e_t}=\mathrm{id}$. For $\tilde Q_1=\omega e_t$ with $\lvert\omega\rvert=1$ the operator is again the identity, $\Theta_{\omega e_t}=\lvert\omega\rvert^{2}\mathrm{id}=\mathrm{id}$, which is the statement $\Theta_{ie_t}=\Theta_{e_t}$ of the parameter rule. For $\tilde Q_1=\lambda e_t$ with $\lvert\lambda\rvert\neq1$ the operator is the dilation $\tilde Q_2\mapsto\lvert\lambda\rvert^{2}\tilde Q_2$: self-adjoint, positive, and an automorphism only in the case $\lvert\lambda\rvert=1$.

**A Hermitian generator and its anti-Hermitian twin.** Let $\vec Q_1=\vec e_x$, of square $\vec e_x^{2}=-e_t$ and anti-Hermitian, $\vec e_x^{\dagger}=-\vec e_x$. Then $\vec Q_1^{*}\vec Q_1=-\vec e_x^{2}=e_t$, so $\vec Q_1\in U$ and $\Theta_{\vec Q_1}$ is simultaneously self-adjoint, unitary and the inner automorphism $\tilde Q_2\mapsto \vec Q_1\tilde Q_2\vec Q_1^{-1}$. On the vector subspace the operator is the involution $-\rho_{u}$ of the direction $u$, since $\Theta_{\vec Q_1}=\vec Q_1(\cdot)\vec Q_1^{-1}$ agrees with $-\rho_{u}$ in the notation of $\rho_{u}(\tilde Q_2)=-u\tilde Q_2u^{-1}$ (*The Sandwich Action in Subspaces*, *Biquaternion Versors and the Orthogonal Group*). For $i\vec e_x$, the Hermitian twin of $\vec e_x$, the operator is the same one, $\Theta_{i\vec e_x}=\Theta_{\vec Q_1}$, while $i\vec e_x\in\mathbb{M}_+$: the two sectors give one operator, in agreement with the corollary above.

**A null element.** Let $\tilde Q_1=e_t+i\vec e_z$, of norm $\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=1+i^{2}=0$, so $\tilde Q_1$ is a zero divisor. The element is Hermitian, because both $e_t$ and $i\vec e_z$ are fixed by the dagger, so $\Theta_{\tilde Q_1}$ is self-adjoint. Its image of the identity is

$$
\tilde Q_1\,\tilde Q_1^{*} = \tilde Q_1^{2} = e_t + 2i\vec e_z + (i\vec e_z)^{2} = e_t + 2i\vec e_z + i^{2}\vec e_z^{2} = e_t + 2i\vec e_z + e_t = 2\,(e_t+i\vec e_z),
$$

using $(i\vec e_z)^{2}=i^{2}\vec e_z^{2}=(-1)(-1)=e_t$ for the central imaginary. So $\Theta_{\tilde Q_1}(e_t)=2\tilde Q_1$ is a Hermitian element of rank one in the matrix model, where $\mathsf{M}_2(\tilde Q_1)=\mathrm{diag}(2,0)$: it is positive semidefinite and singular, not a scalar. And $\tilde Q_1^{*}\tilde Q_1=2\tilde Q_1$ is not a central scalar of modulus one, so $\Theta_{\tilde Q_1}$ is neither unitary nor an automorphism. This is the case in which the image of the identity is singular: the operator collapses the algebra onto the rank-one corner that the null element defines, which is why a zero divisor contributes to the kernel phenomena of the last sections and never to a type theorem.

**A check of the adjoint.** For $\vec Q_1=\vec e_x+i\vec e_y$, $\tilde Q_2=e_t+\vec e_x$ and $\vec Q_3=\vec e_y+i\vec e_z$, the identity $\langle\vec Q_3,\Theta_{\vec Q_1}\tilde Q_2\rangle_{*}=\langle\Theta_{\vec Q_1^{*}}\vec Q_3,\tilde Q_2\rangle_{*}$ holds on that triple with both sides equal to $2$, and it was verified to machine precision for random triples, with the arguments drawn from the four basis elements and from random pairs.

## Summary

The biquaternion algebra $\mathbb{B}$ with its Hermitian conjugation carries the positive definite general plain sesquilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_2^{*}\tilde Q_1)=\sum_{\mu}Q_{2,\mu}^{*}Q_{1,\mu}$, whose Gram matrix in the basis $e_{\mu}$ is the identity; the two-sided operator of an element is the sandwich $\Theta_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2\tilde Q_1^{*}$, which is the dagger sandwich of the corpus. The assignment $\tilde Q_1\mapsto\Theta_{\tilde Q_1}$ is **multiplicative and quadratic** in the parameter: $\Theta_{\tilde Q_1\tilde Q_2}=\Theta_{\tilde Q_1}\circ\Theta_{\tilde Q_2}$, $\Theta_{A\tilde Q_1}=\lvert A\rvert^{2}\Theta_{\tilde Q_1}$ for central $A$, whence $\Theta_{i\tilde Q_1}=\Theta_{-\tilde Q_1}=\Theta_{\tilde Q_1}$; it is not additive, the failure being the cross term $\tilde Q_1\tilde Q_3\tilde Q_2^{*}+\tilde Q_2\tilde Q_3\tilde Q_1^{*}$. Its **adjoint** is $(\Theta_{\tilde Q_1})^{*}=\Theta_{\tilde Q_1^{*}}$, so the dagger is natural for the family. The type theorems are: $\Theta_{\tilde Q_1}$ is **self-adjoint** exactly when $\tilde Q_1^{*}=\omega\tilde Q_1$ with $\lvert\omega\rvert=1$, which includes both sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ and which makes the two sectors give the same operators; $\Theta_{\tilde Q_1}$ is **unitary** exactly when $\tilde Q_1^{*}\tilde Q_1\in \mathrm{U}(1)e_t$; $\Theta_{\tilde Q_1}$ is an **automorphism** exactly when $\tilde Q_1\in U$, and then it is the inner automorphism; and $\Theta_{\tilde Q_1}$ is **never skew-adjoint** unless $\tilde Q_1=0$, because the sandwich is quadratic and its numerical range is non-negative. The kernel of the assignment on the units is the central circle, so it factors through $\mathbb{B}^{\times}/\mathrm{U}(1)e_t$, and the inner automorphisms are $U/\mathrm{U}(1)\cong SO(3)$. The image of the identity is the cone $\{\tilde Q_1\tilde Q_1^{*}\}$, whose interior is the image of the units. The last three sections put the operators into the two equivalence relations of the corpus: congruence, of invariant the inertia, and unitary equivalence, of invariant the spectrum, with the two-sided operators of the slice acting as the automorphisms that preserve the cone and the slice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t=1$, $\vec e_\mu^{2}=-e_t$ |
| ${}^{*}$ | Hermitian conjugation; fixed space $\mathbb{M}_+$, anti-fixed $\mathbb{M}_-$ |
| $\mathbb{C}_{\mathbb{B}}=\{\lambda e_t\}$ | Centre of the algebra, the complex scalars |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_2^{*}\tilde Q_1)$ | Scalar form of the dagger; Gram matrix the identity |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu}Q_{\mu}^{2}$ | Biquaternion norm; complex quadratic, indefinite |
| $\Theta_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2\tilde Q_1^{*}$ | The two-sided operator of $\tilde Q_1$; the dagger sandwich |
| $\Theta_{\tilde Q_1\tilde Q_2}=\Theta_{\tilde Q_1}\circ\Theta_{\tilde Q_2}$ | Composition law; the assignment is multiplicative |
| $\Theta_{A\tilde Q_1}=\lvert A\rvert^{2}\Theta_{\tilde Q_1}$ | Parameter rule for central $A$; blindness to the phase |
| $(\Theta_{\tilde Q_1})^{*}=\Theta_{\tilde Q_1^{*}}$ | Adjoint of a two-sided operator |
| $U=\{\tilde{Q}^{*}\tilde{Q}=e_t\}=\mathrm{U}(2)$ | The unitary slice; real dimension four |
| $\mathrm{U}(1)e_t$ | Kernel of $\tilde Q_1\mapsto\Theta_{\tilde Q_1}$ on the units; the central circle |
| $\{\tilde{Q}\tilde{Q}^{*}\}$ | The cone of positive semidefinite Hermitian elements |

## Further Reading

- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the Hermitian adjoint side by side with the other three adjoints and for the reading of the suffix of the family as the name of the adjoint
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, the four conjugations, the remarkable subspaces and the scalar form.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the quaternion norm, the invertibility criterion and the group of units, to be kept apart from the positive definite form of this article.
- [One-Sided Operators on the General Plain Sesqualgebra](one-sided-operators-on-the-general-plain-sesqualgebra.html), the companion article, where the parameter enters linearly and the sectors give skew and self-adjoint operators.
- [The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint](the-hermitian-sandwich-in-the-biquaternion-algebra-with-hermitian-adjoint.html), for the same operator in coordinates, the forms, positivity and the slice.
- [The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra](the-indefinite-hermitian-sandwich-on-the-general-quaternionic-sesqualgebra.html), for the same construction with the Krein adjoint $Q^{\dagger}=JQ^{*}J$ instead of $Q^{*}$, where the sandwich is an automorphism for every $J$-unitary parameter.
