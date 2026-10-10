# __The Exponential Map on a Banach Sesqualgebra__

## Introduction

A Banach sesqualgebra carries two products: the associative product $xy$ of its envelope and the derived operation $x \star y = xy^{*}$. The exponential is a construction of the first alone. It is the series $\sum x^{n}/n!$, it needs the powers $x^{n}$ and therefore associativity, and the derived operation has no exponential at all, its powers depending on the bracketing because it is not associative. This article reads the exponential against the sesquilinear structure that the involution imposes, and the outcome is that the exponential belongs to the envelope while the involution carries the only statement of the layer: the **skew-Hermitian** elements exponentiate into the **unitary group**.

Three facts organise the article. The series converges absolutely for the submultiplicative norm, $\lVert\exp x\rVert \leq e^{\lVert x\rVert}$, and it defines a continuous map $A \to A^{\times}$ which is a homomorphism on commuting pairs: the exponential is an operation of the Banach algebra, and the sesquilinear layer does not enter its definition. The involution commutes with it, $(\exp x)^{*} = \exp(x^{*})$, because the involution is continuous and anti-multiplicative; the consequence is that Hermitian elements exponentiate into Hermitian elements and skew-Hermitian elements into unitary ones, $(\exp x)^{*} = (\exp x)^{-1}$, and the exponential of the skew-Hermitian part runs inside the identity component of $U(A)$. And the exponential is not surjective onto the unitary group: on $M_{n}(\mathbb{R})$ for odd $n$ the central element $-I$ is unitary and has determinant $-1$, while every exponential of a skew-Hermitian matrix has determinant $1$, and on the algebra of continuous functions on the circle the unitary of winding number one is not an exponential. The logarithm repairs the failure only locally.

The article defines the standing model and proves the convergence and the functional equation, reads the involution and the two Hermitian parities, treats the image of the skew-Hermitian part and the two failures of surjectivity, and compares the exponential of the sesqualgebra with the exponential of a Banach algebra. The algebraic objects are *Units and the Unitary Elements* and *Hermitian and Skew-Hermitian Elements*; the Lie structure of the skew-Hermitian part is *The Unitary Lie Algebra*; the topological group carried by the unitary elements is *The Unitary Group as a Topological Group*; the involution of a Banach algebra and its isometry are *The Continuity of the Involution* and *The Involution and the Spectral Radius*; and the general theory of the exponential of a Banach algebra is *The Lie Algebra and the Exponential Map*. Throughout, $(\mathbb{K},\varsigma)$ is $\mathbb{R}$ or $\mathbb{C}$ with its continuous involution, $A$ is a **unital Banach algebra** over $\mathbb{K}$ with an isometric $\varsigma$-semilinear involution $*$, carrying the derived product $x \star y = xy^{*}$, so that $A$ is a unital Banach sesqualgebra of *Banach Sesqualgebras*, §*The Derived Operation of an Involutive Banach Algebra*, whose envelope is the algebra $A$ itself; the norm is submultiplicative with $\lVert 1\rVert = 1$.

## The Envelope and the Series

### The Standing Model

**Definition.** The **envelope** of a sesqualgebra $A$ is the associative algebra whose product is the product of $A$ before the involution is inserted, so that the derived operation is read as $x \star y = xy^{*}$ in the envelope. For the objects of this article the envelope is the Banach algebra $A$ itself, and the exponential is taken in the envelope.

**Remark (why the envelope).** The definition is the one the menu blurb demands and it is forced by the series: a power $x^{n}$ is an iterated associative product, the derived operation has no canonical iterates, and an exponential of the derived operation is therefore not available. The article is accordingly a statement about a unital involutive Banach algebra, read as a sesqualgebra through its derived operation, and the involution is the only part of the sesquilinear structure that the exponential sees.

### The Convergence

**Theorem (the exponential series).** For every $x \in A$ the series

$$
\exp x = \sum_{n \geq 0} \frac{x^{n}}{n!}
$$

converges absolutely, $\exp 0 = 1$, and

$$
\lVert \exp x\rVert \leq e^{\lVert x\rVert}, \qquad \lVert \exp x - 1\rVert \leq e^{\lVert x\rVert} - 1 .
$$

The map $\exp : A \to A$ is continuous, and is Lipschitz on every bounded subset.

