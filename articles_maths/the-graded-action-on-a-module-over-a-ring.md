
# __The Graded Action on a Module over a Ring__

## Introduction

A module over a graded ring may be acted on in a way that respects the grading, and the compatibility condition is the module-theoretic form of the sign rule of a graded algebra. A homogeneous element of degree $\bar i$ sends the degree-$\bar j$ part of the module into the degree-$\overline{i+j}$ part, so it acts by an operator of the same parity, and a scalar twist of the action inserts the Koszul sign $(-1)^{\bar i\bar j}$ whenever a homogeneous element passes another. This article fixes the notion of a graded module over a graded ring, states the compatibility of the action with the grading, derives the sign rule it imposes, and identifies the graded action with the module-level shadow of the signed left multiplication of the category.

The article assumes the theory of modules from *Modules* and *Modules over an Algebra*, the graded vocabulary of *Superalgebras and Graded Structures*, and the signed left multiplication of *The Signed Left Multiplication on a Ring*. It uses no distance, no norm and no form: a grading is a direct sum decomposition, not a metric, and the sign rule is an algebraic sign attached to parity. The companion in the group category is *The Graded Action on a Module over a Group*.

Throughout, $k$ is a commutative ring and $A$ is a $k$-algebra with $1 \neq 0$ carrying a **grade involution** $\alpha$, $\alpha^2 = \mathrm{id}$, so that $A = A_{\bar 0}\oplus A_{\bar 1}$ is a $\mathbb{Z}/2$-graded ring when $2$ is invertible, with $A_{\bar i}A_{\bar j}\subseteq A_{\overline{i+j}}$. The module $M$ is a graded $k$-module, $M = M^{\bar 0}\oplus M^{\bar 1}$. Homogeneous elements have a **degree** or **parity** in $\mathbb{Z}/2$; an operator is **even** if it preserves the two parts and **odd** if it interchanges them.

## Graded Modules and the Parity of an Operator

**Definition.** A **graded $k$-module** is a $k$-module $M$ with a direct sum decomposition

$$
M = M^{\bar 0}\oplus M^{\bar 1}.
$$

The elements of $M^{\bar 0}\cup M^{\bar 1}$ are **homogeneous**, of degree $\bar 0$ or $\bar 1$; the **grading involution** of $M$ is the $k$-linear operator $\pi_M$ equal to $+\mathrm{id}$ on $M^{\bar 0}$ and $-\mathrm{id}$ on $M^{\bar 1}$. A $k$-linear operator $T$ on $M$ is **even** if $T\pi_M = \pi_M T$, **odd** if $T\pi_M = -\pi_M T$; the parity is written $|T| \in \mathbb{Z}/2$.

**Proposition (parity as a degree shift).** A $k$-linear operator $T$ on $M$ has parity $\bar i$ exactly when $T(M^{\bar j})\subseteq M^{\overline{i+j}}$ for $j = \bar 0, \bar 1$; and then $T m$ is homogeneous of degree $|T| + |m|$ for every homogeneous $m$.

**Proof.** For homogeneous $m$ of degree $\bar j$ one has $\pi_M m = (-1)^{\bar j}m$ and $\pi_M(Tm) = (-1)^{|T|+\bar j}Tm$, so $T(\pi_M m) = (-1)^{\bar j}Tm$ while $\pi_M(Tm) = (-1)^{|T|+\bar j}Tm$. The two agree for all homogeneous $m$ exactly when $(-1)^{|T|} = 1$, that is, when $T$ is even in the sense of commuting with $\pi_M$; the general statement follows by applying both displays with the sign $(-1)^{|T|}$, and the degree formula is the same computation read on the components.

**Definition.** A **graded ring** is a ring $A$ with a decomposition $A = A_{\bar 0}\oplus A_{\bar 1}$ such that $A_{\bar i}A_{\bar j}\subseteq A_{\overline{i+j}}$; equivalently, $A$ carries a grade involution $\alpha$ when $2$ is invertible, with $A_{\bar 0} = \{a : \alpha(a) = a\}$ and $A_{\bar 1} = \{a : \alpha(a) = -a\}$. An element of $A_{\bar 0}$ is **even**, of $A_{\bar 1}$ **odd**.

