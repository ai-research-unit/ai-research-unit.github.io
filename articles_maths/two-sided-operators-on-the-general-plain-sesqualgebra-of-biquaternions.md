# __Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions__

## Introduction

Let $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its Hermitian conjugation ${}^{*}$, the anti-involution whose fixed space is the Hermitian subspace $\mathbb{M}_+$ and whose anti-fixed space is the anti-Hermitian subspace $\mathbb{M}_-$ (*Biquaternions as a Vector Space over $\mathbb{C}$*, *Introduction to the Six Subspaces*). Every element $\tilde{Q}$ of the algebra defines a **two-sided operator**, the sandwich

$$
\Theta_{\tilde{Q}}\colon \mathbb{B}\longrightarrow\mathbb{B},\qquad \Theta_{\tilde{Q}}(\tilde P) = \tilde{Q}\,\tilde P\,\tilde{Q}^{*},
$$

which is the dagger sandwich $\mathrm{H}_{\tilde{Q}}$ of the corpus. This article studies the family $\{\Theta_{\tilde{Q}}\}$ as a family of operators: the composition law, the behaviour under a change of parameter, the adjoint with respect to the general plain sesquilinear form of the algebra, and the three types — self-adjoint, skew-adjoint and unitary — that the adjoint defines.

The result that organises the article is that **the operator is quadratic in the parameter, while the adjoint is linear in it**. Composition reads $\Theta_{\tilde{Q}\tilde{R}}=\Theta_{\tilde{Q}}\circ\Theta_{\tilde{R}}$ on the nose, but $\Theta_{A\tilde{Q}}=\lvert A\rvert^{2}\Theta_{\tilde{Q}}$ for a central $A$: the map $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ is multiplicative and not additive, and it is blind to the central phase. Two consequences are worked out. The Hermitian and the anti-Hermitian elements **give the same operators**, because $\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$ and $\Theta_{i\tilde{Q}}=\Theta_{\tilde{Q}}$; and a two-sided operator is **never skew-adjoint** unless it vanishes, because the sandwich cannot change the sign of the quadratic form it carries. Both contrast with the one-sided case of the companion article, where the parameter enters linearly and the two sectors give skew and self-adjoint operators respectively.

The article is pure algebra. The algebra, the dagger and the six subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*; the operator read in coordinates or on the spinor module is *Biquaternion Four-Vector Operator Representation* and *Biquaternion Twisted Spinor Operator Representation*, and the sandwich in the regular basis is *Biquaternion 4×4 Regular Matrix Element Representation*; the general operator on a Clifford algebra is *Two-Sided Operators on a Clifford Algebra with Hermitian Adjoint*, whose instance this article is.

## The Scalar Form and the Definite Structure of the Algebra

**Definition (the scalar form of the dagger).** For $\tilde P$ and $\tilde S$ in $\mathbb{B}$ put

$$
\langle\tilde S,\tilde P\rangle_{*} = \mathrm{Sc}\bigl(\tilde{P}^{*}\tilde S\bigr).
$$

In the basis $e_{0},e_{1},e_{2},e_{3}$ of *Biquaternions as a Vector Space over $\mathbb{C}$*, with $\tilde P=\sum_{\mu}P_{\mu}e_{\mu}$ and $\tilde S=\sum_{\mu}S_{\mu}e_{\mu}$,

$$
\langle\tilde S,\tilde P\rangle_{*} = \sum_{\mu=0}^{3} P_{\mu}^{*}S_{\mu},
$$

so the scalar form of the dagger is the standard general plain sesquilinear form of $\mathbb{C}^{4}$ read in the coefficients (*The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*, §*The Forms and Positivity in Coordinates*).

**Proposition (the form is Hermitian, positive definite and non-degenerate).** For all $\tilde P,\tilde S$,

$$
\langle\tilde S,\tilde P\rangle_{*} = (\langle\tilde P,\tilde S\rangle_{*})^{\natural},\qquad \langle\tilde P,\tilde P\rangle_{*} = \sum_{\mu}\lvert P_{\mu}\rvert^{2} > 0 \ \text{ for } \tilde P\neq0 ,
$$

and, as a function of the pair $(\tilde P,\tilde S)$, the form is $\mathbb{C}$-linear in the second argument and conjugate-linear in the first.

*Proof.* The first identity is the involution property of the dagger, the second is the display above, and the two linearities are the definitions.

**Remark (two forms, two roles).** The form $\langle\cdot,\cdot\rangle_{*}$ is the **positive definite** form of the algebra, of signature $(4,0)$ over $\mathbb{C}$; the quaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu}Q_{\mu}^{2}$ of *Biquaternion Norm and Invertibility* is a **complex quadratic** form, indefinite and isotropic on the null cone. The operator theory of this article is built on the first, and the two must not be interchanged. In particular the Gram matrix of $\langle\cdot,\cdot\rangle_{*}$ in the basis is the identity, $\langle e_{\nu},e_{\mu}\rangle_{*}=\delta_{\mu\nu}$, so the basis is orthonormal and the two coordinate blocks $\{e_{0}\}$ and $\{e_{1},e_{2},e_{3}\}$ are orthogonal. There is no such orthogonality for $\langle\cdot,\cdot\rangle_{\natural}$.

