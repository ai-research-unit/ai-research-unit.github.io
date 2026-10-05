# __Opposite Algebras and Anti-Isomorphisms__

## Introduction

Every algebra has a mirror image, the **opposite algebra** $A^{\mathrm{op}}$, obtained by keeping the additive group and the scalars and reversing the order of every product. The mirror is not a curiosity: it is the algebra in which the right modules of $A$ become left modules, and it is the algebra that a right action secretly uses. The maps that compare an algebra with its mirror are the **anti-isomorphisms**, the bijections that reverse products, and the involutions of *Involutive Bilinear Algebras* are exactly the anti-isomorphisms of order two from an algebra to itself.

This article develops the opposite algebra as a construction, with its functoriality and its behaviour under the tensor product, the group algebra and the matrix algebra; the anti-isomorphisms onto it, with the calculus of composition that turns two anti-maps into a map; and the place of the involution as the special anti-isomorphism of order two. The notion of an involution, the symmetric and the skew elements and their Lie and Jordan structures are the subject of *Involutive Bilinear Algebras*, and they are cited rather than restated.

Throughout, $k$ is a field, $A$ and $B$ are unital associative $k$-algebras, and the unit is $1$; the opposite algebra is written $A^{\mathrm{op}}$, and the element $a$ of $A$, viewed in $A^{\mathrm{op}}$, is written $a^{\mathrm{op}}$ when the two algebras are being compared. The tensor products are over $k$, and $\operatorname{End}$ means $\operatorname{End}_k$. The algebras, the ideals and the centre are those of *Algebras*, *Ideals and Quotients of Algebras* and *Centre, Units, Zero Divisors and Division Algebras*; the modules are those of *Modules over an Algebra* and the tensor products those of *Tensor Products of Algebras*.

## The Opposite Algebra

### Definition

**Definition.** The **opposite algebra** $A^{\mathrm{op}}$ of $A$ is the $k$-algebra whose additive group and scalar action are those of $A$ and whose product is

$$
a^{\mathrm{op}} \cdot b^{\mathrm{op}} = (ba)^{\mathrm{op}} .
$$

The identity of $A^{\mathrm{op}}$ is $1^{\mathrm{op}}$, and the **opposite map**

$$
\iota_A : A \longrightarrow A^{\mathrm{op}}, \qquad \iota_A(a) = a^{\mathrm{op}}
$$

is $k$-linear and bijective, and reverses products, $\iota_A(ab) = \iota_A(b)\iota_A(a)$; it is therefore an anti-isomorphism.

The opposite algebra is introduced with the object in *Algebras*; the definition is repeated here because the whole article is the reading of the construction. The map $\iota_A$ is the identity on the underlying set and the reversal of the product, so it is an anti-isomorphism and not an isomorphism unless $A$ is commutative.

### Elementary Properties

**Proposition.** Let $A$ be a unital associative $k$-algebra. Then

**(a)** $(A^{\mathrm{op}})^{\mathrm{op}} = A$, with $\iota_{A^{\mathrm{op}}} \circ \iota_A = \mathrm{id}_A$;

**(b)** $A^{\mathrm{op}}$ is associative with the same unit, and $Z(A^{\mathrm{op}}) = Z(A)$;

**(c)** $A$ is commutative if and only if $A^{\mathrm{op}} = A$;

**(d)** $(A^{\mathrm{op}})^\times = A^\times$ as a set, and the group $(A^{\mathrm{op}})^\times$ is the opposite group of $A^\times$;

**(e)** for ideals $I \subseteq A$ the set $I$ is a two-sided ideal of $A^{\mathrm{op}}$, and $(A/I)^{\mathrm{op}} = A^{\mathrm{op}}/I$.

*Proof.* (a) Reversing the product twice restores it, and the two maps are inverse bijections. (b) The associativity of $A^{\mathrm{op}}$ is the associativity of $A$ read in the reverse order, and the unit is unaffected; $z$ commutes with every $a$ in $A^{\mathrm{op}}$ exactly when $az = za$ in $A$, which is the centre. (c) $A^{\mathrm{op}} = A$ says $ab = ba$ for every pair, which is commutativity. (d) A bijective map reverses the product exactly when it carries the unit to the unit and preserves invertibility with the inverse reversed; the group of units of the opposite algebra is the opposite group of $A^\times$ because the product is reversed. (e) An ideal is closed under multiplication on both sides by every element, a property symmetric in the order of the two factors, so it is again an ideal in $A^{\mathrm{op}}$; the quotient product is reversed.

