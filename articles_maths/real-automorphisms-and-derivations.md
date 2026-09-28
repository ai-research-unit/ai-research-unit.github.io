
# __Real Automorphisms and Derivations__

## Introduction

The real algebra $\mathbb{R}$ carries two standard invariants of its algebra structure: the group of algebra **automorphisms** and the Lie space of **derivations**. Both depend on the ground field, so the two views are kept separate and the field is named at each step. The real case is the degenerate base of the family: the automorphism group is trivial over every natural field of definition, and the derivation space vanishes. These are the smallest possible values, and their smallness is a mathematical statement about the complete ordered field rather than an omission.

The conventions are those of *Real Algebra*: basis $e_0 = 1$, a general element $x = x e_0$, the sole involution the identity, norm $N(x) = x\,x = x^2$. The comparison throughout is with the complex algebra $\mathbb{C}$, for which $\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) = \{\operatorname{id}, \bar{\cdot}\} \cong \mathbb{Z}/2$ and $\operatorname{Der}_{\mathbb{R}}(\mathbb{C}) = 0$, and with the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, for which $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C})$ and $\operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathrm{SL}(2,\mathbb{C})$; the present article is the one-dimensional account of the same two invariants.

No physics is invoked and no new results are claimed. Everything below is standard structure theory of the field $\mathbb{R}$, together with two standard facts of its model theory: that the order is definable from the field operations, and that $\mathbb{R}$ is o-minimal.

## Standing Facts: The Field and the Prime Field

The automorphism group and the derivation space of $\mathbb{R}$ are governed by three structural facts, recorded here and used throughout.

**No ideals.** Every nonzero element of $\mathbb{R}$ is invertible, so the only two-sided ideals of $\mathbb{R}$ are $0$ and $\mathbb{R}$: the algebra is a **field**, in particular a division algebra with no proper nonzero ideal. The ideal lattice is the two-point lattice $\{0, \mathbb{R}\}$, the smallest possible.

**The centre.** The centre of $\mathbb{R}$ is $\mathbb{R}$ itself, since the algebra is commutative:

$$
Z(\mathbb{R}) = \{x \in \mathbb{R} : xy = yx \ \text{for all} \ y\} = \mathbb{R}.
$$

Hence, over the ground field $\mathbb{R}$, the algebra is **central simple** — simple, finite-dimensional, with centre exactly the ground field. This is exactly the distinction that holds for $\mathbb{B}$ over $\mathbb{C}$: $\mathbb{B}$ is central simple over $\mathbb{C}$ and merely simple over $\mathbb{R}$. The two algebras differ not in that distinction but in what the invariant groups turn out to be.

**The prime field.** The image of $\mathbb{Q}$ in $\mathbb{R}$ under $q \mapsto q e_0$ is the **prime field**, the smallest subfield, and it is the fixed field of every automorphism and the zero set of every derivation. It is the field-theoretic analogue of the real subspace $\mathbb{R}_{\mathbb{R}}$ of *Real Algebra*, which is the whole of $\mathbb{R}$ here; the relevant substructure of $\mathbb{R}$ is not a proper subspace but the prime field, and it is the suspension of the Galois theory of the one-dimensional case.

## Automorphisms over $\mathbb{R}$

Throughout this section the ground field is $\mathbb{R}$.

**Definition.** An **$\mathbb{R}$-algebra automorphism** of $\mathbb{R}$ is a bijective $\mathbb{R}$-linear map $\sigma : \mathbb{R} \to \mathbb{R}$ with $\sigma(xy) = \sigma(x)\sigma(y)$ and $\sigma(e_0) = e_0$. These maps form a group under composition, written $\operatorname{Aut}_{\mathbb{R}}(\mathbb{R})$.

**Determination by the identity.** An $\mathbb{R}$-algebra automorphism fixes $e_0 = 1$ by definition and is $\mathbb{R}$-linear, so it fixes every element of the form $x e_0$ with $x \in \mathbb{R}$. Since $\mathbb{R}$ is one-dimensional as a vector space over itself and is spanned over $\mathbb{R}$ by the single vector $e_0$, fixing $e_0$ forces $\sigma = \operatorname{id}$.

**Theorem.** $\operatorname{Aut}_{\mathbb{R}}(\mathbb{R}) = \{\operatorname{id}\}$, the trivial group.

**Proof.** By the display above, $\sigma(x e_0) = x\sigma(e_0) = x e_0$ for every $x$, so $\sigma$ is the identity.

The result is the exact analogue of Skolem–Noether for a one-dimensional central simple algebra. In the biquaternion case, by contrast, the central simple algebra is $M_2(\mathbb{C})$, whose automorphisms are the inner ones and form $PGL(2,\mathbb{C})$ of dimension $3$; in the complex case the $\mathbb{R}$-automorphism group is $\mathbb{Z}/2$. Here the algebra is the ground field itself, the group of units modulo scalars is $GL_1(\mathbb{R})/\mathbb{R}^\times = 1$, and the automorphism group is trivial.