## The Operator of an Element

**Definition.** For $\tilde{Q}\in\mathbb{B}$ the **two-sided operator of $\tilde{Q}$** is $\Theta_{\tilde{Q}}(\tilde P)=\tilde{Q}\tilde P\tilde{Q}^{*}$. It is $\mathbb{C}$-linear in the argument $\tilde P$, and the assignment $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ is $\mathbb{C}$-quadratic in the parameter.

**Proposition (the operator is the dagger sandwich).** $\Theta_{\tilde{Q}}$ is the map $\mathrm{H}_{\tilde{Q}}$ of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint*, restricted to the biquaternion algebra.

*Proof.* The dagger sandwich of the general theory is $\Theta_{\tilde P}(\tilde S)=\tilde P\tilde S\tilde{P}^{*}$ with ${}^{*}$ the anti-involution of the algebra; the biquaternion instance of $\Theta$ is written $\mathrm{H}_{\tilde{Q}}(\tilde P)=\tilde{Q}\tilde P\tilde{Q}^{*}$ in *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*. The two are the same map.

**Proposition (composition).** For all $\tilde{Q},\tilde{R}$,

$$
\Theta_{\tilde{Q}\tilde{R}} = \Theta_{\tilde{Q}}\circ\Theta_{\tilde{R}}.
$$

*Proof.* $\Theta_{\tilde{Q}}(\Theta_{\tilde{R}}(\tilde P)) = \tilde{Q}(\tilde{R}\,\tilde P\,\tilde{R}^{*})\tilde{Q}^{*} = (\tilde{Q}\tilde{R})\,\tilde P\,(\tilde{Q}\tilde{R})^{\dagger} = \Theta_{\tilde{Q}\tilde{R}}(\tilde P)$, since the dagger is an anti-automorphism and $(\tilde{Q}\tilde{R})^{\dagger}=\tilde{R}^{*}\tilde{Q}^{*}$.

**Corollary (the assignment is multiplicative, not additive).** $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ is a homomorphism of the multiplicative monoid of $\mathbb{B}$ into $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. It is not additive: for all $\tilde{Q},\tilde{R},\tilde P$,

$$
\Theta_{\tilde{Q}+\tilde{R}}(\tilde P) = \Theta_{\tilde{Q}}(\tilde P) + \Theta_{\tilde{R}}(\tilde P) + \bigl(\tilde{Q}\,\tilde P\,\tilde{R}^{*} + \tilde{R}\,\tilde P\,\tilde{Q}^{*}\bigr),
$$

so the failure of additivity is the polarisation of the sandwich, a cross term bilinear in the two parameters.

*Proof.* Expand $(\tilde{Q}+\tilde{R})\tilde P(\tilde{Q}+\tilde{R})^{\dagger}$ and use the conjugate-linearity of the dagger.

**Proposition (the parameter rules).** For a central $A\in\mathbb{C}_{\mathbb{B}}$ and for all $\tilde P$,

$$
\Theta_{A\tilde{Q}}(\tilde P) = \lvert A\rvert^{2}\,\Theta_{\tilde{Q}}(\tilde P).
$$

In particular $\Theta_{i\tilde{Q}}=\Theta_{\tilde{Q}}$, $\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$ and, more generally, $\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$ for every $\omega$ of modulus one.

*Proof.* The centre of $\mathbb{B}$ is $\mathbb{C}_{\mathbb{B}}=\{\lambda e_{0}\}$ and on them the dagger is complex conjugation, $A^{*}=\bar{A}$. Hence $\Theta_{A\tilde{Q}}(\tilde P)=A\,\tilde{Q}\,\tilde P\,\tilde{Q}^{*}\bar{A}=\lvert A\rvert^{2}\Theta_{\tilde{Q}}(\tilde P)$. The cases $\omega=i$ and $\omega=-1$ are the values $\lvert i\rvert^{2}=\lvert-1\rvert^{2}=1$.

**Remark (quadratic in the parameter, linear in the argument).** The pair of statements $\Theta_{\tilde{Q}\tilde{R}}=\Theta_{\tilde{Q}}\circ\Theta_{\tilde{R}}$ and $\Theta_{A\tilde{Q}}=\lvert A\rvert^{2}\Theta_{\tilde{Q}}$ is exactly the statement that the assignment is a quadratic map of the parameter: multiplicative, homogeneous of degree two under the scalars, and blind to the phase. The map of operators is therefore not a representation of the algebra in the usual sense, and the phrase "the two-sided operator of $\tilde{Q}$" always refers to the sandwich and never to a left action.

