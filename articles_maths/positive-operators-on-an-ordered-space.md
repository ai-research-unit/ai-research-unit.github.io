
# __Positive Operators on an Ordered Space__

## Introduction

A linear map between two ordered vector spaces is **positive** when it carries positive elements to positive elements, and it is then exactly a map that preserves the order:

$$
x\leq y \implies Tx\leq Ty .
$$

Positive operators are the structure-preserving maps of the category of ordered vector spaces, in the same sense in which the algebra homomorphisms preserve the product and the continuous maps preserve the topology, and they are the objects of this article. Their set is a convex cone, the *positive cone of the operators*, closed under addition and composition; it makes the space of operators an ordered vector space in its turn, and the order it defines is the **operator order** $S\leq T \iff T - S\geq0$. The order-bounded functionals of an ordered vector space, the order automorphisms of a convex set, and every operator studied in the rest of this category are instances.

The name "positive operator" recurs in the corpus with another meaning: a **positive operator on a Hilbert space** is a self-adjoint operator with nonnegative quadratic form, the operators of *Self-Adjoint Operators* and *Positive Operators and the Square Root*, and their positivity is measured by an inner product. That notion and the order-theoretic one of this article are different: a positive operator on a Hilbert space is positive in the order of the self-adjoint operators, whereas a positive operator of this article is order preserving and need not be self-adjoint. The two are related when the Hilbert space is ordered by its cone of positive operators, but they are not the same, and the article uses the phrase "positive operator on an ordered space" throughout to fix the meaning.

The order and the order-unit norm are those of *Ordered Vector Spaces and the Order Unit*, the convex-cone vocabulary is *Cones, Extremal Rays and the Choquet Theory*, and the bounded operators and their norms are *Bounded Operators and the Operator Norm* and *The Operator Algebra of a Banach Space* of Part II. The Riesz–Kantorovich theorem, that the regular operators between Riesz spaces form a Riesz space, is deferred to *The Order Projection* later in this category; a forward reference carries the flag.

## Positive Operators

### Definition and Characterisation

Let $E$ and $F$ be ordered vector spaces and let $L(E,F)$ be the real vector space of linear maps.

**Definition.** A linear map $T\in L(E,F)$ is **positive**, written $T\geq0$, when

$$
x\in E_+ \implies Tx\in F_+ .
$$

It is **strictly positive** when it carries every nonzero element of $E_+$ to a nonzero element of $F_+$. The **operator order** on $L(E,F)$ is $S\leq T$ when $T - S\geq0$.

**Proposition (positive equals monotone).** A linear map $T$ is positive if and only if $x\leq y$ implies $Tx\leq Ty$.

*Proof.* If $T\geq0$ and $x\leq y$ then $y - x\in E_+$, so $Ty - Tx = T(y-x)\in F_+$. Conversely if $T$ is monotone and $x\in E_+$ then $0\leq x$ gives $0 = T0\leq Tx$.

**Proposition (the cone of positive operators).** The set $L_+(E,F) = \{T : T\geq0\}$ is a convex cone: it is closed under addition and under multiplication by nonnegative scalars. It is pointed when $E_+$ generates $E$, so that the operator order is a partial order on $L(E,F)$; when $E_+$ does not generate, two operators differing by a map vanishing on the span of $E_+$ are comparable in both directions.

*Proof.* For $S,T\geq0$ and $\lambda,\mu\geq0$ the operator $\lambda S + \mu T$ sends $E_+$ into $E_+$ by the closure of $F_+$ under addition and nonnegative scaling. If $E_+$ generates and $T\geq0$, $-T\geq0$, then for $x = a - b$ with $a,b\in E_+$ one has $Tx = Ta - Tb$ with both terms positive and both negatives positive, so each is zero by the pointedness of $F_+$, and $Tx = 0$ for every $x$.

**Proposition (stability).** A sum of positive operators is positive; a nonnegative multiple of a positive operator is positive; and a composite $E\xrightarrow{S}F\xrightarrow{T}G$ of positive operators is positive. The identity of an ordered vector space is positive, and a positive operator carries an order interval into an order interval, $T[x,y]\subseteq[Tx,Ty]$.

*Proof.* Each statement is the closure of the cone under the corresponding operation, read through the definition; the interval statement is the monotonicity applied to the two endpoints.

### Positive Functionals

**Definition.** A **positive functional** on an ordered vector space $E$ is a positive element of the order dual, $f\in L_+(E,\mathbb{R})$, where $\mathbb{R}$ carries its usual order. The set of positive functionals is the **dual cone** $E^*_+$ of *Cones, Extremal Rays and the Choquet Theory*.

**Proposition.** $f\geq0$ if and only if $f$ is monotone, and then $\lvert f\rvert$ is not defined in general: the difference of two positive functionals need not be positive, and the order on the dual is the dual order.