**Corollary.** Every algebra is anti-isomorphic to its opposite, and the anti-isomorphism $\iota_A$ is canonical. The algebras $A$ and $A^{\mathrm{op}}$ therefore have the same dimension, the same centre and the same lattice of two-sided ideals, and are either equal (when $A$ is commutative) or distinct as subalgebras of a common ambient algebra (when $A$ is not).

The corollary is the reason the opposite algebra is a construction and not a new object: it is the same underlying structure with the product read backwards, and every property of $A$ that is symmetric in the order of a product passes to $A^{\mathrm{op}}$.

### Functoriality

**Proposition.** The assignment $A \mapsto A^{\mathrm{op}}$ on the objects extends to a functor: a $k$-algebra homomorphism $f : A \to B$ induces a $k$-algebra homomorphism $f^{\mathrm{op}} : A^{\mathrm{op}} \to B^{\mathrm{op}}$ by $f^{\mathrm{op}}(a^{\mathrm{op}}) = f(a)^{\mathrm{op}}$, the identities $\mathrm{id}^{\mathrm{op}} = \mathrm{id}$ and $(g \circ f)^{\mathrm{op}} = g^{\mathrm{op}} \circ f^{\mathrm{op}}$ hold, and an isomorphism $f$ induces an isomorphism $f^{\mathrm{op}}$.

*Proof.* For $a, b \in A$, $f^{\mathrm{op}}(a^{\mathrm{op}} b^{\mathrm{op}}) = f^{\mathrm{op}}((ba)^{\mathrm{op}}) = f(ba)^{\mathrm{op}} = (f(b)f(a))^{\mathrm{op}} = f(a)^{\mathrm{op}} f(b)^{\mathrm{op}} = f^{\mathrm{op}}(a^{\mathrm{op}})f^{\mathrm{op}}(b^{\mathrm{op}})$. The functorial identities follow from the definition and the bijectivity from that of $f$.

### Tensor Products and Standard Instances

**Proposition.** For $k$-algebras $A$ and $B$ the swap $\tau(a \otimes b) = b \otimes a$ is an isomorphism of algebras

$$
(A \otimes_k B)^{\mathrm{op}} \cong A^{\mathrm{op}} \otimes_k B^{\mathrm{op}}, \qquad (a \otimes b)^{\mathrm{op}} \longmapsto a^{\mathrm{op}} \otimes b^{\mathrm{op}} .
$$

*Proof.* Both sides are spanned by the decomposable elements and both products reverse the two factors and keep their order: $(a \otimes b)^{\mathrm{op}}(a' \otimes b')^{\mathrm{op}} = ((a' \otimes b')(a \otimes b))^{\mathrm{op}} = (a'a \otimes b'b)^{\mathrm{op}}$, which corresponds to $a^{\mathrm{op}}a'^{\mathrm{op}} \otimes b^{\mathrm{op}}b'^{\mathrm{op}}$, the product of the two images in $A^{\mathrm{op}} \otimes B^{\mathrm{op}}$. The map is $k$-bilinear on the factors, hence defined on the tensor product, and it is a bijection with inverse the corresponding map for the opposite algebras.

**Corollary (the standard instances).** The following hold.

**(1)** For a finite-dimensional $k$-linear space $V$, the transpose is an isomorphism $\operatorname{End}_k(V)^{\mathrm{op}} \cong \operatorname{End}_k(V)$: a matrix acts on the opposite algebra by acting on the transposed matrix, $(X^{\mathsf{T}})^{\mathrm{op}} = X^{\mathsf{T}}$.

**(2)** The matrix algebra is isomorphic to its opposite, $M_n(k)^{\mathrm{op}} \cong M_n(k)$, by the transpose; the isomorphism is an anti-automorphism of $M_n(k)$ of order two, hence an involution, and it is the canonical example of *Involutive Bilinear Algebras*.

