
# __The Jordan Algebra of Self-Adjoint Elements__

## Introduction

The **self-adjoint** (Hermitian) elements of an ordered involutive algebra form a real vector space $H(A)$ on which the associative product is not commutative and not closed, but the **symmetrised product**

$$
\{h,k\} = \tfrac12(hk + kh)
$$

is commutative and does close; with this product $H(A)$ is a **Jordan algebra**, the Jordan algebra of the self-adjoint elements of $A$. Its **positive cone** is $H(A)\cap A_+$, the set of the self-adjoint elements that are sums of squares, and its **order**, the **Jordan order**, is $h\leq k\iff\{k - h,\ \cdot\ \}\geq0$ for the multiplication operators; the purpose of the article is to show that this order is the order of the involutive algebra and that the symmetrised product is the unique product on the Hermitian part compatible with both the order and the associative product.

The Jordan algebra of the self-adjoint elements is the model of the **JB-algebras**: it satisfies the axioms $\lVert h^{2}\rVert = \lVert h\rVert^{2}$ and the formal reality, its order unit is the identity, its multiplication operators $L_h : k\mapsto\{h,k\}$ are self-adjoint for the trace form, and the Gelfand–Naimark theorem represents it as a Jordan algebra of operators. It is also the structure in which the **spectral theorem** is best stated: the **spectral resolution** of a self-adjoint element is the simultaneous diagonalisation of the commuting Jordan algebra it generates, and the order interval $[0,1]$ is the set of the **effects** of the quantum-mechanical reading.

The Jordan structure with its cone is *Jordan Algebras and the Positive Cone*; the JB-algebras and the Gelfand–Naimark theorem are *JB\*-Algebras and the Gelfand–Naimark Theorem*; the Hermitian elements, the order unit and the Jordan decomposition are *Hermitian Elements and the Order Unit*; the symmetrised product and the Jordan order of the involutive algebra are *The Positive Cone of an Involutive Algebra*; the order is *Ordered Vector Spaces and the Order Unit*; the ordered involutive algebra is *Ordered Involutive Algebras*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; and the positive definite forms are *Positive Definite Forms and the Order*.

## The Self-Adjoint Part is a Jordan Algebra

**Definition.** The **self-adjoint part** of the involutive algebra is $H(A) = \{a : a^{*} = a\}$ with the **symmetrised product** $\{h,k\} = \frac12(hk + kh)$ and the square $h^{2} = \{h,h\}$.

**Theorem (the Jordan axioms).** $H(A)$ is a real Jordan algebra: the symmetrised product is commutative and bilinear, and it satisfies the **Jordan identity**

$$
\{\{h^{2},k\},h\} = \{h^{2},\{k,h\}\} ;
$$

moreover $\{h,k\}$ is self-adjoint for self-adjoint $h,k$, and the unit $1$ is the identity of the Jordan algebra.

*Proof.* The commutativity and the bilinearity are immediate. The Jordan identity is the associativity of the associative product after symmetrisation: expanding both sides in terms of the associated products gives $hh\,kh + kh\,hh$ on each side, using the commutativity of the symmetrisation. The self-adjointness is $(hk + kh)^{*} = k^{*}h^{*} + h^{*}k^{*} = kh + hk$ by the anti-multiplicativity.

**Proposition (the cone and the squares).** The positive cone of the Jordan algebra is

$$
J_+ = H(A)\cap A_+ = \Bigl\{\sum_{i} h_i^{2} : h_i\in H(A)\Bigr\} ,
$$

the set of the sums of squares of the self-adjoint elements; it contains $1 = 1^{2}$, it is closed under addition and nonnegative scaling, and it is pointed when $A$ is reduced.

*Proof.* An element of $H(A)\cap A_+$ is a sum $\sum_i a_i^{*}a_i$ of generators. Each generator $a_i^{*}a_i$ is self-adjoint and positive, and by the spectral resolution it is a sum of squares of self-adjoint elements: if $a_i^{*}a_i = \sum_j\lambda_j p_j$ with $\lambda_j\geq0$, then $a_i^{*}a_i = \sum_j(\sqrt{\lambda_j}\,p_j)^{2}$. Hence every element of $H(A)\cap A_+$ is a sum of squares of self-adjoint elements. Conversely a square $h^{2} = h^{*}h$ lies in $A_+$ and is self-adjoint, so the reverse inclusion holds and the two cones agree. The pointedness is the reducedness of $A$.

**Definition.** The **Jordan order** of $H(A)$ is

$$
h\leq k \iff k - h = \sum_{i} h_i^{2} \ \text{ for some } h_i\in H(A) ,
$$