*Proof.* The first assertion is the monotonicity criterion applied with $F = \mathbb{R}$. The second is the elementary observation that $f = f_1 - f_2$ with both $f_i\geq0$ is a stricter condition than $f$ being order bounded; the functionals representable in this way are the **regular** functionals.

**Proposition (the transpose preserves positivity).** Let $T\in L(E,F)$ be positive and let $T' : F^*\to E^*$ be its transpose, $T'g = g\circ T$. Then $T'\geq0$.

*Proof.* If $g\geq0$ on $F$ and $x\in E_+$ then $(T'g)(x) = g(Tx)\geq0$ because $Tx\in F_+$.

### Positive Operators between Order-Unit Spaces

**Proposition (a positive operator is bounded, and its norm is attained at the unit).** Let $E$ and $F$ have order units $u$ and $v$, with order-unit norms $\|\cdot\|_u$ and $\|\cdot\|_v$, and suppose $E$ is Archimedean. A positive operator $T\in L(E,F)$ is bounded for the order-unit norms, and

$$
\|T\| = \|Tu\|_v .
$$

*Proof.* If $\|x\|_u\leq1$ then $-\!u\leq x\leq u$, so $-\!Tu\leq Tx\leq Tu$ by positivity, which is $\|Tx\|_v\leq\|Tu\|_v$; conversely $\|u\|_u = 1$ gives the reverse inequality for the operator norm, which is $\sup\{\|Tx\|_v : \|x\|_u\leq1\}$.

This is the first appearance of the metric theory of the order: a positive operator is automatically continuous for the order topology, and the norm of the operator is read off at the order unit. The order-unit norm and the topology are *Ordered Vector Spaces and the Order Unit*.

## The Operator Order

### Comparability, Intervals and the Cone

**Proposition.** The relation $S\leq T$ is reflexive, transitive and compatible with the linear operations of $L(E,F)$; it is antisymmetric, hence a partial order, exactly when the cone $L_+(E,F)$ is pointed, which holds when $E$ is directed and $F$ is pointed.

*Proof.* Reflexivity is $T - T = 0\in L_+$; transitivity is the closure of $L_+$ under addition; compatibility is linearity. Antisymmetry is the pointedness of the cone, which was characterised in the previous section.

**Proposition (the order interval of operators).** For $S\leq T$ the interval $[S,T]$ consists of the operators of the form $S + R$ with $R\geq0$ and $R\leq T-S$; it is convex, and it is order bounded in $L(E,F)$.

*Proof.* Unwinding $S\leq X\leq T$ gives $0\leq X - S$ and $0\leq (T - S) - (X - S)$, which is the stated form.

### The Order Ideal of Regular Operators and the Deferred Modulus

**Definition.** An operator $T\in L(E,F)$ is **regular** when it is the difference of two positive operators, $T = T_1 - T_2$ with $T_i\geq0$, and **order bounded** when it maps an order interval of $E$ into an order interval of $F$. The regular operators form a linear subspace $L^r(E,F)$, and the order-bounded ones contain it.

**Proposition.** Every positive operator is regular; every regular operator is order bounded; and $L^r(E,F)$ is the span of the cone $L_+(E,F)$, so $L^r(E,F)$ is an ordered vector space with positive cone $L_+(E,F)$.

*Proof.* The first two statements are the definitions with a zero term; the span of a cone is closed under addition and contains the opposites of its elements, so it is a subspace, and its positive part is $L_+$.

**Theorem (Riesz–Kantorovich, deferred).** When $F$ is a Riesz space — an ordered vector space in which every pair has a least upper bound — the regular operators $L^r(E,F)$ are themselves a Riesz space, the lattice operations are computed pointwise on the positive cone of $E$, and every order-bounded operator is regular. The proof and the bands are in *The Order Projection* later in this category, and the statement is quoted here so that the modulus of an operator can be named.

**Definition.** When $L^r(E,F)$ is a Riesz space, the **modulus** of $T\in L^r(E,F)$ is $\lvert T\rvert = T\vee(-T)$, and the **positive and negative parts** are $T^+ = T\vee0$ and $T^- = (-T)\vee0$, so that $T = T^+ - T^-$ and $\lvert T\rvert = T^+ + T^-$.

### The Dual Order and the Adjoint

**Proposition (the operator order on the operators of a Hilbert space is the symmetric one).** Let $H$ be a Hilbert space ordered by the cone of positive operators of *Positive Operators and the Square Root*. A self-adjoint operator $A$ is positive in that order exactly when it is positive in the order-theoretic sense on the ordered space $(H,\overline{H_+})$, where the closure is in the norm; for a general (not self-adjoint) operator the two notions diverge, since an order-preserving operator of $H$ need not be self-adjoint.

*Proof.* For self-adjoint $A$ the condition $\langle Ax,x\rangle\geq0$ for all $x$ is the condition that $A$ maps the cone into itself, by the spectral theorem; a non-self-adjoint order-preserving operator, such as a nonnegative multiple of a nonunitary isometry, is positive on the cone and not positive in the quadratic-form sense, which is defined only for self-adjoint operators.

## Worked Cases

### Multiplication Operators

Let $E = F = C(X)$ with the pointwise order and let $g\in C(X)$. The multiplication operator $M_g(f) = gf$ is positive exactly when $g\geq0$, because the image of the constant function $1$ is $g$; and the map $g\mapsto M_g$ is an order isomorphism onto the multiplication operators. The modulus of $M_g$ is $M_{\lvert g\rvert}$, and the interval $[M_g,M_h]$ consists of the $M_k$ with $g\leq k\leq h$. This is the commutative model of the operator order, and it is the model on which the Riesz–Kantorovich theorem is read in *The Order Projection*.

### Positive Maps of Matrix Algebras

Let $E = F = H_n(\mathbb{R})$ with the Loewner order and let $T : H_n(\mathbb{R})\to H_n(\mathbb{R})$ be linear. Then $T\geq0$ in the order-theoretic sense exactly when $T$ maps the cone of positive semidefinite matrices into itself — that is, when $T$ is a **positive map** in the sense of operator theory. The transpose map $X\mapsto X^{\mathsf{T}}$ is positive, and it is not completely positive; the map $X\mapsto\operatorname{tr}(X)1$ is positive and not faithful. The positive maps form a cone $L_+$ whose extreme rays are described by the Størmer theorem, and the completely positive maps are the subcone that the GNS theory of *Operator Algebras* singles out.

### Positive Functionals and the State Space

Let $E$ have an order unit $u$. The positive functionals are the cone $E^*_+$; a state is a positive functional with $f(u) = 1$, and the state space is a base of the cone by *Ordered Vector Spaces and the Order Unit*. The evaluation $T\mapsto T(u)\in F$ is an order isomorphism from the positive operators to the positive elements of $F$ when $E$ is the free order-unit space generated by $u$ with the interval as its unit ball; the general relation between an operator and its value at the unit is the order-unit estimate of the previous section.

## Summary

A linear map $T$ between ordered vector spaces is **positive** when $T(E_+)\subseteq F_+$, and equivalently when it is monotone for the orders. The positive operators form a **convex cone** $L_+(E,F)$, pointed exactly when $E$ is directed and $F$ pointed; sums, nonnegative multiples, composites and the identity are positive, and a positive operator carries intervals into intervals. The cone makes $L(E,F)$ an ordered vector space under the **operator order** $S\leq T\iff T-S\geq0$, whose comparable pairs are characterised by two positivity conditions. A positive **functional** is a positive element of the order dual; its transpose is positive; and a positive operator between order-unit spaces is bounded, with $\|T\| = \|Tu\|_v$. The **regular** operators are the differences of positive operators and form the span of the cone; when the target is a Riesz space the regular operators form a Riesz space, by **Riesz–Kantorovich**, whose statement is quoted and whose proof is in *The Order Projection*. The order-theoretic positivity of this article is not the positivity of the self-adjoint operators of a Hilbert space, which is defined by an inner product; the two agree on the self-adjoint operators and diverge otherwise. The order and the order-unit norm are *Ordered Vector Spaces and the Order Unit*, the cones and their duals are *Cones, Extremal Rays and the Choquet Theory*, and the bounded operators are *Bounded Operators and the Operator Norm* of Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T\geq0$ | Positive operator, $T(E_+)\subseteq F_+$, equivalently monotone |
| $L_+(E,F)$ | Cone of positive operators |
| $S\leq T \iff T-S\geq0$ | Operator order |
| $E^*_+$ | Cone of positive functionals, the dual cone |
| $T'$ | Transpose, positive when $T$ is |
| $L^r(E,F)$ | Regular operators, the span of $L_+$ |
| $\lvert T\rvert$, $T^\pm$ | Modulus and positive and negative parts, in the Riesz case |
| $\|T\| = \|Tu\|_v$ | Norm of a positive operator between order-unit spaces |

## Further Reading

- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the cone of positive operators, the operator order and the Riesz–Kantorovich theorem.
- Graham Jameson, *Ordered Linear Spaces*, Lecture Notes in Mathematics 141 (Springer, 1970), for positivity, the operator order and the order-unit estimates.
- Peter Meyer-Nieberg, *Banach Lattices* (Springer, 1991), for positive operators on a Riesz space and their norms.
- Erling Størmer, "Positive linear maps of operator algebras", *Acta Mathematica* **110** (1963), 233–278, for the extreme rays of the positive maps of a matrix algebra.
- Man-Duen Choi, "Completely positive linear maps on complex matrices", *Linear Algebra and its Applications* **10** (1975), 285–290, for complete positivity and its difference from positivity.