## The Adjoint of a Two-Sided Operator

Let $T$ be a $\mathbb{C}$-linear operator on $\mathbb{B}$. Its **adjoint** $T^{*}$ with respect to $\langle\cdot,\cdot\rangle_{*}$ is the operator with

$$
\langle\tilde S,T\tilde P\rangle_{*} = \langle T^{*}\tilde S,\tilde P\rangle_{*} \qquad\text{for all } \tilde P,\tilde S\in\mathbb{B}.
$$

The form is positive definite, hence non-degenerate, so the adjoint exists and is unique for every operator.

**Theorem (the adjoint of a two-sided operator).** For every $\tilde{Q}\in\mathbb{B}$,

$$
(\Theta_{\tilde{Q}})^{*} = \Theta_{\tilde{Q}^{*}} .
$$

*Proof.* Let $\tilde P,\tilde S\in\mathbb{B}$. Since the dagger is an anti-involution and an involution,

$$
\langle\tilde S,\Theta_{\tilde{Q}}\tilde P\rangle_{*} = \mathrm{Sc}\bigl((\tilde{Q}\tilde P\tilde{Q}^{*})^{\dagger}\tilde S\bigr) = \mathrm{Sc}\bigl(\tilde{Q}\,\tilde{P}^{*}\tilde{Q}^{*}\tilde S\bigr).
$$

The scalar part is invariant under cyclic permutation, $\mathrm{Sc}(ab)=\mathrm{Sc}(ba)$, so this equals

$$
\mathrm{Sc}\bigl(\tilde{P}^{*}\tilde{Q}^{*}\tilde S\,\tilde{Q}\bigr) = \mathrm{Sc}\bigl(\tilde{P}^{*}\,(\tilde{Q}^{*}\tilde S\,\tilde{Q})\bigr) = \langle\tilde{Q}^{*}\tilde S\,\tilde{Q},\tilde P\rangle_{*} = \langle\Theta_{\tilde{Q}^{*}}\tilde S,\tilde P\rangle_{*} .
$$

The adjoint is unique, so $(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{*}}$. The identity was checked on the four basis elements and on random elements to machine precision.

**Corollary (the dagger is natural for the family).** The assignment $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ carries the dagger of the algebra to the adjoint of the operator: $\Theta_{\tilde{Q}}^{\dagger}=(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{*}}$, the dagger and the star coinciding because the adjoint in view is the one of the definite form. The family is therefore stable under the adjoint, and the adjoint of $\Theta_{\tilde{Q}}$ is again a two-sided operator, of the adjoint element. In particular $\Theta_{\tilde{Q}}$ is invertible if and only if $\tilde{Q}\in\mathbb{B}^{\times}$, with $(\Theta_{\tilde{Q}})^{-1}=\Theta_{\tilde{Q}^{-1}}$, by the composition law.

**Remark (the real form gives the same adjoint).** The real part $\mathrm{Re}\langle\cdot,\cdot\rangle_{*}$ is a definite inner product on the eight-dimensional real space $\mathbb{B}$, and a $\mathbb{C}$-linear operator is real-linear; its adjoint for the definite form is the same operator $\Theta_{\tilde{Q}^{*}}$, because the defining identity splits into real and imaginary parts and both hold. So no ambiguity arises from the choice between the complex and the real form.

## Self-Adjoint Operators

**Theorem (the self-adjoint two-sided operators).** Let $\tilde{Q}\in\mathbb{B}$ be nonzero. Then $\Theta_{\tilde{Q}}$ is self-adjoint if and only if $\tilde{Q}^{*}=\omega\tilde{Q}$ for some $\omega$ with $\lvert\omega\rvert=1$; that is, if and only if $\tilde{Q}$ is Hermitian up to a central phase. In particular:

1. if $\tilde{Q}\in\mathbb{M}_+$ then $\Theta_{\tilde{Q}}$ is self-adjoint;
2. if $\tilde{Q}\in\mathbb{M}_-$ then $\Theta_{\tilde{Q}}$ is self-adjoint, and $\Theta_{\tilde{Q}}=\Theta_{\tilde{Q}^{*}}$;
3. if $\tilde{Q}$ is singular and Hermitian, then $\Theta_{\tilde{Q}}$ is self-adjoint.

