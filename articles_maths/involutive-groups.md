# __Involutive Groups__

## Introduction

An **involution of a group** $G$ is an anti-automorphism of $G$ of order two: a bijection $\sigma : G \to G$ with

$$
\sigma(ab) = \sigma(b)\sigma(a) \qquad \text{for all } a, b \in G, \qquad \sigma \circ \sigma = \mathrm{id} .
$$

The notion presupposes no commutativity. Unlike a ring, a group always carries one such map: the **inversion** $\iota(g) = g^{-1}$, whose anti-multiplicativity is the identity $(ab)^{-1} = b^{-1}a^{-1}$, and which is the canonical isomorphism of $G$ with its opposite group. Every group is therefore isomorphic to its opposite group, and the question is not whether a group has an involution but which ones it has. What an involution carries is recorded by two sets, the elements it **fixes** and the elements it **inverts**; the first need not be a subgroup, the second always is, and the interplay of the two, together with the associated involutive automorphism $\sigma \iota$, organises the theory.

**Terminology.** In this article an **involution of a group** is a map of the kind above, and the article says **element of order two** for an element $x$ with $x^2 = e$. The clash is real: in much of the literature, and in several other articles of this corpus, the word *involution* means an element of order two, and an author who reads one meaning for the other will misread a definition rather than make a mistake of substance.

**Layout and boundaries.** The article has six sections: the involutions of a group and their relation to the automorphisms, the fixed and inverted sets, real elements and products of elements of order two, quotients, subgroups and products, the involutions that come from extensions, and the involutions that come from presentations. It stays inside the theory of groups of Part I and uses nothing from a later part. The vocabulary of subgroups, quotients, conjugacy and abelianisation is *Groups*; automorphism groups of structures are *Transformation Groups*; the semidirect product is *Generators, Presentations and Free Products*; the non-split extensions are *Group Cohomology*. The group case of the rings with involution is *Involutive Rings*, in *Rings and Fields*, and the comparison is drawn at the end: the anti-automorphism there is a genuine extra datum, here it is automatic, and the fixed set, the conjugate products and the ideal theory behave differently. The geometry that an order-two automorphism defines, and the spaces built from a fixed subgroup, are Part IV and are named once to mark the boundary. Throughout, $G$ is a group with unit $e$, $\sigma$ is an involution of $G$, $\iota$ is the inversion, $G^\sigma$ is the fixed set, and $\operatorname{Aut}(G)$ and $\operatorname{Inn}(G)$ are the automorphism and inner automorphism groups.

---

## Involutions of a Group

### Definition

**Definition.** An **involution of a group** $G$ is a bijection $\sigma : G \to G$ satisfying $\sigma(ab) = \sigma(b)\sigma(a)$ for all $a, b \in G$ and $\sigma^2 = \mathrm{id}$. An **involutive group** is a pair $(G, \sigma)$ consisting of a group and an involution of it.

**Remark (determination on generators).** An involution is determined by its values on a generating set, but the values alone do not tell a homomorphism from an anti-homomorphism: on a nonabelian group both exist with the same values on the generators and they differ on products. On the dihedral group $D_n = \langle r, s \rangle$ the assignment $r \mapsto r$, $s \mapsto s$ extended multiplicatively is the identity, while the same assignment extended anti-multiplicatively is the word-reversal involution, which sends $rs$ to $sr = r^{-1}s$. The two maps agree on every element represented by a palindrome, the powers of $r$ among them, and they differ already on the two-letter word $rs$, which the identity sends to $rs$ and the reversal to $sr = r^{-1}s$.

### The Opposite Group and Inversion

**Definition.** The **opposite group** $G^{\mathrm{op}}$ has the same underlying set as $G$ and the product $a \cdot^{\mathrm{op}} b = ba$.

An involution of $G$ is exactly an isomorphism $G \to G^{\mathrm{op}}$ of order two, and the inversion $\iota(g) = g^{-1}$ is such an isomorphism: $\iota(ab) = (ab)^{-1} = b^{-1}a^{-1} = \iota(a)\cdot^{\mathrm{op}}\iota(b)$. The map $\iota$ is an involution of $G$, and it exhibits the isomorphism $G \cong G^{\mathrm{op}}$ explicitly by a formula that needs no choice.

**Remark.** The contrast with rings is sharp. For a ring the existence of an anti-automorphism is a genuine condition, and the involution is the certificate that the ring is isomorphic to its opposite ring; for a group the inversion supplies the certificate for every group at once. What is informative in the group case is the set of involutions and the structure each of them defines, not the bare existence.

### Anti-automorphisms and Automorphisms

**Proposition.** The composition of two anti-automorphisms is an automorphism, and the composition of an automorphism with an anti-automorphism is an anti-automorphism. Hence $\operatorname{Aut}(G) \cup \operatorname{Anti}(G)$ is a subgroup of $\operatorname{Sym}(G)$, written $\operatorname{Aut}^*(G)$, in which $\operatorname{Aut}(G)$ has index two and $\operatorname{Anti}(G)$ is a coset.

**Proof.** If $\sigma, \tau$ are anti-automorphisms then $\sigma\tau(ab) = \sigma(\tau(b)\tau(a)) = \sigma(\tau(a))\sigma(\tau(b)) = \sigma\tau(a)\,\sigma\tau(b)$, so $\sigma\tau \in \operatorname{Aut}(G)$; the remaining statements are the same computation in the other two orders. The set is closed under composition, contains $\mathrm{id}$, and is a subset of the bijections of $G$; each element is invertible with inverse of the same kind, so it is a subgroup.

