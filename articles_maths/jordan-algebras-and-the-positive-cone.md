# __Jordan Algebras and the Positive Cone__

## Introduction

This article is an application of the Jordan theory to convex geometry. The base structure is a **commutative ring** $R$ with identity $1 \neq 0$, but the results are specific to the formally real algebras over $\mathbb{R}$, where a cone can be defined. The Jordan conventions are those of *Jordan Algebras*: the commutative product $\circ$, the square $x^2 = x\circ x$, the identity $[L_x, L_{x^2}] = 0$, the trace form $T(x,y) = \operatorname{tr}(L_{x\circ y})$ and the Peirce decomposition; the examples are those of *Special and Exceptional Jordan Algebras* and *Spin Factors and the Clifford Envelope*.

To a formally real Jordan algebra one attaches its **positive cone**

$$
J_+ = \{x^2 : x \in J\},
$$

the set of squares, and its interior $\Omega = \operatorname{int} J_+$. This is a convex cone, and it is the geometric object that carries the order structure of the algebra. The motivating example is the algebra $H_n(\mathbb{R})$ of real symmetric matrices with the symmetrised product, where $J_+$ is the cone of positive semidefinite matrices; the spin factors give the second-order cones. The convex cone is the algebraic structure considered here — a subset of a real vector space closed under addition and nonnegative scaling, together with the order it defines.

The article defines formally real algebras, derives the cone in the matrix and spin-factor cases, relates the cone to the order and to the spectral resolution, records the Jordan–Banach axiomatisation that makes the cone closed and the algebra complete, and closes with the symmetric cones and the structure group.

## Formally Real Jordan Algebras

### Definition

A Jordan algebra $J$ over $\mathbb{R}$ is **formally real** if

$$
x_1^2 + x_2^2 + \cdots + x_m^2 = 0 \implies x_1 = x_2 = \cdots = x_m = 0 ,
$$

for every finite family $x_i \in J$. Since a sum of finitely many squares can be written as a single square only in special cases, the condition is stated for finite sums. It is equivalent to: $-1$ is not a sum of squares; and, for $J$ finite dimensional and unital, to the trace form $T(x,y) = \operatorname{tr}(L_{x\circ y})$ being positive definite. The last equivalence is the criterion used in the classification, and it is standard.

**Example.** $H_n(\mathbb{R})$, $H_n(\mathbb{C})$, $H_n(\mathbb{H})$ and the spin factors of positive definite forms are formally real. The algebra $H_3(\mathbb{O})$ is formally real. On the other hand, $M_n(\mathbb{R})^+$ and the dual numbers $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ are not formally real: for $n \geq 2$ the matrix with a single entry $1$ in position $(1,2)$ is nonzero with square zero, and in $\mathbb{D}'$ the element $\varepsilon \neq 0$ has $\varepsilon^2 = 0$. Each exhibits a nonzero element whose square is zero, hence a sum of squares equal to zero.

### The Trace Form and the Order

Assume $J$ finite dimensional and formally real. The **positive cone** is

$$
J_+ = \{x^2 : x \in J\}, \qquad \Omega = \operatorname{int} J_+ ,
$$

and the algebra carries the partial order

$$
x \leq y \iff y - x \in J_+ .
$$

**Proposition.** $J_+$ is a pointed closed convex cone, and $\Omega$ is its interior.

*Proof (pointed and closed; convexity in the examples below).* The set $J_+$ is closed under nonnegative scalings, since $(\lambda x)^2 = \lambda^2 x^2$ and $\lambda^2 \geq 0$. It is pointed: if $x \in J_+$ and $-x \in J_+$, then $x = y^2$ and $-x = z^2$ for some $y, z$, whence $y^2 + z^2 = 0$ and formal reality gives $y = z = 0$, so $x = 0$. It is closed because $J_+$ is the nonnegative cone on the image of the unit sphere under the continuous map $x \mapsto x^2$, and that image is compact in finite dimension. Convexity requires more and is established in the examples. $\square$

