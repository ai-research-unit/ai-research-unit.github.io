# __Biquaternion Four-Vector Operator Representation__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_0 = 1, e_1, e_2, e_3$, where $e_k^2 = -e_0$ and $e_j e_k = -e_k e_j$ for $j \neq k$, and with a central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$, written in the four-vector realization as the quadruple $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ of *Biquaternion Four-Vector Element Representation*.

That article answers the question *what is* $\tilde{Q}$: it is a quadruple of complex coefficients, with a product rule, four conjugations, six distinguished subspaces and a biquaternion norm. This article answers the question *what does* $\tilde{Q}$ *do*: the element is used as an operator through the Hermitian sandwich of *Biquaternion Operator Representation Theory*,

$$
\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^{\dagger},
$$

and the whole article is the coefficient reading of that one formula. Everything is computed from the product rule of the four-vector realization and from the coordinate form of the dagger; the operator's matrix, its determinant and its trace belong to other coordinate systems and are not repeated here, and neither is its reading on the matrix algebra.

The article owns the two-step component rule, the image of the basis elements, the reading of the operator on the scalar and the vector part, the coordinate form of the two regimes, and the worked collapse of a null operator on the basis. The purpose of that material is the one the component realization always serves in this corpus: it turns a structural statement into arithmetic that can be checked on a chosen element.

**Conventions.** The product of two elements with four-vectors $a^\mu$ and $b^\mu$ has components

$$
(ab)^0 = a^0b^0 - \sum_{k=1}^{3} a^kb^k, \qquad
(ab)^i = a^0b^i + b^0a^i + \sum_{j,k=1}^{3}\epsilon^{ijk}a^jb^k ,
$$

and the Hermitian conjugate has four-vector

$$
(\tilde{Q}^{\dagger})^\mu = \bigl( \overline{Q^0},\; -\overline{Q^1},\; -\overline{Q^2},\; -\overline{Q^3} \bigr),
$$

with the bar denoting complex conjugation of a component. Indices are written up, as in the element article, and the vector part of $Q^\mu$ is written $\mathbf{Q} = (Q^1, Q^2, Q^3)$. The biquaternion norm is $N(\tilde{Q}) = \sum_\mu (Q^\mu)^2$, and $\mathrm{Sc}$ denotes the scalar part.

## The Operator in Components

**Theorem (the two-step rule).** For every $\tilde{Q}$ and every $x$, the four-vector of $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$ is obtained by applying the product rule twice: first form the four-vector $S^\mu$ of $\tilde{Q}x$,

$$
S^0 = Q^0x^0 - \mathbf{Q}\cdot\mathbf{x}, \qquad
S^i = Q^0x^i + x^0Q^i + (\mathbf{Q}\times\mathbf{x})^i ,
$$

and then multiply by the four-vector of $\tilde{Q}^{\dagger}$,

$$
\mathrm{H}_{\tilde{Q}}(x)^0 = \overline{Q^0}\,S^0 + \sum_{k=1}^{3}\overline{Q^k}\,S^k ,
$$

$$
\mathrm{H}_{\tilde{Q}}(x)^i = -\,S^0\,\overline{Q^i} + \overline{Q^0}\,S^i - (\mathbf{S}\times\overline{\mathbf{Q}})^i .
$$

**Proof.** The general product formula applied to the pair $(\tilde{Q}, x)$ gives $S^\mu$. Applying it again to the pair $(S, \tilde{Q}^{\dagger})$ gives $H^0 = S^0(\tilde{Q}^{\dagger})^0 - \sum_k S^k(\tilde{Q}^{\dagger})^k$ and $H^i = S^0(\tilde{Q}^{\dagger})^i + (\tilde{Q}^{\dagger})^0S^i + \sum_{jk}\epsilon^{ijk}S^j(\tilde{Q}^{\dagger})^k$; substituting $(\tilde{Q}^{\dagger})^0 = \overline{Q^0}$ and $(\tilde{Q}^{\dagger})^k = -\overline{Q^k}$ and collecting gives the two displays. $\square$