**Proposition.** The inversion is central in $\operatorname{Aut}^*(G)$: it commutes with every automorphism and with every anti-automorphism. Consequently $\operatorname{Anti}(G) = \iota \operatorname{Aut}(G) = \operatorname{Aut}(G)\iota$ and $\lvert \operatorname{Anti}(G) \rvert = \lvert \operatorname{Aut}(G) \rvert$.

**Proof.** Every homomorphism or anti-homomorphism $\varphi : G \to G$ satisfies $\varphi(g^{-1}) = \varphi(g)^{-1}$, since $\varphi(g)\varphi(g^{-1}) = \varphi(e) = e$ by multiplicativity or anti-multiplicativity and the inverse is unique; this is the commutation $\varphi\iota = \iota\varphi$. Multiplying the coset statement by $\iota$ gives the equality, and left multiplication by $\iota$ is a bijection $\operatorname{Aut}(G) \to \operatorname{Anti}(G)$.

**Theorem.** The map $\sigma \mapsto \sigma\iota = \iota\sigma$ is a bijection from $\operatorname{Anti}(G)$ onto $\operatorname{Aut}(G)$; its inverse is $\alpha \mapsto \iota\alpha$. Under this bijection the involutions of $G$ correspond exactly to the **involutive automorphisms** of $G$, the automorphisms $\alpha$ with $\alpha^2 = \mathrm{id}$, and the inversion corresponds to the identity.

**Proof.** The product of the two anti-automorphisms $\sigma$ and $\iota$ is an automorphism, so the map lands in $\operatorname{Aut}(G)$, and it is injective because $\sigma = (\sigma\iota)\iota$ recovers $\sigma$ from $\sigma\iota$; it is surjective because $\iota\alpha$ is an anti-automorphism for every automorphism $\alpha$. For the order, $(\sigma\iota)^2 = \sigma\iota\sigma\iota = \sigma^2\iota^2 = \mathrm{id}\cdot\mathrm{id} = \mathrm{id}$ using the commutation of $\iota$ with $\sigma$; conversely if $\alpha^2 = \mathrm{id}$ then $(\iota\alpha)^2 = \iota^2\alpha^2 = \mathrm{id}$. Finally $\sigma\iota = \mathrm{id}$ exactly when $\sigma = \iota$.

**Corollary.** A group has exactly as many involutions as it has involutive automorphisms. The involution $\sigma = \iota\alpha$ is the identity map exactly when $G$ is abelian of exponent dividing two, in which case $\alpha$ and the inversion are both the identity.

**Proposition.** An anti-automorphism of $G$ is an automorphism if and only if $G$ is abelian.

**Proof.** If $\sigma$ is both, then $\sigma(a)\sigma(b) = \sigma(ab) = \sigma(b)\sigma(a)$ for all $a, b$, so the image $\sigma(G) = G$ is abelian. Conversely, on an abelian group $\sigma(ab) = \sigma(a)\sigma(b) = \sigma(b)\sigma(a)$ for every anti-automorphism.

**Corollary.** For an abelian group $\operatorname{Anti}(G) = \operatorname{Aut}(G)$ and the involutions of $G$ are exactly the automorphisms $\alpha$ with $\alpha^2 = \mathrm{id}$. In particular the theory of involutions of an abelian group is the theory of the elements of order at most two in its automorphism group, and it degenerates completely: no nonabelian phenomenon survives.

### Elementary Properties

**Proposition.** Let $\sigma$ be an involution of $G$. Then $\sigma(e) = e$; $\sigma(g^{-1}) = \sigma(g)^{-1}$; if $H \leq G$ then $\sigma(H) \leq G$ with $\lvert \sigma(H) \rvert = \lvert H \rvert$; if $H \trianglelefteq G$ then $\sigma(H) \trianglelefteq G$ and $G/\sigma(H) \cong G/H$, because $gH \mapsto \sigma(g)\sigma(H)$ is an anti-isomorphism of the quotients and composing it with the inversion of the second quotient gives an isomorphism; and $\sigma$ preserves inclusion, so it is an automorphism of the subgroup lattice of $G$ (not of the group, unless $G$ is abelian).

**Proof.** The unit satisfies $\sigma(e) = \sigma(e)\sigma(e)^{-1} = \sigma(e)\sigma(e^{-1}) = \sigma(e^{-1}e) = \sigma(e)$, so $\sigma(e) = e$ after cancelling. Then $\sigma(g)\sigma(g^{-1}) = \sigma(g^{-1}g) = e$, giving the second statement after uniqueness of inverses. The remaining statements are consequences of bijectivity and of the two-sidedness of normality: $\sigma$ is a bijection of the subsets of $G$ that reverses no inclusion, and $gH = Hg$ for all $g$ implies $\sigma(g)\sigma(H) = \sigma(H)\sigma(g)$.

**Proposition.** For $g \in G$ the involution carries the conjugacy class of $g$ onto the conjugacy class of $\sigma(g)$, and it carries the centraliser $C_G(g)$ onto $C_G(\sigma(g))$.

**Proof.** $\sigma(x g x^{-1}) = \sigma(x)^{-1}\sigma(g)\sigma(x)$, so conjugates of $g$ go to conjugates of $\sigma(g)$, and bijectivity makes the correspondence a bijection of classes. For the centralisers, $x g x^{-1} = g$ if and only if $\sigma(x)\sigma(g)\sigma(x)^{-1} = \sigma(g)$.

**Proposition.** The commutator subgroup $[G, G]$ is $\sigma$-stable, and $\sigma$ induces an involution $\sigma^{\mathrm{ab}}$ of the abelianisation $G^{\mathrm{ab}} = G/[G, G]$; for the inversion the induced map is the inversion of the abelian group $G^{\mathrm{ab}}$.

