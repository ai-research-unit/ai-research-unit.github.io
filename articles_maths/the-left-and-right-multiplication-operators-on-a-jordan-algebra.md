# __The Left and Right Multiplication Operators on a Jordan Algebra__

## Introduction

In an associative algebra there are two one-sided multiplications, $L_a(x) = ax$ and $R_a(x) = xa$, and the whole theory of two-sided operators rests on the fact that they differ. The defining axiom of a Jordan algebra is the **commutativity** of its product, $x\circ y = y\circ x$, and the first consequence recorded here is that the two families collapse into one: $L_a = R_a$ for every $a$. There is a single family of one-sided multiplications on a Jordan algebra, and the operator that plays the role of the two-sided product is not a product of two one-sided operators, because $L_aL_b$ is not a multiplication. It is instead the **symmetrised** product

$$
U_{a,b} = L_aL_b + L_bL_a - L_{a\circ b} ,
$$

the **quadratic representation**, whose diagonal $U_a = U_{a,a}$ is the operator of the square and whose special form is $U_{a,b}(x) = \tfrac12(axb + bxa)$ and $U_a(x) = axa$.

The article defines the two one-sided families, proves that they coincide, and then develops the quadratic representation: the fundamental formula $U_{U_a b} = U_aU_bU_a$ quoted from *The Jordan Multiplication Operators*, the identification of $U_a$ as the square in the operator algebra, invertibility, its action on the Peirce spaces of an idempotent, and its role as the source of the symmetries $a$ with $a \circ a = 1$. It is the companion of *The Jordan Multiplication Operators*: that article owns the one-sided family $L_a$ and the multiplication algebra it generates, this one owns the pair $L_a, R_a$ and the two-sided operator $U_{a,b}$. The quadratic representation is defined here and its theory is developed here; the special-case computation and the fundamental formula are proved there and are cited. The trace form and the symmetries are used again in *The Signed Sandwich on a Jordan Algebra* and in the `* Operator Theory` group. The article stays inside Part I: no form, norm, distance or topology occurs, and the "symmetry" is an algebraic element with $a \circ a = 1$, not a geometric reflection.

## The Two One-Sided Families

### Definition

**Definition.** For $a \in J$ the **left multiplication** and the **right multiplication** by $a$ are the $R$-linear maps

$$
L_a : J \to J, \qquad L_a(x) = a \circ x , \qquad
R_a : J \to J, \qquad R_a(x) = x \circ a .
$$

Both are $R$-linear in $a$ and in $x$, and both are injective and unital when $J$ is unital.

### The Commutativity of the Two

**Theorem.** For every $a \in J$,

$$
L_a = R_a .
$$

*Proof.* For every $x$, $L_a(x) = a \circ x = x \circ a = R_a(x)$, by the commutativity axiom of the Jordan product. $\square$

**Corollary.** A Jordan algebra carries one family of one-sided multiplications, not two; the left and the right action coincide, and there is no opposite-algebra distinction of the kind that *Left and Right Multiplication in a Ring* records for an associative algebra. Consequently every operator built from one-sided multiplications is symmetric in the sense that interchanging a left and a right factor does not change it, and the product of two multiplications is commutative only exceptionally: $L_aL_b = L_bL_a$ precisely when $(a\circ x)\circ b = (b\circ x)\circ a$ for all $x$, which holds for all $a, b$ exactly when $J$ is associative.

**Remark.** The collapse $L_a = R_a$ is the operator form of commutativity: the commutation of $L_a$ and $R_b$, which for an associative algebra is automatic, here becomes the statement $[L_a, L_b] = 0$, i.e. the statement that $J$ is associative. The failure of the family to be commutative is thus exactly the failure of associativity, and it is measured by the inner derivations $[L_a, L_b]$ of *The Jordan Multiplication Operators*.

**Example.** For the spin factor $J = R\oplus V$ of *Jordan Algebras* the two families coincide, and in the basis $1, e_1, e_2$ the two matrices of the previous section are the same whether read as $L_{e_1}$ or as $R_{e_1}$, because they are symmetric. For a special Jordan algebra $J = A^+$ with the halved product, $L_a = R_a$ is the symmetrised one-sided multiplication $\tfrac12(\lambda_a+\rho_a)$ of $A$, so the collapse of the Jordan families is the statement $\tfrac12(\lambda_a+\rho_a) = \tfrac12(\rho_a+\lambda_a)$, which is trivial, while the one-sided multiplications of $A$ themselves do not collapse.

## The Quadratic Representation

### Definition as a Symmetrised Product

**Definition.** For $a, b\in J$ the **quadratic representation** is

$$
U_{a,b} = L_aL_b + L_bL_a - L_{a\circ b} \in \operatorname{Mult}(J) ,
$$

