# __Involutive Rings__

## Introduction

An **involution** of a ring $A$ is an additive map $\sigma : A \to A$ such that

$$
\sigma(ab) = \sigma(b)\sigma(a), \qquad \sigma(1) = 1, \qquad \sigma \circ \sigma = \mathrm{id} :
$$

an anti-automorphism of order two. The definition presupposes no commutativity. An involution is the same datum as a bijection $A \to A^{\mathrm{op}}$ of order two onto the ring with the reversed multiplication, so a ring that carries an involution is a ring isomorphic to its opposite ring, and the involution is the certificate of that isomorphism.

In the commutative case the opposite ring is the ring itself, no reversal is visible, and the anti-multiplicativity of the definition becomes ordinary multiplicativity: an involution of a commutative ring is simply an automorphism of order dividing two. What remains from the involution is then the fixed subring, the two conjugates $x$ and $\sigma(x)$ of an element, and the monic quadratic that every element satisfies over the fixed subring; when the ring is a field the pair is a Galois extension of degree two. The commutative case is therefore not a specialisation of the general theory but a second theory of the same datum, and the two are kept apart below.

The article has three general sections — the definition and the opposite ring, the symmetric and skew elements, and the ideals, quotients, products and $\sigma$-prime notions — and one for the commutative case, where the fixed set is a ring and the conjugates of an element generate a quadratic extension of it; a section of examples and a record of what commutativity adds close it. Throughout, $A$ is a ring with $1 \neq 0$, **not assumed commutative**, $R$ is a commutative ring with $1 \neq 0$, and $\sigma$ is an involution; $A^\sigma$ and $R^\sigma$ are the **fixed sets**, which are additive subgroups containing $1$, and which are subrings exactly when closure under multiplication holds. Ideals in the general part are two-sided unless the contrary is said; the vocabulary of ideals, quotients and the opposite ring is *Rings*, and the commutative results cited are those of *Commutative Rings*.

The article stays inside Algebra. Nothing here is measured: the two conjugates of an element are multiplied and added, and nothing is read off them but the two operations of the ring. The forms that an involution can carry, the classification of the involutions of a central simple algebra, and the notions a form or a pairing defines are *Hermitian Forms and Involutions*, in Part II, and are named in this article only to mark the boundary; no definition or proof below uses them. The involutions of rings of functions and of algebras carrying a topology are Part II and Part III, and are not used here either.

---

## Involutions of a Ring

### Definition

**Definition.** An **involution** of the ring $A$ is a map $\sigma : A \to A$ such that for all $a, b \in A$

$$
\sigma(a+b) = \sigma(a)+\sigma(b), \qquad \sigma(ab) = \sigma(b)\sigma(a), \qquad \sigma(1) = 1, \qquad \sigma(\sigma(a)) = a .
$$

An **involutive ring** is a pair $(A,\sigma)$; the involution is **trivial** when $\sigma = \mathrm{id}_A$. The **fixed set** of $\sigma$ is

$$
A^\sigma = \{ a \in A : \sigma(a) = a \},
$$

and its elements are the **symmetric** elements; an element with $\sigma(a) = -a$ is **skew**. The elements $a$ and $\sigma(a)$ are the two **conjugates** of $a$.

**Definition (morphisms).** A **homomorphism** $(A,\sigma) \to (B,\tau)$ of involutive rings is a unital ring homomorphism $\varphi : A \to B$ with $\varphi \circ \sigma = \tau \circ \varphi$. Two involutions $\sigma, \sigma'$ of the same ring are **equivalent** when $\sigma' = \varphi \sigma \varphi^{-1}$ for a ring automorphism $\varphi$; an automorphism of the involutive ring is a ring automorphism commuting with the involution. In the commutative case the involutions of a ring are the automorphisms of order dividing two, so the classification of involutions is a question about automorphism groups, which is *Ring and Field Automorphisms*.

### The Opposite Ring

**Definition.** The **opposite ring** $A^{\mathrm{op}}$ has the same additive group as $A$ and the multiplication $a \cdot b = ba$.

**Theorem.** The involutions of $A$ are exactly the bijections $\sigma : A \to A$ of order two that are ring isomorphisms $A \to A^{\mathrm{op}}$; in particular a ring that carries an involution is isomorphic to its opposite ring.

**Proof.** An involution is additive and bijective with $\sigma^2 = \mathrm{id}$, and $\sigma(ab) = \sigma(b)\sigma(a)$ says exactly that $\sigma$ is multiplicative as a map into $A^{\mathrm{op}}$. Conversely an isomorphism $\sigma : A \to A^{\mathrm{op}}$ that is a bijection of order two is additive, carries $1$ to $1$, satisfies $\sigma^2 = \mathrm{id}$, and its multiplicativity with respect to the reversed product is the anti-multiplicativity of the definition.

**Corollary.** A ring $A$ is commutative exactly when the identity map is an isomorphism $A \to A^{\mathrm{op}}$. In that case the involutions of $A$ and of $A^{\mathrm{op}}$ are the same maps, and they are the automorphisms of $A$ of order dividing two.

**Proof.** $A = A^{\mathrm{op}}$ means $ab = ba$ for all $a, b$; and when $A$ is commutative the opposite ring is the same ring with the same multiplication, so an isomorphism onto it is an automorphism, and the order-two condition is the only one left.

**Remark.** A ring that carries an involution is isomorphic to its opposite ring, by the theorem. The converse implication is a finer question: an isomorphism $A \to A^{\mathrm{op}}$ need not be of order two, and whether its existence forces the existence of an involution is not automatic. Nothing below depends on that question, and every ring in the examples carries an explicit involution.

### Elementary Properties

**Proposition.** Let $\sigma$ be an involution of the ring $A$.

**(a)** $\sigma(0) = 0$, $\sigma(1) = 1$, $\sigma(-a) = -\sigma(a)$, and $\sigma$ is $\mathbb{Z}$-linear.

**(b)** $\sigma$ is bijective with $\sigma^{-1} = \sigma$, and $\sigma(a^n) = \sigma(a)^n$ for every $n \geq 0$.

**(c)** $\sigma$ carries units to units and restricts to a group automorphism of $A^\times$ of order dividing two, with $\sigma(u)^{-1} = \sigma(u^{-1})$.

**(d)** If $I$ is a two-sided ideal then $\sigma(I)$ is a two-sided ideal, and $I \mapsto \sigma(I)$ is an order automorphism of the lattice of two-sided ideals with $\sigma(I+J) = \sigma(I)+\sigma(J)$, $\sigma(IJ) = \sigma(J)\sigma(I)$, $\sigma(I \cap J) = \sigma(I) \cap \sigma(J)$ and $\sigma(\sqrt{I}) = \sqrt{\sigma(I)}$. A left ideal is carried to a right ideal and conversely. For $\sigma$-ideals $\sigma(IJ) = JI$, so the product of two $\sigma$-ideals is a $\sigma$-ideal exactly when $IJ = JI$; in the commutative case this always holds.

**(e)** A prime ideal $\mathrm{P}$ gives a prime ideal $\sigma(\mathrm{P})$, a maximal ideal $\mathrm{M}$ gives a maximal ideal $\sigma(\mathrm{M})$, and $\mathrm{P} \mapsto \sigma(\mathrm{P})$ is an order automorphism of the spectrum.

