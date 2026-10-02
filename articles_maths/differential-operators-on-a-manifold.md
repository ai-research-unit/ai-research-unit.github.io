# __Differential Operators on a Manifold__

## Introduction

A **differential operator** on a manifold is a linear map on the sections of vector bundles whose value at a point depends on the values of the section and finitely many of its derivatives at that point. The order counts the derivatives, and the leading part of the operator, read as a function of the derivative directions, is the **symbol**. The first-order operators of the corpus are the exterior derivative $d$ of *Differential Forms and Stokes' Theorem*, the covariant derivative of a connection of *Fibre Bundles, Connections and Curvature*, and the Lie derivative along a vector field of *Smooth Manifolds and Differential Geometry*; the second-order ones are assembled from them.

The article develops the operators from the definitions. It defines an operator of order at most $k$ on the sections of a vector bundle, proves that the order is well defined, and defines the principal symbol and proves that it is tensorial. It then introduces the **jet bundles** $J^kE$, the universal recipients of the derivatives of a section, and proves the theorem that identifies an operator of order at most $k$ with a bundle homomorphism $J^kE \to F$: this is the structural theorem of the subject, and it is why the jets, and not the coordinates, are the invariant home of the differential operators. It treats the composition, the commutator with a function that lowers the order, the symbol of a composition and of an adjoint, and closes with the elliptic operators and the elliptic complexes, the objects to which the regularity and index theory apply.

The article assumes the smooth manifolds, the tangent and cotangent bundles, the vector fields and the differential of a smooth map of *Smooth Manifolds and Differential Geometry*; the vector bundles, their sections, the covariant derivative and the curvature of *Fibre Bundles, Connections and Curvature*; and the differential forms and the exterior derivative of *Differential Forms and Stokes' Theorem*. The formal adjoint is stated here only as far as its order and its symbol, and is developed in *The Formal Adjoint of a Differential Operator*; the $L^2$ realisation, the domain, the boundary conditions and the closedness are *The L2 Adjoint of a Differential Operator*; the pseudodifferential calculus that closes the theory under inversion is *Pseudodifferential Operators*, and the index of an elliptic complex is *The Atiyah–Singer Index Theorem and K-Theory* in Part IV. No physics is invoked.

## Differential Operators and Their Order

### The Definition

Let $M$ be a smooth manifold and let $E \to M$ and $F \to M$ be smooth vector bundles of ranks $r$ and $s$; write $\Gamma(E)$ for the module of smooth sections, a module over the ring $C^\infty(M)$.

**Definition.** An $\mathbb{R}$-linear map $P : \Gamma(E) \to \Gamma(F)$ is a **differential operator of order at most $k$** if over every chart $(U, x^1, \ldots, x^n)$ with trivialisations of $E$ and $F$, and writing a local section as $u = (u^1, \ldots, u^r)$ in the frame of $E$, the image has components

$$
(Pu)^i = \sum_{a=1}^{r} \sum_{|\alpha| \le k} A^{i\alpha}_{a}(x)\, \partial_\alpha u^a, \qquad i = 1, \ldots, s,
$$

with coefficient functions $A^{i\alpha}_{a} \in C^\infty(U)$ and multi-indices $\alpha = (\alpha_1, \ldots, \alpha_n)$ of length $|\alpha| = \alpha_1 + \cdots + \alpha_n$. The **order** $\operatorname{ord}(P)$ is the least $k$ for which this holds, and $P$ is a differential operator if it has finite order. The space of operators of order at most $k$ from $E$ to $F$ is written $D^k(E, F)$, and $D(E,F) = \bigcup_k D^k(E,F)$.

**Proposition.** The property of being of order at most $k$ is independent of the charts and the frames, so the definition is intrinsic.

*Proof sketch.* Let $y = \psi(x)$ be another chart and let $g(x)$, $h(x)$ be the change-of-frame matrices of $E$ and $F$. The chain rule expresses each $\partial_\alpha$ in the $x$-coordinates as a sum of the $\partial_\beta$ in the $y$-coordinates with $|\beta| \le |\alpha|$, with coefficients that are polynomial in the derivatives of $\psi$ and involve only derivatives of $\psi$ of order at most $|\alpha|$; the terms of order exactly $|\alpha|$ carry the symmetric $|\alpha|$-th power of the Jacobian of $\psi$, and the lower-order terms have coefficients involving the lower derivatives of $\psi$. Conjugating the coefficient matrix by $g$ and $h$ therefore preserves the shape displayed, and the order. The statement is local and the bundle is locally trivial, so the local verifications patch.

