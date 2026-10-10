# __The Hermitian Jordan Algebra__

## Introduction

An involution of a sesqualgebra selects the elements it fixes, and those elements are closed under the symmetrised product. The **Hermitian Jordan algebra** of $A$ is the Hermitian part

$$
J(A) = \bigl(H(A), \circ\bigr), \qquad x \circ y = \tfrac12\bigl(xy^{*} + yx^{*}\bigr) = \tfrac12\bigl(xy + yx\bigr) \text{ on } H(A),
$$

the set $H(A) = \{x : x^{*} = x\}$ with the symmetrised product. It is the single place in the sesquilinear layer where the symmetrisation of the product is a Jordan product, and this article reads the Jordan algebra that arises there: its axioms, the scalars it is an algebra over, its idempotents and Peirce decomposition, its degree, its quadratic representation and its standard cases.

The whole of the article turns on one difference from the bilinear case. For an involution of an algebra the self-adjoint part is a vector space over the base field and the Jordan algebra is an algebra over that field; for a sesqualgebra the two halves are only modules over the **fixed ring** $R^{\varsigma}$, and the Hermitian Jordan algebra is an algebra over $R^{\varsigma}$ and not over $R$. The bilinear theory is *The Self-Adjoint Part of an Algebra*, and the present article is its sesquilinear counterpart, obtained by cutting the scalars down to the fixed ring and keeping everything else.

The setting is that of *Sesqualgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ is an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, and $2$ is invertible in $R$. The two halves, their scalar action and the closure of $H(A)$ under the symmetrised product are *Hermitian and Skew-Hermitian Elements*; the symmetrised product itself, its scalar rules and the failure of the Jordan identity off $H(A)$ are *The Sesquilinear Symmetrised Product*; the Hermitian idempotents and the associative Peirce decomposition are *Hermitian Idempotents and the Peirce Decomposition*; the Hermitian squares and the cone they generate are *Hermitian Squares and the Algebraic Positive Cone*; the general theory of Jordan algebras, their Peirce spaces, their trace forms and their degree is *Jordan Algebras*; and the Lie algebra carried by the other half is *The Unitary Lie Algebra*.

---

## The Hermitian Jordan Algebra

### The Definition

**Definition.** The **Hermitian Jordan algebra** of $A$ is the pair $J(A) = (H(A), \circ)$ formed by the Hermitian elements and the symmetrised product

$$
x \circ y = \tfrac12\bigl(xy + yx\bigr),
$$

the sesquilinear product $x \star y = xy^{*}$ and its symmetrisation being those of *The Sesquilinear Symmetrised Product*. The **square** of an element of $J(A)$ is $x^{\circ 2} = x \circ x = x^{2}$, and the unit is the unit $1$ of $A$, which is Hermitian.

### The Axioms

**Theorem.** $J(A)$ is a commutative Jordan algebra over the fixed ring $R^{\varsigma}$: the product $\circ$ is commutative and $R^{\varsigma}$-bilinear, and it satisfies the Jordan identity

$$
(x \circ y) \circ (x \circ x) = x \circ \bigl(y \circ (x \circ x)\bigr)
$$

for all $x, y \in H(A)$.

**Proof.** On $H(A)$ the symmetrised sesquilinear product is the plain symmetrisation $\tfrac12(xy+yx)$, and that is the symmetrisation of the associative product of $A$; the symmetrisation of an associative algebra satisfies the Jordan identity, by *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*. Commutativity is by construction, and the $R^{\varsigma}$-bilinearity is the scalar theorem of *The Sesquilinear Symmetrised Product*: each slot of $\circ$ receives one linear and one conjugate-linear contribution, and the fixed ring is exactly what survives. $\square$

**Remark.** No hypothesis beyond the associativity of $A$ and the invertibility of $2$ is used, and none is needed: the identity is inherited from the envelope rather than verified in the Jordan algebra. The unit $1$ acts as the identity of $J(A)$ because $1 \circ x = \tfrac12(x + x) = x$ for a Hermitian $x$, and $1$ is Hermitian by *Units and the Unitary Elements*, §*The Unit is Hermitian*.

### The Envelope

**Proposition.** $J(A)$ is a special Jordan algebra and its envelope is the associative algebra $A$ with its involution: $J(A)$ is the Hermitian part of the fixed algebra of $*$ inside the symmetrisation $A^{+}$ of $A$.

