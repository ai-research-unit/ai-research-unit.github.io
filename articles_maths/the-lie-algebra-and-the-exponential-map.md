
# __The Lie Algebra and the Exponential Map__

## Introduction

The Lie algebra of a Lie group is the tangent space at the identity, equipped with the bracket obtained by identifying that tangent space with the left-invariant vector fields. This construction loses nothing locally: the exponential map, which integrates a tangent vector to the one-parameter subgroup it generates, is a local diffeomorphism at the identity, so a neighbourhood of the identity in the group is an image of a neighbourhood of zero in the algebra. The group law is recovered from the algebra by the Campbell–Baker–Hausdorff formula, and in this precise local sense a Lie group is determined by its Lie algebra. The global passage from the algebra back to the group, which is not unique, is not covered here.

This article builds the three objects of the title. It identifies the tangent space at the identity with the left-invariant vector fields, defines the bracket, and constructs the exponential map as the flow of a left-invariant field; it computes the exponential for matrix groups, where it is the ordinary exponential series; it shows that the exponential is a local diffeomorphism and computes its differential, with the singularities that the differential formula exposes; and it states the Campbell–Baker–Hausdorff formula, which exhibits the group law in exponential coordinates as a Lie polynomial.

The manifold conventions are those of the companion article *Lie Groups*: $G$ is a smooth manifold with a group structure for which multiplication and inversion are smooth, the tangent space at the identity is $\mathfrak{g} = T_eG$, and a vector field is a section of the tangent bundle. Lie algebras are written in lowercase fraktur, so $\mathfrak{g}, \mathfrak{h}, \mathfrak{n}$ are Lie algebras; the Lie bracket is $[\cdot, \cdot]$, the adjoint map is $\operatorname{ad}_x(y) = [x, y]$, and the exponential map is $\exp$. The base field is $\mathbb{R}$ or $\mathbb{C}$, written $\mathbb{K}$ when both are possible; where a statement requires $\mathbb{K} = \mathbb{R}$ this is said. No physics is invoked.

## The Tangent Space at the Identity

### Left-Invariant Vector Fields

**Definition.** Let $G$ be a Lie group. For $g \in G$ let $L_g : G \to G$, $L_g(h) = gh$, be the **left translation** by $g$. A vector field $X$ on $G$ is **left-invariant** if

$$
(dL_g)_h\, X_h = X_{gh}
$$

for all $g, h \in G$; equivalently, if $X$ is $L_g$-related to itself for every $g$.

**Proposition.** Evaluation at the identity is a linear isomorphism

$$
\{\text{left-invariant vector fields}\} \longrightarrow \mathfrak{g} = T_eG, \qquad X \mapsto X_e.
$$

Consequently the left-invariant vector fields form a vector space of dimension $\dim G$, and every $v \in \mathfrak{g}$ extends to a unique left-invariant field $X^v$ by $X^v_g = (dL_g)_e v$.

**Proof.** A left-invariant field is determined by its value at $e$, since $X_g = (dL_g)_e X_e$; the assignment $v \mapsto X^v$ is linear, and it is inverse to evaluation, so the map is a linear isomorphism. $\square$

### The Lie Bracket

**Definition.** The **Lie algebra of $G$** is the tangent space $\mathfrak{g} = T_eG$ with the bracket

$$
[v, w] = [X^v, X^w]_e,
$$

the value at the identity of the bracket of the corresponding left-invariant vector fields, where the bracket of vector fields is $[X, Y] = X \circ Y - Y \circ X$ acting on smooth functions.

**Theorem.** With this bracket, $\mathfrak{g}$ is a Lie algebra over $\mathbb{K}$: the bracket is bilinear, alternating, and satisfies the Jacobi identity. Moreover $\mathfrak{g}$ is closed under the bracket, and the bracket of left-invariant fields is left-invariant.

**Proof.** The bracket of vector fields is bilinear and alternating, so the induced bracket on $\mathfrak{g}$ is too. If $X, Y$ are left-invariant, then for every $g$ the fields $X, Y$ are $L_g$-related to themselves, and the bracket of related fields is related, so $[X, Y]$ is left-invariant; this is the closure statement. The Jacobi identity for the bracket of vector fields is a computation in the algebra of derivations of the smooth functions, and it descends to $\mathfrak{g}$. $\square$