**(f)** $\sigma$ permutes the idempotents, the nilpotents and the zero divisors of $A$.

**(g)** The fixed set $A^\sigma$ is an additive subgroup containing $1$ and is closed under $\sigma$; it is closed under multiplication exactly when its elements commute pairwise, and hence it is a subring in the commutative case.

**Proof.** (a) As for a ring homomorphism, with sums in place of products. (b) $\sigma^2 = \mathrm{id}$ makes $\sigma$ its own inverse, and multiplicativity iterates: $\sigma(a^{n}) = \sigma(a)^n$. (c) From $uv = 1$ one gets $\sigma(u)\sigma(v) = \sigma(1) = 1$ and $\sigma(v)\sigma(u) = 1$. (d) $\sigma$ is an isomorphism $A \to A^{\mathrm{op}}$; as such it carries left ideals of $A$ to left ideals of $A^{\mathrm{op}}$, which are the right ideals of $A$, and it is an inclusion-preserving bijection on two-sided ideals. The product formula is $\sigma(IJ) = \sigma(J)\sigma(I)$, because $\sigma$ reverses the order of every product; the formulas for the sum and the intersection are the two instances of $\sigma$ being an isomorphism of the additive lattice, and the radical formula holds because $x^n \in I$ exactly when $\sigma(x)^n \in \sigma(I)$. (e) A ring isomorphism carries primes to primes and preserves inclusion. (f) $\sigma(e)^2 = \sigma(e)$ for an idempotent, $\sigma(x)^n = \sigma(x^n) = 0$ for a nilpotent, and $ab = 0$ gives $\sigma(a)\sigma(b) = 0$. (g) For $x, y \in A^\sigma$ one has $\sigma(xy) = yx$, so $xy$ is fixed exactly when $xy = yx$; in the commutative case that always holds, and in the general case it fails as the symmetric matrices of the next section show.

### Examples

**Example (the identity).** On every ring the identity is an involution, the trivial one, with $A^\sigma = A$.

**Example (the transpose).** On the matrix ring $M_n(R)$ over **any** ring the transpose $X \mapsto X^{T}$ is an involution: $(XY)^{T} = Y^{T}X^{T}$ holds without any commutativity. Its fixed set is the symmetric matrices, and $A^\sigma$ is not closed under multiplication for $n \geq 2$, as the symmetric matrices of the next paragraph show.

**Example (the twisted transpose).** Let $R$ be commutative with an involution $\sigma$. On $M_n(R)$ the map $(a_{ij}) \mapsto (\sigma(a_{ji}))$ is an involution, the transpose composed with the coefficientwise involution.

**Example (group rings).** On the group ring $K[G]$ of a group $G$ over a commutative ring $K$ the map $\sum_g a_g g \mapsto \sum_g a_g g^{-1}$ is an involution, because reindexing a sum over $G$ by $g \mapsto g^{-1}$ is legitimate and $(gh)^{-1} = h^{-1}g^{-1}$. It makes $K[G]$ isomorphic to its opposite ring, and on a group algebra of a finite group it is the involution used throughout the representation theory of that algebra.

**Example (free algebra).** On the free algebra $K\langle x_1, \ldots, x_n\rangle$ over a commutative ring the reversal of words is an involution, since the reverse of a concatenation is the concatenation of the reverses in the opposite order. For $n \geq 2$ it is not an automorphism, because it interchanges the words $x_1x_2$ and $x_2x_1$; the free algebra is thus an example whose involution is genuinely an anti-automorphism, and the words it fixes are the palindromes.

**Example (products).** On a product $A_1 \times A_2$ the componentwise rule $\sigma(a_1,a_2) = (\sigma_1(a_1), \sigma_2(a_2))$ is an involution. On $A \times A$ the **swap** $\varsigma(a_1,a_2) = (a_2,a_1)$ is an involution with fixed set the diagonal, and more generally an **anti-isomorphism** $\tau : A \to B$, that is a bijection with $\tau(ab) = \tau(b)\tau(a)$, gives the involution $(a,b) \mapsto (\tau^{-1}(b), \tau(a))$ of $A \times B$, whose fixed set is the graph of $\tau$. The construction needs $\tau$ anti-multiplicative: with an isomorphism in its place the map still has order two on the underlying set but is not an anti-automorphism unless the two components commute, and the two constructions are of different nature, an involution of a factor being an anti-automorphism while the swap is an automorphism of the product.

**Example (commutative rings).** On $\mathbb{C}$ the conjugation $z \mapsto \bar z$ is an involution with fixed ring $\mathbb{R}$; on $\mathbb{Z}[i]$ the conjugation $a+bi \mapsto a-bi$ has fixed ring $\mathbb{Z}$; and on $\mathbb{R}[x]$ the coefficientwise involution induced by the identity of $\mathbb{R}$ is the identity, the nontrivial involutions of $\mathbb{R}[x]$ being the affine ones of the section on polynomial rings below.

---

## The Symmetric and Skew Elements

### The Additive Decomposition

**Definition.** Let $\sigma$ be an involution of $A$ and let $2$ be invertible in $A$. The **symmetric** and **skew** elements are

$$
\mathrm{Sym}(A,\sigma) = \{a \in A : \sigma(a) = a\} = A^\sigma, \qquad \mathrm{Skew}(A,\sigma) = \{a \in A : \sigma(a) = -a\}.
$$

**Proposition.** Let $2$ be invertible in $A$. For $a \in A$ put $a_+ = \tfrac12(a+\sigma(a))$ and $a_- = \tfrac12(a-\sigma(a))$. Then $a_+$ is symmetric, $a_-$ is skew, and $a = a_+ + a_-$. The sum

$$
A = \mathrm{Sym}(A,\sigma) \oplus \mathrm{Skew}(A,\sigma)
$$

is direct, and the two summands are the eigenspaces of $\sigma$ for the eigenvalues $+1$ and $-1$.

**Proof.** $\sigma(a_+) = \tfrac12(\sigma(a)+\sigma^2(a)) = \tfrac12(\sigma(a)+a) = a_+$ and $\sigma(a_-) = \tfrac12(\sigma(a)-\sigma^2(a)) = \tfrac12(\sigma(a)-a) = -a_-$, both computations using only additivity and $\sigma^2 = \mathrm{id}$, so no commutativity is needed. If $a$ is both symmetric and skew then $a = -a$, so $2a = 0$ and $a = 0$ because $2$ is invertible.

**Remark.** When $2$ is not invertible the two sets meet in $\{a : 2a = 0\}$, and the sum need not be direct; over $\mathbb{F}_2$ they coincide, since $-a = a$ there.

### The Failure of the Grading without Commutativity

In the commutative case the involution makes the ring a $\mathbb{Z}/2\mathbb{Z}$-graded ring, with even part the fixed subring and odd part the skew elements. Without commutativity that structure fails at the first product.

**Proposition.** Let $2$ be invertible in $A$. Then $A^\sigma$ is closed under multiplication exactly when $xy = yx$ for all $x, y \in A^\sigma$, and the product of two skew elements is symmetric exactly when $xy = yx$ for all $x, y \in \mathrm{Skew}(A,\sigma)$.

