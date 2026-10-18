# __The Four-Vector Operator Representation of Biquaternions__

## Introduction

Physically this is the arithmetic of a frame change written in the coordinates of a four-vector: the operand is the rotor, the argument is the four-vector being moved, and the two-step rule below is the transformation written out.

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, where $\vec e_k^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$, and with a central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$, written in the four-vector realization as the quadruple $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ of *The Four-Vector Element Representation of Biquaternions*, with the physical dictionary of that article and of *Conventions in the Biquaternion Universe*.

That article answers the question *what is* $\tilde{Q}$: it is a quadruple of complex coefficients, with a product rule, four conjugations, remarkable subspaces, a biquaternion norm and an interpretation as a material four-vector plus an informational four-vector. This article answers the question *what does* $\tilde{Q}$ *do*: the element is used as an operator through the Hermitian sandwich of *Biquaternion Rotations and Lorentz Transformations*,

$$
\operatorname{H}_{\tilde{Q}}(\tilde W) = \tilde{Q}\,\tilde W\,\tilde{Q}^{*},
$$

and the whole article is the coefficient interpretation of that one formula. Everything is computed from the product rule of the four-vector realization and from the coordinate form of the dagger; the operator's matrix, its determinant and its trace belong to other coordinate systems and are not repeated here, and neither is its interpretation on the matrix algebra.

The article owns the two-step component rule, the image of the basis elements, the interpretation of the operator on the scalar and the vector part, the coordinate form of the two regimes, and the worked collapse of a null operator on the basis. The purpose of that material is the one the component realization always serves in this corpus: it turns a structural statement into arithmetic that can be checked on a chosen element.

**Conventions.** The product of two elements with four-vectors $Q_3^\mu$ and $Q_1^\mu$ has components

$$
(\tilde Q_3\tilde{Q}_1)^0 = Q_3^0Q_1^0 - \sum_{k=1}^{3} Q_3^kQ_1^k, \qquad
(\tilde Q_3\tilde{Q}_1)^i = Q_3^0Q_1^i + Q_1^0Q_3^i + \sum_{j,k=1}^{3}\epsilon^{ijk}Q_3^jQ_1^k ,
$$

and the Hermitian conjugate has four-vector

$$
(\tilde{Q}^{*})^\mu = \bigl( \overline{Q^0},\; -\overline{Q^1},\; -\overline{Q^2},\; -\overline{Q^3} \bigr),
$$

with the bar denoting complex conjugation of a component. Indices are written up, as in the element article, and the vector part of $Q^\mu$ is written $\vec Q = (Q^1, Q^2, Q^3)$. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu (Q^\mu)^2$, and $\mathrm{Sc}$ denotes the scalar part. The physical dictionary writes the element as a material part and an informational part,