**Proof.** $\sigma([x, y]) = [\sigma(y), \sigma(x)]$, so commutators go to commutators and $[G, G]$ is stable; the induced map is well defined and of order two because $\sigma$ is, and for $\sigma = \iota$ it sends $g[G, G]$ to $g^{-1}[G, G]$.

### Examples

**Example (the inversion).** Every group has the involution $\iota(g) = g^{-1}$. It is the identity exactly on the groups of exponent dividing two, in particular on every elementary abelian group; and it is the only involution whose associated automorphism, in the bijection of the theorem above, is the identity.

**Example (the identity).** The identity map is an involution exactly when $G$ is abelian, by the proposition on automorphisms that are anti-automorphisms; then it is the associated automorphism $\alpha$ of the inversion, and it is not the inversion unless the exponent divides two. So on an abelian group the identity and the inversion are distinct involutions as soon as some element has order greater than two.

**Example (products).** On a product $G \times H$ with involutions $\sigma$ on $G$ and $\tau$ on $H$, the componentwise map $(\sigma, \tau)$ is an involution. The **swap** $\varsigma(g, h) = (h, g)$ is an involution of $G \times G$; it is an automorphism, not merely an anti-automorphism, since $(g, h)(g', h') = (gg', hh')$ and the swap of the product is the product of the swaps.

**Example (the action of the automorphism group).** The group $\operatorname{Aut}(G)$ acts on the set of involutions of $G$ by conjugation, $\varphi\cdot\sigma = \varphi\sigma\varphi^{-1}$. The inversion is fixed by every automorphism, since $\varphi\iota\varphi^{-1} = \iota$ for every $\varphi$, so its orbit is the single point $\{\iota\}$. Under the bijection $\sigma \mapsto \sigma\iota$ this action becomes conjugation of the involutive automorphisms, so the involutions of $G$ fall into classes, and the class of the inversion is the singleton.

**Example (symmetric groups).** Inversion is an involution of $S_n$. In the notation in which $S_n$ is generated by the adjacent transpositions $s_1, \ldots, s_{n-1}$, the inversion is the anti-automorphism fixing every generator and reversing words: a product $s_{i_1}\cdots s_{i_k}$ goes to $s_{i_k}\cdots s_{i_1} = (s_{i_1}\cdots s_{i_k})^{-1}$, because each generator is its own inverse.

**Example (dihedral groups).** In $D_n = \langle r, s \mid r^n = s^2 = e,\ srs = r^{-1}\rangle$ the inversion inverts $r$ and fixes $s$, so its associated automorphism is the identity. The **reversal** $\rho$, defined by fixing $r$ and $s$ and extending anti-multiplicatively, that is $\rho(r^k) = r^k$ and $\rho(r^k s) = r^{-k}s$, is a second involution: it is anti-multiplicative on the reduced words, it satisfies $\rho^2 = \mathrm{id}$, and its associated automorphism $\rho\iota$ inverts $r$ and fixes $s$, that is it is conjugation by $s$. So $D_n$ has at least these two involutions, and they differ already on $r$ when $n > 2$, since $\iota(r) = r^{-1}$ whereas $\rho(r) = r$.

**Example (the free group).** Let $F = F(S)$ be free on $S$ and let $\mathrm{rev}$ reverse a reduced word without inverting its letters. Then $\mathrm{rev}(uv) = \mathrm{rev}(v)\mathrm{rev}(u)$, so $\mathrm{rev}$ is an anti-automorphism, and $\mathrm{rev}^2 = \mathrm{id}$; the inversion is a second anti-automorphism, and the two differ on any letter of $S$ that is not its own inverse. Their composition $\iota\,\mathrm{rev}$ is an automorphism of $F$, of order two, and the two commute because every anti-automorphism $\varphi$ satisfies $\varphi(g^{-1}) = \varphi(g)^{-1}$, so $\varphi\iota = \iota\varphi$.

---

## Fixed Elements and Inverted Elements

### The Fixed Set

**Definition.** The **fixed set** of $\sigma$ is $G^\sigma = \{g \in G : \sigma(g) = g\}$. The **inverted set** is $I(\sigma) = \{g \in G : \sigma(g) = g^{-1}\}$.

**Proposition.** $G^\sigma$ contains $e$ and is closed under inversion. It is a subgroup of $G$ exactly when its elements commute pairwise.

**Proof.** $\sigma(e) = e$ and $\sigma(g^{-1}) = \sigma(g)^{-1} = g^{-1}$ for $g \in G^\sigma$. For $g, h \in G^\sigma$ one has $\sigma(gh) = \sigma(h)\sigma(g) = hg$, so $gh \in G^\sigma$ exactly when $hg = gh$. If the elements of $G^\sigma$ commute pairwise, the set is closed under multiplication and under inversion, hence a subgroup; conversely the computation exhibits a failure of closure whenever two of them fail to commute.

**Example (a fixed set that is not a subgroup).** In $S_3$ let $\alpha$ be conjugation by the transposition $(1\,2)$, an involutive automorphism, and let $\sigma = \iota\alpha$. Then $\sigma(g) = \alpha(g)^{-1}$ and

$$
G^\sigma = \{e, (1\,2), (1\,2\,3), (1\,3\,2)\}, \qquad \lvert G^\sigma \rvert = 4 .
$$

This set has four elements and $S_3$ has six, so it is not a subgroup; concretely $(1\,2)(1\,2\,3) = (2\,3)$ is outside it. The example shows that the fixed set of an involution is a subgroup only under the commuting hypothesis, and it is the exact counterpart of the fixed set of a ring involution, which is a subring under the same kind of hypothesis.

### The Inverted Set

