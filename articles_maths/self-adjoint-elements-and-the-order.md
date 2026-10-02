
# __Self-Adjoint Elements and the Order__

## Introduction

The **self-adjoint elements** of an ordered involutive algebra are the fixed points of the involution, $a = a^{*}$, and they are exactly the elements whose **left multiplication** operators are self-adjoint for the trace form,

$$
(L_a)^{*} = L_{a^{*}} ,
$$

so that $L_a = (L_a)^{*}$ if and only if $a = a^{*}$. The article is the element-level companion of *The Adjoint of a Positive Operator*: the order of the ordered involutive algebra is transported, by the map $a\mapsto L_a$, into the **quadratic order** of the operators, and the transport is an **order isomorphism** on the self-adjoint part,

$$
a\geq0 \iff L_a\geq0 \iff \langle L_ax,x\rangle\geq0 \ \text{ for every } x \iff \varphi(a)\geq0 \ \text{ for every positive functional } \varphi ,
$$

so that the order of the self-adjoint elements, the order of their multiplication operators and the order of the positive functionals are the same order read in three ways. The self-adjointness is what makes the three readings compatible: on a general element the left multiplication is not self-adjoint and the quadratic form need not be real, whereas on the self-adjoint part the quadratic form of $L_a$ is the **real** form $x\mapsto\langle ax,x\rangle$, and its positivity is the positivity of $a$.

The article states the adjoint of the left multiplication, the transport of the order, the correspondence between the self-adjoint elements and the self-adjoint operators, and the extremal order-theoretic facts: the order unit, the Jordan decomposition, the order ideals and the **self-adjointness** of the order isomorphisms. It is thus the bridge between the element theory of *Hermitian Elements and the Order Unit* and the operator theory of *Positive Operators on an Ordered Space*, and it prepares the adjoints of the left multiplications and the signed operators that follow.

The Hermitian elements and the order unit are *Hermitian Elements and the Order Unit*; the adjoint and the order of the operators are *The Adjoint of a Positive Operator*; the positive operators are *Positive Operators on an Ordered Space*; the positive functionals are *The Cone of Positive Functionals* and *Positive Functionals and Self-Adjointness*; the forms are *Positive Definite Forms and the Order*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; the ordered involution is *Ordered Involutive Algebras*; and the concrete adjoints are *The Adjoint of the Left Multiplication on an Ordered Algebra*, *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*.

## The Adjoint of the Left Multiplication

**Definition.** For $a\in A$ the **left multiplication** is $L_a : x\mapsto ax$ and the **right multiplication** is $R_a : x\mapsto xa$; the **trace form** is $\langle x,y\rangle = \operatorname{tr}(x^{*}y)$ when $A$ carries a faithful trace, and the **adjoint** is taken with respect to it.

**Proposition (the adjoint of the one-sided multiplications).** The adjoints of the one-sided multiplications are

$$
(L_a)^{*} = L_{a^{*}}, \qquad (R_a)^{*} = R_{a^{*}} ;
$$

consequently $L_a$ is **self-adjoint** if and only if $a$ is self-adjoint, and the map $a\mapsto L_a$ is a **\*-homomorphism**: $L_{ab} = L_aL_b$ and $L_{a^{*}} = (L_a)^{*}$, so it carries the involution of the algebra to the adjoint involution of the operators.

*Proof.* $\langle L_ax,y\rangle = \operatorname{tr}((ax)^{*}y) = \operatorname{tr}(x^{*}a^{*}y) = \langle x,a^{*}y\rangle = \langle x,L_{a^{*}}y\rangle$, so $(L_a)^{*} = L_{a^*}$; the right-handed computation is the same with the factors in the other order. The \*-homomorphism property is the associativity $L_{ab} = L_aL_b$ together with the adjoint statement.

**Proposition (the decomposition of the left multiplication).** For every $a$ the operator $L_a$ decomposes as

$$
L_a = L_{\operatorname{Re}a} + iL_{\operatorname{Im}a} ,
$$

the sum of two self-adjoint operators, and the symmetrised combination $L_a + L_{a^{*}} = 2L_{\operatorname{Re}a}$ is self-adjoint with the quadratic form $x\mapsto 2\operatorname{Re}\langle ax,x\rangle$; the operator $L_a$ is **normal** exactly when $a$ is normal, $(L_a)^{*}L_a = L_a(L_a)^{*} = L_{a^{*}a}$.