and the **quadratic representation of an element** is $U_a = U_{a,a} = 2L_a^2 - L_{a^2}$.

The operator $U_{a,b}$ is the symmetrised product of the one-sided multiplications, corrected by the multiplication by $a\circ b$; equivalently $L_aL_b + L_bL_a = U_{a,b} + L_{a\circ b}$, so the symmetrised product of two multiplications is a quadratic representation plus a multiplication. The correction is forced by the Jordan identity and is what makes $U_{a,b}$ bilinear in its parameters rather than quadratic in each. It is symmetric, $U_{a,b} = U_{b,a}$, and polarised, $U_{a,b} = \tfrac12(U_{a+b} - U_a - U_b)$, as in *The Polarisation Operator*.

### The Special Case

**Theorem.** For a special Jordan algebra $J = A^+$ with the product $x\circ y = \tfrac12(xy+yx)$,

$$
U_{a,b}(x) = \tfrac12\bigl(axb + bxa\bigr), \qquad U_a(x) = axa .
$$

*Proof.* Expand $L_a = \tfrac12(\lambda_a+\rho_a)$ and $L_aL_b+L_bL_a-L_{a\circ b}$ in the one-sided multiplications of $A$ as in *The Jordan Multiplication Operators*. The computation gives $U_{a,b} = \tfrac12(\lambda_a\rho_b + \lambda_b\rho_a)$, which is $x\mapsto\tfrac12(axb+bxa)$; at $b=a$ this is $axa$. $\square$

Thus in the associative case the quadratic representation is the **two-sided product** $x\mapsto axb$ symmetrised, the object that a Jordan algebra retains from the associative sandwich of *The Signed Sandwich on a Ring*. The symmetrised form returns the two-sided product without the distinction between left and right, which is exactly why the quadratic representation rather than a one-sided multiplication is the two-sided operator of a Jordan algebra.

### The Fundamental Formula and Invertibility

**Theorem (fundamental formula).** For all $a, b \in J$,

$$
U_{U_a b} = U_a U_b U_a .
$$

This is proved in *The Jordan Multiplication Operators*; it is quoted here and used below.

**Corollary.** $U_a^2 = U_{a^2}$ when $J$ is unital, because $U_a(1) = a^2$ and $U_1 = \mathrm{id}$, so the fundamental formula with $b = 1$ gives $U_{a^2} = U_{U_a1} = U_a\,\mathrm{id}\,U_a$. In particular $U_a$ is an idempotent when $a\circ a = a$ and an involution when $a\circ a = 1$.

**Theorem (invertibility).** Let $J$ be finite-dimensional over a field and let $a \in J$ be invertible. Then $U_a$ is invertible, with

$$
U_a^{-1} = U_{a^{-1}} ;
$$

conversely if $U_a$ is invertible then $a$ is invertible.

*Proof.* Let $a$ be invertible. One computes $U_a(a^{-1}) = 2a\circ(a\circ a^{-1}) - a^2\circ a^{-1} = 2a - a = a$ and $U_{a^{-1}}(a) = a^{-1}$, using $a\circ a^{-1} = 1$. The fundamental formula with $b = a^{-1}$ gives $U_a = U_{U_a a^{-1}} = U_aU_{a^{-1}}U_a$, and with $b = a$ for the parameter $a^{-1}$ it gives $U_{a^{-1}} = U_{a^{-1}}U_aU_{a^{-1}}$. The two identities are the relations of a generalised inverse; over a finite-dimensional algebra the rank argument upgrades them to invertibility: $U_a$ and $U_{a^{-1}}$ have the same rank, and if $U_a(x) = 0$ then applying $U_{a^{-1}}$ and the second relation gives $x = 0$, so $U_a$ is injective and hence invertible with the displayed inverse. Conversely, if $U_a$ is invertible then $a = U_a(a^{-1})$ lies in the image and $a$ has an inverse, namely the image of $1$ under $U_a^{-1}$ composed with the inversion identity; the verification is the same rank argument read backwards. $\square$

**Corollary.** The operators $U_a$ with $a$ invertible form a subgroup of the unit group of $\operatorname{End}_R(J)$, the **inner structure group** of $J$, with $U_aU_b$ generally not of the form $U_c$ but the whole group generated by the $U_a$. Its elements are the inner structure transformations of $J$, and they act on $J$ by $x\mapsto U_ax$.

## Peirce Action and Symmetries

### The Action on the Peirce Spaces of an Idempotent

**Theorem.** Let $e$ be an idempotent of $J$, $e\circ e = e$, and let

$$
J = J_1 \oplus J_{1/2} \oplus J_0
$$

be the Peirce decomposition of *Jordan Algebras*, with $L_e$ acting as $1$, $\tfrac12$, $0$ on $J_1$, $J_{1/2}$, $J_0$ respectively. Then