**Theorem.** The inverted set $I(\sigma)$ is always a subgroup of $G$. In the notation of the bijection $\alpha = \sigma\iota$, it is the fixed subgroup of $\alpha$,

$$
I(\sigma) = G^{\sigma\iota} = G^\alpha ,
$$

and dually $I(\alpha) = G^{\sigma}$ for the same pair $(\sigma, \alpha)$.

**Proof.** For $g, h \in I(\sigma)$ one has $\sigma(gh) = \sigma(h)\sigma(g) = h^{-1}g^{-1} = (gh)^{-1}$, so $gh \in I(\sigma)$; also $e \in I(\sigma)$ and $g^{-1} \in I(\sigma)$ since $\sigma(g^{-1}) = \sigma(g)^{-1} = g$. For the identification, $\sigma(g) = g^{-1}$ is equivalent to $\iota\sigma(g) = g$, that is to $\alpha(g) = g$. The dual statement is the same argument with the roles exchanged.

**Corollary.** For the inversion, $I(\iota) = G$ and $G^\iota = \{g \in G : g^2 = e\}$ is the $2$-torsion set, which is a subgroup exactly when the elements of order dividing two commute pairwise. It is a subgroup in every abelian group, where it is the subgroup of elements of order at most two, and it is not a subgroup of $S_3$, whose four elements of order dividing two multiply $(1\,2)(2\,3)$ to the three-cycle $(1\,2\,3)$ of order three.

**Remark.** The two sets are dual and are easy to confuse. For the inversion, everything is inverted and the fixed set is the $2$-torsion, generally not a subgroup; for an involution whose associated automorphism is not the identity the inverted set is a genuine subgroup and the fixed set is generally not one. The example $S_3$ with $\sigma = \iota\alpha$ above realises both degeneracies at once: $G^\sigma$ has four elements and is not a subgroup, while $I(\sigma) =\{e, (1\,2)\}$ is one.

### The Conjugate Products

In a ring with involution the two products $x\sigma(x)$ and $\sigma(x)x$ are fixed by the involution, and both are needed for the theory. For a group the analogous products $g\sigma(g)$ and $\sigma(g)g$ behave differently, and the difference is a useful warning.

**Proposition.** For $g \in G$ the elements $g\sigma(g)$ and $\sigma(g)g$ are conjugate, and $g\sigma(g)^{-1}$ is fixed by $\sigma$ exactly when $g$ satisfies $g^{4} = e$ in the case $\sigma = \iota$.

**Proof.** The first two are conjugate because $\sigma(g)g = \sigma(g)(g\sigma(g))\sigma(g)^{-1}$: indeed $\sigma(g)(g\sigma(g))\sigma(g)^{-1} = \sigma(g)g$. For the second, with $\sigma = \iota$ the element $g\sigma(g)^{-1}$ is $g\cdot g = g^2$, and $\iota(g^2) = g^{-2}$, so $g^2$ is fixed exactly when $g^4 = e$.

**Example.** In $C_3$ with the inversion, the element $g^2$ of the element $g$ of order three has order three and is not fixed by the inversion, so the conjugate product is not fixed; in $C_4$ the square of a generator has order two and is fixed by the inversion. The ring statement that $x\sigma(x)$ is always symmetric therefore has no group counterpart, because the group product is not commutative and the convergence $g\sigma(g) = \sigma(g)g$ fails.

---

## Real Elements and Products of Elements of Order Two

### Real and Strongly Real Elements

**Definition.** An element $g \in G$ is **real** if $g$ is conjugate to $g^{-1}$, that is if some $x \in G$ satisfies $xgx^{-1} = g^{-1}$; it is **strongly real** if it is a product of two elements of order two. A group is **ambivalent** if every element is real.

**Proposition.** An element is real exactly when its conjugacy class is stable under the inversion. The involution $\iota$ permutes the conjugacy classes, and the real classes are its fixed points.

**Proof.** The class of $g$ is $\{xgx^{-1} : x \in G\}$; it contains $g^{-1}$ exactly when $g^{-1} = xgx^{-1}$ for some $x$, which is the definition of real. Since $g \mapsto g^{-1}$ is a bijection carrying classes to classes by the proposition on classes above, it acts on the set of classes, and the real classes are the classes it fixes.

**Proposition.** An element $g$ is strongly real if and only if some element of order two inverts it, that is if there is $x$ with $x^2 = e$ and $xgx^{-1} = g^{-1}$. Every strongly real element is real.

**Proof.** If $g = xy$ with $x^2 = y^2 = e$, then $xgx^{-1} = x(xy)x^{-1} = yx^{-1} = yx = (xy)^{-1} = g^{-1}$, so $x$ is an element of order two inverting $g$. Conversely if $x^2 = e$ and $xgx^{-1} = g^{-1}$, then $xg = g^{-1}x$, and $y = xg$ satisfies $y^2 = (xg)(xg) = (g^{-1}x)(xg) = g^{-1}x^2g = e$, while $xy = x(xg) = x^2g = g$. So $g$ is a product of the two elements $x$ and $y$ of order two. Strongly real implies real because the inverting element $x$ exhibits the conjugacy.

**Proposition.** For $g \in G$ the set of elements inverting $g$ is either empty or a coset of the centraliser $C_G(g)$.

**Proof.** Suppose $x_0 g x_0^{-1} = g^{-1}$ and let $c \in G$. Then $(x_0c)g(x_0c)^{-1} = x_0(cgc^{-1})x_0^{-1} = g^{-1}$ exactly when $cgc^{-1} = g$, that is exactly when $c \in C_G(g)$. So the inverting elements are the coset $x_0C_G(g)$, and their number is $\lvert C_G(g) \rvert$, hence either zero or $\lvert G \rvert / \lvert \text{class of } g \rvert$.

