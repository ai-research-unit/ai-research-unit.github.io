# __One-Sided Operators with the Signed Product__

## Introduction

The factors of the signed two-sided operator $a\alpha(y)b$ are one-sided, and they are of two different kinds. On the left the sign sits on the **argument**: the signed left multiplication is $y\mapsto a\,\alpha(y)$, the ordinary left multiplication composed with the grade involution. On the right the sign sits on the **parameter**: the signed right multiplication is $y\mapsto y\,\alpha(b)$, the ordinary right multiplication by the twisted parameter. The asymmetry comes from the same place as the anti-multiplicativity of the right family — an automorphism pushes forward through a product, an anti-automorphism pulls back — and it makes the two signed families behave differently under composition.

This article fixes the signed one-sided operators, their composition laws, their fixed elements, and the way a pairing of a signed factor with an ordinary one produces the reflections. The composition laws already show the asymmetry: two signed **left** multiplications compose to an ordinary left multiplication, the two grade involutions cancelling, while two signed **right** multiplications compose to a signed right multiplication, because there the parameter is twisted twice and the twist is an involution. The fixed elements are read off immediately: the signed left multiplication by a scalar is the identity on the even part, minus the identity on the odd part, or zero, according as the scalar is $1$, $-1$ or anything else. And the reflections arise exactly as in the ordinary theory, by pairing: the signed left multiplication by a vector with the ordinary right multiplication by the inverse of its twisted parameter is the reflection.

The one-sided operators and their composition are *One-Sided Operators on a Clifford Algebra*; the operators twisted by the grading are *The Graded Multiplication Operators*; the two-sided signed family is *Two-Sided Operators with the Signed Product*; the signed sandwich and the reflections are *The Sandwich with the Signed Product*; the one-sided action on a module is *The One-Sided Action and the Spin Representation*. Those are cited. The base is a field $F$ of characteristic not $2$, $q$ is non-degenerate and $\alpha$ is the grade involution.

## The Signed One-Sided Family

**Definition.** For $a \in \mathrm{Cl}(V,q)$ the **signed left multiplication** and the **signed right multiplication** are

$$
\mathrm{L}^{\alpha}_a(y) = a\,\alpha(y) = L_a\bigl(\alpha(y)\bigr), \qquad \mathrm{P}^{\alpha}_a(y) = y\,\alpha(a) = R_{\alpha(a)}(y).
$$

So $\mathrm{L}^{\alpha}_a = L_a\circ\alpha$ is the ordinary left multiplication with the **argument** twisted, and $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$ is the ordinary right multiplication with the **parameter** twisted. The two are different kinds of twist, and this is the source of the asymmetry in the composition laws.

**Convention.** The symbol $\Lambda^{\alpha}$ of *One-Sided Operators on a Clifford Algebra* and *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* puts the grade involution on the **parameter**, $\Lambda^{\alpha}_x = L_{\alpha(x)} = \varepsilon_xL_x$, and it is that operator which is the left factor of the signed inner conjugation. The present family is the one-sided form of the **signed product** $T^{\alpha}_{a,b}(y) = a\alpha(y)b$, so its left factor twists the argument instead, and it is written $\mathrm{L}^{\alpha}$ to keep the two apart; the right factor agrees with the other convention, $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$.

**Proposition (elementary properties).** Both families are $F$-linear and bijective for $a$ a unit; $\mathrm{L}^{\alpha}_1 = \alpha = \mathrm{P}^{\alpha}_1$; $\mathrm{L}^{\alpha}_a$ coincides with $L_a$ on the even part and with $-L_a$ on the odd part; and for homogeneous $a$ one has $\mathrm{P}^{\alpha}_a = (-1)^{|a|}R_a$.

**Proof.** $\mathrm{L}^{\alpha}_a$ and $\mathrm{P}^{\alpha}_a$ are composites of $F$-linear bijections when $a$ is a unit; at $a = 1$ both reduce to $\alpha(1) = 1$ applied to the argument, that is to $\alpha$. The sign statements are $\alpha(a) = (-1)^{|a|}a$ for the right family and $\alpha(y) = (-1)^{i}y$ on $\mathrm{Cl}^{i}$ for the left: $\mathrm{L}^{\alpha}_a$ is $L_a\circ\alpha$, so it equals $(-1)^{i}L_a$ on $\mathrm{Cl}^{i}$ and hence $L_a$ on $\mathrm{Cl}^{0}$, $-L_a$ on $\mathrm{Cl}^{1}$; it is **not** a scalar multiple of $L_a$ unless $L_a$ is itself even, the argument twisting a different factor from the parameter.