**Example.** For $G = GL_n(\mathbb{K})$, an open subset of $\mathbb{K}^{n \times n}$, the tangent space at the identity is the full matrix algebra $\mathfrak{gl}(n, \mathbb{K}) = \mathbb{K}^{n\times n}$, and the bracket induced from left-invariant fields is the commutator $[A, B] = AB - BA$. The identification is made explicit by the computation in the next section, where the exponential of a matrix is the exponential of the tangent vector, and the commutator of the exponentials recovers the bracket through the Campbell–Baker–Hausdorff formula.

**Definition.** A map $\varphi : G \to H$ of Lie groups is a **homomorphism of Lie groups** if it is smooth and a group homomorphism. Its **differential** at the identity is the linear map $d\varphi_e : \mathfrak{g} \to \mathfrak{h}$.

**Theorem.** The differential of a Lie group homomorphism is a homomorphism of Lie algebras:

$$
d\varphi_e([v, w]) = [d\varphi_e(v), d\varphi_e(w)].
$$

**Proof.** A homomorphism intertwines the left translations, $\varphi \circ L_g = L_{\varphi(g)} \circ \varphi$, so it carries left-invariant fields to left-invariant fields; the induced map on vector fields preserves the bracket because it is a diffeomorphism on its image, and evaluating at the identity gives the claim. $\square$

**Corollary.** The assignment $G \mapsto \operatorname{Lie}(G) = \mathfrak{g}$ and $\varphi \mapsto d\varphi_e$ is a functor from Lie groups to Lie algebras over $\mathbb{K}$.

### Vector Fields as Derivations

**Remark.** The bracket $[X, Y] = X \circ Y - Y \circ X$ has the two characteristic properties of the bracket of derivations: it is alternating, and the Jacobi identity for it is the statement that the commutator of two derivations is again a derivation. The left-invariant field $X^v$ acts on a smooth function $f$ by

$$
X^v f(g) = \frac{d}{dt}\Big|_{t=0} f(g \exp(tv)),
$$

as follows from $X^v_g = (dL_g)_e v$ and the flow computation of the next section; this is the form in which the infinitesimal action is usually written.

## One-Parameter Subgroups

### Definition

**Definition.** A **one-parameter subgroup** of $G$ is a smooth homomorphism $\gamma : \mathbb{R} \to G$, so that $\gamma(s + t) = \gamma(s)\gamma(t)$ and $\gamma(0) = e$. Its **velocity** is $\gamma'(0) \in \mathfrak{g}$.

**Proposition.** A one-parameter subgroup is determined by its velocity: if $\gamma'(0) = 0$ then $\gamma$ is constant. Every one-parameter subgroup is the flow of a left-invariant vector field.

**Proof.** For fixed $s$, the curve $t \mapsto \gamma(s + t) = \gamma(s)\gamma(t)$ is the left translate by $\gamma(s)$ of the curve $t \mapsto \gamma(t)$; differentiating at $t = 0$ gives $\gamma'(s) = (dL_{\gamma(s)})_e \gamma'(0)$, which is exactly the statement that the velocity field $s \mapsto \gamma'(s)$ is the left-invariant field extending $\gamma'(0)$. If $\gamma'(0) = 0$ the curve has zero velocity field everywhere and is constant. $\square$

### The Correspondence with Left-Invariant Fields

**Theorem.** For every $v \in \mathfrak{g}$ there is exactly one one-parameter subgroup $\gamma_v$ with $\gamma_v'(0) = v$, and it is the flow through $e$ of the left-invariant field $X^v$:

$$
\gamma_v(t) = \Phi^v_t(e),
$$

where $\Phi^v$ is the flow of $X^v$.

**Proof.** The flow of a vector field is locally defined and unique; the left-invariant field is complete because its flow at time $s$ composed with the flow at time $t$ is the flow at time $s+t$ by the group property of left translations, so the local flow extends to all of $\mathbb{R}$. This gives a one-parameter group of diffeomorphisms, and $\gamma_v(t) = \Phi^v_t(e)$ satisfies $\gamma_v(s + t) = \gamma_v(s)\gamma_v(t)$ and $\gamma_v'(0) = X^v_e = v$. Uniqueness is the uniqueness of solutions of the ordinary differential equation $\gamma' = X^v \circ \gamma$ with $\gamma(0) = e$. $\square$

