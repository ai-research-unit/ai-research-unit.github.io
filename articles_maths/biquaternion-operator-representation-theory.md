# __Biquaternion Operator Representation Theory__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$, with $e_k^2 = -e_0$ and $e_j e_k = -e_k e_j$ for $j \neq k$, and a central scalar imaginary $i$ satisfying $i^2 = -1$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The algebra, its conjugations, its six distinguished subspaces and its biquaternion norm $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ are those of *Biquaternion Algebra* and *Biquaternion Norm and Invertibility*.

Two different things can be done with an element, and the corpus keeps them apart.

The element can be used as an **element**. It is then an object: it has four complex coordinates, it has a norm, it lies in a cone or it does not, and the question asked about it is *what it is*. Every article of the group *Focus on Element Representations* answers that question in a different coordinate system — the four coefficients, the $2 \times 2$ matrix, the $4 \times 4$ regular matrix, the polar word.

The element can also be used as an **operator**. It is then a rule: it takes an element and returns an element, and the question asked about it is *what it does*. This article and its companions treat that use. The operator of an element is the **Hermitian sandwich**

$$
\mathrm{H}_{\tilde{Q}} : \mathbb{B} \longrightarrow \mathbb{B}, \qquad \mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}\, x\, \tilde{Q}^{\dagger},
$$

and the point of the whole group is that this rule is *linear*: it is therefore an element of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}) \cong M_4(\mathbb{C})$, it has a matrix, a determinant, a trace, a rank and a spectrum, and all of those are computable from $\tilde{Q}$ alone.

This article fixes the operator and its laws, reads the polar factors through it, and separates the two regimes — the operator of an element *outside* the null cone, which is invertible, and the operator of an element *on* it, which collapses. Every statement below is a statement about $\tilde{Q}$ and the algebraic operations alone, so each holds in every coordinate system the algebra admits; the writing of the operator in the four coefficients, in the coefficient column, in the matrix algebra and on the module is taken up in turn by the other articles of this section.

**Conventions.** The matrix realization is $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation*, fixed by $\Phi(e_k) = -i\sigma_k$ and $\Phi(i) = iI_2$, so that $\det \Phi(\tilde{Q}) = N(\tilde{Q})$ and $\mathrm{Tr}\,\Phi(\tilde{Q}) = 2Q_0$. The polar form, its four factors and its domain are *Biquaternion Polar Element Representation*. The geometric content of the sandwich — the Lorentz action, the orbits, the invariant subspaces and the reflections — belongs to *Biquaternion Rotations and Lorentz Transformations* and is cited, not restated. The group of units is $\mathbb{B}^{\times} \cong GL(2,\mathbb{C})$, the unit-norm slice is $\mathbb{B}^{\times}_1 \cong SL(2,\mathbb{C})$, and the two sectors are the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

## The Hermitian Sandwich

**Definition.** Let $\tilde{Q} \in \mathbb{B}$. The **sandwich** of $\tilde{Q}$ is the map $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$. The element $\tilde{Q}$ is the **operand**, and $x$ is the **argument**.

The word *Hermitian* names the second factor. The involution $\dagger$ is the composite of quaternion conjugation with complex conjugation; it is conjugate-linear, it is an anti-automorphism, $(xy)^{\dagger} = y^{\dagger}x^{\dagger}$, and it splits the algebra into its fixed space $\mathbb{M}_+$ and its anti-fixed space $\mathbb{M}_-$.

**Why the dagger and not the inverse.** Two-sided maps $x \mapsto AxB$ with $A, B$ invertible are the general maps built from an element on both sides. Among them, the ones that carry the fixed space of an involution into itself are exactly the ones whose two factors are matched by that involution. For the dagger,

$$
(AxB)^{\dagger} = B^{\dagger}x^{\dagger}A^{\dagger},
$$

so if $A = \tilde{Q}$ and $B = \lambda\tilde{Q}^{\dagger}$ for a real $\lambda$, then $B^{\dagger} = \lambda\tilde{Q}$ and the image of a Hermitian $x$ is $\lambda\tilde{Q}x\tilde{Q}^{\dagger}$, again Hermitian. A sandwich built from the *inverse* instead, $x \mapsto \tilde{Q}x\tilde{Q}^{-1}$, is the inner automorphism, and it preserves the fixed spaces of the involution conjugated by the image of the identity, $z \mapsto \tilde{Q}\tilde{Q}^{\dagger}z^{\dagger}(\tilde{Q}\tilde{Q}^{\dagger})^{-1}$, which is a different involution as soon as $\tilde{Q}$ is not unitary. The dagger sandwich with $\lambda = 1$ is the normalised choice, and it is the one the corpus uses.