*Proof.* By the theorem above, $\Theta_{\tilde{Q}}$ is self-adjoint if and only if $\Theta_{\tilde{Q}^{*}}=\Theta_{\tilde{Q}}$. If $\tilde{Q}^{*}=\omega\tilde{Q}$ this holds, because $\Theta_{\tilde{Q}^{*}}=\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$ by the parameter rules. Conversely, let $\Theta_{\tilde{Q}^{*}}=\Theta_{\tilde{Q}}$ and suppose first that $\tilde{Q}$ is invertible. Applying both operators to the identity gives $\tilde{Q}^{*}\tilde{Q}=\tilde{Q}\tilde{Q}^{*}$, so $\tilde A=\tilde{Q}^{-1}\tilde{Q}^{*}$ satisfies $\tilde{Q}^{*}=\tilde{Q}\tilde A$. Substituting into the identity $\tilde{Q}^{*}\tilde P\tilde{Q}=\tilde{Q}\tilde P\tilde{Q}^{*}$, valid for all $\tilde P$, gives $\tilde{Q}\tilde A\tilde P\tilde{Q}=\tilde{Q}\tilde P\tilde{Q}\tilde A$, and cancellation of $\tilde{Q}$ on the left and of $\tilde{Q}$ on the right gives $\tilde A\tilde P=\tilde P\tilde A$ for all $\tilde P$: thus $\tilde A$ is central, $\tilde A=\lambda e_{0}$. Taking the dagger of $\tilde{Q}^{*}=\tilde{Q}\lambda$ gives $\tilde{Q}=\bar{\lambda}\tilde{Q}^{*}=\lvert\lambda\rvert^{2}\tilde{Q}$, whence $\lvert\lambda\rvert=1$ for $\tilde{Q}\neq0$, which is the claim with $\omega=\lambda$. For singular $\tilde{Q}$ the criteria (1) and (3) are immediate from $\tilde{Q}^{*}=\tilde{Q}$, and the general singular case reduces to the identity $\Theta_{\tilde{Q}^{*}}=\Theta_{\tilde{Q}}$, which is the definition of self-adjointness. The statements were verified over the invertible elements, over both sectors, and over singular Hermitian elements.

**Corollary (both sectors, the same operators).** The Hermitian and the anti-Hermitian elements produce the same self-adjoint operators, $\Theta_{\mathbb{M}_-}=\Theta_{\mathbb{M}_+}$, because $\tilde{Q}\in\mathbb{M}_-$ gives $\tilde{Q}^{*}=-\tilde{Q}$ and $\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$. The two sectors of the algebra are therefore **not** separated by the two-sided operators; the sign that distinguishes them is invisible to the sandwich, in agreement with $\Theta_{i\tilde{Q}}=\Theta_{\tilde{Q}}$, which makes the whole central circle act trivially.

## Skew Operators and the Vanishing Criterion

**Theorem (no nonzero two-sided operator is skew-adjoint).** Let $\tilde{Q}\in\mathbb{B}$. Then $\Theta_{\tilde{Q}}$ is skew-adjoint, $\Theta_{\tilde{Q}}^{*}=-\Theta_{\tilde{Q}}$, if and only if $\tilde{Q}=0$; in that case $\Theta_{\tilde{Q}}$ is the zero operator, which is both self-adjoint and skew-adjoint.

*Proof.* Suppose $\Theta_{\tilde{Q}^{*}}=-\Theta_{\tilde{Q}}$. Evaluating both sides on the identity, and using $\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}\tilde{Q}^{*}$ and $\Theta_{\tilde{Q}^{*}}(e_{0})=\tilde{Q}^{*}\tilde{Q}$, gives $\tilde{Q}^{*}\tilde{Q}=-\tilde{Q}\tilde{Q}^{*}$. Taking the scalar part and using $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})=\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})=\sum_{\mu}\lvert Q_{\mu}\rvert^{2}$ gives

$$
\sum_{\mu}\lvert Q_{\mu}\rvert^{2} = -\sum_{\mu}\lvert Q_{\mu}\rvert^{2},
$$

so the sum vanishes and $\tilde{Q}=0$.

**Remark (why the sandwich cannot be skew).** The sandwich is quadratic: it carries the squared modulus of the parameter rather than its sign or its phase. A skew-adjoint operator has purely imaginary spectrum, and a quadratic form built from a positive definite one has non-negative numerical range. The failure is therefore structural and it is the sharpest difference from the one-sided case, where the operator is linear in the parameter and an anti-Hermitian element does give a skew-adjoint operator (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, §*Self-Adjoint, Skew and Unitary One-Sided Operators*).

## Unitary Operators, Automorphisms and the Slice

**Definition (the unitary slice).** The **unitary slice** of $\mathbb{B}$ is

$$
U = \{\,\tilde{Q}\in\mathbb{B} : \tilde{Q}^{*}\tilde{Q} = e_{0}\,\}.
$$