*Proof.* Submultiplicativity gives $\lVert x^{n}\rVert \leq \lVert x\rVert^{n}$, so the series of norms is dominated by $\sum \lVert x\rVert^{n}/n! = e^{\lVert x\rVert}$, which is finite; a normed space is complete, so the series converges absolutely by *Normed and Banach Spaces*, §*Banach Spaces and Series*. The two estimates are the same domination, the second applied to the terms of index $n \geq 1$. For continuity let $M = \max(\lVert x\rVert,\lVert y\rVert)$; then $\lVert x^{n} - y^{n}\rVert \leq \lVert x - y\rVert \sum_{k=0}^{n-1}\lVert x\rVert^{k}\lVert y\rVert^{n-1-k} \leq nM^{n-1}\lVert x - y\rVert$, and dividing by $n!$ and summing gives $\lVert \exp x - \exp y\rVert \leq e^{M}\lVert x - y\rVert$, since $\sum_{n \geq 1}nM^{n-1}/n! = e^{M}$. $\square$

### The Functional Equation

**Theorem (the exponential on commuting pairs).** If $xy = yx$ then $\exp(x+y) = \exp x\,\exp y$. Consequently $\exp x$ is invertible with $\exp(x)^{-1} = \exp(-x)$, the map $t \mapsto \exp(tx)$ is a continuous homomorphism $\mathbb{R} \to A^{\times}$, and $\exp : A \to A^{\times}$.

*Proof.* When $xy = yx$ the binomial theorem gives $(x+y)^{n} = \sum_{k}\binom{n}{k}x^{k}y^{n-k}$, and the Cauchy product of the two absolutely convergent series is $\sum_{n}\frac{1}{n!}\sum_{k}\binom{n}{k}x^{k}y^{n-k} = \exp(x+y)$, by *Normed and Banach Spaces*, §*Banach Spaces and Series*. The element $x$ commutes with $-x$, so $\exp x\,\exp(-x) = \exp 0 = 1$ and likewise in the other order; hence $\exp x \in A^{\times}$ with the stated inverse. The one-parameter statement is the functional equation read on the commuting pair $sx$, $tx$, which gives $\exp((s+t)x) = \exp(sx)\exp(tx)$, together with the continuity of $t \mapsto tx$ and of $\exp$. $\square$

**Remark.** The one-parameter subgroup $t \mapsto \exp(tx)$ is the exponential of the Banach algebra, and it is the curve along which the identity component of $A^{\times}$ is reached; the unitary group enters the picture only when $x$ is skew-Hermitian, in which case the curve runs inside $U(A)$ as the next section shows.

## The Involution and the Hermitian Elements

### The Involution and the Exponential

**Theorem (the involution commutes with the exponential).** For every $x \in A$,

$$
(\exp x)^{*} = \exp(x^{*}) .
$$

*Proof.* The involution is anti-multiplicative and of order two, so $(x^{n})^{*} = (x^{*})^{n}$ by induction; it is isometric by the standing hypothesis, hence continuous by *The Continuity of the Involution*, §*The $\mathrm{C}^{*}$-Condition*, and a continuous map commutes with the limits of convergent series. Applying it termwise to $\sum x^{n}/n!$ gives $\sum (x^{*})^{n}/n! = \exp(x^{*})$. $\square$

**Corollary (the parities pass to the exponential).** If $x$ is Hermitian, $x^{*} = x$, then $\exp x$ is Hermitian; if $x$ is skew-Hermitian, $x^{*} = -x$, then $\exp x$ is unitary with

$$
(\exp x)^{*} = \exp(x^{*}) = \exp(-x) = (\exp x)^{-1} .
$$

More generally, if $x$ is normal, $xx^{*} = x^{*}x$, then $\exp x$ is normal.

*Proof.* The Hermitian and the skew-Hermitian cases are the theorem read with $x^{*} = \pm x$, and the inverse in the second is the functional equation of §*The Functional Equation*, the element $-x$ commuting with $x$. For a normal $x$ the elements $x$ and $x^{*}$ commute, so $\exp(x^{*}) = (\exp x)^{*}$ commutes with $\exp x$. $\square$

### The Skew-Hermitian Elements