**Theorem.** In a finite-dimensional formally real Jordan algebra, $J_+$ is a convex cone and $\Omega$ is a symmetric cone: it is homogeneous and self-dual.

The theorem is the Koecher–Vinberg theorem, quoted here as standard. The examples below show convexity directly, and the homogeneity is taken up in the last section.

### Elementary Consequences

**Proposition.** In a formally real Jordan algebra, if $x^2 = 0$ then $x = 0$, and if $x \leq y$ and $y \leq x$ then $x = y$.

*Proof.* The equation $x^2 = 0$ exhibits $0$ as the sum $x^2 + 0^2$ of two squares, so $x = 0$ by formal reality. For the second, $y - x \in J_+$ and $x - y \in J_+$ give $x - y = u^2$ and $y - x = v^2$ for some $u, v$, so $u^2 + v^2 = 0$ and $u = v = 0$, whence $x = y$. $\square$

**Proposition.** If $x = u^2$, $y = v^2$ and $u \circ v = 0$, then $x + y = (u + v)^2 \in J_+$.

*Proof.* By bilinearity and commutativity of $\circ$,

$$
(u + v)^2 = u \circ u + u \circ v + v \circ u + v \circ v = u^2 + 2\,u\circ v + v^2 = x + y ,
$$

so $x + y$ is the square of $u + v$ and lies in $J_+$. $\square$

The cone is closed under addition in general, which says that the sum of two squares is a square; that is the convexity of $J_+$ and is the content of the Koecher–Vinberg theorem, established in the examples below.

## The Matrix Case

### The Cone of a Matrix Algebra

Let $J = H_n(\mathbb{R})$, the real symmetric matrices with $x \circ y = \tfrac12(xy + yx)$ and $x^2 = xx$.

**Proposition.** $J_+$ is the cone of positive semidefinite matrices.

*Proof.* If $x = y^2$ with $y$ symmetric, then $x$ is symmetric, and for every $v \in \mathbb{R}^n$,

$$
\langle xv, v\rangle = \langle y^2 v, v\rangle = \langle yv, yv\rangle = \|yv\|^2 \geq 0 ,
$$

so $x$ is positive semidefinite. Conversely, if $x$ is positive semidefinite then by the spectral theorem $x = u\,\mathrm{diag}(\lambda_1,\ldots,\lambda_n)\,u^{\mathsf T}$ with $\lambda_i \geq 0$ and $u$ orthogonal, and $y = u\,\mathrm{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})\,u^{\mathsf T}$ is a symmetric square root with $y^2 = x$. $\square$

**Corollary.** For $H_n(\mathbb{R})$ the cone $J_+$ is convex, since a nonnegative combination of positive semidefinite matrices is positive semidefinite: if $x, y$ are positive semidefinite and $\lambda, \mu \geq 0$, then for all $v$,

$$
\langle(\lambda x + \mu y)v, v\rangle = \lambda\langle xv,v\rangle + \mu\langle yv,v\rangle \geq 0 .
$$

The interior is the cone of positive definite matrices, and the order $x \leq y$ is the Loewner order. The same computation applies to $H_n(\mathbb{C})$ and $H_n(\mathbb{H})$, with the Hermitian inner product in place of the real one, showing that the positive cone of a Hermitian matrix algebra over $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$ is the cone of positive semidefinite elements.

### Spectral Resolution

In $H_n(\mathbb{R})$ every element has the spectral decomposition $x = \sum_{i=1}^n \lambda_i e_i$ with $\lambda_i \in \mathbb{R}$ and $e_i$ orthogonal idempotents; the $\lambda_i$ are the eigenvalues, and $x \in J_+$ if and only if every $\lambda_i \geq 0$. This is the model for the general statement.

**Theorem.** In a finite-dimensional formally real Jordan algebra every element $x$ admits a **spectral resolution**

$$
x = \sum_{i=1}^{r} \lambda_i e_i ,
$$

