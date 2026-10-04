# __Biquaternion Four-Vector Operator Representation__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_0 = 1, e_1, e_2, e_3$, where $e_k^2 = -e_0$ and $e_j e_k = -e_k e_j$ for $j \neq k$, and with a central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$, written in the four-vector realization as the quadruple $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ of *Biquaternion Four-Vector Element Representation*.

That article answers the question *what is* $\tilde{Q}$: it is a quadruple of complex coefficients, with a product rule, four conjugations, six distinguished subspaces and a biquaternion norm. This article answers the question *what does* $\tilde{Q}$ *do*: the element is used as an operator through the Hermitian sandwich

$$
\mathrm{H}_{\tilde{Q}}(\tilde U) = \tilde{Q}\,\tilde U\,\tilde{Q}^{*},
$$

whose laws are *Biquaternion Rotations and Lorentz Transformations*, and the whole article is the coefficient reading of that one formula. Everything is computed from the product rule of the four-vector realization and from the coordinate form of the dagger; the operator's matrix, its determinant and its trace belong to other coordinate systems and are not repeated here, and neither is its reading on the matrix algebra.

The article owns the two-step component rule, the image of the basis elements, the reading of the operator on the scalar and the vector part, the coordinate form of the two regimes, and the worked collapse of a null operator on the basis. The purpose of that material is the one the component realization always serves in this corpus: it turns a structural statement into arithmetic that can be checked on a chosen element.

**Conventions.** The product of two elements with four-vectors $A^\mu$ and $B^\mu$ has components

$$
(\tilde A\tilde B)^0 = A^0B^0 - \sum_{k=1}^{3} A^kB^k, \qquad
(\tilde A\tilde B)^i = A^0B^i + B^0A^i + \sum_{j,k=1}^{3}\epsilon^{ijk}A^jB^k ,
$$

and the Hermitian conjugate has four-vector

$$
(\tilde{Q}^{*})^\mu = \bigl( \overline{Q^0},\; -\overline{Q^1},\; -\overline{Q^2},\; -\overline{Q^3} \bigr),
$$

with the bar denoting complex conjugation of a component. Indices are written up, as in the element article, and the vector part of $Q^\mu$ is written $\mathbf{Q} = (Q^1, Q^2, Q^3)$. The biquaternion norm is $N(\tilde{Q}) = \sum_\mu (Q^\mu)^2$, and $\mathrm{Sc}$ denotes the scalar part.

## The Operator in Components

**Theorem (the two-step rule).** For every $\tilde{Q}$ and every $\tilde U$, the four-vector of $\mathrm{H}_{\tilde{Q}}(\tilde U) = \tilde{Q}\tilde U\tilde{Q}^{*}$ is obtained by applying the product rule twice: first form the four-vector $S^\mu$ of $\tilde{Q}\tilde U$,

$$
S^0 = Q^0U^0 - \mathbf{Q}\cdot\mathbf{U}, \qquad
S^i = Q^0U^i + U^0Q^i + (\mathbf{Q}\times\mathbf{U})^i ,
$$

and then multiply by the four-vector of $\tilde{Q}^{*}$,

$$
\mathrm{H}_{\tilde{Q}}(\tilde U)^0 = \overline{Q^0}\,S^0 + \sum_{k=1}^{3}\overline{Q^k}\,S^k ,
$$

$$
\mathrm{H}_{\tilde{Q}}(\tilde U)^i = -\,S^0\,\overline{Q^i} + \overline{Q^0}\,S^i - (\mathbf{S}\times(\mathbf{Q})^{\natural})^i .
$$