**Proof.** For $x, y$ fixed, $\sigma(xy) = \sigma(y)\sigma(x) = yx$, so $xy$ is fixed exactly when $xy = yx$. For skew $x, y$ one has $\sigma(xy) = (-y)(-x) = yx$, while $xy$ is skew exactly when $\sigma(xy) = -xy$; the two agree exactly when $xy = yx$.

**Example (a product of two symmetric elements).** In $M_2(F)$ with the transpose, the symmetric elements $x = \begin{pmatrix}1&1\\1&0\end{pmatrix}$ and $y = \begin{pmatrix}0&1\\1&1\end{pmatrix}$ have $xy = \begin{pmatrix}1&2\\0&1\end{pmatrix}$, which is not symmetric; the fixed set is not a subring.

**Example (a product of two skew elements in $M_3$).** Let $A = M_3(F)$ with $2$ invertible in $F$ and $\sigma$ the transpose, and let $a = e_{12}-e_{21}$ and $b = e_{13}-e_{31}$, both skew. Then

$$
ab = (e_{12}-e_{21})(e_{13}-e_{31}) = -e_{23},
$$

which is neither symmetric nor skew. So a product of skew elements can be neither, and the grading of the commutative case has no general analogue.

### The Fixed Set

**Proposition.** The fixed set $A^\sigma$ is an additive subgroup containing $1$ and is closed under $a \mapsto \sigma(a)$. If $2$ is invertible, the **averaging map**

$$
\pi : A \to A, \qquad \pi(a) = \tfrac12(a+\sigma(a)),
$$

is an idempotent endomorphism of the additive group of $A$ with image $\mathrm{Sym}(A,\sigma)$ and kernel $\mathrm{Skew}(A,\sigma)$; it is multiplicative exactly when $\sigma(xy) = \sigma(x)\sigma(y)$ for all $x, y$, that is, exactly when the involution is also a ring homomorphism, which holds for the trivial involution of every ring and for every involution of a commutative ring.

**Proof.** $\pi$ is additive, $\pi(1) = 1$, $\pi^2 = \pi$, and $\pi(a)$ is fixed, so the image is $A^\sigma$; the kernel is the set of $a$ with $a+\sigma(a) = 0$, that is $\mathrm{Skew}(A,\sigma)$. For multiplicativity one would need $\sigma(xy) = \sigma(x)\sigma(y)$, which is the additional requirement that the anti-automorphism be an automorphism.

The **centre** is preserved: $\sigma(Z(A)) = Z(A)$, and $A^\sigma \cap Z(A) = Z(A)^\sigma$ is the fixed subring of the involution of the commutative ring $Z(A)$.

### The Two Conjugate Products

**Definition.** For $a \in A$ the two **conjugate products** and the **conjugate sum** are

$$
a\sigma(a), \qquad \sigma(a)a, \qquad a+\sigma(a).
$$

**Proposition.** Let $\sigma$ be an involution of $A$.

**(a)** $a\sigma(a)$, $\sigma(a)a$ and $a+\sigma(a)$ are symmetric for every $a \in A$, and $a \mapsto a+\sigma(a)$ is additive with $1 \mapsto 2$.

**(b)** $a\sigma(a)$ and $\sigma(a)a$ need not be equal, and the conjugate product is not multiplicative: the general law is

$$
(xy)\sigma(xy) = x\,(y\sigma(y))\,\sigma(x),
$$

which agrees with the multiplicative law $(xy)\sigma(xy) = x\sigma(x)\,y\sigma(y)$ exactly when $\sigma(x)$ commutes with $y\sigma(y)$, and fails to do so in $M_2(F)$ with the transpose for $x = e_{12}$, $y = e_{21}$.

**(c)** The conjugate sums of $xy$ and of $yx$ need not be equal: the first is $xy+\sigma(y)\sigma(x)$ and the second is $yx+\sigma(x)\sigma(y)$.

**(d)** $a^2 - (a+\sigma(a))a + \sigma(a)a = 0$ and $a^2 - a\,(a+\sigma(a)) + a\sigma(a) = 0$; the coefficients of these two quadratics lie in $A^\sigma$, but they need not commute with $a$.

**Proof.** (a) $\sigma(a\sigma(a)) = \sigma(\sigma(a))\sigma(a) = a\sigma(a)$, similarly $\sigma(\sigma(a)a) = \sigma(a)\sigma(\sigma(a)) = \sigma(a)a$, and $\sigma(a+\sigma(a)) = \sigma(a)+a$. (b) Expanding, $(xy)\sigma(xy) = xy\sigma(y)\sigma(x) = x\,(y\sigma(y))\,\sigma(x)$; for $x = e_{12}$ and $y = e_{21}$ in $M_2(F)$ with the transpose one has $(xy)\sigma(xy) = e_{11}e_{11} = e_{11}$, whereas $x\sigma(x)\,y\sigma(y) = e_{11}e_{22} = 0$, so the two sides differ; and for a single element, $\sigma(e_{12})e_{12} = e_{22} \neq e_{11} = e_{12}\sigma(e_{12})$. (c) In the same ring the conjugate sum of $e_{12}e_{21} = e_{11}$ is $2e_{11}$, while that of $e_{21}e_{12} = e_{22}$ is $2e_{22}$. (d) $(a+\sigma(a))a = a^2+\sigma(a)a$, and $a(a+\sigma(a)) = a^2+a\sigma(a)$.

**Remark.** On a commutative ring the two conjugate products coincide, their product relation reads $(xy)\sigma(xy) = x\sigma(x)\,y\sigma(y)$, the two conjugate sums coincide, and the quadratic relation becomes the integrality relation of the commutative part below. Each item of the proposition is thus a precise statement of what commutativity supplies.

---

## Ideals, Quotients and Products

### $\sigma$-Ideals

**Definition.** A two-sided ideal $I$ of $A$ is a **$\sigma$-ideal** (also a **$*$-ideal**) when $\sigma(I) = I$, equivalently $\sigma(I) \subseteq I$. An ideal is a $\sigma$-ideal exactly when it is a union of orbits of the action of $\langle\sigma\rangle$ on $A$.

**Proposition.** The sum, the intersection and the radical of $\sigma$-ideals are $\sigma$-ideals, and the kernel of a homomorphism of involutive rings is a $\sigma$-ideal.

**Proof.** The first part is immediate from the elementary properties of $\sigma$ on ideals; the kernel of a homomorphism $\varphi$ with $\varphi\sigma = \tau\varphi$ satisfies $\sigma(\ker\varphi) = \ker\varphi$ because $\varphi(\sigma(a)) = \tau(\varphi(a))$.

**Remark.** The product is not among them. For $\sigma$-ideals $I, J$ one has $\sigma(IJ) = \sigma(J)\sigma(I) = JI$, so $IJ$ is a $\sigma$-ideal exactly when $IJ = JI$, and in a non-commutative ring that can fail: in the free algebra $K\langle x, y\rangle$ with the reversal involution the ideals $(x)$ and $(y)$ are $\sigma$-ideals, and $(x)(y)$ is the ideal generated by $xy$, whose image under $\sigma$ is the ideal generated by $yx$, a different ideal. In the commutative case $IJ = JI$ always, and the product of $\sigma$-ideals is a $\sigma$-ideal.

### Quotients

**Proposition.** Let $I$ be a $\sigma$-ideal. Then $\sigma$ induces an involution $\bar\sigma$ of the quotient $A/I$ by $\bar\sigma(a+I) = \sigma(a)+I$, and