**Proposition (the parity).** $\mathrm{L}^{\alpha}_a$ and $\mathrm{P}^{\alpha}_a$ have the parity of $a$: they carry $\mathrm{Cl}^{i}$ to $\mathrm{Cl}^{i+|a|}$.

**Proof.** $\mathrm{L}^{\alpha}_a = L_a\circ\alpha$ and $\alpha$ preserves the degree modulo two while $L_a$ shifts it by $|a|$; $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$ and $\alpha(a)$ has the parity of $a$, so the right multiplication by it shifts the degree by $|a|$.

## The Composition Laws

**Proposition (the left family).** For all $a, c$

$$
\mathrm{L}^{\alpha}_a \circ \mathrm{L}^{\alpha}_c = L_{a\alpha(c)}, \qquad
\mathrm{L}^{\alpha}_a \circ L_c = \mathrm{L}^{\alpha}_{a\alpha(c)}, \qquad
L_a \circ \mathrm{L}^{\alpha}_c = \mathrm{L}^{\alpha}_{ac}.
$$

So the composite of **two** signed left multiplications is an ordinary left multiplication, the two grade involutions cancelling; the composite of a signed and an ordinary left multiplication, in either order, is signed.

**Proof.** $\mathrm{L}^{\alpha}_aL_c(y) = a\alpha(cy) = a\alpha(c)\alpha(y) = \mathrm{L}^{\alpha}_{a\alpha(c)}(y)$; $L_a\mathrm{L}^{\alpha}_c(y) = ac\alpha(y) = \mathrm{L}^{\alpha}_{ac}(y)$; and composing two of the first kind gives $L_{a\alpha(c)}\alpha\circ\alpha = L_{a\alpha(c)}$.

**Proposition (the right family carries no new operators).** Since $\alpha$ is a bijection, $\{\mathrm{P}^{\alpha}_a : a \in \mathrm{Cl}(V,q)\} = \{R_b : b \in \mathrm{Cl}(V,q)\}$: the signed right multiplications are exactly the ordinary right multiplications, reparametrised by $b = \alpha(a)$. Consequently

$$
\mathrm{P}^{\alpha}_a \circ \mathrm{P}^{\alpha}_c = \mathrm{P}^{\alpha}_{ca}, \qquad
\mathrm{P}^{\alpha}_a \circ R_c = \mathrm{P}^{\alpha}_{\alpha(c)\,a}, \qquad
R_c \circ \mathrm{P}^{\alpha}_a = \mathrm{P}^{\alpha}_{a\,\alpha(c)},
$$

and the signed right family is a group, being the ordinary right family. The genuine asymmetry is that the signed left multiplications are new maps while the signed right multiplications are not.

**Proof.** $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$ by definition, and $\alpha$ is surjective, which gives the first sentence; the laws are the ordinary laws $R_bR_d = R_{db}$ under the substitution $b = \alpha(a)$, $d = \alpha(c)$. Explicitly, $\mathrm{P}^{\alpha}_aR_c(y) = yc\alpha(a) = y\alpha(\alpha(c))\alpha(a) = y\alpha(\alpha(c)a) = \mathrm{P}^{\alpha}_{\alpha(c)a}(y)$.

**Corollary (the mirror of the coset structure).** The signed left multiplications form, together with the ordinary ones, the coset $L(\Gamma)\alpha$ of the group $L(\Gamma)$ of invertible left multiplications; the signed right multiplications are the ordinary right multiplications themselves. The asymmetry is exactly the difference between an automorphism acting on the **argument** and the same automorphism acting on the **parameter**: on the left the twist changes the operator, and on the right it merely relabels it. The genuinely signed one-sided family is therefore the left one, and it is a coset and not a group.

**Proof.** The left statement is the first law, the right statement the first law of the right family, and the isomorphism is $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$.

## Fixed Elements

**Definition.** The **fixed space** of an operator $T$ is $\mathrm{Fix}(T) = \{y : T(y) = y\}$.

**Proposition.** For $a \in \mathrm{Cl}(V,q)$,