$$
\tilde{Q} = \underbrace{(ict)\,e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z}_{\in\,\mathbb{M}_-} \;+\; \underbrace{(ct')\,e_t + i(q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z)}_{\in\,\mathbb{M}_+},
$$

with the eight real parameters $q'_t = c\,t$, $(q_x, q_y, q_z)$ the space components of the material part, $q_t = c\,t'$, $(q'_x, q'_y, q'_z)$ the space components of the informational part, and with $c$ the speed of light in the medium.

## The Operator in Components

**Theorem (the two-step rule).** For every $\tilde{Q}$ and every $\tilde W$, the four-vector of $\operatorname{H}_{\tilde{Q}}(\tilde W) = \tilde{Q}\tilde W\tilde{Q}^{*}$ is obtained by applying the product rule twice: first form the four-vector $S^\mu$ of $\tilde{Q}\tilde W$,

$$
S^0 = Q^0W^0 - \vec Q\cdot\vec W, \qquad
S^i = Q^0W^i + W^0Q^i + (\vec Q\times\vec W)^i ,
$$

and then multiply by the four-vector of $\tilde{Q}^{*}$,

$$
\operatorname{H}_{\tilde{Q}}(\tilde W)^0 = \overline{Q^0}\,S^0 + \sum_{k=1}^{3}\overline{Q^k}\,S^k ,
$$

$$
\operatorname{H}_{\tilde{Q}}(\tilde W)^i = -\,S^0\,\overline{Q^i} + \overline{Q^0}\,S^i - (\vec S\times\overline{\vec Q})^i .
$$

**Proof.** The general product formula applied to the pair $(\tilde{Q}, \tilde W)$ gives $S^\mu$. Applying it again to the pair $(S, \tilde{Q}^{*})$ gives $H^0 = S^0(\tilde{Q}^{*})^0 - \sum_k S^k(\tilde{Q}^{*})^k$ and $H^i = S^0(\tilde{Q}^{*})^i + (\tilde{Q}^{*})^0S^i + \sum_{jk}\epsilon^{ijk}S^j(\tilde{Q}^{*})^k$; substituting $(\tilde{Q}^{*})^0 = \overline{Q^0}$ and $(\tilde{Q}^{*})^k = -\overline{Q^k}$ and collecting gives the two displays.

Two features of the rule carry the meaning of the operator.

The first factor is **not** conjugated and the second **is**: the pair of signs $\overline{Q^0}$ and $-\overline{Q^k}$ is what makes the operator Hermitian rather than an inner automorphism, and it is the coordinate trace of the dagger.

The rule is **linear in $\tilde W$ and quadratic in $\tilde{Q}$**. It is linear in $\tilde W$ because both steps of the product are bilinear and only one factor carries $\tilde W$; linearity over $\mathbb{C}$ follows because the central scalar $\lambda$ in $\tilde W \mapsto \lambda \tilde W$ passes through both factors. It is quadratic in $\tilde{Q}$ because $\tilde{Q}$ occurs once on each side and once conjugated. This is the component form of the two laws of *Biquaternion Rotations and Lorentz Transformations*, that $\operatorname{H}_{\tilde{Q}\tilde U} = \operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde U}$ and that $\operatorname{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\operatorname{H}_{\tilde{Q}}$ for a central $z$: doubling the operand quadruples the operator, and it is the reason the rotor stores the half-rapidity while the transformation it generates has the full one.

**Corollary (the operator of a scalar multiple).** In particular $\operatorname{H}_{\tilde{Q}} = 0$ if and only if $\tilde{Q} = 0$, since the scalar component of the rule contains the nonzero factor $\overline{Q^0}$ composed with $Q^0$ as soon as any component of $\tilde{Q}$ is nonzero; and $\operatorname{H}_{i\tilde{Q}} = \operatorname{H}_{\tilde{Q}}$, since $\lvert i\rvert^{2} = 1$.

## The Image of the Basis

Applied to the four basis elements, the rule gives the four columns of the operator, and the first of them is a norm.

**Proposition (the image of the identity).** $\operatorname{H}_{\tilde{Q}}(e_t) = \tilde{Q}\tilde{Q}^{*}$, with four-vector

$$
\bigl(\tilde{Q}\tilde{Q}^{*}\bigr)^0 = \sum_{\mu\in\{t,x,y,z\}}\lvert Q^\mu\rvert^{2} = \mathrm{Sc}\bigl(\tilde{Q}\tilde{Q}^{*}\bigr) \geq 0,
$$

$$
\bigl(\tilde{Q}\tilde{Q}^{*}\bigr)^i = \overline{Q^0}Q^i - Q^0\overline{Q^i} - (\vec Q\times\overline{\vec Q})^i .
$$

The scalar component is the sum of the squared moduli of the four coefficients, a non-negative real that vanishes only for $\tilde{Q} = 0$; it is the value at the operand of the positive Hermitian form $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*}) = \langle\tilde{Q},\tilde{Q}\rangle_{*}$. That form and the biquaternion norm are the two quadratic forms of the framework: the norm $\sum_\mu (Q^\mu)^2$ is complex and indefinite, and it is the interval of the Lorentzian interpretation, while $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*}) = \langle\tilde{Q},\tilde{Q}\rangle_{*}$ is real and positive definite, and it is the Euclidean interpretation the informational sector carries. The vector components of the image are purely imaginary, as the four-vector table of the remarkable subspaces requires of a Hermitian element: the image of the identity is Hermitian for every $\tilde{Q}$, and it is central, hence a multiple of $e_t$, exactly when the vector components vanish — that is, exactly when the operand is a rotation up to a central phase.

**Proposition (the image of the vector basis).** For $k = 1,2,3$,

$$
\operatorname{H}_{\tilde{Q}}(\vec e_k) = \tilde{Q}\,\vec e_k\,\tilde{Q}^{*} = \bigl(\tilde{Q}\vec e_k\bigr)\tilde{Q}^{*},
$$

