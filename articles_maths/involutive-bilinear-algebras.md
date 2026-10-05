# __Involutive Bilinear Algebras__

## Introduction

An **involution** of an algebra $A$ over a field $F$ is an $F$-linear map $\sigma : A \to A$ of order two that reverses the product,

$$
\sigma(ab) = \sigma(b)\sigma(a), \qquad \sigma(1) = 1, \qquad \sigma \circ \sigma = \mathrm{id} :
$$

an anti-automorphism of order two, the same map as in *Involutive Rings*, now read together with the scalars and the product that the algebra carries. Two kinds of order-two map live on an algebra, and they must not be confused. The **involution** reverses the product, and an **involutive automorphism** preserves it; on a commutative algebra the two are the same maps, on a non-commutative algebra they are not, and every statement about fixed elements must therefore say which map it is about. The involution is the notion of this article; the involutive automorphism is the second notion that the product makes possible.

The product contributes two structures that a linear space cannot carry. The **skew** elements, the elements with $\sigma(x) = -x$, are closed under the commutator $[x,y] = xy - yx$, so they form a Lie algebra; the **symmetric** elements, the elements with $\sigma(x) = x$, are closed under the symmetrised product $x \bullet y = \tfrac12(xy + yx)$, so they form a Jordan algebra. The fixed set of an involution is therefore always a Jordan algebra, and it is an algebra exactly when its elements commute among themselves: when $A$ is commutative it is a subalgebra, and when $A$ is not it may still be one — the diagonal matrices inside the upper triangular ones are the instance below — but it need not be. For an involutive automorphism the fixed set is always a subalgebra and the whole algebra is $\mathbb{Z}/2$-graded, so the grading is the property that an anti-automorphism fails to have, and the product of a symmetric and a skew element is skew only when the two commute. The contrast between the two kinds of order-two map is one of the subjects below.

The scalars contribute a third. An involution of the $F$-algebra $A$ may be $F$-linear, or it may be twisted by an involution $\varsigma$ of $F$ so that $\sigma(\lambda a) = \varsigma(\lambda)\sigma(a)$; the twisted case is the one that produces the involutions of the second kind and the descent from $B \otimes_F K$ to $B$. The algebra case carries one sign only: $\sigma(1) = 1$ forces $\sigma^2(1) = 1$, so the sign $\sigma^2 = -\mathrm{id}$ of the linear-space article has no unital counterpart here.

**Terminology.** In this article an **involution** of $A$ is an anti-automorphism of order two, the article says **involutive automorphism** for an automorphism of order two, and it reserves the plain word **automorphism** for an automorphism of any order. The corpus also meets involutions of a ring, of a group and of a linear space; the comparison is drawn at the end, and the linear-space article is the one that owns the map of order two considered without a product.

**Layout and boundaries.** The article has four thematic sections and a closing comparison: the definition and the opposite algebra, the symmetric and the skew elements with the Lie and Jordan structures, the ideals, quotients, products and tensor products, the place of the scalars, which is where the two kinds and the descent appear, and finally the comparison with the group, ring and linear-space cases. It stays inside the algebra of Part I and uses no form and no distance: no norm, no length, no orthogonality, no bilinear, sesquilinear or Hermitian form. The vocabulary is that of *Algebras* and *Associative Algebras* for the object and *Unital Algebras* for the unit, *Ideals and Quotients of Algebras* for the ideals and the quotients, *Centre, Units, Zero Divisors and Division Algebras* for the centre and the group of units, *Automorphisms and Derivations of Algebras* for the automorphisms and the inner ones, *The Operators on an Algebra* for the algebra of endomorphisms, *Tensor Products of Algebras* for the tensor product, and *Central Simple Algebras and the Brauer Group* for the opposite algebra and the centre of a simple algebra. The commutator makes *Lie Algebras* and the symmetrised product makes *Jordan Algebras* the owners of the two structures; both lie in the bilinear-algebra reading unit, so they may be named here. Three boundaries are marked rather than crossed. The forms, the adjoint involution that a form defines, the classification of the involutions of the first kind into the orthogonal and the symplectic type, and the trace form and the reduced norm belong to Part II and to *Hilbert Algebras*, which owns them. The graded algebra is *Superalgebras and Graded Structures*, named once where the grading appears. The quaternion conjugation and the involutions of the composition algebras are *Division Algebras* and are not used. The companions in the other categories are *Involutive Rings*, *Involutive Groups* and *Involutive Linear Spaces*. Throughout, $F$ is a field, $A$ is a unital associative $F$-algebra, not assumed commutative, $\sigma$ is an involution of $A$, $\alpha$ is an involutive automorphism of $A$, and $\varsigma$ is an involution of $F$; the fixed set is $A^\sigma = A^+$, the skew elements are $A^-$, and $A^{\mathrm{op}}$ is the opposite algebra.

---

## Involutions of an Algebra

### Definition

**Definition.** Let $A$ be a unital associative $F$-algebra. An **involution** of $A$ is a map $\sigma : A \to A$ such that for all $a, b \in A$ and all $\lambda \in F$

$$
\sigma(a+b) = \sigma(a)+\sigma(b), \qquad \sigma(\lambda a) = \lambda\,\sigma(a), \qquad \sigma(ab) = \sigma(b)\sigma(a), \qquad \sigma(1) = 1, \qquad \sigma(\sigma(a)) = a .
$$

An **involutive linear algebra** is a pair $(A,\sigma)$, the involution is **trivial** when $\sigma = \mathrm{id}_A$, and its **fixed set** is

$$
A^\sigma = \{ a \in A : \sigma(a) = a \},
$$

whose elements are the **symmetric** elements; an element with $\sigma(a) = -a$ is **skew**. When the base field matters the map above is called an $F$-linear involution, and we write $A^+ = A^\sigma$ for the symmetric elements and $A^-$ for the skew elements.

**Definition (semilinear).** Let $\varsigma$ be an involution of the field $F$. A **$\varsigma$-semilinear involution** of $A$ is a map $\sigma : A \to A$ with

$$
\sigma(\lambda a + \mu b) = \varsigma(\lambda)\sigma(a) + \varsigma(\mu)\sigma(b), \qquad \sigma(ab) = \sigma(b)\sigma(a), \qquad \sigma(1) = 1, \qquad \sigma^2 = \mathrm{id} .
$$

The $F$-linear case is the case $\varsigma = \mathrm{id}$, so the semilinear notion contains the linear one. Since $\sigma(1) = 1$ we have $\sigma(\lambda\cdot 1) = \varsigma(\lambda)\cdot 1$, so a $\varsigma$-semilinear involution restricts to $\varsigma$ on the copy $F\cdot 1$ of $F$ inside $A$; in particular the twisting automorphism is determined by the involution and is not extra data.