## Automorphisms of the Field and of the Ordered Field

The triviality of $\operatorname{Aut}_{\mathbb{R}}(\mathbb{R})$ is not an artefact of the ground field: it persists when automorphisms are required only to preserve the field or the order.

**Theorem (field automorphisms).** Every field automorphism of $\mathbb{R}$ is the identity.

**Proof.** Let $\sigma$ be a field automorphism. It fixes the prime field $\mathbb{Q}$ pointwise, because it fixes $1$ and hence every integer and every rational. It preserves squares, so $x > 0$ implies $x = y^2$ for some $y \neq 0$ and $\sigma(x) = \sigma(y)^2 > 0$; hence $\sigma$ is **order-preserving**, $x < y \Rightarrow \sigma(x) < \sigma(y)$. An order-preserving bijection of $\mathbb{R}$ that fixes $\mathbb{Q}$ is the identity: given $x$ and any rationals $q < x < r$ one has $q = \sigma(q) < \sigma(x) < \sigma(r) = r$, and since the rationals are dense and $x$ is the supremum of the rationals below it, $\sigma(x) = x$.

**Theorem (ordered-field automorphisms).** Every automorphism of $\mathbb{R}$ as an ordered field is the identity, and $\operatorname{Aut}(\mathbb{R})$ is the same trivial group whether $\mathbb{R}$ is regarded as a field, as an ordered field, or as an $\mathbb{R}$-algebra.

**Proof.** An ordered-field automorphism is in particular a field automorphism, so it is the identity by the previous theorem; conversely the identity preserves the order.

**The order is definable.** The reason the three automorphism groups coincide is a definability fact rather than a statement about the order axiom by axiom: in the language of fields the order is already present, because

$$
x \leq y \iff \exists z \ (z^2 = y - x),
$$

since a real number is a square exactly when it is non-negative. The order is therefore **definable** from the field operations alone, with no parameters, and every field automorphism is automatically an order automorphism. This is the model-theoretic mechanism that forces the rigidity of $\mathbb{R}$: the order adds no structure to the field, it is recoverable from it, and so it restricts the automorphisms no further.

**The relation to the real closed structure.** The field $\mathbb{R}$ is **real closed**: it admits no ordering other than its own, it has no proper ordered algebraic extension, and every odd-degree polynomial over it has a root. The definability of the order is a consequence of real closedness, and it is the form of it that concerns the automorphism group.

## Derivations

**Definition.** An **$\mathbb{R}$-linear derivation** of $\mathbb{R}$ is an $\mathbb{R}$-linear map $D : \mathbb{R} \to \mathbb{R}$ with

$$
D(xy) = D(x)\,y + x\,D(y) \qquad (x, y \in \mathbb{R}).
$$

The set of such maps is a real vector space, written $\operatorname{Der}_{\mathbb{R}}(\mathbb{R})$, carrying the commutator bracket and hence a Lie algebra structure.

**Every derivation vanishes on the base field.** Every derivation satisfies $D(e_0) = 0$, since $D(e_0) = D(e_0 e_0) = 2D(e_0)$ in characteristic not $2$, and hence $D(q e_0) = 0$ for all $q \in \mathbb{Q}$.

**Theorem.** $\operatorname{Der}_{\mathbb{R}}(\mathbb{R}) = 0$.

**Proof.** A derivation $D$ is $\mathbb{R}$-linear and $\mathbb{R} = \mathbb{R} e_0$, so $D$ is determined by the single value $D(e_0)$. By $\mathbb{R}$-linearity and the derivation rule,

$$
D(x) = D(x\,e_0) = x\,D(e_0) + D(x)\,e_0 = x\,D(e_0) + D(x),
$$

so $x D(e_0) = 0$ for all $x$, whence $D(e_0) = 0$; therefore $D = 0$. Equivalently, $D$ is $\mathbb{R}$-linear and $D(1) = 0$, so $D(x) = x D(1) = 0$ for every $x$.

**Vanishing of the inner derivations.** For a commutative algebra every inner derivation vanishes:

$$
\operatorname{ad}_x(y) = xy - yx = 0 \qquad (x, y \in \mathbb{R}),
$$

so the kernel of $\operatorname{ad} : \mathbb{R} \to \operatorname{Der}_{\mathbb{R}}(\mathbb{R})$ is all of $\mathbb{R}$, and the map itself is the zero map. In the biquaternion case $\operatorname{ad} : \mathbb{B} \to \operatorname{Der}_{\mathbb{C}}(\mathbb{B})$ has kernel the centre and induces $\operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathbb{B}/\mathbb{C}_{\mathbb{B}} \cong \mathrm{SL}(2,\mathbb{C})$; here the source and the target both collapse to the commutativity of the field. The complex case is the same one dimension up: its derivation space vanishes over both ground fields, and its inner derivations vanish identically.