**Proof.** The general product formula applied to the pair $(\tilde{Q}, \tilde U)$ gives $S^\mu$. Applying it again to the pair $(S, \tilde{Q}^{*})$ gives $H^0 = S^0(\tilde{Q}^{*})^0 - \sum_k S^k(\tilde{Q}^{*})^k$ and $H^i = S^0(\tilde{Q}^{*})^i + (\tilde{Q}^{*})^0S^i + \sum_{jk}\epsilon^{ijk}S^j(\tilde{Q}^{*})^k$; substituting $(\tilde{Q}^{*})^0 = \overline{Q^0}$ and $(\tilde{Q}^{*})^k = -\overline{Q^k}$ and collecting gives the two displays.

Two features of the rule carry the meaning of the operator.

The first factor is **not** conjugated and the second **is**: the pair of signs $\overline{Q^0}$ and $-\overline{Q^k}$ is what makes the operator Hermitian rather than an inner automorphism, and it is the coordinate trace of the dagger.

The rule is **linear in $\tilde U$ and quadratic in $\tilde{Q}$**. It is linear in $\tilde U$ because both steps of the product are bilinear and only one factor carries $\tilde U$; linearity over $\mathbb{C}$ follows because the central scalar $\lambda$ in $\tilde U \mapsto \lambda \tilde U$ passes through both factors. It is quadratic in $\tilde{Q}$ because $\tilde{Q}$ occurs once on each side and once conjugated. This is the component form of the two laws of *Biquaternion Rotations and Lorentz Transformations*, that $\mathrm{H}_{\tilde{Q}\tilde{R}} = \mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{R}}$ and that $\mathrm{H}_{A\tilde{Q}} = \lvert A\rvert^{2}\mathrm{H}_{\tilde{Q}}$ for a central $A$: doubling the operand quadruples the operator.

**Corollary (the operator of a scalar multiple).** In particular $\mathrm{H}_{\tilde{Q}} = 0$ if and only if $\tilde{Q} = 0$, since the scalar component of the rule contains the nonzero factor $\overline{Q^0}$ composed with $Q^0$ as soon as any component of $\tilde{Q}$ is nonzero; and $\mathrm{H}_{i\tilde{Q}} = \mathrm{H}_{\tilde{Q}}$, since $\lvert i\rvert^{2} = 1$.

## The Image of the Basis

Applied to the four basis elements, the rule gives the four columns of the operator, and the first of them is a norm.

**Proposition (the image of the identity).** $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{*}$, with four-vector

$$
\bigl(\tilde{Q}\tilde{Q}^{*}\bigr)^0 = \sum_{\mu=0}^{3}\lvert Q^\mu\rvert^{2} = \mathrm{Sc}\bigl(\tilde{Q}\tilde{Q}^{*}\bigr) \geq 0,
$$

$$
\bigl(\tilde{Q}\tilde{Q}^{*}\bigr)^i = \overline{Q^0}Q^i - Q^0\overline{Q^i} - (\mathbf{Q}\times(\mathbf{Q})^{\natural})^i .
$$

The scalar component is the sum of the squared moduli of the four coefficients, a non-negative real that vanishes only for $\tilde{Q} = 0$; it is the value at the operand of the positive Hermitian form $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})$ of *Introduction to the Six Subspaces*. The vector components are purely imaginary, as the four-vector table of the six subspaces requires of a Hermitian element: the image of the identity is Hermitian for every $\tilde{Q}$, and it is central, hence a multiple of $e_0$, exactly when the vector components vanish.

**Proposition (the image of the vector basis).** For $k = 1,2,3$,

$$
\mathrm{H}_{\tilde{Q}}(e_k) = \tilde{Q}\,e_k\,\tilde{Q}^{*} = \bigl(\tilde{Q}e_k\bigr)\tilde{Q}^{*},
$$

and the scalar component of this image is

$$
\mathrm{H}_{\tilde{Q}}(e_k)^0 = 2i\,\mathrm{Im}\bigl(Q^0\overline{Q^k}\bigr) - (\mathbf{Q}\times(\mathbf{Q})^{\natural})^k .
$$