$$
(A^\sigma + I)/I \subseteq (A/I)^{\bar\sigma} .
$$

The inclusion can be strict: in $\mathbb{Z}[i]$ with the conjugation and $I = (2)$ the quotient has four elements, $-1 \equiv 1$ and $-i \equiv i$ modulo $2$, so $\bar\sigma$ is the identity and $(A/I)^{\bar\sigma}$ has four elements, while the image of the fixed set has two.

**Proof.** The map is well defined because $\sigma(I) \subseteq I$, and its square is the identity. An element of the image, $\sigma(a)+I$ with $\sigma(a) = a$, is fixed; the computation over $\mathbb{Z}[i]$ is the one in the commutative part below.

The **correspondence** of ideals is equivariant: the $\sigma$-ideals of $A$ containing $I$ correspond to the $\sigma$-ideals of $A/I$. Consequently $I$ is a $\sigma$-prime ideal of $A$ exactly when $A/I$ is a $\sigma$-prime ring.

### Products

**Definition.** On a product $\prod_i A_i$ the **componentwise involution** acts by $(\sigma_i)$ on the components; on $A \times A$ the **swap** $\varsigma(a_1,a_2) = (a_2,a_1)$ is an involution, and for an anti-isomorphism $\tau : A \to B$ the map $(a,b) \mapsto (\tau^{-1}(b),\tau(a))$ is an involution of $A \times B$ with fixed set the graph of $\tau$; with an isomorphism in place of the anti-isomorphism the map has order two but is not an anti-automorphism in general.

**Proposition.** For the swap involution on $A \times A$ the $\sigma$-ideals are exactly the $I \times I$ with $I$ an ideal of $A$, and the $\sigma$-prime ideals are exactly the $\mathrm{P} \times \mathrm{P}$ with $\mathrm{P}$ prime; hence $A \times A$ with the swap involution is a $\sigma$-prime ring exactly when $A$ is a prime ring.

**Proof.** An ideal of a product of unital rings is a product of ideals, $I_1 \times I_2$, and the swap carries it to $I_2 \times I_1$, so it is a $\sigma$-ideal exactly when $I_1 = I_2$. For the $\sigma$-prime condition, $(I \times I)(J \times J) = IJ \times IJ$ is contained in $\mathrm{P} \times \mathrm{P}$ exactly when $IJ \subseteq \mathrm{P}$, and $I \times I \subseteq \mathrm{P} \times \mathrm{P}$ is equivalent to $I \subseteq \mathrm{P}$; so the condition on $A$ is the defining condition of a prime ideal. The last statement is the case $I = J = (0)$.

### $\sigma$-Prime Ideals and $\sigma$-Prime Rings

**Definition.** A proper $\sigma$-ideal $\mathrm{P}$ is **$\sigma$-prime** when for $\sigma$-ideals $I, J$ the inclusion $IJ \subseteq \mathrm{P}$ forces $I \subseteq \mathrm{P}$ or $J \subseteq \mathrm{P}$. A ring is **$\sigma$-prime** (or **$*$-prime**) when its zero ideal is $\sigma$-prime, that is when $IJ \neq 0$ for all nonzero $\sigma$-ideals $I, J$.

**Proposition.** Every prime $\sigma$-ideal is $\sigma$-prime.

**Proof.** If $\mathrm{P}$ is prime and $\sigma$-ideals $I, J$ satisfy $IJ \subseteq \mathrm{P}$ with $J \nsubseteq \mathrm{P}$, choose $b \in J \setminus \mathrm{P}$; for $a \in I$ the product $ab$ lies in $\mathrm{P}$, and $b \notin \mathrm{P}$ gives $a \in \mathrm{P}$. Hence $I \subseteq \mathrm{P}$.

**Proposition (sufficient condition).** If $aAb^{*} \neq 0$ for all nonzero $a, b \in A$, then $A$ is $\sigma$-prime.

**Proof.** Let $I, J$ be nonzero $\sigma$-ideals with $IJ = 0$ and choose $a \in I$, $b \in J$ nonzero. Since $J$ is a $\sigma$-ideal, $b^{*} = \sigma(b) \in J$, and $b^{*}A \subseteq J$; hence $aAb^{*} \subseteq IJ = 0$, contradicting the hypothesis.

**Remark.** The condition is sufficient and not necessary, so it does not characterise the $\sigma$-prime rings, and the definition by $\sigma$-ideals is the correct one. In $A = M_n(F) \times M_n(F)$ with the swap involution of the next example the ring is $\sigma$-prime, its only nonzero $\sigma$-ideal being $A$, and yet $a = (e_{11}, 0)$ and $b = (e_{12}, 0)$ give $b^{*} = (0, e_{12})$ and $aAb^{*} = 0$; the two elements sit in opposite components, and no product $axb^{*}$ can meet them. A prime ring, by contrast, does satisfy the analogous condition with $b$ in place of $b^{*}$: if $a$ and $b$ are nonzero, the two-sided ideals they generate are nonzero, so their product is nonzero, and some $axb$ is nonzero. Hence every prime ring is $\sigma$-prime, because the zero ideal of a prime ring is prime and every prime $\sigma$-ideal is $\sigma$-prime.

**Example ($\sigma$-prime without prime).** Let $A = M_n(F) \times M_n(F)$ with the swap involution, $n \geq 1$. By the proposition on products the ring is $\sigma$-prime because $M_n(F)$ is prime, while it is not prime, since the nonzero ideals $M_n(F) \times (0)$ and $(0) \times M_n(F)$ have zero product.

**Example ($\sigma$-prime ideal without prime ideal).** In $\mathbb{C}[x]$ with the coefficientwise conjugation $\sigma$, the ideal $(x^2+1)$ is $\sigma$-prime and not prime. Every ideal is principal. The ideal $(f)$ is a $\sigma$-ideal exactly when $f$ and $\sigma(f)$ are associates, and $\sigma(f)(z) = \overline{f(\bar z)}$, so in that case $f(z) = 0$ if and only if $f(\bar z) = 0$, with the same multiplicity: the root multiset of a generator of a $\sigma$-ideal is conjugation-stable with equal multiplicities. Now let $(f)$ and $(g)$ be $\sigma$-ideals with $(f)(g) \subseteq (x^2+1)$, that is $x^2+1 \mid fg$. Because $f$ is the generator of a $\sigma$-ideal, either both $i$ and $-i$ are roots of $f$, in which case $x^2+1 \mid f$, or neither is a root of $f$, in which case $x^2+1 \mid fg$ forces $(x-i) \mid g$ and $(x+i) \mid g$, hence $x^2+1 \mid g$ because the two linear factors are coprime in the unique factorisation domain $\mathbb{C}[x]$. So $(f) \subseteq (x^2+1)$ or $(g) \subseteq (x^2+1)$, and $(x^2+1)$ is $\sigma$-prime. It is not prime, since $x^2+1 = (x-i)(x+i)$ exhibits a product in the ideal with neither factor in it, and the factors $(x-i)$ and $(x+i)$ are themselves interchanged by $\sigma$, so neither is a $\sigma$-ideal and no $\sigma$-prime condition is violated by them. So the passage from prime to $\sigma$-prime is a genuine weakening, measured by the conjugate pair of roots $i$ and $-i$ in a quadratic factor.

