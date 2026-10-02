
# __The Signed Adjoint of the Left Multiplication on a Symmetry Group__

## Introduction

The signed left multiplication is the one-sided member of the signed layer, $\Lambda^{\alpha}_a(x) = a\,\alpha(x)$, and its adjoint with respect to the invariant form is a signed left multiplication again, by the adjointed parameter:

$$
\bigl(\Lambda^{\alpha}_a\bigr)^{*} = \Lambda^{\alpha}_{\alpha(a)^{*}} .
$$

The one-sided case is where the adjoint formula is at its simplest — no reverse product appears, because a left multiplication has no other factor — and it is the building block of the two-sided case, since the signed sandwich factors as a signed left multiplication followed by a right multiplication and its adjoint factors the same way. The signed left multiplication is not closed under composition, so the set of the adjoints is not a group, and the unitarity condition is the single equation $\alpha(a)^{*}\alpha(a) = e$ rather than the two conditions of the two-sided case.

The article treats the signed left multiplication as an operator, its adjoint, the factorisation of the signed sandwich by the adjoint, and the fixed elements. The signed left multiplication, its parity sign, its composition law and its inverse are *The Signed Left Multiplication on a Symmetry Group*; the adjoint of the general signed sandwich is *The Signed Adjoint Sandwich on a Symmetry Group*, the previous article, of which this is the one-sided factor; the adjoint of a symmetry operator and the operator involution are *The Adjoint of a Symmetry Operator*, the first article of this group; the graded structure and the Clifford case are *The Signed Sandwich on a Symmetry Group*, *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* and *Involutive Graded Algebras*. The grade involution $\alpha$ is the parity of the grading and not the involution of the group `- * Theory`; the two-structures question of an involution on the elements against the adjoint on the operators is settled in *The Adjoint of a Symmetry Operator* and is cited only.

The article has four sections: the signed left multiplication; its adjoint; the factorisation and the sandwich; and the worked cases. Throughout, $G$ is a graded group with central sign element $z$ and grade involution $\alpha(g) = \varepsilon(g)g$, $A = kG$ the group algebra over a field $k$ of characteristic not $2$ with involution $x \mapsto x^{*}$ and trace form $\langle x, y\rangle = \tau(x^{*}y)$, the grade involution a `*`-automorphism preserving the trace, and $L_a(x) = ax$, $\Lambda^{\alpha}_a(x) = a\alpha(x)$ the left multiplications.

## The Signed Left Multiplication

### The Operator

**Definition.** The **signed left multiplication** by $a$ is the operator

$$
\Lambda^{\alpha}_a : G \longrightarrow G, \qquad \Lambda^{\alpha}_a(x) = a\,\alpha(x),
$$

the composite of the left multiplication and the grade involution in either order, $\Lambda^{\alpha}_a = L_a\circ\alpha = \alpha\circ L_{\alpha(a)}$; it is the one-sided member of the signed layer of *The Signed Left Multiplication on a Symmetry Group*.

**Proposition.** The signed left multiplication is a bijection with inverse $(\Lambda^{\alpha}_a)^{-1} = \Lambda^{\alpha}_{\alpha(a)^{-1}}$; it agrees with the unsigned left multiplication on the even part and differs by the sign element on the odd part, $\Lambda^{\alpha}_a(x) = \varepsilon(x)L_a(x)$; and the composite of two is an ordinary left multiplication,

$$
\Lambda^{\alpha}_a \circ \Lambda^{\alpha}_b = L_{a\alpha(b)},
$$

so the signed left multiplications are not closed under composition and form a coset of the left multiplications in the group they generate with the grade involution.

**Proof.** The inverse and the parity sign are *The Signed Left Multiplication on a Symmetry Group*; the composite is $\Lambda^{\alpha}_a(\Lambda^{\alpha}_b x) = a\alpha(b\alpha(x)) = a\alpha(b)\alpha^2(x) = a\alpha(b)x$.

**Remark.** The one-sided signed operator is a bijection whose class is not a group: the composite of two signed left multiplications is unsigned, exactly as the composite of two signed sandwiches is unsigned. The adjoint below inherits this one-sidedness.

## The Adjoint of the Signed Left Multiplication

### The Formula

**Theorem (the signed adjoint of the left multiplication).** The adjoint of the signed left multiplication with respect to the trace form is the signed left multiplication by the adjointed parameter,

$$
\bigl(\Lambda^{\alpha}_a\bigr)^{*} = \Lambda^{\alpha}_{\alpha(a)^{*}}, \qquad\text{that is}\qquad \bigl(\Lambda^{\alpha}_a\bigr)^{*}(y) = \alpha(a)^{*}\,\alpha(y) .
$$