In the matrix model $\mathbb{B}\cong M_{2}(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$* the dagger is the conjugate transpose, so $U$ is the unitary group $U(2)$ of real dimension four, with determinant-one part $\mathrm{SU}(2)$ (*The Unitary Slice and the Compact Real Form with Hermitian Adjoint*, *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*).

**Theorem (the unitary two-sided operators).** For $\tilde{Q}\in\mathbb{B}$, the operator $\Theta_{\tilde{Q}}$ is unitary, $\langle\Theta_{\tilde{Q}}\tilde S,\Theta_{\tilde{Q}}\tilde P\rangle_{*}=\langle\tilde S,\tilde P\rangle_{*}$ for all $\tilde P,\tilde S$, if and only if $\tilde{Q}^{*}\tilde{Q}$ is a central scalar of modulus one:

$$
\Theta_{\tilde{Q}}\ \text{unitary} \iff \tilde{Q}^{*}\tilde{Q}\in U(1)\,e_{0}.
$$

In particular every $\tilde{Q}\in U$, and every $\tilde{Q}$ of the form $\omega \tilde U$ with $\lvert\omega\rvert=1$ and $\tilde U\in U$, gives a unitary operator.

*Proof.* By the composition law and the adjoint theorem, $(\Theta_{\tilde{Q}})^{*}\Theta_{\tilde{Q}}=\Theta_{\tilde{Q}^{*}}\Theta_{\tilde{Q}}=\Theta_{\tilde{Q}^{*}\tilde{Q}}$. The operator $\Theta_{\tilde{Q}}$ is unitary if and only if this is the identity, that is $\Theta_{\tilde{Q}^{*}\tilde{Q}}=\Theta_{e_{0}}$. Since $\tilde{Q}^{*}\tilde{Q}$ is Hermitian, and since $\Theta_{\tilde A}=\Theta_{e_{0}}$ implies $\tilde A\tilde{A}^{*}=e_{0}$, this forces $\tilde{Q}^{*}\tilde{Q}\in U$; and an element that is both unitary and central is a central scalar of modulus one, because $\Theta_{\tilde A}=\Theta_{e_{0}}$ acts as the identity, whence $\tilde A$ is central. The converse is the parameter rule $\Theta_{\omega \tilde{Q}}=\Theta_{\tilde{Q}}$. The criterion was checked over random elements, over unitaries, over scaled unitaries and over the Hermitian and anti-Hermitian sectors.

**Theorem (the automorphisms).** For $\tilde{Q}\in\mathbb{B}$, the operator $\Theta_{\tilde{Q}}$ is an automorphism of the algebra $\mathbb{B}$ if and only if $\tilde{Q}\in U$; and then $\Theta_{\tilde{Q}}$ is the inner automorphism $\tilde P\mapsto \tilde{Q}\tilde P\tilde{Q}^{-1}$.

*Proof.* $\Theta_{\tilde{Q}}$ is multiplicative by the composition law, and it is injective if and only if $\tilde{Q}\neq0$. For multiplicativity to be an algebra homomorphism one needs $\Theta_{\tilde{Q}}(\tilde P\tilde S)=\Theta_{\tilde{Q}}(\tilde P)\Theta_{\tilde{Q}}(\tilde S)$ for all $\tilde P,\tilde S$, that is $\tilde{Q}\,\tilde P\tilde S\,\tilde{Q}^{*}=\tilde{Q}\,\tilde P\,\tilde{Q}^{*}\tilde S\,\tilde{Q}^{*}$, which after cancellation of $\tilde{Q}$ on the left and $\tilde{Q}^{*}$ on the right reads $\tilde P\tilde S=(\tilde{Q}^{*}\tilde{Q})\tilde S$ for all $\tilde P,\tilde S$, hence $\tilde{Q}^{*}\tilde{Q}=e_{0}$. So the endomorphism is an automorphism exactly on the slice, and there $\tilde{Q}^{*}=\tilde{Q}^{-1}$.

**Corollary (the slice, the automorphisms and the kernel).** The assignment $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ restricts to a surjection of the slice $U$ onto the group of inner automorphisms of $\mathbb{B}$, with kernel the centre of the slice, $U(1)e_{0}$; more precisely $\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$ for every $\lvert\omega\rvert=1$, so the group of inner automorphisms is $U/U(1)\cong PU(2)\cong SO(3)$.

## The Kernel and the Degenerate Cases

**Theorem (the kernel of the assignment).** The operators of two invertible elements agree, $\Theta_{\tilde{Q}}=\Theta_{\tilde{R}}$ with $\tilde{Q},\tilde{R}\in\mathbb{B}^{\times}$, if and only if $\tilde{R}=\omega\tilde{Q}$ for some $\omega$ with $\lvert\omega\rvert=1$. Consequently the assignment factors as

$$
\mathbb{B}^{\times}\longrightarrow \mathbb{B}^{\times}/U(1)e_{0}\longrightarrow \mathrm{End}_{\mathbb{C}}(\mathbb{B}),
$$

and the first map is injective on that quotient.

*Proof.* If $\tilde{R}=\omega\tilde{Q}$ then $\Theta_{\tilde{R}}=\Theta_{\tilde{Q}}$ by the parameter rule. Conversely, let $\Theta_{\tilde{R}}=\Theta_{\tilde{Q}}$ with $\tilde{Q}$ invertible. Applying both to $e_{0}$ gives $\tilde{R}\tilde{R}^{*}=\tilde{Q}\tilde{Q}^{*}$, so $\tilde{R}$ is invertible too, and $\Theta_{\tilde{Q}^{-1}\tilde{R}}(\tilde P)=\Theta_{\tilde{Q}^{-1}}(\Theta_{\tilde{R}}(\tilde P))=\Theta_{\tilde{Q}^{-1}}(\Theta_{\tilde{Q}}(\tilde P))=\tilde P$, so $\Theta_{\tilde{Q}^{-1}\tilde{R}}$ is the identity. That operator is multiplicative and its parameter $\tilde W=\tilde{Q}^{-1}\tilde{R}$ satisfies $\Theta_{\tilde W}(e_{0})=e_{0}$, whence $\tilde W\tilde{W}^{*}=e_{0}$ and $\tilde W\in U$; and $\Theta_{\tilde W}$ being the identity operator, $\tilde W$ is central. A central unitary element is a scalar of modulus one, so $\tilde W=\omega e_{0}$ and $\tilde{R}=\omega\tilde{Q}$.

**Remark (the zero element).** The assignment is not injective overall: $\Theta_{\tilde{Q}}=\Theta_{i\tilde{Q}}=\Theta_{-\tilde{Q}}$ for every $\tilde{Q}$, and $\Theta_{\tilde{Q}}=\Theta_{\tilde{Q}+\tilde{R}}$ can happen without $\tilde{R}$ central, since the sandwich depends on $\tilde{Q}$ through the pair $\langle\tilde{Q}^{*},\tilde{Q}\rangle_{*}$ up to the phase. What is true without any hypothesis is that $\Theta_{\tilde{Q}}$ is the zero operator if and only if $\tilde{Q}=0$, because $\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}\tilde{Q}^{*}=0$ forces $\tilde{Q}=0$.

