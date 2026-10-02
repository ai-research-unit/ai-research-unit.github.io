
# __The Adjoint of a Positive Operator__

## Introduction

On an ordered space with a **positive definite form** — the trace form $\langle x,y\rangle$ of an ordered involutive algebra, or the inner product of an ordered Hilbert space — every linear operator $T$ has an **adjoint** $T^{*}$ with $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$, and the adjoint interacts with the order in a way that mirrors the positivity: the adjoint of a **positive operator** is positive,

$$
T\geq0 \implies T^{*}\geq0 ,
$$

where $T\geq0$ means $\langle Tx,x\rangle\geq0$ for every $x$, equivalently $T$ order preserving on the positive cone when the cone is self-dual. The adjoint is an **order isomorphism** of the operator space for the order of the forms, the map $T\mapsto T^{*}$ is an involution that reverses the products, $(ST)^{*} = T^{*}S^{*}$, and the self-adjoint operators $T = T^{*}$ form the ordered real subspace on which the order of the operators is the concrete order of the article. The purpose of the article is to state the adjoint and the order together: the adjoint is the algebraic expression of the self-duality of the form, and the positivity is preserved by it.

The article is the first of the **adjoint** family of the `- * Operator Theory` group: the adjoint of a single operator is followed by the adjoint of the left multiplication, of the signed sandwich, of the reflection and of the graded action, each of which is a concrete computation of the general adjoint displayed here. The order enters twice: through the **positivity of the adjoint** and through the **order of the self-adjoint operators**, in which the operators are compared by their quadratic forms. The commutative and the matrix cases exhibit the two behaviours: the pointwise adjoint is the ordinary adjoint of a function, and the matrix adjoint is the conjugate transpose, both manifestly preserving the positivity.

The ordered space and the order are *Ordered Vector Spaces and the Order Unit*; the positive operators are *Positive Operators on an Ordered Space*; the forms and the self-duality are *Positive Definite Forms on an Ordered Space* and *Positive Definite Forms and the Order*; the Hilbert cone and the self-duality are *The Hilbert Cone of an Involutive Algebra*; the self-adjoint elements are *Self-Adjoint Elements and the Order*; the involution on the order automorphisms is *The Involution on the Order Automorphisms*; the adjoint of the left multiplication is *The Adjoint of the Left Multiplication on an Ordered Algebra*; and the signed adjoints are *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*. The operator-algebraic models are *Operator Algebras* and *The Hilbert Space Adjoint* of Part II.

## The Adjoint and the Form

**Definition.** Let $E$ be a real or complex vector space with a positive definite form $\langle\cdot,\cdot\rangle$ (the trace form in the involutive-algebra case), and let $T : E\to E$ be linear. The **adjoint** is the linear map $T^{*}$ with

$$
\langle Tx,y\rangle = \langle x,T^{*}y\rangle \quad \text{for every } x,y\in E .
$$

**Proposition (the adjoint is an involution reversing the products).** When the adjoints exist, the map $T\mapsto T^{*}$ is conjugate-linear, is an involution $(T^{*})^{*} = T$, reverses the products, $(ST)^{*} = T^{*}S^{*}$, and fixes the identity, $I^{*} = I$; the **self-adjoint** elements are the fixed points $T = T^{*}$, they form a real vector space, and every operator decomposes as $T = \operatorname{Re}T + i\operatorname{Im}T$ with $\operatorname{Re}T = \frac12(T + T^{*})$ and $\operatorname{Im}T = \frac1{2i}(T - T^{*})$ self-adjoint.

*Proof.* The conjugate-linearity and the order-two property are immediate from the definition; the reversal of the products follows from $\langle STx,y\rangle = \langle Tx,S^{*}y\rangle = \langle x,T^{*}S^{*}y\rangle$; the identity is self-adjoint, and the decomposition is the same computation as for the Hermitian elements of an involutive algebra.