**Corollary.** One-parameter subgroups of $G$ are in bijection with the vectors of $\mathfrak{g}$.

**Example.** For $G = GL_n(\mathbb{K})$ and a matrix $A$, the one-parameter subgroup with velocity $A$ is $\gamma_A(t) = e^{tA}$, where $e^{tA}$ is the matrix exponential. This is verified in the next section.

## The Exponential Map

### Definition via the Flow

**Definition.** The **exponential map** of $G$ is

$$
\exp : \mathfrak{g} \to G, \qquad \exp(v) = \gamma_v(1),
$$

the time-one value of the one-parameter subgroup with velocity $v$. Equivalently $\exp(v) = \Phi^v_1(e)$.

**Theorem.** The exponential map is smooth, and for all $s, t \in \mathbb{R}$ and $v \in \mathfrak{g}$:

**(a)** $\exp(0) = e$ and $\exp((s+t)v) = \exp(sv)\exp(tv)$;

**(b)** $\exp(tv) = \gamma_v(t)$ and $\exp(-v) = \exp(v)^{-1}$;

**(c)** $\exp$ is natural: for a Lie group homomorphism $\varphi : G \to H$ and $v \in \mathfrak{g}$,

$$
\varphi(\exp_G v) = \exp_H(d\varphi_e v).
$$

**Proof.** (a) and (b) are the one-parameter group property of $\gamma_v$, and the smoothness of $\exp$ follows from the smooth dependence of the flow on its initial condition. For (c), the curve $t \mapsto \varphi(\gamma_v(t))$ is a one-parameter subgroup of $H$ with velocity $d\varphi_e v$, so by uniqueness it is $\gamma_{d\varphi_e v}$; evaluating at $t = 1$ gives the claim. $\square$

**Corollary.** The differential of $\exp$ at $0$, under the canonical identification $T_0\mathfrak{g} \cong \mathfrak{g}$, is the identity:

$$
d(\exp)_0 = \mathrm{id}_{\mathfrak{g}}.
$$

**Proof.** The derivative of $t \mapsto \exp(tv)$ at $t = 0$ is $v$, so the linear map $d(\exp)_0$ fixes every $v$. $\square$

### The Matrix Exponential

**Theorem.** Let $G \subseteq GL_n(\mathbb{K})$ be a Lie subgroup with Lie algebra $\mathfrak{g} \subseteq \mathfrak{gl}(n, \mathbb{K})$. Then the exponential map of $G$ agrees with the ordinary matrix exponential on $\mathfrak{g}$:

$$
\exp(A) = \sum_{k=0}^{\infty} \frac{A^k}{k!} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots,
$$

and the series converges absolutely for every $A$.

**Proof.** The series converges because its norm is bounded by $e^{\|A\|}$; differentiating it term by term gives $\frac{d}{dt}e^{tA} = A e^{tA}$, so $t \mapsto e^{tA}$ is a one-parameter subgroup of $GL_n$ with velocity $A$; by uniqueness it is $\gamma_A(t)$, and evaluating at $t = 1$ gives the claim. For $G$ a subgroup, the curve $e^{tA}$ lies in $G$ for $A \in \mathfrak{g}$ because $G$ is a Lie subgroup with that Lie algebra, so the exponential of $G$ agrees with the matrix exponential. $\square$

**Proposition (properties of the matrix exponential).** For matrices $A, B$:

**(a)** $e^{A+B} = e^A e^B$ if $AB = BA$;

**(b)** $e^{A}$ is invertible, $(e^A)^{-1} = e^{-A}$, and $\det(e^A) = e^{\operatorname{tr}(A)}$;

**(c)** $A e^{A} = e^{A} A$;

**(d)** $e^{BAB^{-1}} = B e^A B^{-1}$ for invertible $B$.

