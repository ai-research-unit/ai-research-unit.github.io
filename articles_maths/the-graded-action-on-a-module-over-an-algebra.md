# __The Graded Action on a Module over an Algebra__

## Introduction

An algebra acts on its modules by linear operators, and when both the algebra and the module carry a $\mathbb{Z}/2$-grading the action has to respect it. The compatibility is a degree rule — multiplying by an element of degree $i$ shifts the degree of a homogeneous element by $i$ — and it forces a sign rule on the operators that represent the action: the even elements act by degree-preserving operators, the odd ones by degree-reversing operators, and the representation is a morphism of graded algebras whose brackets carry a sign.

The present article studies the action as an operator and reads off the degree and the sign. The module theory itself is *Modules over an Algebra*, the grading of the algebra comes from the involutive automorphism $\alpha$ of *The Signed Sandwich on an Algebra*, and the general theory of graded algebras and graded modules, of the Koszul sign rule and of the symmetric monoidal structure is *Superalgebras and Graded Structures*, which is named as the owner and not used.

Throughout, $k$ is a field, $A$ is a unital associative $k$-algebra with an involutive automorphism $\alpha$, and $A = A^+ \oplus A^-$ is the induced $\mathbb{Z}/2$-grading of *The Signed Sandwich on an Algebra*. Elements of $A^\pm$ are **homogeneous** of degree $0$ (even) or $1$ (odd), written $|a| \in \{0,1\}$; a product of homogeneous elements is homogeneous of degree $|a| + |b|$ taken modulo two. The module theory, the bimodule structures and the tensor products are those of *Modules over an Algebra* and *The Balanced Product over an Algebra*.

## The Graded Module

### Definition

**Definition.** Let $M$ be an $A$-module. A **$\mathbb{Z}/2$-grading** of $M$ compatible with the grading of $A$ is a direct sum decomposition

$$
M = M^+ \oplus M^- = M^0 \oplus M^1
$$

such that

$$
A^i \cdot M^j \subseteq M^{i+j}, \qquad i, j \in \{0,1\},
$$

with the degrees added modulo two. A module with such a grading is a **graded module** over the graded algebra $A$, and its elements in $M^0$ and $M^1$ are the even and the odd elements of $M$.

The condition is the module analogue of the multiplication table of the grading of $A$, and it is exactly the statement that the action sees the grading: an even element of the algebra sends an even module element to an even one and an odd one to an odd one; an odd element of the algebra reverses the parity. When $A^- = 0$ the condition is vacuous and every module carries the trivial grading $M^0 = M$, $M^1 = 0$.

### The Operators of the Action

**Definition.** Let $M$ be a graded $A$-module. For $a \in A$ let

$$
\rho(a) : M \to M, \qquad \rho(a)(m) = a \cdot m
$$

be the operator by which $a$ acts on $M$. The assignment $\rho : A \to \operatorname{End}_k(M)$ is the **action map**, or representation, of the module.

**Proposition.** The action map is a homomorphism of unital $k$-algebras, $\rho(ab) = \rho(a)\rho(b)$ and $\rho(1) = \mathrm{id}_M$. If $a$ is homogeneous then $\rho(a)$ has a definite degree, and

$$
\rho(a)\bigl(M^j\bigr) \subseteq M^{\,j + |a|} \qquad \text{for homogeneous } a \text{ and } j \in \{0,1\}.
$$

*Proof.* The homomorphism property is the associativity and the unit of the module action, from *Modules over an Algebra*. The degree statement is the compatibility $A^i M^j \subseteq M^{i+j}$ with $i = |a|$, read through $\rho(a)m = am$.

**Corollary.** The even elements of $A$ act by parity-preserving operators, $\rho(a)(M^j) \subseteq M^j$ for $a \in A^+$, and the odd elements act by parity-reversing operators, $\rho(a)(M^j) \subseteq M^{1-j}$ for $a \in A^-$. In particular an even element preserves each graded piece and an odd element exchanges the two.

The corollary is the operator form of the degree rule: the grading of the algebra becomes a grading of the operators, and the action is a graded action. The refined theory of the space $\operatorname{End}_k(M)$ as a graded algebra, with the sign attached to the transposition of two odd operators, belongs to *Superalgebras and Graded Structures*; the present article records the degrees and the brackets of the elements actually met.

## The Degree and the Sign Rule

### The Degree of the Action