**Example.** For the matrix algebra with the trace form the adjoint is the conjugate transpose, $T^{*} = \bar T^{\mathsf{T}}$; for the function algebra with the $L^{2}$ form it is the complex conjugate; for the Hilbert space it is the operator adjoint. In all three the involution is the one of the involutive-algebra structure, and the adjoint of the multiplication $L_a$ is $L_{a^{*}}$.

## The Positivity of the Adjoint

**Definition.** An operator $T$ is **positive**, $T\geq0$, when $\langle Tx,x\rangle\geq0$ for every $x$; it is **order preserving** when it maps the positive cone into itself, $T(E_+)\subseteq E_+$.

**Theorem (the adjoint preserves the positivity and the order).** The adjoint of a positive operator is positive,

$$
T\geq0 \implies T^{*}\geq0 ,
$$

so the adjoint is an **order isomorphism** of the operator space for the order $\leq$ defined by the quadratic forms; when the cone is self-dual for the form the quadratic positivity coincides with the order preservation, and then the adjoint of an order-preserving operator is order preserving. The adjoint of an order **isomorphism** is an order isomorphism, and the positivity is therefore an invariant of the adjoint.

*Proof.* If $T\geq0$ then $\langle Tx,x\rangle$ is real and nonnegative for every $x$; the Hermitian symmetry of the form gives $\langle T^{*}x,x\rangle = \overline{\langle x,T^{*}x\rangle} = \overline{\langle Tx,x\rangle} = \langle Tx,x\rangle\geq0$, so the quadratic forms of $T$ and $T^{*}$ agree and both operators are positive. The order-preservation statement is the definition of the self-duality, under which $\langle Tx,x\rangle\geq0$ for all $x$ is equivalent to $T(E_+)\subseteq E_+$; the order-isomorphism statement is the two-sided preservation.

**Corollary (the quadratic order and the operator order).** The operators are ordered by their quadratic forms,

$$
S\leq T \iff \langle Sx,x\rangle\leq\langle Tx,x\rangle \ \text{ for every } x ,
$$

and the adjoint is an order isomorphism of this order; the self-adjoint operators of the form $T = T^{*}$ form an ordered real vector space with the order interval $[0,I]$ the set of the positive contractions, which is the order of the **effects** when the space is a Hilbert space.

*Proof.* The order is defined by the quadratic forms and is a cone order because the set of the positive quadratic forms is a cone; the adjoint preserves it by the theorem; the self-adjoint part with this order is the ordered space whose interval at $I$ is the set of the contractions, by the standard argument of *Positive Operators on an Ordered Space*.

## The Order Automorphisms and the Adjoint

**Proposition (the adjoint of an order automorphism).** If $T$ is an order automorphism of the ordered space with the form and $T^{-1} = T^{*}$ (an orthogonal automorphism), then $T$ preserves the quadratic positivity; the adjoint of an order automorphism is an order automorphism, and the group of the order automorphisms that are isometric for the form is closed under the adjoint.

*Proof.* The invariance of the form under an orthogonal $T$ gives $\langle Tx,Ty\rangle = \langle x,y\rangle$, so the quadratic order is preserved; the adjoint of a bijective order-preserving map is order preserving by the two-sided statement of the theorem; the group is closed under the adjoint because the inverse and the adjoint coincide on the orthogonal automorphisms.

**Proposition (the involution and the positivity of the automorphisms).** The **involution** of the ordered involutive algebra acts on the order automorphisms by the conjugation

$$
T\mapsto \alpha\,T\,\alpha^{-1} = \alpha T\alpha ,
$$

and the positive automorphisms are carried to positive automorphisms; the fixed points are the automorphisms commuting with the involution, which are the **\*-automorphisms** of the ordered involutive structure. This is the conjugation action of *The Involution on the Order Automorphisms*, of which the present article displays the adjoint form.

*Proof.* The conjugation by an order automorphism $\alpha$ carries the cone to itself, so it carries an order automorphism to an order automorphism; it preserves the positivity because $\alpha$ and $\alpha^{-1}$ preserve the cone; the fixed points are the automorphisms with $\alpha T = T\alpha$, the \*-automorphisms.

