# __Involutions of the Operator Algebra__

## Introduction

An algebra carries two layers: the elements, which the product multiplies, and the operators, which the product moves. The involution of the `- * Theory` group sits on the elements; the present article puts an involution on the operators. The passage is a **pairing** on the algebra: with respect to a nondegenerate pairing $\langle\cdot,\cdot\rangle$ every operator $T$ has an **adjoint** $T^{*}$ determined by $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$, and the assignment $T\mapsto T^{*}$ is an involution of the operator algebra $E=\operatorname{End}_k(A)$ — a $k$-linear anti-automorphism of order two. Its fixed elements are the **self-adjoint operators**, its negated elements the **skew-adjoint** ones, and the operator algebra with this involution is an involutive algebra, so that its self-adjoint part is a Jordan algebra, its skew part a Lie algebra, and its units carry the unitary operators of *Unitary Operators of an Involutive Algebra*.

This article develops the pairing of the category, the adjoint of an operator and the involution it defines on $E$, the fixed part and the structures it carries, and the relation between the involution of the elements and the involution of the operators — two structures that one pairing marries but that are not one and the same. The operator space and its ladder of subspaces are *The Operators on an Algebra*; the one-sided multiplications are *Left and Right Multiplication*; the trace, the pairing $\langle x,y\rangle=\tau(xy)$ and its nondegeneracy are *Frobenius Algebras*; the involutions of an algebra, its self-adjoint part and its unitary elements are *Involutive Algebras*, *The Self-Adjoint Part of an Algebra* and *Unitary Elements of an Involutive Algebra*; the opposite algebra and the anti-isomorphisms are *Opposite Algebras and Anti-Isomorphisms*. The adjoint attached to the twisted pairing is *The Adjoint in an Involutive Algebra*; the adjoints of the one-sided, the signed and the graded operators are *The Adjoint of the Left Multiplication on an Algebra*, *The Signed Adjoint Sandwich on an Algebra* and *The Graded Adjoint Action on a Module over an Algebra*, the following articles of this group. The Hilbert-space adjoint, the norm, the positivity and the topology of the operator algebra are Part II and *Operator Algebras*, and are named as the owner and not used.

Throughout, $k$ is a field of characteristic not two, $A$ is a finite-dimensional unital associative $k$-algebra, and $\tau : A \to k$ is a trace whose pairing $\langle x,y\rangle=\tau(xy)$ is nondegenerate; a functional whose product pairing is nondegenerate is a Frobenius functional, and a trace with a nondegenerate one makes $A$ a symmetric Frobenius algebra. The operator space is $E=\operatorname{End}_k(A)$, of dimension $(\dim_k A)^2$ over $k$, the left and right multiplications by $a$ are $L_a$ and $R_a$, and the adjoint of $T \in E$ for the pairing $\langle\cdot,\cdot\rangle$ is written $T^{*}$. An involution of the elements is written $\sigma$ and its image $\sigma(x)$; the adjoint for the twisted pairing is written $T^{*_\sigma}$.

## The Pairing of the Category

**Definition.** The **pairing of the category** on $A$ is

$$
\langle x,y\rangle = \tau(xy),
$$

where $\tau : A \to k$ is a linear functional. It is **symmetric** when $\tau(xy)=\tau(yx)$ for all $x,y$, that is when $\tau$ is a trace, and **nondegenerate** when $\langle x,z\rangle=0$ for all $z$ forces $x=0$ and $\langle z,y\rangle=0$ for all $z$ forces $y=0$. A trace with a nondegenerate product pairing is a **Frobenius trace**, and $(A,\tau)$ is then a **symmetric Frobenius algebra**.

**Proposition.** The pairing is symmetric for a trace, reflexive, and associative in the sense

$$
\langle xy,z\rangle=\langle x,yz\rangle ;
$$

it is compatible with the two multiplications,

$$
\langle ax,y\rangle=\langle x,ya\rangle, \qquad \langle xa,y\rangle=\langle x,ay\rangle \qquad (a,x,y \in A).
$$

