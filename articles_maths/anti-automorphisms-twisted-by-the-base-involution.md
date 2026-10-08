# __Anti-Automorphisms Twisted by the Base Involution__

## Introduction

An anti-automorphism of an algebra reverses the order of a product. When the algebra is defined over a ring carrying an involution $\varsigma$, a second kind of map appears: the anti-automorphisms that are $\varsigma$-semilinear, $f(\lambda x) = \varsigma(\lambda)f(x)$, the same twist that the sesqualgebra product carries in its second variable. This article reads the calculus of those maps at any order. Two twisted anti-automorphisms compose to a linear automorphism; a twisted one and a linear one compose to a twisted one; the twist is multiplicative under composition; and the two bits of the twist and of the orientation place every semilinear map of the algebra in one of four classes, which form the Klein group over the linear automorphisms. The order of a twisted map is the second subject: its $n$-th power has twist $\varsigma^{n}$, so a twisted map of finite order has even order, and the order-two case is the involutions of *The Involutions of a Sesqualgebra*.

The article is the companion of *The Involutions of a Sesqualgebra*, which keeps only the order-two case; here the maps are taken at any order and the parity of that order is the point. The coset of the anti-automorphisms is *Opposite Algebras and Anti-Isomorphisms*, §*The Coset of the Anti-Automorphisms*, for the layer $\varsigma = \mathrm{id}$; the present article adds the twist, which turns the two classes of that theorem into four and the quotient $\mathbb{Z}/2$ into the Klein group. The relation to the involutions of a central simple algebra, the two kinds and the inner reduction, is *Involutions of a Central Simple Algebra*.

The setting is that of *Sesqualgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and $A$ is an associative unital $R$-algebra with a $\varsigma$-semilinear involution $*$, the datum. The datum is itself one of the maps studied here, of order two. The inner automorphisms of a unitary element and the unitary group are *Units and the Unitary Elements*; the linear automorphisms of a central simple algebra and the inner ones are *Central Simple Algebras and the Brauer Group*; the opposite algebra is *Opposite Algebras and Anti-Isomorphisms*; and the case $\varsigma = \mathrm{id}$, where the twist disappears, is *Algebras: A General Introduction*.

---

## The Twisted Maps

### The Twisted Anti-Automorphisms

**Definition.** A **$\varsigma$-twisted anti-automorphism** of $A$ is a bijective additive map $f : A \to A$ with

$$
f(\lambda x) = \varsigma(\lambda) f(x) , \qquad f(xy) = f(y)f(x) .
$$

The set of them is written $\operatorname{Tw}_{\varsigma}(A)$, or $\operatorname{Tw}(A,A^{\mathrm{op}})$ when it is read as the isomorphisms to the opposite algebra. The **twist** of $f$ is the involution $\varsigma$ that appears in the first rule.

**Lemma (the twist is unique).** Let $R$ be a domain and $A$ a nonzero unital $R$-algebra. A bijective map $f$ has at most one twist: if $f(\lambda x) = \varsigma(\lambda)f(x)$ and $f(\lambda x) = \varsigma'(\lambda)f(x)$ for all $\lambda \in R$, $x \in A$, then $\varsigma = \varsigma'$.

**Proof.** Subtracting, $(\varsigma(\lambda) - \varsigma'(\lambda))f(x) = 0$ for every $x$, and $f$ is onto, so $(\varsigma(\lambda) - \varsigma'(\lambda))A = 0$; taking $1 \in A$ and using that $R$ is a domain with $1 \neq 0$ gives $\varsigma(\lambda) = \varsigma'(\lambda)$ for every $\lambda$. $\square$

**Remark.** The datum $*$ is an element of $\operatorname{Tw}_{\varsigma}(A)$, of order two, so the set is not empty and every statement below has the datum as its base point. The definition is the one of the anti-automorphisms when $\varsigma = \mathrm{id}$, and $\operatorname{Tw}_{\mathrm{id}}(A)$ is the layer of *Opposite Algebras and Anti-Isomorphisms*, §*The Coset of the Anti-Automorphisms*.

### The Twisted Automorphisms

**Definition.** A **$\varsigma$-twisted automorphism** of $A$ is a bijective additive map $f : A \to A$ with

$$
f(\lambda x) = \varsigma(\lambda) f(x) , \qquad f(xy) = f(x)f(y) .
$$