## Worked Cases

### The Matrix Algebra

Let $E = M_n(\mathbb{C})$ with the trace form $\langle T,S\rangle = \operatorname{tr}(S^{*}T)$. The adjoint is the conjugate transpose, a positive matrix has a positive conjugate transpose, and the order of the self-adjoint matrices is the Loewner order; the order automorphisms are the unitary conjugations, all of which are orthogonal for the trace form, and the involution on them is the conjugation by $\operatorname{diag}(1,-1)$ in the graded cases of the earlier articles. This is the model instance.

### The Hilbert Space

Let $E = H$ a Hilbert space with its inner product. The operators are the bounded operators on $H$, the adjoint is the Hilbert-space adjoint, the positive operators are the positive semidefinite ones, and the order is the Loewner order; the order automorphisms are the unitary and the antiunitary bijections, and the positivity of the adjoint is the standard fact $\langle T^{*}x,x\rangle = \langle Tx,x\rangle$ for the real part. The effects $[0,I]$ are the quantum-mechanical yes–no measurements.

### The Continuous Functions

Let $E = L^{2}(X,\mu)$ with the pointwise order and the $L^{2}$ form. The multiplication by a nonnegative function is a positive operator, its adjoint is the multiplication by the same function and is positive, and the order is the pointwise order of the functions; the order automorphisms are the multiplications by the functions of modulus one, which are unitary for the form, and the adjoint of the multiplication operator is the multiplication by the conjugate function. The commutative case is the simplest instance in which the adjoint and the order are both pointwise.

## Summary

The **adjoint** of an operator on a space with a positive definite form is defined by $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$; it is conjugate-linear, is an involution, reverses the products, and fixes the identity, and the **self-adjoint** operators are its fixed points, forming an ordered real vector space under the **quadratic order** $S\leq T\iff\langle Sx,x\rangle\leq\langle Tx,x\rangle$. The adjoint **preserves the positivity**, $T\geq0\implies T^{*}\geq0$, because the quadratic forms of $T$ and $T^{*}$ agree; consequently it is an **order isomorphism** of the operator space, the adjoint of an order automorphism is an order automorphism, and the orthogonal automorphisms are closed under the adjoint. The involution of the ordered involutive algebra acts on the order automorphisms by the conjugation $T\mapsto\alpha T\alpha$, whose fixed points are the **\*-automorphisms**; the models are the conjugate transpose on the matrix algebra, the Hilbert-space adjoint, and the pointwise conjugation on $L^{2}$. The order is *Ordered Vector Spaces and the Order Unit*; the positive operators are *Positive Operators on an Ordered Space*; the forms are *Positive Definite Forms on an Ordered Space* and *Positive Definite Forms and the Order*; the self-duality is *The Hilbert Cone of an Involutive Algebra*; the self-adjoint elements are *Self-Adjoint Elements and the Order*; the involution on the automorphisms is *The Involution on the Order Automorphisms*; and the concrete adjoints are *The Adjoint of the Left Multiplication on an Ordered Algebra*, *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$ | Adjoint |
| $(ST)^{*} = T^{*}S^{*}$ | The adjoint reverses the products |
| $T^{*} = T$ | Self-adjoint operator |
| $T\geq0$ | Positive operator, $\langle Tx,x\rangle\geq0$ |
| $T\geq0\implies T^{*}\geq0$ | The adjoint preserves the positivity |
| $S\leq T\iff\langle Sx,x\rangle\leq\langle Tx,x\rangle$ | Quadratic order |
| $T\mapsto\alpha T\alpha$ | Involution on the order automorphisms |
| $[0,I]$ | Effects |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the Hilbert-space adjoint, the positive operators and the order.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the positive operators and the order isomorphism of an operator space.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the \*-automorphisms and the conjugation by the involutions.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the order automorphisms, the effects and the state spaces.
- Béla Sz.-Nagy, *Spektraldarstellung linearer Transformationen des Hilbertschen Raumes* (Springer, 1942), for the adjoint, the self-adjoint operators and the quadratic order.