**Definition.** An element $x \in A$ is **skew-Hermitian** when $x^{*} = -x$; the set of them is the skew-Hermitian part $S(A)$ of *Hermitian and Skew-Hermitian Elements*, and it is the real Lie algebra of the unitary group under the commutator, by *The Unitary Lie Algebra*.

**Remark (over $\mathbb{R}$ there is no imaginary unit).** Over $\mathbb{C}$ the Hermitian and the skew-Hermitian elements are exchanged by the multiplication by $i$, and every element is a sum $h + s$ of a Hermitian and a skew-Hermitian part, $h = \tfrac12(x + x^{*})$ and $s = \tfrac12(x - x^{*})$; over $\mathbb{R}$ the two parts are the symmetric and the antisymmetric parts relative to the involution, the decomposition $x = h + s$ is available there as well because $2$ is invertible, and what is missing over $\mathbb{R}$ is only the exchange of the two parts by the multiplication by $i$. The exponential of the skew-Hermitian part is the bridge from the Lie algebra to the group, and it is a map over the reals in both cases.

### The Exponential into the Unitary Group

**Theorem (the exponential of the skew-Hermitian part lands in the identity component).** The exponential restricts to a continuous map

$$
\exp : S(A) \longrightarrow U(A) , \qquad \exp(S(A)) \subseteq U(A)_{0},
$$

where $U(A)_{0}$ is the component of the identity of the unitary group of *The Unitary Group as a Topological Group*.

*Proof.* The corollary gives $\exp x \in U(A)$ for $x \in S(A)$. The path $t \mapsto \exp(tx)$, $t \in [0,1]$, is continuous by §*The Functional Equation*, takes the value $\exp 0 = 1$ at $0$ and $\exp x$ at $1$, and its values are unitary because $tx$ is skew-Hermitian for every real $t$; so $\exp x$ is joined to $1$ inside $U(A)$, which is the definition of the identity component. $\square$

**Remark.** The theorem is the reason the skew-Hermitian part is called the Lie algebra of the unitary group: the exponential is the map that carries it into the group, it is the source of the one-parameter subgroups, and the failure of its surjectivity is exactly the difference between the group and the image of its Lie algebra.

## The Image and Its Defects

### The Failure of Surjectivity

**Theorem (the exponential is not surjective onto the unitary group).** Let $A = M_{n}(\mathbb{R})$ with the transpose as the involution, the operator norm and the derived product $X \star Y = XY^{\mathsf{T}}$, and let $n$ be odd. Then $-I$ is unitary, $-I \in U(A) \setminus \exp(S(A))$, and $U(A)$ is not connected.

*Proof.* The matrix $-I$ satisfies $(-I)(-I)^{\mathsf{T}} = I$, so it is unitary, and it is Hermitian with $(-I)^{2} = I$. A skew-Hermitian matrix of the article is a skew-symmetric one, $X^{\mathsf{T}} = -X$; its exponential is orthogonal, $\exp(X)\exp(X)^{\mathsf{T}} = I$ by the corollary, and $\det\exp(X) = e^{\operatorname{tr}X} = e^{0} = 1$, since the diagonal of a skew-symmetric matrix vanishes. Hence $\exp(X) \in \mathrm{SO}(n)$, whereas $\det(-I) = (-1)^{n} = -1$ for odd $n$, so $-I \notin \exp(S(A))$ and in particular $-I \notin U(A)_{0}$; the unitary group therefore has at least the two components of the determinant $\pm1$. $\square$

**Theorem (the exponential is not surjective in infinite dimension).** Let $A = C(X,\mathbb{C})$ for $X = S^{1}$, with the supremum norm, the involution $\sigma(f) = \bar f$ relative to the conjugation of the scalars, and the derived product $f \star g = f\,\bar g$. Then the unitary group is $U(A) = \{f : \lvert f\rvert = 1\} = C(S^{1},S^{1})$, the skew-Hermitian part is $S(A) = \{ig : g \ \text{real continuous}\}$, and the element $f_{0}(z) = z$ is unitary and not in $\exp(S(A))$.

