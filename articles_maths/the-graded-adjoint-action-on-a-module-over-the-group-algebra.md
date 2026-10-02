
# __The Graded Adjoint Action on a Module over the Group Algebra__

## Introduction

A graded module over the group algebra carries a grading, a homogeneous action and a twisted action, and the adjoint of the action is a second action: the algebra acts on the endomorphisms by conjugation, on the dual module by the transposed action, and the grading involution keeps a bookkeeping of parities and signs. What makes the construction graded is that the grading involution is part of the data, so that the compatibility of the action with the grading becomes a compatibility of the adjoint action with the grade involution, and the sign rule attaches a parity to every operator and a sign to every transpose, exactly as the graded action attaches a sign to every product. On the group algebra the construction acquires its analytic content from the `*`-structure: the adjoint of the action operator of $a$ is the action operator of $a^*$, and the adjoint action of a unitary element preserves self-adjointness. This article fixes the graded adjoint action, its compatibility with the grading, the sign rule for the transpose, and the connection with the involution.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra, its involution and its `*`-structure from *The Convolution Algebra $L^1(G)$* and *The Group Algebra as an Involutive Algebra*; the grade involution, the signed sandwich and the signed left multiplication from *The Signed Sandwich on the Group Algebra* and *The Signed Left Multiplication on the Group Algebra*; the graded module, the grading involution, the homogeneous action, the sign rule and the twisted action from *The Graded Action on a Module over the Group Algebra*; the abstract graded module, the graded bilinear forms, the transposes and the adjoint action from *The Graded Adjoint Action on a Module over a Graded Algebra* and *The Graded Adjoint Action on a Module over a Topological Group*; the adjoints of the elementary operators from *Hermitian Operators on a Group Algebra*, *Unitary Representations and the Adjoint* and *The Signed Adjoint of the Left Multiplication on the Group Algebra*, immediately preceding; and the Hilbert spaces, the bounded operators, the adjoint and the commutant from *Operator Algebras*.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$; $\mathcal{A} = L^1(G)$ carries the involution $f^*$ and the Haar pairing; $\alpha$ is a grade involution, $\mathrm{A}f = \alpha(f)$, and $M = M^+\oplus M^-$ is a **graded Banach module** over $\mathcal{A}$ with grading involution $\varepsilon$ ($+1$ on $M^+$, $-1$ on $M^-$) and bounded homogeneous action written $\pi(a)m = a\cdot m$, so that $\varepsilon\,\pi(a)\,\varepsilon = \pi(\alpha(a))$; the **twisted action** is $a\cdot_\alpha m = \pi(\alpha(a))m$. When $M$ is a Hilbert space and the action is `*`-compatible, $\pi(a^*) = \pi(a)^*$.

## Graded Forms and Transposes

**Definition.** A **graded form** on $M$ is a bilinear form $B$ with $B(\varepsilon v,\varepsilon w) = B(v,w)$ (**even**) or $B(\varepsilon v,\varepsilon w) = -B(v,w)$ (**odd**); the **transpose** $T^\#$ of an operator $T$ on $M$ is defined by $B(Tv,w) = B(v,T^\#w)$ when $B$ is nondegenerate.

**Proposition (the grading involution and the transpose).** The grading involution is self-adjoint for an even graded form and anti-self-adjoint for an odd one,

$$
\varepsilon^\# = \varepsilon \ \text{(even)},\qquad \varepsilon^\# = -\varepsilon \ \text{(odd)},
$$

and for a homogeneous operator $T$ of parity $|T|$ the transpose has the same parity, $\varepsilon T^\#\varepsilon = (-1)^{|T|}T^\#$.

**Proof.** For homogeneous $v,w$, $B(\varepsilon v,w) = (-1)^{|v|}B(v,w)$ and $B(v,\varepsilon w) = (-1)^{|w|}B(v,w)$; an even form pairs equal parities and an odd form opposite parities, which gives the two cases for $\varepsilon^\#$, and the parity of the transpose follows from $B(\varepsilon Tv,w) = (-1)^{|v|+|T|}B(Tv,w) = (-1)^{|T|}B(v,T^\#w)$ compared with $B(\varepsilon Tv,w) = B(Tv,\varepsilon^\#w)$. $\square$