**Definition (involutive automorphism).** An **involutive automorphism** of $A$ is an algebra automorphism $\alpha$ with $\alpha^2 = \mathrm{id}$, and its fixed set is $A^\alpha$. An automorphism is $F$-linear by definition, so no semilinear variant is needed here; the order-two condition is the only one, and $\alpha^2 = \mathrm{id}$ again forces no second sign.

**Remark.** An involution is bijective, because $\sigma^2 = \mathrm{id}$, so the word "anti-automorphism" is accurate. The definition imposes no condition on $F$; in particular $2$ need not be invertible, and the two places where that matters — the decomposition into symmetric and skew elements, and the closure of the symmetric elements under the symmetrised product — are marked in the text.

**Definition (morphisms).** A **homomorphism** $(A,\sigma) \to (B,\tau)$ of involutive algebras is a unital algebra homomorphism $\varphi : A \to B$ with $\varphi \circ \sigma = \tau \circ \varphi$. Two involutions of the same algebra are **equivalent** when $\sigma' = \varphi \sigma \varphi^{-1}$ for an algebra automorphism $\varphi$; an automorphism of $(A,\sigma)$ is an algebra automorphism commuting with $\sigma$. With $B = A$ the condition says that the automorphism commutes with the involution, so the automorphism group of $(A,\sigma)$ is the centraliser of $\sigma$ in $\operatorname{Aut}(A)$.

### The Opposite Algebra

**Definition.** The **opposite algebra** $A^{\mathrm{op}}$ has the same additive group and the same scalars as $A$ and the product $a \cdot b = ba$; it is introduced in *Algebras* and used in *Central Simple Algebras and the Brauer Group*.

**Theorem.** The involutions of $A$ are exactly the $F$-algebra isomorphisms $\sigma : A \to A^{\mathrm{op}}$ of order two. In particular an algebra carries an involution only if it is isomorphic to its opposite algebra, and the involution is the certificate of that isomorphism.

**Proof.** An involution is additive, $F$-linear, bijective with $\sigma^2 = \mathrm{id}$, and carries $1$ to $1$; its anti-multiplicativity says exactly that it is multiplicative as a map into $A^{\mathrm{op}}$. Conversely an algebra isomorphism $\sigma : A \to A^{\mathrm{op}}$ with $\sigma^2 = \mathrm{id}$ is additive and $F$-linear, fixes $1$, and its multiplicativity with respect to the reversed product is the anti-multiplicativity of the definition.

**Corollary.** $A$ is commutative exactly when the identity is an isomorphism $A \to A^{\mathrm{op}}$, and in that case the involutions of $A$ are its automorphisms of order dividing two. An anti-automorphism of $A$ is an automorphism of $A$ exactly when $A$ is commutative.

**Proof.** $A = A^{\mathrm{op}}$ says $ab = ba$; then an anti-automorphism is multiplicative in the ordinary sense, and conversely an automorphism of a non-commutative algebra reverses no product.

**Theorem (the anti-automorphisms form a coset).** Let $A$ carry an involution $\sigma$, and let $\operatorname{Anti}(A)$ be the set of its anti-automorphisms. The map $\alpha \mapsto \sigma \circ \alpha$ is a bijection $\operatorname{Aut}(A) \to \operatorname{Anti}(A)$, whose inverse is $\rho \mapsto \sigma \circ \rho$. Consequently the composite of two anti-automorphisms is an automorphism, and the involutions of $A$ correspond under the bijection to the automorphisms $\alpha$ with $(\sigma\alpha)^2 = \mathrm{id}$.

**Proof.** For $\alpha \in \operatorname{Aut}(A)$ the composite $\sigma\alpha$ is additive and $F$-linear, carries $1$ to $1$, and reverses a product, so it lies in $\operatorname{Anti}(A)$; the map $\rho \mapsto \sigma\rho$ inverts it because $\sigma(\sigma\alpha) = \alpha$ and $\sigma(\sigma\rho) = \rho$. If $\rho, \rho'$ are anti-automorphisms then $\rho\rho'$ is multiplicative in the ordinary sense, hence an automorphism. Finally $(\sigma\alpha)^2 = \mathrm{id}$ is the condition that $\sigma\alpha$ be an involution, and it is a genuine condition: the coset $\operatorname{Anti}(A)$ usually contains anti-automorphisms of infinite order beside the involutions.

**Remark.** The theorem is the algebra case of the phenomenon of *Involutive Groups*, where the involution is the inversion and the anti-automorphisms are a coset of the automorphism group under $\operatorname{Anti}(G) \cong \operatorname{Aut}(G)$; here the inversion is replaced by the chosen involution $\sigma$, which is an extra datum unless the algebra is commutative.

### Elementary Properties

**Proposition.** Let $\sigma$ be an involution of $A$.

**(a)** $\sigma(0) = 0$, $\sigma(1) = 1$, $\sigma(-a) = -\sigma(a)$, and $\sigma$ is additive and $F$-linear.

**(b)** $\sigma$ maps the set of units onto itself by $u \mapsto \sigma(u)$, and $\sigma(u^{-1}) = \sigma(u)^{-1}$; the restriction $\sigma|_{A^\times}$ is an anti-automorphism of order two of the group of units $A^\times$, in the sense of *Involutive Groups*.

**(c)** $\sigma$ carries a right ideal to a left ideal and a two-sided ideal to a two-sided ideal, and it preserves products and sums of ideals.

**(d)** The centre $Z(A)$ is $\sigma$-stable, and $\sigma|_{Z(A)}$ is an automorphism of $Z(A)$ with $(\sigma|_{Z(A)})^2 = \mathrm{id}$; its fixed subring is $Z(A) \cap A^+$.

**(e)** The elements $a + \sigma(a)$, $a\sigma(a)$ and $\sigma(a)a$ are symmetric, and $a - \sigma(a)$ is skew.

**Proof.** (a) is immediate from additivity and $\sigma^2 = \mathrm{id}$. (b) $\sigma(u)\sigma(u^{-1}) = \sigma(u^{-1}u) = \sigma(1) = 1$ and likewise in the other order, so $\sigma(u)$ is a unit with the stated inverse; the restriction is a group map of order two, and it reverses a product because $\sigma$ does. (c) If $rA \subseteq I$ then $A\sigma(r) = \sigma(rA) \subseteq \sigma(I)$, and the two-sided case follows by applying the same computation on both sides. (d) For $z$ central and $a$ arbitrary, $z\sigma(a) = \sigma(az) = \sigma(za) = \sigma(a)z$, so $\sigma(z)$ is central; the restriction is a ring automorphism of order two. (e) Apply $\sigma$: $\sigma(a+\sigma(a)) = \sigma(a)+a$, $\sigma(a\sigma(a)) = \sigma(\sigma(a))\sigma(a) = a\sigma(a)$, and $\sigma(\sigma(a)a) = \sigma(a)a$; and $\sigma(a-\sigma(a)) = -(a-\sigma(a))$.