**Proof.** Use the factorisation $\Lambda^{\alpha}_a = \alpha\circ L_{\alpha(a)}$: the adjoint of a composite is the composite of the adjoints in reverse order, $(\alpha L_{\alpha(a)})^{*} = L_{\alpha(a)}^{*}\alpha^{*}$, and $L_{b}^{*} = L_{b^{*}}$, $\alpha^{*} = \alpha$ from *The Signed Adjoint Sandwich on a Symmetry Group*, so
$$
\bigl(\Lambda^{\alpha}_a\bigr)^{*} = L_{\alpha(a)^{*}}\circ\alpha = \Lambda^{\alpha}_{\alpha(a)^{*}} .
$$
Directly: $\langle \Lambda^{\alpha}_a(x), y\rangle = \tau((a\alpha(x))^{*}y) = \tau(\alpha(x)^{*}a^{*}y) = \tau(\alpha(x^{*})a^{*}y) = \tau(x^{*}\alpha(a^{*}y)) = \tau(x^{*}\alpha(a)^{*}\alpha(y)) = \langle x, \alpha(a)^{*}\alpha(y)\rangle$.

### The Parity Sign and the Unitarity

**Proposition.** The adjoint of the signed left multiplication is the signed left multiplication with the parameter replaced by $\alpha(a)^{*}$; for $\alpha = \mathrm{id}$ the formula is $L_a^{*} = L_{a^{*}}$, the adjoint of the ordinary left multiplication. The signed left multiplication is unitary exactly when

$$
\alpha(a)^{*}\,\alpha(a) = e, \qquad \text{i.e.,} \qquad \alpha(a)^{*} = \alpha(a)^{-1},
$$

because the composite of the adjoint with the operator is an ordinary left multiplication,

$$
\bigl(\Lambda^{\alpha}_a\bigr)^{*}\Lambda^{\alpha}_a = \Lambda^{\alpha}_{\alpha(a)^{*}}\circ\Lambda^{\alpha}_a = L_{\alpha(a)^{*}\alpha(a)},
$$

which is the identity exactly when the parameter is the unit.

**Proof.** The adjoint formula is the theorem; the composite uses the composition law $\Lambda^{\alpha}_c\Lambda^{\alpha}_d = L_{c\alpha(d)}$ with $c = \alpha(a)^{*}$, $d = a$, giving $L_{\alpha(a)^{*}\alpha(a)}$; a left multiplication $L_c$ is the identity exactly when $c = e$.

**Remark.** The unitarity condition $\alpha(a)^{*}\alpha(a) = e$ is **one** equation, against the two of the two-sided case, because a left multiplication has one factor to be right-adjointed; the adjoint is nonetheless a signed left multiplication and not an unsigned one, so the sign structure survives the adjoint exactly as in the two-sided case.

## The Factorisation and the Sandwich

### The Factorisation

**Proposition.** The signed sandwich factors as a signed left multiplication followed by a right multiplication,

$$
S^{\alpha}_{a,b} = R_b\circ\Lambda^{\alpha}_a, \qquad S^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b,
$$

and its adjoint factors the same way, in reverse order:

$$
\bigl(S^{\alpha}_{a,b}\bigr)^{*} = \bigl(\Lambda^{\alpha}_a\bigr)^{*}\circ R_b^{*} = \Lambda^{\alpha}_{\alpha(a)^{*}}\circ R_{b^{*}} ,
$$

which is the formula $(S^{\alpha}_{a,b})^{*} = S^{\alpha}_{\alpha(a)^{*},\alpha(b)^{*}}$ of *The Signed Adjoint Sandwich on a Symmetry Group*.

**Proof.** The factorisation is the associativity of the product, $a\alpha(x)b = (a\alpha(x))b$; the adjoint of a composite reverses the order, and $R_b^{*} = R_{b^{*}}$, giving $\Lambda^{\alpha}_{\alpha(a)^{*}}R_{b^{*}}$; evaluating at $y$ gives $\alpha(a)^{*}\alpha(y)b^{*}$, which is $S^{\alpha}_{\alpha(a)^{*},\alpha(b)^{*}}(y)$ since $\alpha(b)^{*} = \alpha(b^{*})$ and $R_{b^{*}}(y) = yb^{*}$.

### The Two-Sided Case from the One-Sided Case

**Proposition.** The adjoint of the signed sandwich is the composite of the adjoint of the signed left multiplication with the adjoint of the right multiplication; hence the two-sided adjoint formula is the product of the one-sided formula and the right case, and the one-sided article is the atomic case of which the two-sided one is the product.

**Proof.** The adjoint of a composite is the reverse composite; the two factors are the signed left multiplication and the right multiplication, whose adjoints are the theorem above and $R_{b^{*}}$.

**Remark.** The relation is one of **factorisation**, not of reduction: the one-sided operator is not a special case of the two-sided one with $b = e$ alone, because the class of signed left multiplications is not closed under composition. The adjoint nonetheless commutes with the factorisation, which is the content of the proposition.

## Worked Cases

**Example (the trivial grading).** Let $\alpha = \mathrm{id}$; then the signed left multiplication is the ordinary left multiplication and the theorem is the `*`-algebra identity $L_a^{*} = L_{a^{*}}$, with the unitarity condition $a^{*}a = e$, which is the condition for the left multiplication to be an isometry of the trace form. The example specialises the sign away.