**Proposition.** For homogeneous $a \in A$ and homogeneous $m \in M$, the product $a \cdot m$ is homogeneous of degree

$$
|a \cdot m| = |a| + |m| \pmod 2 .
$$

Equivalently, the action is a bilinear map of graded sets

$$
A^i \times M^j \to M^{\,i+j},
$$

and it is the unique extension of its values on homogeneous elements to all of $A \times M$ by linearity.

*Proof.* The degree formula is the containment $A^i M^j \subseteq M^{i+j}$ written for a single homogeneous pair; bilinearity is the definition of a module action, and the extension by linearity is the definition of the sum decomposition.

### The Sign Rule of the Graded Commutator

**Definition.** For two homogeneous operators $S, T$ on a graded module their **graded commutator** is

$$
[S, T]_{\mathrm{gr}} = S T - (-1)^{|S||T|} T S,
$$

where $|S|$ is the degree of the operator; for operators of even degree this is the ordinary commutator and for two odd operators it is the ordinary anticommutator.

**Theorem.** Let $M$ be a graded $A$-module and let $\rho$ be its action map. For homogeneous $a, b \in A$,

$$
\bigl[\rho(a),\, \rho(b)\bigr]_{\mathrm{gr}} = \rho\bigl([a,b]_{\mathrm{gr}}\bigr), \qquad \text{where} \qquad [a,b]_{\mathrm{gr}} = ab - (-1)^{|a||b|} b a .
$$

Hence the action map is a morphism of graded algebras: it carries the graded commutator of the algebra to the graded commutator of the operators, and it preserves the degrees.

*Proof.* By the homomorphism property $\rho(a)\rho(b) = \rho(ab)$ and $\rho(b)\rho(a) = \rho(ba)$. The operator $\rho(a)$ has degree $|a|$ by the degree proposition, so $|\rho(a)| = |a|$, and the sign in the graded commutator of the operators is $(-1)^{|a||b|}$, the same as in the algebra. Subtracting gives $\rho(ab) - (-1)^{|a||b|}\rho(ba) = \rho(ab - (-1)^{|a||b|}ba)$.

**Corollary.** If $a$ and $b$ are both even, then $[\rho(a),\rho(b)] = \rho([a,b])$; if $a$ is even, then $\rho(a)$ commutes with every operator $\rho(b)$ in the graded sense; and if $a$ and $b$ are both odd, then

$$
\{\rho(a),\rho(b)\} = \rho(\{a,b\}), \qquad \{a,b\} = ab + ba .
$$

*Proof.* The sign $(-1)^{|a||b|}$ is $+1$ when at least one of the degrees is even and $-1$ when both are odd.

The corollary is the sign rule that the graded action imposes: even elements act by operators that commute with the whole representation, and the odd elements produce anticommutators. It is the module-level statement of the same rule that appears on the algebra alone in *The Signed Left Multiplication on an Algebra*, where the commutator of an odd left multiplication with a signed one is the anticommutator.

### The Twisted Action

**Definition.** Let $M$ be a graded $A$-module. The **twisted action** is the action of the same algebra with the twist inserted,

$$
a \star m = \alpha(a) \cdot m = \rho(\alpha(a))(m) .
$$

An element $a \in A$ is **graded central** on $M$ if it commutes with the action up to the sign of the degrees,

$$
a \cdot (b \cdot m) = (-1)^{|a||b|}\, b \cdot (a \cdot m) \quad \text{for homogeneous } a, b, m .
$$

**Proposition.** The twisted action is an action of $A$ on $M$, its operators are $\rho(\alpha(a))$, and the degree of the operator $\rho(\alpha(a))$ equals $|a|$ because $\alpha$ preserves the grading. An element $a$ is graded central on $M$ exactly when $\rho(a)$ commutes with every operator $\rho(b)$ in the graded sense, that is when $\rho(a)$ lies in the graded centre of the image of $\rho$.

*Proof.* The composite $\rho \circ \alpha$ is a homomorphism because $\alpha$ is an algebra automorphism of $A$, and a homomorphism $A \to \operatorname{End}_k(M)$ is an action. The degree is preserved because $\alpha(A^\pm) = A^\pm$. The graded centrality of $a$ is the equation $\rho(a)\rho(b) = (-1)^{|a||b|}\rho(b)\rho(a)$ for all homogeneous $b$, which is the definition of the graded centraliser of the image.