The two involutions are not a curiosity. The inner automorphism acts by the same formula on the algebra and is a genuine algebra automorphism, while the dagger sandwich is linear but not multiplicative; the full comparison is *Biquaternion Other Algebraic Element Representations*, and the infinitesimal versions are *Biquaternion Automorphisms and Derivations*.

## The Laws of the Operator

Three identities govern the sandwich, and they are the whole of its algebra.

**Proposition (composition).** For all $\tilde{Q}, \tilde{R} \in \mathbb{B}$,

$$
\mathrm{H}_{\tilde{Q}\tilde{R}} = \mathrm{H}_{\tilde{Q}} \circ \mathrm{H}_{\tilde{R}} .
$$

**Proof.** $\mathrm{H}_{\tilde{Q}}(\mathrm{H}_{\tilde{R}}(x)) = \tilde{Q}(\tilde{R}x\tilde{R}^{\dagger})\tilde{Q}^{\dagger} = (\tilde{Q}\tilde{R})x(\tilde{Q}\tilde{R})^{\dagger} = \mathrm{H}_{\tilde{Q}\tilde{R}}(x)$, using the anti-automorphism property $(\tilde{Q}\tilde{R})^{\dagger} = \tilde{R}^{\dagger}\tilde{Q}^{\dagger}$. $\square$

Consequently $\tilde{Q} \mapsto \mathrm{H}_{\tilde{Q}}$ is a homomorphism of the multiplicative monoid of $\mathbb{B}$ into the linear maps of $\mathbb{B}$, and of the group of units into $GL(\mathbb{B}) \cong GL(4,\mathbb{C})$.

**Proposition (the central rule).** For every central $z$ and every $x$,

$$
\mathrm{H}_{z\tilde{Q}}(x) = |z|^{2}\,\mathrm{H}_{\tilde{Q}}(x) .
$$

**Proof.** A central element commutes with everything and $z^{\dagger} = \bar{z}$, so $\mathrm{H}_{z\tilde{Q}}(x) = z\tilde{Q}x\tilde{Q}^{\dagger}\bar{z} = |z|^{2}\mathrm{H}_{\tilde{Q}}(x)$. $\square$

Two readings follow. The second, the phase, is the sharp one: taking $z = e^{i\theta}$ gives $\mathrm{H}_{e^{i\theta}\tilde{Q}} = \mathrm{H}_{\tilde{Q}}$, so **the sandwich is blind to the scalar imaginary** — the operator of $i\tilde{Q}$ is the operator of $\tilde{Q}$. The first, the scale, is a genuine dilatation of the operator by $|z|^{2}$.

**Proposition (the kernel).** $\mathrm{H}_{\tilde{Q}}$ is the identity exactly when $\tilde{Q} = e^{i\theta}e_0$ for some real $\theta$.

**Proof.** If $\mathrm{H}_{\tilde{Q}} = \mathrm{id}$, then $x = e_0$ gives $\tilde{Q}\tilde{Q}^{\dagger} = e_0$, so $\tilde{Q}$ is unitary, and an arbitrary $x$ gives $\tilde{Q}x = x\tilde{Q}$, so $\tilde{Q}$ is central; a central unitary of $\mathbb{B}$ is $e^{i\theta}e_0$. Conversely such an element acts trivially. The detail is in *Biquaternion Rotations and Lorentz Transformations*. $\square$

The kernel is therefore the circle $U(1)$ of central phases, of one real dimension, and it is the operator group that loses exactly the phase: $\tilde{Q}$ and $e^{i\theta}\tilde{Q}$ define the same operator and nothing else does.

**Proposition (the image of the identity).** $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{\dagger}$, which is Hermitian and, for a general unit, not central and not a scalar.

This single evaluation is the reason the sandwich does not preserve the four subspaces of the scalar–vector decomposition: the centre is not preserved, and neither is the vector subspace.

## The Operator Is Not an Automorphism

A sandwich is built from two factors, and the insertion needed to make it multiplicative is exactly the defect.