**Examples.** A smooth vector field $X$, read as the map $f \mapsto X(f)$ on functions, is an operator of order at most $1$ from the trivial line bundle to itself, and it is of order exactly $1$ where $X \neq 0$. The exterior derivative $d : \Omega^p(M) \to \Omega^{p+1}(M)$ is of order at most $1$. The covariant derivative $\nabla_X$ along a vector field, on the sections of a vector bundle, is of order at most $1$; the connection Laplacian $\nabla^*\nabla$ and the Laplace–Beltrami operator of a metric are of order at most $2$. An operator of order $0$ is exactly a bundle homomorphism $E \to F$, that is, a section of $\operatorname{Hom}(E, F)$ acting fibrewise.

### Order, Composition and the Commutator

**Proposition.** The order has the following formal properties.

**(a)** The sum of two operators of order at most $k$ is of order at most $k$, and $D^k(E,F)$ is a real vector space; more, it is a module over $C^\infty(M)$ under multiplication of the values.

**(b)** If $P : \Gamma(E) \to \Gamma(F)$ has order at most $k$ and $Q : \Gamma(F) \to \Gamma(G)$ has order at most $l$, then $Q \circ P$ has order at most $k + l$.

**(c)** If $P$ has order at most $k$ and $f \in C^\infty(M)$, the commutator $[P, f] = P f - f P$, where $f$ acts by multiplication, has order at most $k - 1$; for $k = 0$ it vanishes.

*Proof.* Part (a) is immediate from the shape of the local expressions. Part (b) is the Leibniz rule: applying $l$ derivatives to a sum of products of derivatives of $u$ of order at most $k$ produces terms of order at most $k + l$, and no term of higher order. Part (c) is also the Leibniz rule: the highest derivatives of $fu$, of total order $k$, are $f$ times the highest derivatives of $u$, because the derivatives fall on $f$ only in the lower-order terms; every term of order exactly $k$ carries a coefficient multiplied by $f$ and cancels between $Pf$ and $fP$. Hence the surviving terms have order at most $k-1$.

Part (c) characterises the order: a linear map $P$ has order at most $k$ if and only if the iterated commutator $[\cdots[[P, f_0], f_1], \ldots, f_k]$ vanishes for all smooth functions $f_0, \ldots, f_k$. This **multilinear** form of the definition is the one that is manifestly intrinsic and that the symbol is read from.

## The Principal Symbol

### Definition and Tensoriality

Let $P \in D^k(E,F)$ and let $x \in M$. In a chart with coordinates $x^j$ and frames of $E$ and $F$, write the top-order part of $P$ as

$$
P_k u = \sum_{|\alpha| = k} A_\alpha(x)\,\partial_\alpha u
$$

with $A_\alpha$ an $s \times r$ matrix of functions. For a covector $\xi = \sum_j \xi_j\, dx^j$ at $x$ put

$$
\sigma_k(P)(x, \xi) = \sum_{|\alpha| = k} A_\alpha(x)\,\xi^\alpha \in \operatorname{Hom}(E_x, F_x),
$$

where $\xi^\alpha = \xi_1^{\alpha_1}\cdots\xi_n^{\alpha_n}$. This is the **principal symbol** of $P$ at $x$ in the direction $\xi$.

**Proposition.** The expression $\sigma_k(P)(x,\xi)$ is independent of the chart and the frames, so the principal symbol is a smooth section

$$
\sigma_k(P) \in \Gamma\!\left(\operatorname{Sym}^k TM \otimes \operatorname{Hom}(E,F)\right),
$$

equivalently a smooth family of linear maps $\sigma_k(P)(x,\xi) : E_x \to F_x$ polynomial of degree $k$ in $\xi \in T^*_xM$. For $k = 0$ it is $P$ itself, read fibrewise; for every $k$ it depends on $P$ only through its part of order exactly $k$, so $\sigma_k$ is constant on the affine subspace $\{P + D^{k-1}(E,F)\}$.