**Remark.** Part (b) is the passage to the group case: an involution of the algebra restricts to an anti-automorphism of order two of the group of units, and the fixed units of $\sigma$ are a subgroup only when the symmetric units commute, by the structure theory of *Involutive Groups*. The linear-group consequences of the restriction — the orthogonal and the unitary groups that a form selects among the fixed units — are Part II.

### Examples

**Example (the transpose).** On $M_n(F)$ the transpose $X \mapsto X^{\mathsf{T}}$ is an $F$-linear involution, since $(XY)^{\mathsf{T}} = Y^{\mathsf{T}}X^{\mathsf{T}}$, $(X^{\mathsf{T}})^{\mathsf{T}} = X$ and $(\lambda X)^{\mathsf{T}} = \lambda X^{\mathsf{T}}$. Its symmetric elements are the symmetric matrices and its skew elements the antisymmetric matrices; it is the prototype, and it fixes the centre $F\cdot 1$ pointwise.

**Example (the exchange involution).** On $A \times A^{\mathrm{op}}$, with the product $(a_1,a_2)(b_1,b_2) = (a_1b_1,\; b_2a_2)$, the swap $\sigma(a_1,a_2) = (a_2,a_1)$ is an $F$-linear involution; its fixed set is the diagonal $\{(a,a)\}$ and its skew elements are the antidiagonal $\{(a,-a)\}$. The construction makes every algebra the fixed set of an involution on an algebra that contains it, and it is used below.

**Example (a group algebra).** On the group algebra $F[G]$, the linear extension of $g \mapsto g^{-1}$ is an $F$-linear involution, because $(gh)^{-1} = h^{-1}g^{-1}$ and $(g^{-1})^{-1} = g$. Its symmetric elements are the sums $\sum a_g g$ with $a_g = a_{g^{-1}}$; on an abelian $G$ the inversion is the identity on $G$ and every element is symmetric.

**Example (an involutive automorphism).** On $M_n(F)$ with $n \geq 1$ and $T$ a matrix with $T^2 = 1$, the map $\Phi_T(X) = TXT$ is an involutive automorphism, because $T^2 = 1$; its fixed set is $\{X : TXT = X\}$, which for $T = \operatorname{diag}(1,-1)$ is the algebra of matrices of the shape $\begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix}$. The same $T$ gives the linear involution $\Phi_T$ of the underlying space that is analysed in *Involutive Linear Spaces*, and the composite $X \mapsto T X^{\mathsf{T}} T$ is an anti-automorphism of order two, hence an involution of $M_n(F)$; one matrix $T$ thus produces both kinds of order-two map, and the two kinds coincide as notions only when the algebra is commutative.

**Example (a field extension).** Let $K/F$ be a quadratic extension with nontrivial automorphism $\varsigma$. The $F$-algebra $K$ carries $\varsigma$ as an involution, which is $F$-linear because $\varsigma$ fixes $F$; it is the identity on $F$ and not on $K$, and its fixed set is $F$.

**Example (a polynomial algebra).** On $F[x_1,\dots,x_n]$ the algebra automorphism that negates each variable, $x_i \mapsto -x_i$, has order two and is an involutive automorphism whose fixed set is the span of the monomials of even total degree; on $F[x,y]$ the swap $x \leftrightarrow y$ is an involutive automorphism whose fixed set is the algebra of symmetric polynomials in two variables. On a commutative algebra the anti-automorphism and the automorphism are the same maps, and these two examples are therefore also involutions.

**Example (the complex case).** On $M_n(\mathbb{C})$ the entrywise conjugation $\overline{X}$ is a $\varsigma$-semilinear **automorphism** of order two, with $\varsigma$ the conjugation of $\mathbb{C}$, and the transpose is a $\mathbb{C}$-linear anti-automorphism of order two; the conjugate transpose $X^{*} = \overline{X}^{\mathsf{T}}$ is a $\varsigma$-semilinear anti-automorphism of order two, since $(XY)^{*} = Y^{*}X^{*}$ and $(X^{*})^{*} = X$, while $(X+Y)^{*} = X^{*}+Y^{*}$ and $(\lambda X)^{*} = \overline{\lambda}\,X^{*}$. The fixed elements of the entrywise conjugation are the matrices with real entries, that is the real algebra $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$.

---

## The Symmetric and Skew Elements

### The Additive Decomposition

**Theorem.** Let $F$ be a field with $2 \neq 0$ and let $\sigma$ be an involution of $A$. Then

$$
p_+ = \tfrac12(\mathrm{id}+\sigma), \qquad p_- = \tfrac12(\mathrm{id}-\sigma)
$$

are $F$-linear maps with $p_+^2 = p_+$, $p_-^2 = p_-$, $p_+ + p_- = \mathrm{id}$ and $p_+p_- = p_-p_+ = 0$, and

$$
A = A^+ \oplus A^-, \qquad A^+ = \ker(\sigma - \mathrm{id}), \qquad A^- = \ker(\sigma + \mathrm{id}).
$$

**Proof.** $(2p_+)^2 = (\mathrm{id}+\sigma)^2 = \mathrm{id} + 2\sigma + \sigma^2 = 2(\mathrm{id}+\sigma) = 4p_+$, so $p_+^2 = p_+$ because $2$ is invertible; the same computation with $\sigma$ replaced by $-\sigma$ gives $p_-^2 = p_-$, and the sum and the products follow from the definitions. The images of $p_+$ and $p_-$ are the fixed and the negated elements, and every element is $a = p_+(a) + p_-(a)$, uniquely.

**Corollary.** The involution $\sigma$ is a linear involution of the underlying space $A$ in the sense of *Involutive Linear Spaces*, and its type as a linear involution is the pair $(\dim_F A^+, \dim_F A^-)$.

**Proof.** A linear involution is an $F$-linear map of order two, which $\sigma$ is, and the summands of the general theory are $A^+$ and $A^-$.