For general $x, y$,

$$
\tilde{Q}xy\tilde{Q}^{\dagger} \neq (\tilde{Q}x\tilde{Q}^{\dagger})(\tilde{Q}y\tilde{Q}^{\dagger}),
$$

the two sides differing by the element $\tilde{Q}^{\dagger}\tilde{Q}$ inserted between $x$ and $y$. Since $\tilde{Q}^{\dagger}\tilde{Q} = e_0$ exactly when $\tilde{Q}$ is unitary, the sandwich is an algebra homomorphism precisely on the unitary slice, and there it is the conjugation $x \mapsto \tilde{Q}x\tilde{Q}^{-1}$, which is an inner automorphism.

The sandwich is therefore a **linear action of the group of units on the algebra**, not an action by automorphisms. That is the precise sense in which the operator point of view is wider than the automorphism point of view, and the two agree on the unitary elements.

## The Polar Factors as Operators

Off the null cone an element has the polar word $\tilde{Q} = r e^{i\alpha} B\hat{q}$, a positive scale $r$, a central phase $e^{i\alpha}$, a Hermitian positive boost $B$ and a unit real quaternion rotor $\hat{q}$ (*Biquaternion Polar Element Representation*). The sandwich reads those four factors with a definite pattern.

**Proposition (the factorisation of the operator).** Let $\tilde{Q} = r e^{i\alpha}B\hat{q}$ with $N(\tilde{Q}) \neq 0$, and put $\tilde{\Lambda} = B\hat{q}$, of unit norm. Then

$$
\mathrm{H}_{\tilde{Q}} = r^{2}\,\mathrm{H}_{\tilde{\Lambda}} ,
\qquad\text{and}\qquad
N\bigl(\mathrm{H}_{\tilde{Q}}(x)\bigr) = \lvert N(\tilde{Q})\rvert^{2}N(x) = r^{4}N(x) .
$$

**Proof.** The Hermitian conjugates of the factors are $\hat{q}^{\dagger} = \hat{q}^{-1}$, $B^{\dagger} = B$, $r^{\dagger} = r$ and $(e^{i\alpha})^{\dagger} = e^{-i\alpha}$, so

$$
\mathrm{H}_{\tilde{Q}}(x) = r e^{i\alpha}B\hat{q}\;x\;\hat{q}^{-1}Br e^{-i\alpha} = r^{2}B\bigl(\hat{q}x\hat{q}^{-1}\bigr)B = r^{2}\tilde{\Lambda}x\tilde{\Lambda}^{\dagger},
$$

the two central factors cancelling against their inverses. The norm statement follows from the multiplicativity of $N$ and from $N(\tilde{Q}^{\dagger}) = N(\tilde{Q})^{*}$. $\square$

| polar factor | range | as an operator on the algebra |
|---|---|---|
| scale $r$ | $(0,\infty)$ | dilatation by $r^{2}$, the factor counted twice |
| phase $e^{i\alpha}$ | $U(1)$ | none; it cancels and lies in the kernel |
| boost $B$ | rapidity $\psi$, axis $\hat{\mathbf{n}}$ | boost of the **doubled** rapidity |
| rotor $\hat{q}$ | angle $\theta$ | rotation by the **doubled** angle |

The pattern is forced by the bilinearity. A non-central factor occurs once on each side, so its parameter is deposited twice; a central factor occurs on both sides and cancels. The exact diagonal case is

$$
\Phi(B) = \mathrm{diag}\bigl(e^{\psi/2}, e^{-\psi/2}\bigr)
\quad\Longrightarrow\quad
\Phi(B)\,X\,\Phi(B) = \mathrm{diag}\bigl(e^{\psi}, e^{-\psi}\bigr)X ,
$$

in which the operator stores the half-rapidity and produces the rapidity. The same doubling holds for the rotation angle, and it is the geometric origin of the double cover $SL(2,\mathbb{C}) \to SO^{+}(1,3)$, where *Biquaternion Rotations and Lorentz Transformations* reads it as the two-to-one rotor map. The module side of the same statement is that the sandwich acts on the simple module through the element itself, so its stored half-parameters are the ones the module sees.

**Corollary (the image of the operator group).** As $\tilde{Q}$ runs over the units with a fixed norm, the sandwich runs over the Lorentz group; as it runs over all units, it runs over $\mathbb{R}_{>0} \times SO^{+}(1,3)$, the dilatations together with the Lorentz transformations, and no phase appears.