**Dimension.** $\dim_{\mathbb{R}} \operatorname{Der}_{\mathbb{R}}(\mathbb{R}) = 0$.

## The Lie Algebra of the Trivial Group

The derivations of an algebra are the Lie algebra of its automorphism group. For $\mathbb{R}$ this consistency is visible on both sides.

The group $\operatorname{Aut}(\mathbb{R}) = 1$ is discrete; its identity component is the trivial group, and the Lie algebra of a discrete group is $0$, matching $\operatorname{Der}(\mathbb{R}) = 0$. Thus the identity

$$
\operatorname{Lie} \operatorname{Aut}(\mathbb{R}) = \operatorname{Der}(\mathbb{R}) = 0
$$

holds, in the degenerate sense that both sides are the zero space and the group has trivial identity component. In the biquaternion case the corresponding identity is $\operatorname{Lie}\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) = \operatorname{Der}_{\mathbb{C}}(\mathbb{B}) = \mathrm{SL}(2,\mathbb{C})$, of dimension $3$; in the complex case it is $\operatorname{Lie}\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) = \operatorname{Der}_{\mathbb{R}}(\mathbb{C}) = 0$, with the group $\mathbb{Z}/2$ finite. The real case is the same identity with the group reduced to the trivial group.

## The Relation to the Galois Theory and the Model Theory

**Galois theory.** The automorphism group computed above is the Galois group of the extension $\mathbb{R}/\mathbb{R}$, namely the trivial group. The extension that carries the nontrivial Galois theory of the line is not $\mathbb{R}$ over itself but the quadratic extension $\mathbb{C}/\mathbb{R}$, with

$$
\operatorname{Gal}(\mathbb{C}/\mathbb{R}) = \operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) \cong \mathbb{Z}/2,
$$

generated by complex conjugation. Because $\mathbb{R}$ is real closed, $\mathbb{R}(i) = \mathbb{C}$ is algebraically closed, so $\mathbb{C}$ is the algebraic closure of $\mathbb{R}$ and the absolute Galois group of $\mathbb{R}$ is the same $\mathbb{Z}/2$. The triviality of $\operatorname{Aut}(\mathbb{R})$ is thus the statement that $\mathbb{R}$ is a **rigid** field: it is its own prime field's completion, and it has no symmetry beyond the identity. The field-theoretic development is the subject of the companion article on the Galois theory of $\mathbb{C}/\mathbb{R}$; the present article records the automorphism group as an algebra invariant and stops at that boundary.

**Model theory.** The definability of the order makes $\mathbb{R}$ an **o-minimal** structure: every subset of $\mathbb{R}$ definable with parameters in the field language is a finite union of points and intervals. This is the tameness property developed in the companion article *O-Minimality*; here it is recorded only for the statement it makes about the invariants of this article. A model-theoretic automorphism of $\mathbb{R}$ is a field automorphism, hence the identity, so the structure is rigid; and the rigidity is a consequence of the order being definable, not of the order being primitive. The theory of real closed fields is complete and decidable (Tarski), and it is model complete; the field $\mathbb{R}$ is its unique model up to isomorphism among the complete ordered fields.

**The boundary between the two articles.** This article owns $\operatorname{Aut}$ and $\operatorname{Der}$ as algebra invariants of $\mathbb{R}$; the companion article *O-Minimality* owns definability, cell decomposition and the tameness of definable sets. The order's definability is stated here only in its automorphism-forcing role, and the model theory of definable sets is left to that article.

## Worked Examples

**The automorphism group is trivial.** Suppose $\sigma$ is an $\mathbb{R}$-algebra automorphism and $x \in \mathbb{R}$. Since $\sigma$ is $\mathbb{R}$-linear and $\sigma(1) = 1$, $\sigma(x) = \sigma(x\cdot 1) = x\,\sigma(1) = x$. For instance $\sigma(1) = 1$ and $\sigma(\tfrac{3}{4}) = \tfrac{3}{4}$; there is no other value an automorphism can assign, because the value on $1$ has already determined it.

**A field automorphism fixes the sign.** A field automorphism $\sigma$ preserves squares, so a positive number stays positive: $\sigma(4) = \sigma(2^2) = \sigma(2)^2 = 4 > 0$ and $\sigma(-1) = -1$. Hence a sign can never be moved by an automorphism, which is the concrete content of the order-preservation in the proof.

**No nonzero derivation.** Suppose $D$ is an $\mathbb{R}$-linear derivation with $D(1) = c$. Applying the derivation rule to $1 = 1\cdot 1$,