**Remark (characteristic two).** Let $2 = 0$ in $F$. Then $x = -x$ for every $x$, so the skew elements and the symmetric elements coincide, $A^+ = A^-$, the sum $A^+ + A^-$ is all of $A$ but not direct, and the map $p_+$ of the theorem is not available. The point of the failure is the same as in *Involutive Linear Spaces*: the classifications and the decompositions that use the two eigenvalues $\pm 1$ are not available, and the article says which of its statements survive. The Lie structure of the next subsection survives, because $[x,y] = xy-yx = xy+yx$ there; the Jordan structure is not available, because $\tfrac12$ does not exist, and a Jordan product in characteristic two would have to be defined by the anticommutator $xy+yx$ instead, which is a different notion.

### The Skew Elements Form a Lie Algebra

**Definition.** On $A$ the **commutator** is $[x,y] = xy - yx$; it is $F$-bilinear, alternating, $[x,x] = 0$, and it satisfies the Jacobi identity, so $A$ with the commutator is a Lie algebra over $F$ in the sense of *Lie Algebras*.

**Theorem.** Let $\sigma$ be an involution of $A$. Then

$$
[A^+, A^+] \subseteq A^-, \qquad [A^+, A^-] \subseteq A^+, \qquad [A^-, A^-] \subseteq A^- .
$$

In particular $A^-$ is a Lie subalgebra, $A^+$ is a module over it, and $A^- \oplus A^+$ is a $\mathbb{Z}/2$-graded Lie algebra whose even part is $A^-$ and whose odd part is $A^+$.

**Proof.** For symmetric $x$ and $y$, $\sigma(xy) = \sigma(y)\sigma(x) = yx$, so $\sigma([x,y]) = yx - xy = -[x,y]$ and $[x,y]$ is skew. For symmetric $x$ and skew $y$, $\sigma(xy) = \sigma(y)\sigma(x) = (-y)x = -yx$, so $\sigma([x,y]) = -yx + xy = [x,y]$ and $[x,y]$ is symmetric. For skew $x$ and $y$, $\sigma(xy) = \sigma(y)\sigma(x) = (-y)(-x) = yx$, so $\sigma([x,y]) = yx - xy = -[x,y]$ and $[x,y]$ is skew. The Jacobi identity is inherited from $A$, and the grading statement is the three inclusions with the degrees $\deg A^- = 0$ and $\deg A^+ = 1$.

**Example.** On $M_n(F)$ with the transpose the skew elements are the antisymmetric matrices, of dimension $n(n-1)/2$ for $2 \neq 0$, and the theorem says that the commutator of two antisymmetric matrices is antisymmetric; for $n = 3$ they form a three-dimensional Lie algebra, and the bracket of two of its basis elements is again a basis element. Nothing of this kind exists on a bare linear space: the bracket needs the product, and this is the first place where the algebra is more than its underlying space.

### The Symmetric Elements Form a Jordan Algebra

**Definition.** On $A$ the **symmetrised product** is $x \bullet y = \tfrac12(xy + yx)$, defined when $2 \neq 0$; it is commutative, $F$-bilinear, and satisfies the Jordan identity, so $A$ with it is a Jordan algebra in the sense of *Jordan Algebras*.

**Theorem.** Let $2 \neq 0$ and let $\sigma$ be an involution of $A$. Then $A^+$ is closed under the symmetrised product, so $A^+$ is a Jordan subalgebra of $A$. Moreover $A^+$ is closed under the ordinary product if and only if its elements commute pairwise, that is $[x,y] = 0$ for all $x, y \in A^+$; in particular $A^+$ is a subalgebra whenever $A$ is commutative.

**Proof.** For symmetric $x$ and $y$, $\sigma(xy) = \sigma(y)\sigma(x) = yx$ and $\sigma(yx) = xy$, so $\sigma(x \bullet y) = \tfrac12(yx + xy) = x \bullet y$ and $x \bullet y$ is symmetric. For the criterion, $xy \in A^+$ says $\sigma(xy) = xy$, that is $yx = xy$; the condition is therefore $[x,y] = 0$ for all symmetric $x$ and $y$, and it holds for all pairs as soon as $A$ is commutative.

**Remark (the fixed set may still be an algebra).** $A$ need not be commutative for $A^+$ to be a subalgebra, because the criterion is only that the symmetric elements commute among themselves. On the algebra $T$ of upper triangular $2 \times 2$ matrices the map

$$
\sigma\begin{pmatrix} a & b \\ 0 & d \end{pmatrix} = \begin{pmatrix} d & -b \\ 0 & a \end{pmatrix}
$$

is an involution: it is additive and $F$-linear, its square is the identity, and it reverses products. Its fixed set is the algebra of diagonal matrices, a subalgebra of the non-commutative $T$ that is properly contained in it. So the symmetric elements of an involution may be a proper subalgebra, and the Jordan algebra of the theorem is the general statement: the centre is the symmetric part of an involution when the involution is chosen so that its fixed set is the centre, as the invariants of a form do in Part II.

**Example (the failure).** In $M_2(F)$ with $2 \neq 0$ take the symmetric matrices $S_1 = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ and $S_2 = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$; then

$$
S_1S_2 = \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix}, \qquad S_2S_1 = \begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix},
$$

neither of which is symmetric, while $S_1 \bullet S_2$, their average, is. The fixed set of the transpose is thus a Jordan algebra of dimension $3$ that is not an algebra, and the product of two symmetric elements is symmetric precisely when the two commute; for the transpose the symmetric matrices of $M_n(F)$ therefore form an algebra only when $n = 1$.

**Remark (no grading here).** For the transpose the decomposition $A = A^+ \oplus A^-$ is not a grading of the algebra: with $S = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ symmetric and $K = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ skew, the product $SK = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is neither symmetric nor skew. The product of a symmetric and a skew element is skew exactly when the two commute, so an anti-automorphism does not grade the algebra, and only an automorphism does.

### Involutive Automorphisms and the Fixed Subalgebra

**Theorem.** Let $\alpha$ be an involutive automorphism of $A$ and let $2 \neq 0$. Then

$$
A^+ = \ker(\alpha - \mathrm{id}), \qquad A^- = \ker(\alpha + \mathrm{id}), \qquad A = A^+ \oplus A^-
$$

as before, and now $A^+$ is a subalgebra, $A^-$ is an $A^+$-bimodule, and

$$
A^+A^+ \subseteq A^+, \qquad A^+A^- \subseteq A^-, \qquad A^-A^- \subseteq A^+ :
$$

the algebra is $\mathbb{Z}/2$-graded, with $A^+$ the even part and $A^-$ the odd part.