**Proof.** Write $\tilde B = e_k\tilde{Q}^{*}$, of four-vector $B^0 = \overline{Q^k}$ and $B^j = \overline{Q^0}\delta^j_k + \epsilon^{kjl}\overline{Q^l}$, the second term being read from $e_ke_j = \epsilon^{kjl}e_l$ and vanishing for $j = k$. The scalar component of $\tilde{Q}\tilde B$ is then

$$
Q^0B^0 - \sum_{j=1}^{3}Q^jB^j = Q^0\overline{Q^k} - Q^k\overline{Q^0} - (\mathbf{Q}\times(\mathbf{Q})^{\natural})^k,
$$

whose first two terms are $Q^0\overline{Q^k} - \overline{Q^0\overline{Q^k}} = 2i\,\mathrm{Im}(Q^0\overline{Q^k})$.

The scalar component of the image of a vector basis element is thus a pure imaginary number built from the imaginary part of $Q^0\overline{Q^k}$ together with the cross product $\mathbf{Q}\times(\mathbf{Q})^{\natural}$. It vanishes for every $k$ as soon as the four coefficients of $\tilde{Q}$ are real: then every $\mathrm{H}_{\tilde{Q}}(e_k)$ is again a vector, the operator is built from the quaternion conjugation and from a positive real scale, and it preserves the scalar–vector decomposition. It also vanishes for every $k$ when $\tilde{Q}$ is central, whose operator is a multiple of the identity; the complete list of the operators preserving the whole subspace structure is *Biquaternion Rotations and Lorentz Transformations*.

## The Scalar and the Vector Part

Since the operator is linear, its behaviour is fixed by its behaviour on the four basis elements, and the scalar–vector decomposition organizes the answer.

**Corollary (the operator on the scalar and the vector part).** Write $\tilde U = U^0e_0 + \mathbf{U}$ and $\tilde V = \tilde{Q}\tilde U\tilde{Q}^{*} = V^0e_0 + \mathbf{V}$. Then

$$
V^0 = \overline{Q^0}\,\bigl(Q^0U^0 - \mathbf{Q}\cdot\mathbf{U}\bigr) + (\mathbf{Q})^{\natural}\cdot\bigl(Q^0\mathbf{U} + U^0\mathbf{Q} + \mathbf{Q}\times\mathbf{U}\bigr),
$$

$$
\mathbf{V} = \overline{Q^0}\bigl(Q^0\mathbf{U} + U^0\mathbf{Q} + \mathbf{Q}\times\mathbf{U}\bigr) - \bigl(Q^0U^0 - \mathbf{Q}\cdot\mathbf{U}\bigr)(\mathbf{Q})^{\natural} - \Bigl(\bigl(Q^0\mathbf{U} + U^0\mathbf{Q} + \mathbf{Q}\times\mathbf{U}\bigr)\times(\mathbf{Q})^{\natural}\Bigr) .
$$

**Proof.** This is the two-step rule with $S^0 = Q^0U^0 - \mathbf{Q}\cdot\mathbf{U}$ and $\mathbf{S} = Q^0\mathbf{U} + U^0\mathbf{Q} + \mathbf{Q}\times\mathbf{U}$, written out.

The display is the coordinate statement of a structural fact that the matrix realizations make cleaner. Reading $\tilde U$ as a pair $(\text{scalar}, \text{vector})$ and $\tilde V$ likewise, the operator mixes the two parts through the scalar component of $\tilde{Q}$ and its vector component $\mathbf{Q}$, and the mixing is controlled by the term $Q^0U^0 - \mathbf{Q}\cdot\mathbf{U}$, which is the scalar component of the intermediate product. Three consequences are worth recording.

The **centre is not preserved**. Taking $\tilde U = e_0$ gives $\tilde V = \tilde{Q}\tilde{Q}^{*}$, which is central only when $\mathbf{Q}\times(\mathbf{Q})^{\natural} = 0$ and the components align, that is, only for special operands; for a general unit the image of the identity has a nonzero vector part.

