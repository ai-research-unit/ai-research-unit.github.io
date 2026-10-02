
# __Reflections as Signed Two-Sided Operators on an Ordered Algebra__

## Introduction

A **reflection** of an algebra is an automorphism of order two, and a **reflection element** is an element $a$ that the grade involution inverts, $\alpha(a) = a^{-1}$. The previous article showed that every reflection element produces a reflection of the algebra, the **signed conjugation**

$$
\tau_a : x\mapsto a\,\alpha(x)\,a^{-1} = \Theta^{\alpha}_{a,\alpha(a)^{-1}}(x),
$$

which is a signed two-sided operator. This article reads the correspondence in both directions: the reflection elements form a group under the twisted product $(a,b)\mapsto a\alpha(b)$, the map $a\mapsto\tau_a$ is a **homomorphism** from that group onto the reflections of the algebra that the signed sandwich realises, and the homomorphism has a kernel — the **central reflection elements**, which act trivially — so that the correspondence is neither injective nor surjective. The **grade involution** itself is the reflection $\tau_1$ realised by the identity, which is the reason the graded structure sits inside the reflections; and the failure of the correspondence in the degenerate cases — central elements, an inner grade involution, and characteristic two — is stated exactly.

The article also gives the order-theoretic reading, which is what an ordered algebra adds: a reflection is **positive** when it preserves the cone of the algebra, and the signed two-sided operators that are positive are the ones whose grade involution and whose parameters preserve the cone. The reflections of the ordered algebra are therefore an invariant of the order as much as of the algebra, and the ones that come from the sandwich split into the order-preserving and the order-reversing ones according to the signs of the parameters.

The signed sandwich, its composition law and its reflection elements are *The Signed Sandwich on an Ordered Algebra*; the one-sided multiplications and the ordered algebra are *The Left and Right Multiplication Operators on an Ordered Algebra*; the grading and the grade involution are *Superalgebras and Graded Structures* of Part I; the order and the operator order are *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; the outer automorphisms and the conjugation classes are *The Operators on an Algebra* of Part I. The signed left multiplication, which is the one-sided companion of this article, is *The Signed Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Action on a Module over an Ordered Algebra*; and the adjoint of the signed sandwich is *The Signed Adjoint Sandwich on an Ordered Algebra* at the end of this category. The **unsigned** reflections of the associative algebra, the inner automorphisms and the involution of the algebra, are *The Operators on an Algebra* and *Ordered Involutive Algebras*, and they are cited.

## Reflections and Reflection Elements

**Definition.** A **reflection** of an algebra $A$ is an algebra automorphism $\sigma$ with $\sigma^2 = \mathrm{id}$. It is **positive** when it preserves the cone, $\sigma(A_+)\subseteq A_+$, and **order reversing** when $\sigma(A_+)\subseteq -A_+$. A **reflection element** is an element $a\in A$ with $\alpha(a) = a^{-1}$; the associated **signed two-sided operator** is the signed conjugation $\tau_a$.

**Proposition (well definedness and the fibre of the correspondence).** For every reflection element $a$ the operator $\tau_a$ is a reflection. Two reflection elements give the same reflection,