**Proof.** (a) The binomial theorem applies to commuting $A, B$ and gives the product series. (b) The inverse is $e^{-A}$ from (a) with $B = -A$. For the determinant, reduce to the triangular case: over $\mathbb{C}$ every matrix is conjugate to an upper triangular matrix; for upper triangular $T$ with diagonal entries $t_i$ the matrix $e^T$ is upper triangular with diagonal $e^{t_i}$, so $\det e^T = \prod_i e^{t_i} = e^{\sum_i t_i} = e^{\operatorname{tr}T}$; conjugating by (d) and extending from $\mathbb{C}$ to $\mathbb{K}$ gives the general case. (c) is immediate from the series. (d) is $(BAB^{-1})^k = B A^k B^{-1}$. $\square$

**Example.** For $A = \begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix}$ one has $e^A = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t\end{pmatrix}$, the rotation by angle $t$. This exhibits the exponential as the map from the line of skew matrices to the circle group $SO(2)$, and it shows that $\exp$ is not injective: $\exp(A) = I$ for $t = 2\pi$.

### Local Diffeomorphism

**Theorem (inverse function theorem for the exponential).** The exponential map is a local diffeomorphism at the origin of $\mathfrak{g}$: there is an open neighbourhood $U$ of $0$ in $\mathfrak{g}$ and an open neighbourhood $V$ of $e$ in $G$ such that $\exp|_U : U \to V$ is a diffeomorphism.

**Proof.** The differential $d(\exp)_0$ is the identity by the corollary above, hence invertible; the inverse function theorem for smooth manifolds gives a neighbourhood on which $\exp$ is a diffeomorphism onto its image. $\square$

**Corollary.** The pair $(G, \mathfrak{g})$ is locally determined by $\mathfrak{g}$: exponential coordinates on $V$ identify a neighbourhood of the identity with a neighbourhood of $0$ in the vector space $\mathfrak{g}$.

**Remark (global failure of injectivity and surjectivity).** The exponential is only a local diffeomorphism in general. It is not injective: for the circle group $U(1)$ the kernel consists of the multiples of $2\pi i$. It is not surjective onto a connected group in general: for $G = SL_2(\mathbb{R})$ there are matrices with no real logarithm, so they lie outside the image of $\exp$. It is surjective when $G$ is connected and nilpotent, and when $G$ is compact and connected; the failure of surjectivity is a global phenomenon with no counterpart in the algebra.

### Naturality and Conjugation

**Definition.** For $g \in G$ the **conjugation** by $g$ is the automorphism $c_g : G \to G$, $c_g(h) = ghg^{-1}$.

**Definition.** The **adjoint representation** of $G$ is $\operatorname{Ad} : G \to GL(\mathfrak{g})$, $\operatorname{Ad}(g) = d(c_g)_e$.

**Proposition.** For all $g \in G$ and $v \in \mathfrak{g}$,

$$
\exp(\operatorname{Ad}(g)\, v) = g \exp(v) g^{-1}.
$$

**Proof.** Apply the naturality of $\exp$ to the homomorphism $c_g$, whose differential is $\operatorname{Ad}(g)$ by definition. $\square$

**Corollary.** $\operatorname{Ad}(g)$ is a Lie algebra automorphism of $\mathfrak{g}$ for every $g$, and its Lie algebra differential at the identity is $\operatorname{ad}$: $\operatorname{ad}_v = d(\operatorname{Ad})_e(v)$. This is developed.

## The Differential of the Exponential

### The Formula for $d\exp$

**Theorem.** Identify $T_v\mathfrak{g}$ with $\mathfrak{g}$ for every $v$, and $T_{\exp(v)}G$ with $\mathfrak{g}$ by left translation. Then the differential of the exponential is the operator

$$
d(\exp)_v = \sum_{k=0}^{\infty} \frac{(-1)^k}{(k+1)!}\, (\operatorname{ad}_v)^k = \frac{1 - e^{-\operatorname{ad}_v}}{\operatorname{ad}_v},
$$

the series being the entire function $\frac{1-e^{-z}}{z}$ applied to the endomorphism $\operatorname{ad}_v$.

**Proof sketch.** Differentiate the identity $\exp(v + s w) = \exp(v)\exp(sW(s))$ for a curve $W$ in $\mathfrak{g}$ with $W(0) = 0$; the derivative at $s = 0$ is $d(\exp)_v(w) = \sum_{k \geq 0}\frac{(-1)^k}{(k+1)!}(\operatorname{ad}_v)^k(w)$, obtained by expanding the Campbell–Baker–Hausdorff series. The expansion is the standard computation, and its coefficients are the Bernoulli-like numbers $\frac{(-1)^k}{(k+1)!}$. $\square$

