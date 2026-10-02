# __Bounded Operators on a Hilbert Space__

## Introduction

The bounded linear operators of a Hilbert space $H$ form the object on which the whole of the present category is built. They carry three structures at once: they are a Banach algebra under composition and the operator norm, a $C^*$-algebra under the adjoint, and a topological space under three natural topologies — the norm topology, the strong operator topology and the weak operator topology. This article fixes the three structures and the passage between them. It is the operator-theoretic opening of the category: the later articles of the group treat the compact ideal, the spectral operator, the Banach-space analogue and the one-sided and two-sided multiplications, each of them an addition to the algebra defined here.

The algebra $B(H)$ is introduced only as far as the later articles need it. The norm, completeness and the operator norm are recalled from *Banach and Hilbert Spaces*; the adjoint is recalled from the same article, where it is constructed through the Riesz representation theorem, and is used here for its consequences — the $C^*$-identity, the lattice of projections and the partial isometries. The spectral theorem is *Self-Adjoint Operators and the Spectral Theorem* below; the compact and Schatten ideals are *Compact Operators*; the algebra of operators with its predual and the weak topology of the predual are *Operator Algebras* (Part II); the Hilbert–Schmidt and trace-class pairings used to describe the weak operator topology are *Compact Operators*; the module-theoretic reading of the same operators is *Modules over a Ring* (Part I). Nothing below is unbounded, and no measure theory beyond the $L^2$ examples of *Banach and Hilbert Spaces* is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ and $H$ is a Hilbert space over $\mathbb{K}$ with inner product $\langle\cdot,\cdot\rangle$ linear in the first argument and conjugate-linear in the second. The set of bounded linear maps $H\to H$ is $B(H)$; the operator norm is $\|T\|=\sup_{\|x\|\le1}\|Tx\|$; the adjoint is $T^*$ with $\langle Tx,y\rangle=\langle x,T^*y\rangle$; the identity is $I$, and the finite-rank operators are written $F(H)$.

## The Algebra of Bounded Operators

**Definition.** The **algebra of bounded operators** on $H$ is $B(H)$, the set of bounded linear maps $H\to H$ with the pointwise vector-space operations, the composition product and the operator norm.

**Proposition (a unital Banach algebra).** $B(H)$ is a complex (or real) associative algebra with unit $I$, and it is complete for the operator norm, which is submultiplicative, $\|ST\|\le\|S\|\,\|T\|$ and $\|I\|=1$. So $B(H)$ is a unital Banach algebra.

*Proof.* The vector-space and algebra axioms are inherited from the pointwise operations on maps. Completeness is that of the operator norm: a Cauchy sequence in norm converges pointwise on a dense set and the limit is bounded with the limiting norm. Submultiplicativity and $\|I\|=1$ are immediate from the supremum definition.

**Proposition (properness in infinite dimension).** When $H$ is infinite-dimensional, $B(H)$ is not commutative and is not finite-dimensional; it contains operators that are injective without being surjective, and isometries that are not unitary.

*Proof.* The unilateral shift $S$ on $\ell^2$ with $S e_n=e_{n+1}$ is an isometry, $S^*S=I$, with $S S^*\neq I$ the projection onto the span of $e_1,e_2,\dots$; so $B(H)$ contains a proper isometry and the two-sided properties differ. A commutant example such as the diagonal operators against the shift exhibits non-commutativity.

## The Involution and the C\*-Identity

**Definition.** The **adjoint** of $T\in B(H)$ is the unique operator $T^*$ with

$$
\langle Tx,y\rangle=\langle x,T^*y\rangle \qquad (x,y\in H),
$$

and the map $T\mapsto T^*$ is the **involution** of $B(H)$.

**Proposition (calculus of the adjoint).** The involution is conjugate-linear, involutive and reversing: for $S,T\in B(H)$ and $\lambda\in\mathbb{K}$,

$$
(S+T)^*=S^*+T^*,\qquad (\lambda T)^*=\bar\lambda T^*,\qquad (ST)^*=T^*S^*,\qquad T^{**}=T .
$$

It is isometric, $\|T^*\|=\|T\|$.

*Proof.* These are the identities of *Banach and Hilbert Spaces*, obtained by uniqueness in the defining relation and the Riesz representation theorem; isometry is $\|T^*\|=\|T\|$ there.

**Theorem (the C\*-identity).** For every $T\in B(H)$,

$$
\|T^*T\|=\|T\|^2 .
$$

Hence $B(H)$ is a $C^*$-algebra: a Banach algebra with an isometric involution satisfying the $C^*$-identity.

*Proof.* $\|T^*T\|\le\|T^*\|\|T\|=\|T\|^2$, and for $\|x\|\le1$ one has $\|Tx\|^2=\langle Tx,Tx\rangle=\langle T^*Tx,x\rangle\le\|T^*Tx\|\le\|T^*T\|$, so $\|T\|^2\le\|T^*T\|$.

