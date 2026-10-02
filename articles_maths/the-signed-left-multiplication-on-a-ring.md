
# __The Signed Left Multiplication on a Ring__

## Introduction

The **signed left multiplication** by an element $a$ of a graded ring is the twist of the ordinary left multiplication by the grade involution:
$$T_a(x) = a\,\alpha(x).$$
It is not an endomorphism of the ring — it is not even multiplicative in the ordinary sense — but it is a twisted homomorphism, $T_a(xy) = T_a(x)\,\alpha(y)$, and it is the one-sided operator out of which the reflection $r_u = T_u\circ R_{u^{-1}}$ is built. This article studies $T_a$ as an operator: its relation to the plain left multiplication $L_a$, its composition and twisted multiplicativity, its kernel and image, and the point at which it becomes an automorphism.

The signed left multiplication is the one-sided member of the signed family of *The Signed Sandwich on a Ring*: with a right factor it gives the signed sandwich $S^{\alpha}_{a,b} = T_a\circ R_b$, and with the unit as right factor it gives the reflection. The article stays inside Part I: the grade involution $\alpha$ is an automorphism of the ring, the operator $T_a$ is additive, and no distance, form or norm occurs. The comparison throughout is with the plain left multiplication $L_a(x) = ax$ of *Left and Right Multiplication in a Ring*, which is recovered as the case $\alpha = \mathrm{id}$.

Throughout, $A$ is a ring with $1 \neq 0$, not assumed commutative; $\alpha$ is a grade involution, $\alpha^2 = \mathrm{id}$; $L_a$, $R_a$ are the one-sided multiplications; and $T_a$ is the signed left multiplication. The notation $\alpha A$ means the image of $A$ under $\alpha$, which is $A$ itself.

## Definition and the Relation to the Plain Left Multiplication

### Definition

**Definition.** Let $A$ be a ring with grade involution $\alpha$. For $a \in A$ the **signed left multiplication** by $a$ is the additive map

$$
T_a : A \to A, \qquad T_a(x) = a\,\alpha(x).
$$

It is the composite $T_a = L_a \circ \alpha$ of the grade involution with a left multiplication, and it is also the composite $\alpha \circ L_{\alpha(a)}$ of a left multiplication with $\alpha$.

**Proposition.** For all $a \in A$,

$$
T_a = L_a \circ \alpha = \alpha \circ L_{\alpha(a)}, \qquad T_a(1) = a, \qquad T_{a+b} = T_a + T_b, \qquad T_a = 0 \iff a = 0 .
$$

Hence $a \mapsto T_a$ is an injective additive map $A \to \operatorname{End}(A)$, and $T_a = T_b$ if and only if $a = b$.

**Proof.** $L_a(\alpha(x)) = a\alpha(x)$ and $\alpha(L_{\alpha(a)}(x)) = \alpha(\alpha(a)x) = \alpha^2(a)\alpha(x) = a\alpha(x)$. The value at the unit is $T_a(1) = a\alpha(1) = a$; additivity in the parameter follows from the distributivity; and $T_a = 0$ forces $a = T_a(1) = 0$, while $a=0$ gives the zero map. The value at the unit also separates the parameters.

### The relation to the plain left multiplication

The two operators are related by conjugation with the grade involution, and this is the precise sense in which the signed left multiplication is the plain one twisted.

**Proposition.** For all $a \in A$,

$$
T_a = L_a\circ\alpha, \qquad T_{\alpha(a)} = \alpha\circ L_a, \qquad L_a = T_a\circ\alpha, \qquad \alpha\,L_a\,\alpha^{-1} = L_{\alpha(a)} .
$$

**Proof.** The first is the definition. The second is $\alpha L_a(x) = \alpha(ax) = \alpha(a)\alpha(x) = T_{\alpha(a)}(x)$. The third is $T_a(\alpha(x)) = a\alpha^2(x) = ax$. The fourth follows from the first two, $\alpha L_a\alpha^{-1} = T_{\alpha(a)}\alpha = L_{\alpha(a)}$, and it is the conjugation law already recorded in *The Signed Sandwich on a Ring*.