**Remark.** There is no general commutator relation between the twisted action and the original one, and none is claimed: the two actions agree on $A^+$ and satisfy $\rho(\alpha(a)) = \rho(a)$ for even $a$, while for odd $a$ the twisted operator is $-\rho(a)$. The sign rule of the article is the graded bracket of the single action, not a bracket between the two actions. The module-level form of the signed sandwich is the operator $L(a)\alpha$ of *The Signed Left Multiplication on an Algebra*, which is the regular action with the involution inserted in the middle of the operator.

## The Regular and the Trivial Gradings

### The Regular Module

**Proposition.** The algebra $A$ is a graded module over itself with the left action of *Modules over an Algebra*, and its action map is the left regular representation $L$ of *Left and Right Multiplication*. The inner action sends homogeneous $a$ to an operator of degree $|a|$, so $L$ is a morphism of graded algebras

$$
L : A \to \operatorname{End}_k(A), \qquad [L(a), L(b)]_{\mathrm{gr}} = L\bigl([a,b]_{\mathrm{gr}}\bigr).
$$

*Proof.* The module axioms are those of the regular module, and the degree statement is the degree proposition for $M = A$; the bracket identity is the theorem applied to the left action.

**Corollary.** The signed left multiplication $\Lambda(a) = L(a)\alpha$ of *The Signed Left Multiplication on an Algebra* is the left regular action composed with the involution on the module, and its degree is $|a|$; it satisfies the same graded bracket rule. On the even part $\Lambda(a) = L(a)$, and on the odd part $\Lambda(a) = -L(a)$.

*Proof.* This is the identity $\Lambda(a) = L(a)\alpha$ of *The Signed Left Multiplication on an Algebra*, with $\alpha$ read as the involution acting on the module $A$; since $\alpha$ is the identity on $A^+$ and minus the identity on $A^-$, the two statements on the parities follow. The bracket rule holds because the left action is a graded homomorphism and $\alpha$ preserves the grading.

### The Trivial Grading

**Proposition.** If $A^- = 0$, equivalently $\alpha = \mathrm{id}$ by *The Signed Sandwich on an Algebra*, then every module carries the trivial grading $M^0 = M$, $M^1 = 0$, every operator is even, the graded commutator is the ordinary commutator, and the sign rule is empty. Every statement of the article reduces to the corresponding statement of *Modules over an Algebra*.

*Proof.* With $A^- = 0$ the compatibility $A^i M^j \subseteq M^{i+j}$ is vacuous, the degrees are all zero, and $(-1)^{|a||m|} = 1$; the graded commutator of two even operators is the ordinary one.

### The Free Module

**Proposition.** The free module $A^n$ of *Modules over an Algebra*, with the grading that puts a copy of $A$ in each summand, is a graded module, and its action is by the matrix of left multiplications of *Left and Right Multiplication*. In particular the action of $A$ on $A^n$ is the operator of the matrix multiplication by $a$, of degree $|a|$, and the graded bracket of two such operators is the operator of the graded bracket of the two matrices.

*Proof.* The action of $A$ on $A^n$ is componentwise left multiplication, so it is the direct sum of $n$ copies of the regular action and inherits its degree and its brackets.

## The Morphisms

### The Graded Module Homomorphisms

**Definition.** Let $M$ and $N$ be graded $A$-modules. An $A$-module homomorphism $f : M \to N$ is **graded** if it is homogeneous of some degree $j$, $f(M^i) \subseteq N^{\,i+j}$, and the module of graded homomorphisms of degree $j$ is written $\operatorname{Hom}_A(M,N)^j$, so that

$$
\operatorname{Hom}_A(M, N) = \operatorname{Hom}_A(M,N)^0 \oplus \operatorname{Hom}_A(M,N)^1 .
$$

**Proposition.** The composition of a graded homomorphism of degree $j$ with one of degree $j'$ has degree $j + j'$, so $\operatorname{Hom}_A(M,M)$ is a graded algebra under composition; and each $\operatorname{Hom}_A(M,N)^j$ is a $k$-subspace of $\operatorname{Hom}_k(M,N)$.

*Proof.* Degrees add under composition of graded maps, and $A$-linearity is preserved by composition; the subspace statement is the definition.

**Corollary.** The action map $\rho : A \to \operatorname{End}_k(M)$ is a graded homomorphism of degree zero from the graded algebra $A$ to the graded algebra $\operatorname{End}_k(M)$, and the graded commutator rule of the theorem is the statement that it is a morphism of graded algebras.