with $e_i$ pairwise orthogonal idempotents, $\lambda_i \in \mathbb{R}$, and $r$ at most the degree of $J$; the $\lambda_i$ are the eigenvalues of $x$, and $x \in J_+$ if and only if all $\lambda_i \geq 0$. The eigenvalues are the roots of the generic minimum polynomial of $x$ and depend continuously on $x$.

The existence of the resolution rests on power associativity and the Peirce decomposition of *Jordan Algebras*: the subalgebra generated by $x$ is associative by power associativity, and it is a finite-dimensional formally real associative algebra, hence a product of copies of $\mathbb{R}$ by the standard structure theorem, which yields the idempotents. This is standard.

## The Spin-Factor Case

### The Second-Order Cone

Let $J = JSpin(V)$ for a positive definite form $q$ on a finite-dimensional real vector space $V$, as in *Spin Factors and the Clifford Envelope*: elements $(\alpha, v)$ with $(\alpha, v)^2 = (\alpha^2 + q(v),\, 2\alpha v)$.

**Proposition.** $J_+ = \{(\alpha, v) : \alpha \geq 0,\ \alpha^2 \geq q(v)\}$, the second-order cone of the form $q$.

*Proof.* Suppose $(\alpha, v) = (\beta, w)^2 = (\beta^2 + q(w),\, 2\beta w)$. Then $v = 2\beta w$ and $\alpha = \beta^2 + q(w)$, so

$$
\alpha^2 - q(v) = \bigl(\beta^2 + q(w)\bigr)^2 - q(2\beta w) = \bigl(\beta^2 - q(w)\bigr)^2 \geq 0 ,
$$

using $q(2\beta w) = 4\beta^2 q(w)$, and $\alpha = \beta^2 + q(w) \geq 0$. Conversely, given $(\alpha, v)$ with $\alpha \geq 0$ and $\alpha^2 \geq q(v)$, one solves $\beta^2 + q(w) = \alpha$, $2\beta w = v$: taking $\beta^2 = \tfrac12(\alpha \pm \sqrt{\alpha^2 - q(v)})$ and $w = v/(2\beta)$ realises the element as a square, the sign chosen so that $\beta \neq 0$ when $(\alpha,v) \neq 0$, and the zero element is $0^2$. $\square$

**Corollary.** $J_+$ is convex. Indeed, for $\lambda, \mu \geq 0$ and $(\alpha, v), (\beta, w) \in J_+$, the sum $(\lambda\alpha+\mu\beta, \lambda v+\mu w)$ satisfies

$$
(\lambda\alpha + \mu\beta)^2 - q(\lambda v + \mu w) \geq \lambda^2(\alpha^2 - q(v)) + \mu^2(\beta^2 - q(w)) + 2\lambda\mu\bigl(\alpha\beta - B(v,w)\bigr) \geq 0,
$$

because $B(v,w) \leq \sqrt{q(v)q(w)} \leq \alpha\beta$ by the Cauchy–Schwarz inequality and the defining inequalities. Since the first coordinate is automatically nonnegative, the sum lies in $J_+$. The cone is the classical **second-order cone**, and the order it defines is the order used in the theory of quadratic forms.

**Example.** For $JSpin_2 = \mathbb{R}\oplus\mathbb{R}^2$ the cone is $\{(\alpha, v_1, v_2) : \alpha \geq \sqrt{v_1^2 + v_2^2}\}$, the circular cone of revolution in three dimensions. For an indefinite form the spin factor is not formally real at all, since $v$ with $q(v) < 0$ gives $v^2 = q(v)1$ and hence $v^2 + |q(v)|1 = 0$ with both terms nonzero; the set $\{\alpha \geq 0 : \alpha^2 \geq q(v)\}$ then contains whole lines through the origin. The second-order cone proper is the case of a definite form.

## The Order Structure

### Order Units