**Corollary (recovering the plain case).** $T_a = L_a$ for every $a$ exactly when $\alpha = \mathrm{id}$; for a nontrivial grade involution the two families differ whenever $\alpha(a) \neq a$ somewhere, that is, whenever $A$ has a nonzero odd part.

## The Multiplicative Structure

### The twisted product rule

The signed left multiplication is not a ring endomorphism, but it is a homomorphism twisted by $\alpha$, and the twist is exactly the price of the sign in the middle.

**Proposition (twisted multiplicativity).** For all $a, x, y \in A$,

$$
T_a(xy) = T_a(x)\,\alpha(y) .
$$

Thus $T_a$ is a homomorphism **twisted by $\alpha$** on the right.

**Proof.** $T_a(xy) = a\alpha(xy) = a\alpha(x)\alpha(y) = T_a(x)\alpha(y)$.

**Remark.** The companion identity $T_a(xy) = \alpha(x)T_{\alpha^{-1}(a)}(y)$ would require moving $a$ past $\alpha(x)$ and holds only when $a$ commutes with the image of $\alpha$; the first display is the one valid in general. The twist always sits on the second factor, which is the operator form of the sign in the middle of the graded product.

**Corollary.** $T_a$ is a unital ring endomorphism exactly when $a = 1$, and then $T_1 = \alpha$. In general $T_a$ is a twisted homomorphism and not an ordinary one.

### Composition

**Proposition.** For all $a, b \in A$,

$$
T_a \circ T_b = L_{a\,\alpha(b)}, \qquad T_a \circ L_b = T_{a\,\alpha(b)}, \qquad L_b \circ T_a = T_{ba} .
$$

**Proof.** $T_a(T_b(x)) = a\alpha(b\alpha(x)) = a\alpha(b)\alpha^2(x) = a\alpha(b)\,x = L_{a\alpha(b)}(x)$. Next, $T_a(L_b(x)) = a\alpha(bx) = a\alpha(b)\alpha(x) = T_{a\alpha(b)}(x)$. Finally, $L_b(T_a(x)) = b\,a\,\alpha(x) = T_{ba}(x)$.

**Corollary (the monoid generated by the plain and signed left multiplications).** The set $\{L_a, T_a : a \in A\}$ is closed under composition and contains the identity $L_1$; it is a monoid of endomorphisms of the additive group $A$. Its composition law is that of the semidirect product $A \rtimes A$ twisted by $\alpha$, in which $(a,0)$ denotes $L_a$ and $(a,1)$ denotes $T_a$ and

$$
(a,0)(b,0) = (ab,0), \quad (a,0)(b,1) = (ab,1), \quad (a,1)(b,0) = (a\alpha(b),1), \quad (a,1)(b,1) = (a\alpha(b),0) .
$$

In particular the product of two signed left multiplications is a plain left multiplication, and the product of one of each is a signed one.

### Comparison with the reflection and the sandwich

**Proposition.** For a unit $u$ the reflection of *Reflections as Signed Two-Sided Operators on a Ring* factors through the signed left multiplication:

$$
r_u(x) = u\,\alpha(x)\,u^{-1} = T_u\bigl(R_{u^{-1}}(x)\bigr) = \bigl(T_u \circ R_{u^{-1}}\bigr)(x),
$$

and generally the signed sandwich is $S^{\alpha}_{a,b} = T_a \circ R_b$ for all $a, b \in A$.

**Proof.** $T_u(R_{u^{-1}}(x)) = T_u(xu^{-1}) = u\alpha(xu^{-1}) = u\alpha(x)\alpha(u)^{-1} = u\alpha(x)u^{-1}$, since $\alpha(u^{-1}) = \alpha(u)^{-1}$; the sandwich statement is the definition $S^{\alpha}_{a,b}(x) = a\alpha(x)b$ together with $R_b(x) = xb$.