## The Examples

### The Exterior Algebra as a Graded Module

Let $A = \Lambda(V)$ with the degree grading and let $M = A$ with the regular action. The even part is spanned by the products of an even number of vectors, the odd part by the products of an odd number, and an even element of $A$ acts by a parity-preserving operator while an odd element acts by a parity-reversing one; the action is the exterior multiplication, of degree equal to the degree of the multiplying element. The operator $\Lambda(v)$ for an odd $v$ is a square-zero operator of degree one, by *The Signed Left Multiplication on an Algebra*, and its square acts by the element $v\alpha(v) = -v^2 = 0$.

### A Group Algebra with a Parity

Let $A = k[G]$ with a parity homomorphism $\chi$ as in *The Signed Sandwich on an Algebra*, and let $M = k[G]$ with the regular action. A group element $g$ acts with degree $|g| = 0$ when $\chi(g) = 1$ and degree $1$ when $\chi(g) = -1$; the even group elements act by parity-preserving operators, the odd ones by parity-reversing operators, and two odd group elements have the anticommutator relation $\{\rho(g),\rho(h)\} = \rho(gh) + \rho(hg)$.

### A Module Concentrated in One Degree

Let $M = M^0$ be an even module over $A$, so that $A^- \cdot M = 0$; the action of the odd part of the algebra is zero, and the graded module is the ordinary module of *Modules over an Algebra* with the trivial grading. This is the degenerate case, and it is the one in which the whole graded theory collapses.

## Summary

Let $A$ be graded by the involutive automorphism $\alpha$, $A = A^+ \oplus A^-$. A **graded module** is an $A$-module $M$ with a decomposition $M = M^0 \oplus M^1$ compatible with the grading, $A^i M^j \subseteq M^{i+j}$. Its action map $\rho(a)m = am$ is a unital algebra homomorphism with $\rho(a)(M^j) \subseteq M^{j + |a|}$ for homogeneous $a$, so the even elements act by parity-preserving operators and the odd elements by parity-reversing ones, and the degree of a product is additive, $|a \cdot m| = |a| + |m|$ modulo two. The sign rule is the graded bracket: with $[S,T]_{\mathrm{gr}} = ST - (-1)^{|S||T|}TS$ one has

$$
[\rho(a),\rho(b)]_{\mathrm{gr}} = \rho\bigl([a,b]_{\mathrm{gr}}\bigr), \qquad [a,b]_{\mathrm{gr}} = ab - (-1)^{|a||b|}ba,
$$

so that even elements commute with the whole action in the graded sense and two odd elements have the anticommutator rule $\{\rho(a),\rho(b)\} = \rho(ab + ba)$. The twisted action $a \star m = \alpha(a)m$ is the module-level form of the signed sandwich; the regular module realizes the action as the left multiplications $L$, which is a morphism of graded algebras, and $\Lambda(a) = L(a)\alpha$ is the same action with the involution inserted; the free module realizes it as matrix multiplication, and the graded homomorphisms form a graded algebra under composition. When $A^- = 0$ the grading is trivial and the theory reduces to *Modules over an Algebra*; the general theory of graded algebras, of the symmetric monoidal structure and of the Koszul sign rule is *Superalgebras and Graded Structures*, and the module and tensor theory used here is *Modules over an Algebra* and *The Balanced Product over an Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A = A^+ \oplus A^-$ | the graded algebra, from the involutive automorphism $\alpha$ |
| $M = M^0 \oplus M^1$ | the graded module |
| $A^i M^j \subseteq M^{i+j}$ | the compatibility of the action with the grading |
| $\rho(a)(m) = a \cdot m$ | the action map of the module |
| $|a|, |m| \in \{0,1\}$ | the degrees of homogeneous elements |
| $\rho(a)(M^j) \subseteq M^{j + |a|}$ | the degree of the operator $\rho(a)$ |
| $[S,T]_{\mathrm{gr}} = ST - (-1)^{|S||T|}TS$ | the graded commutator of operators |
| $\{a,b\} = ab + ba$ | the anticommutator of two odd elements |
| $a \star m = \alpha(a)m$ | the twisted action |
| $\operatorname{Hom}_A(M,N)^j$ | the graded homomorphisms of degree $j$ |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the module theory and the representation map.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the action of a graded algebra and the graded modules.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the regular module and the inner action.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, second edition, 1997), for the sign rule of the graded and super setting.