---

## The Commutative Case

### Involutions as Automorphisms

From here $R$ is a **commutative ring with identity** $1 \neq 0$ and $\sigma$ is an involution. Because $R = R^{\mathrm{op}}$, the anti-multiplicativity of the definition is the equation $\sigma(ab) = \sigma(a)\sigma(b)$ itself, so $\sigma$ is an automorphism of $R$ of order dividing two, the fixed set $R^\sigma$ is a **subring**, and the grading of the next section is available. Everything in the general part applies: $\mathrm{Sym}(R,\sigma) = R^\sigma$ and $\mathrm{Skew}(R,\sigma) = R^-$.

### The Fixed Subring and the Symmetric–Skew Decomposition

**Proposition.** Let $2$ be invertible in $R$. For $a \in R$ put $a_+ = \tfrac12(a+\sigma(a))$ and $a_- = \tfrac12(a-\sigma(a))$. Then $a_+ \in R^\sigma$, $\sigma(a_-) = -a_-$, $a = a_+ + a_-$, and the sum

$$
R = R^\sigma \oplus R^-
$$

with $R^- = \{a \in R : \sigma(a) = -a\}$ is direct.

**Proof.** The general computation of the symmetric and skew elements plus the fact that $\sigma$ is multiplicative, which makes $a_+$ and $a_-$ fixed-ring elements of the stated kinds.

**Proposition (multiplication).** $R^\sigma R^\sigma \subseteq R^\sigma$, $R^\sigma R^- \subseteq R^-$ and $R^-R^- \subseteq R^\sigma$.

**Proof.** Multiplicativity of the automorphism $\sigma$: for $x, y \in R^-$ one has $\sigma(xy) = \sigma(x)\sigma(y) = (-x)(-y) = xy$, and the other two are immediate.

So the involution makes $R$ a **$\mathbb{Z}/2\mathbb{Z}$-graded ring**, with even part the fixed subring and odd part the skew elements.

**Remark (the hypothesis is needed).** In $\mathbb{F}_2[x]$ the map $\sigma(x) = x+1$ is an involution by the affine criterion below, and $-f = f$ there, so $R^- = R^\sigma$; hence $R^\sigma + R^- = R^\sigma \neq R$ and there is no eigenspace decomposition.

### The Conjugates and the Quadratic Relation

**Definition.** For $x \in R$ the **conjugate product** and the **conjugate sum** are

$$
x\,\sigma(x), \qquad x + \sigma(x) .
$$

**Proposition.** Let $\sigma$ be an involution of the commutative ring $R$.

**(a)** $x\sigma(x) \in R^\sigma$ and $x+\sigma(x) \in R^\sigma$ for every $x \in R$.

**(b)** The map $x \mapsto x\sigma(x)$ is multiplicative, $(xy)\sigma(xy) = x\sigma(x)\,y\sigma(y)$, and it fixes $1$; it is unchanged when $x$ is replaced by $\sigma(x)$, that is $\sigma(x)\sigma(\sigma(x)) = x\sigma(x)$. Hence it carries units of $R$ to units of $R^\sigma$, and $R^\times$ maps into $(R^\sigma)^\times$.

**(c)** The map $x \mapsto x+\sigma(x)$ is additive, fixes $\sigma(x)$ as well as $x$, and satisfies $x+\sigma(x) = y+\sigma(y)$ for conjugate arguments.

**(d)** For $r \in R^\sigma$ one has $(rx)\sigma(rx) = r^2\,x\sigma(x)$ and $rx+\sigma(rx) = r\,(x+\sigma(x))$.

**(e)** $\sigma(x) = (x+\sigma(x))-x$, and $x$ satisfies the monic quadratic

$$
X^2 - (x+\sigma(x))\,X + x\sigma(x) = 0
$$

with coefficients in $R^\sigma$.

**(f)** The square of the skew element $x-\sigma(x)$ is fixed:

$$
(x-\sigma(x))^2 = (x+\sigma(x))^2 - 4\,x\sigma(x) \in R^\sigma .
$$

**Proof.** (a) $\sigma(x\sigma(x)) = \sigma(x)\sigma^2(x) = \sigma(x)x = x\sigma(x)$ by commutativity, and $\sigma(x+\sigma(x)) = \sigma(x)+x$. (b) $(xy)\sigma(xy) = xy\sigma(x)\sigma(y) = x\sigma(x)y\sigma(y)$ by commutativity, and $\sigma(1)\sigma(1) = 1$; a unit $u$ has conjugate product $u\sigma(u)$ with inverse $u^{-1}\sigma(u)^{-1}$, and the product is fixed by (a). (c) Additivity is immediate and $\sigma(x+\sigma(x)) = x+\sigma(x)$. (d) For $r \in R^\sigma$, $\sigma(rx) = r\sigma(x)$, so $(rx)\sigma(rx) = rx\cdot r\sigma(x) = r^2x\sigma(x)$ and $rx+\sigma(rx) = r(x+\sigma(x))$. (e) Substitution. (f) Expanding, $(x+\sigma(x))^2-4x\sigma(x) = x^2-2x\sigma(x)+\sigma(x)^2 = (x-\sigma(x))^2$, which is fixed by $\sigma$ because $\sigma(x-\sigma(x)) = \sigma(x)-x = -(x-\sigma(x))$.

**Theorem (integrality over the fixed subring).** Every element $x$ of $R$ satisfies a monic quadratic equation with coefficients in $R^\sigma$, namely the one displayed in (e). Consequently $R$ is integral over $R^\sigma$, and the subring generated by $x$ over $R^\sigma$ is generated by $1$ and $x$. No hypothesis on $2$ is used.

**Proof.** The quadratic has its coefficients in $R^\sigma$ by (a); a monic quadratic relation is integrality of degree at most two, and the development of integral extensions and their prime spectra is *Integral Extensions and Krull Dimension*, later in this category.

**Remark.** The quadratic is not minimal when $x \in R^\sigma$, where it reduces to $(X-x)^2$. It is the minimal polynomial exactly when $x \notin R^\sigma$ and $R$ is a domain: there $x\sigma(x)$ is nonzero for $x \neq 0$, since $\sigma$ is injective, so an element outside $R^\sigma$ has degree exactly two over $R^\sigma$. Off a domain the quadratic can be reducible although $x \notin R^\sigma$.

### Polynomial Rings

**Proposition.** Let $\sigma$ be an involution of $R$ and let $f^\sigma$ denote the polynomial obtained from $f$ by applying $\sigma$ to its coefficients. There is a unique ring endomorphism $\tilde\sigma_f$ of $R[x]$ with $\tilde\sigma_f|_R = \sigma$ and $\tilde\sigma_f(x) = f(x)$, and it is an involution exactly when

$$
f^\sigma\bigl(f(x)\bigr) = x .
$$

In the **affine** case $f(x) = ax+b$ the conditions are $a\sigma(a) = 1$ and $\sigma(a)b+\sigma(b) = 0$.