Two features of the rule carry the meaning of the operator.

The first factor is **not** conjugated and the second **is**: the pair of signs $\overline{Q^0}$ and $-\overline{Q^k}$ is what makes the operator Hermitian rather than an inner automorphism, and it is the coordinate trace of the dagger.

The rule is **linear in $x$ and quadratic in $\tilde{Q}$**. It is linear in $x$ because both steps of the product are bilinear and only one factor carries $x$; linearity over $\mathbb{C}$ follows because the central scalar $\lambda$ in $x \mapsto \lambda x$ passes through both factors. It is quadratic in $\tilde{Q}$ because $\tilde{Q}$ occurs once on each side and once conjugated. This is the component form of the two laws of *Biquaternion Operator Representation Theory*, that $\mathrm{H}_{\tilde{Q}\tilde{R}} = \mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{R}}$ and that $\mathrm{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\mathrm{H}_{\tilde{Q}}$ for a central $z$: doubling the operand quadruples the operator.

**Corollary (the operator of a scalar multiple).** In particular $\mathrm{H}_{\tilde{Q}} = 0$ if and only if $\tilde{Q} = 0$, since the scalar component of the rule contains the nonzero factor $\overline{Q^0}$ composed with $Q^0$ as soon as any component of $\tilde{Q}$ is nonzero; and $\mathrm{H}_{i\tilde{Q}} = \mathrm{H}_{\tilde{Q}}$, since $\lvert i\rvert^{2} = 1$.

## The Image of the Basis

Applied to the four basis elements, the rule gives the four columns of the operator, and the first of them is a norm.

**Proposition (the image of the identity).** $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{\dagger}$, with four-vector

$$
\bigl(\tilde{Q}\tilde{Q}^{\dagger}\bigr)^0 = \sum_{\mu=0}^{3}\lvert Q^\mu\rvert^{2} = \mathrm{Sc}\bigl(\tilde{Q}\tilde{Q}^{\dagger}\bigr) \geq 0,
$$

$$
\bigl(\tilde{Q}\tilde{Q}^{\dagger}\bigr)^i = \overline{Q^0}Q^i - Q^0\overline{Q^i} - (\mathbf{Q}\times\overline{\mathbf{Q}})^i .
$$

The scalar component is the sum of the squared moduli of the four coefficients, a non-negative real that vanishes only for $\tilde{Q} = 0$; it is the value at the operand of the positive Hermitian form $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{\dagger})$ of *Biquaternion Hermitian Subspace*. The vector components are purely imaginary, as the four-vector table of the six subspaces requires of a Hermitian element: the image of the identity is Hermitian for every $\tilde{Q}$, and it is central, hence a multiple of $e_0$, exactly when the vector components vanish.

**Proposition (the image of the vector basis).** For $k = 1,2,3$,

$$
\mathrm{H}_{\tilde{Q}}(e_k) = \tilde{Q}\,e_k\,\tilde{Q}^{\dagger} = \bigl(\tilde{Q}e_k\bigr)\tilde{Q}^{\dagger},
$$

and the scalar component of this image is

$$
\mathrm{H}_{\tilde{Q}}(e_k)^0 = 2i\,\mathrm{Im}\bigl(Q^0\overline{Q^k}\bigr) - (\mathbf{Q}\times\overline{\mathbf{Q}})^k .
$$

**Proof.** Write $b = e_k\tilde{Q}^{\dagger}$, of four-vector $b^0 = \overline{Q^k}$ and $b^j = \overline{Q^0}\delta^j_k + \epsilon^{kjl}\overline{Q^l}$, the second term being read from $e_ke_j = \epsilon^{kjl}e_l$ and vanishing for $j = k$. The scalar component of $\tilde{Q}b$ is then

$$
Q^0b^0 - \sum_{j=1}^{3}Q^jb^j = Q^0\overline{Q^k} - Q^k\overline{Q^0} - (\mathbf{Q}\times\overline{\mathbf{Q}})^k,
$$