*Proof.* Symmetry is the trace property $\tau(xy)=\tau(yx)$, and a symmetric pairing is reflexive because $\langle x,y\rangle=0$ and $\langle y,x\rangle=0$ are then the same equation. Associativity is the identity $\tau(xyz)=\tau(xyz)$ read with the product grouped on the two sides. The first compatibility is $\langle ax,y\rangle=\tau(axy)=\tau(xya)=\langle x,ya\rangle$ by the cyclicity $\tau(uv)=\tau(vu)$ of the trace, and the second is $\langle xa,y\rangle=\tau(xay)=\langle x,ay\rangle$ by the definition of the pairing.

The compatibility is what makes the pairing the one of the category: the product acts on the pairing by moving an element from one argument to the other, and this move is the reason the one-sided multiplications have adjoints at all. The functional $\tau$ is the abstract trace, and $\langle x,y\rangle=\tau(xy)$ is its associated pairing in the sense of *Frobenius Algebras*; the nondegeneracy is the Frobenius condition, a condition on $\tau$ and not on $A$.

**Example (the matrix algebra).** For $A=M_n(k)$ and $\tau=\operatorname{Tr}$ the matrix trace, $\langle X,Y\rangle=\operatorname{Tr}(XY)$ is symmetric and nondegenerate; the pairing of the category is the trace pairing of the matrix algebra.

**Example (the group algebra).** For $A=k[G]$ with $G$ finite and $\tau$ the coefficient of the identity element, $\langle x,y\rangle$ is the coefficient of $1$ in $xy$; it is symmetric, and it is nondegenerate because the coefficient of $1$ in $gh$ is nonzero exactly for $h=g^{-1}$. The Frobenius trace is the coefficient functional of the group algebra.

**Example (the exterior algebra).** For $A=\Lambda(V)$ with $V$ of finite dimension and $\tau$ the coefficient of the top power, the pairing is the Frobenius pairing of the exterior algebra; it is supersymmetric rather than symmetric, and its graded reading is *The Graded Adjoint Action on a Module over an Algebra* below.

## The Adjoint of an Operator

**Definition.** Let $T \in E$. An operator $T^{*} \in E$ is an **adjoint** of $T$ for the pairing when

$$
\langle Tx,y\rangle=\langle x,T^{*}y\rangle \qquad \text{for all } x,y \in A .
$$

**Theorem.** For a nondegenerate pairing every $T \in E$ has exactly one adjoint $T^{*}$.

*Proof.* Fix $y \in A$. The map $x \mapsto \langle Tx,y\rangle$ is a $k$-linear functional on $A$, because $T$ and the pairing are linear. A nondegenerate pairing on a finite-dimensional space represents every functional uniquely: the map $z \mapsto \langle\cdot,z\rangle$ is an isomorphism $A \to A^{\vee}$ in finite dimension, so there is exactly one $z$ with $\langle x,z\rangle=\langle Tx,y\rangle$ for all $x$. That $z$ depends on $y$, and the dependence is $k$-linear because $y \mapsto \langle Tx,y\rangle$ is; write $T^{*}y=z$. Uniqueness of the represented element gives uniqueness of the adjoint: if $S$ also represents, then $\langle x,(S-T^{*})y\rangle=0$ for all $x$ and $y$, so $S=T^{*}$.

The adjoint is therefore not an extra datum but a function of the pairing, and a different nondegenerate pairing gives a different adjoint of the same operator. The transpose and the Hermitian conjugate of a matrix are both adjoints of it, taken with respect to the trace pairing and to the positive definite pairing; the former is the pairing of this category, and the latter is Part II.

**Proposition (the adjoint of a composite).** For $S,T \in E$,

$$
\langle STx,y\rangle=\langle x,T^{*}S^{*}y\rangle ,
$$

so the adjoint of a composite is the composite of the adjoints in the reverse order.

*Proof.* Apply the definition twice, the second time with the input $Tx$: $\langle STx,y\rangle=\langle Tx,S^{*}y\rangle=\langle x,T^{*}S^{*}y\rangle$.

## The Involution of the Operator Algebra

**Theorem.** The assignment $T \mapsto T^{*}$ is an involution of the $k$-algebra $E$:

$$
(T+S)^{*}=T^{*}+S^{*}, \qquad (\lambda T)^{*}=\lambda T^{*}, \qquad (TS)^{*}=S^{*}T^{*}, \qquad (T^{*})^{*}=T, \qquad \mathrm{id}^{*}=\mathrm{id} .
$$

