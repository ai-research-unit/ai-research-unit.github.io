
# __Operator Algebras__

## Introduction

*Topological Algebras and Banach Algebras* developed algebras carrying a complete norm, and showed that the analytic structure of a Banach algebra already controls its algebra: the unit group is open, the spectrum is nonempty, and a complex Banach division algebra must be $\mathbb{C}$. Operator algebras are the algebras that arise when the Banach algebra is an algebra of bounded operators on a Hilbert space and the norm is supplemented by an involution, the adjoint. The extra structure is rigid enough to make the algebra almost determine itself: a $\mathrm{C}^*$-algebra carries a canonical norm, it has a faithful representation on Hilbert space, and, in the commutative case, it is nothing but an algebra of continuous functions.

This article develops that theory. It is the analytic counterpart of the structural articles *Ideals and Quotients of Algebras*, *Centre, Units, Zero Divisors and Division Algebras* and *Automorphisms and Derivations of Algebras*, and it uses the Banach-algebra theory throughout. The representation theory of Hilbert-space representations is intrinsic to the subject and is treated here; the module-theoretic representation theory of algebras belongs to category 08. No physics is invoked, and no particular operator algebra of physical origin is developed. Throughout, $A$ denotes a $\mathrm{C}^*$-algebra, $\mathcal{M}$ a von Neumann algebra and $H$ a Hilbert space; the von Neumann algebra is written $\mathcal{M}$ so that the plain letter $M$ keeps its meaning of a module in the structural articles. The modular operators $\Delta_\omega$ and $\varsigma_t^\omega$ are introduced where they are used.

## Algebras of Bounded Operators

**Definition.** Let $H$ be a complex Hilbert space with inner product $\langle \cdot, \cdot\rangle$ linear in the first variable. The set $B(H)$ of bounded linear operators on $H$ is a complex algebra under addition, composition and scalar multiplication, with the **operator norm**

$$
\|T\| = \sup_{\|x\| \leq 1}\|Tx\|,
$$

under which it is complete, and with the **adjoint** $T^*$ characterised by

$$
\langle Tx, y\rangle = \langle x, T^*y\rangle, \qquad x, y \in H .
$$

The map $T \mapsto T^*$ is conjugate-linear, involutive and an anti-automorphism: $(ST)^* = T^*S^*$.

**Proposition (the $\mathrm{C}^*$-identity).** For every $T \in B(H)$,

$$
\|T^*T\| = \|T\|^2 .
$$

*Proof.* One inequality is $\|T^*T\| \leq \|T^*\|\|T\| = \|T\|^2$ since $\|T^*\| = \|T\|$, which follows from the definition of the adjoint. For the other, $\|Tx\|^2 = \langle Tx, Tx\rangle = \langle x, T^*Tx\rangle \leq \|x\|^2\|T^*T\|$, so $\|T\|^2 \leq \|T^*T\|$. $\square$

**Definition.** A **$\mathrm{C}^*$-algebra** is a complex Banach algebra $A$ with an involution $a \mapsto a^*$ satisfying

$$
(ab)^* = b^*a^*, \qquad (a^*)^* = a, \qquad \|a^*a\| = \|a\|^2
$$

for all $a, b \in A$. A **$\mathrm{C}^*$-subalgebra** of $B(H)$ is a subalgebra closed in the norm and closed under the adjoint; it is a $\mathrm{C}^*$-algebra in its own right.

**Example.** $B(H)$ itself; the algebra $K(H)$ of compact operators on $H$, which is a $\mathrm{C}^*$-subalgebra without identity unless $H$ is finite-dimensional; $C_0(X)$ for a locally compact Hausdorff space $X$, with pointwise multiplication and complex conjugation, which is a commutative $\mathrm{C}^*$-algebra; and $\mathbb{M}_n(\mathbb{C})$ (*Matrix Algebras*), the finite-dimensional case.

**Definition.** An element $a$ of a $\mathrm{C}^*$-algebra is **self-adjoint** if $a^* = a$, **normal** if $a^*a = aa^*$, **unitary** if $a^*a = aa^* = 1$, and a **projection** if $a^* = a = a^2$. Every element has a unique decomposition $a = u + iv$ with $u, v$ self-adjoint,

$$
u = \tfrac{1}{2}(a + a^*), \qquad v = \tfrac{1}{2i}(a - a^*),
$$

so the self-adjoint elements span the algebra over $\mathbb{R}$; the involution is a real-linear anti-automorphism of order two.

**Theorem (spectral theorem for normal operators, standard).** A normal operator $T \in B(H)$ is unitarily equivalent to multiplication by a bounded measurable function on a direct sum of spaces $L^2(\mu)$, and a self-adjoint operator has a **projection-valued measure** $E$ on its spectrum with

$$
T = \int_{\sigma(T)} \lambda \, dE(\lambda).
$$

**Remark.** The spectral theorem is stated for reference; it is standard and is the source of the commutative examples below.

## The Gelfand–Naimark Theorems

The rigidity of $\mathrm{C}^*$-algebras begins with the fact that the abstract axioms already force a Hilbert-space representation.

**Theorem (Gelfand–Naimark).** Every $\mathrm{C}^*$-algebra $A$ is isometrically $*$-isomorphic to a $\mathrm{C}^*$-subalgebra of $B(H)$ for some Hilbert space $H$.

*Proof (sketch).* For each state $\omega$ on $A$ the GNS construction below produces a representation $\pi_\omega$ on a Hilbert space $H_\omega$; when $A$ has no identity the construction is applied to the unitisation of $A$, with states normalised by $\|\omega\| = 1$. Then

$$
\|a\| = \sup_{\omega \text{ a state}} \|\pi_\omega(a)\|
$$

for every $a \in A$; the direct sum of the representations $\pi_\omega$ over all states is therefore faithful and isometric. $\square$

**Theorem (commutative Gelfand–Naimark).** Every commutative $\mathrm{C}^*$-algebra $A$ is isometrically $*$-isomorphic to $C_0(X)$ for a locally compact Hausdorff space $X$, namely the space of characters of $A$ with the weak-$*$ topology; if $A$ has an identity, $X$ is compact and $A \cong C(X)$.