## The Graded Action

**Definition.** A **graded module over the graded ring** $A$ is a graded $k$-module $M$ together with a $k$-linear action of $A$ such that

$$
A_{\bar i}\cdot M^{\bar j}\subseteq M^{\overline{i+j}} \qquad \text{for } i, j \in \mathbb{Z}/2 .
$$

The action is **graded** or **parity-respecting**.

**Proposition (equivalence with the parity of the action operators).** For a homogeneous $a \in A_{\bar i}$ let $L_a$ denote the operator $m\mapsto a\cdot m$ on $M$. The action is graded if and only if every homogeneous $a$ acts by an operator of parity $|a|$,

$$
L_a\,\pi_M = (-1)^{|a|}\,\pi_M\,L_a,
$$

and then the **sign rule** holds on homogeneous elements,

$$
|a\cdot m| = |a| + |m| .
$$

**Proof.** The inclusion $A_{\bar i}M^{\bar j}\subseteq M^{\overline{i+j}}$ says exactly that $L_a$ sends $M^{\bar j}$ into $M^{\overline{i+j}}$, which by the previous proposition is the statement that $L_a$ has parity $|a|$; the sign rule is the degree formula of that proposition.

**Example.** Let $M = A$ with $M^{\bar j} = A_{\bar j}$ and let $A$ act by left multiplication. Then $A_{\bar i}\cdot A_{\bar j} = A_{\bar i}A_{\bar j}\subseteq A_{\overline{i+j}}$, so the regular module is graded, and $L_a$ is the left multiplication of *Left and Right Multiplication in a Ring*; the parity statement is that an even element preserves the two parts of the ring and an odd element swaps them, which is the conclusion of *The Signed Sandwich on a Ring*.

## The Sign Rule and the Signed Action

The graded action can be twisted by the grading involution of the module at the cost of a sign on each homogeneous element, and the cost is the Koszul cocycle.

**Definition.** Let $M$ be a graded module over the graded ring $A$. The **signed action** of $A$ on $M$ is

$$
a\triangleright m = (-1)^{|a|\,|m|}\,a\cdot m
$$

on homogeneous $a$ and $m$, extended linearly; equivalently $a\triangleright m = a\cdot\pi_M^{|a|}(m)$.

**Proposition (it is a projective action with the Koszul cocycle).** For homogeneous $a, b$ and homogeneous $m$,

$$
a\triangleright(b\triangleright m) = (-1)^{|a||b|}\,(ab)\triangleright m .
$$

Hence the signed action is a **projective action** with cocycle the **Koszul sign** $c(a,b) = (-1)^{|a||b|}$; it is an honest action exactly when the grading is trivial, that is, when $A = A_{\bar 0}$.

**Proof.** The operator of the signed action is $T_a = L_a\pi_M^{|a|}$. The parity of a composite is the sum of the parities, $\pi_M$ has parity $\bar 0$, and $L_a$ has parity $|a|$ by the previous section, so $T_a$ has parity $|a|$. Computing on a homogeneous $m$ of degree $j$,

$$
a\triangleright(b\triangleright m) = (-1)^{|a|(|b|+j)}(-1)^{|b|j}\,ab\cdot m = (-1)^{|a||b|}(-1)^{(|a|+|b|)j}ab\cdot m = (-1)^{|a||b|}(ab)\triangleright m,
$$

because $ab$ is homogeneous of degree $|a|+|b|$. The cocycle is $c(a,b) = (-1)^{|a||b|}$ by reading off the middle expression, and it is $1$ for all $a, b$ exactly when every element is even.

**Corollary (the two actions agree on the even part).** If $a$ is even then $a\triangleright m = a\cdot m$ for all $m$ and the operator $L_a$ is even; if $a$ is odd then $a\triangleright m = a\cdot\pi_M(m)$, which agrees with $a\cdot m$ on $M^{\bar 0}$ and equals $-a\cdot m$ on $M^{\bar 1}$, and the operator has parity $\bar 1$. The signed action is an honest action of the even part $A_{\bar 0}$ and is only projective on all of $A$.