**Proof.** $R[x]$ is generated as a ring by $R$ together with $x$, so a ring endomorphism is determined by its values on $R$ and on $x$ and these are arbitrary; the map $\tilde\sigma_f$ that extends $\sigma$ and sends $x$ to $f(x)$ is therefore unique. Its square fixes $R$ and takes $x$ to $\tilde\sigma_f(f(x)) = f^\sigma(f(x))$, since $\tilde\sigma_f$ applies $\sigma$ to coefficients and substitutes $f$ for $x$; so the square is the identity exactly when that value is $x$. In the affine case $f^\sigma(f(x)) = \sigma(a)ax+\sigma(a)b+\sigma(b)$, which equals $x$ exactly under the two conditions.

**Example.** On $\mathbb{C}[x]$ with the coefficientwise conjugation the translations $x \mapsto x+b$ are involutions exactly when $b+\bar b = 0$, that is when $b$ is purely imaginary, since then $a = 1$ satisfies $a\bar a = 1$ and $\bar b+b = 0$. On $\mathbb{Z}[i][x]$ with the coefficientwise conjugation the substitution $x \mapsto ix$ is an involution, since $i\bar i = 1$ and $b = 0$.

**Proposition (fixed subrings).** Let $\sigma$ be an involution of $R$ and write $R^- = \{a : \sigma(a) = -a\}$.

**(a)** The coefficientwise extension of $\sigma$ to $R[x]$ is an involution with fixed subring $R^\sigma[x]$.

**(b)** The involution $x \mapsto -x$ with coefficients acted on by $\sigma$ has fixed subring $R^\sigma[x^2] + R^-x$, a direct sum of abelian groups.

**Proof.** (a) A polynomial is fixed coefficientwise exactly when every coefficient is fixed. (b) The extension is $\tilde\sigma(\sum_k a_kx^k) = \sum_k\sigma(a_k)(-x)^k$, so the fixed polynomials are those with $a_k \in R^\sigma$ for even $k$ and $a_k \in R^-$ for odd $k$, and the sum is direct on the monomials.

### Localization and the Fraction Field

**Definition.** A multiplicative set $S \subseteq R$ with $1 \in S$ is **$\sigma$-stable** when $\sigma(S) = S$, and its fixed part is $S^\sigma = S \cap R^\sigma$.

**Theorem.** Let $S$ be a $\sigma$-stable multiplicative set. Then $\sigma$ extends to an involution $\tilde\sigma$ of the localization $S^{-1}R$ by $\tilde\sigma(r/s) = \sigma(r)/\sigma(s)$, and

$$
(S^{-1}R)^{\tilde\sigma} = (S^\sigma)^{-1}R^\sigma ,
$$

the localization of the fixed subring at the fixed part of $S$, identified with its image in $S^{-1}R$.

**Proof.** If $r/s = r'/s'$ there is $t \in S$ with $t(rs'-r's) = 0$, and applying $\sigma$ gives $\sigma(t)(\sigma(r)\sigma(s')-\sigma(r')\sigma(s)) = 0$ with $\sigma(t) \in S$, so $\tilde\sigma$ is well defined; it is an involution because $\sigma$ is. For the fixed ring, let $x = r/s$ satisfy $\sigma(x) = x$, so that $t(\sigma(r)s-r\sigma(s)) = 0$ for some $t \in S$. Put

$$
b = s\,\sigma(s)\,t\,\sigma(t), \qquad a = r\,\sigma(s)\,\sigma(t)\,t .
$$

Then $b \in S^\sigma$, since $\sigma(b) = \sigma(s)s\sigma(t)t = b$ by commutativity, and $a \in R^\sigma$, since $\sigma(a) = \sigma(r)s t\sigma(t) = t\sigma(r)s\sigma(t) = tr\sigma(s)\sigma(t) = a$, the identity $t(\sigma(r)s-r\sigma(s)) = 0$ being used in the middle. Moreover $a/b = r/s$, so $x \in (S^\sigma)^{-1}R^\sigma$. The reverse inclusion is clear, an element of $(S^\sigma)^{-1}R^\sigma$ being fixed because both its numerator and its denominator are.

**Corollary.** Let $\mathrm{P}$ be a $\sigma$-stable prime and $S = R\setminus\mathrm{P}$, which is $\sigma$-stable. Then $R_\mathrm{P}$ carries the induced involution and $(R_\mathrm{P})^{\tilde\sigma} = (R^\sigma)_{\mathrm{P}\cap R^\sigma}$.

**Corollary.** Let $R$ be an integral domain with involution $\sigma$, and let $\sigma$ act on the fraction field by $\sigma(a/b) = \sigma(a)/\sigma(b)$. Then

$$
\operatorname{Frac}(R)^\sigma = \operatorname{Frac}(R^\sigma) .
$$

**Proof.** Take $S = R\setminus\{0\}$, which is $\sigma$-stable with fixed part $R^\sigma\setminus\{0\}$, and apply the theorem.

### Fields with Involution

**Theorem.** Let $F$ be a field with an involution $\sigma$. If $\sigma = \mathrm{id}$ then $F^\sigma = F$. If $\sigma \neq \mathrm{id}$ then $F^\sigma$ is a proper subfield, $[F:F^\sigma] = 2$, the extension is Galois with group $\{\mathrm{id},\sigma\}$, and for $\alpha \in F\setminus F^\sigma$ the minimal polynomial is

$$
X^2 - (\alpha+\sigma(\alpha))X + \alpha\sigma(\alpha),
$$

so $F = F^\sigma(\alpha)$.

**Proof.** The fixed field is proper exactly because $\sigma \neq \mathrm{id}$. Artin's theorem, of *Galois Theory*, gives $[F:F^\sigma] \leq |\langle\sigma\rangle| = 2$ with equality because the extension is proper, and identifies the Galois group. For $\alpha \notin F^\sigma$ the quadratic relation gives degree at most two over $F^\sigma$, and $\alpha \notin F^\sigma$ gives degree at least two, so that quadratic is the minimal polynomial.

**Theorem (the two characteristics).** Let $F$ be a field with $\sigma \neq \mathrm{id}$ and let $\alpha \in F\setminus F^\sigma$.

**(a)** If $\operatorname{char}F \neq 2$ then $\delta = \alpha-\sigma(\alpha)$ is nonzero and skew, with

$$
\delta^2 = (\alpha+\sigma(\alpha))^2 - 4\,\alpha\sigma(\alpha) \in F^\sigma ;
$$

hence $F = F^\sigma(\delta)$ is obtained by adjoining a square root of an element of $F^\sigma$, and the quadratic extensions of $F^\sigma$ are classified by the quotient $F^{\sigma\times}/(F^{\sigma\times})^2$, the exponent-two case of *Kummer Theory*, later in this category.

**(b)** If $\operatorname{char}F = 2$ then $\alpha+\sigma(\alpha) \neq 0$ and $\beta = \alpha/(\alpha+\sigma(\alpha))$ satisfies

$$
\beta^2+\beta = \frac{\alpha\sigma(\alpha)}{(\alpha+\sigma(\alpha))^2} \in F^\sigma ,
$$

the Artin–Schreier equation of a quadratic Galois extension.

**Proof.** (a) $\alpha \notin F^\sigma$ makes $\delta \neq 0$, $\sigma(\delta) = -\delta$, and $\delta^2 = (\alpha-\sigma(\alpha))^2$ is fixed by the previous section. (b) In characteristic two $-a = a$, so $\alpha+\sigma(\alpha) \neq 0$ exactly when $\alpha \notin F^\sigma$; dividing $\alpha^2+(\alpha+\sigma(\alpha))\alpha+\alpha\sigma(\alpha) = 0$ by $(\alpha+\sigma(\alpha))^2$ and substituting $\beta = \alpha/(\alpha+\sigma(\alpha))$ gives the equation.