**Definition.** An operator $T$ is **self-adjoint** if $T^*=T$, **skew-adjoint** if $T^*=-T$, **normal** if $T^*T=TT^*$, **unitary** if $T^*T=TT^*=I$, **positive** if $T=T^*$ and $\langle Tx,x\rangle\ge0$ for all $x$, and a **projection** if $T^2=T=T^*$. A **partial isometry** is a $T$ with $T^*T$ a projection; its **initial** and **final** projections are $T^*T$ and $TT^*$.

**Proposition (real and imaginary parts).** Every $T\in B(H)$ decomposes as $T=A+iB$ with $A,B$ self-adjoint, $A=\tfrac12(T+T^*)$ and $B=\tfrac1{2i}(T-T^*)$, and this decomposition is unique; $T$ is normal exactly when $A$ and $B$ commute, and unitary exactly when $A,B$ are self-adjoint with $A^2+B^2=I$ and $AB=BA$.

*Proof.* The two combinations are self-adjoint by the calculus, and their sum is $T$; uniqueness is the reality of the self-adjoint part. Normality is $[A,B]=0$, and unitarity adds $A^2+B^2=I$ since $T^*T=A^2+B^2+i[A,B]$.

## The Three Topologies

### The Norm Topology

**Definition.** The **norm topology** on $B(H)$ is the metric topology of $\|S-T\|$. A net $T_\alpha\to T$ in norm means $\|T_\alpha-T\|\to0$.

The norm topology is the topology of the Banach algebra structure and the one in which the involution and the product are continuous. It is in general strictly finer than the two topologies below.

### The Strong Operator Topology

**Definition.** The **strong operator topology** (SOT) is the topology of pointwise convergence on $H$: a net $T_\alpha\to T$ strongly means $\|T_\alpha x-Tx\|\to0$ for every $x\in H$.

**Proposition.** Addition and the involution are SOT-continuous, and multiplication is SOT-continuous in each variable separately; multiplication is not jointly SOT-continuous. The SOT is generated by the seminorms $T\mapsto\|Tx\|$, $x\in H$, and a strong limit of bounded operators is bounded.

*Proof.* Pointwise convergence preserves the vector operations and the adjoint, and $S_\alpha T_\alpha x-S Tx=(S_\alpha-S)T_\alpha x+S(T_\alpha-T)x$ requires a uniform bound on $\|T_\alpha x\|$, which a net need not have, giving the failure of joint continuity; the seminorms give the stated topology by definition.

### The Weak Operator Topology

**Definition.** The **weak operator topology** (WOT) is the topology of the matrix coefficients: a net $T_\alpha\to T$ weakly means $\langle T_\alpha x,y\rangle\to\langle Tx,y\rangle$ for all $x,y\in H$.

**Proposition (matrix coefficients and the predual).** The WOT is the coarsest topology making every linear functional $T\mapsto\langle Tx,y\rangle$ continuous; it is generated by the seminorms $T\mapsto|\langle Tx,y\rangle|$. On a separable $H$ the WOT is metrisable on norm-bounded subsets.

*Proof.* The seminorms define the topology by definition; the metrisability is the countability of the dense set over which the coefficients are tested together with the bound on $\|T\|$.

**Proposition (comparison of the topologies).** Every norm-convergent net converges strongly, and every strongly convergent net converges weakly:

$$
\text{norm}\ \Longrightarrow\ \text{SOT}\ \Longrightarrow\ \text{WOT},
$$

and both implications are strict in infinite dimension; on the unit ball of $B(H)$ the WOT and the SOT have the same closed convex sets, so a WOT-closed convex set is SOT-closed and conversely.

*Proof.* Norm convergence gives $\|T_\alpha x-Tx\|\le\|T_\alpha-T\|\|x\|$, whence SOT; SOT gives $|\langle(T_\alpha-T)x,y\rangle|\le\|(T_\alpha-T)x\|\|y\|$, whence WOT. The strictness is the shift: $S^{*n}\to0$ weakly but not strongly, while no nonzero SOT-null net converges in norm. The equality of the closed convex sets is Mazur's standard separation argument.

## The Unit Ball

**Theorem (compactness).** The unit ball $\{T:\|T\|\le1\}$ of $B(H)$ is compact in the WOT and in the SOT; on a separable $H$ both topologies on the ball are metrisable, hence sequentially compact.

*Proof.* The ball is a pointwise-bounded family of operators, so by the Tychonoff theorem the product of the closed discs $\{Tx:\|x\|\le1\}$ over a dense set is compact; the closed conditions $\langle Tx,y\rangle$ cut out a closed subset, giving WOT compactness; SOT compactness follows from the equality of the closed convex sets and the closedness of the ball. Metrisability is the countable dense test set.

**Remark.** The compactness of the ball in the WOT is the operator form of the Banach–Alaoglu theorem, and the equality of the WOT- and SOT-closed convex sets is the operator form of Mazur's theorem; both are used by the spectral theory of this Part. The predual description, in which $\langle Tx,y\rangle$ is the pairing of $T$ with the rank-one operator $x\otimes y$ of trace class, belongs to *Compact Operators*, where the trace-class space and its pairing with $B(H)$ are introduced.