**Theorem (the sign rule for the transpose).** For a homogeneous operator $T$ and a homogeneous graded form, the transpose is characterised by

$$
B(Tv,w) = (-1)^{|T|\,q}\,B(v,T^\#w),
$$

with $q = 0$ for an even form and $q = 1$ for an odd form; the sign is the product of the parity of the operator and the parity of the form.

**Proof.** The case $q = 0$ is the definition; for $q = 1$ it follows from the anti-self-adjointness of $\varepsilon$ by the computation of the proposition, and both are extended by linearity to the homogeneous decomposition. $\square$

## The Adjoint Action on the Endomorphisms

**Definition.** For a unit $a\in\mathcal{A}$ the **adjoint action** on the endomorphisms of $M$ is

$$
a\cdot T = \pi(a)\,T\,\pi(a)^{-1} .
$$

**Theorem (it is an action preserving the parity).** The adjoint action is an action of the unit group of $\mathcal{A}$ on $\mathrm{End}(M)$, it is compatible with the grading in the form

$$
\varepsilon\,(a\cdot T)\,\varepsilon = \alpha(a)\cdot(\varepsilon\,T\,\varepsilon) = (\alpha(a))\cdot T^{\varepsilon}, \qquad T^\varepsilon = \varepsilon T\varepsilon ,
$$

and it preserves the parity, $|a\cdot T| = |T|$.

**Proof.** The action property is the standard conjugation identity $(ab)\cdot T = a\cdot(b\cdot T)$ with $ab$ written multiplicatively in $\mathcal{A}$; the compatibility is $\varepsilon\,\pi(a)\,T\,\pi(a)^{-1}\,\varepsilon = \pi(\alpha(a))\,\varepsilon T\varepsilon\,\pi(\alpha(a))^{-1}$, using $\varepsilon\pi(a)\varepsilon = \pi(\alpha(a))$ twice; the parity is preserved because conjugation by any invertible operator and the twist $\sigma$ preserve homogeneous degree. $\square$

**Corollary (the twisted action appears).** Reading the compatibility on the module rather than on the endomorphisms, the grading involution interchanges the given action and the twisted action, $\varepsilon\pi(a) = \pi(\alpha(a))\varepsilon$, which is the sign rule of *The Graded Action on a Module over the Group Algebra*; the adjoint action of $a$ on the endomorphisms equals the given action of $a$ composed with the inverse of the given action of $a$, and the twisted adjoint action is its $\alpha$-transport.

**Proof.** The interchange identity is $\varepsilon\pi(a)\varepsilon = \pi(\alpha(a))$ composed on the right with $\varepsilon$; the description of the adjoint action is its definition, and the twisted version is obtained by replacing $a$ with $\alpha(a)$. $\square$

## The Hilbert Adjoint and the Involution

**Theorem (the adjoint of the action operator).** Suppose $M$ is a Hilbert space and the action is `*`-compatible, $\pi(a^*) = \pi(a)^*$; then for a unitary element $a$ the action operator is unitary, $\pi(a)^{-1} = \pi(a)^*$, and the adjoint of the adjoint action is

$$
\bigl(a\cdot T\bigr)^* = a\cdot T^* ,
$$

so the adjoint action of a unitary element preserves self-adjointness, positivity and unitarity.

**Proof.** $(a\cdot T)^* = (\pi(a)T\pi(a)^{-1})^* = \pi(a)^{-1*}T^*\pi(a)^* = \pi(a)T^*\pi(a)^{-1}$ when $\pi(a)^* = \pi(a)^{-1}$; positivity is preserved because $a\cdot T = \pi(a)T\pi(a)^*$ is a `*`-congruence, and unitarity because the map is a `*`-automorphism of $\mathrm{End}(M)$. $\square$

**Corollary (the grading and the Hilbert adjoint).** If the two summands $M^\pm$ are orthogonal and $\pi$ is `*`-compatible, then the grading involution is self-adjoint, $\varepsilon^* = \varepsilon$, and it commutes with the adjoint action, $\varepsilon(a\cdot T)\varepsilon = (a\cdot(\varepsilon T\varepsilon))$; the signs of the graded forms of the previous section are then the signs read off the orthogonal decomposition.

**Proof.** Orthogonality of $M^\pm$ makes the projection $\varepsilon$ self-adjoint; the commutation with the adjoint action is the compatibility of the action with the grading, and the identification of the signs is the proposition on graded forms in the Hilbert-space case. $\square$

## The Degenerate Cases

**Theorem (trivial and inner grade involutions).** If $\alpha = \mathrm{id}$ then the given and the twisted actions coincide and the adjoint action is the ordinary conjugation, $\varepsilon$ commuting with everything; if $\alpha = c_z$ is inner then the twisted action is the transport of the given action by $z$ and the compatibility reduces to the conjugation by $z$. In both cases the parity bookkeeping collapses.

**Proof.** With $\alpha = \mathrm{id}$, $\varepsilon$ is central and $\pi(\alpha(a)) = \pi(a)$; with $\alpha = c_z$, $\pi(\alpha(a)) = \pi(z)\pi(a)\pi(z)^{-1}$, which gives the stated transport and compatibility. $\square$

**Remark (what the article does not do).** The adjoint of a convolution operator on its own terms, its expression on $L^p$ and the involutive algebra of convolution operators are *The Adjoint of a Convolution Operator*, the last article of this group; the abstract graded adjoint action over a graded algebra and the graded module over a topological group are the Part I and Part II articles of the same name; the graded forms of this article are not the Hermitian forms of the `- * Theory` group, which are conjugate-linear and are treated in *Hermitian Forms and the Group Algebra*.

## Summary

A graded module over the group algebra carries a homogeneous action and its $\alpha$-twist, the grading involution $\varepsilon$ interchanging them, and the adjoint action $a\cdot T = \pi(a)T\pi(a)^{-1}$ of a unit is compatible with the grading in the form $\varepsilon(a\cdot T)\varepsilon = \alpha(a)\cdot(\varepsilon T\varepsilon)$, preserving the parity of operators. For a homogeneous graded form the transpose obeys the sign rule $B(Tv,w) = (-1)^{|T|q}B(v,T^\#w)$ with $q = 0$ for an even form and $q = 1$ for an odd one, and the grading involution is self-adjoint for an even form and anti-self-adjoint for an odd one. When the module is a Hilbert space with a `*`-compatible action and $a$ is unitary, the adjoint of the adjoint action is $(a\cdot T)^* = a\cdot T^*$, so self-adjointness, positivity and unitarity are preserved by the adjoint action; and when the two graded summands are orthogonal the grading involution is self-adjoint and commutes with the adjoint action. The degenerate cases are the trivial grade involution, where the two actions coincide and the grading is central, and the inner grade involution, where the compatibility is conjugation by the inner element. The adjoint of a convolution operator is the neighbouring article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M = M^+\oplus M^-$, $\varepsilon$ | The graded module and its grading involution |
| $a\cdot m = \pi(a)m$ | The homogeneous action |
| $a\cdot_\alpha m = \pi(\alpha(a))m$ | The twisted action |
| $\varepsilon\pi(a)\varepsilon = \pi(\alpha(a))$ | The compatibility of the action with the grading |
| $B(Tv,w) = \pm B(v,T^\#w)$ | The sign rule for the transpose |
| $\varepsilon^\# = \pm\varepsilon$ | Self- or anti-self-adjointness of $\varepsilon$ |
| $a\cdot T = \pi(a)T\pi(a)^{-1}$ | The adjoint action |
| $\varepsilon(a\cdot T)\varepsilon = \alpha(a)\cdot(\varepsilon T\varepsilon)$ | Compatibility with the grading |
| $(a\cdot T)^* = a\cdot T^*$ | The Hilbert adjoint, unitary $a$ |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint, the `*`-congruences and the commutant.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for graded forms, their parity and the transposes they define.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the adjoint action of a group on an operator algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the graded module, the sign rule and the twisted action.
- George W. Mackey, *The Theory of Unitary Group Representations* (University of Chicago Press, 1976), for the module picture of a representation and the conjugation action.
