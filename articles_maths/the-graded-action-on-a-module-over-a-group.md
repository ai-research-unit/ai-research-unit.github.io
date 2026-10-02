
# __The Graded Action on a Module over a Group__

## Introduction

A module over a group that carries a grading may be acted on in a way that respects the grading or in a way that twists it, and the sign rule that governs the passage between the two is the group form of the Koszul rule of a graded algebra. This article fixes the notion of a graded module over a group, states the compatibility of the action with the grading, derives the sign rule that the compatibility imposes, and identifies the graded action with the module-theoretic shadow of the signed operators of the category.

The article assumes the elementary theory of groups from *Groups*, the group algebra, its module theory and the augmentation from *Group Algebras*, and the signed left multiplication and signed sandwich from *The Signed Left Multiplication on a Group* and *The Signed Sandwich on a Group*. It uses no distance, no norm and no form; a grading is a direct sum decomposition, not a metric.

## Graded Modules

**Definition.** Let $k$ be a commutative ring. A **graded $k$-module** is a $k$-module together with a direct sum decomposition

$$
M = M^{\bar0}\oplus M^{\bar1} .
$$

The elements of $M^{\bar0}\cup M^{\bar1}$ are **homogeneous**, of **degree** $\bar0$ or $\bar1$; the **grading involution** of $M$ is the $k$-linear map $\pi_M$ equal to $+\mathrm{id}$ on $M^{\bar0}$ and $-\mathrm{id}$ on $M^{\bar1}$. A $k$-linear operator $T$ on $M$ is **even** if $T\pi_M=\pi_M T$ and **odd** if $T\pi_M=-\pi_M T$; the parity of $T$ is written $|T|\in\mathbb{Z}/2$.

**Definition.** A **degree** on a group $G$ is a homomorphism $\varepsilon : G\to\{\pm1\}$. The kernel of $\varepsilon$ is the **even part** $G^{\bar0}$ and its complement $G^{\bar1}=\{g:\varepsilon(g)=-1\}$ is the **odd part**; the collection $(G,\varepsilon)$ is a **graded group**.

**Definition.** A **graded module over a graded group** $(G,\varepsilon)$ is a graded $k$-module $M$ together with a $k$-linear action of $G$ such that

$$
g\cdot M^{\bar i}\subseteq M^{\overline{i+\varepsilon(g)}} \qquad\text{for all } g\in G,\ i\in\mathbb{Z}/2 .
$$

An element of the even part preserves each part of $M$; an element of the odd part swaps the two parts.

**Proposition (equivalence with the sign rule).** The action is graded if and only if every $g$ acts by an operator of parity $\varepsilon(g)$,

$$
g\,\pi_M = \varepsilon(g)\,\pi_M\, g ,
$$

and then the degree of a product obeys the sign rule

$$
|g\cdot m| = \varepsilon(g) + |m| \quad\text{for } m \text{ homogeneous}.
$$

**Proof.** On a homogeneous $m$ of degree $|m|$, the operator $\pi_M$ acts by the scalar $(-1)^{|m|}$. The condition $g\cdot M^{\bar i}\subseteq M^{\overline{i+\varepsilon(g)}}$ says that for $m$ homogeneous, $g\cdot m$ is homogeneous of degree $|m|+\varepsilon(g)$, which is the sign rule. Comparing $\pi_M g m = (-1)^{|m|+\varepsilon(g)}gm$ with $g\pi_M m=(-1)^{|m|}gm$ gives $\pi_M g=\varepsilon(g) g\pi_M$, that is $g\pi_M=\varepsilon(g)\pi_M g$. The three statements are therefore equivalent.

The parity statement is the group form of the rule $T\pi=\pm\pi T$ for an operator on a graded module; the sign $\varepsilon(g)$ plays the role of the Koszul sign attached to the degree of a homogeneous element of a graded algebra.

## The Grading of the Group Algebra

The degree on the group makes the group algebra into a graded algebra, and the graded modules over the group are the graded modules over that algebra.

**Proposition.** If $\varepsilon : G\to\{\pm1\}$ is a degree, then the group algebra is graded by

$$
k[G]^{\bar0} = \Bigl\{\sum_{g\in G^{\bar0}} c_g\,g\Bigr\}, \qquad k[G]^{\bar1} = \Bigl\{\sum_{g\in G^{\bar1}} c_g\,g\Bigr\},
$$