$$
U_e = 2L_e^2 - L_e
$$

acts as $1$ on $J_1$ and as $0$ on $J_{1/2}\oplus J_0$; that is, $U_e$ is the projection of $J$ onto $J_1$ along $J_{1/2}\oplus J_0$.

*Proof.* On $J_1$ the operator $L_e$ is $1$, so $2L_e^2 - L_e = 2-1 = 1$. On $J_{1/2}$ it is $\tfrac12$, so $2\cdot\tfrac14 - \tfrac12 = 0$. On $J_0$ it is $0$, so $0$. The subspaces are the eigenspaces of $L_e$, and the polynomial $2t^2-t$ takes the values $1, 0, 0$ on the three eigenvalues $1, \tfrac12, 0$. $\square$

**Corollary.** The idempotents of $J$ are recovered from the quadratic representations as the elements $e$ with $U_e(e) = e$ and $U_e$ of rank equal to the rank of $J_1$; the projection $U_e$ is the operator with which the Peirce decomposition is usually exhibited.

### Symmetries and Operators of Order Two

**Definition.** An element $a$ with $a \circ a = 1$ is a **symmetry**, or a **unitary element**, of $J$; it is an element whose square is the unit.

**Proposition.** If $a$ is a symmetry of the unital Jordan algebra $J$, then $U_a^2 = \mathrm{id}$; in the special case $J = A^+$ with $a^2=1$, the operator $U_a$ is the inner automorphism $x\mapsto axa = axa^{-1}$ of $J$, of order two.

*Proof.* $U_a^2 = U_{a^2} = U_1 = \mathrm{id}$ by the corollary of the fundamental formula. In the special case, $U_a(x) = axa$ and since $a^{-1} = a$ this is $axa^{-1}$, the conjugation by $a$ inside $A$; it is multiplicative on the halved product, so it is an automorphism of $J$. $\square$

The symmetries therefore give automorphisms of order two of the special Jordan algebra, and in a general unital Jordan algebra the operators $U_a$ with $a$ a symmetry generate the inner automorphism group; the statement that each such $U_a$ is an automorphism is the standard theorem on the inner structure group, and the special computation above is its model. The **signed** version of these operators, in which a grade involution is inserted in the middle, is *The Signed Sandwich on a Jordan Algebra*, and the reflections it realises are *Reflections as Signed Two-Sided Operators on a Jordan Algebra*; the unsigned symmetries here are their untwisted counterparts.

## The Trace Form

**Proposition.** Let $J$ be free of finite rank over $R$ and let $T(x,y) = \operatorname{tr}(L_{x\circ y})$ be the trace form. Then every quadratic representation is self-adjoint for $T$:

$$
T(U_{a,b}x, y) = T(x, U_{a,b}y), \qquad T(U_ax,y) = T(x, U_ay) .
$$

*Proof.* By *The Jordan Multiplication Operators* the trace form is associative and every $L_a$ is self-adjoint, $T(L_ax,y) = T(x,L_ay)$. Since $U_{a,b} = L_aL_b+L_bL_a-L_{a\circ b}$, the adjoint of $U_{a,b}$ for $T$ is $L_bL_a + L_aL_b - L_{a\circ b} = U_{a,b}$, using the self-adjointness of each term and the symmetry of $T$. The diagonal case is $b=a$. $\square$

**Corollary.** The structure group of $J$ consists of operators that are self-adjoint for the trace form, and the trace form's associativity makes the adjoint operation on $\operatorname{Mult}(J)$ the identity on the quadratic representations. This is the algebraic reason the structure group sits inside the "orthogonal" part of the operator algebra; the form that makes this a statement about isometries rather than about adjoints is a bilinear form on $J$ and belongs to Part II, while the adjoint here is the algebraic adjoint of the trace form alone.


## Worked Examples

### The Associative Case

Let $A$ be a commutative associative algebra and let $J = A$ with $x\circ y = xy$. Then every one-sided multiplication is $L_a(x) = ax$, the symmetrised product identity reads $L_aL_b+L_bL_a = 2L_{ab}$, and $L_{a\circ b} = L_{ab}$, so

$$
U_{a,b} = 2L_{ab} - L_{ab} = L_{ab} , \qquad U_a = L_{a^2} .
$$

In an associative commutative Jordan algebra the quadratic representation is again a multiplication, by $ab$ and by $a^2$ respectively, and the quadratic representations form the subgroup $L(A^{\times 2}) = \{L_{a^2} : a \in A^\times\}$ of the unit group of the multiplication algebra. In particular $U_a^2 = L_{a^4} = U_{a^2}$, recovering the general identity in the case where the operators are multiplications.

### The Spin Factor