**Proof.** The decomposition is the theorem of the first subsection. For $x,y$ fixed, $\alpha(xy) = \alpha(x)\alpha(y) = xy$; for $x$ fixed and $y$ negated, $\alpha(xy) = x(-y) = -xy$ and likewise on the other side; and for $x,y$ negated, $\alpha(xy) = (-x)(-y) = xy$. Each line says that the product lands in the stated summand.

**Corollary (the inner case).** Let $u$ be a unit of $A$. Then $\operatorname{ad}_u(x) = uxu^{-1}$ is an involutive automorphism exactly when $u^2 \in Z(A)$, and then its fixed subalgebra is the centraliser $C_A(u)$. In particular an inner involutive automorphism is the identity on the centre, and if $A$ is central simple then every involutive automorphism is inner, by Skolem–Noether, so every involutive automorphism of $A$ is of this form.

**Proof.** $\operatorname{ad}_u^2(x) = u^2xu^{-2}$, so $\operatorname{ad}_u^2 = \mathrm{id}$ exactly when $u^2$ is central; $x$ is fixed exactly when $ux = xu$. An inner automorphism fixes the centre pointwise, and for a central simple algebra every automorphism is inner by the Skolem–Noether theorem of *Automorphisms and Derivations of Algebras*.

**Remark.** The two kinds of order-two map thus give two different theorems about the fixed set: for an involutive automorphism the fixed set is a subalgebra and the algebra is graded by it, whereas for an involution the fixed set is a Jordan algebra in general and the grading fails. The contrast is the reason both notions are defined above, and it is a contrast that the commutative case cannot show, because there the two maps coincide. The graded algebras themselves, their sign rule and their tensor products, belong to *Superalgebras and Graded Structures*.

---

## Ideals, Quotients and Products

### Stable Ideals and Quotients

**Definition.** A subspace or ideal $I$ of $A$ is **$\sigma$-stable** when $\sigma(I) \subseteq I$, which for a two-sided ideal is equivalent to $\sigma(I) = I$ because $\sigma^2 = \mathrm{id}$.

**Theorem.** Let $I$ be a $\sigma$-stable two-sided ideal of the involutive algebra $(A,\sigma)$. Then $\sigma$ induces an involution $\bar\sigma$ of the quotient algebra $A/I$ by $\bar\sigma(a+I) = \sigma(a)+I$, and

$$
(A^+ + I)/I \;\subseteq\; (A/I)^{\bar\sigma},
$$

with equality when $2 \neq 0$. In characteristic two only the inclusion is claimed.

**Proof.** The map is well defined because $\sigma(I) \subseteq I$, it is additive and $F$-linear, it fixes $1+I$, and it reverses products because $\sigma$ does; its square is the identity because $\sigma^2 = \mathrm{id}$. For the inclusion, let $s \in A^+$ and $i \in I$; then $\bar\sigma(s+i+I) = s+\sigma(i)+I = s+i+I$, because $\sigma(i)-i \in I$ by the stability of $I$. For the equality, an element $a+I$ fixed by $\bar\sigma$ satisfies $a-\sigma(a) \in I$, and when $2 \neq 0$

$$
a = \tfrac12(a+\sigma(a)) + \tfrac12(a-\sigma(a))
$$

exhibits $a$ as a symmetric element plus an element of $I$.

**Corollary.** The kernel of a homomorphism of involutive algebras is $\sigma$-stable and two-sided, and the first isomorphism theorem holds in the form $A/\ker\varphi \cong \operatorname{im}\varphi$ with the induced involution.

**Proof.** If $\varphi \circ \sigma = \tau \circ \varphi$ and $\varphi(a) = 0$ then $\varphi(\sigma(a)) = \tau(0) = 0$, so the kernel is $\sigma$-stable; the rest is the isomorphism theorem for algebras with the involution transported.

**Remark.** The invariant quotients of an algebra with an involution — the ideals stable under the involution and the algebras they define — are the algebra case of the $\sigma$-ideals of *Involutive Rings*, and the two theories run in parallel. Which of these quotients are semiprime, prime or reduced is the subject of *Semiprime Rings*, *Prime Rings* and *Reduced Rings and the Nilradical*, in *Rings and Fields*.

### The Exchange Involution and $A \times A^{\mathrm{op}}$

**Definition.** On the algebra $A \times A^{\mathrm{op}}$ the product is $(a_1,a_2)(b_1,b_2) = (a_1b_1,\; b_2a_2)$ and the **exchange** is $\sigma(a_1,a_2) = (a_2,a_1)$.

**Theorem.** The exchange is an $F$-linear involution of $A \times A^{\mathrm{op}}$, its fixed set is the diagonal $\{(a,a) : a \in A\}$, of the same dimension as $A$, and its skew elements are the antidiagonal $\{(a,-a) : a \in A\}$. The diagonal is closed under the symmetrised product, and it is a subalgebra if and only if $A$ is commutative.

**Proof.** For $x = (a_1,a_2)$ and $y = (b_1,b_2)$ the products are $xy = (a_1b_1, b_2a_2)$ and $\sigma(y)\sigma(x) = (b_2,b_1)(a_2,a_1) = (b_2a_2,\; a_1b_1)$, so $\sigma(xy) = (b_2a_2, a_1b_1) = \sigma(y)\sigma(x)$; the map is additive, $F$-linear, fixes $(1,1)$ and has square the identity. An element is fixed exactly when $a_1 = a_2$ and is negated exactly when $a_1 = -a_2$. For the closure, $(a,a)(b,b) = (ab,ba)$ and $(a,a) \bullet (b,b) = (a \bullet b,\; a \bullet b)$, so the diagonal is stable under the symmetrised product and the ordinary product stays in it exactly when $ab = ba$ for all $a, b$.

**Corollary (universality).** Every $F$-algebra $A$ is the fixed set of an involution of an $F$-algebra, namely of the exchange of $A \times A^{\mathrm{op}}$, and the diagonal is isomorphic to $A$ as a Jordan algebra; and $A \times A^{\mathrm{op}}$ is commutative if and only if $A$ is.

**Proof.** The fixed set is the diagonal by the theorem, and $a \mapsto (a,a)$ is an isomorphism of $A$ onto the diagonal that carries the symmetrised product of $A$ to the symmetrised product of the diagonal, by $(a,a) \bullet (b,b) = (a \bullet b, a \bullet b)$. For the commutativity, the products of $(a,1)$ and $(b,1)$ are $(ab,1)$ and $(ba,1)$, so commutativity forces $ab = ba$; conversely if $A$ is commutative then $A^{\mathrm{op}} = A$ and the product is componentwise.

