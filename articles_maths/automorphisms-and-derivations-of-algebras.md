
# __Automorphisms and Derivations of Algebras__

## Introduction

The ideal theory of an algebra records its quotients; the group $\operatorname{Aut}_R(A)$ of its $R$-algebra automorphisms and the Lie algebra $\operatorname{Der}_R(A)$ of its derivations record its symmetries and their infinitesimal counterparts. This article develops both, together with the relation between them: inner automorphisms, the normal subgroup they form, the outer automorphism group that results, the derivation algebra with its bracket, the inner derivations, and the exponential that passes from one to the other when the ground ring permits.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ and $A$ is an $R$-algebra. Automorphisms are $R$-algebra automorphisms, so they are $R$-linear and multiplicative; the ground ring is named whenever the group depends on it. The pair $(\operatorname{Aut}_R(A), \operatorname{Der}_R(A))$ is the algebra analogue of a Lie group and its Lie algebra, and over a general ring only the algebraic shadow of that correspondence survives; the analytic version requires the topology of a topological or Banach algebra, supplied in Part II.

No metric structure is part of the data of an algebra. An automorphism preserves addition, scalar multiplication and the product, and nothing else; lengths and angles are extra structures that an algebra automorphism need not preserve. The final section makes that point with an example.

## Algebra Automorphisms

**Definition.** An **$R$-algebra automorphism** of $A$ is a bijective $R$-linear map $\sigma : A \to A$ with

$$
\sigma(xy) = \sigma(x)\sigma(y)
$$

for all $x, y \in A$. The set of all such maps is a group under composition, written $\operatorname{Aut}_R(A)$, with identity the identity map. If $A$ is unital and the automorphisms are required to be unital, $\sigma(1_A) = 1_A$, the resulting subgroup is written $\operatorname{Aut}_R^{\mathrm{un}}(A)$; over a unital algebra multiplicativity already forces $\sigma(1_A) = 1_A$, so the two groups coincide there. Indeed $e = \sigma(1_A)$ satisfies $e^2 = \sigma(1_A \cdot 1_A) = e$, and since $\sigma$ is surjective there is $a$ with $\sigma(a) = 1_A$, whence $\sigma(a) = \sigma(a \cdot 1_A) = \sigma(a)e = e$, so $a = 1_A$ by injectivity and $e = 1_A$.

**Proposition.** Every algebra automorphism maps the centre onto itself, and it preserves idempotents, units, zero divisors and the lattice of two-sided ideals.

*Proof.* The centre statement is proved in *Centre, Units, Zero Divisors and Division Algebras*: $\sigma$ restricts to an automorphism of $Z(A)$. If $e^2 = e$ then $\sigma(e)^2 = \sigma(e)$; if $u$ is a unit then $\sigma(u)^{-1} = \sigma(u^{-1})$; if $zw = 0$ then $\sigma(z)\sigma(w) = 0$; and if $I$ is a two-sided ideal then $\sigma(I)$ is one, with inverse the same statement for $\sigma^{-1}$.

### Inner Automorphisms

**Definition.** Let $A$ be unital and associative, and let $u \in A^\times$. The **inner automorphism** determined by $u$ is

$$
\iota_u(x) = uxu^{-1}, \qquad x \in A.
$$

**Proposition.** For every unit $u$, the map $\iota_u$ is an algebra automorphism, and

$$
\iota_u \circ \iota_v = \iota_{uv}, \qquad \iota_u^{-1} = \iota_{u^{-1}}, \qquad \iota_1 = \mathrm{id}.
$$

Hence $u \mapsto \iota_u$ is a group homomorphism $A^\times \to \operatorname{Aut}_R(A)$ whose image is the subgroup of **inner automorphisms**, written $\operatorname{Inn}_R(A)$.

*Proof.* The map is $R$-linear and bijective with inverse $\iota_{u^{-1}}$, and

$$
\iota_u(xy) = uxyu^{-1} = (uxu^{-1})(uyu^{-1}) = \iota_u(x)\iota_u(y).
$$

The composition and identity statements are direct.

**Theorem.** The homomorphism $A^\times \to \operatorname{Aut}_R(A)$, $u \mapsto \iota_u$, has kernel $Z(A)^\times$, so

$$
\operatorname{Inn}_R(A) \;\cong\; A^\times / Z(A)^\times.
$$