**Remark.** The signed action is the module-level form of the passage from the plain left multiplication $L_a$ to the signed left multiplication $T_a = L_a\circ\alpha$ of *The Signed Left Multiplication on a Ring*: on the odd elements it inserts the module-graded twist $\pi_M$ in place of the ring-graded twist $\alpha$, and on the even elements it uses the plain operator. The signed action is **not** an action, and its failure to be one is measured by a $\mathbb{Z}/2$-cocycle, the Koszul cocycle.

## The Action as a Superalgebra Representation

**Definition.** For homogeneous operators $S, T$ on $M$ the **graded commutator** is

$$
[S, T]_{\mathrm g} = ST - (-1)^{|S||T|}\,TS .
$$

**Proposition.** The graded action of $A$ on $M$ is a homomorphism of graded rings $A \to \operatorname{End}_k(M)$ with the graded commutator as bracket; for homogeneous $a, b \in A$,

$$
[L_a, L_b]_{\mathrm g} = L_{ab - (-1)^{|a||b|}ba} .
$$

In particular the action is a **Lie superalgebra representation** exactly when $A$ is graded-commutative, $ab = (-1)^{|a||b|}ba$ for homogeneous $a, b$; and a graded-commutative ring acts on every graded module by a representation of its Lie superalgebra.

**Proof.** $L_{ab} = L_aL_b$ by associativity, so $[L_a,L_b]_{\mathrm g} = L_aL_b - (-1)^{|a||b|}L_bL_a = L_{ab} - (-1)^{|a||b|}L_{ba} = L_{ab-(-1)^{|a||b|}ba}$, since $L$ is additive in the parameter. The bracket vanishes for all homogeneous $a, b$ exactly under the graded-commutativity condition.