### The Cases of Injectivity and Singularity

**Corollary.** $d(\exp)_v$ is invertible exactly when $\operatorname{ad}_v$ has no eigenvalue in $2\pi i\mathbb{Z} \setminus \{0\}$. In particular $d(\exp)_0 = \mathrm{id}$, $d(\exp)_v$ is invertible for small $\|v\|$, and by the inverse function theorem the exponential map is a local diffeomorphism at $v$ exactly when $d(\exp)_v$ is invertible.

**Proof.** The operator is $f(\operatorname{ad}_v)$ with $f(z) = (1-e^{-z})/z$, whose zeros are the nonzero multiples of $2\pi i$; a polynomial-like function of a diagonalisable endomorphism is invertible exactly when it is nonzero on the spectrum. $\square$

**Example.** For a matrix $A$ with eigenvalues $a_j$, the eigenvalues of $\operatorname{ad}_A$ on $\mathfrak{gl}(n)$ are the differences $a_i - a_j$, and $d(\exp)_A$ is singular exactly when some $a_i - a_j$ is a nonzero multiple of $2\pi i$. This is the reason the exponential fails to be a local diffeomorphism at matrices whose eigenvalues differ by $2\pi i\,\mathbb{Z}$.

### The Relation to the Invariant Volume

**Remark.** The determinant of $d(\exp)_v$ can be written in terms of the roots of $\mathfrak{g}$: if $\mathfrak{g} = \bigoplus_\alpha \mathfrak{g}_\alpha$ with respect to a Cartan subalgebra and $v$ is regular in a Cartan subalgebra $\mathfrak{h}$, then

$$
\det\bigl(d(\exp)_v\bigr) = \prod_{\alpha \in \Phi} \frac{1 - e^{-\alpha(v)}}{\alpha(v)},
$$

the product over the roots, and this is the Jacobian of the exponential in exponential coordinates. It vanishes precisely where some $\alpha(v) \in 2\pi i\mathbb{Z}\setminus\{0\}$, in agreement with the corollary above. The description of the exponential in terms of a maximal torus and the roots is the starting point of the Weyl integration formula, and the local structure is not covered here.

## The Campbell–Baker–Hausdorff Formula

### Statement

**Theorem (Campbell–Baker–Hausdorff).** There is a neighbourhood of $0$ in $\mathfrak{g} \times \mathfrak{g}$ on which the equation

$$
\exp(X)\exp(Y) = \exp(Z(X, Y))
$$

has a unique solution $Z(X, Y)$, and this solution is a **Lie polynomial**: it is a convergent series in $X, Y$ whose every term is obtained from $X, Y$ by iterated brackets. Its first terms are

$$
Z(X, Y) = X + Y + \tfrac{1}{2}[X, Y] + \tfrac{1}{12}[X, [X, Y]] - \tfrac{1}{12}[Y, [X, Y]] - \tfrac{1}{24}[Y, [X, [X, Y]]] + \cdots.
$$

**Proof sketch.** The derivative formula for the exponential gives the differential equation satisfied by $Z$ along the path $\exp(X)\exp(tY)$, and the solution is obtained by successive approximation; each step introduces one more bracket, and the convergence for small $X, Y$ follows from the analytic dependence on the two variables, by the analytic implicit function theorem. $\square$

### Consequences

**Corollary.** The binary operation

$$
X \cdot Y = Z(X, Y) = X + Y + \tfrac{1}{2}[X, Y] + \cdots
$$

defined near the origin of $\mathfrak{g}$ is a local Lie group law with the property that $\exp$ is a local isomorphism from $(\mathfrak{g}, \cdot)$ to $G$. In particular the germ of the group law of $G$ at the identity is recovered from the Lie bracket.

**Corollary.** If $[X, Y] = 0$ then $Z(X, Y) = X + Y$, so $\exp(X + Y) = \exp(X)\exp(Y)$; this recovers the abelian case and the matrix identity $e^{A+B} = e^A e^B$ for commuting matrices.