*Proof.* The inner automorphism $\iota_u$ is the identity exactly when $ux = xu$ for all $x$, that is, when $u \in Z(A)$; with $u$ a unit this is $u \in Z(A)^\times$. The first isomorphism theorem for groups gives the displayed isomorphism.

**Proposition.** $\operatorname{Inn}_R(A)$ is a normal subgroup of $\operatorname{Aut}_R(A)$, and for $\sigma \in \operatorname{Aut}_R(A)$,

$$
\sigma \circ \iota_u \circ \sigma^{-1} = \iota_{\sigma(u)}.
$$

*Proof.* Compute on $x$: $(\sigma \iota_u \sigma^{-1})(x) = \sigma(u\,\sigma^{-1}(x)\,u^{-1}) = \sigma(u)\,x\,\sigma(u)^{-1} = \iota_{\sigma(u)}(x)$, using multiplicativity of $\sigma$ and $\sigma^{-1}$. Since $\sigma(u)$ is a unit, $\sigma \operatorname{Inn}\sigma^{-1} \subseteq \operatorname{Inn}$; applying this to $\sigma^{-1}$ gives equality.

**Definition.** The **outer automorphism group** is the quotient

$$
\operatorname{Out}_R(A) = \operatorname{Aut}_R(A)/\operatorname{Inn}_R(A).
$$

These definitions require $A$ unital and associative. For a commutative algebra every inner automorphism is the identity, because $Z(A) = A$ and $A^\times/Z(A)^\times$ is trivial; all automorphisms are outer.

### Worked Cases

**Commutative algebras.** Let $A$ be commutative and associative. Then $\operatorname{Inn}_R(A) = 1$ and $\operatorname{Aut}_R(A) = \operatorname{Out}_R(A)$ is simply the group of $R$-algebra automorphisms of $A$. For $A = \mathbb{C}$ over $R = \mathbb{R}$, an $\mathbb{R}$-algebra automorphism fixes $\mathbb{R}$ pointwise and sends $i$ to an element $z$ with $z^2 = -1$, so $z = \pm i$; hence

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) = \{\mathrm{id}, \kappa\} \cong \mathbb{Z}/2, \qquad \kappa(z) = \bar{z}.
$$

Over $\mathbb{C}$ there are no nontrivial automorphisms fixing $\mathbb{C}$, so the $\mathbb{C}$-algebra automorphism group is trivial. As a *field*, however, $\mathbb{C}$ has many more automorphisms than the identity and conjugation: every automorphism of the field $\mathbb{C}$ restricting to a permutation of a transcendence basis over $\mathbb{Q}$ is nontrivial, and there are uncountably many. The contrast shows that the group depends on the ground ring and on the structure one is preserving.

**The split complex numbers.** Over $\mathbb{R}$, an automorphism of $\mathbb{D}$ sends $j$ to an element $c$ with $c^2 = 1$. Writing $c = a + bj$ and solving $a^2 + b^2 = 1$, $ab = 0$ gives $c = \pm 1$ or $c = \pm j$; the values $\pm 1$ fail injectivity on $j \mp 1$, so $c = \pm j$ and

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{D}) = \{\mathrm{id}, \tau\} \cong \mathbb{Z}/2, \qquad \tau(j) = -j,
$$

which is the swap $e_+ \leftrightarrow e_-$ of the two idempotents.

**The dual numbers.** An automorphism of $\mathbb{D}'$ fixes $1$ and sends $\varepsilon$ to $c + d\varepsilon$; from $0 = \varphi(\varepsilon^2) = \varphi(\varepsilon)^2 = c^2 + 2cd\varepsilon$ one gets $c = 0$, and $d \neq 0$ by injectivity. Every $d \in \mathbb{R}^\times$ occurs, so

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{D}') \cong \mathbb{R}^\times, \qquad \varepsilon \mapsto d\varepsilon.
$$

This automorphism fixes $1$ and rescales the infinitesimal direction; it changes a structure that happens to be present on the underlying module, which is the first indication that an automorphism carries no information beyond the product.

**The quaternions.** Over $\mathbb{R}$ one has

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{H}) = \operatorname{Inn}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}^\times/\mathbb{R}^\times .
$$