### The Elements of Order Two

**Proposition.** The set of products of two elements of order two contains every element of order two (take the other factor to be $e$) and is contained in the set of real elements. It is not in general a subgroup: in $Q_8$ the elements of order two are $e$ and $-1$, and their products are $e$ and $-1$ again, whereas $Q_8$ has six further real elements.

**Proof.** The containment statements are immediate, and the assertions about $Q_8$ are read from the multiplication table: $-1$ is the unique element of order two, so the products of two elements of order two are among $e$ and $-1$, and the elements $i, -i, j, -j, k, -k$ of order four are real because $jij^{-1} = -i = i^{-1}$ and likewise.

### Ambivalent Groups

**Proposition.** An abelian group is ambivalent exactly when it has exponent dividing two; then every element is a product of two elements of order two.

**Proof.** In an abelian group conjugation is trivial, so $g$ is real exactly when $g = g^{-1}$, that is $g^2 = e$. If every element has order at most two, every element is itself of order two, hence a product of two elements of order two, namely itself and $e$.

**Proposition.** A cyclic group $C_n$ has exponent dividing two only for $n \leq 2$; for $n \geq 3$ its elements of order greater than two are not real.

**Example (symmetric groups).** Every permutation is conjugate to its inverse, because a permutation and its inverse have the same cycle type and, in a symmetric group, conjugate permutations are exactly those of the same cycle type. So $S_n$ is ambivalent. Stronger, every permutation is a product of two elements of order two: it is enough to do a $k$-cycle, since involutions supported in disjoint cycles commute and their product is the product of the cycles, and for the $k$-cycle one may take the two elements of order two

$$
y = (1\ k)(2\ k-1)(3\ k-2)\cdots, \qquad x = (2\ k)(3\ k-1)(4\ k-2)\cdots,
$$

each a product of disjoint transpositions and so of order two, whose product is $xy = (1\,2\,\cdots\,k)$. So every element of $S_n$ is strongly real.

**Example (dihedral groups).** In $D_n = \langle r, s\rangle$ the elements of order two are the reflections, and $r^{n/2}$ when $n$ is even; and the rotation $r^k$ is the product $s\cdot(sr^k)$ of two reflections, hence strongly real. So $D_n$ is ambivalent and every element is a product of two elements of order two. The reflections are fixed by the inversion, each being its own inverse, and each rotation class $\{r^k, r^{-k}\}$ is inversion-stable; the number of classes is $(n+3)/2$ for $n$ odd and $n/2+3$ for $n$ even, and the inversion fixes every one of them.

**Example (the quaternion group).** In $Q_8$ the unique element of order two is $-1$, so the products of two elements of order two are $\pm 1$, while the six elements of order four are real. Hence $Q_8$ is ambivalent but not every element is strongly real: real does not imply strongly real, and the failure is detected by the products of two elements of order two.

**Example (alternating groups).** The group $A_4$ is not ambivalent. Its eight three-cycles fall into two conjugacy classes of four, and the two classes are interchanged by the inversion; a three-cycle is therefore conjugate in $A_4$ to the inverse of the elements of the other class and not to its own inverse. In $A_5$ the situation is different: $A_5$ is ambivalent, a fact that belongs with its conjugacy classes (*Finite Groups and Symmetry*, "Conjugacy Classes of $S_n$ and $A_n$") rather than with the involutions.

**Example (the small groups, counted).** The following table gives the automorphism group, the number of involutions as maps, ambivalence, and the set of products of two elements of order two, for the small groups discussed in this article:

| $G$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ | $C_6$ | $C_7$ | $C_8$ | $C_9$ | $C_{10}$ | $V_4$ | $S_3$ | $D_4$ | $Q_8$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\lvert \operatorname{Aut}(G)\rvert = \lvert \operatorname{Anti}(G)\rvert$ | $1$ | $2$ | $2$ | $4$ | $2$ | $6$ | $4$ | $6$ | $4$ | $6$ | $6$ | $8$ | $24$ |
| involutions as maps | $1$ | $2$ | $2$ | $2$ | $2$ | $2$ | $4$ | $2$ | $2$ | $4$ | $4$ | $6$ | $10$ |
| ambivalent | yes | no | no | no | no | no | no | no | no | yes | yes | yes | yes |
| products of two elements of order two | all | $\{e\}$ | $\{e, r^2\}$ | $\{e\}$ | $\{e, r^3\}$ | $\{e\}$ | $\{e, r^4\}$ | $\{e\}$ | $\{e, r^5\}$ | all | all | all | $\{e, -1\}$ |

**Remark.** Two entries deserve comment. The cyclic group $C_8$ has four involutions as maps, not two: besides the identity and the inversion there are the multiplications by the residues $r$ with $r^2 \equiv 1$ modulo eight and $r \not\equiv \pm 1$, namely $r = 3$ and $r = 5$, and these are genuinely different involutions of the same group. And $C_5, C_7, C_9, C_{10}$ have exactly two, the identity and the inversion, so the count is not simply a function of the order. The involution count is the number of involutive automorphisms, by the theorem of the first section, and the automorphism group of a cyclic group of order $n$ is the group of the residues coprime to $n$ under multiplication modulo $n$; the elements of order dividing two among them are the solutions of $r^2 \equiv 1$. For an odd prime $p$ these are $r = \pm 1$, so $C_p$ has exactly two.

---

## Quotients, Subgroups and Products

### Stable Subgroups and Quotients

**Definition.** A subgroup $H \leq G$ is **$\sigma$-stable** if $\sigma(H) = H$.