*Proof.* The decomposition is the linearity of $a\mapsto L_a$ and the fact that $\operatorname{Re}a$, $\operatorname{Im}a$ are self-adjoint; the quadratic form is the computation $\langle (L_a + L_{a^*})x,x\rangle = \langle ax,x\rangle + \langle x,ax\rangle = 2\operatorname{Re}\langle ax,x\rangle$; the normality is the \*-homomorphism property applied to $a^{*}a = aa^{*}$.

## The Order of the Self-Adjoint Elements

**Theorem (the order of the self-adjoint elements is the order of their operators).** For self-adjoint $a,b$ the following are equivalent:

$$
\text{(i)} \ a\leq b ; \quad \text{(ii)} \ L_{b-a}\geq0 ; \quad \text{(iii)} \ \langle (b-a)x,x\rangle\geq0 \ \text{ for every } x ; \quad \text{(iv)} \ \varphi(b-a)\geq0 \ \text{ for every positive functional } \varphi ,
$$

so the map $a\mapsto L_a$ is an **order isomorphism** of the self-adjoint part onto its image in the self-adjoint operators, and the order of the elements is the **quadratic order** of the multiplication operators.

*Proof.* The equivalence (i) $\iff$ (iv) is the theorem that the order is the intersection of the forms of *Positive Definite Forms and the Order*; (i) $\iff$ (iii) is the quadratic form of $L_{b-a}$ computed at $x$: $\langle (b-a)x,x\rangle = \langle L_{b-a}x,x\rangle$ for the trace form; (ii) $\iff$ (iii) is the definition of the positivity of an operator. Hence the four conditions are equivalent, and the transport is an order isomorphism because it is injective (the algebra is faithful) and preserves the order in both directions.

**Corollary (the positivity of an element and of its multiplication).** An element is positive if and only if its left multiplication is positive, and if and only if its right multiplication is positive,

$$
a\geq0 \iff L_a\geq0 \iff R_a\geq0 ;
$$

the map $a\mapsto L_a$ carries the order unit to the identity operator, the Jordan decomposition to the decomposition of $L_a$ into self-adjoint parts, and the order interval $[0,1]$ to the interval $[0,L_1] = [0,I]$ of the multiplication operators.

*Proof.* The equivalences are the theorem with $b - a = a$ and $a = 0$; the order unit is carried to $L_1 = I$; the Jordan decomposition is the spectral decomposition transported by the \*-homomorphism; the interval statement is the order isomorphism applied to $[0,1]$.

**Proposition (self-adjointness and the order isomorphisms).** An order isomorphism of the self-adjoint part that commutes with the adjoint is a **self-adjoint order isomorphism**, and the order isomorphisms induced by the \*-automorphisms of the algebra are exactly the order isomorphisms of the form $L_a\circ R_{a^{-1}}$ for a unitary $a$ for which the conjugation is a \*-automorphism; the identity component of these is the group of the inner \*-automorphisms, and the order is preserved by the action.

*Proof.* A \*-automorphism $\Phi$ of the algebra induces the order isomorphism $T\mapsto\Phi T\Phi^{-1}$ on the operators, and its restriction to the self-adjoint part is an order isomorphism commuting with the adjoint, which is the definition of a **self-adjoint order isomorphism**; the inner ones are the conjugations $L_aR_{a^{-1}}$ with $a^* = a^{-1}$, which is the unitarity, and this conjugation is a \*-automorphism exactly when it commutes with the involution, which holds for the unitaries of the connected component.

## The Order and the Self-Adjoint Operators

**Proposition (the self-adjoint operators are an ordered space).** The self-adjoint operators on the space with the trace form form a real ordered vector space under the quadratic order, with the identity as order unit and the order-unit norm equal to the operator norm; the map $a\mapsto L_a$ is an order isomorphism of the self-adjoint part onto a subalgebra of this space, and it is **isometric** for the order-unit norms when the algebra is a $\ast$-normed algebra.

*Proof.* The ordered-space structure is that of *The Adjoint of a Positive Operator*; the order-unit norm is the operator norm; the map $L$ is an isometric order isomorphism on the self-adjoint part by the \*-homomorphism and the order-isomorphism properties together.