## Kernel, Image and Invertibility

### Kernel and image

**Proposition.** For $a \in A$,

$$
\ker T_a = \alpha^{-1}\bigl(\ell(a)\bigr), \qquad \operatorname{im} T_a = Aa,
$$

where $\ell(a) = \{x : ax = 0\}$ is the left annihilator. Hence the image of $T_a$ is the same left ideal as the image of $L_a$, and the kernel is the $\alpha$-pullback of the left annihilator of $a$.

**Proof.** $T_a(x) = 0 \iff a\alpha(x) = 0 \iff \alpha(x) \in \ell(a) \iff x \in \alpha^{-1}(\ell(a))$. The image is $\{a\alpha(x)\} = a\,\alpha(A) = aA = Aa$, since $\alpha$ is onto and $Aa = \{ax\}$.

### Invertibility

**Proposition.** For $a \in A$, the operator $T_a$ is invertible if and only if $a \in A^\times$, and then

$$
T_a^{-1} = T_{\alpha(a)^{-1}} = T_{\alpha(a^{-1})}.
$$

**Proof.** If $T_a$ is bijective then $T_a(1) = a$ has a two-sided inverse by surjectivity and $a$ is not a zero divisor by injectivity, so $a$ is a unit. Conversely, $T_a T_{\alpha(a^{-1})}(x) = a\alpha(\alpha(a^{-1})\alpha(x)) = a\,a^{-1}\alpha^2(x) = x$, and the opposite composite is computed the same way; so $T_a$ is invertible with that inverse. The two displayed forms of the inverse agree because $\alpha(a^{-1}) = \alpha(a)^{-1}$.

**Corollary.** The signed left multiplications by the units form, together with the plain left multiplications by the units, the two-sided version of the unit group's one-sided action: $T_u = L_u\alpha$ and $T_u^{-1} = T_{\alpha(u)^{-1}}$, so $u \mapsto T_u$ is a map from $A^\times$ onto a set of invertible operators with the composition $T_uT_v = L_{u\alpha(v)}$.

### The elements fixed by a signed left multiplication

**Proposition.** For $a \in A$ the fixed set

$$
\operatorname{Fix}(T_a) = \{x \in A : a\,\alpha(x) = x\}
$$

is an additive subgroup of $A$; it is an eigenspace of the grade involution exactly for $a = \pm 1$,

$$
\operatorname{Fix}(T_1) = \operatorname{Fix}(\alpha) = A_{\bar 0}, \qquad \operatorname{Fix}(T_{-1}) = A_{\bar 1},
$$

the even and the odd part; and $\operatorname{Fix}(T_0) = \{0\}$.

**Proof.** If $a\alpha(x)=x$ and $a\alpha(y)=y$ then $a\alpha(x+y)=x+y$, so the fixed set is an additive subgroup; it contains $0$. For $a=1$ the equation is $\alpha(x)=x$, whose solutions are $A_{\bar0}$; for $a=-1$ it is $-\alpha(x)=x$, that is $\alpha(x)=-x$, whose solutions are $A_{\bar1}$; and for $a=0$ it is $0=x$.

## Examples

**(a) The trivial grade involution.** If $\alpha = \mathrm{id}$ then $T_a = L_a$ for every $a$, and the whole article collapses to the plain left multiplication. The signed operators are new only when the grading is nontrivial.

**(b) The sign on the odd part.** For every $a$, the signed and the plain left multiplications agree on the even part and differ by a sign on the odd part: for homogeneous $x$,

$$
T_a(x) = L_a(x) \ \text{ if } x \in A_{\bar 0}, \qquad T_a(x) = -L_a(x) \ \text{ if } x \in A_{\bar 1},
$$