It is a $k$-linear anti-automorphism of $E$ of order two, and $(E,*)$ is an involutive algebra in the sense of *Involutive Algebras*.

*Proof.* Additivity and homogeneity follow from the linearity of the representing element in the preceding theorem, and anti-multiplicativity is the proposition above. For order two, use the symmetry of the pairing: $\langle T^{*}x,y\rangle=\langle y,T^{*}x\rangle=\langle Ty,x\rangle=\langle x,Ty\rangle$, the middle equality being the definition of $T^{*}$ read with its two arguments exchanged. Comparing $\langle T^{*}x,y\rangle=\langle x,T^{**}y\rangle$ with $\langle T^{*}x,y\rangle=\langle x,Ty\rangle$ and using nondegeneracy in $x$ gives $T^{**}y=Ty$ for every $y$. The identity is self-adjoint because $\langle \mathrm{id}\,x,y\rangle=\langle x,y\rangle=\langle x,\mathrm{id}\,y\rangle$.

**Corollary (invertibility).** If $T$ is invertible then $T^{*}$ is invertible, with

$$
(T^{-1})^{*}=(T^{*})^{-1} .
$$

*Proof.* Apply $*$ to $TT^{-1}=\mathrm{id}$ and to $T^{-1}T=\mathrm{id}$, using anti-multiplicativity and $\mathrm{id}^{*}=\mathrm{id}$: $(T^{-1})^{*}T^{*}=\mathrm{id}=T^{*}(T^{-1})^{*}$, so $(T^{-1})^{*}$ is the two-sided inverse of $T^{*}$.

**Corollary (the involution and the unit group).** The involution $*$ restricts to an anti-automorphism of order two of the unit group $E^{\times}$, and the composite

$$
\theta : E^{\times} \to E^{\times}, \qquad \theta(T)=(T^{*})^{-1},
$$

is an automorphism of $E^{\times}$ of order two. Its fixed subgroup is the group of unitary operators of *Unitary Operators of an Involutive Algebra*.

*Proof.* The involution maps units to units and reverses products, and inversion reverses products, so $\theta$ preserves them; $\theta^{2}(T)=\theta\bigl((T^{*})^{-1}\bigr)=\bigl(((T^{*})^{-1})^{*}\bigr)^{-1}=\bigl((T^{-1})\bigr)^{-1}=T$, where the invertibility corollary is applied to $T^{*}$ in the middle step. The structure of the fixed subgroup is the general theory of *Unitary Elements of an Involutive Algebra*, applied to the involutive algebra $(E,*)$.

## The Fixed Elements

**Definition.** The **self-adjoint operators** and the **skew-adjoint operators** of $(E,*)$ are

$$
E^{+}=\{T \in E : T^{*}=T\}, \qquad E^{-}=\{T \in E : T^{*}=-T\}.
$$

**Theorem.** $E^{+}$ and $E^{-}$ are $k$-linear subspaces of $E$ with

$$
E=E^{+}\oplus E^{-}, \qquad T=\tfrac12\bigl(T+T^{*}\bigr)+\tfrac12\bigl(T-T^{*}\bigr),
$$

and the involution acts as the identity on $E^{+}$ and as minus the identity on $E^{-}$. With the symmetrised product $S\bullet T=\tfrac12(ST+TS)$ the space $E^{+}$ is a Jordan algebra, with the commutator $[S,T]=ST-TS$ the space $E^{-}$ is a Lie algebra, and the two are tied by the inclusions $E^{+}\bullet E^{-}\subseteq E^{-}$ and $[E^{+},E^{-}]\subseteq E^{+}$, so that $(E^{+},E^{-})$ is the Jordan–Lie pair of the involution.