and the scalar component of this image is

$$
\operatorname{H}_{\tilde{Q}}(\vec e_k)^0 = 2i\,\mathrm{Im}\bigl(Q^0\overline{Q^k}\bigr) - (\vec Q\times\overline{\vec Q})^k .
$$

**Proof.** Let $\tilde B = \vec e_k\tilde{Q}^{*}$, of four-vector $B^0 = \overline{Q^k}$, $B^k = \overline{Q^0}$ and $B^j = \epsilon^{kjl}\overline{Q^l}$ for $j \neq k$, where the last expression is read from $\vec e_k \vec e_j = \epsilon^{kjl}\vec e_l$ and carries no sum over $l$. The scalar component of $\tilde{Q}\tilde B$ is then

$$
Q^0B^0 - \sum_{j=1}^{3}Q^jB^j = Q^0\overline{Q^k} - Q^k\overline{Q^0} - \sum_{j\neq k}\epsilon^{kjl}Q^j\overline{Q^l},
$$

whose first two terms are $Q^0\overline{Q^k} - \overline{Q^0\overline{Q^k}} = 2i\,\mathrm{Im}(Q^0\overline{Q^k})$, while the last is $-(\vec Q\times\overline{\vec Q})^k$, since the cross product collects exactly the terms with $j \neq k$.

The scalar component of the image of a vector basis element is thus a pure imaginary number built from the imaginary part of $Q^0\overline{Q^k}$ together with the cross product $\vec Q\times\overline{\vec Q}$. It vanishes for every $k$ as soon as the four coefficients of $\tilde{Q}$ are real: then every $\operatorname{H}_{\tilde{Q}}(\vec e_k)$ is again a vector, the operator is built from the quaternion conjugation and from a positive real scale, and it preserves the scalar–vector decomposition. It also vanishes for every $k$ when $\tilde{Q}$ is a central element, whose operator is a multiple of the identity; the complete list of the operators preserving the whole subspace structure is *Biquaternion Rotations and Lorentz Transformations*.

## The Scalar and the Vector Part

Since the operator is linear, its behaviour is fixed by its behaviour on the four basis elements, and the scalar–vector decomposition organizes the answer.

**Corollary (the operator on the scalar and the vector part).** Write $\tilde W = W^0e_t + \vec W$ and $\tilde V = \tilde{Q}\tilde W\tilde{Q}^{*} = V^0e_t + \vec V$. Then

$$
V^0 = \overline{Q^0}\,\bigl(Q^0W^0 - \vec Q\cdot\vec W\bigr) + \overline{\vec Q}\cdot\bigl(Q^0\vec W + W^0\vec Q + \vec Q\times\vec W\bigr),
$$

$$
\vec V = \overline{Q^0}\bigl(Q^0\vec W + W^0\vec Q + \vec Q\times\vec W\bigr) - \bigl(Q^0W^0 - \vec Q\cdot\vec W\bigr)\overline{\vec Q} - \Bigl(\bigl(Q^0\vec W + W^0\vec Q + \vec Q\times\vec W\bigr)\times\overline{\vec Q}\Bigr) .
$$

**Proof.** This is the two-step rule with $S^0 = Q^0W^0 - \vec Q\cdot\vec W$ and $\vec S = Q^0\vec W + W^0\vec Q + \vec Q\times\vec W$, written out.

The display is the coordinate statement of a structural fact that the matrix realizations make cleaner. Reading $\tilde W$ as a pair $(\text{scalar}, \text{vector})$ and $\tilde V$ likewise, the operator mixes the two parts through the scalar component of $\tilde{Q}$ and its vector component $\vec Q$, and the mixing is controlled by the term $Q^0W^0 - \vec Q\cdot\vec W$, which is the scalar component of the intermediate product. Three consequences are worth recording.

The **centre is not preserved**. Taking $\tilde W = e_t$ gives $\tilde V = \tilde{Q}\tilde{Q}^{*}$, which is central only when $\vec Q\times\overline{\vec Q} = 0$ and the components align, that is, only for rotations and their central multiples; for a boost the image of the identity has a nonzero vector part, which is the coordinate form of the statement that a boost moves the time axis.