whose first two terms are $Q^0\overline{Q^k} - \overline{Q^0\overline{Q^k}} = 2i\,\mathrm{Im}(Q^0\overline{Q^k})$. $\square$

The scalar component of the image of a vector basis element is thus a pure imaginary number built from the imaginary part of $Q^0\overline{Q^k}$ together with the cross product $\mathbf{Q}\times\overline{\mathbf{Q}}$. It vanishes for every $k$ as soon as the four coefficients of $\tilde{Q}$ are real: then every $\mathrm{H}_{\tilde{Q}}(e_k)$ is again a vector, the operator is built from the quaternion conjugation and from a positive real scale, and it preserves the scalar–vector decomposition. It also vanishes for every $k$ when $\tilde{Q}$ is central, whose operator is a multiple of the identity; the complete list of the operators preserving the whole subspace structure is *Biquaternion Rotations and Lorentz Transformations*.

## The Scalar and the Vector Part

Since the operator is linear, its behaviour is fixed by its behaviour on the four basis elements, and the scalar–vector decomposition organizes the answer.

**Corollary (the operator on the scalar and the vector part).** Write $x = x^0e_0 + \mathbf{x}$ and $y = \tilde{Q}x\tilde{Q}^{\dagger} = y^0e_0 + \mathbf{y}$. Then

$$
y^0 = \overline{Q^0}\,\bigl(Q^0x^0 - \mathbf{Q}\cdot\mathbf{x}\bigr) + \overline{\mathbf{Q}}\cdot\bigl(Q^0\mathbf{x} + x^0\mathbf{Q} + \mathbf{Q}\times\mathbf{x}\bigr),
$$

$$
\mathbf{y} = \overline{Q^0}\bigl(Q^0\mathbf{x} + x^0\mathbf{Q} + \mathbf{Q}\times\mathbf{x}\bigr) - \bigl(Q^0x^0 - \mathbf{Q}\cdot\mathbf{x}\bigr)\overline{\mathbf{Q}} - \Bigl(\bigl(Q^0\mathbf{x} + x^0\mathbf{Q} + \mathbf{Q}\times\mathbf{x}\bigr)\times\overline{\mathbf{Q}}\Bigr) .
$$

**Proof.** This is the two-step rule with $S^0 = Q^0x^0 - \mathbf{Q}\cdot\mathbf{x}$ and $\mathbf{S} = Q^0\mathbf{x} + x^0\mathbf{Q} + \mathbf{Q}\times\mathbf{x}$, written out. $\square$

The display is the coordinate statement of a structural fact that the matrix realizations make cleaner. Reading $x$ as a pair $(\text{scalar}, \text{vector})$ and $y$ likewise, the operator mixes the two parts through the scalar component of $\tilde{Q}$ and its vector component $\mathbf{Q}$, and the mixing is controlled by the term $Q^0x^0 - \mathbf{Q}\cdot\mathbf{x}$, which is the scalar component of the intermediate product. Three consequences are worth recording.

The **centre is not preserved**. Taking $x = e_0$ gives $y = \tilde{Q}\tilde{Q}^{\dagger}$, which is central only when $\mathbf{Q}\times\overline{\mathbf{Q}} = 0$ and the components align, that is, only for special operands; for a general unit the image of the identity has a nonzero vector part.

The **vector subspace is not preserved** either. Taking $x = e_k$ gives an image whose scalar component is displayed above, and that component does not vanish in general.

The **two Hermitian sectors are preserved**. If $x^{\dagger} = x$ then $(\tilde{Q}x\tilde{Q}^{\dagger})^{\dagger} = \tilde{Q}x\tilde{Q}^{\dagger}$, and in coordinates the Hermitian condition on $x$ is $x^0 \in \mathbb{R}$ and $\mathbf{x} \in i\mathbb{R}^3$, which is a condition on the components of $x$ alone and is therefore inherited by the image. The same computation with $x^{\dagger} = -x$ gives the anti-Hermitian sector. The invariant subspaces of the operator are treated in *Biquaternion Rotations and Lorentz Transformations*, and their six-subspace table is not repeated here.