$$
\tau_a = \tau_{a'} ,
$$

if and only if the ratio $a^{-1}a'$ is central; consequently the map $a\mapsto\tau_a$ is injective modulo the central reflection elements, and no more.

*Proof.* The reflection property is the reflection theorem of *The Signed Sandwich on an Ordered Algebra*. If $a^{-1}a' = z$ is central then $a' = az$ and $\tau_{a'}(x) = az\alpha(x)(az)^{-1} = a\alpha(x)a^{-1} = \tau_a(x)$ because a central element commutes with everything; conversely $\tau_a = \tau_{a'}$ gives $a^{-1}a'\,\alpha(x) = \alpha(x)\,a^{-1}a'$ for every $x$, so $a^{-1}a'$ commutes with $\alpha(A) = A$.

**Proposition (the product of two realised reflections).** For reflection elements $a,b$,

$$
\tau_a\,\tau_b = \tau_{a\alpha(b)} ,
$$

the sandwich with the **product parameter** $c = a\alpha(b)$; this product is again a **realised reflection** if and only if $c$ is again a reflection element, which happens exactly when $a$ and $b$ commute. Hence a set of pairwise commuting reflection elements is a group under the twisted product $a\cdot b = a\alpha(b)$, with inverse $a\mapsto\alpha(a) = a^{-1}$ and identity $1$, and the correspondence is a group homomorphism on it.

*Proof.* By the composition law of the signed sandwich, $\tau_a\tau_b = \Theta^{\alpha}_{a\alpha(b),\,b^{-1}\alpha(a)^{-1}}$; the reflection-element identities $b^{-1} = \alpha(b)$ and $\alpha(a)^{-1} = a$ give $\Theta^{\alpha}_{a\alpha(b),\,b^{-1}a}$, which is $\tau_{a\alpha(b)}$ because $\alpha(a\alpha(b))^{-1} = (a^{-1}b)^{-1} = b^{-1}a$. The product parameter $c = a\alpha(b)$ is a reflection element exactly when $\alpha(c) = c^{-1}$, that is, $a^{-1}b = b\,a^{-1}$, which is the commutation of $a$ and $b$. When the elements commute pairwise, the closure, the associativity, the identity and the inverse make the set a group and the product formula makes $\tau$ a homomorphism.

## The Correspondence

**Theorem (the reflections realised by the signed sandwich).** The map

$$
\tau : R(A,\alpha)\to \operatorname{Aut}(A), \qquad a\mapsto\tau_a,
$$

from the set $R(A,\alpha)$ of reflection elements into the group of automorphisms of $A$ takes its values in the reflections, and two reflection elements give the same reflection exactly when their ratio is central. The image is

$$
\operatorname{im}\tau = \{\operatorname{Inn}_a\circ\alpha : a\in R(A,\alpha)\} ,
$$

the **realised reflections**, and the grade involution is the reflection $\tau_1$; every realised reflection is the composite of the grade involution with an inner automorphism, $\tau_a = \operatorname{Inn}_a\circ\alpha = \alpha\circ\operatorname{Inn}_{\alpha(a)^{-1}}$. When the grade involution is inner the realised reflections are exactly the inner reflections of $A$.

*Proof.* That $\tau_a$ is an involution is the reflection theorem of the previous article, and the fibre is the fibre proposition above. If $a$ is a reflection element then $\tau_a = \operatorname{Inn}_a\circ\alpha$ by definition and $\alpha\circ\operatorname{Inn}_{\alpha(a)^{-1}}(x) = \alpha(\alpha(a)^{-1}x\alpha(a)) = a\alpha(x)a^{-1}$, so the two composites agree. The inner case is the inner shift of the signed sandwich, under which the realised reflections are the inner automorphisms of $A$ of order two.

**Corollary (the reflections of the algebra that are realised).** A reflection $\sigma$ of $A$ is a signed two-sided operator if and only if $\alpha^{-1}\sigma$ is an inner automorphism; the parameters realising it are the reflection elements $a$ with $\operatorname{Inn}_a = \alpha^{-1}\sigma$, and they form a coset of the central reflection elements.

*Proof.* If $\sigma = \tau_a$ then $\alpha^{-1}\sigma = \operatorname{Inn}_a$ is inner by the composite formula. Conversely if $\alpha^{-1}\sigma = \operatorname{Inn}_a$ then $\sigma = \tau_a$; and $a$ is a reflection element because $\tau_a$ is a reflection, by the reflection theorem read backwards. The ambiguity is the fibre of $\operatorname{Inn}$, which is the centre.

### Positivity of the Reflections

**Proposition.** A realised reflection $\tau_a$ is positive if and only if the signed sandwich $\Theta^{\alpha}_{a,\alpha(a)^{-1}}$ is positive; in particular, if the grade involution is positive and both $a$ and $\alpha(a)^{-1}$ are positive, then $\tau_a$ is positive, and if the grade involution is positive and $a$ is positive while $\alpha(a)^{-1} = \alpha(a^{-1})$ is negative, then $\tau_a$ is order reversing. In the graded case with parity $\varepsilon$ the reflection acts as

$$
\tau_a(x) = \varepsilon_x\,\operatorname{Inn}_a(x) \qquad (x \ \text{homogeneous}) ,
$$

so it agrees with the ordinary inner conjugation on the even part and is its negative on the odd part.

*Proof.* The first statement is the definition of the positivity of an operator; the positivity criteria are those of the positivity proposition of *The Signed Sandwich on an Ordered Algebra*; the parity formula is the parity formula of the same proposition applied to the sandwich $\Theta^\alpha_{a,\alpha(a)^{-1}}$.

## The Failure in the Degenerate Cases

**Theorem (the correspondence is not injective).** The central reflection elements act trivially. If the centre of $A$ is nontrivial and the grade involution is the identity, every central involution is a reflection element with $\tau_a = \mathrm{id}$, so the map $a\mapsto\tau_a$ is not injective, and the reflections must be read **up to the centre**. In $A = \mathbb{R}$ the element $-1$ is a central reflection element with $\tau_{-1} = \mathrm{id}$; since $\mathbb{R}$ has no non-trivial algebra automorphism, the correspondence realises only the identity, and the example shows the smallest possible degeneracy.

*Proof.* This is the identification of the fibre in the well-definedness proposition; in a commutative algebra every element is central, so $\tau_a$ depends on $a$ only through the coset $aZ$.

**Theorem (the correspondence is not surjective).** An outer automorphism of order two that does not differ from the grade involution by an inner automorphism is a reflection of $A$ that is **not** a signed two-sided operator. In particular, if $\alpha$ is inner, no outer reflection is realised, and the image of $\tau$ consists of the inner reflections.

*Proof.* By the corollary, a realised reflection is $\alpha$ composed with an inner automorphism, so its class in the outer automorphism group is the class of $\alpha$; a reflection with a different outer class is not realised. When $\alpha$ is inner, the class of $\alpha$ is trivial, so the image is inner.

**Proposition (the collapse in the degenerate cases).** The correspondence degenerates in three ways: when the grade involution is **inner**, every signed sandwich is an unsigned sandwich with shifted parameters, so the realised reflections are the ordinary inner reflections; when the algebra is **commutative**, every element is central and the fibre is everything, so no non-trivial reflection is realised by the sandwich unless the grade involution differs from the identity; and in **characteristic two** the equation $\alpha^2 = \mathrm{id}$ with $\alpha$ an algebra automorphism forces every element to be even, the grading collapses, and the sign rule is trivial.

*Proof.* The inner case is the inner shift of the previous article; the commutative case is the non-injectivity theorem; in characteristic two, $-1 = 1$ so the two eigenspaces of $\alpha$ coincide and the decomposition into even and odd parts is the trivial one.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{R})$ with the identity grade involution. The reflection elements are the involutions $a^2 = 1$, and the reflected operator is the ordinary conjugation $\tau_a(x) = axa^{-1}$. The realised reflections are the inner involutions and the fibre over the trivial reflection is the set of central involutions $\{\pm I\}$, so $I$ and $-I$ realise the same reflection; the map $a\mapsto\tau_a$ is therefore not injective, and the reflections are read **up to the centre**. This is the simplest non-injective case.