*Proof.* Under a change of coordinates the top-order part transforms by the $k$-th symmetric power of the Jacobian, by the argument of the previous section, while the lower-order derivatives of the transition functions contribute only to the terms of order below $k$; and the change of frames conjugates $A_\alpha$ by the two frame matrices. Both operations preserve the displayed combination at every $\xi$, because $\xi^\alpha$ transforms by the inverse transpose of the Jacobian. For the last statement, $A_\alpha$ is unchanged when an operator of order at most $k-1$ is added, since the latter has no terms of order $k$.

The symmetric $k$-linear form underlying $\sigma_k(P)$ is recovered from the polynomial by polarisation, and it is the function of $k$ tangent vectors

$$
(\xi_1, \ldots, \xi_k) \longmapsto \frac{1}{k!}\sum_{\epsilon_1, \ldots, \epsilon_k = \pm 1} \epsilon_1\cdots\epsilon_k\, \sigma_k(P)(\epsilon_1\xi_1 + \cdots + \epsilon_k\xi_k).
$$

**Proposition (symbols of a composition and of an adjoint).** Let $P \in D^k(E,F)$ and $Q \in D^l(F,G)$. Then

$$
\sigma_{k+l}(QP) = \sigma_l(Q)\,\sigma_k(P),
$$

the product being the composition of the two homomorphisms of the fibres. If $E$ and $F$ carry metrics and $P^*$ is the formal adjoint of $P$ with respect to them, then $P^*$ has order $k$ and

$$
\sigma_k(P^*)(x,\xi) = (-1)^k\, \sigma_k(P)(x,\xi)^*,
$$

the transpose being taken with respect to the two metrics.

*Proof.* For the composition, the product $QP$ has order at most $k+l$, and its part of order exactly $k+l$ is obtained by applying the order-$l$ part of $Q$ to the order-$k$ part of $P$; the lower-order parts of one composed with the highest part of the other have order at most $k+l-1$. Substituting the top-order expressions gives the product of the symbols. For the adjoint, differentiate the identity $\langle Pu, v\rangle = \langle u, P^*v\rangle$ to top order: each of the $k$ derivatives is moved from $u$ to $v$, producing the factor $(-1)^k$, and the matrices are transposed.

### Elliptic Operators

**Definition.** An operator $P \in D^k(E,F)$ is **elliptic** at $x$ if $\sigma_k(P)(x,\xi) : E_x \to F_x$ is invertible for every nonzero $\xi \in T^*_xM$; it is elliptic if it is elliptic at every point. The **characteristic variety** of $P$ is the subset of $T^*M$ on which $\sigma_k(P)(x,\xi)$ is not invertible, that is, the zeros of $\det \sigma_k(P)(x,\xi)$ in a pair of frames.

Since the symbol of a composition is the product of the symbols, an elliptic operator has $\operatorname{rank} E = \operatorname{rank} F$, and the composition of two elliptic operators is elliptic; the identity operator is elliptic of order $0$, and $d^k \star d$ type combinations are elliptic of order $2k$. The characteristic variety is a cone in the cotangent bundle, invariant under the scaling of the fibres, and it is empty for an elliptic operator.

**Examples.** The exterior derivative $d : \Omega^p \to \Omega^{p+1}$ has symbol $\sigma_1(d)(x,\xi) = \xi \wedge \cdot$, the exterior multiplication by $\xi$; it is not invertible, and it is not elliptic, because $\xi\wedge\xi = 0$. The de Rham operator $d + \delta$ and the Laplace–de Rham operator $\Delta = d\delta + \delta d$ have symbols the Clifford multiplication by $\xi$ and $-\lvert\xi\rvert^2$ respectively read on forms, and both are elliptic; the symbol of the Laplace–Beltrami operator of a metric is $-\lvert\xi\rvert_g^2$. The Cauchy–Riemann operator and the Dirac operator are first-order elliptic, with symbols the multiplication by $\xi$ and by the Clifford element $\xi$; the equations that these symbols control are the elliptic equations of *Partial Differential Equations*.

## Jet Bundles

### The Jet of a Section

**Definition.** Let $E \to M$ be a vector bundle and $k \ge 0$. Two sections $s, t \in \Gamma(E)$ **agree to order $k$** at $x \in M$ if in one, hence every, chart and trivialisation about $x$ the difference $s - t$ and all its partial derivatives of total order at most $k$ vanish at $x$. This is an equivalence relation, and the class of $s$ is the **$k$-jet** $j_k s(x)$ of $s$ at $x$. The set of $k$-jets at $x$ is $J^k_xE$, and the disjoint union $J^kE = \bigsqcup_{x \in M} J^k_xE$ is the **bundle of $k$-jets** of $E$.