## The Two Regimes in Coordinates

The operator is defined for every $\tilde{Q}$, zero divisors included, but its rank is not the same on the two sides of the null cone.

**Theorem (the rank in coordinates).** Let $\tilde{Q} \neq 0$. Then $\mathrm{H}_{\tilde{Q}}$ has rank $4$ if $N(\tilde{Q}) \neq 0$ and rank $1$ if $N(\tilde{Q}) = 0$. On the cone the image of the operator is the single complex line spanned by the Hermitian element $\tilde{Q}\tilde{Q}^{\dagger}$ up to scale, and that element, normalised, is the minimal idempotent

$$
\tilde\Pi = \tfrac{1}{2}\bigl(e_0 + i\mathbf{n}\cdot\mathbf{e}\bigr)
$$

for a unit vector $\mathbf{n}$ determined by $\mathbf{Q}$. Moreover $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\mathrm{H}_{\tilde{Q}}$ on the cone.

**Proof.** The rank statement and the scalar $4\lvert Q^0\rvert^{2}$ are proved in *Biquaternion Operator Representation Theory*; the coordinate form of the image is the statement that every column $\mathrm{H}_{\tilde{Q}}(e_k)$ is a multiple of the single element $\tilde{Q}\tilde{Q}^{\dagger}$, which is immediate from the rank-one form $\Phi(\tilde{Q}) = uv^{\dagger}$ and is displayed in the worked case below. $\square$

Two numbers therefore decide everything in coordinates: whether $N(\tilde{Q}) = \sum_\mu (Q^\mu)^2$ vanishes, and whether $Q^0$ vanishes.

**Outside the cone, $N(\tilde{Q}) \neq 0$.** The four columns $\mathrm{H}_{\tilde{Q}}(e_0), \ldots, \mathrm{H}_{\tilde{Q}}(e_3)$ are linearly independent, the operator is invertible, and it preserves the rank of every argument. In coordinates this is the statement that the two-step rule is an invertible linear substitution of the quadruple $x^\mu$.

**On the cone, $N(\tilde{Q}) = 0$.** All four columns lie on one line, and the operator has rank one. The line is that of the Hermitian element $\tilde{Q}\tilde{Q}^{\dagger}$, so the operator sends the whole algebra onto the Hermitian sector, and the target is the projection onto one direction of that sector. If in addition $Q^0 = 0$ the operator is nilpotent, $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 0$, and the second application destroys everything; if $Q^0 \neq 0$ then $\mathrm{H}_{\tilde{Q}}$ is a nonzero multiple of a projection, and normalising $\tilde{Q}$ makes it exactly one.

## Worked Cases

**A null operand with no scalar part.** Take $\tilde{Q} = e_1 + ie_2$, so that $Q^\mu = (0, 1, i, 0)$. Then

$$
N(\tilde{Q}) = 1^2 + i^2 = 1 - 1 = 0, \qquad Q^0 = 0,
$$

so the operand is a zero divisor with vanishing scalar part. The Hermitian conjugate is $\tilde{Q}^{\dagger} = -e_1 + ie_2$, and the sandwich is the nilpotent operator of rank one with

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
\mathrm{H}_{\tilde{Q}}(x) = 2\bigl(x^0 + i x^3\bigr)\bigl(e_0 + ie_3\bigr) = 4\bigl(x^0 + ix^3\bigr)\tilde\Pi_1 ,
$$

in which the image depends only on the two coefficients $x^0$ and $x^3$; the operator has forgotten the other two. Applying it twice gives zero, as the nilpotent case requires. The element $\tilde\Pi_1$ is the idempotent of *Biquaternion Ideals and Peirce Decomposition*, and its vanishing norm is the vanishing of $N(\tilde{Q})$.