**Proposition (the invariants of the operator).** For every $\tilde{Q}$,

$$
\det \mathrm{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}, \qquad \operatorname{Tr}\mathrm{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2} ,
$$

both real and non-negative.

**Proof.** Under $\Phi$ the operator is the endomorphism $T(X) = M X M^{\dagger}$ of $M_2(\mathbb{C})$ with $M = \Phi(\tilde{Q})$. In the basis of matrix units $E_{ij}$ its entries are $T_{(ij),(kl)} = M_{ik}\bar{M}_{jl}$, so $T$ is the Kronecker product $M \otimes \bar{M}$: indeed $(M \otimes \bar M)_{(ij),(kl)} = M_{ik}\bar M_{jl}$. The trace of a Kronecker product is the product of the traces and its determinant is $\det(M \otimes \bar M) = (\det M)^{2}(\det \bar M)^{2}$; hence

$$
\operatorname{Tr} T = (\operatorname{Tr} M)(\operatorname{Tr}\bar{M}) = \lvert\operatorname{Tr} M\rvert^{2} = \lvert 2Q_0\rvert^{2} = 4\lvert Q_0\rvert^{2},
\qquad
\det T = \bigl(\det M \cdot \det \bar M\bigr)^{2} = \lvert N(\tilde{Q})\rvert^{4} ,
$$

using $\det M = N(\tilde{Q})$ and $\operatorname{Tr} M = 2Q_0$ of *Biquaternion 2×2 Matrix Element Representation*. Both are real and non-negative. $\square$

The two numbers are the operator's own, and they are **not** the invariants of the element matrix: the element $\Phi(\tilde{Q})$ has determinant $N(\tilde{Q})$, which is complex, and trace $2Q_0$. The operator has discarded the phase, and what survives is a modulus; this is the numerical form of the loss recorded by the kernel above.

## The Two Regimes: Outside the Cone and On It

The sandwich is defined for **every** element, zero divisors included, because it is only a product. What changes on the null cone is not its existence but its size.

**Theorem (the rank of the operator).** For every $\tilde{Q}$,

$$
\operatorname{rank} \mathrm{H}_{\tilde{Q}} = \bigl(\operatorname{rank}\Phi(\tilde{Q})\bigr)^{2} .
$$

Consequently

$$
\operatorname{rank}\mathrm{H}_{\tilde{Q}} = \begin{cases} 4, & N(\tilde{Q}) \neq 0, \\ 1, & N(\tilde{Q}) = 0,\ \tilde{Q} \neq 0, \\ 0, & \tilde{Q} = 0 . \end{cases}
$$