**Remark.** The construction is the algebra analogue of the swap of *Involutive Groups* and of the exchange of *Involutive Rings*; it shows that the existence of an involution costs nothing once the opposite algebra is at hand, and the informative question is therefore not whether an algebra carries an involution but which involution it carries. The opposite algebra in the second factor is what makes the swap reverse products: on $A \times A$ with the componentwise product the same swap satisfies $\sigma(xy) = \sigma(x)\sigma(y)$ and is an **involutive automorphism**, with the diagonal as its fixed subalgebra, and the two constructions are the two kinds of order-two map of the introduction, exhibited on one algebra. The involutions of $A \times A^{\mathrm{op}}$ that are not the exchange, and the question of which involutions of a product are equivalent to the exchange, belong to the classification of the involutions of a semisimple algebra, which is Part II work when it is read from a form.

### Tensor Products and Endomorphisms

**Theorem.** Let $(A,\sigma)$ and $(B,\tau)$ be involutive $F$-algebras and let $2 \neq 0$. Then $\sigma \otimes \tau$ on $A \otimes_F B$, defined on decomposable elements by $a \otimes b \mapsto \sigma(a) \otimes \tau(b)$, is an $F$-linear involution, and

$$
(A \otimes B)^+ = A^+ \otimes B^+ \;\oplus\; A^- \otimes B^-, \qquad (A \otimes B)^- = A^+ \otimes B^- \;\oplus\; A^- \otimes B^+ .
$$

**Proof.** The map is the tensor product of two $F$-linear maps, hence $F$-linear; it reverses a product because the two factors do, fixes $1 \otimes 1$, and has square the identity because each factor has. For the decomposition, $A \otimes B$ is spanned by the four spaces on the right, and each of them lies in the stated eigenvalue space by the multiplicativity of $\sigma \otimes \tau$; the sum is direct because the decomposition of each factor is direct and tensor products of independent subspaces are independent.

**Example.** For $A = B = M_2(F)$ with the transpose and $2 \neq 0$, the symmetric part has dimension $3 \cdot 3 + 1 \cdot 1 = 10$ and the skew part has dimension $3 \cdot 1 + 1 \cdot 3 = 6$, and $10 + 6 = 16 = 4^2$; the involution $\sigma \otimes \tau$ on the sixteen-dimensional algebra $M_2(F) \otimes M_2(F)$ is thus a linear involution of the underlying space of type $(10,6)$.

**Theorem (endomorphisms).** Let $V$ be a finite-dimensional linear space over $F$ and let $T \in \operatorname{GL}(V)$ with $T^2 = \mathrm{id}$. Then $\Phi_T(X) = TXT$ is an involutive automorphism of the algebra $\operatorname{End}_F(V)$. If moreover $T$ is symmetric with respect to a basis, $T^{\mathsf{T}} = T$ in that basis, then $X \mapsto TX^{\mathsf{T}}T$ is an involution of $\operatorname{End}_F(V)$, and its fixed algebra is the set of the matrices $X$ with $TX^{\mathsf{T}}T = X$.

**Proof.** $\Phi_T(XY) = TXYT = TXT\,TYT = \Phi_T(X)\Phi_T(Y)$ because $T^2 = \mathrm{id}$, and it is $F$-linear and fixes the identity, so it is an algebra automorphism with $\Phi_T^2 = \mathrm{id}$. The map $\rho(X) = TX^{\mathsf{T}}T$ is the composite of the transpose with $\Phi_T$, so by the coset theorem it is an anti-automorphism, and it has order two because

$$
\rho^2(X) = T\,(TX^{\mathsf{T}}T)^{\mathsf{T}}T = T\,TXT\,T = X
$$

using $T^{\mathsf{T}} = T$ and $T^2 = \mathrm{id}$; its fixed set is the set of the $X$ with $\rho(X) = X$.

**Remark.** The involutive automorphism $\Phi_T$ appears on the underlying linear space in *Involutive Linear Spaces*, where its type is computed, and on the algebra in *The Operators on an Algebra*, where the algebra of endomorphisms is introduced. The two readings differ: on the space the datum is a linear involution, on the algebra it is an automorphism, and the transpose, which has no meaning for a bare space, is what turns the one into the other. The form that a given involution of $\operatorname{End}_F(V)$ preserves — the symmetric or alternating form whose adjoint it is — is the subject of *Hilbert Algebras* and is not used here.

---

## Involutions and the Scalars

### Semilinear Involutions

**Theorem.** Let $\varsigma$ be an involution of $F$ and let $\sigma$ be a $\varsigma$-semilinear involution of $A$. Then $\sigma$ is $F$-linear exactly when $\varsigma = \mathrm{id}$, the restriction $\sigma|_{F\cdot 1}$ is $\varsigma$, and $A^+$ and $A^-$ are $F$-subspaces of $A$ only when $\sigma$ is $F$-linear; in the semilinear case $A^+$ is a linear space over the fixed field $F^\varsigma$.

**Proof.** The restriction was computed in the definition. A $\varsigma$-semilinear map that is $F$-linear satisfies $\varsigma(\lambda)a = \lambda a$ for every $\lambda$, so $\varsigma = \mathrm{id}$. For the last statement, if $x$ is fixed and $\mu \in F^\varsigma$ then $\sigma(\mu x) = \varsigma(\mu)\sigma(x) = \mu x$, so $A^+$ is stable under the scalars of $F^\varsigma$.

**Remark.** The strictly semilinear case, where $\varsigma \neq \mathrm{id}$, is the case of a genuine twisting of the scalars, and it is the only way an involution of an algebra over $F$ can fail to be $F$-linear. The two examples that matter are the conjugation on a quadratic extension and the entrywise conjugation on $M_n(\mathbb{C})$; both are automorphisms of order two, and their composite with an $F$-linear anti-automorphism, as for the conjugate transpose, is a semilinear involution.

### The Centre and the Two Kinds

**Definition.** Let $\sigma$ be an involution of $A$ with centre $Z(A)$. Then $Z(A)$ is $\sigma$-stable by the proposition above, and $\sigma$ is of the **first kind** when $\sigma$ is the identity on $Z(A)$ and of the **second kind** when it is not.

**Theorem.** A $\varsigma$-semilinear involution of $A$ is of the first kind exactly when $\varsigma = \mathrm{id}$ on the subfield $F\cdot 1$ of $Z(A)$ and $\sigma$ fixes the whole centre; it is of the second kind exactly when the restriction $\sigma|_{Z(A)}$ is a nontrivial automorphism of order two of the centre, and then the fixed subring $Z(A)^\sigma$ is a subfield of index two in the centre when the centre is a field.

**Proof.** By the elementary proposition the restriction of $\sigma$ to the centre is an automorphism of order dividing two, so it is either the identity, which is the first kind, or an automorphism of order two, which is the second kind; an automorphism of order two of a field has fixed field of index two.