**(3)** For a group $G$, the inversion $g \mapsto g^{-1}$ is an isomorphism $k[G]^{\mathrm{op}} \cong k[G]$, because it reverses products; the group algebra is therefore isomorphic to its opposite for every group.

**(4)** For a quiver $Q$, the reversal of the arrows is an isomorphism $kQ^{\mathrm{op}} \cong kQ^{\mathrm{rev}}$, where $kQ^{\mathrm{rev}}$ is the path algebra of the reversed quiver; it is an isomorphism onto $kQ$ itself exactly when the quiver is isomorphic to its reversal, which is the subject of *Involutions of a Path Algebra*.

*Proof.* (1) and (2): the transpose reverses the order of a product, $(XY)^{\mathsf{T}} = Y^{\mathsf{T}}X^{\mathsf{T}}$, and has order two, so it is an anti-automorphism of order two; the identification of matrices with endomorphisms is *The Operators on an Algebra*. (3) $(gh)^{-1} = h^{-1}g^{-1}$ and $(g^{-1})^{-1} = g$. (4) A path is a word in the arrows and its reversal is the word in the reversed arrows, and concatenation is reversed; the path algebra is that of *Quiver Representations and Representation Type*, and the reversal construction is developed in *Involutions of a Path Algebra*.

The list is the reason the opposite algebra is invisible in the commutative examples and in the matrix algebra: the transpose, the inversion and the arrow reversal are the anti-isomorphisms that identify each of these algebras with its opposite. In each case the anti-isomorphism has order two and is an involution, and it is the map that the rest of the category studies.

## Anti-Isomorphisms

### Definition and Calculus

**Definition.** Let $A$ and $B$ be $k$-algebras. An **anti-homomorphism** is a $k$-linear map $f : A \to B$ with

$$
f(ab) = f(b)f(a) \quad \text{for all } a, b \in A,
$$

an **anti-isomorphism** is a bijective anti-homomorphism, and an **anti-automorphism** is an anti-isomorphism $A \to A$. The set of anti-homomorphisms is written $\operatorname{Anti}(A,B)$ and the set of anti-isomorphisms $\operatorname{AntiIso}(A,B)$.

**Proposition.** Composition of maps gives the following table: the composite of two anti-homomorphisms is a homomorphism; the composite of a homomorphism with an anti-homomorphism, in either order, is an anti-homomorphism; and the composite of two anti-isomorphisms is an isomorphism. In particular $\operatorname{Anti}(A,A)$ is closed under composition, and it is a monoid whose square lies in the endomorphism monoid of $A$.

*Proof.* If $f$ and $g$ both reverse products, then $f(g(ab)) = f(g(b)g(a)) = f(g(a))f(g(b))$, so the composite preserves products; if exactly one reverses, the composite reverses; bijectivity is preserved by composition.

**Theorem (the dictionary).** For $k$-algebras $A$ and $B$ there is a bijection

$$
\operatorname{Anti}(A, B) \longrightarrow \operatorname{Hom}_k(A, B^{\mathrm{op}}), \qquad f \longmapsto \iota_B \circ f,
$$

and it restricts to a bijection $\operatorname{AntiIso}(A,B) \to \operatorname{Iso}_k(A, B^{\mathrm{op}})$. Under the dictionary the anti-automorphisms of $A$ correspond to the isomorphisms $A \to A^{\mathrm{op}}$, and the involutions of $A$ to those isomorphisms of *Involutive Bilinear Algebras* whose square is the identity.

*Proof.* The composite $\iota_B f$ preserves products, because $f$ reverses them and $\iota_B$ reverses them back; the correspondence is inverted by $\rho \mapsto \iota_B \rho$, since $\iota_B^2 = \mathrm{id}$. The statements about anti-automorphisms and involutions are the dictionary read with $B = A$.

The dictionary is the reason anti-isomorphisms need no separate theory: an anti-isomorphism onto $B$ is an isomorphism onto the opposite of $B$, and everything about homomorphisms applies to it through the mirror. In particular the set $\operatorname{AntiIso}(A,B)$ is nonempty exactly when $A \cong B^{\mathrm{op}}$, and the anti-automorphisms of $A$ are nonempty exactly when $A \cong A^{\mathrm{op}}$.

### The Coset of the Anti-Automorphisms