$$
c = D(1) = D(1\cdot 1) = D(1)\cdot 1 + 1\cdot D(1) = 2c \implies c = 0,
$$

the last step in characteristic $0$; hence $D(x) = xD(1) = 0$ for all $x$ by $\mathbb{R}$-linearity, and $D = 0$. There is no derivation of $\mathbb{R}$ over $\mathbb{R}$.

**The inner derivations.** For every $x \in \mathbb{R}$, $\operatorname{ad}_x = 0$; for instance with $x = -\tfrac{3}{4}$ and $y = \tfrac{7}{2}$,

$$
[x, y] = xy - yx = -\tfrac{21}{8} - \bigl(-\tfrac{21}{8}\bigr) = 0,
$$

the two terms being equal by commutativity.

## Summary

The two invariants are the following; the field is stated explicitly in every entry.

| Structure | Value over $\mathbb{R}$ | Value over the other fields |
|---|---|---|
| Algebra | $\mathbb{R}$, real dimension $1$ | $\mathbb{C}$ real dimension $2$; $\mathbb{B}$ complex dimension $4$ |
| Ideals | $\{0\}$ and $\mathbb{R}$ only | the same for $\mathbb{C}$; $\{0\}$ and $\mathbb{B}$ for $\mathbb{B}$ |
| Centre | $\mathbb{R}$, dimension $1$ | $\mathbb{C}$ for $\mathbb{C}$; $\mathbb{C}_{\mathbb{B}}$ for $\mathbb{B}$ |
| Automorphism group | $\{\operatorname{id}\}$, trivial | $\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) \cong \mathbb{Z}/2$; $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) = PGL(2,\mathbb{C})$ |
| Derivation space | $\operatorname{Der}_{\mathbb{R}}(\mathbb{R}) = 0$ | $\operatorname{Der}_{\mathbb{R}}(\mathbb{C}) = 0$; $\operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathrm{SL}(2,\mathbb{C})$ |

In summary: the automorphism group of $\mathbb{R}$ is trivial as an $\mathbb{R}$-algebra, as a field and as an ordered field, and the order adds no restriction because it is definable from the field operations, $x \leq y \iff \exists z\,(z^2 = y-x)$. The derivation space vanishes over $\mathbb{R}$, since the single basis element $e_0$ is fixed and the derivation rule forces $D(e_0) = 0$, and every inner derivation vanishes because the algebra is commutative. In the complex algebra the automorphism group is $\mathbb{Z}/2$ and the derivation space is zero; in the biquaternion algebra the two invariants are $PGL(2,\mathbb{C})$ and $\mathrm{SL}(2,\mathbb{C})$, of dimension $3$. The real field is the case in which both invariants collapse to the trivial group and the zero space, and the surviving structure is the prime field $\mathbb{Q}$ together with the order that is definable from the field.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, basis $e_0 = 1$, the complete ordered field |
| $x = x e_0$ | a real number |
| $\operatorname{id}$ | the identity, the sole automorphism of $\mathbb{R}$ |
| $\operatorname{Aut}_{\mathbb{R}}(\mathbb{R}) = \{\operatorname{id}\}$ | automorphisms over $\mathbb{R}$ |
| $\operatorname{Aut}(\mathbb{R}) = \{\operatorname{id}\}$ | field and ordered-field automorphisms |
| $\operatorname{Der}_{\mathbb{R}}(\mathbb{R}) = 0$ | derivations over $\mathbb{R}$ |
| $\operatorname{ad}_x(y) = [x,y] = xy - yx$ | inner derivation, identically zero |
| $\mathbb{Q}$ | the prime field, fixed by every automorphism and killed by every derivation |
| $x \leq y \iff \exists z\,(z^2 = y-x)$ | definability of the order from the field operations |
| $\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) \cong \mathbb{Z}/2$ | the Galois group of the quadratic extension |

## Further Reading

- Serge Lang, *Algebra*, 3rd edition (Addison–Wesley, 1993), for field automorphisms, the prime field and ordered-field structure.
- Nathan Jacobson, *Basic Algebra I*, 2nd edition (Dover, 2009), for real closed fields, their rigidity and the Galois theory of $\mathbb{C}/\mathbb{R}$.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for derivations, inner derivations and the Lie algebra of the automorphism group.
- David Marker, *Model Theory: An Introduction*, Graduate Texts in Mathematics 217 (Springer, 2002), for the definability of the order in real closed fields and the completeness of the theory RCF.
- Lou van den Dries, *Tame Topology and O-Minimal Structures* (Cambridge University Press, 1998), for o-minimality and the tameness of the real field.
- Alfred Tarski, *A Decision Method for Elementary Algebra and Geometry*, 2nd edition (University of California Press, 1951), for the decidability of the theory of real closed fields.