**Proposition.** The set $J^k_xE$ is a real vector space of dimension $r\binom{n+k}{k}$, the bundle $J^kE \to M$ is a smooth vector bundle of that rank, and a chart $(U,x^1,\ldots,x^n)$ with a frame $e_1,\ldots,e_r$ of $E$ provides fibrewise coordinates $(x^j, u^a, u^a_{j_1}, u^a_{j_1j_2}, \ldots)$ indexed by the multi-indices $|\alpha| \le k$, in which the jet of a section $s = \sum_a s^a e_a$ is

$$
j_k s(x) = \left(x,\ s^a(x),\ \partial_j s^a(x),\ \partial_{j_1j_2} s^a(x),\ \ldots\right)_{|\alpha| \le k}.
$$

The assignment $s \mapsto j_k s$ is a linear map $\Gamma(E) \to \Gamma(J^kE)$ over the identity of $M$.

*Proof.* A section is locally a tuple of functions; the derivatives of total order at most $k$ of the tuple, evaluated at $x$, depend only on the $k$-jet and determine it, by Taylor's theorem with the remainder vanishing to order $k$. This gives the bijection with the displayed coordinate vector space; the transition functions are polynomial in the derivatives of the transition function of the bundle and smooth, which makes $J^kE$ a smooth bundle, and the map on sections is linear because differentiation is.

**Proposition (the jet exact sequence).** For $k \ge 1$ there is a short exact sequence of vector bundles over $M$

$$
0 \longrightarrow S^kT^*M \otimes E \longrightarrow J^kE \xrightarrow{\ \pi_{k-1}\ } J^{k-1}E \longrightarrow 0,
$$

where $\pi_{k-1}(j_k s(x)) = j_{k-1}s(x)$ forgets the derivatives of order exactly $k$, and the kernel is the bundle of the top-order derivatives, isomorphic to the $k$-th symmetric power of the cotangent bundle twisted by $E$. The sequence is natural in the bundle $E$ and splits, though not canonically.

*Proof.* The map $\pi_{k-1}$ is surjective because every $(k-1)$-jet is the truncation of a $k$-jet, and it is a bundle homomorphism. Its kernel at $x$ consists of the $k$-jets with vanishing derivatives of order at most $k-1$, which are the symmetric $k$-tensors $\sum_{|\alpha| = k} u^a_\alpha\, dx^\alpha \otimes e_a$; the transformation law of these coefficients under a change of coordinates is the symmetric $k$-th power of the Jacobian, which identifies the kernel with $S^kT^*_xM \otimes E_x$. A splitting is obtained by the polynomials of degree $k$, hence not canonically.

For $k=1$ the sequence reads $0 \to T^*M \otimes E \to J^1E \to E \to 0$, and the projection $J^1E \to E$ is the value of the jet; the kernel is the bundle of the first derivatives.

### Differential Operators as Bundle Maps

**Theorem.** Let $P : \Gamma(E) \to \Gamma(F)$ be an $\mathbb{R}$-linear map. Then $P$ is a differential operator of order at most $k$ if and only if there is a bundle homomorphism $\Phi : J^kE \to F$ such that

$$
P(s)(x) = \Phi\bigl(j_k s(x)\bigr) \qquad \text{for all } s \in \Gamma(E),\ x \in M .
$$

The homomorphism $\Phi$ is unique, and the assignment $P \leftrightarrow \Phi$ is an isomorphism of $C^\infty(M)$-modules

$$
D^k(E,F) \longrightarrow \Gamma\!\left(\operatorname{Hom}(J^kE, F)\right).
$$

*Proof.* If such a $\Phi$ exists, its expression in a chart and a frame is $\sum_{|\alpha|\le k} A_\alpha(x)\partial_\alpha s(x)$ with $A_\alpha$ the matrix of $\Phi$ on the fibre coordinates, so $P$ has order at most $k$; and $\Phi$ is smooth because $P$ is. Conversely, if $P$ has order at most $k$, its local expression shows that $P(s)(x)$ depends on $s$ only through $j_k s(x)$: two sections agreeing to order $k$ at $x$ have the same $P$-image at $x$, by the shape of the expression in any chart. This defines a map $\Phi_x : J^k_xE \to F_x$ by choosing a section $s$ with the given jet — the Taylor polynomial of the coordinate expression realises every jet — and putting $\Phi_x(j_k s(x)) = P(s)(x)$; the map is linear because $P$ is, and it is smooth because it is given in coordinates by the coefficient matrices, which are smooth. Uniqueness is the surjectivity of $j_k$ on the fibres: a homomorphism vanishing on every jet vanishes on every fibre. The module structure is read from the composition with functions, which act on $J^kE$ through the coordinate functions of the jets.