**Theorem.** Let $A$ carry an anti-automorphism $\rho_0$. Then the map $\alpha \mapsto \rho_0 \circ \alpha$ is a bijection

$$
\operatorname{Aut}_k(A) \longrightarrow \operatorname{Anti}(A,A), \qquad \alpha \longmapsto \rho_0 \alpha,
$$

and the anti-automorphisms of $A$ form a coset of the automorphism group in the monoid of all bijective $k$-linear maps of $A$. Two anti-automorphisms compose to an automorphism, and the products of an odd number of anti-automorphisms are anti-automorphisms.

*Proof.* For an automorphism $\alpha$ the composite $\rho_0\alpha$ reverses products, so the map lands in the anti-automorphisms; it is inverted by $\rho \mapsto \rho_0^{-1}\rho$, which is the composite of two anti-automorphisms and hence an automorphism, and the two composites are the identity by the associativity of composition and $\rho_0^{-1}\rho_0 = \mathrm{id} = \rho_0\rho_0^{-1}$. The statement that the anti-automorphisms form a coset is the definition of a coset under composition with the fixed element $\rho_0$.

**Remark.** When $A$ carries an involution the coset theorem is that of *Involutive Bilinear Algebras*, and the present article adds the case in which the fixed anti-automorphism $\rho_0$ is not of order two; the coset structure is the same and only the inverse map changes. The reason the coset is the right language is that the anti-automorphisms are never a group under composition, because the product of two of them leaves the coset.

## Involutions as Isomorphisms to the Opposite

### The Correspondence

**Definition.** An **involution** of $A$ is an isomorphism $\sigma : A \to A^{\mathrm{op}}$ with $\sigma^2 = \mathrm{id}$, equivalently a $k$-linear map with $\sigma(ab) = \sigma(b)\sigma(a)$, $\sigma(1) = 1$ and $\sigma \circ \sigma = \mathrm{id}$.

The definition is the one of *Involutive Bilinear Algebras*, where the involution, its symmetric and skew elements, the Lie algebra of the skew elements and the Jordan algebra of the symmetric ones are developed; the present article records only the place of the involution in the calculus of the opposite algebra.

**Proposition.** A $k$-linear map $\sigma : A \to A$ is an involution exactly when $\iota_A \circ \sigma : A \to A^{\mathrm{op}}$ is an isomorphism of algebras and $\sigma \circ \sigma = \mathrm{id}_A$. Under the dictionary the involutions of $A$ correspond bijectively to the anti-automorphisms of $A$ of order two, that is, to the elements of order two in the coset $\operatorname{Anti}(A,A)$.

*Proof.* The composite $\iota_A\sigma$ preserves products, because $\sigma$ reverses them and $\iota_A$ reverses them back, so $\sigma$ is an anti-homomorphism exactly when $\iota_A\sigma$ is a homomorphism; $\sigma$ is bijective exactly when $\iota_A\sigma$ is, and the condition $\sigma^2 = \mathrm{id}$ is the order-two condition on $\sigma$ itself. The final statement is the dictionary read with $B = A$.

**Corollary.** An algebra carries an anti-automorphism exactly when it is isomorphic to its opposite, and it carries an involution exactly when there is an isomorphism $\rho : A \to A^{\mathrm{op}}$ whose corresponding anti-automorphism has order two. An algebra with no anti-automorphism has no involution, and an algebra with an anti-automorphism of infinite order need not have an involution.

**Example.** On $M_n(k)$ the transpose is an involution. On $k[G]$ the inversion $g \mapsto g^{-1}$ extends to an anti-automorphism, and it is an involution exactly when every element of $G$ has order dividing two; otherwise it is an anti-automorphism of infinite order, and the group algebra may or may not carry an involution of order two.

## The Centre, the Units and the Ideals of the Opposite

**Proposition.** The centre, the group of units, the radical and the lattice of two-sided ideals of $A^{\mathrm{op}}$ are those of $A$; the simple quotients of $A^{\mathrm{op}}$ are the opposites of the simple quotients of $A$, and $A$ is simple if and only if $A^{\mathrm{op}}$ is.

*Proof.* The centre and the ideals were settled above; the units form the opposite group. A two-sided ideal $I$ is maximal exactly when $A/I$ is simple, and $(A/I)^{\mathrm{op}} = A^{\mathrm{op}}/I$; a ring is simple exactly when its opposite is, because the lattice of two-sided ideals is the same.

