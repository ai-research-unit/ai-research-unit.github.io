
# __The Involution on the Order Automorphisms__

## Introduction

An **order automorphism** of an ordered involutive algebra is an automorphism of the algebra that preserves the involution and the positive cone,

$$
T(ab) = T(a)T(b) , \qquad T(a^{*}) = T(a)^{*} , \qquad T(A_+) = A_+ ;
$$

these form a group $\operatorname{Aut}_o(A)$ under the composition. The **involution** of the algebra enters the group in two ways. First, the involution $\alpha$ is itself an order automorphism of order two, and it acts on the group by the **conjugation**

$$
\operatorname{conj}_\alpha : T\mapsto \alpha\,T\,\alpha^{-1} = \alpha T\alpha ,
$$

which is an automorphism of $\operatorname{Aut}_o(A)$ of order two; its fixed points are the automorphisms commuting with $\alpha$, the **\*-automorphisms** of the graded structure. Second, every order automorphism has an **adjoint** for the trace form, the map $T\mapsto T^{*}$, which is an **anti-automorphism** of the group (it reverses the composition) and preserves the order automorphisms; the composition of the two is the **involution on the order automorphisms**. The article states this double action, proves that it preserves the **positivity** — a positive (cone-preserving) automorphism is carried to a positive automorphism, and the adjoint of an order-preserving map is order preserving — and describes the order of the automorphism group itself.

The reason to isolate the involution on the automorphisms is that it is the structure behind the **graded** automorphisms and the **inner** automorphisms: the conjugations $L_aR_{a^{-1}}$ are order automorphisms, their involution is the conjugation by the corresponding element, and the graded automorphisms are the fixed points of the involution of the algebra. The article is therefore the group-theoretic companion of *Self-Adjoint Elements and the Order* and *The Adjoint of a Positive Operator*, and it prepares the adjoint computations of the signed operators that follow.

The adjoint and the positivity are *The Adjoint of a Positive Operator*; the ordered involution is *Ordered Involutive Algebras*; the self-adjoint elements and the order isomorphisms are *Self-Adjoint Elements and the Order*; the positive functionals are *Positive Functionals and Self-Adjointness*; the order and the order unit are *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; the adjoint of the left multiplication is *The Adjoint of the Left Multiplication on an Ordered Algebra*; and the signed adjoints are *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*. The operator-algebraic automorphism theory is *Operator Algebras* of Part II.

## The Order Automorphisms

**Definition.** The **order automorphisms** are the bijective linear maps $T$ of $A$ with

$$
T(ab) = T(a)T(b), \qquad T(a^{*}) = T(a)^{*}, \qquad T(A_+) = A_+ ,
$$

the group operation being the composition; the **positivity** of $T$ is the cone preservation $T(A_+)\subseteq A_+$, which for a bijection with the same property for $T^{-1}$ is the equality $T(A_+) = A_+$.

**Proposition (the group is carried to its opposite by the adjoint).** The adjoint map $T\mapsto T^{*}$ carries order automorphisms to order automorphisms and is an **anti-automorphism** of the group,

$$
(ST)^{*} = T^{*}S^{*}, \qquad (T^{-1})^{*} = (T^{*})^{-1} ,
$$

and it is an involution of order two; the group $\operatorname{Aut}_o(A)$ is therefore closed under the adjoint, and the **self-adjoint** order automorphisms $T = T^{*}$ form a distinguished subset.

*Proof.* The adjoint reverses the composition by *The Adjoint of a Positive Operator*; the adjoint of an order automorphism is an order automorphism because the adjoint preserves the positivity and the invertibility (the adjoint of the inverse is the inverse of the adjoint, by the order-two property); the order-two property is the involution of the adjoint.

**Proposition (the inner automorphisms).** For every **unitary** $a$ (that is, $a^{*}a = aa^{*} = 1$), the conjugation

$$
\Phi_a : x\mapsto a\,x\,a^{-1}
$$

is an order automorphism; it is a \*-automorphism exactly when it commutes with the involution, $a x a^{-1} = (a x^{*} a^{-1})^{*}$ for every $x$, that is, when $a$ is **central** or the involution is **inner** in the appropriate sense; the map $a\mapsto\Phi_a$ is a homomorphism of the unitary group onto the inner automorphism group, with the central unitaries as kernel.