**Proof.** $H(A)$ is contained in $A$ and is closed under $\circ$, so $J(A)$ is a Jordan subalgebra of the symmetrisation $A^{+}$ of the associative algebra $A$, and a Jordan algebra that is a subalgebra of the symmetrisation of an associative algebra is special, that algebra being its envelope (*Special and Exceptional Jordan Algebras*). $\square$

**Remark.** The envelope is the whole algebra, not the Hermitian part, and this is what makes every computation in $J(A)$ an ordinary associative computation followed by a symmetrisation. The exceptional Jordan algebras have no such envelope, and none arises here: the involution can only cut a piece out of an associative algebra, it cannot manufacture a new kind of algebra.

### Powers

**Proposition.** $J(A)$ is power-associative, and for a Hermitian $x$ the powers of the Jordan algebra are the ordinary powers,

$$
x^{\circ n} = x^{n} \qquad (n \geq 1).
$$

**Proof.** A Jordan algebra is power-associative (*Jordan Algebras*, §*Power Associativity*); the identification $x^{\circ n} = x^n$ is induction on $n$, the product on a single Hermitian element being the ordinary symmetrisation and the element commuting with its own powers. $\square$

**Remark.** The subalgebra of $J(A)$ generated by one Hermitian element is therefore the span over $R^{\varsigma}$ of its powers, $R^{\varsigma}[x]$, an associative and commutative algebra, the Jordan algebra generated by one element being associative in general. Every square-root problem in $A$ is a problem in $J(A)$ alone; the worked instance is *Biquaternion Square Roots of a General Element*.

## The Scalars

### The Fixed Ring

**Proposition.** $H(A)$ is a module over $R^{\varsigma}$ and not over $R$ in general, and $J(A)$ is an algebra over $R^{\varsigma}$ and not over $R$. A scalar $\lambda$ with $\varsigma(\lambda) = -\lambda$ carries $H(A)$ into $S(A)$, so it is not a scalar of $J(A)$.

**Proof.** For $\lambda \in R^{\varsigma}$ and $h \in H(A)$, $(\lambda h)^{*} = \varsigma(\lambda)h^{*} = \lambda h$, so $\lambda h \in H(A)$; for $\varsigma(\lambda) = -\lambda$ the same computation gives $(\lambda h)^{*} = -\lambda h$, so $\lambda h \in S(A)$ and the scalar leaves the Hermitian part. The scalars preserving $H(A)$ are those with $(\varsigma(\lambda) - \lambda)H(A) = 0$, a set that contains the fixed ring and equals it when $H(A)$ has zero annihilator in $R$, over an integral domain for instance; this is *Hermitian and Skew-Hermitian Elements*, §*The Scalar Action*, and the counterexample over a ring with zero divisors is *The Unitary Lie Algebra*, §*The Scalars*. $\square$

**Remark.** The scalar story is the one structural place where the sesquilinear Jordan algebra differs from the bilinear one: over a field the self-adjoint part of *The Self-Adjoint Part of an Algebra* is a vector space over that field, whereas here the scalars are cut down to the fixed ring. In the model $M_n(\mathbb{C})$ with the conjugate transpose the fixed ring is $\mathbb{R}$ and $J(A)$ is a real Jordan algebra while the ambient algebra is a complex one; the multiplication by $i$ is the scalar with $\varsigma(\lambda) = -\lambda$ that carries the Hermitian matrices to the skew-Hermitian ones, which is the statement that the two halves of $A$ are two real forms and not two complex subspaces.

### The Trace Form

**Proposition.** Let $\tau$ be a trace on $A$, that is an additive map with $\tau(xy) = \tau(yx)$. Then

$$
\tau(x \circ y) = \tau(xy)
$$

defines a symmetric $R^{\varsigma}$-bilinear form on $J(A)$, the trace form of the Jordan algebra.

**Proof.** $\tau(x \circ y) = \tfrac12\bigl(\tau(xy) + \tau(yx)\bigr) = \tau(xy)$ by the trace property, and $\tau(xy) = \tau(yx)$ shows the symmetry. The $R^{\varsigma}$-bilinearity is inherited from the product. $\square$

**Remark.** For $A = M_n(\mathbb{C})$ with the ordinary trace the form is $\mathrm{Tr}(x \circ y) = \mathrm{Tr}(xy)$, and on Hermitian $x, y$ it takes real values, being the trace of the product of two Hermitian matrices; it is the trace form of the Jordan algebra and not a form on the ambient algebra, and its general theory, its non-degeneracy and its role in the classification are *Jordan Algebras*, §*The Trace Form*. No positivity, no order and no distance is claimed of it here.