**Corollary.** For a simply connected Lie group the group law is determined by the Lie algebra, and two simply connected Lie groups with isomorphic Lie algebras are isomorphic. This is one direction of the Lie correspondence; the general statement is.

### Exponential Coordinates

**Definition.** **Exponential coordinates** on a neighbourhood of the identity are the coordinates obtained by composing $\exp^{-1}$ with a linear identification $\mathfrak{g} \cong \mathbb{K}^n$.

**Remark.** In exponential coordinates the group law is the Campbell–Baker–Hausdorff product, the inversion is $X \mapsto -X$, and the differential of the multiplication at the origin is $(X, Y) \mapsto X + Y$; in this sense the group is, to first order at the identity, its Lie algebra. The higher-order terms measure the failure of the group to be abelian, and their leading term is the bracket.

## Example: The Unit Quaternions

Let $G = S^3 = \{q \in \mathbb{H} : |q| = 1\}$, the group of unit quaternions under multiplication; it is the spin group $\operatorname{Spin}(3)$, and it is a Lie group of dimension $3$. The tangent space at $1$ is the space of purely imaginary quaternions,

$$
\mathfrak{g} = \operatorname{Im}\mathbb{H} = \{u = u_1 e_1 + u_2 e_2 + u_3 e_3\},
$$

which is a three-dimensional real vector space. With the commutator bracket inherited from the associative algebra $\mathbb{H}$, the bracket of two imaginary quaternions is

$$
[u, v] = uv - vu = 2\, (u \times v),
$$

twice the cross product. The one-parameter subgroup generated by $u \neq 0$ is

$$
\exp(tu) = \cos(t|u|) + \frac{u}{|u|}\sin(t|u|),
$$

a curve of unit quaternions, and the exponential map is

$$
\exp(u) = \cos|u| + \frac{u}{|u|}\sin|u|, \qquad \exp(0) = 1.
$$

The exponential is surjective onto $S^3$, since every unit quaternion has the form $\cos\theta + n\sin\theta$ with $n$ a unit imaginary quaternion; it is not injective, since $\exp(u) = 1$ exactly when $u = 2\pi k\, n$ for some integer $k$ and some unit imaginary $n$ with $|u| = 2\pi|k|$. The differential $d(\exp)_u$ is singular exactly when $\operatorname{ad}_u$ has a nonzero eigenvalue in $2\pi i\mathbb{Z}$: the eigenvalues of $\operatorname{ad}_u$ on $\operatorname{Im}\mathbb{H}$ are $\pm 2i|u|$ (with the zero eigenvalue on the line $\mathbb{R}u$), so $d(\exp)_u$ is singular for $|u| \in \pi\mathbb{Z}\setminus\{0\}$, that is, at the multiples of $\pi$ other than zero. This is the quaternionic form of the failure of the exponential to be a local diffeomorphism at the antipode.

**Remark.** The group $S^3$ is the simplest nonabelian compact example in which the exponential is surjective but not injective, and it exhibits the two global failures side by side. The Lie algebra is $\operatorname{Im}\mathbb{H}$ with the bracket $[u, w] = uw - wu$, which is the compact real form of the algebra of type $A_1$ of *Root Systems and Classification*; the quaternionic exponential is the restriction of the matrix exponential under the identification of $S^3$ with $SU(2)$.

## Summary

For a Lie group $G$ the tangent space at the identity, identified with the space of left-invariant vector fields by evaluation at $e$, carries the bracket of vector fields and becomes the Lie algebra $\mathfrak{g} = \operatorname{Lie}(G)$; the construction is functorial, and the differential at the identity of a Lie group homomorphism is a homomorphism of Lie algebras. One-parameter subgroups are in bijection with the vectors of $\mathfrak{g}$: the subgroup with velocity $v$ is the flow of the left-invariant field extending $v$.

