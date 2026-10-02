
# __Reflections as Signed Two-Sided Operators on a Lie Algebra__

## Introduction

A **reflection** of a graded Lie algebra is a signed two-sided operator that is its own inverse — an involution of the algebra produced by the adjoint action, the inner automorphisms and the grade involution. The model is the conjugation $x\mapsto a\alpha(x)a^{-1}$ of a group, and its Lie-algebraic form is the signed conjugation $\rho_a = \operatorname{Ad}_{\exp a}\alpha$; the reflection attached to an element $a$ is an involution exactly when the element $a+\alpha(a)$ is central, and the elements satisfying this are the ones that **act by an involution**. The article identifies the carrying elements of a reflection, computes the fixed subalgebra, records the correspondence between the reflections and the elements acting by an involution, and analyses the three ways in which the construction degenerates.

This article treats the reflections of a Lie algebra read as signed two-sided operators, the correspondence with the elements acting by an involution, and its failure in the degenerate cases. It is the sixth article of the `- Operator Theory` group of the category; the signed sandwich is *The Signed Sandwich on a Lie Algebra*, above, the signed left multiplication is *The Signed Left Multiplication on a Lie Algebra*, below, the grading and the involution are *Graded Lie Algebras with an Involution* and *Symmetric Pairs of a Lie Algebra*, and the adjoint of a reflection is *The Signed Adjoint of the Reflection on a Lie Algebra* of the `- * Operator Theory` group, below in the category.

The article assumes the graded Lie algebra and its grade involution from *Graded Lie Algebras and Lie Superalgebras* and *Graded Lie Algebras with an Involution*, the adjoint action, the inner automorphisms and the exponential from *The Lie Correspondence and the Adjoint Representation* and *The Lie Algebra and the Exponential Map*, the symmetric pairs and the involutions of an algebra from *Symmetric Pairs of a Lie Algebra*, and the signed sandwich with its square from *The Signed Sandwich on a Lie Algebra*. The reflections of the group, which carry an inverse, are *Reflections as Signed Two-Sided Operators on a Group*; the geometric reflection in a hyperplane requires a form and belongs to Part IV, and no geometry is made here.

## The Signed Conjugation

### The Definition

**Definition.** Let $\mathrm{G}$ be a Lie algebra with the grade involution $\alpha$ and let $a\in\mathrm{G}$. The **signed conjugation** by $a$ is the signed two-sided operator

$$
\rho_a = \operatorname{Ad}_{\exp a}\circ\alpha , \qquad \rho_a(x) = e^{\operatorname{ad}_a}\bigl(\alpha(x)\bigr) ,
$$

where $\operatorname{Ad}_{\exp a} = e^{\operatorname{ad}_a}$ is the inner automorphism attached to the group element $\exp a$.

**Proposition.** The signed conjugation is an automorphism of the algebra, being the composite of the inner automorphism $e^{\operatorname{ad}_a}$ and the grade involution $\alpha$; its inverse is $\alpha\circ e^{-\operatorname{ad}_a} = e^{-\operatorname{ad}_{\alpha(a)}}\alpha$, and it acts on the grading by exchanging the roles of the even and the odd parts through $\alpha$.

*Proof.* The composite of two automorphisms is an automorphism; the inverse is the composite of the inverses in the reverse order, and the identification $e^{-\operatorname{ad}_{\alpha(a)}} = \alpha e^{-\operatorname{ad}_a}\alpha^{-1}$ is the naturality of the adjoint action under the automorphism $\alpha$.

### The Square

**Theorem.** The square of the signed conjugation is the inner automorphism of the element $a + \alpha(a)$,

$$
\rho_a^{2} = e^{\operatorname{ad}_{a+\alpha(a)}} = \operatorname{Ad}_{\exp(a+\alpha(a))} ,
$$

and $\rho_a$ is an involution of the algebra exactly when $a+\alpha(a)$ is central.