$$
\mathrm{Fix}(\mathrm{L}^{\alpha}_a) = \{\, y : a\,\alpha(y) = y \,\}, \qquad \mathrm{Fix}(\mathrm{P}^{\alpha}_a) = \{\, y : y\,\alpha(a) = y \,\}.
$$

In particular $\mathrm{Fix}(\mathrm{L}^{\alpha}_1) = \mathrm{Fix}(\alpha) = \mathrm{Cl}^{0}(V,q)$ is the even part, and for a scalar $\lambda$

$$
\mathrm{Fix}(L_{\lambda}\alpha) = \begin{cases} \mathrm{Cl}^{0}(V,q), & \lambda = 1, \\ \mathrm{Cl}^{1}(V,q), & \lambda = -1, \\ 0, & \lambda \neq \pm1. \end{cases}
$$

**Proof.** Write $y = y_0 + y_1$. The equation $\lambda\alpha(y) = y$ is $\lambda y_0 = y_0$ and $-\lambda y_1 = y_1$; the two are satisfied independently, giving the three cases. The general formulae are the definitions.

**Remark (fixed elements against the graded parts).** The fixed space of the signed left multiplication by a scalar is a **graded subspace**, the even or the odd part; this is the operator form of the statement that the grade involution is the parity operator. For a general $a$ the fixed space is not graded, and it is a right or left translate of a graded subspace by the equation above.

## The Reflections

**Proposition (the pairing).** For a unit $x$, the signed sandwich of *The Sandwich with the Signed Product* is the pairing of the signed left multiplication by $x$ with the ordinary right multiplication by the inverse of the twisted parameter:

$$
\Sigma_x = \mathrm{L}^{\alpha}_x \circ R_{\alpha(x)^{-1}} .
$$

**Proof.** $\mathrm{L}^{\alpha}_x\bigl(R_{\alpha(x)^{-1}}(y)\bigr) = x\,\alpha\bigl(y\,\alpha(x)^{-1}\bigr) = x\,\alpha(y)\,\alpha\bigl(\alpha(x)^{-1}\bigr) = x\,\alpha(y)\,\alpha^{2}(x)^{-1} = x\,\alpha(y)\,x^{-1} = \Sigma_x(y)$, using that $\alpha$ is an automorphism, that $\alpha^{-1} = \alpha$, and that $\alpha^{2} = \mathrm{id}$. The inverse right multiplication of the other convention, $R_{x^{-1}}$, gives only $\varepsilon_x\Sigma_x$, because $\alpha(x)^{-1} = \varepsilon_x x^{-1}$; the two pairings agree exactly on the even part of the unit group, which is the reason the corpus keeps the two families apart.

**Theorem (the reflections).** Let $u \in V$ with $q(u) \neq 0$. Then $\Sigma_u = \mathrm{L}^{\alpha}_u\circ R_{\alpha(u)^{-1}}$ restricted to $V$ is the reflection $\rho_u$, and its fixed vectors in $V$ are the hyperplane $u^{\perp}$:

$$
\mathrm{Fix}\bigl(\Sigma_u\big|_V\bigr) = u^{\perp} = \{\, v \in V : B(u,v) = 0 \,\}.
$$

**Proof.** The reflection statement is the theorem of *The Sandwich with the Signed Product*; for the fixed space, $\rho_u(v) = v$ exactly when $2B(v,u)q(u)^{-1}u = 0$, that is $B(v,u) = 0$.

**Remark (why one side is not enough).** A signed left multiplication by a vector never preserves $V$, for the same reason an ordinary left multiplication does not: $L_u\alpha(\mathrm{Cl}^{1})$ contains the scalars as well as the vectors, since $\alpha$ flips the parity. Only the pairing with an ordinary right multiplication brings the parity back and produces an operator of $V$. This is the one-sided form of the statement of *One-Sided Operators on a Clifford Algebra* that the scalar is the only one-sided operator preserving the quadratic space.

## Worked Cases

### A Scalar in $\mathrm{Cl}_{0,3}(\mathbb{R})$

With $e_j^{2} = -1$ let $\lambda = -1$. Then $L_{-1}\alpha$ is the identity on the odd part and minus the identity on the even part, so its fixed space is the four-dimensional odd part $\mathrm{span}(e_1,e_2,e_3,\omega)$, and $L_{-1}\alpha = -\alpha$ has square $-\mathrm{id}$; the example shows a signed one-sided operator whose fixed space is a full graded summand.