**Example.** On $M_n(F)$ the transpose fixes the centre $F\cdot 1$ and is of the first kind, and every $F$-linear involution of $M_n(F)$ is of the first kind because the centre is $F\cdot 1$. On $M_n(\mathbb{C})$ the transpose is again of the first kind, while the conjugate transpose restricts to the centre as the conjugation of $\mathbb{C}$ and is of the second kind; on the $\mathbb{R}$-algebra $\mathbb{C}$ itself the conjugation is of the second kind with fixed field $\mathbb{R}$. The classification of the involutions of the first kind of a central simple algebra into the orthogonal and the symplectic type, and the theory of the second-kind case over a quadratic extension, are the subject of *Hilbert Algebras*, where the invariants are the forms and the dimensions of the symmetric elements; the present article stops at the definition of the kind, which uses only the centre.

### The Fixed Algebra of a Second-Kind Involution

**Theorem (the second-kind involution on a scalar extension).** Let $K/F$ be a quadratic extension with nontrivial automorphism $\varsigma$, let $t \in K$ satisfy $\varsigma(t) = -t$ and $K = F \oplus Ft$ when $2 \neq 0$, and let $B$ be an $F$-algebra carrying an $F$-linear involution $\tau$. On the $K$-algebra $A = B \otimes_F K$ the map

$$
\sigma(b \otimes k) = \tau(b) \otimes \varsigma(k)
$$

is a $\varsigma$-semilinear involution of the second kind, and

$$
A^+ = (B^+ \otimes 1) \oplus (B^- \otimes t), \qquad A^- = (B^+ \otimes t) \oplus (B^- \otimes 1).
$$

**Proof.** The map is additive and $\varsigma$-semilinear, because $\sigma(\lambda(b \otimes k)) = \sigma(b \otimes \lambda k) = \tau(b) \otimes \varsigma(\lambda k) = \varsigma(\lambda)\,\sigma(b \otimes k)$; it reverses products, because $\sigma\big((b \otimes k)(b' \otimes k')\big) = \tau(bb') \otimes \varsigma(kk') = \tau(b')\tau(b) \otimes \varsigma(k)\varsigma(k') = \sigma(b' \otimes k')\,\sigma(b \otimes k)$; it fixes $1 \otimes 1$ and its square is the identity because $\tau^2 = \varsigma^2 = \mathrm{id}$. Writing an element of $A$ as $b \otimes 1 + b' \otimes t$ with $b, b' \in B$, which is unique when $2 \neq 0$, its image is $\tau(b) \otimes 1 - \tau(b') \otimes t$; it is fixed exactly when $\tau(b) = b$ and $\tau(b') = -b'$, that is $b \in B^+$ and $b' \in B^-$, and it is negated exactly when $b \in B^-$ and $b' \in B^+$. The kind is second because the centre of $A$ contains $1 \otimes K$ and $\sigma$ acts there as the nontrivial involution $\varsigma$.

**Corollary (descent of a commutative algebra).** Let $B$ be commutative and let $\tau = \mathrm{id}_B$, which is an involution because $B$ is commutative; then $\sigma = \mathrm{id}_B \otimes \varsigma$ and

$$
A^+ = B \otimes 1 \cong B, \qquad A^- = B \otimes t ,
$$

so the commutative $F$-algebra $B$ is recovered from its scalar extension $B \otimes_F K$ by the involution alone. The case $B = F$ is the quadratic extension itself: $A = K$, $\sigma = \varsigma$ and $K^\sigma = F$.

**Proof.** With $\tau = \mathrm{id}$ the theorem gives $B^+ = B$ and $B^- = 0$, so $A^+ = B \otimes 1$ and $A^- = B \otimes t$.

**Remark (the trap in the non-commutative case).** For a non-commutative $B$ the map $\mathrm{id}_B \otimes \varsigma$ is multiplicative and **not** anti-multiplicative, so it is an involutive automorphism and not an involution; the fixed algebra of that map is $B \otimes 1$, but the map is the wrong kind, and the involution of the second kind is $\tau \otimes \varsigma$, whose fixed algebra is the twist $B^+ \oplus B^-t$ rather than $B$. The two maps coincide as maps only when $\tau = \mathrm{id}_B$, that is only when $B$ is commutative. In particular the descent in the non-commutative case recovers the pair $(B,\tau)$ and not $B$ alone.

**Example (the complex case).** For $F = \mathbb{R}$, $K = \mathbb{C}$, $t = i$ and $B = M_2(\mathbb{R})$ with $\tau$ the transpose, the algebra $A$ is $M_2(\mathbb{C})$ and $\sigma$ is the conjugate transpose; the fixed algebra $A^+ = \mathrm{Sym}_2(\mathbb{R}) \oplus i\,\mathrm{Skew}_2(\mathbb{R})$ is the algebra of Hermitian matrices, of real dimension $3 + 1 = 4$, and the skew part $A^- = \mathrm{Sym}_2(\mathbb{R})\,i \oplus \mathrm{Skew}_2(\mathbb{R})$ has the same real dimension $4$, with $4 + 4 = 8$ the real dimension of $M_2(\mathbb{C})$. With $B = \mathbb{R}$ in place of $M_2(\mathbb{R})$ the same computation gives $A = \mathbb{C}$, $\sigma$ the conjugation, $A^+ = \mathbb{R}$ and $A^- = \mathbb{R}i$, which is the corollary.

**Remark.** The descent is the algebra case of the conjugate-linear involution $\kappa$ of the complexification in *Involutive Linear Spaces*, and of the real form that a conjugate-linear structure defines there; the difference is that the fixed set is now closed under the product in the commutative case, where it is the copy $B \otimes 1$, so what descends is an algebra and not only a space, while in the non-commutative case the fixed set is the twist $B^+ \oplus B^-t$ and the datum that descends is the pair $(B,\tau)$. The extension of scalars itself, the complexification and the behaviour of the involution under it, are *Extension of Scalars*.

## The Three Other Cases

**Groups.** In *Involutive Groups* the involution of a group is an anti-automorphism of order two, and the inversion $g \mapsto g^{-1}$ is the model; an involution of an algebra restricts to the group of units, by the proposition on the elementary properties, and not every involution of that group extends to the algebra. The coset theorem above is the algebra case of the coset $\operatorname{Anti}(G)$ of the group theory, with the chosen involution $\sigma$ in the place of the inversion.