*Proof.* The element $f$ is unitary exactly when $f\bar f = 1$, that is $\lvert f\rvert = 1$; and it is skew-Hermitian exactly when $\bar f = -f$, that is $f = ig$ with $g$ real valued. For real continuous $g$ the map $t \mapsto e^{itg}$ is a continuous path in $U(A)$ from the constant $1$ to $e^{ig}$, so $\exp(ig) = e^{ig}$ and $e^{ig}$ lies in the identity component of $U(A)$; equivalently, its winding number around the origin is zero, because it is homotopic to a constant through the unitary elements. The element $f_{0}(z) = z$ has winding number one, so it is not in the identity component and not in the image of the exponential. $\square$

**Remark (the two failures are different).** On $M_{n}(\mathbb{R})$ the obstruction is the disconnectedness of the orthogonal group and it is finite-dimensional and of order two; on $C(S^{1},\mathbb{C})$ the obstruction is a degree, it is infinite-dimensional, and the components of $U(A)$ are indexed by the winding number, whose group is $\mathbb{Z}$. Both are instances of the same statement, that the exponential of a Lie algebra reaches no further than the identity component of its group.

### The Logarithm

**Theorem (the logarithm is a local inverse).** Let $y \in A$ with $\lVert y\rVert < 1$. Then the series

$$
\log(1+y) = \sum_{n \geq 1} \frac{(-1)^{n+1}}{n}\,y^{n}
$$

converges absolutely with $\lVert\log(1+y)\rVert \leq -\log(1-\lVert y\rVert)$, and $\exp(\log(1+y)) = 1+y$. Conversely, if $\lVert x\rVert < \log 2$ then $\lVert\exp x - 1\rVert \leq e^{\lVert x\rVert} - 1 < 1$ and $\log(\exp x) = x$. Hence the exponential is a homeomorphism of a neighbourhood of $0$ onto a neighbourhood of $1$.

*Proof.* Absolute convergence follows from $\lVert y^{n}\rVert \leq \lVert y\rVert^{n}$ and the convergence of the real logarithm series for $\lVert y\rVert < 1$, and the estimate is the real estimate read on the norms. The identity $\exp\log(1+y) = 1+y$ is the Cauchy product of the two series, which converges because it converges in the commutative subalgebra generated by $y$: the real identity $\exp\log(1+t) = 1+t$ holds for $\lvert t\rvert < 1$ and it is an identity of power series, so it holds for the element $y$ of norm less than one. The converse is the same power-series identity $\log\exp(t) = t$ at $t = x$, admissible because the series for $\log(\exp x - 1)$ converges as soon as $\lVert\exp x - 1\rVert < 1$, which is the case under $\lVert x\rVert < \log 2$. $\square$

**Remark.** The logarithm is the two-sided inverse of the exponential near the origin and nowhere else in general; the theorem makes of $\exp$ a chart of the Banach Lie group $A^{\times}$ at the identity, and the failures of §*The Failure of Surjectivity* are exactly the global obstructions to extending it.

## The Comparison with the Exponential of a Banach Algebra

### The Collapse at the Trivial Involution

**Theorem (the comparison).** Let $\varsigma = \mathrm{id}$. Then $A$ is a unital Banach algebra with a continuous isometric involution, the derived operation is the algebra product read through $*$, and the exponential of the article is the exponential of the Banach algebra $A$: the series, the convergence, the functional equation and the logarithm are those of *The Lie Algebra and the Exponential Map*, §*The Exponential Map*, applied to $A$. The sesquilinear layer adds exactly the two statements that the Hermitian part is closed under the exponential and that the skew-Hermitian part is exponentiated into the unitary group.

*Proof.* At $\varsigma = \mathrm{id}$ the second scalar rule is the first and the product is $\mathbb{K}$-bilinear, so $A$ is a Banach algebra with involution, by the collapse theorem of *Banach Sesqualgebras*, §*The Collapse*; the exponential series names only the associative product and the scalar field, so it is the exponential of that algebra. The two additional statements are the corollary of §*The Involution and the Exponential*, which uses the involution alone. $\square$

### Why the Derived Operation Has No Exponential

**Theorem (the iterates of the derived operation are bracketing-dependent).** The derived operation is not associative, and a power of a single element under it is not defined without a bracketing. Over $\mathbb{R}$ and in $M_{2}(\mathbb{R})$, with the transpose and $x = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$,