An **order unit** of $J$ is an element $u \in \Omega = \operatorname{int} J_+$; equivalently, $u$ is an element such that every $x \in J$ satisfies $-\lambda u \leq x \leq \lambda u$ for some $\lambda \geq 0$. For a unital Jordan algebra the identity $1$ is an order unit: for $x$ with spectral resolution $x = \sum_i \lambda_i e_i$ one has $-\lambda\,1 \leq x \leq \lambda\,1$ with $\lambda = \max_i |\lambda_i|$. The **order-unit norm** is

$$
\|x\|_u = \inf\{\lambda > 0 : -\lambda u \leq x \leq \lambda u\},
$$

a norm on $J$ whose unit ball is the order interval $[-u, u]$. In a JB-algebra the order-unit norm of the identity is the given norm, by the axioms; the order unit, the cone and the norm are mutually determined.

**Proposition.** For $x \in J$ one has $x \in J_+$ if and only if $\|x - \lambda 1\|_1 \leq \lambda$ for all sufficiently large $\lambda$, where $\|\cdot\|_1$ is the order-unit norm of the order unit $1$.

*Proof.* The inequality $\|x - \lambda 1\|_1 \leq \lambda$ means $-\lambda 1 \leq x - \lambda 1 \leq \lambda 1$, that is $0 \leq x \leq 2\lambda 1$, which holds exactly for $x \in J_+$ and $\lambda$ large. $\square$

Thus membership in the cone is detected by a family of norm inequalities centred at the identity; this is the form in which the cone and the order-unit norm encode each other, and the form in which the cone is used in the metric theory.

### The Functional Calculus

The spectral resolution yields a functional calculus on the cone.

**Theorem.** Let $J$ be a finite-dimensional formally real Jordan algebra and let $x = \sum_{i=1}^r \lambda_i e_i$ be its spectral resolution. For any real-valued function $f$ defined on the set of eigenvalues of $x$, put

$$
f(x) = \sum_{i=1}^r f(\lambda_i) e_i .
$$

Then $f(x)$ depends only on $x$ and $f$, the map $x \mapsto f(x)$ is continuous on the set of elements with spectrum in the domain of $f$, and it respects pointwise operations: $(f + h)(x) = f(x) + h(x)$, $(fh)(x) = f(x)\circ h(x)$, $(\mathrm{id})^n(x) = x^n$.

The construction is standard; it is the Jordan analogue of the continuous functional calculus of matrices and of operators, and for $H_n(\mathbb{R})$ it is the ordinary functional calculus of symmetric matrices. Consequences used above are the square root, $x = (\sqrt{x})^2$ for $x \in J_+$, the absolute value $|x| = \sqrt{x^2}$, and the indicator-type idempotents obtained by applying a characteristic function of a spectral value.

**Corollary.** $J_+ = \{x : x = \sqrt{x}\circ\sqrt{x}\} = \{x : x \geq 0\}$, and $x \in \Omega$ if and only if $\sqrt{x}$ is invertible.

### Extreme Rays and Idempotents

An idempotent is **primitive** if it is nonzero and cannot be written as a sum of two nonzero orthogonal idempotents; in $H_n(\mathbb{R})$ these are the rank-one projections.

**Proposition.** Let $J$ be a finite-dimensional formally real Jordan algebra. The extreme rays of $J_+$ are exactly the rays $\mathbb{R}_{\geq 0}e$ through the primitive idempotents $e$.

*Proof.* Let $e$ be primitive and suppose $e = x + y$ with $x, y \in J_+$. Then $0 \leq x \leq e$, and the standard Peirce theory of *Jordan Algebras* gives $x \in J_1(e)$, the unital subalgebra with identity $e$. For a primitive idempotent in a formally real algebra the Peirce cell $J_1(e)$ is one-dimensional, $J_1(e) = \mathbb{R}e$; hence $x = se$ and $y = te$ with $s, t \geq 0$ and $s + t = 1$, so both lie on the ray through $e$, which is therefore extreme. Conversely, if $x \in J_+$ is not proportional to a primitive idempotent, its spectral resolution $x = \sum_i \lambda_i e_i$ has either two nonzero eigenvalues or a single eigenvalue with a nonprimitive idempotent, and in both cases $x$ is a nontrivial sum of two elements of $J_+$; so $x$ does not generate an extreme ray. $\square$