The **vector subspace is not preserved** either. Taking $\tilde W = \vec e_k$ gives an image whose scalar component is displayed above, and that component does not vanish in general.

The **two Hermitian sectors are preserved**. If $\tilde W^{*} = \tilde W$ then $(\tilde{Q}\tilde W\tilde{Q}^{*})^{*} = \tilde{Q}\tilde W\tilde{Q}^{*}$, and in coordinates the Hermitian condition on $\tilde W$ is $W^0 \in \mathbb{R}$ and $\vec W \in i\mathbb{R}^3$, which is a condition on the components of $\tilde W$ alone and is therefore inherited by the image. The same computation with $\tilde W^{*} = -\tilde W$ gives the anti-Hermitian sector, the material one. The invariant subspaces of the operator are treated in *Biquaternion Rotations and Lorentz Transformations* and *The Sandwich Action in Subspaces*, and their remarkable-subspace table is not repeated here.

## The Two Regimes in Coordinates

The operator is defined for every $\tilde{Q}$, zero divisors included, but its rank is not the same on the two sides of the light cone.

**Theorem (the rank in coordinates).** Let $\tilde{Q} \neq 0$. Then $\operatorname{H}_{\tilde{Q}}$ has rank $4$ if $\langle\tilde{Q}\rangle_{\natural} \neq 0$ and rank $1$ if $\langle\tilde{Q}\rangle_{\natural} = 0$. On the cone the image of the operator is the single complex line spanned by the Hermitian element $\tilde{Q}\tilde{Q}^{*}$ up to scale, and that element, normalised, is the minimal idempotent

$$
\tilde\Pi = \tfrac{1}{2}\bigl(e_t + i\vec u\cdot\mathbf{e}\bigr)
$$

for a unit vector $\vec u$ determined by $\vec Q$. Moreover $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\operatorname{H}_{\tilde{Q}}$ on the cone.

**Proof.** Off the light cone, $\langle\tilde{Q}\rangle_{\natural} \neq 0$, the element and its Hermitian conjugate are invertible, so $\operatorname{H}_{\tilde{Q}} = L_{\tilde{Q}} \circ R_{\tilde{Q}^{*}}$ is a composite of two bijections and has rank $4$. On the cone, with $\tilde{Q} \neq 0$, the matrix of the element has rank one (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*), so the left ideal $\mathbb{B}\tilde{Q}^{*}$ is minimal of complex dimension $2$ (*Ideals and Peirce Decomposition of the Biquaternion Algebra*), and the image is the single complex line $\mathbb{B}\,\tilde{Q}\tilde{Q}^{*} = \mathbb{C}\cdot\tilde{Q}\tilde{Q}^{*}$ spanned by the Hermitian element of norm zero, hence of rank $1$. The scalar $4\lvert Q^0\rvert^{2}$ is the trace of the operator: in the matrix realization the congruence $X \mapsto MXM^{\dagger}$ has trace $\lvert\operatorname{Tr}M\rvert^{2} = \lvert 2Q^0\rvert^{2} = 4\lvert Q^0\rvert^{2}$, and a rank-one endomorphism $T$ satisfies $T^{2} = (\operatorname{Tr}T)\,T$, so $\operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\operatorname{H}_{\tilde{Q}}$. The coordinate form of the image is the statement that every column $\operatorname{H}_{\tilde{Q}}(\vec e_k)$ is a multiple of $\tilde{Q}\tilde{Q}^{*}$, displayed in the worked case below.

Two numbers therefore decide everything in coordinates: whether $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu (Q^\mu)^2$ vanishes, and whether $Q^0$ vanishes.

**Outside the cone, $\langle\tilde{Q}\rangle_{\natural} \neq 0$.** The four columns $\operatorname{H}_{\tilde{Q}}(e_t), \ldots, \operatorname{H}_{\tilde{Q}}(\vec e_z)$ are linearly independent, the operator is invertible, and it preserves the rank of every argument. In coordinates this is the statement that the two-step rule is an invertible linear substitution of the quadruple $W^\mu$.