*Proof (sketch).* The characters form a locally compact space $X$ in the weak-$*$ topology, and the Gelfand transform $\hat a(\chi) = \chi(a)$ is a $*$-homomorphism $A \to C_0(X)$; for a $\mathrm{C}^*$-algebra the Gelfand transform is isometric, because $\|\hat a\|_\infty^2 = \|\widehat{a^*a}\|_\infty = \|a^*a\| = \|a\|^2$ by the $\mathrm{C}^*$-identity, and it is surjective by the Stone–Weierstrass theorem. $\square$

**Corollary (the norm is determined algebraically).** A $\mathrm{C}^*$-algebra carries at most one norm making it a $\mathrm{C}^*$-algebra, and every $*$-homomorphism from a $\mathrm{C}^*$-algebra to a $\mathrm{C}^*$-algebra is norm-decreasing, hence continuous.

*Proof.* If $\|\cdot\|_1, \|\cdot\|_2$ both satisfy the $\mathrm{C}^*$-identity, then the completion in one norm has the same spectral values for each self-adjoint element, and for self-adjoint $a$ the norm is the spectral radius, $\|a\| = \sup\{|\lambda| : \lambda \in \sigma(a)\}$; hence the two norms agree on self-adjoint elements and therefore on all elements, by the $\mathrm{C}^*$-identity applied to $a^*a$. For the second statement, a $*$-homomorphism $\pi$ sends self-adjoint elements to self-adjoint elements and $\sigma(\pi(a)) \subseteq \sigma(a)$, so $\|\pi(a)\|^2 = \|\pi(a^*a)\| = r(\pi(a^*a)) \leq r(a^*a) = \|a\|^2$. $\square$

This corollary is the sharpest contrast with the general Banach-algebra setting: a $\mathrm{C}^*$-algebra's analytic structure is entirely determined by its algebra and involution.

## The Gelfand–Naimark–Segal Construction

**Definition.** A **state** on a $\mathrm{C}^*$-algebra $A$ with identity is a linear functional $\omega : A \to \mathbb{C}$ that is **positive** ($\omega(a^*a) \geq 0$ for all $a$) and **normalised** ($\omega(1) = 1$); for a $\mathrm{C}^*$-algebra without identity the normalisation is replaced by $\|\omega\| = 1$, positivity being unchanged. A **representation** of $A$ on a Hilbert space $H$ is a $*$-homomorphism $\pi : A \to B(H)$; it is **cyclic** if some $x \in H$ satisfies $\overline{\pi(A)x} = H$.

**Theorem (GNS construction).** Let $\omega$ be a state on $A$. Then there exist a Hilbert space $H_\omega$, a representation $\pi_\omega : A \to B(H_\omega)$ and a cyclic unit vector $x_\omega \in H_\omega$ with

$$
\omega(a) = \langle \pi_\omega(a)x_\omega, x_\omega\rangle, \qquad a \in A .
$$

*Proof.* Consider the sesquilinear form on $A$ defined by $[a,b]_\omega = \omega(b^*a)$. From positivity, $\omega(a^*a) \geq 0$, and the Cauchy–Schwarz inequality $|\omega(b^*a)|^2 \leq \omega(a^*a)\,\omega(b^*b)$ for positive functionals gives that the form is positive semidefinite and vanishes exactly on the left ideal $N_\omega = \{a : \omega(a^*a) = 0\}$. The quotient $A/N_\omega$ is a pre-Hilbert space with inner product $[\,\cdot\, , \cdot\,]_\omega$; let $H_\omega$ be its completion. Define $\pi_\omega(a)$ on the image of $b$ by

$$
\pi_\omega(a)(b + N_\omega) = ab + N_\omega .
$$

This is well defined because $N_\omega$ is a left ideal, and it is bounded: for self-adjoint $a$, the estimate $[ab,ab]_\omega = \omega(b^*a^*ab) \leq \|a\|^2\,\omega(b^*b) = \|a\|^2[b,b]_\omega$ follows from the positivity of the functional $b \mapsto \omega(b^*(\|a\|^2 - a^*a)b)$ on the algebra with $\|a\|^2 - a^*a \geq 0$ in the self-adjoint part; the general case follows by applying this to $a^*a$. Hence $\pi_\omega(a)$ extends to a bounded operator on $H_\omega$, and it is a $*$-homomorphism because the involution and multiplication of $A$ act on the quotient as expected. The class $x_\omega = 1 + N_\omega$ is cyclic, and

$$
\langle\pi_\omega(a)x_\omega, x_\omega\rangle = [a, 1]_\omega = \omega(1^*a) = \omega(a) . \qquad \square
$$

**Corollary (states exist).** Every $\mathrm{C}^*$-algebra with identity has at least one state, hence a nontrivial representation, and the Gelfand–Naimark theorem follows.

## Functional Calculus and the Spectral Theory

**Theorem (continuous functional calculus).** Let $a$ be a normal element of a $\mathrm{C}^*$-algebra $A$ with identity. Then there is a unique isometric $*$-isomorphism

$$
C(\sigma(a)) \longrightarrow C^*(a, 1) \subseteq A, \qquad f \longmapsto f(a),
$$

from the continuous functions on the compact spectrum of $a$ onto the $\mathrm{C}^*$-subalgebra generated by $a$ and $1$.

*Proof.* The subalgebra $C^*(a,1)$ is generated by $a$ and $a^*$, which commute with one another because $a$ is normal, so it is commutative; by commutative Gelfand–Naimark it is $C(X)$ for its character space $X$, and $X$ is homeomorphic to $\sigma(a)$ by the identification of characters with spectral points. The inverse of the Gelfand transform is the required map. $\square$

**Corollary (the square root and the modulus).** Every positive element $a$ (that is, $a = b^*b$ for some $b$) has a unique positive square root; every element has a polar decomposition $a = u|a|$ with $|a| = (a^*a)^{1/2}$ and a partial isometry $u$.

**Theorem (order structure).** The relation $a \leq b$ defined by $b - a = c^*c$ for some $c$ is a partial order on the self-adjoint elements, compatible with addition and with multiplication by positive scalars; the self-adjoint part is a partially ordered real vector space, and $1$ is an order unit when $A$ has an identity.