**Rings.** *Involutive Rings* gives the same map with the field removed: there the involution of a ring is an anti-automorphism of order two, the datum is an order-two isomorphism $A \to A^{\mathrm{op}}$, and the $\sigma$-ideals, the $\sigma$-prime notions and the reduced questions are its subject. The present article adds the field $F$, the $F$-linearity and the scalar twisting, and the $\varsigma$-semilinear case exists only here.

**Linear spaces.** *Involutive Linear Spaces* gives a map of order two on a space that carries no product. An algebra involution is such a map on the underlying space, so every statement about the involution alone is the linear-space statement, as the corollary of the additive decomposition records; what the algebra adds is the Lie structure on $A^-$, the Jordan structure on $A^+$, the grading of the involutive automorphism and the two kinds through the centre. The second sign of the linear case, $\theta^2 = -\mathrm{id}$, disappears here, by the remark at the definition.

---

## Summary

An involution of a unital associative $F$-algebra $A$ is an $F$-linear anti-automorphism $\sigma$ with $\sigma^2 = \mathrm{id}$, the same datum as an $F$-algebra isomorphism $A \to A^{\mathrm{op}}$ of order two; a second kind of order-two map, the involutive automorphism, preserves the product, and the two coincide exactly on a commutative algebra. When $A$ carries an involution the anti-automorphisms of $A$ form a coset $\operatorname{Anti}(A) = \sigma\operatorname{Aut}(A)$, the composite of two of them is an automorphism, and the involutions among them are those $\sigma\alpha$ with $(\sigma\alpha)^2 = \mathrm{id}$. The centre and the group of units are stable, the restriction to the units is an anti-automorphism of order two of the group, and the elements $a+\sigma(a)$, $a\sigma(a)$ and $\sigma(a)a$ are symmetric.

Over a field with $2 \neq 0$ the involution decomposes the algebra, $A = A^+ \oplus A^-$, the symmetric and the skew elements; the skew elements are closed under the commutator, so $A^-$ is a Lie subalgebra, $A^+$ is a module over it and $A^- \oplus A^+$ is a $\mathbb{Z}/2$-graded Lie algebra; the symmetric elements are closed under the symmetrised product, so $A^+$ is a Jordan algebra, and it is a subalgebra exactly when its elements commute pairwise, so it is one when $A$ is commutative and it may be a proper subalgebra when $A$ is not, the diagonal matrices inside the upper triangular algebra being the instance; the failure is exhibited by the two symmetric matrices $S_1$ and $S_2$ that do not commute. For an involutive automorphism $\alpha$ the fixed set $A^+$ is instead always a subalgebra and $A = A^+ \oplus A^-$ is a $\mathbb{Z}/2$-grading, and an inner $\alpha$ is $\operatorname{ad}_u$ with $u^2$ central. In characteristic two the symmetric and the skew elements coincide, the decomposition and the Jordan structure are unavailable, and the Lie structure survives.

A $\sigma$-stable ideal has an induced involution on its quotient, with $(A^+ + I)/I \subseteq (A/I)^{\bar\sigma}$ and equality when $2 \neq 0$; the exchange involution on $A \times A^{\mathrm{op}}$ has the diagonal as its fixed set, so every algebra is the fixed set of an involution of an algebra, and the swap on $A \times A$ is the involutive automorphism with the diagonal as its fixed subalgebra; the tensor product carries $\sigma \otimes \tau$, with symmetric part $A^+ \otimes B^+ \oplus A^- \otimes B^-$; and on $\operatorname{End}_F(V)$ the map $\Phi_T$ is an involutive automorphism while the transpose is an involution. A $\varsigma$-semilinear involution twists the scalars, is $F$-linear exactly when $\varsigma = \mathrm{id}$, and is of the first or the second kind according to its restriction to the centre; for a quadratic extension $K/F$ the involution $\tau \otimes \varsigma$ on $B \otimes_F K$, with $\tau$ an involution of $B$, is of the second kind, its fixed algebra is $(B^+ \otimes 1) \oplus (B^- \otimes t)$ with $t$ the $\varsigma$-skew element of $K$, and in the commutative case it is the descent, with fixed algebra $B \otimes 1 \cong B$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $F$ | the field of scalars |
| $A$ | a unital associative $F$-algebra, not assumed commutative |
| $\sigma$ | an involution of $A$, that is an anti-automorphism with $\sigma^2 = \mathrm{id}$ |
| $\tau$ | an involution of a second algebra, for instance of $B$ in the descent |
| $\alpha$ | an involutive automorphism of $A$, that is an automorphism with $\alpha^2 = \mathrm{id}$ |
| $A^\sigma$, $A^+$ | the symmetric elements, $\{a : \sigma(a) = a\}$, the fixed set |
| $A^-$ | the skew elements, $\{a : \sigma(a) = -a\}$ |
| $A^{\mathrm{op}}$ | the opposite algebra, $a \cdot b = ba$ |
| $[x,y]$ | the commutator $xy - yx$ |
| $x \bullet y$ | the symmetrised product $\tfrac12(xy + yx)$, when $2 \neq 0$ |
| $\operatorname{Anti}(A)$ | the anti-automorphisms of $A$, a coset $\sigma \operatorname{Aut}(A)$ |
| $A \times A^{\mathrm{op}}$ | with the product $(a_1,a_2)(b_1,b_2) = (a_1b_1, b_2a_2)$, and the exchange $\sigma(a_1,a_2) = (a_2,a_1)$ |
| $\Phi_T$ | the involutive automorphism $X \mapsto TXT$ of $\operatorname{End}_F(V)$, $T^2 = \mathrm{id}$ |
| $\varsigma$ | an involution of the field $F$ |
| $K/F$, $t$ | a quadratic extension, and a $\varsigma$-skew element $t$ with $K = F \oplus Ft$ |
| $A^\varsigma$ | the fixed field of $\varsigma$, when $\varsigma$ is an involution of a field $A$ |
| $B \otimes_F K$ | with the second-kind involution $\tau \otimes \varsigma$, whose fixed algebra is $(B^+ \otimes 1) \oplus (B^- \otimes t)$ |

## Further Reading

- Paul M. Cohn, *Algebra*, volume 1 (Wiley, second edition, 1982), for algebras with involution, the opposite algebra and the elementary properties of an anti-automorphism.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the semilinear maps, the descent from a quadratic extension and the trace of a quadratic extension.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the symmetric and skew elements of a ring with involution and the structures they carry.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the involutions of a simple algebra, the first and the second kind and the descent of a central simple algebra over a quadratic extension.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan algebra of the symmetric elements of an involution and the Lie algebra of the skew elements.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the classification of the involutions of a central simple algebra, which is Part II work and is named here only at the boundary.