**Proposition.** Let $H$ be a $\sigma$-stable subgroup. Then $\sigma$ restricts to an involution of $H$, and $H \cap G^\sigma = H^\sigma$ and $H \cap I(\sigma) = I(\sigma|_H)$. If in addition $H \trianglelefteq G$, then $\sigma$ induces an involution $\bar\sigma$ of the quotient $G/H$, and

$$
\pi(G^\sigma) \subseteq (G/H)^{\bar\sigma}, \qquad \pi(I(\sigma)) \subseteq I(\bar\sigma),
$$

where $\pi : G \to G/H$ is the quotient map. Both inclusions can be strict.

**Proof.** The restriction of an anti-automorphism to a stable subgroup is an anti-automorphism of that subgroup, and its square is the identity; the intersections are the definitions. For the quotient, $\bar\sigma(gH) = \sigma(g)H$ is well defined because $\sigma(H) = H$, and it is an anti-automorphism of order at most two, hence an involution because it is a bijection with $\bar\sigma^2(gH) = gH$. An element of $G^\sigma$ visibly has an image in $(G/H)^{\bar\sigma}$, which gives the first inclusion, and the second is the same statement in the inverted set.

**Example (a strict inclusion).** Let $G = \mathbb{Z}/4\mathbb{Z}$ with the inversion $\iota(g) = -g$ and let $H$ be the subgroup $\{0, 2\}$. Then $G^\iota = \{0, 2\}$ and $\pi(G^\iota) = \{0\}$, while $G/H \cong \mathbb{Z}/2\mathbb{Z}$ and the induced involution is the identity, so $(G/H)^{\bar\iota}$ has two elements. The image of the fixed set is properly smaller than the fixed set of the quotient.

**Remark.** The example is the group counterpart of the corresponding strictness for a ring with involution, where the fixed ring can fail to map onto the fixed ring of a quotient. The mechanism is the same: an element of the quotient can be fixed although no fixed element of $G$ represents it.

### Products and the Swap

**Proposition.** Let $\sigma$ be an involution of $G$ and $\tau$ an involution of $H$. The componentwise map $(\sigma, \tau)$ is an involution of $G \times H$, and its fixed set is $G^\sigma \times H^\tau$. The swap is an involutive automorphism of $G \times G$ whose fixed subgroup is the diagonal $\{(g, g) : g \in G\}$; the diagonal is a subgroup because the swap is multiplicative.

**Proof.** Componentwise statements are immediate. For the swap, $(g, h)(g', h') = (gg', hh')$ and $\varsigma((g, h)(g', h')) = (h h', g g') = \varsigma(g, h)\varsigma(g', h')$, so the swap is an automorphism of order two; its fixed points satisfy $(h, g) = (g, h)$, that is $g = h$.

### The Twisted Map

**Proposition.** Let $\tau : G \to H$ be an **anti-isomorphism** of groups, that is a bijection with $\tau(ab) = \tau(b)\tau(a)$, and define $\sigma(g, h) = (\tau^{-1}(h), \tau(g))$ on $G \times H$. Then $\sigma$ is an involution of $G \times H$ and its fixed set is the graph $\{(g, \tau(g)) : g \in G\}$ of $\tau$.

**Proof.** $\sigma^2(g, h) = \sigma(\tau^{-1}(h), \tau(g)) = (\tau^{-1}(\tau(g)), \tau(\tau^{-1}(h))) = (g, h)$. For anti-multiplicativity, using that $\tau$ and $\tau^{-1}$ are anti-multiplicative (as $\tau^{-1}\tau = \mathrm{id}$ and $\tau$ is anti),

$$
\sigma\bigl((g, h)(g', h')\bigr) = \sigma(gg', hh') = \bigl(\tau^{-1}(hh'), \tau(gg')\bigr) = \bigl(\tau^{-1}(h')\tau^{-1}(h), \tau(g')\tau(g)\bigr),
$$

which equals $\sigma(g', h')\sigma(g, h) = (\tau^{-1}(h'), \tau(g'))(\tau^{-1}(h), \tau(g))$ by the componentwise product; so $\sigma$ is an anti-automorphism, of order two, hence an involution. Fixed points satisfy $(g, h) = (\tau^{-1}(h), \tau(g))$, that is $h = \tau(g)$, the graph.

**Remark (a trap).** The same formula with $\tau$ an **isomorphism** has order two but is not an anti-automorphism in general: with $G = H$ nonabelian and $\tau$ an inner automorphism the computation of anti-multiplicativity fails on the first component. The construction needs $\tau$ anti-multiplicative, for the same reason that the twisted transposed matrix needs the transpose and not an arbitrary bijection.

**Remark (the graph is not a subgroup).** When $\tau$ is an anti-isomorphism and not a homomorphism, its graph is not a subgroup of $G \times H$, in agreement with the failure of the fixed set of an involution to be a subgroup: the product of $(g, \tau(g))$ and $(h, \tau(h))$ is $(gh, \tau(g)\tau(h))$, whereas an element of the graph over $gh$ has second component $\tau(gh) = \tau(h)\tau(g)$. For example in $S_3 \times S_3$ with $\tau = \iota$ the graph of the inversion is the set of pairs $(g, g^{-1})$, of size six, and it is not closed under multiplication.

---

## Involutions and Extensions

### The Semidirect Product by an Involutive Automorphism

**Theorem.** Let $\alpha$ be an involutive automorphism of $G$, so that $\alpha^2 = \mathrm{id}$, and let $C_2 = \langle t\rangle$ act on $G$ through $\alpha$. The semidirect product $G \rtimes C_2$ has order $2\lvert G \rvert$, contains $G$ as a normal subgroup of index two, and conjugation by $t$ realises $\alpha$. Conversely, an extension of $G$ by $C_2$ that splits gives, by letting $t$ act on $G$ by conjugation, an involutive automorphism of $G$; isomorphism classes of such split extensions correspond to the conjugacy classes of involutive automorphisms under the action of $\operatorname{Aut}(G)$.