The set of them is written $\operatorname{Aut}_{\varsigma}(A)$; the untwisted case is $\operatorname{Aut}_{R}(A) = \operatorname{Aut}_{\mathrm{id}}(A)$, the ordinary group of the $R$-linear automorphisms of $A$.

**Remark.** The twisted automorphisms are invisible in the treatment of the involutions, since an involution is anti-multiplicative by definition, and they are what the twist adds to the classical theory: an algebra over a ring with a nontrivial involution can carry a conjugate-linear automorphism, and for the complex matrix algebra the entrywise conjugation is one. A twisted automorphism is a bijection of $A$ that is not $R$-linear and nevertheless respects the multiplication, and it is the second of the two bits that the next section separates.

## The Calculus of the Twists

### The Multiplicativity of the Twist

**Theorem.** Let $f$ and $g$ be bijective semilinear maps of $A$ with twists $\varsigma_{f}$ and $\varsigma_{g}$. Then the composite $f \circ g$ has twist $\varsigma_{f} \circ \varsigma_{g}$, and the two orientations multiply as the rule

$$
(\text{anti}) \circ (\text{anti}) = \text{auto} , \qquad (\text{anti}) \circ (\text{auto}) = \text{anti} , \qquad (\text{auto}) \circ (\text{auto}) = \text{auto} .
$$

**Proof.** For the twist, $(f \circ g)(\lambda x) = f\bigl(\varsigma_{g}(\lambda)g(x)\bigr) = \varsigma_{f}\bigl(\varsigma_{g}(\lambda)\bigr)(f \circ g)(x)$. For the orientations, if $f$ and $g$ both reverse products then $(f \circ g)(xy) = f(g(y)g(x)) = f(g(x))f(g(y)) = (f \circ g)(x)(f \circ g)(y)$, so the composite is multiplicative; the other two cases are the same computation with one reversal. $\square$

**Corollary.** The product of two $\varsigma$-twisted anti-automorphisms is an $R$-linear automorphism, and a twisted anti-automorphism composed with a linear automorphism on either side is again a twisted anti-automorphism.

**Proof.** Two anti-automorphisms give an automorphism, and their twists multiply to $\varsigma^{2} = \mathrm{id}$, so the composite is $R$-linear. A linear automorphism has twist $\mathrm{id}$, so the twist of the composite is $\varsigma$ and the orientation is the one of the anti-automorphism. $\square$

**Remark.** The corollary is the reason the set of the twisted anti-automorphisms is a coset and not a group: the composite of two of its elements leaves the set, and only the composites with the linear automorphisms keep it. It is also the reason the datum composed with a unitary inner automorphism stays in the set, which is the family $\sigma_{u} = \alpha_{u} \circ *$ of *The Involutions of a Sesqualgebra*.

### The Four Classes and the Klein Group

**Theorem.** Let $R$ be a domain, let $A$ be a noncommutative unital $R$-algebra, and let the twist take values in $\{\mathrm{id},\varsigma\}$, so that the twist of a semilinear map is unique by the lemma above. Then the four sets

$$
\operatorname{Aut}_{R}(A) , \qquad \operatorname{Aut}_{\varsigma}(A) , \qquad \operatorname{Tw}_{\mathrm{id}}(A) , \qquad \operatorname{Tw}_{\varsigma}(A)
$$

form a group $P$ under composition, each of them is either empty or a coset of the linear automorphism group $\operatorname{Aut}_{R}(A)$, and the map that records the twist and the orientation,

$$
\psi : P \longrightarrow \mathbb{Z}/2 \times \mathbb{Z}/2 ,
$$

is a homomorphism with kernel $\operatorname{Aut}_{R}(A)$. When all four classes are nonempty, $\psi$ is onto and $P / \operatorname{Aut}_{R}(A) \cong \mathbb{Z}/2 \times \mathbb{Z}/2$, the Klein group.

**Proof.** The composition table of the twist and of the orientation is the theorem above, and the four sets are closed under it: with the twists in the group $\{\mathrm{id},\varsigma\} \cong \mathbb{Z}/2$ and the orientations in $\{\text{auto},\text{anti}\} \cong \mathbb{Z}/2$, the product of two elements whose twist and orientation lie in the respective classes lies in the class of the product of the labels. The inverse of an element of a class has the same twist, since $\varsigma = \varsigma^{-1}$, and the same orientation, so each class is closed under inversion, and $P$ is a group. The kernel of $\psi$ is the class with twist $\mathrm{id}$ and orientation auto, that is $\operatorname{Aut}_{R}(A)$. If $f_{0}$ and $g_{0}$ are two elements of the same nonempty class then $f_{0}^{-1}g_{0}$ has twist $\mathrm{id}$ and orientation auto, so $g_{0} = f_{0}(f_{0}^{-1}g_{0})$ with $f_{0}^{-1}g_{0} \in \operatorname{Aut}_{R}(A)$, which exhibits the class as a coset. Surjectivity of $\psi$ is the nonemptiness of the four classes, and the quotient is then $\mathbb{Z}/2 \times \mathbb{Z}/2$. $\square$