$$
(x \star x) \star x = E_{11} + 2E_{12} + E_{21} + 3E_{22} \neq E_{11} + E_{12} + 2E_{21} + 3E_{22} = x \star (x \star x) .
$$

*Proof.* The products are computed from $x \star y = xy^{\mathsf{T}}$: for $x = E_{11} + E_{21} + E_{22}$ one has $x^{\mathsf{T}} = E_{11} + E_{12} + E_{22}$ and $x \star x = xx^{\mathsf{T}} = E_{11} + E_{12} + E_{21} + 2E_{22}$, whence $(x \star x) \star x = (x \star x)x^{\mathsf{T}}$ and $x \star (x \star x) = x(x \star x)^{\mathsf{T}}$, which are the two displayed matrices. $\square$

**Remark.** The theorem is the reason the article is written on the envelope. A series $\sum x_{\star}^{n}/n!$ in the derived operation would depend on the choice of bracketing at every order, so no exponential of the derived operation exists; what the sesquilinear structure supplies is the involution, and through it the identification of the skew-Hermitian part with the Lie algebra of the unitary group. The exponential is thus an operation of the bilinear layer whose *meaning* in the sesquilinear layer is the passage from a Lie algebra to its group, and the article is the record of that passage.

## Examples

### The Matrices

**Example (the complex matrices, verdict: the exponential onto $U(n)$).** Let $A = M_{n}(\mathbb{C})$ with the operator norm, the conjugation, the conjugate transpose and $X \star Y = XY^{*}$. The skew-Hermitian matrices are the matrices $X$ with $X^{*} = -X$, that is $X = iH$ with $H$ Hermitian, and $\exp$ is the matrix exponential; it maps the skew-Hermitian matrices onto the connected group $U(n)$, since every unitary matrix is $e^{iH}$ for a Hermitian $H$, by the spectral theorem of *Self-Adjoint Operators and the Spectral Theorem*. The article's failure of surjectivity is therefore absent here, and its presence in $M_{n}(\mathbb{R})$ is the price of the disconnectedness of $O(n)$.

**Example (the real matrices of odd size, verdict: $-I$ is not an exponential).** The object of §*The Failure of Surjectivity* with $n$ odd: $-I$ is a Hermitian unitary element, $(-I)^{2} = I$ and $(-I)^{*} = -I$, and it is not the exponential of a skew-Hermitian matrix; the verdict is that the exponential of the Lie algebra is a proper part of the unitary group, and that the Hermitian unitary elements of *Units and the Unitary Elements* are not all reachable from the Lie algebra. The smallest cases make both sides explicit: at $n=2$

$$
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=H^{*},\qquad iH=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=-(iH)^{*},\qquad e^{iH}=\begin{pmatrix}e^{i}&0\\0&e^{-i}\end{pmatrix}\in U(2),
$$

and at $n=1$ over $\mathbb{R}$

$$
-1\in M_1(\mathbb{R}),\qquad (-1)^{*}=-1,\qquad -1\neq e^{0}=1,
$$

so the only skew-Hermitian real number is $0$ and $-1$ is out of reach.

### The Field and the Quaternions

**Example (the field, verdict: the exponential onto the circle).** Let $A = \mathbb{C}$ with the modulus, the conjugation and $z \star w = z\bar w$. The skew-Hermitian elements are the purely imaginary numbers $z = i\theta$ with $\theta$ real, the unitary group is the circle $U(\mathbb{C}) = \{z : \lvert z\rvert = 1\}$, and $\exp(i\theta) = e^{i\theta}$ maps $\mathbb{R}$ onto the circle, so here the exponential is surjective. The example is the one-dimensional model of the surjectivity that fails in $M_{n}(\mathbb{R})$ and in $C(S^{1},\mathbb{C})$.

**Example (the quaternions, verdict: the exponential onto $S^{3}$).** Let $A = \mathbb{H}$ over $\mathbb{R}$ with the quaternion conjugation and the Euclidean norm. The skew-Hermitian elements are the purely imaginary quaternions, the unitary group is the sphere $S^{3}$, and for $v = \theta u$ with $u$ imaginary of norm one, $\exp v = \cos\theta + u\sin\theta$, so the exponential maps the Lie algebra onto $S^{3}$; the map is surjective and every unit quaternion is $\cos\theta + u\sin\theta$ for some $\theta$ and $u$. The example is the compact division-algebra case, where the exponential reaches the whole unitary group and the only failure is the loss of injectivity at the multiples of $2\pi$.