equivalently $h\leq k\iff k - h\in A_+$.

## The Symmetrised Product and the Order

**Proposition (the order-preserving product).** The symmetrised product is **positive**: if $h\geq0$ and $k\geq0$ then $\{h,k\}\geq0$; and it is compatible with the order in the sense that $\{h,\cdot\}$ is an order-preserving operator for $h\geq0$,

$$
k\geq0 \implies \{h,k\}\geq0 .
$$

*Proof.* The positivity of the symmetrised product is the theorem of *The Positive Cone of an Involutive Algebra*; the operator formulation is the same statement read for the multiplication operator.

**Definition.** The **multiplication operator** of the Jordan algebra is

$$
L_h : H(A)\to H(A), \qquad L_h k = \{h,k\} .
$$

**Proposition (the multiplication operators).** The assignment $h\mapsto L_h$ is linear, and the **Jordan identity is equivalent** to the commuting relation

$$
[L_{h^{2}},L_h] = 0 \quad \text{for every } h ,
$$

that is, the multiplication operator of $h^{2}$ commutes with that of $h$; the operator $L_h$ is self-adjoint for the trace form $\langle h,k\rangle = \operatorname{tr}(hk)$ when $A$ carries a faithful trace; and $L_h\geq0$ if and only if $h\geq0$.

*Proof.* The linearity is immediate. The equivalence of the Jordan identity with $[L_{h^2},L_h]=0$ is the standard operator form of the identity: $(h^{2}k)h = h^{2}(kh)$ in the symmetrised product is exactly $L_{h^{2}}L_h = L_hL_{h^{2}}$. The self-adjointness is the symmetry of the trace, $\operatorname{tr}(h\{k,l\}) = \operatorname{tr}(\{h,k\}l)$, which is the invariance of the trace form; the positivity criterion is the positivity of the symmetrised product.

**Proposition (uniqueness of the product).** The symmetrised product is the unique bilinear product on $H(A)$ that is commutative, has $\{h,h\} = h^{2}$ for every $h$, and is compatible with the associative product in the sense that the operators $L_h$ are the restrictions of the associative multiplications; hence the Jordan structure of the Hermitian part is canonical and is determined by the cone and the order.

*Proof.* The product is determined on the squares by $\{h,h\} = h^{2}$ and in general by the commutativity and the bilinearity through the polarisation $2\{h,k\} = \{h+k,h+k\} - \{h,h\} - \{k,k\} = (h+k)^{2} - h^{2} - k^{2} = hk + kh$, which is the symmetrisation.

## The Jordan Order

**Proposition (the order unit and the Archimedean property).** The identity is the order unit of the Jordan algebra, and the Jordan order is Archimedean in a $\ast$-normed algebra: $0\leq h\leq\lambda1$ for every $\lambda>0$ forces $h = 0$. The norm is the order-unit norm, $\lVert h\rVert = \inf\{\lambda : -\lambda1\leq h\leq\lambda1\}$.

*Proof.* The order unit statement is that of *Hermitian Elements and the Order Unit*; the Archimedean property and the order-unit-norm identity are the corresponding statements of *The Positive Cone of an Involutive Algebra* and *Hermitian Elements and the Order Unit*, read in the Jordan algebra.

**Theorem (the spectral resolution).** Every self-adjoint element $h$ has a **spectral resolution**

$$
h = \sum_{i} \lambda_i\, p_i
$$

with the $\lambda_i$ the real spectral values and the $p_i$ a **Jordan partition of the unit**, the $p_i$ self-adjoint, $\{p_i,p_j\} = 0$ for $i\neq j$, $p_i^{2} = p_i$, and $\sum_i p_i = 1$; the resolution is the diagonalisation of the commutative Jordan algebra generated by $h$, and it gives the functional calculus $f(h) = \sum_i f(\lambda_i)p_i$ for every real function $f$ on the spectrum.

*Proof.* The algebra generated by $h$ is commutative and associative; its Gelfand representation is a space of continuous functions on the spectrum, and the indicator functions of the spectral points pull back to the idempotents $p_i$, which satisfy the displayed relations by the multiplicativity of the representation; the functional calculus is the pullback of $f$.

**Corollary (the order and the spectral resolution).** $h\geq0$ if and only if all the spectral values of $h$ are nonnegative; the positive part and the negative part of the Jordan decomposition are the sums of the spectral pieces with $\lambda_i>0$ and with $\lambda_i<0$; and the order-ideal generated by a positive $h$ is the union $\bigcup_{\lambda>0}[0,\lambda h]$ of the intervals at the positive multiples of $h$.