**A null operand with a nonzero scalar part.** Take $\tilde{Q} = \tfrac12(e_0 - ie_3) = \tilde\Pi_2$. Then $Q^\mu = (\tfrac12, 0, 0, -\tfrac{i}{2})$, of norm $\tfrac14 + (-\tfrac{i}{2})^2 = \tfrac14 - \tfrac14 = 0$ and of scalar part $\tfrac12 \neq 0$. This operand is **Hermitian**: $(\tfrac12)^{\dagger} = \tfrac12$ and $(ie_3)^{\dagger} = i^{\dagger}e_3^{\dagger} = (-i)(-e_3) = ie_3$, so $\tilde{Q}^{\dagger} = \tilde{Q}$ and the operator is the two-sided product $\tilde\Pi_2\,x\,\tilde\Pi_2$. On a general $x = x^0e_0 + x^1e_1 + x^2e_2 + x^3e_3$ its value is

$$
\mathrm{H}_{\tilde{Q}}(x) = \tfrac14(e_0 - ie_3)\,x\,(e_0 - ie_3) = \tfrac12\bigl(x^0 + ix^3\bigr)\bigl(e_0 - ie_3\bigr) = \bigl(x^0 + ix^3\bigr)\tilde\Pi_2 ,
$$

and in particular $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde\Pi_2$, $\mathrm{H}_{\tilde{Q}}(e_1) = \mathrm{H}_{\tilde{Q}}(e_2) = 0$ and $\mathrm{H}_{\tilde{Q}}(e_3) = i\tilde\Pi_2$. The same two coefficients survive and the same kind of line is the target, but now the target is the idempotent $\tilde\Pi_2$ itself and the operator is a projection: applying it twice returns the same element, in agreement with $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\mathrm{H}_{\tilde{Q}} = 1\cdot\mathrm{H}_{\tilde{Q}}$, since $4\lvert\tfrac12\rvert^{2} = 1$. The two null cases differ only in the value of the scalar part of the operand, and that one number separates the nilpotent collapse from the projection.

**A unit operand of non-real type.** Take the boost rotor $\tilde{Q} = \cosh\tfrac{\psi}{2}\,e_0 + i\sinh\tfrac{\psi}{2}\,e_1$ with $\psi$ real, of norm $\cosh^{2}\tfrac{\psi}{2} - \sinh^{2}\tfrac{\psi}{2} = 1$ and Hermitian, so that $\tilde{Q}^{\dagger} = \tilde{Q}$. The operator is invertible, and on the identity

$$
\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{\dagger} = \tilde{Q}^2 = \bigl(\cosh^{2}\tfrac{\psi}{2} + \sinh^{2}\tfrac{\psi}{2}\bigr)e_0 + 2i\sinh\tfrac{\psi}{2}\cosh\tfrac{\psi}{2}\,e_1 = \cosh\psi\,e_0 + i\sinh\psi\,e_1 ,
$$

which has a nonzero vector component: the centre is not preserved, and the operand, which stores the half-rapidity $\psi/2$, produces the full rapidity $\psi$. On the anti-Hermitian element $e_1$ the same computation gives $\mathrm{H}_{\tilde{Q}}(e_1) = \cosh\psi\,e_1 - i\sinh\psi\,e_0$, again anti-Hermitian, so the two Hermitian sectors are preserved while the scalar–vector decomposition is not. The general statement of which subspaces survive is *Biquaternion Rotations and Lorentz Transformations*.

## Summary

The element article of this pair lists the four coefficients; this article makes them act. The operator of $\tilde{Q}$ read in the four-vector realization is the Hermitian sandwich $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$, computed by applying the four-vector product rule twice: multiply by $\tilde{Q}$, then by $\tilde{Q}^{\dagger}$, whose four-vector is $(\overline{Q^0}, -\overline{Q^1}, -\overline{Q^2}, -\overline{Q^3})$. The rule is linear in the argument and quadratic in the operand, and the second factor being conjugated is what makes the operator Hermitian rather than an inner automorphism.