### The Functions

**Example (the continuous functions on the circle, verdict: the winding number).** The object of §*The Failure of Surjectivity*: the unitary group is $C(S^{1},S^{1})$, the skew-Hermitian part is the functions $ig$ with $g$ real, and the exponential is $g \mapsto e^{ig}$, whose image is the class of the maps of winding number zero; the verdict is that the exponential of the Lie algebra misses every component of positive or negative winding, and that the components of the unitary group are counted by a degree and not by a sign as in the orthogonal case.

## Summary

The **exponential** of a unital Banach sesqualgebra is the series $\exp x = \sum x^{n}/n!$ taken in the **envelope**, the associative product $xy$ out of which the derived operation $\star$ is built; it converges absolutely by submultiplicativity, $\lVert\exp x\rVert \leq e^{\lVert x\rVert}$, it is continuous and Lipschitz on bounded sets, and it satisfies $\exp(x+y) = \exp x\,\exp y$ for commuting $x$ and $y$, so that $\exp x$ is invertible with $\exp(x)^{-1} = \exp(-x)$ and $t \mapsto \exp(tx)$ is a continuous one-parameter subgroup of $A^{\times}$. The involution commutes with it, $(\exp x)^{*} = \exp(x^{*})$, because the involution is continuous and anti-multiplicative; hence **Hermitian elements exponentiate into Hermitian elements**, **skew-Hermitian elements into unitary ones**, $(\exp x)^{*} = (\exp x)^{-1}$, and the exponential of the skew-Hermitian part lands in the **identity component** of the unitary group. The exponential is not surjective onto $U(A)$: on $M_{n}(\mathbb{R})$ for odd $n$ the unitary $-I$ has determinant $-1$ while every skew-symmetric exponential has determinant $1$, and on $C(S^{1},\mathbb{C})$ the unitary of winding number one is not an exponential; the **logarithm** $\log(1+y) = \sum(-1)^{n+1}y^{n}/n$ inverts the exponential on a neighbourhood of the identity and nowhere else in general. At $\varsigma = \mathrm{id}$ the object is a Banach algebra with involution and the exponential is the exponential of a Banach algebra, the layer adding only the two statements about the Hermitian parities. The derived operation carries **no** exponential, its iterates being bracketing-dependent, and that is why the article is written on the envelope.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\exp x = \sum_{n \geq 0} x^{n}/n!$ | the exponential, taken in the envelope |
| $\lVert\exp x\rVert \leq e^{\lVert x\rVert}$ | the absolute convergence, by submultiplicativity |
| $\exp(x+y) = \exp x\,\exp y$ (for $xy = yx$) | the functional equation on commuting pairs |
| $(\exp x)^{*} = \exp(x^{*})$ | the involution commutes with the exponential |
| $x^{*} = x \Rightarrow (\exp x)^{*} = \exp x$ | the Hermitian part is closed |
| $x^{*} = -x \Rightarrow (\exp x)^{*} = (\exp x)^{-1}$ | the skew-Hermitian part lands in $U(A)$ |
| $\exp(S(A)) \subseteq U(A)_{0}$ | the exponential runs in the identity component |
| $\log(1+y) = \sum_{n \geq 1}(-1)^{n+1}y^{n}/n$ | the local inverse, for $\lVert y\rVert < 1$ |
| $(x \star x) \star x \neq x \star (x \star x)$ | the derived operation has no exponential |
| $\varsigma = \mathrm{id}$ | the collapse: the exponential of a Banach algebra |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the exponential of a Banach algebra, the one-parameter subgroups and the unitary group.
- Theodore W. Palmer, *Banach Algebras and the General Theory of \*-Algebras, Volume I* (Cambridge University Press, 1994), for the exponential series, the group of units and the involutions of a Banach algebra.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the logarithm, the exponential chart and the topological structure of the group of units.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the exponential of a Lie algebra, the identity component and the failures of surjectivity.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the Hermitian and skew-Hermitian elements and the unitary group of a ring with involution.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 1–3* (Springer, 1989), for the exponential map of a Lie group and the exponential of its Lie algebra.