**Proposition.** The extreme points of the order interval $[0,1]$ are exactly the idempotents of $J$.

*Proof.* If $x \in [0,1]$ has spectral resolution $x = \sum_i\lambda_i e_i$ with $0 \leq \lambda_i \leq 1$ and some $\lambda_j \in (0,1)$, then for small $\varepsilon > 0$ the two elements obtained from $x$ by replacing $\lambda_j$ by $\lambda_j \pm \varepsilon$ also lie in $[0,1]$, and $x$ is their midpoint, so $x$ is not extreme. If on the other hand every $\lambda_i \in \{0,1\}$, then $x = \sum_{i\in S}e_i$ is an idempotent. It remains to see that every idempotent is extreme; this is the standard characterisation of the extreme points of the order-unit interval of a JB-algebra. Put $z = \tfrac12(x - y)$, so that $x = e + z$ and $y = e - z$. The inequalities $0 \leq x, y \leq 1$ read $-e \leq z \leq e$ and $-(1 - e) \leq z \leq 1 - e$, that is $|z| \leq e$ and $|z| \leq 1 - e$. Since $0 \leq a \leq p$ for an idempotent $p$ forces $a \in J_1(p)$ by the Peirce theory, the element $|z|$ lies in $J_1(e) \cap J_1(1 - e) = J_1(e) \cap J_0(e) = 0$, so $z = 0$ and $x = y = e$. $\square$

Thus the primitive idempotents generate the extreme rays of the cone, while all idempotents are the extreme points of the order interval. For the simple algebras the algebra automorphism group acts transitively on the primitive idempotents (the extreme rays), and the structure group acts transitively on $\Omega$ itself; the two transitivity statements are the extreme-ray and the interior faces of the homogeneity of the cone. For $H_n(\mathbb{C})$ the primitive idempotents are the rank-one projections, and for the Albert algebra they are the rank-one idempotents on which $F_4$ acts transitively.

## The Axiomatisation: JB-Algebras

### Definition

The cone of squares organises and completes the algebra.

**Definition.** A **JB-algebra** is a real Jordan algebra $J$ that is simultaneously a real Banach space such that, for all $x, y \in J$,

1. $\|x \circ y\| \leq \|x\|\,\|y\|$;
2. $\|x^2\| = \|x\|^2$;
3. $\|x^2\| \leq \|x^2 + y^2\|$.

The conditions make the product continuous and force the cone $J_+$ to be closed and the order to be archimedean. In a JB-algebra the norm is determined by the cone, and the cone determines the norm.

**Example.** The algebra $C(X,\mathbb{R})$ of continuous real functions on a compact Hausdorff space $X$, with the pointwise product, the supremum norm and the cone of nonnegative functions, is a JB-algebra; here $x \circ y = xy$ and the conditions are elementary. The algebras $H_n(\mathbb{R})$, $H_n(\mathbb{C})$, $H_n(\mathbb{H})$ with the operator norm and the cone of positive semidefinite elements are JB-algebras, and so are the spin factors of positive definite forms with the spectral norm $\|(\alpha, v)\| = |\alpha| + \sqrt{q(v)}$, which is the order-unit norm of the identity. The Albert algebra $H_3(\mathbb{O})$ with the spectral norm is a JB-algebra; it is the exceptional example.

**Theorem.** The finite-dimensional JB-algebras are exactly the finite-dimensional formally real Jordan algebras, by the classical Jordan–von Neumann–Wigner classification. In general every JB-algebra is the self-adjoint part of a JB*-algebra and admits a Gelfand–Naimark representation as a Jordan algebra of self-adjoint operators on a complex Hilbert space; the representation theorem is due to Alfsen, Shultz and Størmer.