**Remark.** The noncommutativity of $A$ is needed so that the orientation is a well-defined function: over a commutative algebra every anti-automorphism is an automorphism, the two orientations coincide, and the four classes collapse to one per twist, that is to two when $\varsigma \neq \mathrm{id}$ and to one when $\varsigma = \mathrm{id}$. For a noncommutative algebra the Klein group is genuine, and the matrix model realises it, as the worked case below shows. The theorem is the twisted refinement of *Opposite Algebras and Anti-Isomorphisms*, §*The Coset of the Anti-Automorphisms*: there the anti-automorphisms form a single coset of the automorphism group, here the twist doubles the coset and the quotient becomes the Klein group.

## The Order of a Twisted Map

### The Parity Theorem

**Theorem (the parity of the order).** Let $R$ be a domain, $A$ a nonzero unital $R$-algebra, $\varsigma \neq \mathrm{id}$ an involution of $R$, and $f$ a bijective map of $A$ that is semilinear with twist $\varsigma$ and multiplicative or anti-multiplicative. Then the $k$-th power $f^{k}$ has twist $\varsigma^{k}$, and if $f$ has finite order $n$ then $n$ is even. In particular $f$ is not the identity, and it has no order $3$, $5$, $7$, $\dots$

**Proof.** The twist is multiplicative under composition, so $f^{k}$ has twist $\varsigma^{k}$ by induction. If $f^{n} = \mathrm{id}$ then the identity has twist $\varsigma^{n}$; the identity is $R$-linear, so it has twist $\mathrm{id}$ as well, and the uniqueness of the twist gives $\varsigma^{n} = \mathrm{id}$. If $n$ were odd then $\varsigma^{n} = \varsigma \neq \mathrm{id}$, a contradiction. $\square$

**Remark.** The theorem is the exact sense in which the twist constrains the order: the twist is a homomorphism from the group generated by $f$ into $\mathbb{Z}/2$, so an element with a nontrivial image has even order, and a twisted map of odd order would have an image of odd order in $\mathbb{Z}/2$, which does not exist. The order-two case and the order-four case both occur, and the odd orders do not; the matrix worked case gives one map of each of the two admissible orders, and for its order-four map the powers $f$, $f^{2}$ and $f^{3}$ are all different from the identity.

### The Squares

**Corollary.** With the hypotheses of the parity theorem, $f^{2}$ is an $R$-linear automorphism, every even power of $f$ is $R$-linear, and every odd power has twist $\varsigma$ and the same orientation as $f$.

**Proof.** The twist of $f^{k}$ is $\varsigma^{k}$, which is $\mathrm{id}$ for $k$ even and $\varsigma$ for $k$ odd; the orientation is auto for $k$ even and that of $f$ for $k$ odd. $\square$

**Remark.** A twisted anti-automorphism is therefore a square root of the linear automorphism $f^{2}$, and the twisted maps are square roots of automorphisms. This is the structural reason the set of the twisted anti-automorphisms is governed by $\operatorname{Aut}_{R}(A)$: the squares of its elements are there, and the coset theorem of the next section makes the statement exact for the first powers.

## The Coset of the Twisted Anti-Automorphisms

### The Coset Theorem

**Theorem.** Let $\operatorname{Tw}_{\varsigma}(A)$ be nonempty and let $f_{0}$ be an element of it. Then the map $\sigma \mapsto f_{0}\sigma$ is a bijection

$$
\operatorname{Aut}_{R}(A) \longrightarrow \operatorname{Tw}_{\varsigma}(A) ,
$$

so that $\operatorname{Tw}_{\varsigma}(A) = f_{0}\operatorname{Aut}_{R}(A)$ is a right coset of the linear automorphism group; it is also the left coset $\operatorname{Aut}_{R}(A)f_{0}$, because $f_{0}\sigma f_{0}^{-1}$ is an $R$-linear automorphism for every $\sigma$.