The **vector subspace is not preserved** either. Taking $\tilde U = e_k$ gives an image whose scalar component is displayed above, and that component does not vanish in general.

The **two Hermitian sectors are preserved**. If $\tilde{U}^{*} = \tilde U$ then $(\tilde{Q}\tilde U\tilde{Q}^{*})^{\dagger} = \tilde{Q}\tilde U\tilde{Q}^{*}$, and in coordinates the Hermitian condition on $\tilde U$ is $U^0 \in \mathbb{R}$ and $\mathbf{U} \in i\mathbb{R}^3$, which is a condition on the components of $\tilde U$ alone and is therefore inherited by the image. The same computation with $\tilde{U}^{*} = -\tilde U$ gives the anti-Hermitian sector. The invariant subspaces of the operator are treated in *Biquaternion Rotations and Lorentz Transformations*, and their six-subspace table is not repeated here.

## The Two Regimes in Coordinates

The operator is defined for every $\tilde{Q}$, zero divisors included, but its rank is not the same on the two sides of the null cone.

**Theorem (the rank in coordinates).** Let $\tilde{Q} \neq 0$. Then $\mathrm{H}_{\tilde{Q}}$ has rank $4$ if $N(\tilde{Q}) \neq 0$ and rank $1$ if $N(\tilde{Q}) = 0$. On the cone the image of the operator is the single complex line spanned by the Hermitian element $\tilde{Q}\tilde{Q}^{*}$ up to scale, and that element, normalised, is the minimal idempotent

$$
\tilde\Pi = \tfrac{1}{2}\bigl(e_0 + i\mathbf{n}\cdot\mathbf{e}\bigr)
$$

for a unit vector $\mathbf{n}$ determined by $\mathbf{Q}$. Moreover $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\mathrm{H}_{\tilde{Q}}$ on the cone.

**Proof.** Off the cone, $N(\tilde{Q}) \neq 0$, the element and its Hermitian conjugate are invertible, so $\mathrm{H}_{\tilde{Q}} = L_{\tilde{Q}} \circ R_{\tilde{Q}^{*}}$ is a composite of two bijections and has rank $4$. On the cone, with $\tilde{Q} \neq 0$, the matrix of the element has rank one (*Biquaternion 2×2 Matrix Element Representation*), so $\tilde{Q}$ is a nonzero zero divisor, the left ideal $\mathbb{B}\tilde{Q}^{*}$ is minimal of complex dimension $2$ (*Biquaternion Ideals and Peirce Decomposition*), and

$$
\operatorname{im}\mathrm{H}_{\tilde{Q}} = L_{\tilde{Q}}\bigl(\mathbb{B}\tilde{Q}^{*}\bigr) = \mathbb{B}\,\tilde{Q}\tilde{Q}^{*} = \mathbb{C}\cdot\tilde{Q}\tilde{Q}^{*},
$$