The theorem is the mathematical axiomatisation of the cone-and-norm structure; it is quoted here as standard and belongs to functional analysis. Its content for this article is that conditions 1–3 characterise the algebras considered above, so that the cone, the algebra and the norm are three descriptions of one object.

### The Order Unit

In a JB-algebra the order unit of the previous section is an element $u \in J_+$ such that for every $x \in J$ there is $\lambda > 0$ with $-\lambda u \leq x \leq \lambda u$; the infimum of such $\lambda$ is the **order-unit norm** $\|x\|_u$, whose closed unit ball is the order interval $[-u,u]$. In a unital JB-algebra the identity $1$ is an order unit, and the order-unit norm agrees with the given norm for the matrix and spin-factor examples, so that the cone, the order unit and the norm are three descriptions of the same structure.

## Symmetric Cones and the Structure Group

### Homogeneity and Self-Duality

The interior $\Omega = \operatorname{int} J_+$ of the positive cone of a finite-dimensional formally real Jordan algebra is a **symmetric cone**: it is convex, open, and

1. **homogeneous**: the group of linear automorphisms of $\Omega$ acts transitively on it;
2. **self-dual**: the dual cone $\{y : T(x,y) \geq 0 \text{ for all } x \in \overline{\Omega}\}$ equals $\overline{\Omega}$, with respect to the trace form $T$ of *Jordan Algebras*.

For $H_n(\mathbb{R})$ the cone of positive definite matrices is homogeneous under $x \mapsto sxs^{\mathsf T}$ for $s$ invertible, and self-dual for the trace pairing $\langle x, y\rangle = \operatorname{tr}(xy)$; for the spin factor the cone is homogeneous under the conformal orthogonal group of the norm form $N(\alpha, v) = \alpha^2 - q(v)$ on $\mathbb{R} \oplus V$, by the last section of *Spin Factors and the Clifford Envelope*.

**Theorem (Koecher–Vinberg).** The symmetric cones are exactly the interiors of the positive cones of finite-dimensional formally real Jordan algebras; the correspondence between the cone and the algebra is bijective up to isomorphism.

This is the precise sense in which the positive cone and the algebra are the same data. It explains why the exceptional Albert algebra appears in convex geometry as the exceptional symmetric cone: the 27-dimensional cone of $H_3(\mathbb{O})$ has no classical model, its algebra automorphism group is the exceptional group $F_4$, and its structure group is the group of norm similitudes, of dimension $79$, an extension of the norm-preserving $E_6$ of dimension $78$ by the dilations, which acts transitively on the cone.

### Structure Group and Cone Automorphisms

Two groups act on a formally real Jordan algebra, and they must not be confused. The **algebra automorphism group** $\operatorname{Aut}(J)$ preserves the product and hence the cone, since it carries squares to squares: for a simple formally real algebra it is compact and acts transitively on the primitive idempotents, that is on the extreme rays of $J_+$. The **structure group** $\operatorname{Str}(J)$ of *Spin Factors and the Clifford Envelope*, the linear maps $s$ with $N(sx) = \nu(s)N(x)$ for a scalar $\nu(s)$, is larger and noncompact; it is the group that acts transitively on the open cone $\Omega$, and this transitivity is the homogeneity of the symmetric cone. The tabulation of algebra automorphism groups of the simple formally real algebras is

| $J$ | $\dim J$ | $\operatorname{Aut}(J)$ | $\operatorname{Str}(J)$ |
|---|---|---|---|
| $H_n(\mathbb{R})$, $n \geq 3$ | $\tfrac{n(n+1)}{2}$ | $PO(n)$ | $GL_n(\mathbb{R})/\{\pm1\}$ |
| $H_n(\mathbb{C})$, $n \geq 3$ | $n^2$ | $PU(n)$ | $GL_n(\mathbb{C})/U(1)$ |
| $H_n(\mathbb{H})$, $n \geq 3$ | $n(2n-1)$ | $PU(n,\mathbb{H})$ | $GL_n(\mathbb{H})/\{\pm1\}$ |
| $H_3(\mathbb{O})$ | $27$ | $F_4$ | $E_6\cdot\mathbb{R}_{>0}$ |