### The Biquaternion Algebra

Let $A = \mathbb{B} = M_2(\mathbb{C})$ with $\alpha$ the conjugation by $\operatorname{diag}(1,-1)$. The off-diagonal element with $a^2 = -1$ is an odd reflection element, and $\tau_a$ is the signed conjugation: the ordinary conjugation by $a$ on the even part and its negative on the odd part. Since $\alpha$ is inner in $M_2(\mathbb{C})$, the signed conjugation is an unsigned sandwich after the shift of parameters, and the reflection $\tau_a$ is inner; the signed structure is thus invisible in the operator but visible in the **parity** of the element that realises it. This is the exact sense in which "the signed Hermitian member is not a second structure": the reflection is the ordinary one and the sign is the parity.

### The Clifford Algebra

Let $A$ be the Clifford algebra of a **nondegenerate** quadratic form on a vector space $V$, with the grade involution the parity. A vector $e$ with $e^2 = -1$ is odd and satisfies $\alpha(e) = -e = e^{-1}$, so it is a reflection element, and $\tau_e$ is an involution of $A$; restricted to $V$ it is a reflection of the vector space, up to the sign conventions of the form. The vectors $e$ and $-e$ give the same reflection, so the fibre is again $\{\pm1\}$ and the correspondence between the reflections of $V$ and the reflection elements is bijective modulo the sign. When the form is **degenerate** there are nonzero isotropic vectors $e$ with $e^2 = 0$; such an $e$ has no inverse, the reflection-element condition cannot be met, and the correspondence fails. This is the geometric content of the phrase "the failure in the degenerate cases", and the Clifford algebra instance that motivates the whole construction.