## Idempotents and the Peirce Decomposition

### The Hermitian Idempotents

**Proposition.** The idempotents of the Jordan algebra $J(A)$ are the idempotents of $A$ that are Hermitian:

$$
e \circ e = e \iff e^{2} = e = e^{*} .
$$

**Proof.** $e \circ e = \tfrac12(e^2 + e^2) = e^2$, so $e \circ e = e$ is $e^2 = e$; an element of $J(A)$ is Hermitian by definition. $\square$

The Hermitian idempotents, their involution-invariance and their behaviour under the derived operation are *Hermitian Idempotents and the Peirce Decomposition*, §*Idempotents and Hermitian Idempotents*.

### Jordan Orthogonality

**Definition.** Two idempotents $e, f$ of $J(A)$ are **Jordan orthogonal** when $e \circ f = 0$.

**Proposition.** Let $e, f \in H(A)$ be Hermitian idempotents. Then $e \circ f = 0$ if and only if $ef = fe = 0$.

**Proof.** $e \circ f = \tfrac12(ef + fe)$, so Jordan orthogonality is $ef + fe = 0$. Multiplying by $e$ on the left and on the right gives $efe = -ef$ and $efe = -fe$, whence $ef = fe$; together with $ef = -fe$ and the invertibility of $2$ this gives $ef = 0$. The converse is immediate. $\square$

**Remark.** Jordan orthogonality is the ordinary vanishing of the product for Hermitian idempotents, so a family of pairwise Jordan-orthogonal Hermitian idempotents is a family of pairwise orthogonal projections; the partial order and the compatibility of such families with the involution are read in *Hermitian Idempotents and the Peirce Decomposition*, §*Orthogonality and the Partial Order*.

### The Peirce Decomposition

**Theorem.** Let $e$ be a Hermitian idempotent of $A$ and put $f = 1 - e$. Then $f$ is a Hermitian idempotent, the Jordan algebra splits as

$$
J(A) = \mathrm{J}_1(e) \oplus \mathrm{J}_{1/2}(e) \oplus \mathrm{J}_0(e),
$$

where $\mathrm{J}_\lambda(e)$ is the $\lambda$-eigenspace of the operator $x \mapsto e \circ x$ on $J(A)$, and the three spaces are the Hermitian parts of the associative Peirce spaces of $e$:

$$
\mathrm{J}_1(e) = H(A) \cap eAe , \qquad \mathrm{J}_{1/2}(e) = H(A) \cap \bigl(eAf \oplus fAe\bigr) , \qquad \mathrm{J}_0(e) = H(A) \cap fAf .
$$

**Proof.** The associative Peirce decomposition $A = eAe \oplus eAf \oplus fAe \oplus fAf$ is recalled in *Hermitian Idempotents and the Peirce Decomposition*, §*The Classical Splitting*, and the involution exchanges the two mixed spaces and fixes the two corners; a Hermitian element therefore has Hermitian components in the three groups $eAe$, $eAf \oplus fAe$ and $fAf$, so $H(A)$ is the sum of the three Hermitian parts displayed. For $h \in H(A) \cap eAe$ one has $eh = h = he$, so $e \circ h = h$; for $h = u + u^{*}$ with $u = eaf \in eAf$ one has $eh = u$ and $he = u^{*}$, so $e \circ h = \tfrac12 h$; and for $h \in H(A) \cap fAf$ one has $eh = he = 0$, so $e \circ h = 0$. The three spaces are therefore eigenspaces for the three distinct eigenvalues $1, \tfrac12, 0$, hence independent and direct, and their sum is $H(A)$. $\square$

**Remark.** The Peirce decomposition of the Jordan algebra is the Hermitian part of the Peirce decomposition of the associative algebra, component by component: the corners of the Jordan algebra are the Hermitian parts of the corners, $R^{\varsigma}e$ and $R^{\varsigma}f$, and the middle space is the Hermitian part of the two mixed spaces together, which is where the off-diagonal part of a Hermitian element lives. The three eigenvalues $1, \tfrac12, 0$ are those of a Jordan algebra in general (*Jordan Algebras*, §*The Peirce Spaces*), and the superscript of $\mathrm{J}_{1/2}$ is the halving that the invertibility of $2$ supplies.

### The Degree

**Definition.** A family of pairwise Jordan-orthogonal idempotents of $J(A)$ summing to the unit is **complete**, and the number of its members is the **degree** of the Jordan algebra.