**Corollary (central simple algebras).** If $A$ is central simple over $k$, then so is $A^{\mathrm{op}}$, and the two are related by the Brauer group: the class of $A^{\mathrm{op}}$ is the inverse of the class of $A$ in $\operatorname{Br}(k)$, as in *Central Simple Algebras and the Brauer Group*. In particular $A \cong A^{\mathrm{op}}$ for every central simple algebra, and the isomorphism can be chosen of order two when $A$ is a matrix algebra.

The corollary is the reason the opposite algebra is a construction of the theory and not a separate family: over a field every central simple algebra is anti-isomorphic to itself, and the anti-isomorphism is what the transpose realises for the matrix algebra.

## Summary

The **opposite algebra** $A^{\mathrm{op}}$ is $A$ with the product reversed, $a^{\mathrm{op}}b^{\mathrm{op}} = (ba)^{\mathrm{op}}$, the opposite map $\iota_A : A \to A^{\mathrm{op}}$ being an anti-isomorphism; $(A^{\mathrm{op}})^{\mathrm{op}} = A$, $A^{\mathrm{op}}$ has the same centre, unit, units, radical and lattice of two-sided ideals as $A$, and $A^{\mathrm{op}} = A$ exactly when $A$ is commutative. The construction is functorial, it commutes with the tensor product by the swap, $(A \otimes B)^{\mathrm{op}} \cong A^{\mathrm{op}} \otimes B^{\mathrm{op}}$, and it is realised by the transpose for $\operatorname{End}_k(V)$ and for $M_n(k)$, by the inversion for a group algebra, and by the arrow reversal for a path algebra.

An **anti-homomorphism** $f : A \to B$ satisfies $f(ab) = f(b)f(a)$; the composite of two anti-maps is a map, and the dictionary $f \mapsto \iota_B f$ is a bijection $\operatorname{Anti}(A,B) \cong \operatorname{Hom}_k(A,B^{\mathrm{op}})$ restricting to $\operatorname{AntiIso}(A,B) \cong \operatorname{Iso}_k(A,B^{\mathrm{op}})$. The anti-automorphisms of $A$ form the coset $\rho_0\operatorname{Aut}_k(A)$ for any fixed anti-automorphism $\rho_0$, and they are a group only when empty or when $A$ is commutative. An **involution** is an isomorphism $\sigma : A \to A^{\mathrm{op}}$ of order two, that is an anti-automorphism of order two; the involutions, their symmetric and skew elements and the Lie and Jordan structures they carry are the subject of *Involutive Bilinear Algebras*, the involutions of the tensor algebra, the free algebra, the graded algebras and the path algebra are the subject of *Involutions of the Tensor Algebra*, *Involutions of a Free Algebra*, *Involutive Graded Algebras* and *Involutions of a Path Algebra*, and the adjoints built from an involution are the subject of the group `- * Operator Theory` of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A, B$ | unital associative $k$-algebras |
| $A^{\mathrm{op}}$ | the opposite algebra, product $a \cdot b = ba$ |
| $\iota_A : A \to A^{\mathrm{op}}$ | the opposite map, an anti-isomorphism |
| $\operatorname{Anti}(A,B)$ | the anti-homomorphisms $A \to B$ |
| $\operatorname{AntiIso}(A,B)$ | the anti-isomorphisms $A \to B$ |
| $\operatorname{Anti}(A,A)$ | the anti-automorphisms, a coset of $\operatorname{Aut}_k(A)$ |
| $\sigma : A \to A^{\mathrm{op}}$ | an involution, an isomorphism of order two |
| $M_n(k)^{\mathrm{op}} \cong M_n(k)$ | the transpose |
| $k[G]^{\mathrm{op}} \cong k[G]$ | the inversion |
| $kQ^{\mathrm{op}} \cong kQ^{\mathrm{rev}}$ | the reversal of the arrows |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the opposite algebra, the anti-isomorphisms and the standard instances.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the opposite ring and the anti-automorphisms of a simple algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions as isomorphisms to the opposite and the coset of the anti-automorphisms.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the opposite algebra and the passage from right to left modules.