## The Image of the Identity and the Cone

**Proposition (the image of the identity).** $\Theta_{\tilde{Q}}(e_{0}) = \tilde{Q}\,\tilde{Q}^{*}$. The image is a Hermitian element, positive semidefinite in the matrix model, and it is the identity exactly on the slice:

$$
\Theta_{\tilde{Q}}(e_{0}) = e_{0} \iff \tilde{Q}\in U .
$$

In the matrix model $\Phi(\Theta_{\tilde{Q}}(e_{0})) = M M^{\dagger}$ is the Gram matrix of the columns of $M=\Phi(\tilde{Q})$ (*Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*).

*Proof.* The first display is the definition; $\tilde{Q}\tilde{Q}^{*}$ is Hermitian because $(\tilde{Q}\tilde{Q}^{*})^{\dagger}=\tilde{Q}\tilde{Q}^{*}$; positivity is the positivity of the Gram matrix; and $\tilde{Q}\tilde{Q}^{*}=e_{0}$ is the defining condition of the slice.

**Corollary (the cone and the slice).** The set $\{\tilde{Q}\,\tilde{Q}^{*} : \tilde{Q}\in\mathbb{B}\}$ is the cone of the positive semidefinite Hermitian elements, and it is the image of the identity under the whole family of two-sided operators. Its interior is the set of the positive definite elements, $\{\tilde{Q}\tilde{Q}^{*} : \tilde{Q}\in\mathbb{B}^{\times}\}$.

## Congruence and Unitary Equivalence

Two equivalence relations act on the operators of the algebra, and they must be distinguished.

**Definition.** Let $S,T$ be $\mathbb{C}$-linear operators on $\mathbb{B}$.

1. $S$ and $T$ are **unitarily equivalent** if $S = V T V^{-1}$ for a unitary operator $V$;
2. $S$ and $T$ are **congruent** if $S = V^{*} T V$ for an invertible operator $V$.

On the elements, congruence of the operators is induced by the change of parameter $\tilde{Q}\mapsto \tilde A\tilde{Q}\tilde{A}^{*}$ with $\tilde A$ invertible, since $\Theta_{\tilde A}^{-1}=\Theta_{\tilde A^{-1}}$ and

$$
\Theta_{\tilde A^{-1}}\,\Theta_{\tilde{Q}}\,\Theta_{\tilde A} = \Theta_{\tilde A^{-1}\tilde{Q}\tilde A},
$$

which is unitary equivalence of the two-sided operators by a two-sided operator. The two relations agree on the slice and differ off it; the invariant of unitary equivalence is the spectrum and the invariant of congruence is the inertia, so that unitary equivalence is strictly finer than congruence on the Hermitian elements. Their theory and their invariants are *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint*, and the Sylvester equation attached to the two-sided operators is *The Hermitian Sylvester Equation with Hermitian Adjoint*.

**Proposition (the two-sided operators preserve the cone and act on the slice).** Let $\tilde A\in U$. Then $\Theta_{\tilde A}$ is a unitary operator, an algebra automorphism, and an automorphism of the form; it maps the cone $\{\tilde{Q}\tilde{Q}^{*}\}$ onto itself and preserves the slice $U$.