a single complex line, because the Hermitian element $\tilde{Q}\tilde{Q}^{*}$ has norm zero and is a nonzero multiple of a minimal idempotent (*Biquaternion Idempotents and Projections*); hence the rank is $1$. The scalar $4\lvert Q^0\rvert^{2}$ is the trace of the operator: in the matrix realization the congruence $X \mapsto MXM^{\dagger}$ has trace $\lvert\operatorname{Tr}M\rvert^{2} = \lvert 2Q^0\rvert^{2} = 4\lvert Q^0\rvert^{2}$, and a rank-one endomorphism $T$ satisfies $T^{2} = (\operatorname{Tr}T)\,T$, so $\mathrm{H}_{\tilde{Q}} \circ \mathrm{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\mathrm{H}_{\tilde{Q}}$. The coordinate form of the image is the statement that every column $\mathrm{H}_{\tilde{Q}}(e_k)$ is a multiple of the single element $\tilde{Q}\tilde{Q}^{*}$, which is displayed in the worked case below.

Two numbers therefore decide everything in coordinates: whether $N(\tilde{Q}) = \sum_\mu (Q^\mu)^2$ vanishes, and whether $Q^0$ vanishes.

**Outside the cone, $N(\tilde{Q}) \neq 0$.** The four columns $\mathrm{H}_{\tilde{Q}}(e_0), \ldots, \mathrm{H}_{\tilde{Q}}(e_3)$ are linearly independent, the operator is invertible, and it preserves the rank of every argument. In coordinates this is the statement that the two-step rule is an invertible linear substitution of the quadruple $U^\mu$.

**On the cone, $N(\tilde{Q}) = 0$.** All four columns lie on one line, and the operator has rank one. The line is that of the Hermitian element $\tilde{Q}\tilde{Q}^{*}$, so the operator sends the whole algebra onto the Hermitian sector, and the target is the projection onto one direction of that sector. If in addition $Q^0 = 0$ the operator is nilpotent, $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 0$, and the second application destroys everything; if $Q^0 \neq 0$ then $\mathrm{H}_{\tilde{Q}}$ is a nonzero multiple of a projection, and normalising $\tilde{Q}$ makes it exactly one.

## Worked Cases

**A null operand with no scalar part.** Take $\tilde{Q} = e_1 + ie_2$, so that $Q^\mu = (0, 1, i, 0)$. Then

$$
N(\tilde{Q}) = 1^2 + i^2 = 1 - 1 = 0, \qquad Q^0 = 0,
$$

so the operand is a zero divisor with vanishing scalar part. The Hermitian conjugate is $\tilde{Q}^{*} = -e_1 + ie_2$, and the sandwich is the nilpotent operator of rank one with

$$
\begin{aligned}
\mathrm{H}_{\tilde{Q}}(e_0) &= (e_1 + ie_2)e_0(-e_1 + ie_2) = 2e_0 + 2ie_3, \\
\mathrm{H}_{\tilde{Q}}(e_1) &= (e_1 + ie_2)e_1(-e_1 + ie_2) = 0, \\
\mathrm{H}_{\tilde{Q}}(e_2) &= (e_1 + ie_2)e_2(-e_1 + ie_2) = 0, \\
\mathrm{H}_{\tilde{Q}}(e_3) &= (e_1 + ie_2)e_3(-e_1 + ie_2) = 2ie_0 - 2e_3 .
\end{aligned}
$$

The two middle columns vanish, and the two remaining ones are $\pm 2$ times the same element $e_0 + ie_3 = 2\tilde\Pi_1$ with $\tilde\Pi_1 = \tfrac12(e_0 + ie_3)$: the image is the line $\mathbb{C}\tilde\Pi_1$. On a general argument the same computation gives the closed form

$$
\mathrm{H}_{\tilde{Q}}(\tilde U) = 2\bigl(U^0 + i U^3\bigr)\bigl(e_0 + ie_3\bigr) = 4\bigl(U^0 + iU^3\bigr)\tilde\Pi_1 ,
$$

in which the image depends only on the two coefficients $U^0$ and $U^3$; the operator has forgotten the other two. Applying it twice gives zero, as the nilpotent case requires. The element $\tilde\Pi_1$ is the idempotent of *Biquaternion Ideals and Peirce Decomposition*, and its vanishing norm is the vanishing of $N(\tilde{Q})$.

**A null operand with a nonzero scalar part.** Take $\tilde{Q} = \tfrac12(e_0 - ie_3) = \tilde\Pi_2$. Then $Q^\mu = (\tfrac12, 0, 0, -\tfrac{i}{2})$, of norm $\tfrac14 + (-\tfrac{i}{2})^2 = \tfrac14 - \tfrac14 = 0$ and of scalar part $\tfrac12 \neq 0$. This operand is **Hermitian**: $(\tfrac12)^{\dagger} = \tfrac12$ and $(ie_3)^{\dagger} = i^{\dagger}e_3^{\dagger} = (-i)(-e_3) = ie_3$, so $\tilde{Q}^{*} = \tilde{Q}$ and the operator is the two-sided product $\tilde\Pi_2\,\tilde U\,\tilde\Pi_2$. On a general $\tilde U = U^0e_0 + U^1e_1 + U^2e_2 + U^3e_3$ its value is

$$
\mathrm{H}_{\tilde{Q}}(\tilde U) = \tfrac14(e_0 - ie_3)\,\tilde U\,(e_0 - ie_3) = \tfrac12\bigl(U^0 + iU^3\bigr)\bigl(e_0 - ie_3\bigr) = \bigl(U^0 + iU^3\bigr)\tilde\Pi_2 ,
$$

and in particular $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde\Pi_2$, $\mathrm{H}_{\tilde{Q}}(e_1) = \mathrm{H}_{\tilde{Q}}(e_2) = 0$ and $\mathrm{H}_{\tilde{Q}}(e_3) = i\tilde\Pi_2$. The same two coefficients survive and the same kind of line is the target, but now the target is the idempotent $\tilde\Pi_2$ itself and the operator is a projection: applying it twice returns the same element, in agreement with $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\mathrm{H}_{\tilde{Q}} = 1\cdot\mathrm{H}_{\tilde{Q}}$, since $4\lvert\tfrac12\rvert^{2} = 1$. The two null cases differ only in the value of the scalar part of the operand, and that one number separates the nilpotent collapse from the projection.

**A unit operand of non-real type.** Take the boost rotor $\tilde{Q} = \cosh\tfrac{\psi}{2}\,e_0 + i\sinh\tfrac{\psi}{2}\,e_1$ with $\psi$ real, of norm $\cosh^{2}\tfrac{\psi}{2} - \sinh^{2}\tfrac{\psi}{2} = 1$ and Hermitian, so that $\tilde{Q}^{*} = \tilde{Q}$. The operator is invertible, and on the identity

$$
\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{*} = \tilde{Q}^2 = \bigl(\cosh^{2}\tfrac{\psi}{2} + \sinh^{2}\tfrac{\psi}{2}\bigr)e_0 + 2i\sinh\tfrac{\psi}{2}\cosh\tfrac{\psi}{2}\,e_1 = \cosh\psi\,e_0 + i\sinh\psi\,e_1 ,
$$

which has a nonzero vector component: the centre is not preserved, and the operand, which stores the half-rapidity $\psi/2$, produces the full rapidity $\psi$. On the anti-Hermitian element $e_1$ the same computation gives $\mathrm{H}_{\tilde{Q}}(e_1) = \cosh\psi\,e_1 - i\sinh\psi\,e_0$, again anti-Hermitian, so the two Hermitian sectors are preserved while the scalar–vector decomposition is not. The general statement of which subspaces survive is *Biquaternion Rotations and Lorentz Transformations*.

## Summary

The element article of this pair lists the four coefficients; this article makes them act. The operator of $\tilde{Q}$ read in the four-vector realization is the Hermitian sandwich $\mathrm{H}_{\tilde{Q}}(\tilde U) = \tilde{Q}\tilde U\tilde{Q}^{*}$, computed by applying the four-vector product rule twice: multiply by $\tilde{Q}$, then by $\tilde{Q}^{*}$, whose four-vector is $(\overline{Q^0}, -\overline{Q^1}, -\overline{Q^2}, -\overline{Q^3})$. The rule is linear in the argument and quadratic in the operand, and the second factor being conjugated is what makes the operator Hermitian rather than an inner automorphism.

On the identity the operator returns $\tilde{Q}\tilde{Q}^{*}$, whose scalar component is the positive quantity $\sum_\mu\lvert Q^\mu\rvert^{2}$, the value of the Hermitian form $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})$; on the vector basis elements it returns elements whose scalar components are $2i\,\mathrm{Im}(Q^0\overline{Q^k}) - (\mathbf{Q}\times(\mathbf{Q})^{\natural})^k$. The centre and the vector subspace are therefore not preserved, while the two Hermitian sectors are, because the Hermitian condition constrains the components of the argument alone.

