# __The Sandwich on a Clifford Algebra__

## Introduction

Let $V$ be a finite-dimensional vector space over a field $F$ of characteristic not $2$, let $q$ be a non-degenerate quadratic form on $V$ with polar form $B$, and let $\mathrm{Cl}(V,q)$ be its Clifford algebra. The **sandwich** attached to a pair $a, b \in \mathrm{Cl}(V,q)$ is the two-sided operator

$$
T_{a,b} : \mathrm{Cl}(V,q) \longrightarrow \mathrm{Cl}(V,q), \qquad T_{a,b}(y) = a\,y\,b .
$$

It is the most primitive two-sided operator the algebra carries: the left multiplication $L_a$ followed by the right multiplication $R_b$, the two composites agreeing because the product is associative. Everything later in the family is a restriction of it. Setting $b = a^{-1}$ gives the inner conjugation, setting $b = a^{\dagger}$ gives the Hermitian sandwich once the base carries an involution, and setting $b = a^{r}$ or $b = a^{\natural}$ gives the two intrinsic sandwiches.

The pair is genuinely two parameters. The operator remembers the product $ab$ and forgets the split of that product between the two sides, so different pairs give the same operator, and the ambiguity is by a central unit. The first half of this article fixes the operator, its composition law, its kernel and its two-parameter indeterminacy.

The second half concerns the quadratic space. A sandwich whose two parameters are a versor and its inverse maps $V$ to itself, and the orthogonal transformation it induces is not quite the classical twisted conjugation: the two differ by the parity sign of the versor. The **versor action** is the one that is correct on both parities, and it is the action on which the pin and spin groups are built.

The classification of all two-sided operators, with a left factor carrying an automorphism and a right factor carrying an anti-automorphism, and its five members, is *Two-Sided Operators on a Clifford Algebra*; nothing of that general theory is repeated here. The groups cut out of the versors are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the plain inner conjugation, its kernel and its action through the twisted conjugation, is *The Inner Conjugation on the Two-Sided Operators*; and its signed twin is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*. This article owns the two-parameter product, its composition and indeterminacy, and the way the sandwich of a versor meets the twisted conjugation on $V$. The algebra, its grading and its three intrinsic involutions are *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*.

## The Two-Parameter Sandwich

### Definition and Linearity

**Definition.** For $a, b \in \mathrm{Cl}(V,q)$ the **sandwich** by the pair $(a,b)$ is $T_{a,b}(y) = a\,y\,b$. In terms of the one-sided multiplications,

$$
T_{a,b} = L_a \circ R_b = R_b \circ L_a .
$$

The two composites agree because the product of the algebra is associative, so no parenthesis is needed.

**Proposition.** $T_{a,b}$ is $F$-linear, and for a central scalar $\lambda \in F$ one has $T_{\lambda a, b} = T_{a, \lambda b} = \lambda T_{a,b}$. In particular $T_{1,1} = \mathrm{id}$ and $T_{0,b} = T_{a,0} = 0$.

**Proof.** Both one-sided multiplications are $F$-linear by the axioms of the algebra, and the scalar is central.

### Composition

**Proposition (the composition law).** For all $a,b,c,d \in \mathrm{Cl}(V,q)$,

$$
T_{a,b} \circ T_{c,d} = T_{ac,\,db} .
$$

**Proof.** For every $y$, $T_{a,b}\bigl(T_{c,d}(y)\bigr) = a\,(c\,y\,d)\,b = (ac)\,y\,(db)$ by associativity.

The law is the semi-direct product of the two one-sided families and it is worth reading off its two consequences. The parameters multiply on the left and on the right **independently and without reversal**: the left factors compose as $a c$ and the right factors as $d b$. So the set of sandwiches is a monoid isomorphic to the direct product of the multiplicative monoids of the algebra with the reverse order on the second factor,

$$
\{T_{a,b}\} \cong \mathrm{Cl}(V,q)^{\mathrm{op}} \times \mathrm{Cl}(V,q) ,
$$

where $\mathrm{Cl}(V,q)^{\mathrm{op}}$ has the reversed product.

**Corollary (units).** $T_{a,b}$ is a bijection if and only if $a$ and $b$ are units; then $T_{a,b}^{-1} = T_{a^{-1}, b^{-1}}$.