*Proof.* The conjugation by an invertible element is an algebra automorphism; it preserves the cone because $a$ and $a^{-1}$ preserve the cone as unitaries of the ordered involutive algebra; the \*-preservation is the displayed condition, which holds when the involution intertwines as indicated; the kernel is the set of the $a$ with $ax = xa$ for all $x$, the central unitaries.

## The Involution on the Automorphisms

**Theorem (the conjugation by the involution).** The map

$$
\operatorname{conj}_\alpha : \operatorname{Aut}_o(A)\to\operatorname{Aut}_o(A), \qquad \operatorname{conj}_\alpha(T) = \alpha\,T\,\alpha^{-1} ,
$$

is an **automorphism of the group of order two**, an **order automorphism** of the group in the sense that it preserves the positivity,

$$
T(A_+)\subseteq A_+ \implies \operatorname{conj}_\alpha(T)(A_+)\subseteq A_+ ,
$$

and its fixed points are the automorphisms commuting with the involution of the algebra,

$$
\operatorname{conj}_\alpha(T) = T \iff \alpha T = T\alpha ,
$$

the **\*-automorphisms** of the ordered involutive structure.

*Proof.* The conjugation by a fixed automorphism is a group automorphism; it is of order two because $\alpha$ is of order two. It preserves the positivity because $\alpha$ and $\alpha^{-1}$ preserve the cone, so their composition with a cone-preserving $T$ is cone preserving. The fixed-point statement is the rearrangement $\alpha T\alpha^{-1} = T\iff\alpha T = T\alpha$.

**Proposition (the involution on the automorphisms is the adjoint-composition).** The two actions on $\operatorname{Aut}_o(A)$ — the conjugation by the involution and the adjoint map — combine into the **involution on the order automorphisms**

$$
T\mapsto (\operatorname{conj}_\alpha\circ *)(T) = \alpha T^{*}\alpha^{-1} = \alpha T^{*}\alpha ,
$$

which is an **anti-automorphism** of order two of the group, preserves the order automorphisms, and is the identity exactly on the order automorphisms that are **self-adjoint and \*-commuting**, $T^{*} = \alpha T\alpha$.

*Proof.* The composition of a group automorphism of order two with a group anti-automorphism of order two is an anti-automorphism of order two; the preservation of the order automorphisms is the two statements above; the fixed-point computation is the rearrangement $\alpha T^{*}\alpha = T$.

**Corollary (the order and the involution).** The order automorphisms that commute with the involution form a subgroup of $\operatorname{Aut}_o(A)$, and the order automorphisms whose adjoint is their inverse form the subgroup of the **orthogonal** order automorphisms; the involution on the automorphisms restricts to an automorphism of the first and to the identity on the second, so the order-automorphism group splits into the \*-commuting automorphisms and the orthogonal ones.

*Proof.* The subgroups are defined by the algebraic conditions and are closed under the composition; the action of the involution coincides with the adjoint on the \*-commuting automorphisms and with the inverse on the orthogonal ones, giving the stated restrictions.

## The Positivity and the Order of the Group

**Definition.** The **order** of the automorphism group is

$$
S\preceq T \iff S^{-1}T(A_+)\subseteq A_+ ,
$$

the **positive order** of $\operatorname{Aut}_o(A)$ by the positivity of the "quotient" $S^{-1}T$.

**Proposition (the positivity of the automorphisms).** The relation $\preceq$ is a partial order on $\operatorname{Aut}_o(A)$ compatible with the group structure, it is preserved by the involution on the automorphisms, and the positive automorphisms are exactly the cone-preserving ones, $T(A_+)\subseteq A_+$, which are the same as the automorphisms with $1\preceq T$ in the positive order.

*Proof.* The relation is reflexive ($S^{-1}S = 1$ preserves the cone), transitive (the composition of the cone-preserving maps preserves the cone) and antisymmetric on the automorphisms (a bijection preserving the cone with the same property for the inverse is an order automorphism, and the only order automorphism $\preceq$-below and above the identity is the identity); the compatibility with the group structure is the multiplicativity of the conjugation; the preservation by the involution is the preservation of the positivity by the conjugation; the identification of the positive elements is the definition.

