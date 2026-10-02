
# __The Graded Adjoint Action on a Module over a Ring__

## Introduction

When a ring $A$ carries a $\mathbb{Z}/2$-grading and a module $M$ over it is graded as well, the operators that respect the grading acquire a **sign**: a homogeneous operator $T$ of degree $\lvert T\rvert$ satisfies $T(xa) = (-1)^{\lvert T\rvert\lvert a\rvert}T(x)a$ and $T(ax) = (-1)^{\lvert T\rvert\lvert a\rvert}aT(x)$ according to the side, and the adjoint of a product carries the Koszul sign,

$$
(ST)^{*} = (-1)^{\lvert S\rvert\lvert T\rvert}\,T^{*}S^{*} .
$$

The **adjoint action** is the inner operator $\operatorname{ad}_x(y) = xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx$ of the graded commutator; it is a graded derivation of degree $\lvert x\rvert$, it is compatible with the grading in the sense that it shifts the degree by $\lvert x\rvert$, and it is compatible with an involution $\sigma$ of degree zero exactly when $x$ lies in the appropriate eigenspace of $\sigma$. This article fixes the graded pairing on a graded module, computes the adjoint of a homogeneous operator, states the Koszul sign rule, and reads the adjoint action as a graded derivation with its sign.

It assumes *The Graded Action on a Module over a Ring* for the graded action, *Involutions of the Endomorphism Ring* for the adjoint, *Star-Derivations and the Skew Derivations* for the inner derivations; the superalgebra of the sign rule is *Superalgebras and Graded Structures* and is named rather than used. Throughout, $A$ is a ring with a $\mathbb{Z}/2$-grading, $M$ is a graded module over $A$, the pairing $\langle-,-\rangle$ is biadditive and homogeneous of degree zero, homogeneous elements are written with their parity $\lvert a\rvert\in\mathbb{Z}/2$, and the sign $(-1)^{\lvert a\rvert\lvert b\rvert}$ is the Koszul sign.

## The Graded Pairing and the Adjoint

**Definition.** The pairing $\langle x,y\rangle$ on the graded module is **graded** when it is biadditive and homogeneous of degree zero, $\lvert\langle x,y\rangle\rvert = \lvert x\rvert+\lvert y\rvert$, and **supersymmetric** when

$$
\langle y,x\rangle = (-1)^{\lvert x\rvert\lvert y\rvert}\langle x,y\rangle .
$$

The **grade involution** of the ring acts on homogeneous elements by $a\mapsto (-1)^{\lvert a\rvert}a$; it is the operator $\alpha$ of the signed articles of this group.

**Theorem.** For a homogeneous operator $T$ the adjoint $T^{*}$ defined by $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$ is homogeneous of degree $\lvert T\rvert$, and for homogeneous $S, T$

$$
(ST)^{*} = (-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}, \qquad (T^{*})^{*} = T, \qquad \mathrm{id}^{*} = \mathrm{id} .
$$

The adjoint is a **graded involution**: it is anti-multiplicative up to the Koszul sign.