The quotient is read on the pure imaginary part, which an inner automorphism preserves: the kernel of $\mathbb{H}^\times \to \operatorname{Inn}_{\mathbb{R}}(\mathbb{H})$ is $\mathbb{R}^\times$, so the unit quaternions form a subgroup mapping onto the quotient with kernel $\{\pm 1\}$. The identification of this group with the group of rotations of $\mathbb{R}^3$, and the double cover by the unit quaternions, are made in *Quaternion Rotations and Reflections*, where a form and a length are available.

**The quaternion and biquaternion algebras over other rings.** Over $\mathbb{C}$, the biquaternion algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, and every automorphism is inner, so

$$
\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) \cong GL_2(\mathbb{C})/\mathbb{C}^\times = PGL(2,\mathbb{C}) = PSL(2,\mathbb{C}).
$$

Over $\mathbb{R}$ the group is larger, $\operatorname{Aut}_{\mathbb{R}}(\mathbb{B}) \cong PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2$, the extra coset supplied by complex conjugation. The two ground fields and the Skolem–Noether theorem behind the first case are worked out in Part V.

**Matrix algebras.** Let $k$ be a field. Every $k$-algebra automorphism of $M_n(k)$ is inner:

$$
\operatorname{Aut}_k(M_n(k)) = \operatorname{Inn}_k(M_n(k)) \cong GL_n(k)/k^\times = PGL_n(k).
$$

This is the Skolem–Noether theorem: for every automorphism $\sigma$ there exists $g \in GL_n(k)$ with $\sigma(x) = gxg^{-1}$. The theorem holds more generally for every central simple algebra over a field.

**The Galois action.** Let $L/K$ be a field extension and let $A$ be a $K$-algebra. For $\sigma \in \operatorname{Aut}_K(L)$ define

$$
\sigma \cdot (\lambda \otimes a) = \sigma(\lambda) \otimes a
$$

on $L \otimes_K A$. If $L/K$ is a finite Galois extension, this gives an action of $\operatorname{Gal}(L/K) = \operatorname{Aut}_K(L)$ by $K$-algebra automorphisms of $L \otimes_K A$, and the fixed points are the image of $1 \otimes A$. This is the way a Galois group acts on an algebra obtained by extension of scalars, and it is the algebraic input to Galois descent.

## Derivations

**Definition.** Let $A$ be an $R$-algebra. A **derivation** of $A$ over $R$ is an $R$-linear map $\delta : A \to A$ satisfying the **Leibniz rule**

$$
\delta(xy) = \delta(x)\,y + x\,\delta(y)
$$

for all $x, y \in A$. The set of all such maps is written $\operatorname{Der}_R(A)$.

If $A$ is unital then every derivation satisfies $\delta(1_A) = 0$, because $\delta(1_A) = \delta(1_A \cdot 1_A) = 2\delta(1_A)$. The Leibniz rule is the infinitesimal form of multiplicativity: a one-parameter family of automorphisms $\varphi_t$ with $\varphi_0 = \mathrm{id}$ and $\varphi_t(xy) = \varphi_t(x)\varphi_t(y)$ has derivative at $t = 0$ obeying the rule, which is why a derivation is called an **infinitesimal automorphism**.

**Example.** For the polynomial algebra, a derivation satisfies $\delta(1) = 0$ and is determined by its value $f(x) = \delta(x)$ at $x$, since

$$
\delta(x^n) = n x^{n-1}\delta(x) = n x^{n-1} f(x).
$$

Hence $\delta = f \partial_x$ and

$$
\operatorname{Der}_R(R[x]) = R[x]\,\partial_x,
$$

a free $R[x]$-module of rank one, with $\partial_x = d/dx$ the usual formal derivative.

**Example.** For the quaternion algebra, $\operatorname{Der}_{\mathbb{R}}(\mathbb{H})$ is the space of inner derivations below; it is three-dimensional and its bracket is twice the commutator product on the space of pure imaginary quaternions.

**Example.** For the dual numbers, $\delta(1) = 0$ and Leibniz applied to $\varepsilon^2 = 0$ gives $0 = \delta(\varepsilon^2) = 2\varepsilon\,\delta(\varepsilon)$, so $\delta(\varepsilon)$ lies in the annihilator of $\varepsilon$, which is $\mathbb{R}\varepsilon$. Thus $\delta(\varepsilon) = c\varepsilon$ and $\delta(x + y\varepsilon) = cy\varepsilon$; consequently