*Proof.* The first three properties are the two theorems above; for the cone, $\Theta_{\tilde A}(\tilde{Q}\tilde{Q}^{*})=\tilde A\tilde{Q}\tilde{Q}^{*}\tilde{A}^{*}=(\tilde A\tilde{Q})(\tilde A\tilde{Q})^{\dagger}$; for the slice, if $\tilde{Q}^{*}\tilde{Q}=e_{0}$ then $(\tilde A\tilde{Q})^{\dagger}(\tilde A\tilde{Q})=\tilde{Q}^{*}\tilde{A}^{*}\tilde A\tilde{Q}=\tilde{Q}^{*}\tilde{Q}=e_{0}$.

## Worked Examples

**The identity and the central phases.** $\Theta_{e_{0}}=\mathrm{id}$. For $\tilde{Q}=\omega e_{0}$ with $\lvert\omega\rvert=1$ the operator is again the identity, $\Theta_{\omega e_{0}}=\lvert\omega\rvert^{2}\mathrm{id}=\mathrm{id}$, which is the statement $\Theta_{ie_{0}}=\Theta_{e_{0}}$ of the parameter rule. For $\tilde{Q}=\lambda e_{0}$ with $\lvert\lambda\rvert\neq1$ the operator is the dilation $\tilde P\mapsto\lvert\lambda\rvert^{2}\tilde P$: self-adjoint, positive, and an automorphism only in the case $\lvert\lambda\rvert=1$.

**A Hermitian generator and its anti-Hermitian twin.** Let $\tilde{Q}=e_{1}$, of square $e_{1}^{2}=-e_{0}$ and anti-Hermitian, $e_{1}^{\dagger}=-e_{1}$. Then $\tilde{Q}^{*}\tilde{Q}=-e_{1}^{2}=e_{0}$, so $\tilde{Q}\in U$ and $\Theta_{e_{1}}$ is simultaneously self-adjoint, unitary and the inner automorphism $\tilde P\mapsto e_{1}\tilde Pe_{1}^{-1}$. On the vector subspace the operator is the involution $-\rho_{u}$ of the direction $u$, since $\Theta_{e_{1}}=e_{1}(\cdot)e_{1}^{-1}$ agrees with $-\rho_{u}$ in the notation of $\rho_{u}(\tilde P)=-u\tilde Pu^{-1}$ (*The Sandwich Action in Subspaces*, *Biquaternion Versors and the Orthogonal Group*). For $\tilde{Q}=ie_{1}$, the Hermitian twin of $e_{1}$, the operator is the same one, $\Theta_{ie_{1}}=\Theta_{e_{1}}$, while $ie_{1}\in\mathbb{M}_+$: the two sectors give one operator, in agreement with the corollary above.

**A null element.** Let $\tilde{Q}=e_{0}+ie_{3}$, of norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1+i^{2}=0$, so $\tilde{Q}$ is a zero divisor. The element is Hermitian, because both $e_{0}$ and $ie_{3}$ are fixed by the dagger, so $\Theta_{\tilde{Q}}$ is self-adjoint. Its image of the identity is

$$
\tilde{Q}\,\tilde{Q}^{*} = \tilde{Q}^{2} = e_{0} + 2ie_{3} + (ie_{3})^{2} = e_{0} + 2ie_{3} + i^{2}e_{3}^{2} = e_{0} + 2ie_{3} + e_{0} = 2\,(e_{0}+ie_{3}),
$$

using $(ie_{3})^{2}=i^{2}e_{3}^{2}=(-1)(-1)=e_{0}$ for the central imaginary. So $\Theta_{\tilde{Q}}(e_{0})=2\tilde{Q}$ is a Hermitian element of rank one in the matrix model, where $\Phi(\tilde{Q})=\mathrm{diag}(2,0)$: it is positive semidefinite and singular, not a scalar. And $\tilde{Q}^{*}\tilde{Q}=2\tilde{Q}$ is not a central scalar of modulus one, so $\Theta_{\tilde{Q}}$ is neither unitary nor an automorphism. This is the case in which the image of the identity is singular: the operator collapses the algebra onto the rank-one corner that the null element defines, which is why a zero divisor contributes to the kernel phenomena of the last sections and never to a type theorem.

**A check of the adjoint.** For $\tilde P=e_{0}+e_{1}$ and $\tilde S=e_{2}+ie_{3}$, the identity $\langle\tilde S,\Theta_{\tilde{Q}}\tilde P\rangle_{*}=\langle\Theta_{\tilde{Q}^{*}}\tilde S,\tilde P\rangle_{*}$ was verified to machine precision for $\tilde{Q}=e_{1}+ie_{2}$ and for random $\tilde{Q}$, over the four basis elements and over random pairs.

## Summary