The algebra automorphism groups are the compact groups acting on the extreme rays; the structure groups act transitively on $\Omega$, so $\Omega$ is a homogeneous space of the structure group. For $H_n(\mathbb{R})$ the transitivity is the classical statement that any two positive definite matrices are related by $x\mapsto gxg^{\mathsf T}$, and the group preserving the cone is the structure group $GL_n(\mathbb{R})/\{\pm1\}$; only the scalars $\{\pm1\}$ act trivially on symmetric matrices, so $PGL_n(\mathbb{R})$ is the structure group modulo all scalars and acts on the projectivised cone rather than on the cone itself. The exceptional line of the table is the convex-geometric reading of the classification of *Jordan Algebras*: the 27-dimensional symmetric cone has automorphism group $F_4$ and structure group $E_6\cdot\mathbb{R}_{>0}$ of dimension $79$, whose norm-preserving part is the $E_6$ of dimension $78$.

### The Albert Cone

The exceptional case deserves its own paragraph because it is the one symmetric cone with no matrix model. Let $J = H_3(\mathbb{O})$ with its trace form and its cubic generic norm $N$ of *Special and Exceptional Jordan Algebras*. The cone is the connected component of

$$\{x \in H_3(\mathbb{O}) : N(x) > 0\}$$

containing the identity; it has dimension $27$, and it is self-dual and homogeneous. Its algebra automorphism group is the compact exceptional group $F_4$, which acts transitively on the primitive idempotents with stabiliser a copy of $\operatorname{Spin}(9)$; the orbit is the octonionic projective plane $\mathbb{OP}^2$, of dimension

$$
\dim F_4 - \dim \operatorname{Spin}(9) = 52 - 36 = 16 .
$$

The homogeneity of the cone itself uses the larger group: the connected structure group has dimension $79$ and is an extension of the noncompact $E_6$ by the dilations, and the stabiliser of the identity is the compact automorphism group $F_4$ of dimension $52$, so that $\Omega \cong \operatorname{Str}(H_3(\mathbb{O}))^{\circ}/F_4$ and $79 - 52 = 27$. The cone of the Albert algebra is therefore the meeting point of the constructions of this category: it is the convex cone of squares of the unique exceptional formally real Jordan algebra, and it is the exceptional symmetric cone among the objects classified by the Koecher–Vinberg theorem.

## Summary