and the multiplication respects the grading, $k[G]^{\bar i}\,k[G]^{\bar j}\subseteq k[G]^{\overline{i+j}}$.

**Proof.** The two subspaces span $k[G]$ because $G$ is the disjoint union of $G^{\bar0}$ and $G^{\bar1}$, and they meet only in $0$. The product of a term of degree $i$ and a term of degree $j$ has degree $i+j$ because $\varepsilon$ is a homomorphism, $\varepsilon(gh)=\varepsilon(g)\varepsilon(h)$.

**Corollary (the compatibility of the action).** A graded module over $(G,\varepsilon)$ is a graded module over the graded algebra $k[G]$, in the sense that the action is compatible with the grading,

$$
k[G]^{\bar i}\cdot M^{\bar j}\subseteq M^{\overline{i+j}} .
$$

**Proof.** It suffices to check the inclusion on the basis $G\subseteq k[G]$, where it is the defining property of the graded action, and to extend by linearity.

**Remark.** The grading of the group algebra exists exactly when the degree is a homomorphism; a subset of $G$ alone does not make $k[G]$ a graded algebra. This is the group-theoretic analogue of the requirement that the grading of an algebra be compatible with its product, and it is why the degree is part of the structure $(G,\varepsilon)$ and not a property of $G$.

## The Signed Action and the Koszul Sign

The graded action can be converted to one by even operators at the cost of a sign, and the cost is a cocycle.

**Definition.** Let $M$ be a graded module over $(G,\varepsilon)$. The **signed action** of $G$ on $M$ is

$$
g\triangleright m = \varepsilon(g)^{|m|}\, g\cdot m = (-1)^{\varepsilon(g)|m|}\,g\cdot m,
$$

on homogeneous $m$, extended linearly.

**Proposition (it is a projective action).** For homogeneous $m$ the signed action satisfies

$$
g\triangleright(h\triangleright m) = (-1)^{\varepsilon(g)\varepsilon(h)}\,(gh)\triangleright m .
$$

Hence the signed action is a **projective action** with cocycle the **Koszul sign** $c(g,h)=(-1)^{\varepsilon(g)\varepsilon(h)}$; it is an honest action exactly when the degree is trivial. Each operator $g\pi_M^{\varepsilon(g)}$ is even, and the assignment $g\mapsto g\pi_M^{\varepsilon(g)}$ is a projective representation with the same cocycle.

**Proof.** Write $\varepsilon(g)=0$ for even and $1$ for odd. The left side is $\varepsilon(h)^{|m|}\varepsilon(g)^{|h\cdot m|}g\cdot(h\cdot m)$, and $|h\cdot m|=|m|+\varepsilon(h)$, so it equals $\varepsilon(h)^{|m|}\varepsilon(g)^{|m|}\varepsilon(g)^{\varepsilon(h)}(gh)\cdot m$. The right side is $(-1)^{\varepsilon(g)\varepsilon(h)}\varepsilon(gh)^{|m|}(gh)\cdot m=(-1)^{\varepsilon(g)\varepsilon(h)}\varepsilon(g)^{|m|}\varepsilon(h)^{|m|}(gh)\cdot m$. The two agree because the remaining factor $\varepsilon(g)^{\varepsilon(h)}$ equals $(-1)^{\varepsilon(g)\varepsilon(h)}$, an identity that is trivial when $\varepsilon(h)=0$ and is $\varepsilon(g)=(-1)^{\varepsilon(g)}$ when $\varepsilon(h)=1$. The operator $g\pi_M^{\varepsilon(g)}$ is even because $\pi_M^{\varepsilon(g)}$ has parity $\varepsilon(g)$ and $g$ also has parity $\varepsilon(g)$, so the product has parity $0$; the product of two of them picks up the factor computed above, which is the cocycle.

**Corollary (the two actions agree on the even part).** If $g$ is even then $g\triangleright m=g\cdot m$ for all $m$; if $g$ is odd then $g\triangleright m=g\cdot m$ on $M^{\bar0}$ and $g\triangleright m=-g\cdot m$ on $M^{\bar1}$. In particular the signed action is an honest action on the even part of $G$, and the obstruction to its being an honest action on all of $G$ is the Koszul cocycle.

## Relation to the Signed Operators