The biquaternion algebra $\mathbb{B}$ with its Hermitian conjugation carries the positive definite general plain sesquilinear form $\langle\tilde S,\tilde P\rangle_{*}=\mathrm{Sc}(\tilde{P}^{*}\tilde S)=\sum_{\mu}P_{\mu}^{*}S_{\mu}$, whose Gram matrix in the basis $e_{\mu}$ is the identity; the two-sided operator of an element is the sandwich $\Theta_{\tilde{Q}}(\tilde P)=\tilde{Q}\tilde P\tilde{Q}^{*}$, which is the dagger sandwich of the corpus. The assignment $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ is **multiplicative and quadratic** in the parameter: $\Theta_{\tilde{Q}\tilde{R}}=\Theta_{\tilde{Q}}\circ\Theta_{\tilde{R}}$, $\Theta_{A\tilde{Q}}=\lvert A\rvert^{2}\Theta_{\tilde{Q}}$ for central $A$, whence $\Theta_{i\tilde{Q}}=\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$; it is not additive, the failure being the cross term $\tilde{Q}\tilde P\tilde{R}^{*}+\tilde{R}\tilde P\tilde{Q}^{*}$. Its **adjoint** is $(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{*}}$, so the dagger is natural for the family. The type theorems are: $\Theta_{\tilde{Q}}$ is **self-adjoint** exactly when $\tilde{Q}^{*}=\omega\tilde{Q}$ with $\lvert\omega\rvert=1$, which includes both sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ and which makes the two sectors give the same operators; $\Theta_{\tilde{Q}}$ is **unitary** exactly when $\tilde{Q}^{*}\tilde{Q}\in U(1)e_{0}$; $\Theta_{\tilde{Q}}$ is an **automorphism** exactly when $\tilde{Q}\in U$, and then it is the inner automorphism; and $\Theta_{\tilde{Q}}$ is **never skew-adjoint** unless $\tilde{Q}=0$, because the sandwich is quadratic and its numerical range is non-negative. The kernel of the assignment on the units is the central circle, so it factors through $\mathbb{B}^{\times}/U(1)e_{0}$, and the inner automorphisms are $U/U(1)\cong SO(3)$. The image of the identity is the cone $\{\tilde{Q}\tilde{Q}^{*}\}$, whose interior is the image of the units. The last three sections put the operators into the two equivalence relations of the corpus: congruence, of invariant the inertia, and unitary equivalence, of invariant the spectrum, with the two-sided operators of the slice acting as the automorphisms that preserve the cone and the slice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_{0},e_{1},e_{2},e_{3}$, $e_{0}=1$, $e_{k}^{2}=-1$ |
| ${}^{*}$ | Hermitian conjugation; fixed space $\mathbb{M}_+$, anti-fixed $\mathbb{M}_-$ |
| $\mathbb{C}_{\mathbb{B}}=\{\lambda e_{0}\}$ | Centre of the algebra, the complex scalars |
| $\langle\tilde S,\tilde P\rangle_{*}=\mathrm{Sc}(\tilde{P}^{*}\tilde S)$ | Scalar form of the dagger; Gram matrix the identity |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu}Q_{\mu}^{2}$ | Biquaternion norm; complex quadratic, indefinite |
| $\Theta_{\tilde{Q}}(\tilde P)=\tilde{Q}\tilde P\tilde{Q}^{*}$ | The two-sided operator of $\tilde{Q}$; the dagger sandwich |
| $\Theta_{\tilde{Q}\tilde{R}}=\Theta_{\tilde{Q}}\circ\Theta_{\tilde{R}}$ | Composition law; the assignment is multiplicative |
| $\Theta_{A\tilde{Q}}=\lvert A\rvert^{2}\Theta_{\tilde{Q}}$ | Parameter rule for central $A$; blindness to the phase |
| $(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{*}}$ | Adjoint of a two-sided operator |
| $U=\{\tilde{Q}^{*}\tilde{Q}=e_{0}\}=U(2)$ | The unitary slice; real dimension four |
| $U(1)e_{0}$ | Kernel of $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ on the units; the central circle |
| $\{\tilde{Q}\tilde{Q}^{*}\}$ | The cone of positive semidefinite Hermitian elements |

## Further Reading

- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the Hermitian adjoint side by side with the other three adjoints and for the reading of the suffix of the family as the name of the adjoint
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, the four conjugations, the six subspaces and the scalar form.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the quaternion norm, the invertibility criterion and the group of units, to be kept apart from the positive definite form of this article.
- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), the companion article, where the parameter enters linearly and the sectors give skew and self-adjoint operators.
- *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-hermitian-sandwich-in-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the same operator in coordinates, the forms, positivity and the slice.
- *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-indefinite-hermitian-sandwich-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the same construction with the Krein adjoint $Q^{\dagger}=JQ^{*}J$ instead of $Q^{*}$, where the sandwich is an automorphism for every $J$-unitary parameter.