In a formally real Jordan algebra $J$ the set of squares $J_+ = \{x^2 : x\in J\}$ is a pointed closed convex cone with interior $\Omega$, and the order $x \leq y \Leftrightarrow y - x \in J_+$ makes $J$ a partially ordered real vector space. For the Hermitian matrix algebra $H_n(\mathbb{R})$ the cone is the positive semidefinite cone, $J_+ = \{x : x = y^2,\ y \text{ symmetric}\}$, proved by the spectral theorem, and it is convex; for the spin factor $JSpin(V)$ of a positive definite form it is the second-order cone $\{(\alpha,v) : \alpha \geq 0,\ \alpha^2 \geq q(v)\}$, proved by completing the square, and it is convex by Cauchy–Schwarz. Every element has a spectral resolution $x = \sum_i \lambda_i e_i$ in orthogonal idempotents, and $x \in J_+$ exactly when all eigenvalues are nonnegative. The JB-algebra axioms — a real Jordan algebra with a Banach norm satisfying $\|x\circ y\|\leq\|x\|\|y\|$, $\|x^2\|=\|x\|^2$ and $\|x^2\|\leq\|x^2+y^2\|$ — characterise the algebras whose cone is closed and whose order is archimedean, and the finite-dimensional ones are exactly the formally real Jordan algebras. The interior is a symmetric cone, homogeneous and self-dual; the Koecher–Vinberg theorem makes this a bijective correspondence between symmetric cones and formally real Jordan algebras, and the structure group is the group that acts transitively on it. The algebra automorphism group preserves the cone and acts transitively on the extreme rays; for $H_n(\mathbb{R})$, $H_n(\mathbb{C})$, $H_n(\mathbb{H})$ and the Albert algebra these are $PO(n)$, $PU(n)$, $PU(n,\mathbb{H})$ and $F_4$, while the structure groups are $GL_n(\mathbb{R})/\{\pm1\}$, $GL_n(\mathbb{C})/U(1)$, $GL_n(\mathbb{H})/\{\pm1\}$ and the $79$-dimensional $E_6\cdot\mathbb{R}_{>0}$, the quotient in each matrix case being by the scalars that act trivially on the Hermitian matrices, namely $\{\pm1\}$ over $\mathbb{R}$ and over $\mathbb{H}$ and the unit circle over $\mathbb{C}$, whereas on the Albert algebra no scalar other than $1$ acts trivially, so the dilations are retained and the structure group is one dimension larger than its norm-preserving part $E_6$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | Real Jordan algebra with product $\circ$ |
| Formally real | $\sum x_i^2 = 0 \Rightarrow$ all $x_i = 0$ |
| $J_+ = \{x^2 : x \in J\}$ | Positive cone, the set of squares |
| $\Omega = \operatorname{int} J_+$ | Interior of the positive cone |
| $x \leq y$ | $y - x \in J_+$ |
| $x = \sum_i \lambda_i e_i$ | Spectral resolution in orthogonal idempotents |
| $T(x,y) = \operatorname{tr}(L_{x\circ y})$ | Trace form, self-duality pairing |
| $JSpin(V)$ | Spin factor, second-order cone $\alpha^2 \geq q(v)$ |
| JB-algebra | Real Jordan Banach algebra with axioms 1–3 |
| $u$ | Order unit; order-unit norm $\|\cdot\|_u$ |
| $\operatorname{Str}(J)$ | Structure group, preserves the cone (transitively) |
| $\operatorname{Aut}(J)$ | Algebra automorphism group, compact, preserves the cone |
| Primitive idempotent | Nonzero idempotent not a sum of two orthogonal nonzero idempotents |
| $J_1(e)$ | Peirce-1 space of an idempotent $e$ |
| $N(x)$ | Generic norm; determinant for $H_3(\mathbb{O})$ |
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual numbers, the standard non-formally-real example |
| $F_4$ | Automorphism group of the Albert algebra, compact, of dimension $52$ |
| $\operatorname{Str}(H_3(\mathbb{O}))$, $E_6\cdot\mathbb{R}_{>0}$ | Structure group of the Albert cone, norm similitudes of dimension $79$ |
| $E_6$ | Norm-preserving part of the structure group of the Albert algebra, of dimension $78$ |
| $\overline{\Omega} = J_+$ | Closure of the cone |

## Further Reading

- Max Koecher, *The Minnesota Notes on Jordan Algebras and Their Applications* (Springer, 1999), for the positive cone and the Koecher–Vinberg theorem.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford University Press, 1994), for symmetric cones, homogeneity and self-duality.
- Erik M. Alfsen and Frederik W. Shultz, *Geometry of Jordan and Lie Structures* (Springer, 2001), for the Jordan–Banach axiomatisation and its structure theory.
- Harald Hanche-Olsen and Erling Størmer, *Jordan Operator Algebras* (Pitman, 1984), for the axiomatisation and the classification of JB-algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for formally real algebras, spectral resolutions and the matrix and spin examples.
- Ottmar Loos, *Symmetric Spaces II: Compact Spaces and Classification* (Benjamin, 1969), for the classification of symmetric cones via Jordan algebras.