**Proof.** If $a, b$ are units the inverse is the composition law applied twice. Conversely, if $L_aR_b$ is injective then $R_b$ is injective, and if it is surjective then $L_a$ is surjective; in a finite-dimensional algebra an injective right multiplication has $b$ a unit, and a surjective left multiplication has $a$ a unit, a one-sided inverse there being two-sided.

### The Kernel and the Value at the Unit

**Proposition.** $T_{a,b}(1) = ab$; in particular the sandwich that is the identity map must have $ab = 1$, and the pairs that actually give the identity are determined below.

**Proposition (the indeterminacy).** Let $a, b, a', b'$ be units. Then $T_{a,b} = T_{a',b'}$ if and only if there is a unit $c$ in the centre $Z(\mathrm{Cl}(V,q))$ with

$$
a' = a\,c, \qquad b' = c^{-1} b .
$$

**Proof.** If $T_{a,b} = T_{a',b'}$, then evaluating at $y = 1$ gives $a'b' = ab$, so $a^{-1}a' = b\,b'^{-1} =: c$. For every $y$,

$$
a\,c\,y\,b' = a'\,y\,b' = a\,y\,b = a\,y\,b'\,c ,
$$

so $c\,y = y\,c$ for every $y$, and $c$ is central. Conversely if $c$ is central then $a'yb' = acyc^{-1}b = ayb$.

**Corollary (the kernel).** The sandwiches that act as the identity are exactly the pairs $(c, c^{-1})$ with $c$ a unit of the centre,

$$
\ker\bigl((a,b) \mapsto T_{a,b}\bigr) = \{\, (c, c^{-1}) : c \in Z(\mathrm{Cl}(V,q))^{\times} \,\}.
$$

In even dimension the centre is $F$, so the kernel is the scalars $F^{\times}$; in odd dimension the centre is $F \oplus F\omega$ with $\omega$ the volume element, so the kernel is $F^{\times} \cup F^{\times}\omega$ in the diagonal of the unit group.

## The Versor Action on the Quadratic Space

### The Twisted Conjugation

**Definition.** Let $x \in \mathrm{Cl}(V,q)^{\times}$ be a unit. The **twisted conjugation** by $x$ is

$$
\chi_x : \mathrm{Cl}(V,q) \longrightarrow \mathrm{Cl}(V,q), \qquad \chi_x(y) = x\,y\,\alpha(x)^{-1},
$$

where $\alpha$ is the grade involution. It is the sandwich by the pair $(x, \alpha(x)^{-1})$.

**Definition.** An element $x$ is a **versor** when $\chi_x$ preserves the vector space $V$, that is when $\chi_x(V) \subseteq V$. The set of versors is the **Clifford group** $\Gamma(V,q)$.

**Remark (the two forms of the definition).** A versor is usually defined by the condition $x\,v\,x^{-1} \in V$ for every $v \in V$; the two conditions are equivalent because $\alpha(x)^{-1}$ differs from $x^{-1}$ by the central scalar $\varepsilon_x = \pm 1$ on a homogeneous element, and a central scalar carries $V$ to itself. The article *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* uses the second form and proves the equivalence; here the first form is the convenient one because it is a sandwich.

### The Sandwich of a Versor

**Proposition (the relation to the sandwich).** Let $x$ be homogeneous of degree $k$ and let $\varepsilon_x = (-1)^{k}$, so that $\alpha(x) = \varepsilon_x x$. Then for every $y$,

$$
\chi_x(y) = \varepsilon_x\, T_{x, x^{-1}}(y) = \varepsilon_x\, x\,y\,x^{-1}.
$$

On the space of vectors the sandwich and the twisted conjugation therefore differ by the parity sign, and they agree exactly on the even part of $\Gamma(V,q)$.

**Proof.** The inverse of the grade involution is again $\alpha$, and on a homogeneous element $\alpha(x)^{-1} = \varepsilon_x x^{-1}$ because $\varepsilon_x^{2} = 1$. Substituting gives the displayed identity.

**Theorem (the versor action is orthogonal).** Let $x \in \Gamma(V,q)$. Then the restriction of $\chi_x$ to $V$ is an isometry of the quadratic space,

$$
q\bigl(\chi_x(v)\bigr) = q(v), \qquad B\bigl(\chi_x(v), \chi_x(w)\bigr) = B(v, w), \qquad v, w \in V .
$$