The exponential map $\exp : \mathfrak{g} \to G$ sends $v$ to the time-one value of that flow; it is smooth, satisfies $\exp((s+t)v) = \exp(sv)\exp(tv)$, is natural with respect to homomorphisms, and has $d(\exp)_0 = \mathrm{id}_{\mathfrak{g}}$, so it is a local diffeomorphism at $0$ by the inverse function theorem. For a matrix group it is the ordinary exponential series, with $\det(e^A) = e^{\operatorname{tr}A}$ and $e^{A+B} = e^A e^B$ for commuting $A, B$. The differential in general is $d(\exp)_v = \sum_k \frac{(-1)^k}{(k+1)!}(\operatorname{ad}_v)^k$, invertible exactly when $\operatorname{ad}_v$ has no nonzero eigenvalue in $2\pi i\mathbb{Z}$. The exponential is neither injective nor surjective in general, but for connected nilpotent or connected compact groups it is surjective. The Campbell–Baker–Hausdorff formula writes $\exp(X)\exp(Y) = \exp(Z(X,Y))$ with $Z$ a Lie polynomial whose first terms are $X + Y + \frac12[X,Y] + \cdots$, so the germ of the group law is determined by the bracket.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G, H$ | Lie groups over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ |
| $\mathfrak{g} = T_eG$ | Lie algebra of $G$; tangent space at the identity |
| $\mathfrak{h} = T_eH$ | Lie algebra of $H$; the codomain of $d\varphi_e$ |
| $L_g$, $dL_g$ | Left translation and its differential |
| $X^v$ | Left-invariant vector field extending $v \in \mathfrak{g}$ |
| $[X, Y] = X \circ Y - Y \circ X$ | Bracket of vector fields; $[v,w] = [X^v, X^w]_e$ |
| $d\varphi_e$ | Differential at the identity of a Lie group homomorphism; a Lie algebra homomorphism |
| $\mathfrak{gl}(n, \mathbb{K})$ | Matrix Lie algebra $\mathbb{K}^{n\times n}$; the ambient algebra of a matrix group |
| $\gamma_v(t)$ | One-parameter subgroup with velocity $v$ |
| $\exp : \mathfrak{g} \to G$ | Exponential map, $\exp(v) = \gamma_v(1) = \Phi^v_1(e)$ |
| $\exp((s+t)v) = \exp(sv)\exp(tv)$, $\varphi(\exp_G v) = \exp_H(d\varphi_e v)$ | Functional properties of $\exp$ |
| $e^A = \sum_k A^k/k!$ | Matrix exponential; agrees with $\exp$ for matrix groups |
| $\det(e^A) = e^{\operatorname{tr}A}$ | Determinant of a matrix exponential |
| $d(\exp)_0 = \mathrm{id}_{\mathfrak{g}}$ | $\exp$ is a local diffeomorphism at $0$ |
| $d(\exp)_v = \sum_k \frac{(-1)^k}{(k+1)!}(\operatorname{ad}_v)^k = \frac{1-e^{-\operatorname{ad}_v}}{\operatorname{ad}_v}$ | Differential of $\exp$ |
| $c_g$, $\operatorname{Ad}(g) = d(c_g)_e$ | Conjugation and the adjoint representation of $G$; $\exp(\operatorname{Ad}(g)v) = g\exp(v)g^{-1}$ |
| $Z(X, Y) = X + Y + \frac12[X,Y] + \frac1{12}[X,[X,Y]] - \frac1{12}[Y,[X,Y]] + \cdots$ | Campbell–Baker–Hausdorff Lie polynomial |
| $\exp(X)\exp(Y) = \exp(Z(X,Y))$ | Group law in exponential coordinates |
| $\operatorname{Im}\mathbb{H}$ | Lie algebra of $S^3$, bracket $[u,v] = 2(u\times v)$ |





## Further Reading

- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2nd ed. 2013), for flows, left-invariant vector fields, and the differential of the exponential.
- John F. Adams, *Lectures on Lie Groups* (University of Chicago Press, 1969), for the exponential map and its differential in the classical setting.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the exponential map, the Jacobian, and the differential formula.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the exponential map, one-parameter subgroups, and the local group law.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for matrix Lie groups, the matrix exponential, and the Campbell–Baker–Hausdorff formula.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, 1992), for exponential coordinates and the Lie correspondence.
- Wilhelm Magnus, Abraham Karrass, and Donald Solitar, *Combinatorial Group Theory* (Dover, 2nd ed. 1976), for the Campbell–Baker–Hausdorff series and its convergence.