$$
\operatorname{Der}_{\mathbb{R}}(\mathbb{D}') = \mathbb{R}\,\delta, \qquad \delta(\varepsilon) = \varepsilon,
$$

a one-dimensional space whose exponential is the automorphism $\varepsilon \mapsto e^{c}\varepsilon$.

### The Lie Algebra Structure

**Theorem.** Let $A$ be associative. For $\delta, \varepsilon \in \operatorname{Der}_R(A)$ define the commutator

$$
[\delta, \varepsilon] = \delta \circ \varepsilon - \varepsilon \circ \delta.
$$

Then $[\delta, \varepsilon]$ is a derivation, $\operatorname{Der}_R(A)$ is an $R$-module under this bracket, and the bracket is antisymmetric and satisfies the Jacobi identity. Hence $\operatorname{Der}_R(A)$ is a Lie algebra over $R$.

*Proof.* For the Leibniz rule,

$$
(\delta\varepsilon - \varepsilon\delta)(xy) = \delta\bigl(\varepsilon(x)y + x\varepsilon(y)\bigr) - \varepsilon\bigl(\delta(x)y + x\delta(y)\bigr)
$$

$$
= \delta\varepsilon(x)\,y + \varepsilon(x)\delta(y) + \delta(x)\varepsilon(y) + x\,\delta\varepsilon(y) - \varepsilon\delta(x)\,y - \delta(x)\varepsilon(y) - \varepsilon(x)\delta(y) - x\,\varepsilon\delta(y)
$$

$$
= (\delta\varepsilon - \varepsilon\delta)(x)\,y + x\,(\delta\varepsilon - \varepsilon\delta)(y),
$$

where $\delta(x)$ and $\varepsilon(x)$ were interchanged by associativity. Antisymmetry is immediate, and the Jacobi identity is the identity of operators on the composition of linear maps: for endomorphisms $u,v,w$ of any module, $[u,[v,w]] + [v,[w,u]] + [w,[u,v]] = 0$.

Associativity of $A$ is needed in the displayed expansion, at the point where the middle terms regroup. The derivation space is also a module over the centre: for $z \in Z(A)$ and $\delta \in \operatorname{Der}_R(A)$, the map $z\delta$ is a derivation because $z$ may be moved past $\delta(x)$ and past $x$.

**Example.** $\operatorname{Der}_{\mathbb{R}}(\mathbb{R}) = 0$ and $\operatorname{Der}_{\mathbb{R}}(\mathbb{C}) = 0$: a derivation of a field extension vanishes on the ground field and, for $\mathbb{C}$, is forced to vanish on $i$ by $0 = \delta(i^2) = 2i\,\delta(i)$. More generally $\operatorname{Der}_K(K) = 0$ for any field $K$ and ground field $K$ itself.

**Example (the split complex numbers revisited).** $\operatorname{Der}_{\mathbb{R}}(\mathbb{D})$ is zero. If $\delta$ is a derivation then $0 = \delta(j^2) = j\delta(j) + \delta(j)j = 2j\,\delta(j)$, and $j$ is a unit, so $\delta(j) = 0$ and $\delta = 0$. Thus $\mathbb{D}$ has automorphisms but no infinitesimal automorphisms, while $\mathbb{D}'$ has both.

### Inner Derivations

**Definition.** Let $A$ be associative, and for $a \in A$ define

$$
\mathrm{ad}_a(x) = ax - xa = [a, x], \qquad x \in A.
$$

The map $\mathrm{ad}_a$ is the **inner derivation** determined by $a$, and the set of inner derivations is written $\operatorname{InnDer}_R(A)$.

**Proposition.** For each $a \in A$, the map $\mathrm{ad}_a$ is a derivation, and

$$
[\mathrm{ad}_a, \mathrm{ad}_b] = \mathrm{ad}_{[a,b]}
$$

for all $a, b \in A$. Hence $a \mapsto \mathrm{ad}_a$ is a Lie algebra homomorphism $A \to \operatorname{Der}_R(A)$ whose kernel is the centre $Z(A)$, and

$$
\operatorname{InnDer}_R(A) \;\cong\; A/Z(A)
$$

as Lie algebras, where $A/Z(A)$ carries the bracket induced by the commutator.

*Proof.* The Leibniz rule is the identity $[a, xy] = [a,x]y + x[a,y]$, which is associativity. The bracket identity is the Jacobi identity in the form $[[a,b],x] = [a,[b,x]] - [b,[a,x]]$. The kernel of $\mathrm{ad}$ consists of those $a$ with $[a,x] = 0$ for all $x$, which is exactly $Z(A)$.

**Theorem (every derivation of a central simple algebra is inner).** Let $k$ be a field and let $A$ be a finite-dimensional central simple $k$-algebra. Then $\operatorname{Der}_k(A) = \operatorname{InnDer}_k(A)$.

The proof is the standard one, by a computation with matrix units after extending scalars to an algebraic closure; for $M_n(k)$ it also follows from the identification $\operatorname{Der}_k(M_n(k)) \cong \mathrm{SL}_n(k)$ below. The theorem is the derivation-level companion of Skolem–Noether and is a special case of the vanishing of the first Hochschild cohomology of a separable algebra.

**Example ($M_n(k)$).** Since $Z(M_n(k)) = k I_n$ is one-dimensional, the inner derivations form the quotient $M_n(k)/k I_n$, the **traceless matrices** $\mathrm{SL}_n(k)$, of dimension $n^2 - 1$. Hence

$$
\operatorname{Der}_k(M_n(k)) = \operatorname{InnDer}_k(M_n(k)) \cong \mathrm{SL}_n(k).
$$

Writing $E_{ij}$ for the matrix units, the derivations $\mathrm{ad}_{E_{ij}}$ for $(i,j) \neq (n,n)$ span the space, and the bracket is the matrix commutator.

**Example ($\mathbb{H}$).** By the theorem, $\operatorname{Der}_{\mathbb{R}}(\mathbb{H}) = \operatorname{InnDer}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}/\mathbb{R}$, the three-dimensional space of pure imaginary quaternions. For pure imaginary $p$ and $q$ the quaternion product splits as $pq = \mathrm{Sc}(pq) + \mathrm{Vec}(pq)$ into its scalar and its pure imaginary part, and