Consequently $\chi_x\big|_{V} \in O(V,q)$, and the map $x \mapsto \chi_x\big|_{V}$ is a homomorphism from $\Gamma(V,q)$ onto $O(V,q)$.

**Proof.** On a vector $v$ one has $v^{2} = q(v)\cdot 1$, and since $\alpha$ is an algebra automorphism fixing $F$ it carries the fundamental relation to $(x v \alpha(x)^{-1})^{2} = q(v)\cdot 1$, which is exactly the statement that $\chi_x(v)$ is a vector of the same square. For a product of two vectors the polar identity $B(v,w) = \tfrac12\bigl(q(v+w) - q(v) - q(w)\bigr)$ gives the bilinear statement. Surjectivity is quoted from *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

**Corollary (Cartan–Dieudonné, one step).** If $u \in V$ with $q(u) \neq 0$, then $\chi_u = \rho_u$ is the reflection in the hyperplane $u^{\perp}$; if $x \in \Gamma(V,q)$ is even, then $\chi_x = \mathrm{Ad}_x$ is a rotation, the product of an even number of reflections.

**Proof.** For a vector, $\varepsilon_u = -1$, so $\chi_u(v) = -u v u^{-1}$, and the fundamental relation $uvu = 2B(u,v)u - q(u)v$ gives $\chi_u(v) = v - 2B(v,u)q(u)^{-1}u = \rho_u(v)$. The second statement is the same computation with $\varepsilon_x = 1$.

**Remark (why the versor action and not the sandwich).** Both maps are defined on the algebra, both are bijections, and both preserve $V$ when $x$ is a versor. Only the twisted conjugation is orthogonal on every parity. The sandwich $T_{x,x^{-1}}$ agrees with it on the even part and is its negative on the odd part, which is why the reflections are carried by the twisted conjugation and the rotations by either.

## Worked Cases

### An Odd Versor in $\mathrm{Cl}_{0,3}(\mathbb{R})$

With $e_j^{2} = -1$ let $x = e_1$. Then $x$ is a versor, $\varepsilon_x = -1$, $x^{-1} = -e_1$, and $T_{x,x^{-1}} = \mathrm{Ad}_{e_1}$ acts on the basis by $(e_1, -e_2, -e_3)$, while

$$
\chi_{e_1} = -\mathrm{Ad}_{e_1} \quad \text{acts by} \quad (-e_1, e_2, e_3),
$$

which is $\rho_{e_1}$, the reflection in $e_1^{\perp}$, since $\rho_{e_1}(e_1) = -e_1$ when $q(e_1) = -1$ and $\rho_{e_1}$ fixes $e_2, e_3$. Indeed $\alpha(e_1)^{-1} = (-e_1)^{-1} = e_1$, so $\chi_{e_1}(v) = e_1\,v\,e_1$, and

$$
\chi_{e_1}(e_1) = e_1^{3} = -e_1, \qquad \chi_{e_1}(e_2) = e_1e_2e_1 = -e_1^{2}e_2 = e_2, \qquad \chi_{e_1}(e_3) = e_3 .
$$

The sandwich gives the negative $\mathrm{Ad}_{e_1} = -\rho_{e_1}$ and is the wrong action for an odd versor.

### An Even Versor and a Rotation

In the same algebra let $R = e_1e_2$. Then $R$ is even, $\varepsilon_R = 1$, so $\chi_R = T_{R,R^{-1}} = \mathrm{Ad}_R$, and with $R^{-1} = -e_1e_2$,

$$
\chi_R(e_1) = -e_1, \qquad \chi_R(e_2) = -e_2, \qquad \chi_R(e_3) = e_3 ,
$$

the half-turn of the plane spanned by $e_1, e_2$. The value at the unit is $R R^{-1} = 1$, and the sandwich fixes the unit.

### A Central Indeterminacy

In $\mathrm{Cl}_{0,3}$ the volume element $\omega = e_1e_2e_3$ is central and odd with $\omega^{2} = 1$, so $\omega$ is a unit of the centre and

$$
T_{\omega a, \omega^{-1} b} = T_{a, b}
$$