because $\alpha(x) = \pm x$ according to the parity of $x$. So $T_a = L_a$ as operators exactly when $A = A_{\bar 0}$, that is, when $\alpha = \mathrm{id}$; otherwise the two families differ on every nonzero odd element, and the sign is carried by the parity of the **argument**, not by the parity of the parameter $a$.

**(c) The matrix ring with a grading.** In $A = M_2(k)$ with $\alpha = \operatorname{conj}_J$, $J = \operatorname{diag}(1,-1)$, the even part is the diagonal matrices and the odd part the off-diagonal ones, and the sign rule of (b) applies. For the unit $u = E_{12}+E_{21}$, which is odd with $\alpha(u) = -u$, the composition law gives

$$
T_u^2 = T_uT_u = L_{u\alpha(u)} = L_{-u^2} = L_{-I} = -L_I,
$$

so $T_u^2$ is the negation of the identity and $T_u$ is not an involution; the reflection $r_u = T_uR_{u^{-1}}$ nevertheless satisfies $r_u^2 = \operatorname{conj}_{u\alpha(u)} = \operatorname{conj}_{-I} = \mathrm{id}$, because $-I$ is central.

**(d) The graded action on a module.** When $M$ is a graded module over a graded ring and the action is required to respect the grading, the operators that occur are precisely the signed left multiplications $T_a$ with $a$ homogeneous, the case of *The Graded Action on a Module over a Ring*.

## Summary

For a ring $A$ with a grade involution $\alpha$, the **signed left multiplication** by $a$ is $T_a(x) = a\alpha(x) = L_a\circ\alpha = \alpha\circ L_{\alpha(a)}$. It is additive in its parameter with $T_a(1) = a$ and injective in $a$, and it recovers the plain left multiplication as $L_a = T_a\circ\alpha$, so that the two families coincide exactly when $\alpha = \mathrm{id}$. It is not a ring endomorphism but a **twisted** one: $T_a(xy) = T_a(x)\alpha(y)$. Its compositions are $T_aT_b = L_{a\alpha(b)}$, $T_aL_b = T_{a\alpha(b)}$ and $L_bT_a = T_{ba}$, so the plain and signed left multiplications together form a monoid, the twisted semidirect product $A \rtimes A$, and the reflection and the signed sandwich factor through it as $S^{\alpha}_{a,b} = T_aR_b$ and $r_u = T_uR_{u^{-1}}$. The kernel of $T_a$ is $\alpha^{-1}(\ell(a))$, its image is the left ideal $Aa$, and it is invertible exactly when $a$ is a unit, with inverse $T_{\alpha(a)^{-1}}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\alpha$ | Ring with $1 \neq 0$ and its grade involution |
| $T_a(x) = a\alpha(x)$ | Signed left multiplication by $a$ |
| $T_a = L_a\alpha = \alpha L_{\alpha(a)}$ | Relation to the plain left multiplication |
| $L_a = T_a\alpha$ | Recovery of the plain left multiplication |
| $T_a(xy) = T_a(x)\alpha(y)$ | Twisted multiplicativity |
| $T_aT_b = L_{a\alpha(b)}$ | Product of two signed left multiplications is plain |
| $T_aL_b = T_{a\alpha(b)}$, $L_bT_a = T_{ba}$ | Mixed composition laws; the monoid $A\rtimes A$ |
| $\ker T_a = \alpha^{-1}(\ell(a))$ | Kernel, the $\alpha$-pullback of the left annihilator |
| $\operatorname{im} T_a = Aa$ | Image, the left ideal generated by $a$ |
| $T_a^{-1} = T_{\alpha(a)^{-1}}$ | Inverse on the units |
| $S^{\alpha}_{a,b} = T_aR_b$, $r_u = T_uR_{u^{-1}}$ | Sandwich and reflection through $T$ |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the graded structures of an algebra with an involution and the twisted multiplications.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the signed one-sided operators of a Clifford algebra and their composition.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the parity sign and the graded multiplications.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the semilinear maps and the twisted endomorphism rings of a graded algebra.