$$
[p, q] = pq - qp = 2\,\mathrm{Vec}(pq),
$$

so the bracket on $\operatorname{Der}_{\mathbb{R}}(\mathbb{H})$ is twice the commutator product of the pure imaginary parts. Rescaling the basis to $D_k = \tfrac{1}{2}\mathrm{ad}_{e_k}$ gives the structure constants

$$
[D_1, D_2] = D_3, \qquad [D_2, D_3] = D_1, \qquad [D_3, D_1] = D_2 .
$$

Hence

$$
\operatorname{Der}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}/\mathbb{R} \text{ with the bracket } [p,q] = 2\,\mathrm{Vec}(pq),
$$

the commutator Lie algebra of the automorphism group $\operatorname{Aut}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}^\times/\mathbb{R}^\times$ computed above. The identification of this three-dimensional Lie algebra with the Lie algebra of the rotations of $\mathbb{R}^3$ is made in *Quaternion Rotations and Reflections*, where a form is available; the structure constants alone are what this article computes.

**Example ($\mathbb{B}$).** The biquaternion algebra is $M_2(\mathbb{C})$ over $\mathbb{C}$, so every $\mathbb{C}$-linear derivation is inner and $\operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathrm{SL}_2(\mathbb{C})$, of complex dimension $3$. Over $\mathbb{R}$ the same space results, because $\mathbb{R}$-linear derivations of $\mathbb{B}$ are automatically $\mathbb{C}$-linear: the centre $\mathbb{C}_{\mathbb{B}}$ is a finite separable field extension of $\mathbb{R}$ and admits no nonzero derivation. The details, including the identification with the traceless part, are.

## The Exponential Correspondence

**Proposition.** Suppose $A$ is an associative $R$-algebra with $\mathbb{Q} \subseteq R$, so that the rational numbers act, and let $\delta \in \operatorname{Der}_R(A)$ be **nilpotent**, $\delta^N = 0$ for some $N \geq 1$. Then

$$
\exp(\delta) = \sum_{k=0}^{N-1} \frac{\delta^k}{k!}
$$

is an algebra automorphism of $A$, with inverse $\exp(-\delta)$.