## Summary

A **reflection** of an algebra is an automorphism of order two, **positive** when it preserves the cone; a **reflection element** is an $a$ with $\alpha(a) = a^{-1}$. The reflected operator is the signed two-sided operator $\tau_a(x) = a\alpha(x)a^{-1} = \Theta^{\alpha}_{a,\alpha(a)^{-1}}(x)$; the map $\tau : a\mapsto\tau_a$ takes the reflection elements into the reflections, two reflection elements give the same reflection exactly when their ratio is central — this is the **non-injectivity** — and $\tau$ is a group homomorphism for the **twisted product** $a\cdot b = a\alpha(b)$ exactly on a set of pairwise commuting reflection elements. The realised reflections are exactly the composites of the grade involution with the inner automorphisms, $\tau_a = \operatorname{Inn}_a\circ\alpha$; the reflections with a different outer class are **not** realised — this is the **non-surjectivity**. The **grade involution is the reflection $\tau_1$**. In the graded case $\tau_a(x) = \varepsilon_x\operatorname{Inn}_a(x)$, the ordinary conjugation on the even part and its negative on the odd part, and the correspondence **collapses** when the grade involution is inner, when the algebra is commutative, and in characteristic two. The signed sandwich and its composition law are *The Signed Sandwich on an Ordered Algebra*; the one-sided multiplications are *The Left and Right Multiplication Operators on an Ordered Algebra*; the grading is *Superalgebras and Graded Structures*; the order is *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; and the adjoint of the signed sandwich is *The Signed Adjoint Sandwich on an Ordered Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma^2 = \mathrm{id}$ | Reflection, an automorphism of order two |
| $\alpha(a) = a^{-1}$ | Reflection element |
| $\tau_a(x) = a\alpha(x)a^{-1}$ | Reflected signed two-sided operator |
| $a\cdot b = a\alpha(b)$ | Twisted product of the reflection elements |
| $R(A,\alpha)$ | Set of reflection elements |
| $\tau_{a\alpha(b)} = \tau_a\tau_b$ | Product of two realised reflections |
| $a^{-1}a'$ central | The fibre: $\tau_a = \tau_{a'}$, the non-injectivity |
| $\tau_a = \operatorname{Inn}_a\circ\alpha$ | Outer class obstruction, the non-surjectivity |
| $\tau_1 = \alpha$ | The grade involution as a reflection |
| $\tau_a(x) = \varepsilon_x\operatorname{Inn}_a(x)$ | Parity formula in the graded case |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the reflections realised by the conjugation by a unit vector and the parity grading.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the graded structure and the reflection formula of a Clifford algebra.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1956), for the automorphisms, the inner automorphisms and the centre of an associative algebra.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the reflections and the sandwich operators of the Jordan structures.
- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the automorphisms of an operator algebra and the inner-outer dichotomy.