**Example.** For $\mathbb{C}/\mathbb{R}$ the involution is the conjugation, $\alpha\sigma(\alpha) = \alpha\bar\alpha$ is the product of the two conjugates, $\alpha+\sigma(\alpha) = 2\operatorname{Re}\alpha$, and part (a) applies with $\delta = \alpha-\bar\alpha = 2i\operatorname{Im}\alpha$. For $\mathbb{F}_{q^2}/\mathbb{F}_q$ the involution is the Frobenius $x \mapsto x^q$, whose conjugate product and conjugate sum are $x^{q+1}$ and $x+x^q$; the applicable part is (b) in characteristic two and (a) otherwise. This is the case used in *Finite Fields*, later in this category.

### Involutions and Orderings

**Theorem.** An ordered field has no order-preserving involution other than the identity.

**Proof.** Let $P$ be the positive cone and let $\sigma$ preserve it, so $\sigma(P) = P$. If $\sigma \neq \mathrm{id}$, choose $x$ with $\sigma(x) \neq x$; one of $x-\sigma(x)$ and $\sigma(x)-x$ lies in $P$. If $x-\sigma(x) \in P$, applying $\sigma$ gives $\sigma(x)-x \in P$, and $P \cap (-P) = \{0\}$ forces $x = \sigma(x)$, a contradiction; the other case is symmetric.

**Proposition.** Let $F$ be formally real with an involution $\sigma$. Then $F^\sigma$ is formally real, and any ordering of $F$ restricts to an ordering of $F^\sigma$.

**Proof.** A subfield of an ordered field is ordered by restriction and a subfield of a formally real field is formally real; the theory is *Ordered Fields*, later in this category. The relation of the involutions of a formally real field to the real spectrum is part of *Real Algebraic Geometry* and is not developed here.

---

## Examples

### A Table of Involutions

| $A$ | $\sigma$ | Symmetric | Skew |
|---|---|---|---|
| any $A$ | $\mathrm{id}$ | $A$ | $(0)$ |
| $M_n(R)$, any $R$ | transpose | symmetric matrices | skew-symmetric matrices, $2$ invertible |
| $M_n(R)$, $R$ commutative | $(a_{ij}) \mapsto (\sigma(a_{ji}))$ | the $\sigma$-symmetric matrices | the $\sigma$-skew-symmetric matrices |
| $K[G]$ | $\sum a_g g \mapsto \sum a_g g^{-1}$ | those with $a_g = a_{g^{-1}}$ | those with $a_g = -a_{g^{-1}}$ |
| $K\langle x_1,\ldots,x_n\rangle$ | word reversal | those with $a_w = a_{\mathrm{rev}(w)}$ | those with $a_w = -a_{\mathrm{rev}(w)}$ |
| $A \times A$ | swap | the diagonal | the anti-diagonal |

**Remark.** The swap row differs in kind from the others: the swap is an automorphism of $A \times A$, not an anti-automorphism, so its fixed set, the diagonal, is always a subring. What the swap makes visible is the $\sigma$-prime structure: its $\sigma$-ideals are the $I \times I$, and the ring is $\sigma$-prime exactly when $A$ is prime, so $M_n(F) \times M_n(F)$ with the swap is $\sigma$-prime and not prime. The failure of $A^\sigma$ to be a subring and the failure of the grading are phenomena of a genuine anti-automorphism, such as the transpose of the second row.

### The Fixed Ring and the Divisibility Chain

**Example (the fixed ring of a unique factorisation domain need not be one).** Let $k$ be a field, let $R = k[x,y]$ and let $\sigma(x) = -x$, $\sigma(y) = -y$. Then $\sigma$ reverses every monomial of odd total degree, so

$$
R^\sigma = k[x^2, xy, y^2] = k[u,v,w]/(uw-v^2), \qquad u = x^2,\ v = xy,\ w = y^2 .
$$

In $R^\sigma$ the three elements $u, v, w$ are irreducible and pairwise non-associate, and $v^2 = uw$ are two inequivalent factorisations into irreducibles; hence $R^\sigma$ is not a unique factorisation domain although $R = k[x,y]$ is one. The verification is the following. The ring is the subring $k[s^2, st, t^2]$ of $k[s,t]$, whose monomials are exactly the $s^at^b$ with $a \equiv b \pmod 2$, and whose units are $k^\times$. If $u = s^2 = fg$ in $R^\sigma$ then $f = cs^i$ and $g = c's^{2-i}$ in the unique factorisation domain $k[s,t]$, and $s^i \in k[s^2,st,t^2]$ only for $i$ even, so one of $f, g$ is a unit; thus $u$ is irreducible, and $w = t^2$ likewise. If $v = st = fg$ in $R^\sigma$ then $f = cs^it^j$ with $i, j \in \{0,1\}$ and $f \in R^\sigma$ only for $(i,j) = (0,0)$ or $(1,1)$, so $f$ is a unit or an associate of $v$; thus $v$ is irreducible. The three are non-associate because their monomial supports differ.

**Example (the failure in the other direction).** In $R = \mathbb{Z}[\sqrt{-5}]$ with the conjugation the fixed ring is $R^\sigma = \mathbb{Z}$, a unique factorisation domain, while $R$ is not one, since $6 = 2\cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ are two inequivalent factorisations into irreducibles. The fixed ring neither preserves nor reflects unique factorisation, and the divisibility rungs of *Unique Factorisation Domains*, *Principal Ideal Domains* and *Euclidean Domains*, below this article in this category, are therefore not inherited by a fixed subring of an involution.

---

## What Commutativity Adds

Each item is a statement of the general part that fails without commutativity, with its commutative repair.

**A. The anti-automorphism condition.** In the general case $\sigma(ab) = \sigma(b)\sigma(a)$ is a genuine constraint, and the involutions of a ring are a finer datum than its automorphisms; in the commutative case the two orders of the factors agree and $\sigma$ is an automorphism of order dividing two, so a commutative involution is nothing but an automorphism of order at most two.

**B. The fixed set is a subring.** $A^\sigma$ is closed under multiplication exactly when its elements commute pairwise; $R^\sigma$ is always a subring.

**C. The $\mathbb{Z}/2\mathbb{Z}$-grading.** The product of two skew elements is symmetric in the commutative case and fails in $M_3(F)$ with the transpose, where the product of $e_{12}-e_{21}$ and $e_{13}-e_{31}$ is $-e_{23}$, neither symmetric nor skew.

**D. The two conjugate products.** $x\sigma(x)$ and $\sigma(x)x$ coincide on a commutative ring; in $M_2(F)$ with the transpose they are $e_{11}$ and $e_{22}$ for $x = e_{12}$.

**E. Multiplicativity of the conjugate product.** $(xy)\sigma(xy) = x\sigma(x)\,y\sigma(y)$ holds in the commutative case; in general $(xy)\sigma(xy) = x\,(y\sigma(y))\,\sigma(x)$, and in $M_2(F)$ with the transpose $x = e_{12}$, $y = e_{21}$ the two sides are $e_{11}$ and $0$.