**Proposition.** For $A = M_n(\mathbb{C})$ with the conjugate transpose the Hermitian idempotents are the orthogonal projections of $\mathbb{C}^{n}$ and the degree is $n$; for $n = 1$, and for the field $\mathbb{C}$ with the conjugation, the degree is $1$.

**Proof.** A Hermitian idempotent is a matrix $P$ with $P^2 = P = P^{*}$, that is an orthogonal projection, and its image is the subspace it projects onto. A complete family of pairwise Jordan-orthogonal Hermitian idempotents is a family of pairwise orthogonal projections summing to the identity, that is an orthogonal decomposition of $\mathbb{C}^{n}$ into the images; such a decomposition has at most $n$ nonzero members, and the $n$ matrix units $E_{11}, \dots, E_{nn}$ realise the bound, so the degree is $n$. For $n = 1$ the only nonzero idempotent is $1$, and for $\mathbb{C}$ with the conjugation the Hermitian elements are real and $1$ is the only nonzero idempotent; in both cases the degree is $1$. $\square$

**Remark.** The degree is the number of the pieces of a complete orthogonal decomposition, and it is not the number of elements of a basis of $J(A)$: the two coincide only in the smallest cases. In the biquaternion layer the same invariant is two, the Hermitian subspace carrying two orthogonal idempotents, as recorded in *Remarkable Subspaces and the Four General Products*.

## The Quadratic Representation

**Definition.** For $x \in H(A)$ the **quadratic representation** is the operator

$$
U_x : J(A) \longrightarrow J(A), \qquad U_x(y) = 2\,x \circ (x \circ y) - (x \circ x) \circ y .
$$

**Proposition.** $U_x$ takes its values in $J(A)$, is $R^{\varsigma}$-linear, and read through the associative product of $A$ it is

$$
U_x(y) = xyx .
$$

**Proof.** For $y \in H(A)$ the element $xyx$ is Hermitian, $(xyx)^{*} = x^{*}y^{*}x^{*} = xyx$, so the operator preserves $J(A)$, and it is $R^{\varsigma}$-linear because the product is $R^{\varsigma}$-bilinear on the Hermitian part. Expanding, $x \circ (x \circ y) = \tfrac14(x^{2}y + 2xyx + yx^{2})$ and $(x \circ x)\circ y = \tfrac12(x^{2}y + yx^{2})$, so the combination displayed is $xyx$. $\square$

**Corollary.** $U_x(x) = x^{3}$ and $U_1 = \mathrm{id}$; the map $x \mapsto U_x$ is quadratic in $x$, and it replaces the associativity that the Jordan product does not have, in the sense that the products of three elements of $J(A)$ are governed by it.

**Proof.** $x x x = x^{3}$ and $1y1 = y$; the quadratic dependence is read from the definition, which is homogeneous of degree two in $x$ and linear in $y$. $\square$

## Worked Cases

### The Complex Matrices

For $A = M_n(\mathbb{C})$ with the conjugate transpose the Hermitian Jordan algebra is the real vector space of the Hermitian matrices with the symmetrised product $\tfrac12(xy + yx)$, spanned over $\mathbb{R}$ by the $n$ diagonal units $E_{ii}$ and the $n(n-1)$ Hermitian and skew-Hermitian off-diagonal combinations $E_{ij} + E_{ji}$ and $i(E_{ij} - E_{ji})$. Its degree is $n$; its trace form is $\mathrm{Tr}(xy)$, real-valued on it; its idempotents are the orthogonal projections; and at the idempotent $E_{11}$ its Peirce spaces are $\mathbb{R}E_{11}$, the Hermitian off-diagonal matrices, and $\mathbb{R}E_{22}$, the eigenvalues being $1, \tfrac12, 0$. The algebra is the Jordan algebra of the Hermitian matrices of *Jordan Algebras*, §*Hermitian Matrices*, read over the fixed ring.

### The Field

For $A = \mathbb{C}$ over the datum $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation and the derived product $x \star y = x\bar y$, the Hermitian elements are the real numbers, so $J(A) = \mathbb{R}$ with the ordinary multiplication, of degree $1$. The symmetrised product of two complex numbers is $\mathrm{Re}(x\bar y)$, a real number, and its restriction to the Hermitian part is the multiplication of the reals; the case is the smallest in which the fixed ring is a proper subring of $R$ and the Jordan algebra a proper real form of the algebra.

### The Quaternions