**Proof.** Write the singular value decomposition $\Phi(\tilde{Q}) = P\Sigma V^{\dagger}$ with $P, V$ unitary and $\Sigma = \mathrm{diag}(\sigma_1,\sigma_2)$, $\sigma_j \geq 0$. Then, on the matrix side, the operator is $X \mapsto P\Sigma (V^{\dagger}XV)\Sigma P^{\dagger}$. As $X$ runs over $M_2(\mathbb{C})$ so does $V^{\dagger}XV$, and $\Sigma Y \Sigma$ has entries $\sigma_i\sigma_j Y_{ij}$, so the set $\{\Sigma Y\Sigma\}$ is exactly the coordinate subspace spanned by the matrix units $E_{ij}$ with $\sigma_i\sigma_j \neq 0$, of complex dimension $(\#\{j : \sigma_j \neq 0\})^{2}$. Conjugation by the fixed invertible $P$ is an isomorphism of vector spaces and does not change the dimension. The number of nonzero singular values is the rank of $\Phi(\tilde{Q})$, which is $2$ for $N \neq 0$, $1$ for a nonzero zero divisor, and $0$ only for $\tilde{Q} = 0$. $\square$

The two regimes are therefore the following, and they are as different as they can be.

**Outside the cone, $N(\tilde{Q}) \neq 0$.** The operator is invertible: $\mathrm{H}_{\tilde{Q}} \in GL(4,\mathbb{C})$, of rank four. It is a congruence by an invertible matrix, so it preserves the rank of every argument, and it is an isomorphism of the algebra onto itself. Its determinant and trace are the invariants of the proposition above,

$$
\det \mathrm{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}, \qquad \operatorname{Tr}\mathrm{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2} .
$$

**On the cone, $N(\tilde{Q}) = 0$ and $\tilde{Q} \neq 0$.** The operator has rank **one**: it annihilates a three-dimensional subspace and maps the whole eight-dimensional algebra onto a single complex line. That line is not arbitrary. Writing $\Phi(\tilde{Q}) = p\,\sigma\,v^{\dagger}$ with $p$ the left singular vector of the unique nonzero singular value, the image of the operator is

$$
\operatorname{im}\mathrm{H}_{\tilde{Q}} = \mathbb{C}\cdot p\,p^{\dagger},
$$

the line spanned by a **rank-one Hermitian matrix**, that is, by a minimal idempotent of the algebra. In the algebra itself the generator of that line is the element $\tfrac12(e_0 + i\mathbf{n}\cdot\mathbf{e})$ for a unit vector $\mathbf{n}$ determined by $\tilde{Q}$ — Hermitian, idempotent, of norm zero.

**Theorem (the square of a null operator).** If $N(\tilde{Q}) = 0$ then

$$
\mathrm{H}_{\tilde{Q}} \circ \mathrm{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\,\mathrm{H}_{\tilde{Q}} .
$$

**Proof.** The operator has rank one, so on its image it acts as a single scalar, and that scalar is its trace; the trace is $4\lvert Q_0\rvert^{2}$ by the proposition above. $\square$

The scalar is zero exactly when the scalar part of $\tilde{Q}$ vanishes, and then the operator is **nilpotent**: $\mathrm{H}_{\tilde{Q}} \circ \mathrm{H}_{\tilde{Q}} = 0$, so applying a null operator twice gives zero. When the scalar part does not vanish the operator is a **scaled projection**, and normalising $\tilde{Q}$ makes it a projection. The two cases occur inside the same cone, and they are distinguished by the single number $Q_0$.

A worked case fixes the picture. Take $\tilde{Q} = e_1 + ie_2$, of norm $1 + i^{2} = 0$ and with $Q_0 = 0$. Then

$$
\Phi(\tilde{Q}) = \begin{pmatrix} 0 & -2i \\ 0 & 0 \end{pmatrix}, \qquad
\begin{aligned}
e_0 &\mapsto 2e_0 + 2ie_3, \\
e_1 &\mapsto 0, \\
e_2 &\mapsto 0, \\
e_3 &\mapsto 2ie_0 - 2e_3,
\end{aligned}
$$

so that every image is a multiple of the idempotent $\tfrac12(e_0 + ie_3)$ and the second application gives zero. The same computation can be carried out in every coordinate system the algebra admits, and the coordinates always show the two coefficients $x^0 + ix^3$ surviving and the other two disappearing.

## The Coordinate Systems of the Operator

The operator is one map, but it can be written in every coordinate system the algebra carries, and each writing makes a different part of it visible. In the four coefficients it is a component rule, quadratic in the operand and linear in the argument, and its action on the identity already exhibits the non-commutativity of the quaternion part. In the coefficient column it is a matrix, and then it has a determinant, a trace and a spectrum, and the product of the two regular maps that produces it shows why it is a congruence rather than a similarity. In the matrix algebra it is a congruence of $M_2(\mathbb{C})$, and then it acts on ranks, and the rank-one case of a singular multiplier is the collapse. On the simple module it is the operator version of the polar word, and then it has a twist and a domain.

Two cautions follow from the laws above. First, the operator group and the element group are not the same group: the element group acts by multiplication on a module, the operator group by congruence on the algebra, and the two have different kernels — the element action loses nothing while the operator action loses the phase circle. Second, the operator is *quadratic* in $\tilde{Q}$: doubling the operand quadruples the operator, and it is the reason the sandwich doubles the boost and rotation parameters of the polar word.

## Summary

An element of $\mathbb{B}$ can be used as an element or as an operator, and the corpus separates the two. The operator of $\tilde{Q}$ is the Hermitian sandwich $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$, the normalised two-sided map whose two factors are matched by the involution $\dagger$; it preserves the two Hermitian sectors and no other pair of the six distinguished subspaces, and the geometric reading of that preservation is *Biquaternion Rotations and Lorentz Transformations*.

Three laws govern it. It composes, $\mathrm{H}_{\tilde{Q}\tilde{R}} = \mathrm{H}_{\tilde{Q}} \circ \mathrm{H}_{\tilde{R}}$; it is homogeneous of degree two in the centre, $\mathrm{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\mathrm{H}_{\tilde{Q}}$, so it is blind to the scalar imaginary; and its kernel is exactly the circle of central phases $U(1)$, so the phase is the one polar factor the operator discards. It is not an automorphism: the insertion needed for multiplicativity is $\tilde{Q}^{\dagger}\tilde{Q}$, so it is multiplicative exactly on the unitary slice, where it becomes the inner automorphism. On the polar word $\tilde{Q} = re^{i\alpha}B\hat{q}$ it factors as $\mathrm{H}_{\tilde{Q}} = r^{2}\mathrm{H}_{\tilde{\Lambda}}$ with $\tilde{\Lambda} = B\hat{q}$ of unit norm: the scale is counted twice, the phase not at all, and the boost and the rotor deposit their parameters doubled, as $\mathrm{diag}(e^{\psi/2},e^{-\psi/2}) \mapsto \mathrm{diag}(e^{\psi},e^{-\psi})$ shows exactly.

The two regimes are separated by the null cone, and the separator is the rank. The rank of the operator is the square of the rank of the matrix of the element, so it is four for every element outside the cone, one for every nonzero zero divisor, and zero only at the origin. Outside the cone the operator is an invertible congruence with the invariants $\det\mathrm{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}$ and $\operatorname{Tr}\mathrm{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$, obtained as the determinant and the trace of the Kronecker product $\Phi(\tilde{Q}) \otimes \overline{\Phi(\tilde{Q})}$; both are real and non-negative, which is the operator's way of discarding the phase. On the cone it collapses the eight-dimensional algebra onto one complex line, the line of a rank-one Hermitian element, that is, of a minimal idempotent; and it satisfies $\mathrm{H}_{\tilde{Q}} \circ \mathrm{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\mathrm{H}_{\tilde{Q}}$, so it is nilpotent when the scalar part of the operand vanishes and a scaled projection when it does not. The same operator is written in the coefficients, in the coefficient column, in the matrix algebra and on the module, and what differs between those writings is the coordinate system and with it the part of the operator that becomes visible.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, basis $e_0,e_1,e_2,e_3$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | general element; the operand of the operator |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$ | biquaternion norm |
| $\dagger$ | quaternion conjugation composed with complex conjugation |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian sectors, the fixed spaces of $\dagger$ |
| $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$ | the Hermitian sandwich, the operator of $\tilde{Q}$ |
| $\mathrm{H}_{\tilde{Q}\tilde{R}} = \mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{R}}$ | composition law |
| $\mathrm{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\mathrm{H}_{\tilde{Q}}$, $z$ central | central rule; blindness to $i$ |
| $\ker = \{e^{i\theta}e_0\} = U(1)$ | the kernel is the circle of central phases |
| $\mathrm{H}_{\tilde{Q}} = r^{2}\mathrm{H}_{\tilde{\Lambda}}$, $\tilde{\Lambda} = B\hat{q}$ | the polar factors as operators |
| $\operatorname{rank}\mathrm{H}_{\tilde{Q}} = (\operatorname{rank}\Phi(\tilde{Q}))^{2}$ | rank of the operator: $4$, $1$ or $0$ |
| $\det\mathrm{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}$ | determinant of the operator |
| $\operatorname{Tr}\mathrm{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$ | trace of the operator |
| $\operatorname{im}\mathrm{H}_{\tilde{Q}} = \mathbb{C}\cdot pp^{\dagger}$, $N(\tilde{Q}) = 0$ | the null collapse: one Hermitian line |
| $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\mathrm{H}_{\tilde{Q}}$, $N = 0$ | nilpotent if $Q_0 = 0$, scaled projection otherwise |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for versors, the sandwich action, and the difference between the conjugation and the dagger form.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for rotors, the sandwich by a versor, and the doubling of the half-angle.
- I. M. Gel'fand, R. A. Minlos, and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the Lorentz action on the algebra and the double cover.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2nd ed. 2013), for the singular value decomposition, the rank of a congruence, and the eigenvalue products $\lambda_i\bar{\lambda}_j$ of the map $X \mapsto MXM^{\dagger}$.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for group actions by linear maps, kernels and quotient groups.