**F. Symmetry of the conjugate sum.** $xy+\sigma(xy) = yx+\sigma(yx)$ holds in the commutative case; in general the two are $xy+\sigma(y)\sigma(x)$ and $yx+\sigma(x)\sigma(y)$, unequal for $x = e_{12}$, $y = e_{21}$ in $M_2(F)$ with the transpose.

**G. Integrality.** The quadratic $X^2-(x+\sigma(x))X+x\sigma(x)$ has coefficients in $R^\sigma$ and makes $R$ integral over $R^\sigma$; in the general case the quadratic relation $a^2-(a+\sigma(a))a+\sigma(a)a = 0$ also has coefficients in $A^\sigma$, but $A^\sigma$ need not be central and no integrality statement follows.

**H. Galois theory.** For a commutative ring the fixed subring of a finite group of automorphisms is the Galois theory of commutative rings; the field case and the degree-two case are the ones used here, and the general theory, with its further hypotheses, belongs to *Galois Theory*, later in this category.

**I. Where the measured notions live.** A form, the pairing a form defines, and the involutions classified by such a pairing are *Hermitian Forms and Involutions*, in Part II. Nothing of this article is measured: the conjugate product and the conjugate sum are the ring's own product and sum taken on the two conjugates, and no length, sign or size is read off them. This is the boundary the article respects, and it is why the classification of the involutions of a central simple algebra is named only in the introduction.

---

## Summary

An involution is an anti-automorphism of order two; the definition needs no commutativity, and it is the same datum as a bijection $A \to A^{\mathrm{op}}$ of order two, so a ring with an involution is isomorphic to its opposite ring. The opposite ring of a commutative ring is the ring itself, and there the involution is an automorphism of order dividing two, so the commutative case is a second theory of the same datum and not a specialisation of the general one.

In general the fixed set $A^\sigma$ is an additive subgroup containing $1$ and closed under the involution, and it is a subring exactly when its elements commute pairwise; the symmetric and skew elements are the eigenspaces of $\sigma$ when $2$ is invertible, with $A = \mathrm{Sym} \oplus \mathrm{Skew}$, but the product of two skew elements need not be symmetric, and in $M_3$ with the transpose it is neither symmetric nor skew. The conjugate products $x\sigma(x)$ and $\sigma(x)x$ are symmetric but differ in general, the multiplicative law is $(xy)\sigma(xy) = x\,(y\sigma(y))\,\sigma(x)$, the conjugate sum satisfies $xy+\sigma(y)\sigma(x)$ with no symmetry, and the quadratic relation $a^2-(a+\sigma(a))a+\sigma(a)a = 0$ has coefficients in $A^\sigma$ but gives no integrality because $A^\sigma$ need not be central. A $\sigma$-ideal is an ideal with $\sigma(I) = I$; the $\sigma$-prime ideals are those for which a product of $\sigma$-ideals inside forces a factor inside, every prime $\sigma$-ideal is $\sigma$-prime, the condition $aAb^{*} \neq 0$ is a sufficient elementwise criterion for $\sigma$-primality but not a characterisation, and the converse of the ideal-theoretic implication fails: $M_n(F) \times M_n(F)$ with the swap involution is $\sigma$-prime and not prime, and $(x^2+1)$ in $\mathbb{C}[x]$ with the coefficientwise conjugation is a $\sigma$-prime ideal that is not prime. An involution passes to a quotient by a $\sigma$-ideal, where the fixed set of the quotient can be strictly larger than the image of the fixed set, and to a product, where the swap makes the $\sigma$-ideals the $I \times I$.

In the commutative case the fixed set is the subring $R^\sigma$, the ring is $\mathbb{Z}/2\mathbb{Z}$-graded by the eigenspaces when $2$ is invertible, and the conjugate product is multiplicative and the conjugate sum is symmetric, so that every element satisfies the monic quadratic $X^2-(x+\sigma(x))X+x\sigma(x)=0$ with coefficients in $R^\sigma$ and $R$ is integral over $R^\sigma$; the square $(x-\sigma(x))^2$ is a fixed element. Affine involutions of $R[x]$ are classified by $a\sigma(a) = 1$ and $\sigma(a)b+\sigma(b) = 0$, with fixed subrings $R^\sigma[x]$ and $R^\sigma[x^2]+R^-x$ for the two basic cases; an involution on a $\sigma$-stable localization has fixed subring the localization of the fixed subring, and $\operatorname{Frac}(R)^\sigma = \operatorname{Frac}(R^\sigma)$ for a domain. A field with a nontrivial involution is a quadratic Galois extension of its fixed field, quadratic in characteristic not two and Artin–Schreier in characteristic two, and no nontrivial involution of an ordered field preserves the order. The fixed subring is not a rung of the divisibility chain: $k[x^2,xy,y^2]$ is not a unique factorisation domain although $k[x,y]$ is, and $\mathbb{Z}[\sqrt{-5}]$ is not one although its fixed ring $\mathbb{Z}$ is.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(A,\sigma)$ | Involutive ring; $A$ a ring with $1 \neq 0$, $\sigma$ an involution |
| $A^{\mathrm{op}}$ | Opposite ring, same additive group with $a \cdot b = ba$ |
| $A^\sigma$ | Fixed set $\{a : \sigma(a) = a\}$; a subring in the commutative case |
| $\mathrm{Sym}(A,\sigma)$, $\mathrm{Skew}(A,\sigma)$ | Symmetric and skew elements, the eigenspaces of $\sigma$ |
| $a_+, a_-$ | $\tfrac12(a+\sigma(a))$ and $\tfrac12(a-\sigma(a))$ |
| $a\sigma(a)$, $\sigma(a)a$ | The two conjugate products; equal on a commutative ring |
| $a+\sigma(a)$ | The conjugate sum of $a$ |
| $\sigma$-ideal | Ideal $I$ with $\sigma(I) = I$ |
| $\sigma$-prime ideal | Proper $\sigma$-ideal with $IJ \subseteq \mathrm{P}$ forcing $I \subseteq \mathrm{P}$ or $J \subseteq \mathrm{P}$ for $\sigma$-ideals |
| $\sigma$-prime ring | Ring whose zero ideal is $\sigma$-prime; the condition $aAb^{*} \neq 0$ is sufficient for it |
| $R$, $R^\sigma$, $R^-$ | Commutative ring with involution, fixed subring, skew part |
| $x\sigma(x)$, $x+\sigma(x)$ | Conjugate product and conjugate sum in the commutative case |
| $F^\sigma$, $[F:F^\sigma]$ | Fixed field of a field with involution, of degree two when $\sigma \neq \mathrm{id}$ |
| $S^\sigma$ | Fixed part $S \cap R^\sigma$ of a $\sigma$-stable multiplicative set |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the general theory, the fixed set, and the $\sigma$-prime ideals and $\sigma$-prime rings.
- Louis H. Rowen, *Ring Theory*, Volume I (Academic Press, 1988), for rings with involution, their ideals and their quotients.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for involutions of rings and algebras and their fixed subrings.
- Stephen U. Chase, David K. Harrison and Alex Rosenberg, *Galois Theory and Galois Cohomology of Commutative Rings* (Memoirs of the AMS 52, 1965), for the fixed subring of a group action on a commutative ring.
- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the ideal theory, quotients, localization and the spectrum used in the commutative case.