**Proof.** For $\sigma \in \operatorname{Aut}_{R}(A)$ the composite $f_{0}\sigma$ is bijective, additive, $\varsigma$-semilinear and anti-multiplicative, so it lies in $\operatorname{Tw}_{\varsigma}(A)$; the map is injective because $f_{0}$ is, and it is surjective because $f \in \operatorname{Tw}_{\varsigma}(A)$ gives $f = f_{0}(f_{0}^{-1}f)$ with $f_{0}^{-1}f$ of twist $\mathrm{id}$ and orientation auto, that is in $\operatorname{Aut}_{R}(A)$. For the left coset, $f_{0}^{-1}$ has twist $\varsigma$ and orientation anti, so $f_{0}\sigma f_{0}^{-1}$ has twist $\varsigma \cdot \mathrm{id} \cdot \varsigma = \mathrm{id}$ and orientation auto, hence it is in $\operatorname{Aut}_{R}(A)$; this conjugation is the inner automorphism of the group $P$ induced by $f_{0}$, and it preserves the kernel $\operatorname{Aut}_{R}(A)$. $\square$

**Remark.** The theorem is the twisted form of the coset theorem of *Opposite Algebras and Anti-Isomorphisms*, §*The Coset of the Anti-Automorphisms*, which is the case $\varsigma = \mathrm{id}$; the twist adds the conjugation that relates the right coset to the left one, and it is what makes the set of the twisted anti-automorphisms a torsor and not only a coset. The coset is free and transitive, so two twisted anti-automorphisms differ by exactly one linear automorphism, and the parametrisation is the one used to compare them.

### The Reading as the Anti-Isomorphisms to the Opposite

**Proposition.** Let $A^{\mathrm{op}}$ be the opposite algebra of *Opposite Algebras and Anti-Isomorphisms*. Then $\operatorname{Tw}_{\varsigma}(A)$ is exactly the set of the $\varsigma$-semilinear isomorphisms $A \to A^{\mathrm{op}}$, and the coset theorem reads: the $\varsigma$-semilinear isomorphisms from $A$ to its opposite form a coset of the group $\operatorname{Aut}_{R}(A)$.

**Proof.** A bijective anti-multiplicative map $A \to A$ is a multiplicative map $A \to A^{\mathrm{op}}$, by the definition of the product of the opposite algebra; the additivity and the $\varsigma$-semilinearity are the same on the two sides. $\square$

**Remark.** The reading identifies the twisted anti-automorphisms with the isomorphisms of $A$ with its own opposite, and it makes the order-two case the statement that an involution is an isomorphism of $A$ with $A^{\mathrm{op}}$ whose composite with itself is the identity; that case is *The Involutions of a Sesqualgebra*. The proposition is the reason the symbols $\operatorname{Tw}(A,A^{\mathrm{op}})$ and $\operatorname{Tw}_{\varsigma}(A)$ name the same set.

## The Classical Case

### The Two Kinds

**Proposition.** Let $A$ be a central simple algebra over a field $F$ and let $f$ be an anti-automorphism of $A$ of order two. Then exactly one of the following holds: the restriction of $f$ to $F$ is the identity, in which case $f$ is $F$-linear and of the **first kind**; or the restriction of $f$ to $F$ is a nontrivial involution $\varsigma$, in which case $F$ is a quadratic extension of its fixed field $F^{\varsigma}$ and $f$ is $\varsigma$-semilinear and of the **second kind**. For an anti-automorphism of any order the restriction to the centre is an automorphism of $F$ of that same order, so the quadratic alternative is special to the order two.

**Proof.** An anti-automorphism carries the centre onto the centre, so the restriction $f|_{F}$ is a field automorphism of $F$, of order dividing the order of $f$. When $f$ has order two, $f|_{F}$ has order one or two. In the first case $f$ is $F$-linear and of the first kind. In the second case $\varsigma = f|_{F}$ is a nontrivial involution of $F$ and, by the quadratic-extension theorem of *Involutions of a Central Simple Algebra*, §*First and Second Kind*, its fixed field $F^{\varsigma}$ has index two in $F$, so $F$ is quadratic over $F^{\varsigma}$ and $f$ is $\varsigma$-semilinear. For an anti-automorphism of order $n$ the same argument gives $(f|_{F})^{n} = \mathrm{id}$, so $f|_{F}$ need not be an involution and the two alternatives do not exhaust the possibilities. $\square$