## Ideals and Quotients

The ideal theory of $\mathrm{C}^*$-algebras is where the structural theory of *Ideals and Quotients of Algebras* meets the involution: quotients behave especially well.

**Theorem (closed ideals are self-adjoint).** Every closed two-sided ideal $I$ of a $\mathrm{C}^*$-algebra $A$ satisfies $I^* = I$. Consequently, the quotient $A/I$ is a $\mathrm{C}^*$-algebra with the quotient norm and the involution induced by that of $A$, and the quotient map is a $*$-homomorphism.

*Proof (sketch).* If $I$ is a closed two-sided ideal and $a \in I$, then $a^*a \in I$. Let $(u_\lambda)$ be an approximate identity for $I$, with $0 \leq u_\lambda \leq 1$ and $u_\lambda \in I$; then

$$
\|a(1-u_\lambda)\|^2 = \|(1-u_\lambda)a^*a(1-u_\lambda)\| \longrightarrow 0 ,
$$

so $au_\lambda \to a$ and hence $\|u_\lambda a^* - a^*\| = \|au_\lambda - a\| \to 0$. Since $u_\lambda a^* \in I$ and $I$ is closed, $a^* \in I$. The quotient is a Banach algebra with an involution; the $\mathrm{C}^*$-identity for the quotient norm is checked using the approximate units of $I$. $\square$

**Definition.** A $\mathrm{C}^*$-algebra is **simple** if it has no nontrivial closed two-sided ideals. The **Calkin algebra** is the quotient $B(H)/K(H)$.

**Example.** $K(H)$ is simple, and $B(H)/K(H)$ is a $\mathrm{C}^*$-algebra; this is the simplest construction of a $\mathrm{C}^*$-algebra that is presented as a quotient of one operator algebra by another. The finite-dimensional analogue is the quotient of $\mathbb{M}_n(\mathbb{C})$ by an ideal, and by the theory of *Ideals and Quotients of Algebras* the ideals of $\mathbb{M}_n(\mathbb{C})$ are trivial, so $\mathbb{M}_n(\mathbb{C})$ is simple.

**Proposition (the quotient is the algebra of the orthogonal complement).** Let $\mathcal{M} \subseteq B(H)$ be a $\mathrm{C}^*$-subalgebra and let $K \subseteq H$ be a closed subspace invariant under $\mathcal{M}$. Then the restriction map $T \mapsto T|_K$ is a $*$-homomorphism $\mathcal{M} \to B(K)$; if $K^\perp$ is invariant as well, so that $K$ is reducing, the restriction is the quotient of $\mathcal{M}$ by the ideal of operators of $\mathcal{M}$ that vanish on $K$.

*Proof.* Invariance of $K$ under each $T \in \mathcal{M}$ implies invariance under $T^*$ when $\mathcal{M}$ is self-adjoint and $K$ is reducing; then $T|_K$ is bounded with $\|T|_K\| \leq \|T\|$, and $(T|_K)^* = T^*|_K$. The kernel is a closed two-sided ideal, and the induced map on the quotient is injective with dense image, hence an isomorphism onto its image. $\square$

## Von Neumann Algebras

The norm topology is not the only relevant one; operators act pointwise, and the topology of pointwise convergence produces algebras closed under stronger operations.

**Definition.** The **strong operator topology** on $B(H)$ is the topology of pointwise convergence on vectors, $T \mapsto Tx$; the **weak operator topology** is the topology of pointwise convergence of the matrix entries $T \mapsto \langle Tx, y\rangle$. A **von Neumann algebra** is a $*$-subalgebra $\mathcal{M} \subseteq B(H)$ containing $1$ and closed in the weak operator topology. The **commutant** of a set $S \subseteq B(H)$ is

$$
S' = \{T \in B(H) : TS = ST \text{ for all } S \in S\}.
$$

**Theorem (von Neumann bicommutant theorem).** A $*$-subalgebra $\mathcal{M} \subseteq B(H)$ containing $1$ is a von Neumann algebra if and only if $\mathcal{M} = \mathcal{M}''$.

*Proof (sketch).* The inclusion $\mathcal{M} \subseteq \mathcal{M}''$ is immediate. For the converse one shows that the weak operator closure of $\mathcal{M}$ equals $\mathcal{M}''$: a vector $\xi \in H$ and an operator $T \in \mathcal{M}''$ are compared by applying the double commutant to the closure of $\mathcal{M}\xi$, which is $\mathcal{M}''\xi$; the strong closure of $\mathcal{M}$ contains every operator in $\mathcal{M}''$ by a Kaplansky density argument together with the fact that the unit ball is compact in the weak operator topology. $\square$

**Proposition (the centre and the decomposition).** The centre of a von Neumann algebra $\mathcal{M}$ is $Z(\mathcal{M}) = \mathcal{M} \cap \mathcal{M}'$, and it is a commutative von Neumann algebra; hence $Z(\mathcal{M}) \cong C(X)$ for a compact hyperstonean space $X$, and $\mathcal{M}$ decomposes as a direct integral of **factors**, von Neumann algebras with trivial centre.

*Proof.* $\mathcal{M} \cap \mathcal{M}'$ is commutative because each element commutes with the other by definition; it is a von Neumann algebra and is commutative, so the commutative Gelfand–Naimark theorem applies, and the spectral decomposition of the centre gives the direct-integral decomposition. $\square$

## Traces, the Trace Class and the Hilbert–Schmidt Class

On $B(H)$ the algebra has a distinguished functional, and the ideals it defines are the finite-rank ideals of the operator theory.

**Definition.** For $T \in B(H)$ the **absolute value** is $|T| = (T^*T)^{1/2}$, and the **singular values** $s_1 \geq s_2 \geq \dots \geq 0$ are the eigenvalues of $|T|$ counted with multiplicity. Then

$$
L^1(H) = \{T : \mathrm{Tr}|T| = \textstyle\sum_n s_n < \infty\}, \qquad L^2(H) = \{T : \mathrm{Tr}(T^*T) = \textstyle\sum_n s_n^2 < \infty\}
$$