## Concrete Classes and the Order

### Projections

**Proposition (the lattice of projections).** The projections of $B(H)$ are the orthogonal projections of *Banach and Hilbert Spaces*; they stand in a natural order $P\le Q$ iff $P H\subseteq Q H$, equivalently $QP=P$, and under this order the projections form a complete lattice with $P\wedge Q$ the projection onto $PH\cap QH$ and $P\vee Q$ the projection onto the closed span of $PH\cup QH$.

*Proof.* A projection is the orthogonal projection onto its range, and the range correspondence converts the inclusion of subspaces into the order; the lattice operations are the projection onto the intersection and onto the closed sum, whose existence is the projection theorem.

### Partial Isometries

**Proposition.** $T$ is a partial isometry exactly when $T=TT^*T$, and then $TT^*$ and $T^*T$ are projections and $T$ maps $\operatorname{ran}T^*T$ isometrically onto $\operatorname{ran}TT^*$. Every operator has a polar decomposition $T=U|T|$ with $|T|=(T^*T)^{1/2}$ positive and $U$ a partial isometry with $\ker U=\ker T$; the decomposition is unique, and $T$ is unitary exactly when $|T|=I$.

*Proof.* $T^*T$ is positive, so $|T|$ exists; the polar decomposition is the standard one and is developed in *Positive Operators and the Square Root* below, where the uniqueness is proved.

**Example (finite dimension).** For $H=\mathbb{K}^n$ the algebra $B(H)$ is $M_n(\mathbb{K})$ with the operator norm; the adjoint is the conjugate transpose, the $C^*$-identity is the familiar inequality for matrix norms, the WOT on the finite-dimensional ball is the usual topology, and every operator is compact, so the distinctions of the next article vanish in finite dimension.

**Example (diagonal and multiplication operators).** On $\ell^2$ the diagonal operators $D_a e_n=a_n e_n$ with $a\in\ell^\infty$ form a commutative $C^*$-subalgebra; on $L^2(X,\mu)$ the multiplication operators $M_f g=fg$ with $f\in L^\infty$ form a commutative $C^*$-subalgebra whose projections are the multiplications by indicator functions. In both cases the WOT is the topology of pointwise convergence of the coefficients and the norm topology is that of uniform convergence.

## Summary

On a Hilbert space $H$ the bounded operators form a unital Banach algebra $B(H)$ that is a $C^*$-algebra: the involution $T\mapsto T^*$ is conjugate-linear, isometric, order-reversing on products, and satisfies the $C^*$-identity $\|T^*T\|=\|T\|^2$. On a finite-dimensional $H$ this is the matrix algebra $M_n(\mathbb{K})$ with the conjugate transpose; in infinite dimension $B(H)$ is non-commutative and contains proper isometries. The algebra carries three topologies — the norm topology, the strong operator topology of pointwise convergence, and the weak operator topology of convergence of the matrix coefficients — with the strict chain norm $\Rightarrow$ SOT $\Rightarrow$ WOT; multiplication is only separately continuous in the SOT and WOT. The unit ball is WOT- and SOT-compact, and on a separable space both are metrisable on the ball, the two topologies having the same closed convex sets. The self-adjoint, skew-adjoint, normal, unitary, positive, projection and partial-isometry elements are characterised by the calculus of the involution, the projections form a complete lattice, and the polar decomposition reduces an arbitrary operator to a partial isometry and a positive operator, developed in *Positive Operators and the Square Root*. The compact ideal and the trace-class pairing that describes the predual of the WOT are *Compact Operators*; the spectral theorem is *Self-Adjoint Operators and the Spectral Theorem*; the Banach-space analogue is *Operators on a Banach Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$, $\langle\cdot,\cdot\rangle$ | Hilbert space and inner product, linear in the first argument |
| $B(H)$ | the unital $C^*$-algebra of bounded operators |
| $F(H)$ | the finite-rank operators |
| $\|T\|$ | the operator norm, submultiplicative |
| $T^*$ | the adjoint, $\langle Tx,y\rangle=\langle x,T^*y\rangle$ |
| $\|T^*T\|=\|T\|^2$ | the $C^*$-identity |
| SOT, WOT | strong and weak operator topologies |
| $P\le Q$ | the order on projections, $QP=P$ |
| $T=U|T|$ | the polar decomposition |
| $T^*T$, $TT^*$ | initial and final projections of a partial isometry |

## Further Reading

- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the topologies of $B(H)$ and the geometry of its operators.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the $C^*$-algebra structure, the weak operator topology and the compactness of the unit ball.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the predual of $B(H)$ and the weak topology of the predual.
- Gert K. Pedersen, *Analysis Now* (Springer, 1989), for a compact development of the bounded operator theory on Hilbert space.
- John von Neumann, "Zur Algebra der Funktionaloperationen und Theorie der normalen Operatoren", *Mathematische Annalen* **102** (1930), 370–427, for the original weak and strong operator topologies.