**Corollary.** The principal symbol of $P$ is the composition of the bundle surjection $S^kT^*M \otimes E \to J^kE$ of the jet exact sequence with $\Phi$:

$$
\sigma_k(P) : S^kT^*M \otimes E \longrightarrow J^kE \xrightarrow{\ \Phi\ } F .
$$

In particular the symbol is the top-order part of the bundle map, it is tensorial, and it vanishes exactly when $P$ has order at most $k-1$.

**Corollary.** A differential operator is exactly a map on sections that is local — the value of $Ps$ at $x$ depends on the germ of $s$ at $x$ — and $C^\infty(M)$-linear after composition with the jets. In particular the differential operators are the linear maps on sections that are local, and the operators of finite order are the maps that factor through some $J^k$.

*Proof.* The two statements are the theorem read in two directions: a bundle map out of $J^kE$ is local, and every local map of finite order factors through $j_k$ by the argument above. The converse statement that every local linear map of finite order is a differential operator is the same computation in coordinates.

## The Operator Layer of a Manifold

The examples of the previous sections assemble into the operator calculus that the rest of the Part uses, and the calculus is closed under composition, sum, and the operation of taking the adjoint with respect to a metric.

**Proposition.** The differential operators on the sections of the bundles of $M$ form a filtered algebra: the spaces $D^k(E,F)$ are nested and increasing, they are closed under composition with the order filtration, and the associated graded is the graded algebra generated by the symbols, the product being the composition of homomorphisms of fibres. The symbol is the $\sigma_\bullet$ of this graded algebra, and it is the reason the elliptic operators — those with invertible symbols — form a set closed under composition and under the formation of the Laplace-type operators of a complex.

**Elliptic complexes.** A **complex of differential operators** is a sequence

$$
\cdots \longrightarrow \Gamma(E_{i-1}) \xrightarrow{\ P_{i-1}\ } \Gamma(E_i) \xrightarrow{\ P_i\ } \Gamma(E_{i+1}) \longrightarrow \cdots
$$

with $P_i \circ P_{i-1} = 0$ for every $i$. The complex is **elliptic** if the induced sequence of symbols

$$
\cdots \longrightarrow E_{i-1} \xrightarrow{\ \sigma(P_{i-1})(x,\xi)\ } E_i \xrightarrow{\ \sigma(P_i)(x,\xi)\ } E_{i+1} \longrightarrow \cdots
$$

is exact for every $x \in M$ and every nonzero $\xi \in T^*_xM$. An elliptic complex has finite-dimensional cohomology when $M$ is compact, and on it the Hodge theory of *Differential Forms and Stokes' Theorem* applies: the complex carries the Laplace-type operator $\Delta_i = P_i^*P_i + P_{i-1}P_{i-1}^*$, its harmonic sections are the canonical representatives of the cohomology, and the index of the complex, the alternating sum of the dimensions of its cohomology, is the topological invariant that Part IV computes from the symbol.

The **de Rham complex** of *Differential Forms and Stokes' Theorem* is the fundamental example: the operators are the exterior derivative on the forms, the composition $d \circ d = 0$ is the statement of the complex, and the symbol sequence $0 \to \Lambda^p T^*_xM \to \Lambda^{p+1}T^*_xM \to \cdots$ is exact for $\xi \neq 0$ by the algebraic contractibility of the exterior algebra with respect to the multiplication by $\xi$, as in *The Exterior Algebra*. Its Laplace-type operator is the Laplace–de Rham operator, whose analysis is *The Codifferential* and *The L2 Adjoint of a Differential Operator*. The Dolbeault complex of a complex manifold is the other fundamental example, and it is named here with a forward reference to *Hermitian Geometry and Almost Complex Structures* in Part IV, where the complex structure that defines it is treated.

## Summary

A differential operator of order at most $k$ is a linear map on the sections of a vector bundle whose local expression differentiates the coefficients at most $k$ times; the order is well defined, the operators of order at most $k$ form the module $D^k(E,F)$, the sum is order at most the maximum and the composition is order at most the sum. The commutator with a function lowers the order by one, and the iterated commutators characterise the order.