### A Vector

In the same algebra let $a = e_1$. Write $y = y_0 + y_1$ with $y_0$ even and $y_1$ odd, so that $\alpha(y) = y_0 - y_1$ and the equation $e_1\alpha(y) = y$ reads $e_1y_0 - e_1y_1 = y_0 + y_1$. Comparing the even parts gives $y_1 = e_1y_0$, and the odd parts then give $-e_1y_1 = y_0$, that is $-e_1^{2}y_0 = y_0$, which holds identically. So $\mathrm{Fix}(\mathrm{L}^{\alpha}_{e_1}) = \{y_0 + e_1y_0 : y_0 \in \mathrm{Cl}^{0}(V,q)\}$, a four-dimensional space that is not graded, the graph of the left multiplication by $e_1$ in the even part.

### The Reflection

With $u = e_1$ one has $\alpha(e_1)^{-1} = (-e_1)^{-1} = e_1$, and the signed sandwich $\Sigma_{e_1} = \mathrm{L}^{\alpha}_{e_1}\circ R_{e_1}$ acts on the basis of $V$ by $(-e_1, e_2, e_3)$ and fixes the hyperplane $e_1^{\perp} = \mathrm{span}(e_2, e_3)$, as a reflection should. The signed left factor alone does not preserve $V$; the pairing does.

## Summary

The **signed left multiplication** $\mathrm{L}^{\alpha}_a = L_a\circ\alpha$ twists the argument and the **signed right multiplication** $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$ twists the parameter; both have the parity of $a$ and coincide with $\alpha$ at $a = 1$. The asymmetry between them is complete: $\mathrm{L}^{\alpha}_a = L_a\circ\alpha$ is a new operator for an odd $a$, while $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$ is the ordinary right multiplication relabelled, so the signed right family is just the ordinary right family and there are no new right operators. The composition laws record the rest: two signed **left** multiplications give an ordinary left multiplication, $L_{a\alpha(c)}$, because the two grade involutions cancel, so the signed left family is a coset of the ordinary left family and not a group, exactly the one-sided form of the torsor structure of *Two-Sided Operators with the Signed Product*. The fixed space of a signed operator is given by $a\alpha(y) = y$ on the left and $y\alpha(a) = y$ on the right; that of the scalar $\lambda$ is the even part, the odd part or nothing according as $\lambda = 1, -1$ or neither. Finally the reflections are pairings: $\Sigma_x = \mathrm{L}^{\alpha}_x R_{\alpha(x)^{-1}}$, a vector $u$ gives the reflection $\rho_u$, and its fixed vectors are the hyperplane $u^{\perp}$; a signed left multiplication alone never preserves $V$. The ordinary one-sided calculus is *One-Sided Operators on a Clifford Algebra*, the graded twisting is *The Graded Multiplication Operators*, and the two-sided signed family is *Two-Sided Operators with the Signed Product*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{L}^{\alpha}_a = L_a\circ\alpha$ | Signed left multiplication, argument twisted |
| $\mathrm{P}^{\alpha}_a = R_{\alpha(a)}$ | Signed right multiplication, parameter twisted |
| $\mathrm{L}^{\alpha}_a\mathrm{L}^{\alpha}_c = L_{a\alpha(c)}$ | Two signed lefts give an ordinary left |
| $\mathrm{P}^{\alpha}_a\mathrm{P}^{\alpha}_c = \mathrm{P}^{\alpha}_{ca}$ | The signed right family is a group |
| $\mathrm{Fix}(T)$ | Fixed space of $T$ |
| $\mathrm{Fix}(L_{\lambda}\alpha)$ | Even part, odd part or $0$ for $\lambda = 1, -1$ or else |
| $\Sigma_x = \mathrm{L}^{\alpha}_x R_{\alpha(x)^{-1}}$ | The signed sandwich as a pairing |
| $\rho_u$, $u^{\perp}$ | Reflection and its fixed hyperplane |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the one-sided operators and the graded twist.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade involution and the one-sided multiplications.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the reflections and the pairing that stabilises the vectors.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the signed multiplications in the low-dimensional algebras.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the reflections and the hyperplane $u^{\perp}$.