**Proof.** The semidirect product is defined because $\alpha$ is an automorphism, and its properties are those of the construction in *Generators, Presentations and Free Products*; the conjugation by $t$ is the defining action. For the converse, a splitting exhibits a complement $\langle t\rangle$ of order two, and $tgt^{-1}$ defines the action; two actions give isomorphic extensions exactly when the corresponding homomorphisms are conjugate by an automorphism of $G$. The detail of the classification, and the non-split case, is the theory of $H^2$ of *Group Cohomology*.

**Corollary.** The involutions of $G$ are in bijection with the involutive automorphisms of $G$, hence with the split extensions of $G$ by $C_2$ up to isomorphism of the extension.

**Remark.** The involutions of $G$ therefore record the same information as the ways in which $G$ can sit as an index-two normal subgroup of a larger group with a complement of order two. This is the sense in which an involutive group is a group with a small amount of extra structure, and not a new class of groups: the datum is the involutive automorphism $\alpha$, and the involution $\sigma = \iota\alpha$ is the inversion twisted by it.

### Dihedral and Dicyclic Groups

**Example.** Take $G = C_n$ cyclic and $\alpha$ the inversion, an involutive automorphism; the extension is the dihedral group $D_n \cong C_n \rtimes C_2$, with the generator of $C_2$ acting by inversion. For $n$ odd prime this is the whole story of the groups of order $2n$: a group of order $2p$ with $p$ an odd prime is cyclic $C_{2p}$ or dihedral $D_p$, because $\operatorname{Aut}(C_p) \cong C_{p-1}$ has a unique element of order two, the inversion (*Groups*, §13 and §16).

**Example.** The dicyclic group $\operatorname{Dic}_n$ is a non-split extension of $C_{2n}$ by $C_2$ in which the generator of the quotient acts by inversion and the complement squares to the element of order two of $\langle a\rangle$; so it is not a semidirect product $C_{2n} \rtimes C_2$, although the action of the quotient on the kernel is exactly the inversion. The dicyclic groups are exactly the finite groups with a unique element of order two that are not cyclic (*Finite Groups and Symmetry*, "Dicyclic Groups"). The example shows that the involutive automorphism of the kernel does not determine the extension: the split and the non-split extensions with the same action are different groups.

### The Abelian Case

**Proposition.** Let $G$ be abelian. Then $\operatorname{Anti}(G) = \operatorname{Aut}(G)$, so the involutions of $G$ are the automorphisms of order at most two; the inversion is one of them; and the fixed set of the inversion is the subgroup of elements of order at most two.

**Proof.** The first statement is the corollary in the first section, the second is the definition of the bijection, and the third is $G^\iota = \{g : g^2 = e\}$, which in an abelian group is closed because $g, h$ of order dividing two give $(gh)^2 = g^2h^2 = e$.

**Remark.** On an abelian group the whole theory collapses to the study of $\operatorname{Aut}(G)$. The interesting involutions are those of nonabelian groups, where the inversion is a genuine anti-automorphism and not an automorphism, and where the associated involutive automorphism $\alpha = \sigma\iota$ is a separate piece of information.

---

## Involutions and Presentations

### Free Groups and Reverse Words

**Proposition.** On the free group $F(S)$ the inversion $\iota(w) = w^{-1}$ and the word reversal $\mathrm{rev}$ are distinct involutions whenever $S$ contains a letter $s$ with $s^2 \neq e$, and $\iota\,\mathrm{rev} = \mathrm{rev}\,\iota$ is an involutive automorphism of $F(S)$.

**Proof.** Both maps are anti-automorphisms of order two, so their composition is an automorphism; they commute because every anti-automorphism $\varphi$ satisfies $\varphi(g^{-1}) = \varphi(g)^{-1}$, and directly because reversing a word and inverting its letters commute, $\iota(\mathrm{rev}(w)) = \mathrm{rev}(\iota(w))$ for every $w$. On a letter $s$ with $s^2 \neq e$ one has $\iota(s) \neq \mathrm{rev}(s) = s$, so the two involutions differ.

**Example.** In the free group $F(x, y)$ the two involutions send the word $xy$ to $y^{-1}x^{-1}$ and to $yx$ respectively, which are different elements.

### Coxeter Groups

**Example.** In a Coxeter group $W$ with generating set $S$ the inversion is the anti-automorphism fixing each generator and reversing words; it is an involution of $W$, and for a Coxeter group it is the same map as the word reversal, because each generator is its own inverse. Composing it with the automorphisms induced by the symmetries of the diagram gives further involutions: if $\tau$ is a symmetry of the diagram of order two, then $\iota\tau$ is an involution of $W$, since $\iota$ commutes with every automorphism and $(\iota\tau)^2 = \tau^2 = \mathrm{id}$. For the dihedral type $I_2(m)$, which is $D_m$, the swap of the two generators is such a symmetry, and the composition is an involution different from the inversion as soon as the diagram has two nodes and the group is nonabelian. The combinatorial theory of the Coxeter generators is *Coxeter Groups*; the reflection representations and the Weyl groups need a form and belong to Part II.

### Braid Groups