**Remark.** The two kinds are those of *Involutions of a Central Simple Algebra*, §*First and Second Kind*, and the second kind is exactly the layer of the present article: the twist $\varsigma$ is the restriction of the map to the centre, and the datum of the quadratic extension is what the $\varsigma$-twist adds to the algebra. For the first kind the twist is trivial and the theory is that of the coset of *Opposite Algebras and Anti-Isomorphisms*; for the second kind the parity theorem applies and the order is even or infinite.

### The Order-Two Case

**Proposition.** The $\varsigma$-twisted anti-automorphisms of order two are the involutions $\operatorname{Inv}(A)$ of *The Involutions of a Sesqualgebra*, and the datum $*$ is one of them.

**Proof.** An order-two $\varsigma$-twisted anti-automorphism is a $\varsigma$-semilinear anti-automorphism with $f^{2} = \mathrm{id}$, which is the definition of an element of $\operatorname{Inv}(A)$. $\square$

**Remark.** The order-two case is the case of the parity theorem that is always available: the twist forbids the odd orders and allows the even ones, and the first even order is two. The inner conjugates of the datum, $f = \alpha_{u} \circ *$ with $u$ unitary, are of order two exactly when $u^{2}$ is central, which is the criterion of *The Involutions of a Sesqualgebra*, §*The Family of a Unitary Element*; the linear counterpart, the inner reduction for two involutions of a central simple algebra, is *Involutions of a Central Simple Algebra*, §*Comparing Two Involutions*.

## Worked Cases

### The Matrix Algebra

Let $A = M_{n}(\mathbb{C})$ with $\varsigma$ the complex conjugation. Four maps realise the four classes. The **transpose** $x \mapsto x^{\mathsf{T}}$ is $R$-linear and reverses the product, so it lies in $\operatorname{Tw}_{\mathrm{id}}(A)$; the **conjugate transpose** $x \mapsto x^{*}$ reverses the product and is $\varsigma$-semilinear, so it lies in $\operatorname{Tw}_{\varsigma}(A)$ and it is the datum; the **entrywise conjugation** $x \mapsto \bar{x}$ respects the product and is $\varsigma$-semilinear, so it lies in $\operatorname{Aut}_{\varsigma}(A)$; and the inner automorphisms $x \mapsto uxu^{*}$ lie in $\operatorname{Aut}_{R}(A)$. The composite of the transpose and the conjugate transpose is the entrywise conjugation in either order,

$$
x^{\mathsf{T}*} = \bar{x} = x^{*\mathsf{T}} ,
$$

which is the concrete form of the composition rule, and the three involutions $x \mapsto x^{\mathsf{T}}$, $x \mapsto x^{*}$ and $x \mapsto \bar{x}$ generate the Klein group of the four classes. The algebra is noncommutative, so the four classes are distinct and the quotient of the theorem is $\mathbb{Z}/2 \times \mathbb{Z}/2$. For an example of the admissible order four, let $\zeta$ be a primitive eighth root of unity, let $w = \mathrm{diag}(\zeta, \zeta^{3})$, so that $w^{4} = -I$ is central while $w^{2}$ is not, and let $f = \alpha_{w} \circ *$; then $f^{2} = \alpha_{w^{2}}$ is not the identity and $f^{4} = \alpha_{w^{4}} = \mathrm{id}$, so $f$ has order four, and no odd power of $f$ is the identity, which is the parity theorem on the nose. The smallest cases are the order two of the datum and the order four of $f$, and the order three is impossible.

**Remark.** The computation of the order of $f$ uses the identity $\sigma_{u}^{2} = \alpha_{u^{2}}$ of *The Involutions of a Sesqualgebra*, §*The Family of a Unitary Element*, and it is the reason that identity is stated there in full: the parity theorem is visible on the matrix algebra through the square of the inner conjugates.

### The Field

