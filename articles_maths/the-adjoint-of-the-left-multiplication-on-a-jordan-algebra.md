# __The Adjoint of the Left Multiplication on a Jordan Algebra__

## Introduction

A finite-dimensional Jordan algebra carries the **trace form** $T(x,y) = \operatorname{tr}(L_{x\bullet y})$, the trace of the multiplication by the product; it is symmetric, and it is **associative** in the sense

$$
T(x\bullet y, z) = T(x, y\bullet z) \qquad \text{that is} \qquad T(L_xy, z) = T(y, L_xz) ,
$$

which is the invariance of the trace under the associativity of the multiplication algebra. The associativity of the trace form says that **the left multiplication is self-adjoint** with respect to it: the adjoint of $L_x$ is $L_x$ itself,

$$
L_x^{\dagger} = L_x .
$$

This is the Jordan-algebra counterpart of the familiar adjointness of the left and right multiplications in an associative algebra, and it is the reason the trace form is the natural pairing in the structure theory of a Jordan algebra: the multiplications, and with them the quadratic representations $U_x = 2L_x^2-L_{x^2}$, are self-adjoint.

The article defines the trace form, proves its symmetry and its associativity, deduces the self-adjointness of every left multiplication and of every polynomial in the multiplications, and describes the **symmetries**: the quadratic representation $U_x$ is self-adjoint, and for invertible $x$ the operator $U_x$ is invertible with $U_x^{-1} = U_{x^{-1}}$, so the automorphisms of the form that it generates are the symmetries of the algebra. It then describes the induced adjoint involution on the endomorphism algebra, its self-adjoint part — which contains the multiplication algebra and its polynomial closure — and the quadratic operators. The comparison with the associative case is *Adjoints in a Commutative Involutive Algebra*, where the left and the right multiplications are mutual adjoints; in the Jordan case the two multiplications coincide because the product is commutative, and the common operator is self-adjoint.

The article assumes *Jordan Algebras* for the product $\bullet$, the left multiplication and the quadratic representation, *The Operators on an Algebra* for the multiplication algebra, *The Adjoint of an Endomorphism* for the adjoint with respect to a bilinear pairing, *Involutive Linear Algebras* for the involution of the endomorphism algebra, and *Commutative Algebras with an Involution* for the comparison with the associative case. The signed variants are *The Signed Adjoint Sandwich*, *The Signed Adjoint of the Reflection* and *The Signed Adjoint of the Left Multiplication*, in this group; the forms and the positivity of the trace form are Part II. Throughout, $F$ is a field with $2 \ne 0$, $J$ is a finite-dimensional unital Jordan algebra over $F$, $L_x$ is the left multiplication, $U_x = 2L_x^2-L_{x^2}$ is the quadratic representation, and $T$ is the trace form; no norm, distance, positivity or operator spectrum occurs.

## The Trace Form of a Jordan Algebra

### Definition and Symmetry

**Definition.** The **trace form** of a finite-dimensional Jordan algebra $J$ is

$$
T : J\times J\to F, \qquad T(x,y) = \operatorname{tr}(L_{x\bullet y}),
$$

the trace of the multiplication by the product in the finite-dimensional $F$-linear space $J$.

**Proposition.** The trace form is symmetric and $F$-bilinear; it is non-degenerate when $J$ is semisimple, in which case the pairing is a reflexive pairing in the sense of *The Adjoint of an Endomorphism*.

*Proof.* $T(x,y) = \operatorname{tr}(L_{x\bullet y}) = \operatorname{tr}(L_{y\bullet x}) = T(y,x)$ by the commutativity of $\bullet$; bilinearity is the bilinearity of the trace of a bilinear expression; the non-degeneracy for a semisimple Jordan algebra is standard. $\square$

### Associativity of the Trace Form

**Theorem.** The trace form is **associative**: for all $x, y, z \in J$

$$
T(x\bullet y, z) = T(x, y\bullet z) , \qquad \text{equivalently} \qquad T(L_xy, z) = T(y, L_xz) .
$$

*Proof.* By the **linearised Jordan identity** the operator $L_{(x\bullet y)\bullet z}-L_{x\bullet(y\bullet z)}$ is a sum of commutators of the left multiplications $L_x, L_y, L_z$; the trace of a commutator vanishes, so $\operatorname{tr}(L_{(x\bullet y)\bullet z}) = \operatorname{tr}(L_{x\bullet(y\bullet z)})$, which is the displayed associativity. Equivalently, the multiplication algebra is associative and the trace of a product is invariant under the cyclic permutation of its factors, by which both sides equal $\operatorname{tr}(L_xL_yL_z)$. $\square$

**Corollary.** The trace form is invariant under the multiplications, $T(x\bullet y,z) = T(x,y\bullet z)$; it is therefore an associative symmetric bilinear structure on $J$, and every left multiplication is self-adjoint for it, in the sense of the invariant pairings of *Adjoints in a Commutative Involutive Algebra*.

## The Adjoint of the Left Multiplication

### Self-Adjointness

**Theorem.** For every $x \in J$ the adjoint of the left multiplication with respect to the trace form is the left multiplication itself:

$$
L_x^{\dagger} = L_x .
$$

*Proof.* The associativity of $T$ reads $T(L_xy,z) = T(y,L_xz)$ for all $y, z$, which is exactly the defining relation $T(L_xy,z) = T(y,L_x^{\dagger}z)$ of the adjoint; the adjoint is unique by the non-degeneracy, so $L_x^{\dagger} = L_x$. $\square$