are the **trace class** and the **Hilbert–Schmidt class**, and on the trace class the **trace** is

$$
\mathrm{Tr}\,T = \sum_n \langle T e_n, e_n\rangle,
$$

the sum being absolutely convergent and independent of the orthonormal basis $(e_n)$.

**Proposition (the chain of ideals).** One has the inclusions

$$
L^1(H) \subseteq L^2(H) \subseteq K(H) \subseteq B(H),
$$

$L^1(H)$ and $L^2(H)$ are two-sided $*$-ideals, $L^2(H)$ is dense in $K(H)$ in the norm of $B(H)$, and

1. $\langle S, T\rangle_2 = \mathrm{Tr}(T^*S)$ is an inner product making $L^2(H)$ a Hilbert space, the **Hilbert–Schmidt space**, with $\|T\| \leq \|T\|_2 = (\mathrm{Tr}\,T^*T)^{1/2}$;
2. $\mathrm{Tr}(ST) = \mathrm{Tr}(TS)$ whenever $S \in L^1(H)$ and $T \in B(H)$, and $\mathrm{Tr}$ is the unique normal tracial weight on $B(H)$ up to scaling;
3. the pairing $(S,T) \mapsto \mathrm{Tr}(ST)$ identifies $L^1(H)$ with the dual of $K(H)$, and $B(H)$ with the dual of $L^1(H)$.

*Proof.* The first two statements are the standard theory of the Schatten classes: $|ST| \leq \|S\|\,|T|$ gives the ideal property, the Schmidt decomposition of a Hilbert–Schmidt operator gives the inner product and the norm inequality, and the trace identity follows from the absolute convergence of the series by a rearrangement. The duality statements are the standard duality of the Schatten classes; the second identification is the one that exhibits the weak operator topology as the $\sigma(B(H), L^1(H))$-topology on bounded sets. $\square$

**Example (the finite-dimensional case).** For $H = \mathbb{C}^n$ all classes coincide with $B(H) = M_n(\mathbb{C})$, the trace is the matrix trace and $\tau = \mathrm{Tr}/n$ is the unique **tracial state**, $\tau(1) = 1$. For a general von Neumann algebra $\mathcal{M}$ a **trace** is a map $\tau : \mathcal{M}_+ \to [0,\infty]$ that is additive, positively homogeneous and unitarily invariant; it is **faithful** if $\tau(x^*x) = 0$ forces $x = 0$, **finite** if $\tau(1) < \infty$, **semifinite** if every nonzero positive element dominates a positive element of finite trace, and a **tracial state** if $\tau(1) = 1$. The existence of a faithful normal tracial weight is the dividing line between the types of the next section, and the trace class is the model: $\mathrm{Tr}$ on $B(H)$ is faithful, normal and semifinite, but not finite when $H$ is infinite-dimensional.

## Factors and the Classification into Types

**Definition.** A **factor** is a von Neumann algebra with centre $Z(\mathcal{M}) = \mathcal{M} \cap \mathcal{M}' = \mathbb{C}1$. The centre of a general von Neumann algebra is commutative and hence of the form $L^\infty(X)$ for a measure space $X$, and the spectral decomposition of the centre presents $\mathcal{M}$ as a direct integral of factors, $\int_X^\oplus \mathcal{M}(x)\,dx$.

**Definition (equivalence of projections).** For projections $p, q \in \mathcal{M}$ write $p \sim q$ if there is a partial isometry $v \in \mathcal{M}$ with $v^*v = p$ and $vv^* = q$ (**Murray–von Neumann equivalence**), and $p \preceq q$ if $p \sim p'$ for some projection $p' \leq q$. The relation $\preceq$ is a partial order on equivalence classes and $\sim$ is an equivalence relation.

**Theorem (classification of factors).** Every factor is of exactly one of the following types.

- **Type I.** $\mathcal{M}$ contains a minimal projection; a factor of type I is isomorphic to $B(H)$ for some Hilbert space $H$, it is of type $\mathrm{I}_n$ when $H$ has dimension $n$ and of type $\mathrm{I}_\infty$ otherwise. The finite-dimensional examples are $M_n(\mathbb{C})$; the model of type $\mathrm{I}_\infty$ is $B(\ell^2)$.
- **Type II.** $\mathcal{M}$ has no minimal projection but carries a faithful normal tracial weight, unique up to scaling. It is of type $\mathrm{II}_1$ when the weight is finite — then $\mathcal{M}$ has a unique tracial state $\tau$ — and of type $\mathrm{II}_\infty$ when it is properly infinite.
- **Type III.** $\mathcal{M}$ has no faithful normal semifinite trace. Every nonzero projection is then properly infinite, and the type is refined into $\mathrm{III}_\lambda$, $\lambda \in [0,1]$, by the flow of weights.

**Example (types $\mathrm{I}$ and $\mathrm{II}_1$).** $B(H)$ is a factor of type I, the finite-dimensional $M_n(\mathbb{C})$ being of type $\mathrm{I}_n$; the group von Neumann algebra $L(G)$ of a discrete group $G$ in which every nontrivial conjugacy class is infinite (an **icc** group) is a factor of type $\mathrm{II}_1$, with unique tracial state $\tau(a) = \langle a\delta_e,\delta_e\rangle$ and no minimal projections. The tensor product $B(H)\bar\otimes R$ of $B(H)$ with a type $\mathrm{II}_1$ factor $R$ is a factor of type $\mathrm{II}_\infty$, and crossed products of a type $\mathrm{II}_\infty$ factor by ergodic non-measure-preserving actions give the Powers factors of type $\mathrm{III}_\lambda$.

*Proof (outline).* Murray–von Neumann's comparison theorem shows that the projections of a factor are totally ordered by $\preceq$, so a factor is finite exactly when no proper projection is equivalent to $1$; finiteness is equivalent to the existence of a faithful normal tracial weight. If a minimal projection exists, $\mathcal{M}$ is isomorphic to the algebra of all bounded operators on its range, which gives type I. If there is no minimal projection and a finite trace exists, the trace is a faithful normal tracial state and the factor is of type $\mathrm{II}_1$; if the trace is only semifinite, the type is $\mathrm{II}_\infty$. If no faithful normal semifinite trace exists, the factor is of type III; the refinement of the type into $\mathrm{III}_\lambda$ uses the modular theory of the next section, $\lambda$ being the invariant read off the crossed product of $\mathcal{M}$ by its modular group. This is the classification of Murray and von Neumann with the refinement of Connes; the details are a substantial theory and are cited rather than reproduced. $\square$