**Proof.** The existence and uniqueness of $T^{*}$ are those of *Involutions of the Endomorphism Ring*; the degree is read off from $\lvert\langle Tx,y\rangle\rvert = \lvert T\rvert+\lvert x\rvert+\lvert y\rvert = \lvert x\rvert+\lvert T^{*}y\rvert$, so $\lvert T^{*}y\rvert = \lvert T\rvert+\lvert y\rvert$ and $\lvert T^{*}\rvert = \lvert T\rvert$. For the product, $(-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$ is the ordinary adjoint of $ST$ with the sign inserted to make the two factors homogeneous of the correct degree: passing $S$ past $T^{*}$ in the chain of the pairing introduces the sign $(-1)^{\lvert S\rvert\lvert T\rvert}$, which is the Koszul rule; the order-two and the unit statements are as in the ungraded case.

**Corollary (compatibility with the grading).** The adjoint of a homogeneous operator preserves the parity, and the map $T\mapsto T^{*}$ is compatible with the grading in the sense of the sign rule above; on the even operators it restricts to the adjoint involution of the ungraded article, and on the odd ones it is the twisted (signed) adjoint.

**Proof.** The degree statement is the theorem; the restriction is the observation that for $\lvert T\rvert = 0$ the Koszul sign is $1$ and the rule is the ungraded one, while for odd operators the sign survives.

## The Adjoint Action

**Definition.** For $x \in A$ the **adjoint action** of $x$ is

$$
\operatorname{ad}_x(y) = xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx ,
$$

the graded commutator; it is a linear map on $A$ and, for each $x$, an operator on the module by the action of $A$.

**Theorem.** For a homogeneous $x$ the operator $\operatorname{ad}_x$ is a graded derivation of degree $\lvert x\rvert$,

$$
\operatorname{ad}_x(yz) = \operatorname{ad}_x(y)z + (-1)^{\lvert x\rvert\lvert y\rvert}y\operatorname{ad}_x(z) ,
$$

it satisfies the graded Leibniz rule in the variable $x$ with the sign $(-1)^{\lvert y\rvert}$, and it is compatible with the grading by shifting the degree, $\lvert\operatorname{ad}_x(y)\rvert = \lvert x\rvert+\lvert y\rvert$.

**Proof.** Expand $\operatorname{ad}_x(yz) = xyz-(-1)^{\lvert x\rvert(\lvert y\rvert+\lvert z\rvert)}yzx$ and compare with $\operatorname{ad}_x(y)z + (-1)^{\lvert x\rvert\lvert y\rvert}y\operatorname{ad}_x(z) = xyz-(-1)^{\lvert x\rvert\lvert y\rvert}yxz+(-1)^{\lvert x\rvert\lvert y\rvert}yxz-(-1)^{\lvert x\rvert\lvert y\rvert}(-1)^{\lvert x\rvert\lvert z\rvert}yzx$; the middle terms cancel and the last term is $-(-1)^{\lvert x\rvert(\lvert y\rvert+\lvert z\rvert)}yzx$, matching. The degree is immediate from the homogeneity of the product.

**Theorem (the graded Lie structure).** The adjoint action satisfies the graded antisymmetry and the graded Jacobi identity,

$$
\operatorname{ad}_x(y) = -(-1)^{\lvert x\rvert\lvert y\rvert}\operatorname{ad}_y(x), \qquad \operatorname{ad}_x\operatorname{ad}_y - (-1)^{\lvert x\rvert\lvert y\rvert}\operatorname{ad}_y\operatorname{ad}_x = \operatorname{ad}_{\operatorname{ad}_x(y)} ,
$$

so the graded commutator turns $A$ into a **graded Lie algebra** and $\operatorname{ad}$ is a representation of it by graded derivations, with kernel the graded centre $Z_{\mathrm{gr}}(A)$.

**Proof.** The antisymmetry is the definition read twice; the Jacobi identity is the expansion of the graded commutator, the same computation as in the ungraded case with the Koszul signs inserted at each transposition; the kernel is the graded centre because $\operatorname{ad}_x = 0$ means $x$ graded-commutes with every element.

**Proposition (compatibility with an involution).** Let $\sigma$ be an involution of $A$ of degree zero commuting with the grade involution $\alpha$. Then

$$
\operatorname{ad}_x^{*_\sigma} = -\operatorname{ad}_{\delta(x)} , \qquad \delta = \sigma\alpha ,
$$

with respect to the twisted pairing: the adjoint of the adjoint action is the adjoint action of $-\delta(x)$, so the adjoint action is skew-adjoint exactly when $\delta(x) = -x$.

**Proof.** $\operatorname{ad}_x = L_x-(-1)^{\lvert x\rvert\lvert\cdot\rvert}R_x$ is the difference of a signed left and a signed right multiplication, and the signed adjoints of the two are $T_{\delta(x)}$ and the corresponding signed right multiplication by $\delta(x)$, by *The Signed Adjoint of the Left Multiplication on a Ring*; the difference is $-\operatorname{ad}_{\delta(x)}$.

## Examples

**(a) The exterior algebra.** For the exterior algebra of a module with the sign $(-1)^{\lvert x\rvert\lvert y\rvert}$, the adjoint action of a vector $v$ is the contraction-insertion operator $\operatorname{ad}_v(\omega) = v\omega-(-1)^{\lvert\omega\rvert}\omega v$, a graded derivation of degree one; its adjoint is $-\operatorname{ad}_v$ for the natural pairing, so the odd part acts by skew-adjoint operators.

**(b) The Clifford algebra.** With the Clifford product and the grading by degree, the adjoint action of a vector is the commutator $[v,\omega] = v\omega-\omega v$ on the even part and the anti-commutator on the odd part, the sign rule of *Hilbert Algebras*; the adjoint is $-\operatorname{ad}_{\delta(v)}$, and for the dagger of that theory $\delta(v) = -v$, so the adjoint action is self-adjoint.

**(c) The matrix superalgebra.** $A = M_{p|q}$ with the transpose and the grading by blocks: the adjoint action is the graded commutator of matrices, and the Koszul sign appears in the product rule the moment two odd matrices are multiplied.

**(d) The sign rule.** In every case the essential point is the sign: the adjoint of a product is $(-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$, and the graded commutator is $xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx$. Setting the grading trivial, $\lvert a\rvert = 0$ for all $a$, recovers the ungraded adjoint involution and the ordinary commutator of *Involutions of the Endomorphism Ring* and *The Skew Field of a Ring with Involution*.

## Summary

On a graded module over a graded ring the pairing is graded and supersymmetric, $\langle y,x\rangle = (-1)^{\lvert x\rvert\lvert y\rvert}\langle x,y\rangle$, and the adjoint of a homogeneous operator is homogeneous of the same degree with the **Koszul sign rule** $(ST)^{*} = (-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$ for products. The **adjoint action** $\operatorname{ad}_x(y) = xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx$ is a graded derivation of degree $\lvert x\rvert$, it satisfies the graded antisymmetry and the graded Jacobi identity, so the graded commutator makes the ring a graded Lie algebra and $\operatorname{ad}$ a representation of it with kernel the graded centre. With respect to the twisted pairing the adjoint of the adjoint action is $-\operatorname{ad}_{\delta(x)}$ for $\delta = \sigma\alpha$, so the adjoint action is skew-adjoint exactly when $\delta(x) = -x$; when the grading is trivial the whole article reduces to the ungraded adjoint involution and the ordinary commutator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lvert a\rvert$ | Parity of a homogeneous element |
| $(-1)^{\lvert a\rvert\lvert b\rvert}$ | Koszul sign |
| $\langle y,x\rangle=(-1)^{\lvert x\rvert\lvert y\rvert}\langle x,y\rangle$ | Supersymmetric graded pairing |
| $(ST)^{*}=(-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$ | Koszul sign rule for the adjoint |
| $\alpha$ | Grade involution, $a\mapsto(-1)^{\lvert a\rvert}a$ |
| $\operatorname{ad}_x(y)=xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx$ | Adjoint action; graded commutator |
| $\lvert\operatorname{ad}_x(y)\rvert=\lvert x\rvert+\lvert y\rvert$ | Degree shift |
| graded Jacobi | Graded Lie algebra; $\operatorname{ad}_{\operatorname{ad}_x(y)}$ |
| $\operatorname{ad}_x^{*_\sigma}=-\operatorname{ad}_{\delta(x)}$ | Adjoint of the adjoint action |
| $\lvert a\rvert = 0$ | Trivial grading; recovers the ungraded case |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded rings, graded modules and the Koszul sign rule.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the inner derivations and the adjoint representation.
- Matej Brešar, *Introduction to Noncommutative Algebra* (Springer, 2014), for the graded derivations, the adjoint action and the graded Lie structure.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the graded involution and the sign rule in the theory of algebras with involution.