**On the cone, $\langle\tilde{Q}\rangle_{\natural} = 0$.** All four columns lie on one line, and the operator has rank one. The line is that of the Hermitian element $\tilde{Q}\tilde{Q}^{*}$, so the operator sends the whole algebra onto the informational sector, and the target is the projection onto one direction of that sector. If in addition $Q^0 = 0$ the operator is nilpotent, $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 0$, and the second application destroys everything; if $Q^0 \neq 0$ then $\operatorname{H}_{\tilde{Q}}$ is a nonzero multiple of a projection, and normalising $\tilde{Q}$ makes it exactly one. Physically, the first case is a lightlike operand whose scalar part vanishes, and the second a lightlike operand carrying a time component; only the operand is null, and in both cases no genuine motion is generated.

## Worked Cases

**A null operand with no scalar part.** Take $\tilde{Q} = \vec e_x + i\vec e_y$, so that $Q^\mu = (0, 1, i, 0)$. Then

$$
\langle\tilde{Q}\rangle_{\natural} = 1^2 + i^2 = 1 - 1 = 0, \qquad Q^0 = 0,
$$

so the operand is a zero divisor with vanishing scalar part. The Hermitian conjugate is $\tilde{Q}^{*} = -\vec e_x + i\vec e_y$, and the sandwich is the nilpotent operator of rank one with

$$
\begin{aligned}
\operatorname{H}_{\tilde{Q}}(e_t) &= (\vec e_x + i\vec e_y)e_t(-\vec e_x + i\vec e_y) = 2e_t + 2i\vec e_z, \\
\operatorname{H}_{\tilde{Q}}(\vec e_x) &= (\vec e_x + i\vec e_y)\vec e_x(-\vec e_x + i\vec e_y) = 0, \\
\operatorname{H}_{\tilde{Q}}(\vec e_y) &= (\vec e_x + i\vec e_y)\vec e_y(-\vec e_x + i\vec e_y) = 0, \\
\operatorname{H}_{\tilde{Q}}(\vec e_z) &= (\vec e_x + i\vec e_y)\vec e_z(-\vec e_x + i\vec e_y) = 2ie_t - 2\vec e_z .
\end{aligned}
$$

The two middle columns vanish, and the two remaining ones are $\pm 2$ times the same element $e_t + i\vec e_z = 2\tilde\Pi_+$ with $\tilde\Pi_+ = \tfrac12(e_t + i\vec e_z)$: the image is the line $\mathbb{C}\tilde\Pi_+$. On a general argument the same computation gives the closed form

$$
\operatorname{H}_{\tilde{Q}}(\tilde W) = 2\bigl(W^0 + i W^3\bigr)\bigl(e_t + i\vec e_z\bigr) = 4\bigl(W^0 + iW^3\bigr)\tilde\Pi_+ ,
$$

in which the image depends only on the two coefficients $W^0$ and $W^3$; the operator has forgotten the other two. Applying it twice gives zero, as the nilpotent case requires. The element $\tilde\Pi_+$ is an idempotent of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, and its vanishing norm is the vanishing of $\langle\tilde{Q}\rangle_{\natural}$. Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

**A null operand with a nonzero scalar part.** Take $\tilde{Q} = \tfrac12(e_t - i\vec e_z) = \tilde\Pi_-$. Then $Q^\mu = (\tfrac12, 0, 0, -\tfrac{i}{2})$, of norm $\tfrac14 + (-\tfrac{i}{2})^2 = \tfrac14 - \tfrac14 = 0$ and of scalar part $\tfrac12 \neq 0$. This operand is **Hermitian**: $(\tfrac12)^{\dagger} = \tfrac12$ and $(i\vec e_z)^{*} = i^{*}\vec e_z^{\dagger} = (-i)(-\vec e_z) = i\vec e_z$, so $\tilde{Q}^{*} = \tilde{Q}$ and the operator is the two-sided product $\tilde\Pi_-\,\tilde W\,\tilde\Pi_-$. On a general $\tilde W = W^0e_t + W^1\vec e_x + W^2\vec e_y + W^3\vec e_z$ its value is

$$
\operatorname{H}_{\tilde{Q}}(\tilde W) = \tfrac14(e_t - i\vec e_z)\,\tilde W\,(e_t - i\vec e_z) = \tfrac12\bigl(W^0 + iW^3\bigr)\bigl(e_t - i\vec e_z\bigr) = \bigl(W^0 + iW^3\bigr)\tilde\Pi_- ,
$$