**Example.** On the braid group $B_n$ with Artin generators $\sigma_1, \ldots, \sigma_{n-1}$ the inversion $\sigma_i \mapsto \sigma_i^{-1}$ and the reversal $\sigma_i \mapsto \sigma_{n-i}$ are automorphisms of order two, and together with the inner automorphisms they generate $\operatorname{Aut}(B_n)$ for $n \geq 3$ (*Braid Groups*, "Automorphisms"). This is the sharpest illustration of the terminology: $B_n$ is torsion-free and has no elements of order two at all, yet it carries the nontrivial involutions $\sigma_i \mapsto \sigma_i^{-1}$ and $\sigma_i \mapsto \sigma_{n-i}$. The word *involution* in the statement of the automorphism theorem refers to the maps, not to elements.

---

## What the Group Case Does Differently

The comparison with *Involutive Rings* is instructive, because the same vocabulary covers two different theories.

- **Existence.** A ring with an involution is a ring satisfying a condition; a group always has one, the inversion, and the informative object is the set of them. The group analogue of the ring question "is this ring isomorphic to its opposite ring" has the trivial answer yes, by $\iota$.
- **The fixed set.** In both theories the fixed set of the involution is closed under the relevant inversion and contains the unit, and is a substructure exactly when its elements commute pairwise. The failure is exhibited by $S_3$ with $\sigma = \iota\alpha$ and by the corresponding ring examples, and it is the same failure.
- **The inverted set.** In a group the set $\{g : \sigma(g) = g^{-1}\}$ is always a subgroup, being the fixed subgroup of the associated automorphism, and this has no ring analogue: the skew-symmetric elements of a ring with involution are only an additive subgroup.
- **The conjugate products.** In a ring $x\sigma(x)$ is fixed; in a group $g\sigma(g)$ need not be, and the two products $g\sigma(g)$ and $\sigma(g)g$ are only conjugate.
- **The quotients.** The group theory uses normal subgroups and the lattice of subgroups, and the ring theory uses ideals and the two-sided lattice. The strictness of the image of the fixed set in the fixed set of a quotient occurs in both, with the same mechanism and the same example shape, $\mathbb{Z}/4\mathbb{Z}$ here and $\mathbb{Z}[i]/(2)$ there.
- **Elementary versus derived.** In a group every element is a word in the generators and the involution is visible on words, which is why the presentations of the free, Coxeter and braid groups give their involutions directly; a ring has no such normal form, and its involutions must be given by formulas.

---

## Summary

An involution of a group is an anti-automorphism of order two. Every group has the inversion, the canonical isomorphism with its opposite group, and the involutions of $G$ are in bijection with the involutive automorphisms $\alpha$ of $G$ through $\sigma = \iota\alpha$; equivalently with the split extensions of $G$ by $C_2$, or with the involutive automorphisms up to conjugacy. An anti-automorphism is an automorphism exactly when the group is abelian. The fixed set $G^\sigma$ contains $e$ and is inversion-closed and is a subgroup exactly when its elements commute pairwise; the inverted set $I(\sigma) = G^{\sigma\iota}$ is always a subgroup, the fixed subgroup of $\alpha$. The inversion acts on the conjugacy classes, its fixed classes being the real classes, and the strongly real elements, the products of two elements of order two, are those inverted by an element of order two. $S_n$ and $D_n$ are ambivalent and strongly real, $Q_8$ is ambivalent but has only $e$ and $-1$ as products of two elements of order two, $A_4$ is not ambivalent, and an abelian group is ambivalent exactly when it has exponent dividing two. On quotients by a stable normal subgroup the induced involution need not have the image of $G^\sigma$ as its whole fixed set; products carry the componentwise involution and the swap, whose fixed subgroup is the diagonal; and the graph of an anti-isomorphism is the fixed set of a twisted involution, the construction failing if the map is only an isomorphism. The involutions of a presented group are read off its presentation: the free group has the inversion and the word reversal, a Coxeter group has the inversion, which is the word reversal, and the braid groups have the inversion and the reversal as automorphisms although they have no elements of order two.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\sigma$ | an involution of a group, that is an anti-automorphism of order two |
| $\iota$ | the inversion $\iota(g) = g^{-1}$, the canonical involution of every group |
| $G^{\mathrm{op}}$ | the opposite group, with $a \cdot^{\mathrm{op}} b = ba$ |
| $\operatorname{Anti}(G)$ | the set of anti-automorphisms of $G$; a coset of $\operatorname{Aut}(G)$ in $\operatorname{Aut}^*(G)$ |
| $\operatorname{Aut}^*(G)$ | $\operatorname{Aut}(G) \cup \operatorname{Anti}(G)$, a subgroup of $\operatorname{Sym}(G)$ |
| $\alpha = \sigma\iota$ | the involutive automorphism associated with $\sigma$ |
| $G^\sigma$ | the fixed set $\{g : \sigma(g) = g\}$ |
| $I(\sigma)$ | the inverted set $\{g : \sigma(g) = g^{-1}\} = G^{\sigma\iota}$ |
| real | conjugate to the inverse |
| strongly real | a product of two elements of order two |
| ambivalent | every element real |

## Further Reading

- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for involutions of groups, the inversion and the opposite group, and the elementary structure of the automorphism group.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for the symmetric and dihedral groups, conjugacy classes, and products of elements of order two.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976), for the theory of real and strongly real elements; the counting of the two kinds by the Frobenius–Schur indicator belongs to representation theory and is not used here.
- O. Ore, "Some studies on group theory", *Duke Mathematical Journal* **18** (1951), for the products of two involutions in a symmetric group and the associated cycle criterion.
- James E. Humphreys, *Reflection Groups and Coxeter Groups* (Cambridge University Press, 1990), for the Coxeter inversion, the diagram automorphisms and the word reversal.
- Christian Kassel and Vladimir Turaev, *Braid Groups* (Springer, 2008), for the Dyer–Grossman theorem that the inversion, the reversal and the inner automorphisms generate $\operatorname{Aut}(B_n)$.