*Proof.* The spaces are the eigenspaces of the order-two linear map $*$ for the eigenvalues $1$ and $-1$, so they are subspaces intersecting in $0$ and summing to $E$ in characteristic not two, by the displayed averaging. The algebraic statements are those of *Involutive Algebras* and *The Self-Adjoint Part of an Algebra*, applied to the involutive algebra $(E,*)$. The inclusions are read off from anti-multiplicativity: for $S,T \in E^{+}$ one has $(ST)^{*}=T^{*}S^{*}=TS$, so $S\bullet T$ is self-adjoint and $[S,T]$ is skew-adjoint; for $S \in E^{+}$ and $T \in E^{-}$ one has $(ST)^{*}=T^{*}S^{*}=(-T)S=-TS$ and $(TS)^{*}=S^{*}T^{*}=S(-T)=-ST$, so $S\bullet T=\tfrac12(ST+TS)$ is skew-adjoint.

**Corollary.** The identity operator is self-adjoint, and a scalar operator $\lambda\,\mathrm{id}$ is self-adjoint for every $\lambda \in k$; the scalars lie in the centre of $E$ and in $E^{+}$.

*Proof.* $\mathrm{id}^{*}=\mathrm{id}$ and the involution is $k$-linear, so $(\lambda\,\mathrm{id})^{*}=\lambda\,\mathrm{id}$; a scalar operator is central because it commutes with every operator.

**Example (the one-sided multiplications).** The multiplications of $A$ satisfy $L_a^{*}=R_a$ and $R_b^{*}=L_b$, computed in *The Adjoint of the Left Multiplication on an Algebra* from the compatibility of the pairing. Hence $L_a$ is self-adjoint exactly when $a$ is central, and the operator involution exchanges the two sides of the regular representation. It acts on the parameters by the element involution only after the twisted pairing is used, which is the content of the next section.

**Example (a matrix algebra).** For $A=M_n(k)$ with the trace pairing, the adjoint of $T \in \operatorname{End}_k(M_n(k))$ is the adjoint of $T$ with respect to the trace pairing, and the self-adjoint operators are those with $\langle TX,Y\rangle=\langle X,TY\rangle$ for all $X,Y$; the left multiplication by a matrix is self-adjoint exactly when that matrix is scalar.

## The Element Involution and the Operator Involution

**Definition.** Let $\sigma$ be an involution of $A$ with $\tau(\sigma(x))=\tau(x)$ for all $x$. The **$\sigma$-twisted pairing** is

$$
\{x,y\}=\tau\bigl(x\,\sigma(y)\bigr).
$$

**Theorem (the twisted pairing).** The twisted pairing is symmetric and nondegenerate, and the map

$$
c_{\sigma} : E \to E, \qquad c_{\sigma}(T)=\sigma\,T\,\sigma,
$$

is an involutive algebra automorphism of $E$ of order two.

*Proof.* For symmetry, $\{y,x\}=\tau(y\sigma(x))=\tau(\sigma(y\sigma(x)))=\tau(x\sigma(y))=\{x,y\}$, using the $\sigma$-invariance of $\tau$ and the anti-multiplicativity $\sigma(y\sigma(x))=\sigma(\sigma(x))\sigma(y)=x\sigma(y)$. For nondegeneracy, $\{x,y\}=0$ for all $y$ means $\tau(xz)=0$ for all $z$ after $y$ is replaced by $\sigma(y)$, which ranges over $A$ because $\sigma$ is bijective; the nondegeneracy of $\langle\cdot,\cdot\rangle$ then gives $x=0$. The map $c_{\sigma}$ is a composite of the anti-automorphism $\sigma$ with itself, hence is multiplicative: $c_{\sigma}(ST)=\sigma ST\sigma=(\sigma T\sigma)(\sigma S\sigma)=c_{\sigma}(T)c_{\sigma}(S)$; it is $k$-linear, unital, and $c_{\sigma}^{2}(T)=\sigma^{2}T\sigma^{2}=T$.

**Proposition (the two involutions differ by the element involution).** Let $T^{*_\sigma}$ be the adjoint of $T$ for the twisted pairing. Then

$$
T^{*_\sigma}=\sigma\,T^{*}\,\sigma=c_{\sigma}(T^{*}),
$$

the twisted adjoint is the conjugate of the plain adjoint by the element involution, and the two involutions of $E$ agree on $T$ exactly when $T^{*}$ commutes with $\sigma$.

*Proof.* The identity is proved in *The Adjoint in an Involutive Algebra* by a comparison of the two pairings; the agreement statement is the case $\sigma T^{*}\sigma=T^{*}$, which is the commutation of $T^{*}$ with $\sigma$.