**Corollary (the self-adjointness of the order).** The order of the ordered involutive algebra is **self-adjoint** in the sense that it is determined by the self-adjoint operators, and every order statement has a self-adjoint operator form: $a\geq0$ if and only if $L_a$ is a positive operator, $a$ is an order unit if and only if $L_a$ is an order unit of the multiplication algebra, and the order ideals of the algebra correspond to the order ideals of the multiplication algebra.

*Proof.* The statements are the transport of the order-theoretic notions by the order isomorphism; the correspondence of the ideals is the definition of an order isomorphism in the ordered-vector-space sense.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the trace form. The self-adjoint elements are the Hermitian matrices, the left multiplication $L_A(B) = AB$ has the adjoint $L_{A^{*}}$, and the order is the Loewner order; the self-adjoint elements correspond to the self-adjoint left multiplications, and the positivity of $A$ is the positivity of $L_A$ as an operator on the Hilbert space of the matrices. This is the finite-dimensional model.

### The Self-Adjoint Operators

Let $A$ be a von Neumann algebra of operators, self-adjoint elements its self-adjoint operators; the left multiplication is the operator $T\mapsto AT$, its adjoint is the multiplication by $A^{*}$, and the order is the Loewner order of the multiplication operators; the self-adjoint part of the algebra is an ordered vector space isomorphic to the corresponding operators. The effects $[0,I]$ are the order interval of the algebra's order unit.

### The Continuous Functions

Let $A = C(X,\mathbb{C})$ with the pointwise order and the $L^{2}$ trace form. The self-adjoint elements are the real-valued functions, the left multiplication is the multiplication by the function, its adjoint is the multiplication by the complex conjugate function, and the order is pointwise; the order isomorphism $f\mapsto L_f$ carries the pointwise order to the order of the multiplication operators, and the order unit is the constant function $1$.

## Summary

For an ordered involutive algebra the **adjoint of the left multiplication** is $(L_a)^{*} = L_{a^{*}}$, so the left multiplication is self-adjoint exactly on the **self-adjoint elements**, and the map $a\mapsto L_a$ is a **\*-homomorphism**. The order of the self-adjoint elements is the **quadratic order** of their operators: $a\leq b$ if and only if $L_{b-a}\geq0$, equivalently $\langle(b-a)x,x\rangle\geq0$ for every $x$, equivalently $\varphi(b-a)\geq0$ for every positive functional $\varphi$; hence $a\mapsto L_a$ is an **order isomorphism** of the self-adjoint part onto its image, carrying the order unit to the identity, the Jordan decomposition to the decomposition into self-adjoint parts, and the order interval $[0,1]$ to $[0,I]$. The isometric order isomorphisms are the \*-automorphisms conjugate by the unitaries, the **self-adjoint order isomorphisms**, and the order is **self-adjoint**: every order statement has a self-adjoint operator form. The Hermitian elements are *Hermitian Elements and the Order Unit*; the adjoint and the order are *The Adjoint of a Positive Operator*; the positive operators are *Positive Operators on an Ordered Space*; the functionals are *The Cone of Positive Functionals* and *Positive Functionals and Self-Adjointness*; the forms are *Positive Definite Forms and the Order*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; and the concrete adjoints are *The Adjoint of the Left Multiplication on an Ordered Algebra*, *The Signed Adjoint Sandwich on an Ordered Algebra*, *The Signed Adjoint of the Reflection on an Ordered Algebra* and *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a x = ax$, $R_a x = xa$ | One-sided multiplications |
| $(L_a)^{*} = L_{a^{*}}$, $(R_a)^{*} = R_{a^{*}}$ | Adjoints of the multiplications |
| $L_{ab} = L_aL_b$ | The map $a\mapsto L_a$ is a homomorphism |
| $a\leq b\iff L_{b-a}\geq0$ | The order of the self-adjoint elements |
| $\langle(b-a)x,x\rangle\geq0$ | Quadratic form of the order |
| $L_1 = I$ | Order unit carried to the identity |
| Self-adjoint order isomorphism | Order isomorphism commuting with the adjoint |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the left multiplications, the adjoints and the order of an operator algebra.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the \*-automorphisms, the inner automorphisms and the order.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the quadratic order, the order isomorphisms and the order-unit norms.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the self-adjoint operators, the order and the normal states.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the order isomorphisms and the self-adjoint structure.