Let $A = \mathbb{C}$ with $\varsigma = \mathrm{id}$, over $R = \mathbb{R}$. The anti-automorphisms of the field coincide with its automorphisms, since a field is commutative, so the orientation cannot separate anything; the twist is trivial as well, and the four classes collapse to a single one, the group $\{\mathrm{id}, \bar{\cdot}\}$ of the two $\mathbb{R}$-algebra automorphisms of $\mathbb{C}$. Let instead $A = \mathbb{C}$ over $R = \mathbb{C}$ with $\varsigma$ the conjugation. A semilinear map is determined on the scalars by $f(\lambda) = \varsigma(\lambda)f(1)$, and with $f(1) = 1$ this gives $f(\lambda) = \varsigma(\lambda)$ for every $\lambda$, so that $\operatorname{Aut}_{\varsigma}(A)$ and $\operatorname{Tw}_{\varsigma}(A)$ are both the singleton $\{\bar{\cdot}\}$, while $\operatorname{Aut}_{R}(A) = \operatorname{Tw}_{\mathrm{id}}(A) = \{\mathrm{id}\}$ because the field is commutative. Here the orientation is again unavailable and the twist is what separates: of the four classes only the two distinct twists survive, the class of the identity and the class of the conjugation. The two readings are the degenerations of the Klein group: over $\mathbb{R}$ the twist is trivial, so a single class remains and the orientation labels nothing; over $\mathbb{C}$ the twist is present but the orientation still labels nothing, so two classes remain and not four. Neither reading shows the four distinct classes, which require a noncommutative algebra.

## Summary

A $\varsigma$-twisted anti-automorphism is a bijective map with $f(\lambda x) = \varsigma(\lambda)f(x)$ and $f(xy) = f(y)f(x)$, and a twisted automorphism is the same map without the reversal in the second rule. The twist is unique over a domain and multiplicative under composition; two anti-automorphisms compose to a linear automorphism; and the twist and the orientation place the semilinear maps of a noncommutative algebra in four classes, which form a group with $\operatorname{Aut}_{R}(A)$ as the kernel of the pair of labels and the Klein group as the quotient when the four classes are nonempty.

The $k$-th power of a twisted map has twist $\varsigma^{k}$, so a twisted map of finite order has even order, and the even powers are linear while the odd powers are twisted; a twisted anti-automorphism is a square root of a linear automorphism. The twisted anti-automorphisms form a coset of $\operatorname{Aut}_{R}(A)$, the twisted form of the coset of *Opposite Algebras and Anti-Isomorphisms*, and they are the isomorphisms of $A$ with its opposite. For a central simple algebra the twist is the second kind, and the order-two case is the involutions of *The Involutions of a Sesqualgebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $f(\lambda x) = \varsigma(\lambda)f(x)$ | the $\varsigma$-semilinearity, the twist of $f$ |
| $f(xy) = f(y)f(x)$ | the reversal of the product, the anti-automorphism rule |
| $\operatorname{Tw}_{\varsigma}(A)$ | the $\varsigma$-twisted anti-automorphisms of $A$ |
| $\operatorname{Aut}_{\varsigma}(A)$ | the $\varsigma$-twisted automorphisms of $A$ |
| $\operatorname{Aut}_{R}(A)$ | the $R$-linear automorphisms, the untwisted class |
| $\varsigma_{f\circ g} = \varsigma_{f}\circ\varsigma_{g}$ | the multiplicativity of the twist |
| $(\text{anti})\circ(\text{anti}) = \text{auto}$ | the multiplication of the orientations |
| $\psi : P \to \mathbb{Z}/2 \times \mathbb{Z}/2$ | the twist and the orientation of a semilinear map |
| $P/\operatorname{Aut}_{R}(A) \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ | the Klein quotient of the four classes |
| $f^{k}$ has twist $\varsigma^{k}$ | the parity of the order |
| $\operatorname{Tw}_{\varsigma}(A) = f_{0}\operatorname{Aut}_{R}(A)$ | the coset of the twisted anti-automorphisms |
| $A^{\mathrm{op}}$ | the opposite algebra, the target of an anti-automorphism |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the semilinear maps, the twisted automorphisms and anti-automorphisms, and the case of the trivial involution.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the anti-automorphisms of a ring, the order of a twisted map and the Galois theory of the fixed rings.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the anti-automorphisms and the involutions as anti-automorphisms of order two.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the first and the second kind of an anti-automorphism of a central simple algebra and the inner reduction.
- Paul K. Draxl, *Skew Fields* (Cambridge University Press, 1983), for the anti-automorphisms of a division algebra and the quadratic extension of the centre that a second-kind map produces.
- The companion articles of this series: *Sesqualgebras*, *Algebras: A General Introduction*, *Opposite Algebras and Anti-Isomorphisms*, *Involutions of a Central Simple Algebra*, *Central Simple Algebras and the Brauer Group*, *Units and the Unitary Elements*, *The Involutions of a Sesqualgebra* and *Hermitian and Skew-Hermitian Elements*.