**Example (the exterior algebra is the extreme case).** Let $A = \Lambda(V)$ be the exterior algebra with its odd generators, a graded-commutative ring; the identification of the **commutation factors** $\varepsilon(I,J) = (-1)^{\#\{(i,j) : i>j\}}$ of *Superalgebras and Graded Structures* makes every squarefree monomial act on $\Lambda(V)$ by a graded operator, and the graded action is the restriction of the regular representation to a graded module. The Clifford algebra is graded but not graded-commutative in general, and its graded action is the one of Part VI.

## Relation to the Signed Operators

**Proposition (the module-level shadow).** Let $M$ be a graded module over the graded ring $A$, and let $T_a^M$ denote the operator of the signed action, $T_a^M = L_a\pi_M^{|a|}$. Then, for homogeneous $a$,

$$
T_a^M = L_a \ (a \text{ even}), \qquad T_a^M = L_a\circ\pi_M \ (a \text{ odd}),
$$

so the signed action uses the plain left multiplication on the even elements and inserts the grading involution of the module on the odd ones. When $M = A$ with $\pi_A = \alpha$, the odd case is the signed left multiplication $T_a = L_a\alpha$ of *The Signed Left Multiplication on a Ring*, while the even case is the plain left multiplication $L_a$; the two operators of that article are the two parities of the graded action.

**Proof.** The two cases are the definition of $\pi_M^{|a|}$, with $\pi_M^{\bar 0} = \mathrm{id}$ and $\pi_M^{\bar 1} = \pi_M$; for $M = A$ and $\pi_A = \alpha$ the odd case is $L_a\alpha = T_a$ and the even case is $L_a$.

**Remark (the group case).** The companion article *The Graded Action on a Module over a Group* treats the same construction with a degree homomorphism $\varepsilon : G \to \{\pm 1\}$ in place of the grade involution $\alpha$; the two structures have the same effect on a graded module, the insertion of the Koszul sign, but they are not the same data, since a degree is a homomorphism and a grade involution is an automorphism of order two.

**Remark (the adjoint action).** The adjoint action of a graded module over a ring with an involution, its compatibility with the grading and the sign rule it imposes are *The Graded Adjoint Action on a Module over a Ring*, in the involutive part of the category; it is the case in which the twisted operator is the adjoint of the one considered here.

## Summary

A **graded $k$-module** is a $k$-module $M = M^{\bar 0}\oplus M^{\bar 1}$ with a grading involution $\pi_M$, and an operator has parity $\bar i$ exactly when it sends $M^{\bar j}$ into $M^{\overline{i+j}}$; a **graded ring** is a ring $A = A_{\bar 0}\oplus A_{\bar 1}$ with $A_{\bar i}A_{\bar j}\subseteq A_{\overline{i+j}}$, equivalently a ring with a grade involution. A **graded module** over $A$ is a graded $k$-module with a $k$-linear action such that $A_{\bar i}\cdot M^{\bar j}\subseteq M^{\overline{i+j}}$; equivalently, each homogeneous $a$ acts by an operator of parity $|a|$, $L_a\pi_M = (-1)^{|a|}\pi_ML_a$, and the **sign rule** $|a\cdot m| = |a|+|m|$ holds. The regular module $M = A$ is graded, and the regular action is the left regular representation with the parity splitting of *The Signed Sandwich on a Ring*.

The **signed action** $a\triangleright m = (-1)^{|a||m|}a\cdot m = a\cdot\pi_M^{|a|}(m)$ satisfies $a\triangleright(b\triangleright m) = (-1)^{|a||b|}(ab)\triangleright m$, so it is a **projective action** with the **Koszul cocycle** $c(a,b) = (-1)^{|a||b|}$; it is an honest action exactly when the grading is trivial, and it agrees with the given action on the even elements while differing by the grading involution on the odd ones. The graded action is a graded-ring homomorphism $A\to\operatorname{End}_k(M)$ with the graded commutator $[S,T]_{\mathrm g} = ST-(-1)^{|S||T|}TS$, and $[L_a,L_b]_{\mathrm g} = L_{ab-(-1)^{|a||b|}ba}$, so a graded-commutative ring acts by a Lie superalgebra representation. The signed action is the module-level shadow of the signed left multiplication: it uses the plain left multiplication on the even elements and inserts the grading involution $\pi_M$ on the odd ones, so on the regular module it realises the plain and signed left multiplications as the two parities of the graded action.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M = M^{\bar 0}\oplus M^{\bar 1}$ | Graded $k$-module |
| $\pi_M$ | Grading involution, $+\mathrm{id}$ on $M^{\bar 0}$, $-\mathrm{id}$ on $M^{\bar 1}$ |
| $A = A_{\bar 0}\oplus A_{\bar 1}$ | Graded ring, equivalently a ring with a grade involution $\alpha$ |
| $|a|$, $|m|$, $|T|$ | Parity of a homogeneous element or operator |
| $A_{\bar i}\cdot M^{\bar j}\subseteq M^{\overline{i+j}}$ | Compatibility of the graded action |
| $L_a\pi_M = (-1)^{|a|}\pi_ML_a$ | Homogeneous $a$ acts with parity $|a|$ |
| $|a\cdot m| = |a|+|m|$ | the sign rule |
| $a\triangleright m = (-1)^{|a||m|}a\cdot m$ | signed action, a projective action |
| $c(a,b) = (-1)^{|a||b|}$ | Koszul cocycle of the signed action |
| $[S,T]_{\mathrm g} = ST-(-1)^{|S||T|}TS$ | Graded commutator of homogeneous operators |
| $[L_a,L_b]_{\mathrm g} = L_{ab-(-1)^{|a||b|}ba}$ | the graded bracket on the action operators |
| $T_a^M = L_a\pi_M^{|a|}$ | Module-level signed left multiplication |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded rings, graded modules and the compatibility of an action with a grading.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the representations of a graded algebra and the sign rule of a graded module.
- Pierre Deligne, "Catégories tensorielles", *Moscow Mathematical Journal* **2** (2002), 227–248, for the Koszul sign as a coherence of the graded symmetric structure.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for grade involutions, the graded modules they determine and the operators of the associated graded action.