*Proof.* Compute $\rho_a^2 = e^{\operatorname{ad}_a}\alpha e^{\operatorname{ad}_a}\alpha$; using $\alpha e^{\operatorname{ad}_a}\alpha^{-1} = e^{\operatorname{ad}_{\alpha(a)}}$ and $\alpha^2 = \mathrm{id}$ gives $e^{\operatorname{ad}_a}e^{\operatorname{ad}_{\alpha(a)}} = e^{\operatorname{ad}_{a+\alpha(a)}}$; an inner automorphism of a connected group is the identity exactly when its generator is central.

**Corollary.** If $a$ lies in the odd part, $\alpha(a) = -a$, then $a + \alpha(a) = 0$ and $\rho_a$ is an involution for every odd $a$; the odd part is therefore the family of the automatically carrying elements, in parallel with the inverted set of the group.

*Proof.* The statement is the substitution $\alpha(a) = -a$; the centrality of $0$ is immediate.

## The Reflections

### The Definition and the Carrying Elements

**Definition.** A **reflection** of the graded Lie algebra $(\mathrm{G},\alpha)$ is a signed conjugation that is an involution,

$$
\rho_a = e^{\operatorname{ad}_a}\alpha, \qquad \rho_a^{2} = \mathrm{id} \iff a + \alpha(a)\in Z(\mathrm{G}) ,
$$

where $Z(\mathrm{G})$ is the centre; the element $a$ is a **carrying element** of the reflection.