The graded action is the module-theoretic shadow of the signed operators of this category, in the same way that the plain action of a group on a module is the shadow of the left regular representation.

**Remark.** When the group carries a grade involution $\alpha$ rather than a degree homomorphism, the twisting of an action by $\alpha$, $g\cdot m\mapsto \alpha(g)\cdot m$, is the module-theoretic counterpart of the signed operators $\ell_a$ and $\Sigma^{\alpha}_{a,b}$ of *The Signed Left Multiplication on a Group* and *The Signed Sandwich on a Group*. The two structures are not the same: a degree is a homomorphism to $\{\pm1\}$, whereas a grade involution is an automorphism of order two, and a group can carry one without the other. What they share is the effect on a graded module, the insertion of a sign that distinguishes the two parts, and it is that effect that the sign rule records.

**Remark (the adjoint action).** The adjoint action of a graded module over a group, its compatibility with the grading and the sign rule it imposes are *The Graded Adjoint Action on a Module over a Group*, in the involutive part of the category; it is the case in which the twisted operator is the adjoint of the one considered here.

## Summary

A **graded $k$-module** is a $k$-module with a decomposition $M=M^{\bar0}\oplus M^{\bar1}$, with **grading involution** $\pi_M$, and a **degree** on a group is a homomorphism $\varepsilon : G\to\{\pm1\}$. A **graded module over a graded group** $(G,\varepsilon)$ is a graded module with a linear action such that $g\cdot M^{\bar i}\subseteq M^{\overline{i+\varepsilon(g)}}$; equivalently each $g$ acts with parity $\varepsilon(g)$, $g\pi_M=\varepsilon(g)\pi_M g$, and the **sign rule** $|g\cdot m|=\varepsilon(g)+|m|$ holds on homogeneous elements. The degree makes the group algebra a graded algebra, $k[G]=k[G]^{\bar0}\oplus k[G]^{\bar1}$, and a graded module over the group is a graded module over this graded algebra, the compatibility $k[G]^{\bar i}M^{\bar j}\subseteq M^{\overline{i+j}}$ being the defining property extended by linearity. The **signed action** $g\triangleright m=\varepsilon(g)^{|m|}g\cdot m$ satisfies $g\triangleright(h\triangleright m)=(-1)^{\varepsilon(g)\varepsilon(h)}(gh)\triangleright m$, so it is a **projective action** with the Koszul cocycle $c(g,h)=(-1)^{\varepsilon(g)\varepsilon(h)}$; it agrees with the given action on the even part of $G$, differs from it by the grading involution on the odd part, and is an honest action exactly when the degree is trivial. The graded action is the module-theoretic shadow of the signed operators; a grade involution and a degree are different structures with the same effect on a graded module, the insertion of the sign that distinguishes the two parts.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=M^{\bar0}\oplus M^{\bar1}$ | a graded $k$-module |
| $\pi_M$ | the grading involution, $+\mathrm{id}$ on $M^{\bar0}$, $-\mathrm{id}$ on $M^{\bar1}$ |
| $\varepsilon : G\to\{\pm1\}$ | a degree, a homomorphism |
| $G^{\bar0}$, $G^{\bar1}$ | even and odd parts of $G$ |
| $g\cdot M^{\bar i}\subseteq M^{\overline{i+\varepsilon(g)}}$ | the compatibility of the graded action with the grading |
| $g\pi_M=\varepsilon(g)\pi_M g$ | the parity of the operator $g$ |
| $|g\cdot m|=\varepsilon(g)+|m|$ | the sign rule |
| $k[G]=k[G]^{\bar0}\oplus k[G]^{\bar1}$ | the group algebra as a graded algebra |
| $g\triangleright m=\varepsilon(g)^{|m|}g\cdot m$ | the signed action, a projective action |
| $c(g,h)=(-1)^{\varepsilon(g)\varepsilon(h)}$ | the Koszul cocycle of the signed action |
| $\alpha$ | a grade involution, the alternative twist when there is no degree |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for the graded structures of an associative algebra and the sign rule of the graded tensor product.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for group algebras, their gradings by a character and their graded modules.
- Pierre Deligne, "Catégories tensorielles", *Moscow Mathematical Journal* **2** (2002), 227–248, for the sign rule as the coherence of a graded symmetric structure.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutive automorphisms and the graded structures they induce.