**Proposition (the positivity of the conjugation).** The conjugation by the involution carries a positive automorphism to a positive automorphism, $T\succeq1\implies\operatorname{conj}_\alpha(T)\succeq1$; the adjoint of a positive order automorphism is positive; and the involution on the automorphisms preserves the positive order. Consequently the positivity of the automorphisms is an invariant of the involution.

*Proof.* The first two statements are the positivity preservation of the conjugation and of the adjoint; the third is their composition; the invariance statement is the conclusion.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the trace form and the Loewner order. The order automorphisms are the conjugations $\Phi_U : X\mapsto UXU^{*}$ by the unitaries, all of which are inner; the involution conjugation by $\alpha = $ the identity in the ungraded case, or by a self-adjoint unitary in a graded case, has the \*-commuting automorphisms as fixed points, and the adjoint of $\Phi_U$ is the conjugation by $U^{*}$. The positivity of the conjugations is the unitary invariance of the Loewner order. This is the finite-dimensional model.

### The Self-Adjoint Operators

Let $A$ be a von Neumann algebra with the Loewner order and the trace form. The order automorphisms are the \*-automorphisms preserving the cone, the inner ones being the conjugations by the unitaries of the algebra, and the involution $\alpha$ acts by conjugation; the fixed points are the \*-automorphisms commuting with $\alpha$, and the adjoint of an inner automorphism is the inner automorphism of the adjoint unitary. The positivity is the cone preservation of the \*-automorphisms.

### The Continuous Functions

Let $A = C(X,\mathbb{C})$ with the pointwise order. The order automorphisms are the homeomorphisms of $X$ acting on the functions by composition, together with the conjugation; the involution acts by conjugation on them, its fixed points are the automorphisms commuting with the conjugation (the "real" homeomorphisms), and the adjoint map is the identity on them because the functions are complex valued and the trace form is symmetric. The commutative case shows that the involution on the automorphisms is the grading of the automorphism group by the reality of the homeomorphisms.

## Summary

The **order automorphisms** of an ordered involutive algebra are the automorphisms preserving the involution and the cone; they form a group, and the **adjoint** map $T\mapsto T^{*}$ is an anti-automorphism of the group of order two which preserves the order automorphisms. The **involution** $\alpha$ acts on the group by the **conjugation** $T\mapsto\alpha T\alpha^{-1}$, an automorphism of order two which **preserves the positivity** and whose fixed points are the **\*-automorphisms** (the automorphisms commuting with $\alpha$); the composition of the two actions is the **involution on the order automorphisms** $T\mapsto\alpha T^{*}\alpha$, an anti-automorphism of order two. The automorphism group carries the **positive order** $S\preceq T\iff S^{-1}T$ is cone preserving, compatible with the group structure and preserved by the involution; the inner automorphisms are the conjugations by the unitaries, and the **positivity** of the automorphisms is the cone preservation, which is invariant under the involution. The adjoint and the positivity are *The Adjoint of a Positive Operator*; the ordered involution is *Ordered Involutive Algebras*; the self-adjoint order isomorphisms are *Self-Adjoint Elements and the Order*; the positive functionals are *Positive Functionals and Self-Adjointness*; the order is *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; and the concrete adjoints are *The Adjoint of the Left Multiplication on an Ordered Algebra*, *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Aut}_o(A)$ | Group of the order automorphisms |
| $T(A_+) = A_+$ | Order automorphism |
| $T\mapsto T^{*}$ | Adjoint, an anti-automorphism of order two |
| $T\mapsto\alpha T\alpha^{-1}$ | Conjugation by the involution |
| $\alpha T = T\alpha$ | Fixed points: the \*-automorphisms |
| $T\mapsto\alpha T^{*}\alpha$ | Involution on the order automorphisms |
| $S\preceq T\iff S^{-1}T(A_+)\subseteq A_+$ | Positive order of the automorphism group |
| $\Phi_a : x\mapsto axa^{-1}$ | Inner automorphism |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the \*-automorphisms, the inner automorphisms and the order.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the automorphism groups, the grading involutions and the positivity.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the \*-automorphisms of the operator algebras and the order.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the order automorphisms of the state spaces and the positivity.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the cone-preserving maps and the positive order of the automorphism groups.