for every pair. Taking the pair $(a,b) = (e_1, -e_1)$, whose operator is $\mathrm{Ad}_{e_1}$, the central unit $\omega$ gives the different pair

$$
a' = \omega e_1 = -e_2e_3, \qquad b' = \omega^{-1}(-e_1) = -\omega e_1 = e_2e_3 ,
$$

and $T_{-e_2e_3,\,e_2e_3} = T_{e_1,-e_1}$, which is the worked form of the indeterminacy by a central unit.

### A Non-Versor

Let $x = 1 + e_1e_2e_3 = 1 + \omega$ in $\mathrm{Cl}_{0,3}$. Then $x^{2} = 1 + 2\omega + \omega^{2} = 2(1+\omega) = 2x$, so $x$ is not invertible and no sandwich with $b = \alpha(x)^{-1}$ is defined; the pair $(x, x)$ still gives the linear map $T_{x,x}$, whose value at the unit is $2x \notin F$. The example isolates invertibility, which is the only hypothesis the twisted conjugation shares with the sandwich.

## Summary

The **sandwich** $T_{a,b}(y) = a\,y\,b$ is the general two-parameter two-sided operator on a Clifford algebra, the composite $L_aR_b$ of a left and a right multiplication. It is $F$-linear, its composition law is $T_{a,b}T_{c,d} = T_{ac, db}$ with the left factors in the written order and the right factors reversed, and the sandwiches form a monoid isomorphic to $\mathrm{Cl}(V,q)^{\mathrm{op}} \times \mathrm{Cl}(V,q)$. It is invertible exactly when $a$ and $b$ are units, with $T_{a,b}^{-1} = T_{a^{-1},b^{-1}}$. It remembers the product $ab$ and the value $T_{a,b}(1) = ab$; two pairs give the same operator exactly when they differ by a central unit, $a' = ac$ and $b' = c^{-1}b$ with $c \in Z(\mathrm{Cl}(V,q))^{\times}$, so the kernel of the parametrisation is the diagonal of the central units.

Restricted to the quadratic space, the sandwich of a versor is the inner conjugation, and the correct action on $V$ is the **twisted conjugation** $\chi_x(y) = x\,y\,\alpha(x)^{-1}$, the sandwich by $(x, \alpha(x)^{-1})$; the two differ by the parity sign, $\chi_x = \varepsilon_x T_{x,x^{-1}}$, so they agree on the even part of the Clifford group and are negatives on the odd part. The twisted conjugation of a versor is an isometry of $V$, a vector gives the reflection $\rho_u = \chi_u$, and an even versor gives a rotation; the map $x \mapsto \chi_x\big|_V$ is the homomorphism $\Gamma(V,q) \to O(V,q)$ on which the pin and spin groups are built. The article owns the two-parameter product and the versor action alone; the general operator family is *Two-Sided Operators on a Clifford Algebra*, and the groups are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V$, $q$, $B$ | Quadratic space, quadratic form and its polar form |
| $\mathrm{Cl}(V,q)$ | Clifford algebra of $(V,q)$ |
| $L_a$, $R_b$ | Left and right multiplication by $a$ and $b$ |
| $T_{a,b}(y) = a\,y\,b$ | The two-parameter sandwich |
| $T_{a,b}T_{c,d} = T_{ac,db}$ | Composition law |
| $T_{a,b}(1) = ab$ | Value at the unit |
| $(ac, c^{-1}b)$, $c \in Z(\mathrm{Cl})^{\times}$ | The indeterminacy of the parametrisation |
| $\alpha$, $\varepsilon_x = (-1)^{k}$ | Grade involution and the parity sign |
| $\chi_x(y) = x\,y\,\alpha(x)^{-1}$ | Twisted conjugation |
| $\chi_x = \varepsilon_x T_{x,x^{-1}}$ | Relation between the twisted conjugation and the sandwich |
| $\Gamma(V,q)$ | Clifford group, the versors |
| $\rho_u(v) = v - 2B(v,u)q(u)^{-1}u$ | Reflection in $u^{\perp}$ |
| $\omega$ | Volume element |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the twisted conjugation $x\,v\,\alpha(x)^{-1}$ and the Lipschitz group.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the sandwich action, the Clifford group and the reflections.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the two-sided operators and the centre of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the reflection formula and the two conjugation actions on vectors.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the orthogonal group generated by the reflections.