**Example (the cyclic group of order four).** Let $G = \mathbb{Z}/4$ with the sign element $z = 2$ and the grading by parity, even part $\{0,2\}$ and odd part $\{1,3\}$; the grade involution is $\alpha(g) = \varepsilon(g)g = -g$, the negation automorphism, with $\alpha(1) = 3$ and $\alpha(3) = 1$. The signed left multiplication $\Lambda^{\alpha}_a(x) = a + \alpha(x)$ is the affine map $x \mapsto a - x$, its adjoint is $\Lambda^{\alpha}_{-a}$, and it is unitary exactly when $-a = -a$, which always holds in this abelian case; the example is the smallest grading with a nonempty odd part and a genuine grade involution.

**Example (the Clifford and pin case).** Let $G = \mathrm{Pin}(V,q)$ and $A$ the Clifford algebra with its conjugation involution $x \mapsto x^{*}$, the grade involution $\alpha$ a `*`-automorphism preserving the trace form. The adjoint of the signed left multiplication is $\Lambda^{\alpha}_{\alpha(a)^{*}}$, and it is unitary exactly for $\alpha(a)$ unitary in the algebra, $\alpha(a)^{*} = \alpha(a)^{-1}$; for $a$ a unit vector the signed left multiplication is the Clifford multiplication by $a$ composed with the grade involution, and its adjoint is the multiplication by $a$ again when $a$ is real.

**Example (a failure of unitarity).** Let $a$ be an odd element with $\alpha(a)^{*} \neq \alpha(a)^{-1}$, for instance a vector $u$ with $u^{*} = -u$ in a complexified Clifford algebra; then $(\Lambda^{\alpha}_u)^{*}\Lambda^{\alpha}_u = L_{\alpha(u)^{*}\alpha(u)} \neq \mathrm{id}$, so the signed left multiplication is not unitary, and the failure is the same reality condition that fails for the signed reflection of *The Signed Adjoint of the Reflection on a Symmetry Group*.

## Summary

The signed left multiplication $\Lambda^{\alpha}_a(x) = a\alpha(x)$ is a bijection with inverse $\Lambda^{\alpha}_{\alpha(a)^{-1}}$, it agrees with the unsigned left multiplication on the even part and differs by the sign element on the odd part, and the composite of two is an ordinary left multiplication, so the class is not a group. Its adjoint with respect to the trace form is the signed left multiplication by the adjointed parameter,

$$
\bigl(\Lambda^{\alpha}_a\bigr)^{*} = \Lambda^{\alpha}_{\alpha(a)^{*}},
$$

proved by factorising $\Lambda^{\alpha}_a = \alpha\circ L_{\alpha(a)}$ and using $L_b^{*} = L_{b^{*}}$, $\alpha^{*} = \alpha$; the general formula for the unsigned case is $L_a^{*} = L_{a^{*}}$. The operator is unitary exactly when $\alpha(a)^{*}\alpha(a) = e$, a single equation, because the composite of the adjoint with the operator is the ordinary left multiplication $L_{\alpha(a)^{*}\alpha(a)}$. The signed sandwich factors as $S^{\alpha}_{a,b} = R_b\circ\Lambda^{\alpha}_a$ and its adjoint factors the same way in reverse order, giving the two-sided formula $(S^{\alpha}_{a,b})^{*} = S^{\alpha}_{\alpha(a)^{*},\alpha(b)^{*}}$ of the previous article; the one-sided case is the atomic factor of the two-sided one. The adjoint on a module over the group is the subject of the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $z$, $\alpha$ | graded group, sign element, grade involution |
| $A = kG$, $\langle x,y\rangle = \tau(x^{*}y)$ | the group algebra and the trace form |
| $L_a(x) = ax$ | the ordinary left multiplication |
| $\Lambda^{\alpha}_a(x) = a\alpha(x)$ | the signed left multiplication |
| $\Lambda^{\alpha}_a = \alpha\circ L_{\alpha(a)}$ | the factorisation with the grade involution |
| $(\Lambda^{\alpha}_a)^{*} = \Lambda^{\alpha}_{\alpha(a)^{*}}$ | the signed adjoint of the left multiplication |
| $(\Lambda^{\alpha}_a)^{*}\Lambda^{\alpha}_a = L_{\alpha(a)^{*}\alpha(a)}$ | the composite; the unitarity condition |
| $\alpha(a)^{*} = \alpha(a)^{-1}$ | the unitarity of the signed left multiplication |
| $S^{\alpha}_{a,b} = R_b\circ\Lambda^{\alpha}_a$ | the sandwich as a one-sided operator times a right multiplication |

## Further Reading

- Sterling K. Berberian, *Baer `*`-Rings* (Springer, 1972), for the adjoint of a left multiplication and the unitary elements in an involutive ring.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint of a left multiplication and of a composite.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the signed left multiplication in the Clifford algebra and its adjoint.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition, 2001), for the one-sided Clifford multiplication and the reality conditions.
- Sigurdur Helgason, *Groups and Geometric Analysis* (Academic Press, 1984), for the one-sided invariant operators and their adjoints.