*Proof.* The sum is finite, so it is a well-defined $R$-linear map. The Leibniz rule iterated gives

$$
\delta^k(xy) = \sum_{j=0}^{k} \binom{k}{j} \delta^j(x)\,\delta^{k-j}(y),
$$

which is the binomial theorem for derivations; dividing by $k!$ and summing over $k$ yields

$$
\exp(\delta)(xy) = \exp(\delta)(x)\,\exp(\delta)(y).
$$

The same identity applied to $\exp(-\delta)$, together with the commutativity of $\delta$ with its powers in the product $\exp(\delta)\exp(-\delta) = \exp(0) = 1$, gives the inverse.

**Proposition (the automorphisms of the dual-number algebra).** Let $\varepsilon^2 = 0$ and let $\varphi = \mathrm{id} + \varepsilon\delta$ be an $R[\varepsilon]$-algebra automorphism of $A[\varepsilon]$. Then $\delta$ is a derivation of $A$.

*Proof.* Write $\varphi(x) = x + \varepsilon\delta(x)$ and expand $\varphi(xy) = \varphi(x)\varphi(y)$; the terms containing $\varepsilon^2$ vanish, and the coefficient of $\varepsilon$ is $\delta(xy) = \delta(x)y + x\delta(y)$.

The proposition is the algebraic form of the statement that the infinitesimal automorphisms of $A$ are its derivations. The analytic form, in which a differentiable family $\varphi_t$ of automorphisms with $\varphi_0 = \mathrm{id}$ is differentiated at $t = 0$, is the same computation read with the derivative of Part III, where the limit is available.

**Theorem (inner derivations exponentiate to inner automorphisms).** Let $a \in A$ and suppose $\exp(a)$ is a unit of $A$. Then

$$
\exp(\mathrm{ad}_a) = \iota_{\exp(a)}, \qquad \text{that is, } \exp(\mathrm{ad}_a)(x) = e^{a}\,x\,e^{-a}.
$$

This is the identity $\mathrm{Ad}_{e^a} = e^{\mathrm{ad}_a}$ of the adjoint representation. The identity is algebraic when $a$ is nilpotent, the series then terminating; in general it is read with the limit of Part II, where the series may be given a value.

**Failure over a general ring.** The exponential is not available over an arbitrary commutative ring. If $\delta$ is not nilpotent the sum $\sum \delta^k/k!$ is a formal series that need not terminate, the coefficients $1/k!$ need not make sense — over a field of characteristic $p > 0$ the integer $k!$ vanishes for $k \geq p$ — and giving the series a value requires a limit, hence the norms of Part II. There is then no map from derivations to automorphisms in general, and the passage from the Lie algebra to the group is treated in *Topological Algebras and Banach Algebras*. Nilpotent derivations are the case in which the exponential survives over any $\mathbb{Q}$-algebra, and that is the case used in practice.

## What an Algebra Automorphism Does Not Preserve

The data of an $R$-algebra $A$ are the module structure and the product. An automorphism is required to preserve exactly these, so any further structure that happens to be present on the underlying module — a length, an angle, a volume — is not automatically preserved.

**Example.** The automorphism $\varphi(\varepsilon) = d\varepsilon$ of $\mathbb{D}'$, $d \neq 1$, has matrix $\begin{pmatrix} 1 & 0 \\ 0 & d \end{pmatrix}$ in the basis $\{1, \varepsilon\}$. It preserves the product because it fixes $1$ and scales $\varepsilon$, but it is not the identity map of the underlying module, and an extra structure on that module is not automatically preserved by it.

**Example.** On $\mathbb{B} \cong M_2(\mathbb{C})$ the invariant $\sum_\mu Q_\mu^2$ of the coefficients — the determinant of the corresponding matrix, an algebraic function of the coordinates — is carried along by **every** inner automorphism, conjugation by a matrix leaving the determinant unchanged; the complex conjugation $\sigma(\tilde{Q}) = \tilde{Q}^{*}$ of the coefficients moves it and is not inner. Whether one of these quantities survives is a property of the quantity and not of the automorphism.

The group of transformations preserving a length or an angle is therefore a different object, generally not contained in $\operatorname{Aut}_R(A)$. Such structure-preserving maps belong to the theory of forms and Clifford algebras, and are treated in the category *Topology on Algebras with a degree-2 form*; the algebra automorphism group is the layer below them.