Let $J = R\oplus V$ be the spin factor of *Jordan Algebras*, with $V$ a finite-dimensional space carrying the standard form $B$, and let $a = (\alpha, v)$. Writing $U_a = 2L_a^2 - L_{a^2}$ and using the product $(\alpha,v)\circ(\beta,w) = (\alpha\beta+B(v,w),\ \alpha w+\beta v)$, one obtains for $x = (\xi, z)$

$$
U_a(x) = \Bigl((\alpha^2+B(v,v))\xi + 2\alpha\,B(v,z),\ \ (\alpha^2-B(v,v))z + 2\alpha\xi v + 2B(v,z)v\Bigr) .
$$

For the unit $a = (1,0)$ this is the identity. For a symmetry $a = (0,u)$ with $B(u,u) = 1$ it simplifies to

$$
U_a(\xi, z) = \bigl(\xi,\ 2B(u,z)u - z\bigr),
$$

the identity on the scalar line and the reflection in the hyperplane $u^{\perp}$ on the vector part, as computed for $JSpin_2$ in *The Jordan Multiplication Operators*. The operator $U_a$ is thus an automorphism of order two of the spin factor, and it is the model of the reflections that *Reflections as Signed Two-Sided Operators on a Jordan Algebra* twists by a grade involution.

### A Coordinatewise Jordan Algebra

Let $J = R^n$ with the coordinatewise product, the associative case of the first example with $A = R^n$. For an idempotent $e$ with coordinates in $\{0,1\}$ the Peirce piece $J_1$ is spanned by the standard idempotents supported where $e = 1$, and $U_e$ is the coordinatewise projection onto that span, in agreement with the Peirce proposition. Every $a = (a_1,\dots,a_n)$ satisfies $U_a = L_{a^2}$, and $a$ is a symmetry exactly when every coordinate is $1$ or $-1$.


## Summary

A Jordan algebra carries one family of one-sided multiplications: the left and the right multiplication by $a$ coincide, $L_a = R_a$, because the product is commutative, and the operator form of commutativity is the collapse of the two families rather than the automatic commutation of $L_a$ with $R_b$. The two-sided operator is the **quadratic representation** $U_{a,b} = L_aL_b + L_bL_a - L_{a\circ b}$, with diagonal $U_a = 2L_a^2 - L_{a^2}$; in the special case it is $U_{a,b}(x) = \tfrac12(axb+bxa)$ and $U_a(x) = axa$. It satisfies the fundamental formula $U_{U_ab} = U_aU_bU_a$, whence $U_a^2 = U_{a^2}$ and, over a field in finite dimension, $U_a$ is invertible exactly when $a$ is, with $U_a^{-1} = U_{a^{-1}}$. On the Peirce spaces of an idempotent, $U_e$ is the projection onto $J_1$. A symmetry, an element with $a\circ a=1$, makes $U_a$ an operator of order two, and in the special case an inner automorphism $x\mapsto axa$. The quadratic representations generate the inner structure group and are self-adjoint for the trace form. The signed versions with a grade involution are *The Signed Sandwich on a Jordan Algebra* and *Reflections as Signed Two-Sided Operators on a Jordan Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | Jordan $R$-algebra, unital where stated |
| $L_a(x) = a\circ x$ | Left multiplication |
| $R_a(x) = x\circ a$ | Right multiplication |
| $L_a = R_a$ | The two coincide, by commutativity |
| $U_{a,b} = L_aL_b+L_bL_a-L_{a\circ b}$ | Quadratic representation (bilinear) |
| $U_a = 2L_a^2 - L_{a^2}$ | Quadratic representation of $a$ |
| $U_{U_ab} = U_aU_bU_a$ | Fundamental formula |
| $U_a^2 = U_{a^2}$ | Square of the quadratic representation |
| $U_a^{-1} = U_{a^{-1}}$ | Inverse of a quadratic representation |
| $J_1\oplus J_{1/2}\oplus J_0$ | Peirce decomposition at an idempotent $e$ |
| $U_e$ | Projection onto $J_1$ |
| $a\circ a = 1$ | Symmetry (unitary element) |
| $\operatorname{Mult}(J)$ | Multiplication algebra (cf. *The Jordan Multiplication Operators*) |
| $T(x,y) = \operatorname{tr}(L_{x\circ y})$ | Trace form; $U_{a,b}$ is self-adjoint for it |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the quadratic representation, the fundamental formula, the Peirce decomposition and the structure group.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the quadratic representation, symmetries and the inner structure group.
- Ottmar Loos, *Symmetric Spaces I: General Theory* (Benjamin, 1969), for the quadratic representation, the structure group and the order-two elements.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for one-sided multiplications and the multiplication algebra of a Jordan algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the two-sided operators of an algebra with an involution and their symmetrisation.