and in particular $\operatorname{H}_{\tilde{Q}}(e_t) = \tilde\Pi_-$, $\operatorname{H}_{\tilde{Q}}(\vec e_x) = \operatorname{H}_{\tilde{Q}}(\vec e_y) = 0$ and $\operatorname{H}_{\tilde{Q}}(\vec e_z) = i\tilde\Pi_-$. The same two coefficients survive and the same kind of line is the target, but now the target is the idempotent $\tilde\Pi_-$ itself and the operator is a projection: applying it twice returns the same element, in agreement with $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\operatorname{H}_{\tilde{Q}} = 1\cdot\operatorname{H}_{\tilde{Q}}$, since $4\lvert\tfrac12\rvert^{2} = 1$. The two null cases differ only in the value of the scalar part of the operand, and that one number separates the nilpotent collapse from the projection.

**A physical boost.** Take the boost rotor $\tilde{Q} = \cosh\tfrac{\psi}{2}\,e_t + i\sinh\tfrac{\psi}{2}\,\vec e_x$ with $\psi$ real, of norm $\cosh^{2}\tfrac{\psi}{2} - \sinh^{2}\tfrac{\psi}{2} = 1$ and Hermitian, so that $\tilde{Q}^{*} = \tilde{Q}$. The operator is invertible, and on the identity

$$
\operatorname{H}_{\tilde{Q}}(e_t) = \tilde{Q}\tilde{Q}^{*} = \tilde{Q}^2 = \bigl(\cosh^{2}\tfrac{\psi}{2} + \sinh^{2}\tfrac{\psi}{2}\bigr)e_t + 2i\sinh\tfrac{\psi}{2}\cosh\tfrac{\psi}{2}\,\vec e_x = \cosh\psi\,e_t + i\sinh\psi\,\vec e_x ,
$$

which has a nonzero vector component: the centre is not preserved, and the operand, which stores the half-rapidity $\psi/2$, produces the full rapidity $\psi$. In numbers, the rotor $\tilde{Q} = \tfrac53 e_t + \tfrac43 i\vec e_z$ of *Biquaternion Rotations and Lorentz Transformations* has $\cosh\tfrac{\psi}{2} = \tfrac53$ and $\sinh\tfrac{\psi}{2} = \tfrac43$, hence $\psi = 2\ln 3$ and $\beta = \tanh\psi = \tfrac{40}{41}$, and the image of the identity is $\tfrac{41}{9}e_t + \tfrac{40}{9}i\vec e_z$, the four-vector of the moved time axis. On the two directions $\vec e_x$ and $\vec e_y$, transverse to the boost axis, the same computation gives $\operatorname{H}_{\tilde{Q}}(\vec e_x) = \vec e_x$ and $\operatorname{H}_{\tilde{Q}}(\vec e_y) = \vec e_y$: a transverse direction is untouched. On $\vec e_z$, along the boost axis, it gives $\operatorname{H}_{\tilde{Q}}(\vec e_z) = -i\sinh\psi\,e_t + \cosh\psi\,\vec e_z$, which is again anti-Hermitian and which mixes the scalar and the vector part, so the two Hermitian sectors are preserved while the scalar–vector decomposition is not. The general statement of which subspaces survive is *Biquaternion Rotations and Lorentz Transformations*.

## Physical Readings

The operator reads as a change of frame written on coefficients: the two-step rule is the sandwich in components, and its interpretation is a physical arithmetic rather than a state. Read on the monoid, this operator is the same map the abstract article calls the left–right composition, so the article is where a process becomes computable (*The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*). Read on the clock, the operator acts on the ledger and its unit-norm slice is what preserves the central phase.

## Summary

The element article of this pair lists the four coefficients; this article makes them act. The operator of $\tilde{Q}$ read in the four-vector realization is the Hermitian sandwich $\operatorname{H}_{\tilde{Q}}(\tilde W) = \tilde{Q}\tilde W\tilde{Q}^{*}$, computed by applying the four-vector product rule twice: multiply by $\tilde{Q}$, then by $\tilde{Q}^{*}$, whose four-vector is $(\overline{Q^0}, -\overline{Q^1}, -\overline{Q^2}, -\overline{Q^3})$. The rule is linear in the argument and quadratic in the operand, and the second factor being conjugated is what makes the operator Hermitian rather than an inner automorphism.