The principal symbol $\sigma_k(P)$ is the top-order part of the operator read as a linear map $S^kT^*M \otimes E \to F$ on the fibres; it is tensorial, it depends on $P$ only through the class of $P$ modulo the operators of order at most $k-1$, and it multiplies under composition and transposes with a sign under the adjoint. The operator is elliptic when its symbol is invertible off the zero section, and the elliptic operators are closed under composition.

The jet bundle $J^kE$ is the bundle of the $k$-jets of the sections, with the jet exact sequence $0 \to S^kT^*M \otimes E \to J^kE \to J^{k-1}E \to 0$, in which the kernel is the bundle of the top-order derivatives. The structural theorem of the subject identifies an operator of order at most $k$ with a bundle homomorphism $J^kE \to F$, uniquely, and this identification is an isomorphism of $C^\infty(M)$-modules: the differential operators of order at most $k$ are the bundle maps out of the $k$-jet bundle, the symbol is the induced map on the graded quotient, and the operators are exactly the local linear maps on sections. The calculus closes under composition and adjoints, and the elliptic complexes — the de Rham complex first among them — are the setting of the Hodge and index theory of the Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E, F, G$ | Smooth vector bundles over $M$; $r = \operatorname{rank} E$, $s = \operatorname{rank} F$ |
| $\Gamma(E)$ | Module of smooth sections of $E$ over $C^\infty(M)$ |
| $D^k(E,F)$ | Differential operators $E \to F$ of order at most $k$ |
| $\operatorname{ord}(P)$ | Order of the operator $P$; least $k$ with $P \in D^k$ |
| $\partial_\alpha$, $\lvert\alpha\rvert$ | Multiple partial derivative and the length of its multi-index |
| $[P,f] = Pf - fP$ | Commutator with the multiplication by a function; order at most $\operatorname{ord}(P)-1$ |
| $\sigma_k(P)(x,\xi)$ | Principal symbol, a linear map $E_x \to F_x$ |
| $S^kT^*M$ | $k$-th symmetric power of the cotangent bundle |
| $\sigma_{k+l}(QP) = \sigma_l(Q)\sigma_k(P)$ | Symbol of a composition |
| $\sigma_k(P^*)(\xi) = (-1)^k\sigma_k(P)(\xi)^*$ | Symbol of a formal adjoint |
| Elliptic, $\operatorname{char}(P)$ | Invertible symbol off the zero section; the zeros of the symbol |
| $J^kE$, $J^k_xE$ | Bundle of $k$-jets of $E$, and its fibre at $x$ |
| $j_k s(x)$ | $k$-jet of the section $s$ at $x$ |
| $\pi_{k-1} : J^kE \to J^{k-1}E$ | Forgetting the derivatives of order exactly $k$ |
| $0 \to S^kT^*M\otimes E \to J^kE \to J^{k-1}E \to 0$ | Jet exact sequence |
| $P = \Phi \circ j_k$ | An operator of order at most $k$ is a bundle map $\Phi : J^kE \to F$ |
| $d$, $\nabla_X$, $\mathcal{L}_X$ | The exterior, covariant and Lie derivatives; operators of order at most $1$ |
| $\Delta = d\delta + \delta d$ | Laplace–de Rham operator; elliptic of order $2$ |
| Complex $(E_\bullet, P_\bullet)$, elliptic complex | $P_iP_{i-1} = 0$, with exact symbol sequence off the zero section |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, vol. III (Springer, 1985), for the calculus of differential operators, the symbol and the jets.
- John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed. (Springer, 2013), for the tangent bundle, the jet bundle and the local characterisation of a differential operator.
- Dominic G. B. Edelen, *Applied Exterior Calculus* (Wiley, 1985), for the jet-bundle formulation of the differential operators.
- Michael E. Taylor, *Partial Differential Equations*, vol. I (Springer, 2nd ed. 2011), for the symbol, ellipticity and the Laplace-type operators of a complex.
- I. M. Gelfand, "On elliptic equations", *Russian Mathematical Surveys* 15 (1960), 113–123, for the ellipticity of a complex of differential operators.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators I", *Annals of Mathematics* 87 (1968), 484–530, for the index of an elliptic complex, cited here for the forward reference to Part IV.