*Proof.* The spectral resolution exhibits $h$ as a sum of the positive multiples of the idempotents; the positivity of $h$ is therefore equivalent to the positivity of the spectral values; the parts are the indicated sums, and the ideal statement is the definition of the order ideal in a Jordan algebra.

## Worked Cases

### The Self-Adjoint Operators

Let $A = B(H)$. The self-adjoint part with the symmetrised product is a JC-algebra, hence a JB-algebra; the order is the Loewner order, the spectral resolution is the spectral theorem for the self-adjoint operators, and the **effects** are the elements of the order interval $[0,1]$, that is, the self-adjoint contractions. The multiplication operators $L_h$ are the maps $k\mapsto\frac12(hk+kh)$, which are self-adjoint for the Hilbert–Schmidt form; the order ideal generated by the identity is the whole algebra.

### The Hermitian Matrices

Let $A = M_n(\mathbb{C})$. The self-adjoint part $H_n(\mathbb{C})$ with the symmetrised product is the Jordan algebra of the Hermitian matrices; the cone is the positive semidefinite cone, the order is the Loewner order, the spectral resolution is the **spectral decomposition** of a Hermitian matrix, and the Jordan partitions of the unit are the families of the mutually orthogonal projections summing to the identity. This is the finite-dimensional model of the article.

### The Group Algebra

Let $A = \mathbb{C}[G]$ with $g^{*} = g^{-1}$. The self-adjoint part with the symmetrised product is the Jordan algebra of the self-adjoint elements of the group algebra; the order is the order of the Hilbert cone of *The Hilbert Cone of an Involutive Algebra*, and the spectral resolution of a self-adjoint element is the diagonalisation of its **convolution operator** on the group, which is the classical correspondence between the self-adjoint elements and the real-valued functions of the unitary dual in the finite and the compact cases.

## Summary

The **self-adjoint part** $H(A)$ of an involutive algebra, with the **symmetrised product** $\{h,k\} = \frac12(hk+kh)$, is a real **Jordan algebra**; the product is commutative, satisfies the **Jordan identity**, and is the unique product on $H(A)$ compatible with the associative product and with $\{h,h\} = h^{2}$. The **positive cone** is the set of the sums of squares, the **order** is the Jordan order $h\leq k\iff k - h\in A_+$, and the **multiplication operators** $L_h : k\mapsto\{h,k\}$ are self-adjoint for the trace form with $L_h\geq0\iff h\geq0$. The identity is the **order unit**, the order is Archimedean, the norm is the **order-unit norm**, and every self-adjoint element has a **spectral resolution** $h = \sum\lambda_ip_i$ into a **Jordan partition of the unit**, which gives the functional calculus, the criterion $h\geq0\iff\lambda_i\geq0$, and the **Jordan decomposition** into the positive and the negative spectral parts. The model is the self-adjoint part of $B(H)$ with the Loewner order and the effects on the interval $[0,1]$; the finite-dimensional model is the Hermitian matrices. The Jordan structure is *Jordan Algebras and the Positive Cone*; the JB-theory is *JB\*-Algebras and the Gelfand–Naimark Theorem*; the Hermitian elements are *Hermitian Elements and the Order Unit*; the symmetrised product is *The Positive Cone of an Involutive Algebra*; the order is *Ordered Vector Spaces and the Order Unit*; the ordered involution is *Ordered Involutive Algebras*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; and the forms are *Positive Definite Forms and the Order*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{h,k\} = \tfrac12(hk+kh)$ | Symmetrised product |
| $h^{2} = \{h,h\}$ | Square of the Jordan algebra |
| $\{\{h^{2},k\},h\} = \{h^{2},\{k,h\}\}$ | Jordan identity |
| $L_h k = \{h,k\}$ | Multiplication operator |
| $h\leq k\iff k - h\in A_+$ | Jordan order |
| $h = \sum_i\lambda_i p_i$ | Spectral resolution |
| $\{p_i,p_j\} = 0$, $p_i^{2} = p_i$, $\sum p_i = 1$ | Jordan partition of the unit |

## Further Reading

- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the Jordan algebra of the self-adjoint elements, the cone and the order.
- Harald Hanche-Olsen and Erling Størmer, *Jordan Operator Algebras* (Pitman, 1984), for the JB-algebras, the symmetrised product and the spectral theory.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the Jordan order, the effects and the order structure.
- Pascual Jordan, John von Neumann and Eugene Wigner, "On an algebraic generalization of the quantum mechanical formalism", *Annals of Mathematics* **35** (1934), 29–64, for the symmetrised product and the order of the observables.
- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the spectral theorem and the functional calculus.