**Proposition (the carrying elements).** Two elements $a,a'$ carry the same reflection exactly when $a - a'$ is central: $\rho_a = \rho_{a'}$ if and only if $a - a'\in Z(\mathrm{G})$.

*Proof.* The condition $\rho_a = \rho_{a'}$ is $e^{\operatorname{ad}_a}\alpha = e^{\operatorname{ad}_{a'}}\alpha$, that is $e^{\operatorname{ad}_{a-a'}} = \mathrm{id}$ on $\mathrm{G}$, which is the centrality of $a - a'$ in the connected case; conversely a central difference gives the identity of the automorphisms.

**Corollary.** The reflection attached to $a$ depends only on the coset $a + Z(\mathrm{G})$, and the reflections are the images of the cosets of the elements $a$ with $a+\alpha(a)$ central.

*Proof.* The fibres of the map $a\mapsto\rho_a$ are the cosets of the centre by the proposition, and the involution condition is the centrality of $a+\alpha(a)$, which is constant on the cosets.

### The Correspondence

**Definition.** An element $a\in\mathrm{G}$ **acts by an involution** when the inner automorphism $e^{\operatorname{ad}_a}$ is an involution of the algebra, equivalently when $2a$ is central.

**Theorem (the correspondence).** Let $R$ be the set of reflections of $(\mathrm{G},\alpha)$ and let $E$ be the set of elements acting by an involution. Then the map

$$
E\longrightarrow \operatorname{Aut}(\mathrm{G}), \qquad a\longmapsto e^{\operatorname{ad}_a}\alpha
$$

has image the reflections whose carrying element is $a$ up to the centre, and its fibres are the cosets of the centre; when the grade involution is the identity the correspondence reduces to the inner automorphisms, and the reflections are the inner involutions.

*Proof.* The image is by definition the set of the signed conjugations, and the involution condition is the centrality of $a+\alpha(a)$; the fibres are the cosets of the centre by the previous proposition. The case $\alpha = \mathrm{id}$ is the substitution.

**Corollary (the odd elements).** Every element of the odd part carries a reflection, the reflection of an odd element $a$ is $\rho_a = e^{\operatorname{ad}_a}\alpha$, and the reflections of the odd part are the signed conjugations whose carrying element is inverted by $\alpha$.

*Proof.* Already computed: for odd $a$, $a+\alpha(a) = 0$; the identification with the inverted set is the definition.

### The Fixed Subalgebra

**Theorem.** The fixed set of the reflection $\rho_a$ is

$$
\operatorname{Fix}(\rho_a) = \{x : \alpha(x) = e^{-\operatorname{ad}_a}x\} ,
$$

and it is a subalgebra of $\mathrm{G}$, nonempty exactly when the operator has a fixed point; when it is nonempty it is a coset of the fixed subalgebra $\mathrm{G}^{\alpha}$ of the grade involution.

*Proof.* The fixed equation is $e^{\operatorname{ad}_a}\alpha(x) = x$, that is $\alpha(x) = e^{-\operatorname{ad}_a}x$; a fixed set of an automorphism is a subalgebra, and the closure under the bracket is the multiplicativity of the automorphism. The coset statement is the computation that the difference of two fixed points is fixed by $\alpha$, in parallel with the group case.

**Corollary.** When $\alpha = \mathrm{id}$ the fixed subalgebra is the centraliser of $a$ in the connected case, $\operatorname{Fix}(\rho_a) = \mathfrak{c}(a) = \{x : [a,x] = 0\}$; the general fixed subalgebra is the set on which the two automorphisms $\alpha$ and $e^{-\operatorname{ad}_a}$ agree.

*Proof.* The equation reduces to $e^{-\operatorname{ad}_a}x = x$, which is $[a,x] = 0$ when the operator is the exponential of the adjoint action.

## The Degenerate Cases

### The Inner Grade Involution

**Proposition.** If the grade involution is inner, $\alpha = e^{\operatorname{ad}_w}$ for an element $w$ of the connected group, then the reflections are the inner automorphisms, $\rho_a = e^{\operatorname{ad}_{a+w}}$, and they are not distinguished from the ordinary conjugations; the correspondence of the theorem becomes the correspondence between the elements and the inner automorphisms modulo the centre.

*Proof.* Substitute $\alpha = e^{\operatorname{ad}_w}$; the composite of two inner automorphisms is inner, with the generator the sum in the abelian algebra, and the reflection condition becomes the centrality of $a+w$ up to the involution condition.

### The Abelian Case

**Proposition.** If $\mathrm{G}$ is abelian then the adjoint action is trivial, $\operatorname{ad}_a = 0$, and every reflection is the grade involution itself, $\rho_a = \alpha$, independent of the carrying element; the correspondence collapses to the single point, and the fixed subalgebra of every reflection is the even part $\mathrm{G}^{+}$ with the odd part as its anti-fixed part.

*Proof.* The adjoint action of an abelian algebra is zero, so $e^{\operatorname{ad}_a} = \mathrm{id}$ and $\rho_a = \alpha$; the fixed set of the grade involution is the even part, by definition.

### The Central Element

**Proposition.** If the carrying element is central, $a\in Z(\mathrm{G})$, then the reflection is the grade involution, $\rho_a = \alpha$, and it is an involution; the direction through the centre therefore carries no information, and the correspondence of the theorem is trivial on the centre.

*Proof.* A central element has $\operatorname{ad}_a = 0$, so $e^{\operatorname{ad}_a} = \mathrm{id}$; the reflection is $\alpha$, which is an involution.

### The Identity Grade Involution

**Proposition.** If $\alpha = \mathrm{id}$, the reflections are the inner automorphisms $e^{\operatorname{ad}_a}$ with $2a$ central, and the correspondence is between the elements of order two modulo the centre and the inner involutions; in this case the signed theory reduces to the unsigned one, and the reflection is an ordinary inner involution.

*Proof.* The substitution and the criterion of the theorem.

## Examples

### The Rank-One Algebra

Let $\mathrm{G} = \mathrm{sl}_2(\mathbb{R})$ with the Cartan involution $\alpha$ equal to the negative transpose, so that $\mathrm{G}^{+} = \mathrm{so}(2)$ and $\mathrm{G}^{-}$ is the space of the symmetric traceless matrices. For $a\in\mathrm{G}^{-}$ the reflection $\rho_a = e^{\operatorname{ad}_a}\alpha$ is an involution, its fixed subalgebra is one-dimensional, and the reflections of the odd part are the involutions attached to the hyperbolic directions; the geometric reading in the hyperbolic plane belongs to Part IV.

### The Orthogonal Algebra

Let $\mathrm{G} = \mathrm{so}(n)$ with the grading by the involution that is the conjugation by a diagonal form of signature $(p,q)$. Then the reflections of the odd part are the inner involutions attached to the elements that the involution inverts; the fixed subalgebra is the centraliser, and the correspondence of the theorem is the classical correspondence between the involutions and the elements of the symmetric space, whose geometry is Part IV.

### The Trivial Involution

Let $\mathrm{G} = \mathrm{gl}(n)$ with $\alpha = \mathrm{id}$. Then the reflections are the inner automorphisms $g\mapsto e^{X}ge^{-X}$ with $2X$ central, that is the scalar multiples of the identity in the semisimple part of the parameter; the reflection is an involution exactly on the cosets of the centre, and the fixed subalgebra is the centraliser of $X$.

## Summary

A **reflection** of a graded Lie algebra is a signed two-sided operator that is an involution; in the present model it is the **signed conjugation** $\rho_a = \operatorname{Ad}_{\exp a}\alpha$ with $\operatorname{Ad}_{\exp a} = e^{\operatorname{ad}_a}$, the Lie-algebraic form of the group conjugation $x\mapsto a\alpha(x)a^{-1}$. Its square is the inner automorphism of $a+\alpha(a)$, so it is an involution exactly when $a+\alpha(a)$ is central; every odd element satisfies this, and the odd part is the family of the automatically carrying elements. Two elements carry the same reflection exactly when they differ by a central element, so a reflection depends on the coset of its carrying element modulo the centre, and the correspondence between the reflections and the elements acting by an involution — the elements with $2a$ central — has the cosets of the centre as its fibres. The fixed set of a reflection is the subalgebra $\{x : \alpha(x) = e^{-\operatorname{ad}_a}x\}$, a coset of the fixed subalgebra of the grade involution, and it reduces to the centraliser when $\alpha = \mathrm{id}$. The construction degenerates when the grade involution is inner, when the algebra is abelian — every reflection then being $\alpha$ itself — when the carrying element is central, and when $\alpha$ is the identity, in which case the reflections are the ordinary inner involutions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | the grade involution, $\alpha^2 = \mathrm{id}$ |
| $\rho_a = e^{\operatorname{ad}_a}\alpha$ | the signed conjugation, the reflection |
| $\rho_a^2 = e^{\operatorname{ad}_{a+\alpha(a)}}$ | the square |
| $a + \alpha(a)\in Z(\mathrm{G})$ | the involution condition, the carrying elements |
| $E$ | the elements acting by an involution, $2a$ central |
| $\operatorname{Fix}(\rho_a) = \{x : \alpha(x) = e^{-\operatorname{ad}_a}x\}$ | the fixed subalgebra |
| $\mathfrak{c}(a) = \{x : [a,x] = 0\}$ | the centraliser, the case $\alpha = \mathrm{id}$ |
| $\mathrm{G}^{\alpha} = \mathrm{G}^{+}$ | the fixed subalgebra of the grade involution |
| odd part $\mathrm{G}^{-}$ | the automatically carrying elements |
| $R$ | the set of the reflections, the image of the correspondence |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the inner automorphisms, the centralisers and the involutions of a Lie algebra.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the inner automorphisms, the symmetric pairs and the Cartan involutions.
- Ottmar Loos, *Symmetric Spaces*, Volume I (Benjamin, 1969), for the involutions of a Lie algebra and the symmetric pairs.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the graded involutions and the correspondence with the elements.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the adjoint action, the inner automorphisms and the fixed subalgebras.