For $A = \mathbb{H}$ with the quaternion conjugation over the datum $(\mathbb{R},\mathrm{id})$ the twist is invisible and the product is bilinear, so the case belongs to *The Self-Adjoint Part of an Algebra*; the Hermitian elements are the real quaternions and $J(A) = \mathbb{R}$ has degree $1$. It is the case in which the sesquilinear layer and the bilinear one coincide, the fixed ring being the whole of $R$, and it is recorded to mark the boundary.

### The Biquaternion Algebra

For $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the star-involution the Hermitian subspace is a Jordan algebra of degree two over $\mathbb{R}$, isomorphic to $H_2(\mathbb{C})$, with the two idempotents $\tilde{\Pi}_1$ and $\tilde{\Pi}_2$ as a complete Jordan-orthogonal family and the Peirce spaces of $\tilde{\Pi}_1$ reading $\mathbb{C}\tilde{\Pi}_1$, the span of $e_1$ and $e_2$, and $\mathbb{C}\tilde{\Pi}_2$. That layer is *The 12 Products of the Biquaternion Complex Space* and *Remarkable Subspaces and the Four General Products*, and it is the worked case in which everything of this article is computed on a basis of eight elements.

## Summary

The Hermitian elements of a sesqualgebra with a $\varsigma$-semilinear involution form, under the symmetrised product $x \circ y = \tfrac12(xy + yx)$, a commutative Jordan algebra over the fixed ring $R^{\varsigma}$. It is special with envelope $A$, it is power-associative with $x^{\circ n} = x^{n}$ on the Hermitian elements, and it carries a symmetric trace form $\tau(x \circ y) = \tau(xy)$ whenever the algebra carries a trace. Its idempotents are the Hermitian idempotents of $A$, its Jordan orthogonality is the vanishing of the product for them, its degree is the length of a complete orthogonal decomposition, and its Peirce decomposition at a Hermitian idempotent $e$ is the Hermitian part of the associative Peirce decomposition of $A$ at $e$, with the eigenvalues $1, \tfrac12, 0$ on the Hermitian parts of the corner $eAe$, of the mixed spaces and of the corner $fAf$. Its quadratic representation is $U_x(y) = xyx$.

The one structural difference from the bilinear theory of *The Self-Adjoint Part of an Algebra* is the scalars: the base involution is not the identity, the two halves are modules over the fixed ring and not over $R$, and the Jordan algebra is an algebra over $R^{\varsigma}$. Everything else is inherited, and inherited from the envelope: the Jordan identity is the associativity of $A$ read through the symmetrisation, which is the reason the identity holds here and fails for the symmetrised sesquilinear product off the Hermitian part, as *The Sesquilinear Symmetrised Product* records.

## Summary of Notation

| symbol | meaning |
|---|---|
| $J(A) = (H(A), \circ)$ | the Hermitian Jordan algebra |
| $H(A) = \{x : x^{*} = x\}$ | the Hermitian elements, the underlying set of $J(A)$ |
| $x \circ y = \tfrac12(xy + yx)$ | the symmetrised product, on $H(A)$ |
| $R^{\varsigma}$ | the fixed ring, the scalars of $J(A)$ |
| $\tau(x \circ y) = \tau(xy)$ | the trace form of the Jordan algebra |
| $e \circ e = e \iff e^2 = e = e^{*}$ | the idempotents of $J(A)$ |
| $e \circ f = 0 \iff ef = fe = 0$ | Jordan orthogonality of Hermitian idempotents |
| $\mathrm{J}_1 \oplus \mathrm{J}_{1/2} \oplus \mathrm{J}_0$ | the Peirce decomposition, the Hermitian parts of $eAe$, $eAf \oplus fAe$ and $fAf$ |
| $U_x(y) = 2\,x \circ (x \circ y) - (x \circ x) \circ y = xyx$ | the quadratic representation |
| $x^{\circ n} = x^{n}$ | the powers of a Hermitian element |
| the degree | the number of members of a complete Jordan-orthogonal family of idempotents |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan axioms, the symmetrisation of an associative algebra, the special algebras and their envelopes, the Peirce decomposition and the degree.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebras, the quadratic representation and the trace form.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the Hermitian elements of an involutive ring and the symmetrised product they carry.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of an algebra and the two halves they cut.
- The companion articles of this series: *Sesqualgebras*, *The Sesquilinear Symmetrised Product*, *Hermitian and Skew-Hermitian Elements*, *Hermitian Idempotents and the Peirce Decomposition*, *Units and the Unitary Elements*, *The Unitary Lie Algebra*, *Hermitian Squares and the Algebraic Positive Cone*, and *The Self-Adjoint Part of an Algebra*.