The proposition is the reason the element involution and the operator involution are two structures and not one: a single pairing produces the operator involution, and the element involution acts on it by conjugation, so that a second pairing must be chosen before the two agree. When the left regular representation satisfies $L_{\sigma(a)}=L_a^{*_\sigma}$ the representation is a `*`-representation, and that agreement is proved, not assumed, in *The Adjoint of the Left Multiplication on an Algebra*.

**Example (the matrix algebra with the transpose).** Let $A=M_n(k)$, $\sigma$ the transpose and $\tau=\operatorname{Tr}$. The plain pairing is $\langle X,Y\rangle=\operatorname{Tr}(XY)$ and the twisted pairing is $\{X,Y\}=\operatorname{Tr}(XY^{\mathsf{T}})=\sum_{i,j}X_{ij}Y_{ij}$, the positive definite trace pairing of the matrix algebra; the conjugation $c_{\sigma}(T)$ is the transpose-conjugate of an operator on matrices, and the two operator involutions differ by it.

## Summary

A nondegenerate symmetric pairing $\langle x,y\rangle=\tau(xy)$ on a finite-dimensional algebra $A$ gives every operator $T \in E=\operatorname{End}_k(A)$ an adjoint $T^{*}$ by $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$, and the assignment $T\mapsto T^{*}$ is a $k$-linear anti-automorphism of $E$ of order two: the **involution of the operator algebra**, which makes $(E,*)$ an involutive algebra. Its fixed part $E^{+}$ is the self-adjoint operators, a Jordan algebra under the symmetrised product, its negated part $E^{-}$ is the skew-adjoint operators, a Lie algebra under the commutator, the two forming the Jordan–Lie pair, and the involution restricts to an anti-automorphism of the unit group with the automorphism $\theta(T)=(T^{*})^{-1}$. An involution $\sigma$ of the elements with $\tau\sigma=\tau$ produces the twisted pairing $\{x,y\}=\tau(x\sigma(y))$, a second nondegenerate pairing, and the two operator involutions differ by the conjugation $c_{\sigma}(T)=\sigma T\sigma$: $T^{*_\sigma}=\sigma T^{*}\sigma$. The involution of the elements and the adjoint of the operators are therefore two structures married by the pairing but not equal, and the agreement on a representation is proved rather than assumed. The adjoints of the one-sided, signed and graded operators are the following articles of the group, and the norm, the positivity and the Hilbert-space adjoint are Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $A$ | the field, and a finite-dimensional unital associative $k$-algebra |
| $\tau$, $\langle x,y\rangle=\tau(xy)$ | the Frobenius trace and the pairing of the category |
| $E=\operatorname{End}_k(A)$ | the algebra of operators of $A$ |
| $T^{*}$ | the adjoint of $T$, defined by $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$ |
| $(TS)^{*}=S^{*}T^{*}$, $(T^{*})^{*}=T$ | the involution of the operator algebra |
| $\theta(T)=(T^{*})^{-1}$ | the order-two automorphism of the unit group $E^{\times}$ |
| $E^{+}$, $E^{-}$ | the self-adjoint and the skew-adjoint operators |
| $\sigma$, $\sigma(x)$ | an involution of the elements and its image |
| $\{x,y\}=\tau(x\sigma(y))$ | the $\sigma$-twisted pairing |
| $T^{*_\sigma}$ | the adjoint for the twisted pairing |
| $c_{\sigma}(T)=\sigma T\sigma$ | the conjugation by the element involution |
| $T^{*_\sigma}=c_{\sigma}(T^{*})$ | the relation between the two operator involutions |
| $L_a$, $R_a$, $L_a^{*}=R_a$ | the one-sided multiplications and their adjoints |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the multiplication algebra, the trace form and the operators of the regular representation.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the adjoint involution on an algebra of operators and its fixed elements.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the operator algebra of a finite-dimensional algebra and the trace pairing.
- Matej Brešar, *Introduction to Noncommutative Algebra* (Springer, 2014), for the endomorphism algebra of a module, the adjoint under a nondegenerate pairing and the centraliser of an involution.