On the identity the operator returns $\tilde{Q}\tilde{Q}^{*}$, whose scalar component is the positive quantity $\sum_\mu\lvert Q^\mu\rvert^{2}$, the value of the Hermitian form $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*}) = \langle\tilde{Q},\tilde{Q}\rangle_{*}$ and the Euclidean square of the operand, to be contrasted with the complex, indefinite biquaternion norm that carries the interval; on the vector basis elements it returns elements whose scalar components are $2i\,\mathrm{Im}(Q^0\overline{Q^k}) - (\vec Q\times\overline{\vec Q})^k$. The centre and the vector subspace are therefore not preserved, while the two Hermitian sectors are, because the Hermitian condition constrains the components of the argument alone. In physical terms a boost mixes the time and space coordinates of the four-vector, and it is only the rotation, and its central multiples, that keeps the two sectors apart.

The two regimes are decided by two numbers: whether the biquaternion norm $\sum_\mu(Q^\mu)^2$ vanishes, and whether the scalar part $Q^0$ vanishes. Outside the light cone the four columns are independent and the operator is invertible; on the cone all four columns lie on the line of the Hermitian element $\tilde{Q}\tilde{Q}^{*}$, whose normalisation is a minimal idempotent $\tfrac12(e_t + i\vec u\cdot\mathbf{e})$. On the cone the square of the operator is $4\lvert Q^0\rvert^{2}$ times the operator, so $Q^0 = 0$ gives a nilpotent operator and $Q^0 \neq 0$ a scaled projection. The worked operands $\vec e_x + i\vec e_y$ and $\tfrac12(e_t - i\vec e_z)$ exhibit the two cases on the same line: both send the algebra onto the span of an idempotent and depend only on $W^0 + iW^3$, and the first is nilpotent while the second is the projection onto its own idempotent. The boost rotor $\tfrac53 e_t + \tfrac43 i\vec e_z$ shows the other regime, in which the half-rapidity of the operand appears as the full rapidity of the motion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q^\mu = (Q^0,Q^1,Q^2,Q^3)$ | the four-vector of the operand |
| $\vec Q = (Q^1,Q^2,Q^3)$ | the vector part |
| $\operatorname{H}_{\tilde{Q}}(\tilde W) = \tilde{Q}\tilde W\tilde{Q}^{*}$ | the Hermitian sandwich, written in components |
| $S^\mu = (\tilde{Q}\tilde W)^\mu$ | intermediate product: $S^0 = Q^0W^0 - \vec Q\cdot\vec W$, $\vec S = Q^0\vec W + W^0\vec Q + \vec Q\times\vec W$ |
| $(\tilde{Q}^{*})^\mu = (\overline{Q^0},-\overline{Q^1},-\overline{Q^2},-\overline{Q^3})$ | the dagger in coordinates |
| $\operatorname{H}_{\tilde{Q}}(e_t) = \tilde{Q}\tilde{Q}^{*}$, scalar part $\sum_\mu\lvert Q^\mu\rvert^{2}$ | image of the identity; the positive Hermitian form |
| $\operatorname{H}_{\tilde{Q}}(\vec e_k)^0 = 2i\,\mathrm{Im}(Q^0\overline{Q^k}) - (\vec Q\times\overline{\vec Q})^k$ | scalar part of the image of a vector unit |
| $\operatorname{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\operatorname{H}_{\tilde{Q}}$, $\operatorname{H}_{i\tilde{Q}} = \operatorname{H}_{\tilde{Q}}$ | central rule; blindness to $i$ |
| $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = 4$ or $1$ | outside the light cone, and on it |
| $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\operatorname{H}_{\tilde{Q}}$, $\langle\tilde{Q}\rangle_{\natural} = 0$ | nilpotent if $Q^0 = 0$, projection up to scale otherwise |
| $\tilde\Pi = \tfrac12(e_t + i\vec u\cdot\mathbf{e})$ | the idempotent whose line is the image on the cone |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the sandwich of a versor written out in components and for the scalar–vector split of a rotor action.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the coordinate calculus of the Clifford algebra $\mathrm{Cl}_{3,1}$ and its conjugations.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2nd ed. 2013), for the rank of a product and the singular value decomposition used for the rank statement.
- Waldyr A. Rodrigues and Edmundo Capelas de Oliveira, *The Many Faces of Maxwell, Dirac and Einstein Equations* (Springer, 2007), for the component calculus of biquaternions in the physical four-vector notation.