## Summary

The **automorphisms** of an $R$-algebra $A$ form the group $\operatorname{Aut}_R(A)$; they preserve the centre, idempotents, units, zero divisors and the lattice of two-sided ideals. Inner automorphisms $\iota_u(x) = uxu^{-1}$ by units form the normal subgroup $\operatorname{Inn}_R(A) \cong A^\times/Z(A)^\times$, the outer automorphism group is $\operatorname{Out}_R(A) = \operatorname{Aut}_R(A)/\operatorname{Inn}_R(A)$, and for a commutative algebra all automorphisms are outer. The worked cases are $\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) \cong \mathbb{Z}/2$, $\operatorname{Aut}_{\mathbb{R}}(\mathbb{D}) \cong \mathbb{Z}/2$, $\operatorname{Aut}_{\mathbb{R}}(\mathbb{D}') \cong \mathbb{R}^\times$, $\operatorname{Aut}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}^\times/\mathbb{R}^\times$, and $\operatorname{Aut}_k(M_n(k)) \cong PGL_n(k)$ for a field $k$; over $\mathbb{C}$ the biquaternion group is $PGL(2,\mathbb{C})$, over $\mathbb{R}$ it is $PGL(2,\mathbb{C}) \rtimes \mathbb{Z}/2$.

The **derivations** $\operatorname{Der}_R(A)$ are the $R$-linear maps satisfying the Leibniz rule; they form a Lie algebra under the commutator, and a module over the centre. The inner derivations $\mathrm{ad}_a = [a,\cdot]$ form the Lie algebra $A/Z(A)$, and for a central simple algebra every derivation is inner, so $\operatorname{Der}_k(M_n(k)) \cong \mathrm{SL}_n(k)$ and $\operatorname{Der}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}/\mathbb{R}$, the bracket being twice the commutator product of the pure imaginary parts. The exponential $\exp(\delta)$ of a nilpotent derivation is an automorphism over any $\mathbb{Q}$-algebra, inner derivations exponentiate to inner automorphisms, and over a general ring the exponential may not exist.

An algebra automorphism preserves the product and nothing more; a length or an angle is extra structure that need not be preserved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $A$ | $R$-algebra, unital and associative where stated |
| $\operatorname{Aut}_R(A)$ | Group of $R$-algebra automorphisms of $A$ |
| $A^\times$ | Group of units of $A$ |
| $\iota_u(x) = uxu^{-1}$ | Inner automorphism by a unit $u$ |
| $\operatorname{Inn}_R(A) \cong A^\times/Z(A)^\times$ | Group of inner automorphisms |
| $\operatorname{Out}_R(A)$ | Outer automorphism group, $\operatorname{Aut}_R/\operatorname{Inn}_R$ |
| $Z(A)$ | Centre of $A$ |
| $\operatorname{Der}_R(A)$ | Lie algebra of $R$-linear derivations |
| $\mathrm{ad}_a(x) = [a,x]$ | Inner derivation by $a$ |
| $\operatorname{InnDer}_R(A) \cong A/Z(A)$ | Inner derivations |
| $[\delta,\varepsilon]$ | Commutator bracket on derivations |
| $\delta = f\partial_x$ | The derivations of $R[x]$ |
| $D_k = \tfrac{1}{2}\mathrm{ad}_{e_k}$ | Basis of $\operatorname{Der}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}/\mathbb{R}$ |
| $PGL_n(k) = GL_n(k)/k^\times$ | Automorphism group of $M_n(k)$ |
| $\exp(\delta)$ | Exponential of a derivation |
| $\mathbb{H}/\mathbb{R}$, $\mathrm{SL}_n(k)$ | Commutator Lie algebra of the imaginary quaternions and traceless matrices |
| $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ | Complex, split complex and dual numbers |
| $\mathbb{H}$, $\mathbb{B}$ | Quaternions and biquaternions |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace of $\mathbb{B}$ |



## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for derivations and their Lie algebra structure.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for automorphisms, inner automorphisms and derivations.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, MAA, 1968), for the Skolem–Noether theorem and central simple algebras.
- John Voight, *Quaternion Algebras* (Springer, 2021), for automorphisms and derivations of quaternion algebras.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the Lie algebra background.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for derivations of algebras over commutative rings.