## The Modular Theory of Tomita–Takesaki

A type III factor has no trace, so the theory above has no invariant to offer; the replacement is a canonical one-parameter group of automorphisms attached to each faithful normal state, and the replacement is exact enough to classify.

**Setting.** Let $\mathcal{M} \subseteq B(H)$ be a von Neumann algebra and let $\omega$ be a **faithful normal state** on $\mathcal{M}$, realised by a vector: $\omega(a) = \langle a\Omega, \Omega\rangle$ for a vector $\Omega \in H$ that is **cyclic** ($\overline{\mathcal{M}\Omega} = H$) and **separating** ($a\Omega = 0$ implies $a = 0$) for $\mathcal{M}$. The GNS construction provides such a realisation: take $H_\omega$ and $\Omega = x_\omega$, which is cyclic by construction and separating by faithfulness, and the pair $(\mathcal{M}, \Omega)$ is the **standard form** of $\omega$.

**Definition (the Tomita operator).** Define an unbounded operator on the dense subspace $\mathcal{M}\Omega$ by

$$
S_0(a\Omega) = a^*\Omega, \qquad a \in \mathcal{M}.
$$

Then $S_0$ is closable; let $S$ be its closure and $S = J\Delta_\omega^{1/2}$ its polar decomposition. Then $\Delta_\omega = S^*S$ is positive, self-adjoint and injective, the **modular operator** of $\omega$, and $J$ is a conjugate-linear isometry with $J^2 = 1$, the **modular conjugation**.

**Theorem (Tomita–Takesaki).** With the notation above,

$$
\Delta_\omega^{it}\mathcal{M}\Delta_\omega^{-it} = \mathcal{M} \quad (t \in \mathbb{R}), \qquad J\mathcal{M}J = \mathcal{M}' .
$$

Hence $\varsigma_t^\omega(a) = \Delta_\omega^{it}a\Delta_\omega^{-it}$ is a one-parameter group of $*$-automorphisms of $\mathcal{M}$, the **modular automorphism group** (or **modular flow**) of $\omega$, and $j(a) = JaJ$ is a $*$-anti-isomorphism of $\mathcal{M}$ onto the commutant $\mathcal{M}'$.

*Proof (sketch).* Cyclicity makes $S_0$ densely defined and faithfulness makes it well defined, and $S_0$ is closable. From the definitions one checks the fundamental relation