On the identity the operator returns $\tilde{Q}\tilde{Q}^{\dagger}$, whose scalar component is the positive quantity $\sum_\mu\lvert Q^\mu\rvert^{2}$, the value of the Hermitian form $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{\dagger})$; on the vector basis elements it returns elements whose scalar components are $2i\,\mathrm{Im}(Q^0\overline{Q^k}) - (\mathbf{Q}\times\overline{\mathbf{Q}})^k$. The centre and the vector subspace are therefore not preserved, while the two Hermitian sectors are, because the Hermitian condition constrains the components of the argument alone.

The two regimes are decided by two numbers: whether the biquaternion norm $\sum_\mu(Q^\mu)^2$ vanishes, and whether the scalar part $Q^0$ vanishes. Outside the cone the four columns are independent and the operator is invertible; on the cone all four columns lie on the line of the Hermitian element $\tilde{Q}\tilde{Q}^{\dagger}$, whose normalisation is a minimal idempotent $\tfrac12(e_0 + i\mathbf{n}\cdot\mathbf{e})$. On the cone the square of the operator is $4\lvert Q^0\rvert^{2}$ times the operator, so $Q^0 = 0$ gives a nilpotent operator and $Q^0 \neq 0$ a scaled projection. The worked operands $e_1 + ie_2$ and $\tfrac12(e_0 - ie_3)$ exhibit the two cases on the same line: both send the algebra onto the span of an idempotent and depend only on $x^0 + ix^3$, and the first is nilpotent while the second is the projection onto its own idempotent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q^\mu = (Q^0,Q^1,Q^2,Q^3)$ | the four-vector of the operand |
| $\mathbf{Q} = (Q^1,Q^2,Q^3)$ | the vector part |
| $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$ | the Hermitian sandwich, written in components |
| $S^\mu = (\tilde{Q}x)^\mu$ | intermediate product: $S^0 = Q^0x^0 - \mathbf{Q}\cdot\mathbf{x}$, $\mathbf{S} = Q^0\mathbf{x} + x^0\mathbf{Q} + \mathbf{Q}\times\mathbf{x}$ |
| $(\tilde{Q}^{\dagger})^\mu = (\overline{Q^0},-\overline{Q^1},-\overline{Q^2},-\overline{Q^3})$ | the dagger in coordinates |
| $\mathrm{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^{\dagger}$, scalar part $\sum_\mu\lvert Q^\mu\rvert^{2}$ | image of the identity; the Hermitian form |
| $\mathrm{H}_{\tilde{Q}}(e_k)^0 = 2i\,\mathrm{Im}(Q^0\overline{Q^k}) - (\mathbf{Q}\times\overline{\mathbf{Q}})^k$ | scalar part of the image of a vector unit |
| $\mathrm{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\mathrm{H}_{\tilde{Q}}$, $\mathrm{H}_{i\tilde{Q}} = \mathrm{H}_{\tilde{Q}}$ | central rule; blindness to $i$ |
| $\operatorname{rank}\mathrm{H}_{\tilde{Q}} = 4$ or $1$ | outside the cone, and on it |
| $\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{Q}} = 4\lvert Q^0\rvert^{2}\mathrm{H}_{\tilde{Q}}$, $N(\tilde{Q}) = 0$ | nilpotent if $Q^0 = 0$, projection up to scale otherwise |
| $\tilde\Pi = \tfrac12(e_0 + i\mathbf{n}\cdot\mathbf{e})$ | the idempotent whose line is the image on the cone |

## Further Reading

- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the sandwich of a versor written out in components and for the scalar–vector split of a rotor action.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the coordinate calculus of the Clifford algebra $\mathrm{Cl}_{3,1}$ and its conjugations.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2nd ed. 2013), for the rank of a product and the singular value decomposition used for the rank statement.
- Waldyr A. Rodrigues and Edmundo Capelas de Oliveira, *The Many Faces of Maxwell, Dirac and Einstein Equations* (Springer, 2007), for the component calculus of biquaternions in the physical four-vector notation.