**Corollary.** Every polynomial in the left multiplications, $P(L_{x_1},\dots,L_{x_k})$, is self-adjoint; in particular the square $L_x^2$, the product $L_xL_y+L_yL_x$ symmetric in $x,y$, and every element of the multiplication algebra generated by the $L_x$ are self-adjoint operators.

*Proof.* If $A, B$ are self-adjoint then $A+B$ and $AB+BA$ are self-adjoint, since $(AB+BA)^{\dagger} = B^{\dagger}A^{\dagger}+A^{\dagger}B^{\dagger} = BA+AB$; the multiplication algebra is generated by the $L_x$ under sums and symmetrised products. $\square$

### The Quadratic Representation

**Theorem.** The quadratic representation is self-adjoint, $U_x^{\dagger} = U_x$; for invertible $x$ it is invertible with

$$
U_x^{-1} = U_{x^{-1}} , \qquad (U_x^{-1})^{\dagger} = U_x^{-1} ,
$$

and the map $U : x\mapsto U_x$ defines the symmetries of the algebra.

*Proof.* $U_x = 2L_x^2-L_{x^2}$ is a polynomial in the self-adjoint operators $L_x$ and $L_{x^2}$, hence self-adjoint by the corollary. The inverse formula $U_x^{-1} = U_{x^{-1}}$ is the standard invertibility criterion of the quadratic representation; the adjoint of the inverse is the inverse of the adjoint, so $U_x^{-1}$ is self-adjoint. $\square$

**Corollary (the symmetries).** The automorphisms of $J$ of the form $U_x$ for invertible $x$ are the **symmetries**; they preserve the trace form, $T(U_xy, U_xz) = T(y,z)$, and they generate the structure group. The inner automorphisms so obtained are the maps by which the Jordan algebra is reflected at the element $x$.

*Proof.* $U_x$ is self-adjoint and invertible and thus an isometry of the non-degenerate form $T$ on the invertible elements by the standard computation $T(U_xy,U_xz) = T(y,U_xU_xz)$; the structure group of a Jordan algebra is generated by the $U_x$. $\square$

## The Self-Adjoint Operators and the Involution

**Theorem.** The assignment $F\mapsto F^{\dagger}$ is an involution of the endomorphism algebra $\operatorname{End}_F(J)$ of the trace form; the self-adjoint operators form a Jordan algebra under the symmetrised product and the skew-adjoint operators a Lie algebra under the commutator, with $\operatorname{End}_F(J) = \operatorname{End}_F(J)^+\oplus\operatorname{End}_F(J)^-$ when $2$ is invertible. The multiplication algebra $\operatorname{Mult}(J)$ is contained in the self-adjoint part, and so is its polynomial closure.

*Proof.* The involution property is *The Adjoint of an Endomorphism*; the Jordan and the Lie structures are *Involutive Linear Algebras*; the inclusion of the multiplications in the self-adjoint part is the self-adjointness of the $L_x$; the polynomial closure is closed under the symmetrised product. $\square$

## Examples

**Example (the symmetric matrices).** Let $J = H_n(F)$ be the Jordan algebra of the symmetric matrices with $x\bullet y = \tfrac12(xy+yx)$. The trace form is a nonzero multiple of the ordinary trace pairing, $T(x,y) = c\,\operatorname{tr}(xy)$, and every $L_x$ is self-adjoint; the quadratic representation $U_x(y) = xyx$ is self-adjoint, and for the invertible $x$ it is a symmetry. The self-adjoint part of $\operatorname{End}_F(J)$ contains the multiplication algebra of the symmetric matrices.

**Example (the scalar algebra).** For $J = F$ the trace form is $T(x,y) = xy$ and $L_x = U_x$ is the multiplication by $x$, self-adjoint; the symmetries are the nonzero scalars acting by $x\mapsto x^2 y$, and the adjoint involution is the identity on $\operatorname{End}_F(F)\cong F$.

## Summary

The **trace form** $T(x,y) = \operatorname{tr}(L_{x\bullet y})$ of a finite-dimensional Jordan algebra is symmetric and **associative**, $T(x\bullet y,z) = T(x,y\bullet z)$, and therefore the **left multiplication is self-adjoint**: $L_x^{\dagger} = L_x$. Every polynomial in the left multiplications is self-adjoint, and in particular the **quadratic representation** $U_x = 2L_x^2-L_{x^2}$ is self-adjoint, with $U_x^{-1} = U_{x^{-1}}$ for invertible $x$; the operators $U_x$ are the **symmetries**, they preserve the trace form and they generate the structure group. The adjoint involution of the endomorphism algebra has the multiplication algebra and its polynomial closure inside its self-adjoint part, which is a Jordan algebra under the symmetrised product. The symmetric matrices and the scalar algebra are the worked examples. No norm, distance, positivity or operator spectrum occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | Finite-dimensional unital Jordan algebra |
| $x\bullet y$ | Jordan product |
| $L_xy = x\bullet y$ | Left multiplication |
| $T(x,y) = \operatorname{tr}(L_{x\bullet y})$ | Trace form |
| $T(x\bullet y,z) = T(x,y\bullet z)$ | Associativity of the trace form |
| $L_x^{\dagger} = L_x$ | Self-adjointness of the left multiplication |
| $U_x = 2L_x^2-L_{x^2}$ | Quadratic representation, self-adjoint |
| $U_x^{-1} = U_{x^{-1}}$ | Symmetry at an invertible element |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the trace form, the associativity and the self-adjointness of the multiplications.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the quadratic representation, the symmetries and the structure group.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the trace forms and the multiplication algebras.
- Hel Braun and Max Koecher, *The Jordan Algebra Approach to Bounded Symmetric Domains* (Springer, 1966), for the trace form, the symmetries and the structure theory.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions, the adjoints and the symmetries.