$$
Sx = x^*S \qquad (x \in \mathcal{M}'),
$$

which after taking adjoints gives $S^*x = x^*S^*$ and hence

$$
\Delta_\omega x = x\Delta_\omega \qquad (x \in \mathcal{M}') :
$$

the modular operator commutes with the commutant. The polar decomposition $S = J\Delta_\omega^{1/2}$ and the standard identity $J\Delta_\omega^{1/2}J = \Delta_\omega^{-1/2}$, equivalently $S = \Delta_\omega^{-1/2}J$, then give $J\mathcal{M}J \subseteq \mathcal{M}'$ by a computation on the dense set $\mathcal{M}\Omega$; the same argument with $\mathcal{M}$ and $\mathcal{M}'$ interchanged gives $J\mathcal{M}'J \subseteq \mathcal{M}$, and since $J^2 = 1$ both inclusions are equalities, which is the second assertion. For the first, take $a \in \mathcal{M}$ and use $J\Delta_\omega^{it}J = \Delta_\omega^{-it}$, the $it$-power of $J\Delta_\omega^{1/2}J = \Delta_\omega^{-1/2}$:

$$
J\bigl(\Delta_\omega^{it}a\Delta_\omega^{-it}\bigr)J = \Delta_\omega^{-it}(JaJ)\Delta_\omega^{it} = JaJ,
$$

the second equality because $JaJ \in \mathcal{M}'$ commutes with $\Delta_\omega^{it}$ by the relation above. Hence $JaJ \in \mathcal{M}'$ implies $\Delta_\omega^{it}a\Delta_\omega^{-it} \in J\mathcal{M}'J = \mathcal{M}$, and applying the same argument with $-t$ gives the reverse inclusion. $\square$

**Remark (notation).** The modular group is written $\varsigma_t^\omega$ and not $\sigma_t^\omega$: the letter $\sigma$ denotes the spectrum $\sigma(a)$ of an element in this article and the symbol $\sigma(\xi)$ of the Cauchy–Riemann operator, and the three uses are kept apart deliberately. Likewise $\Delta_\omega$ here is the modular operator of Tomita–Takesaki theory, not the Laplacian and its companions; the two are unrelated operators and appear in different articles.

**Theorem (the KMS condition).** The modular group of $\omega$ is determined by the following property: for all $a, b \in \mathcal{M}$ there is a function $F_{a,b}$ bounded and continuous on the closed strip $0 \leq \mathrm{Im}\,z \leq 1$ and holomorphic on its interior such that

$$
F_{a,b}(t) = \omega\bigl(\varsigma_t^\omega(a)\,b\bigr), \qquad F_{a,b}(t+i) = \omega\bigl(b\,\varsigma_t^\omega(a)\bigr), \qquad t \in \mathbb{R} .
$$

A state with this property is called a **KMS state** (at $\beta = 1$); for a parameter $\beta > 0$ the **$\beta$-KMS condition** replaces $i$ by $i\beta$, and the two conditions are interchanged by rescaling the group. The modular group is the unique one for which $\omega$ is KMS.

**Corollary (the modular generator).** The logarithm $\log\Delta_\omega$ is an unbounded self-adjoint operator, and the modular flow is the conjugation by the unitary group it generates:

$$
\varsigma_t^\omega(a) = e^{it\log\Delta_\omega}\,a\,e^{-it\log\Delta_\omega}.
$$

The operator $\log\Delta_\omega$ is the **modular generator** of $\omega$, and the pair $(\mathcal{M}, \varsigma^\omega)$ is the **non-commutative flow of weights** of $\mathcal{M}$.

**Theorem (Connes cocycle, standard).** For two faithful normal states $\omega, \omega'$ on $\mathcal{M}$ there is a strongly continuous family of unitaries $(D\omega' : D\omega)_t \in \mathcal{M}$, the **Connes cocycle**, with

$$
\varsigma_t^{\omega'}(a) = (D\omega' : D\omega)_t\,\varsigma_t^\omega(a)\,(D\omega' : D\omega)_t^{*}, \qquad a \in \mathcal{M} .
$$

Consequently the modular group depends on the state only up to an inner perturbation, only its image in $\operatorname{Out}(\mathcal{M}) = \operatorname{Aut}(\mathcal{M})/\operatorname{Inn}(\mathcal{M})$ being independent of the state, and

$$
T(\mathcal{M}) = \{t \in \mathbb{R} : \varsigma_t^\omega \in \operatorname{Inn}(\mathcal{M})\}
$$

is a subgroup of $\mathbb{R}$ independent of $\omega$; it is the **Connes invariant** $T(\mathcal{M})$ of $\mathcal{M}$.

**Theorem (the finite-dimensional case).** Let $\mathcal{M} = M_n(\mathbb{C}) \subseteq B(L^2(\mathcal{M}))$ act on the Hilbert–Schmidt space $L^2(\mathcal{M}) = M_n(\mathbb{C})$ with $\langle A, B\rangle = \mathrm{Tr}(B^*A)$, let $\rho$ be a positive definite density matrix with $\mathrm{Tr}\,\rho = 1$, and let $\omega(a) = \mathrm{Tr}(\rho a)$ with $\Omega = \rho^{1/2}$. Then $\Omega$ is cyclic and separating, and

$$
\Delta_\omega = L_\rho R_\rho^{-1}, \qquad \Delta_\omega^{it}a = \rho^{it}a\rho^{-it}, \qquad J(a) = a^*, \qquad \log\Delta_\omega = \log\rho \otimes 1 - 1\otimes \log\rho,
$$

where $L_\rho, R_\rho$ are left and right multiplication; the modular group is $\varsigma_t(a) = \rho^{it}a\rho^{-it}$.

*Proof.* Since $\rho^{1/2}$ is invertible, $a\rho^{1/2} = 0$ forces $a = 0$ (separating) and $M_n(\mathbb{C})\rho^{1/2} = M_n(\mathbb{C})$ is dense (cyclic). On $\mathcal{M}\Omega = \mathcal{M}\rho^{1/2}$ the Tomita operator acts as $S(a\rho^{1/2}) = a^*\rho^{1/2}$, and

$$
J\Delta_\omega^{1/2}\bigl(a\rho^{1/2}\bigr) = J\bigl(\rho^{1/2}a\rho^{-1/2}\rho^{1/2}\bigr) = J\bigl(\rho^{1/2}a\bigr) = \bigl(\rho^{1/2}a\bigr)^* = a^*\rho^{1/2},
$$

so $S = J\Delta_\omega^{1/2}$ with $\Delta_\omega^{1/2}(a\rho^{1/2}) = \rho^{1/2}a$, that is $\Delta_\omega^{1/2}(a\Omega) = \rho^{1/2}a\Omega$, and hence $\Delta_\omega^{it}a\Omega = \rho^{it}a\rho^{-it}\Omega$: the modular operator is conjugation by $\rho^{it}$ on the left and by $\rho^{-it}$ on the right, $\Delta_\omega = L_\rho R_\rho^{-1}$. Taking logarithms, $\log\Delta_\omega = L_{\log\rho} - R_{\log\rho}$. $\square$

**Verification of the KMS condition.** Define, for $a, b \in M_n(\mathbb{C})$ and $z \in \mathbb{C}$,

$$
F(z) = \mathrm{Tr}\bigl(\rho^{1+iz}\,a\,\rho^{-iz}\,b\bigr) = \mathrm{Tr}\bigl(\rho\,\varsigma_z(a)\,b\bigr), \qquad \varsigma_z(a) = \rho^{iz}a\rho^{-iz},
$$

an entire function of $z$ because $z \mapsto \rho^{iz}$ is entire and matrix multiplication and the trace are polynomial. At $z = t$ real, $F(t) = \omega(\varsigma_t(a)b)$. At $z = t+i$ one has $\rho^{1+i(t+i)} = \rho^{it}\rho^{-1}\rho = \rho^{it}$ and $\rho^{-i(t+i)} = \rho^{1-it} = \rho\rho^{-it}$, so

$$
F(t+i) = \mathrm{Tr}\bigl(\rho^{it}a\rho^{-it}\rho b\bigr) = \mathrm{Tr}\bigl(\rho b\rho^{it}a\rho^{-it}\bigr) = \omega\bigl(b\,\varsigma_t(a)\bigr),
$$

the middle equality being the cyclicity of the trace. This is the KMS condition at $\beta = 1$.

**Corollary (traces and the trivial modular flow).** If $\rho = 1/n$, so that $\omega$ is the tracial state, then $\Delta_\omega = 1$, $H = 0$ and the modular flow is trivial; and the computation above with $\rho = 1/n$ gives $F(t+i\beta) = \omega(ba)$ for every $\beta$, so a tracial state is $\beta$-KMS for every $\beta$. At the other extreme, a factor $\mathcal{M}$ is semifinite (type I or II) if and only if its modular group is inner for every $t$, that is $T(\mathcal{M}) = \mathbb{R}$, and it is of type III exactly when $T(\mathcal{M}) \neq \mathbb{R}$: for a type $\mathrm{III}_1$ factor the modular group is outer at every $t \neq 0$, while a type $\mathrm{III}_\lambda$ factor with $0 < \lambda < 1$ has inner modular automorphisms at the nonzero times in $(2\pi/\lvert\log\lambda\rvert)\mathbb{Z}$. It is in this sense that the modular flow replaces the trace for a type III factor. The finite-dimensional computation is the whole theory in miniature: on $M_n(\mathbb{C})$ the modular operator is explicit, the modular flow is conjugation by $\rho^{it}$, and every question reduces to linear algebra on $n \times n$ matrices.

## Derivations of Operator Algebras

**Definition.** A **derivation** of an algebra $A$ is a linear map $\delta : A \to A$ with

$$
\delta(ab) = \delta(a)\,b + a\,\delta(b), \qquad a, b \in A,
$$

as in *Automorphisms and Derivations of Algebras*. The derivations of $A$ form a Lie algebra under the commutator, and the inner derivations $\operatorname{ad}_h(a) = ha - ah$ form a Lie ideal.

**Theorem (automatic continuity, standard).** Every derivation of a $\mathrm{C}^*$-algebra is bounded, and hence continuous.

*Proof.* This is the Kadison–Sakai theorem; the argument first shows the continuity of derivations on the self-adjoint part, using the order structure and the functional calculus, and then extends to the whole algebra by linearity over $\mathbb{C}$. $\square$

**Theorem (innerness, standard).** Every derivation of a von Neumann algebra $\mathcal{M}$ is inner: for each $\delta$ there is $h \in \mathcal{M}$ with $\delta(a) = [h, a]$ for all $a \in \mathcal{M}$. Consequently every derivation of $\mathbb{M}_n(\mathbb{C})$ and of $B(H)$ is inner.

*Proof (sketch).* For the weakly closed case, take a family of mutually orthogonal projections summing to $1$ and define $h$ by the off-diagonal blocks $\delta(p)\,q$ for projections $p, q$; the commutation relations force $h$ to commute with every element of the commutant, so $h \in \mathcal{M}'' = \mathcal{M}$, and the identity $\delta(a) = [h,a]$ is then checked on a generating set. $\square$

**Corollary (vanishing of the outer derivations).** For a von Neumann algebra the outer derivation space $\operatorname{Der}(\mathcal{M})/\operatorname{Inn}(\mathcal{M})$ vanishes; for a general Banach or associative algebra it need not, as the examples of *Automorphisms and Derivations of Algebras* show.

The rigidity of the operator-algebra setting is thus twofold: the derivations are automatically bounded, and on a weakly closed algebra they are automatically inner.

## Examples from Matrix and Group Algebras

**Example (matrix algebras).** $\mathbb{M}_n(\mathbb{C})$ is a finite-dimensional $\mathrm{C}^*$-algebra, hence a von Neumann algebra on $\mathbb{C}^n$; it is simple, it is a factor of type I, and its unique trace is the normalised matrix trace. It is the model for the finite-dimensional theory in *Matrix Algebras*.

**Example (group algebras).** Let $G$ be a discrete group and $\ell^2(G)$ its Hilbert space of square-summable functions. The **left regular representation** $\lambda : G \to B(\ell^2(G))$ extends to an isometric representation of the group algebra $\mathbb{C}[G]$; its norm closure is the **reduced group $\mathrm{C}^*$-algebra** $C^*_r(G)$, and its weak closure is the **group von Neumann algebra** $L(G)$. The group von Neumann algebra is finite, with faithful trace $\tau(a) = \langle a\delta_e, \delta_e\rangle$, and it is a factor exactly when every nontrivial conjugacy class of $G$ is infinite. These objects are the operator-algebraic completions of the algebraic group algebras of *Group Algebras*.

**Example (commutative algebras).** $C(X)$ for a compact Hausdorff space $X$, with the sup norm and complex conjugation, is the commutative case, and its self-adjoint elements are the real-valued functions. The functional calculus of this algebra is the ordinary functional calculus of operators.

**Example (the Toeplitz algebra).** The $\mathrm{C}^*$-algebra generated by the unilateral shift on $\ell^2(\mathbb{N})$ and its adjoint is the **Toeplitz algebra**; it contains $K(\ell^2(\mathbb{N}))$ as its unique nontrivial closed ideal, and its quotient is $C(\mathbb{T})$. It is the standard example in which the extension theory of operator algebras is visible in a single algebra.

## Summary

A **$\mathrm{C}^*$-algebra** is a complex Banach algebra with an involution satisfying $(ab)^*=b^*a^*$, $(a^*)^*=a$ and the **$\mathrm{C}^*$-identity** $\|a^*a\|=\|a\|^2$; the model is $B(H)$ with the operator norm and the adjoint, where the identity holds and where the spectral theorem governs the normal elements. The **Gelfand–Naimark theorem** realises every abstract $\mathrm{C}^*$-algebra isometrically as a $\mathrm{C}^*$-subalgebra of some $B(H)$, through the **GNS construction** that builds a representation $\pi_\omega$ and a cyclic vector $x_\omega$ from a **state** $\omega$ by completing $A/N_\omega$; the **commutative Gelfand–Naimark theorem** identifies the commutative ones with $C_0(X)$. A $\mathrm{C}^*$-algebra has at most one $\mathrm{C}^*$-norm, and every $*$-homomorphism of $\mathrm{C}^*$-algebras is contractive. The **continuous functional calculus** turns a normal element $a$ into an isometric $*$-isomorphism $C(\sigma(a)) \to C^*(a,1)$, supplying square roots, moduli and polar decomposition.

Closed two-sided ideals of a $\mathrm{C}^*$-algebra are self-adjoint, quotients are again $\mathrm{C}^*$-algebras, and the finite-dimensional algebra $\mathbb{M}_n(\mathbb{C})$ is simple, while $K(H)$ is simple with **Calkin algebra** $B(H)/K(H)$ as quotient. **Von Neumann algebras** are the weakly closed $*$-subalgebras containing $1$; the **bicommutant theorem** characterises them by $\mathcal{M} = \mathcal{M}''$, the centre is $Z(\mathcal{M}) = \mathcal{M} \cap \mathcal{M}'$ and decomposes $\mathcal{M}$ as a direct integral of **factors**, classified into types I, II and III. **Derivations** of a $\mathrm{C}^*$-algebra are automatically bounded, and every derivation of a von Neumann algebra is inner, $\delta = \operatorname{ad}_h$ for some $h$; the outer derivation space $\operatorname{Der}(\mathcal{M})/\operatorname{Inn}(\mathcal{M})$ of a von Neumann algebra therefore vanishes. Matrix algebras, the reduced group $\mathrm{C}^*$-algebra $C^*_r(G)$ and group von Neumann algebra $L(G)$, the commutative algebras $C(X)$ and the Toeplitz algebra illustrate the theory.

The finite-rank ideals of $B(H)$ are the **trace class** $L^1(H)$ and the **Hilbert–Schmidt class** $L^2(H)$, with $L^1(H) \subseteq L^2(H) \subseteq K(H)$, the trace $\mathrm{Tr}\,T = \sum_n\langle Te_n,e_n\rangle$ independent of the basis, $\mathrm{Tr}(ST) = \mathrm{Tr}(TS)$, and the dualities $K(H)^* \cong L^1(H)$, $L^1(H)^* \cong B(H)$. A **factor** is a von Neumann algebra with centre $\mathbb{C}1$, and the classification runs by the structure of its projections: type I, isomorphic to $B(H)$, with the minimal projection present; type II, no minimal projection but a faithful normal tracial weight, unique up to scaling, of type $\mathrm{II}_1$ when the trace is finite and $\mathrm{II}_\infty$ otherwise; type III, admitting no faithful normal semifinite trace, refined into $\mathrm{III}_\lambda$. In place of the missing trace, a **faithful normal state** $\omega$ realised by a cyclic and separating vector $\Omega$ has a **modular operator** $\Delta_\omega$ and **modular conjugation** $J$ through the polar decomposition $S = J\Delta_\omega^{1/2}$ of the Tomita operator $S(a\Omega) = a^*\Omega$, and the **Tomita–Takesaki theorem** gives $\Delta_\omega^{it}\mathcal{M}\Delta_\omega^{-it} = \mathcal{M}$ and $J\mathcal{M}J = \mathcal{M}'$. The resulting **modular automorphism group** $\varsigma_t^\omega = \operatorname{Ad}\Delta_\omega^{it}$ is characterised by the **KMS condition** at $\beta = 1$, different states give groups differing by the **Connes cocycle**, and on $M_n(\mathbb{C})$ the theory is explicit: for $\omega(a) = \mathrm{Tr}(\rho a)$ one has $\Delta_\omega = L_\rho R_\rho^{-1}$, $J(a) = a^*$ and $\varsigma_t(a) = \rho^{it}a\rho^{-it}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | Complex Hilbert space |
| $B(H)$ | Bounded operators on $H$, with operator norm and adjoint |
| $K(H)$ | Compact operators on $H$ |
| $T^*$ | Adjoint of $T$ |
| $\|T\| = \sup_{\|x\|\leq1}\|Tx\|$ | Operator norm |
| $A$ | A $\mathrm{C}^*$-algebra |
| $a^*$ | Involution, with $\|a^*a\| = \|a\|^2$ |
| $\sigma(a)$ | Spectrum of $a$ |
| $\omega$ | State, positive and normalised linear functional |
| $(\pi_\omega, H_\omega, x_\omega)$ | GNS triple of a state |
| $C^*(a,1)$ | $\mathrm{C}^*$-subalgebra generated by $a$ and $1$ |
| $a \leq b$ | Order on self-adjoint elements, $b-a = c^*c$ |
| $I \trianglelefteq A$ | Closed two-sided ideal, automatically self-adjoint |
| $B(H)/K(H)$ | Calkin algebra |
| $\mathcal{M}$ | Von Neumann algebra, a weakly closed $*$-subalgebra of $B(H)$ containing $1$ |
| $\mathcal{M}'$ | Commutant of $\mathcal{M}$ |
| $Z(\mathcal{M}) = \mathcal{M}\cap \mathcal{M}'$ | Centre of a von Neumann algebra |
| $C^*_r(G)$, $L(G)$ | Reduced group $\mathrm{C}^*$-algebra and group von Neumann algebra |
| $\delta$ | Derivation, $\delta(ab) = \delta(a)b + a\delta(b)$ |
| $\operatorname{ad}_h(a) = [h,a]$ | Inner derivation |
| $\operatorname{Der}(\mathcal{M})$, $\operatorname{Inn}(\mathcal{M})$ | Derivations and inner derivations of $\mathcal{M}$ |
| $L^1(H)$, $L^2(H)$ | Trace class and Hilbert–Schmidt class |
| $\mathrm{Tr}$ | Trace, $\mathrm{Tr}\,T = \sum_n\langle Te_n,e_n\rangle$ |
| $\tau$ | Tracial weight, or tracial state when $\tau(1) = 1$ |
| $p \sim q$, $p \preceq q$ | Murray–von Neumann equivalence and subordination of projections |
| $S$ | Tomita operator, $S(a\Omega) = a^*\Omega$ |
| $\Delta_\omega = S^*S$, $J$ | Modular operator and modular conjugation, $S = J\Delta_\omega^{1/2}$ |
| $\varsigma_t^\omega = \operatorname{Ad}\Delta_\omega^{it}$ | Modular automorphism group of $\omega$ |
| $\log\Delta_\omega$ | Modular generator |
| $(D\omega' : D\omega)_t$ | Connes cocycle |
| $\rho$, $\Omega = \rho^{1/2}$ | Density matrix and standard vector in the finite-dimensional case |



## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras* (Academic Press, 1983), for the general theory of $\mathrm{C}^*$- and von Neumann algebras.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for Gelfand–Naimark, states and the GNS construction.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the bicommutant theorem, factors and the classification.
- Gerard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for a concise treatment of ideals, quotients and the functional calculus.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the direct-integral decomposition and the general theory of von Neumann algebras.
- Masamichi Takesaki, *Theory of Operator Algebras II* (Springer, 2003), for the Tomita–Takesaki modular theory, the KMS condition and the structure of factors.
- Alain Connes, *Noncommutative Geometry* (Academic Press, 1994), for the Connes cocycle, the invariant $T(\mathcal{M})$ and the classification of type III factors.
- Barry Simon, *Trace Ideals and Their Applications* (AMS, 2nd ed. 2005), for the trace class, the Hilbert–Schmidt class and the Schatten norms.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the spectral theorem and the elementary Hilbert-space background.