The two regimes are decided by two numbers: whether the biquaternion norm $\sum_\mu(Q^\mu)^2$ vanishes, and whether the scalar part $Q^0$ vanishes. Outside the cone the four columns are independent and the operator is invertible; on the cone all four columns lie on the line of the Hermitian element $\tilde{Q}\tilde{Q}^{*}$, whose normalisation is a minimal idempotent $\tfrac12(e_0 + i\mathbf{n}\cdot\mathbf{e})$. On the cone the square of the operator is $4\lvert Q^0\rvert^{2}$ times the operator, so $Q^0 = 0$ gives a nilpotent operator and $Q^0 \neq 0$ a scaled projection. The worked operands $e_1 + ie_2$ and $\tfrac12(e_0 - ie_3)$ exhibit the two cases on the same line: both send the algebra onto the span of an idempotent and depend only on $U^0 + iU^3$, and the first is nilpotent while the second is the projection onto its own idempotent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q^\mu = (Q^0,Q^1,Q^2,Q^3)$ | the four-vector of the operand |
| $\mathbf{Q} = (Q^1,Q^2,Q^3)$ | the vector part |
| $\mathrm{H}_{\tilde{Q}}(\tilde U) = \tilde{Q}\tilde U\tilde{Q}^{*}$ | the Hermitian sandwich, written in components |
| $S^\mu = (\tilde{Q}\tilde U)^\mu$ | intermediate product: $S^0 = Q^0U^0 - \mathbf{Q}\cdot\mathbf{U}$, $\mathbf{S} = Q^0\mathbf{U} + U^0\mathbf{Q} + \mathbf{Q}\times\mathbf{U}$ |
| $(\tilde{Q}^{*})^\mu = (\overline{Q^0},-\overline{Q^1},-\overline{Q^2},-\overline{Q^3})$ | the dagger in coordinates |
| $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{*}$, scalar part $\sum_\mu\lvert Q^\mu\rvert^{2}$ | image of the identity; the Hermitian form |
| $\mathrm{H}_{\tilde{Q}}(e_k)^0 = 2i\,\mathrm{Im}(Q^0\overline{Q^k}) - (\mathbf{Q}\times(\mathbf{Q})^{\natural})^k$ | scalar part of the image of a vector unit |
| $\mathrm{H}_{A\tilde{Q}} = \lvert A\rvert^{2}\mathrm{H}_{\tilde{Q}}$, $\mathrm{H}_{i\tilde{Q}} = \mathrm{H}_{\tilde{Q}}$ | central rule; blindness to $i$ |
| $\operatorname{rank}\mathrm{H}_{\tilde{Q}} = 4$ or $1$ | outside the cone, and on it |
| $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\mathrm{H}_{\tilde{Q}}$, $N(\tilde{Q}) = 0$ | nilpotent if $Q^0 = 0$, projection up to scale otherwise |
| $\tilde\Pi = \tfrac12(e_0 + i\mathbf{n}\cdot\mathbf{e})$ | the idempotent whose line is the image on the cone |

## Further Reading

- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the sandwich of a versor written out in components and for the scalar–vector split of a rotor action.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the coordinate calculus of the Clifford algebra $\mathrm{Cl}_{3,1}$ and its conjugations.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2nd ed. 2013), for the rank of a product and the singular value decomposition used for the rank statement.
- Waldyr A. Rodrigues and Edmundo Capelas de Oliveira, *The Many Faces of Maxwell, Dirac and Einstein Equations* (Springer, 2007), for the component calculus of biquaternions in the physical four-vector notation.
