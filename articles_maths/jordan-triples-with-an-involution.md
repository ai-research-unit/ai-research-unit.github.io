# __Jordan Triples with an Involution__

## Introduction

A **Jordan triple system** is an $R$-module $T$ with a trilinear ternary product $\{\cdot,\cdot,\cdot\} : T^3\to T$ that is symmetric in the outer two variables and satisfies the Jordan triple identity; the ternary product is the symmetrised form of the binary Jordan product, since a Jordan algebra $J$ with product $\bullet$ becomes a Jordan triple under $\{x,y,z\} = (x\bullet y)\bullet z+(z\bullet y)\bullet x-(x\bullet z)\bullet y$. A **Jordan triple with an involution** is such a system together with a **conjugate-linear involution** $\sigma$ of order two that preserves the ternary product,

$$
\sigma\{x,y,z\} = \{\sigma(x),\sigma(y),\sigma(z)\}, \qquad \sigma^2 = \mathrm{id}, \qquad \sigma(\lambda x) = \varsigma(\lambda)\sigma(x),
$$

$\varsigma$ being an involution of the scalars. The map $\sigma$ is the triple analogue of the involution of a Jordan algebra of *Jordan Algebras with an Involution*: the binary picture is recovered by choosing a Jordan algebra and reading its involution, and the **self-adjoint** elements, those with $\sigma(x) = x$, form the **fixed subtriple** $H(T)$. The purpose of this article is to develop that analogue: the fixed subtriple is itself a Jordan triple, the system decomposes as $T = H(T)\oplus iH(T)$ over a quadratic extension, and the structure of $T$ descends to $H(T)$ by the same functors as for an algebra.

After the definitions the article proves that a $\varsigma$-semilinear involution of a Jordan triple is an automorphism of the ternary structure and that the fixed set is a sub-triple; it specialises to the triple of a Jordan algebra with involution, where the fixed subtriple is the triple of the self-adjoint part and is the object that the rectangular matrix triple and the Hermitian matrices exhibit; and it formulates the descent, according to which the fixed subtriple is the real form of the triple and the structure is recovered by scalar extension. The article stays at the level of the ternary product and never forms a norm, a distance or an operator spectrum.

The article assumes *Jordan Algebras* for the binary product and the binary-to-ternary construction, *Jordan Algebras with an Involution* for the binary involution and its fixed part, *Involutive Bilinear Algebras* for the semilinear involution, *Algebras* for the objects, and *Tensor Products of Modules* for the scalar extension. The binary case is the companion article *Jordan Algebras with an Involution*, and the real forms are *Real Forms and the Descent of an Algebra*, both earlier in this group. Throughout, $R$ is a commutative ring with identity, $\varsigma$ is an involution of the scalars when a conjugate-linear involution is at hand, $T$ is a Jordan triple $R$-module, and $\sigma$ is a $\varsigma$-semilinear involution preserving the triple product; no form, norm, distance or order occurs.

## Jordan Triples

### Definition

**Definition.** A **Jordan triple system** over $R$ is an $R$-module $T$ with an $R$-trilinear map

$$
\{\cdot,\cdot,\cdot\} : T\times T\times T\to T
$$

such that for all $x, y, z, u, v \in T$

$$
\{x,y,z\} = \{z,y,x\}, \qquad
\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\}-\{u,\{y,x,v\},w\}+\{u,v,\{x,y,w\}\}.
$$

The first identity is the symmetry in the outer variables and the second is the **Jordan triple identity**.

**Proposition (the triple of a Jordan algebra).** Let $J$ be a Jordan algebra with product $\bullet$. Then

$$
\{x,y,z\} = (x\bullet y)\bullet z+(z\bullet y)\bullet x-(x\bullet z)\bullet y
$$

makes $J$ a Jordan triple system, and the linear map $y\mapsto \{x,y,x\}$ on $J$ is twice the quadratic representation $U_x$, $\{x,y,x\} = 2\,U_x(y)$.

*Proof.* The symmetry in $x$ and $z$ is the commutativity of $\bullet$; the Jordan triple identity is the linearisation of the Jordan identity $[L_x,L_{x^2}] = 0$, which the binary Jordan identity ensures. The identification $\{x,y,x\} = 2U_x(y)$ is the defining formula $U_x = 2L_x^2-L_{x^2}$ read on $y$. $\square$

**Definition (morphism).** A **homomorphism** of Jordan triple systems is an $R$-linear map $\varphi$ with $\varphi\{x,y,z\} = \{\varphi x,\varphi y,\varphi z\}$; an **anti-homomorphism** reverses the order of the arguments, and $T$ with the reversed arguments is the **opposite** triple.

## The Involution of a Jordan Triple

### Definition

**Definition.** A $\varsigma$-semilinear **involution** of a Jordan triple $T$ is a map $\sigma : T\to T$ with

$$
\sigma(x+y) = \sigma(x)+\sigma(y), \qquad \sigma(\lambda x) = \varsigma(\lambda)\sigma(x), \qquad \sigma\{x,y,z\} = \{\sigma x,\sigma y,\sigma z\}, \qquad \sigma^2 = \mathrm{id}.
$$

It is **linear** when $\varsigma = \mathrm{id}$ and **conjugate-linear** otherwise; a **Jordan triple with involution** is a pair $(T,\sigma)$.

**Theorem.** A $\varsigma$-semilinear involution of a Jordan triple is a bijective morphism of the ternary structure, its restriction to the scalar copy of $R$ is $\varsigma$, and it commutes with the operator $y\mapsto\{x,y,x\}$: $\sigma\{x,y,x\} = \{\sigma x,\sigma y,\sigma x\}$.

*Proof.* The preservation of the triple product is the third axiom; bijectivity is $\sigma^2 = \mathrm{id}$; the commuting with the outer operator is the product preservation read with the outer variables equal. $\square$

### The Fixed Sub-Triple

**Definition.** The **self-adjoint part** of $(T,\sigma)$ is

$$
H(T) = \{x \in T : \sigma(x) = x\},
$$

and the **skew** elements are those with $\sigma(x) = -x$.

**Theorem.** $H(T)$ is a sub-triple of $T$: if $x, y, z \in H(T)$ then $\{x,y,z\}\in H(T)$. If $\sigma$ is conjugate-linear over a quadratic extension $K/F$ with $K = F\oplus Fi$, $\varsigma(i) = -i$, then

$$
T = H(T)\oplus i\,H(T), \qquad H(T) = \{x : \sigma(x) = x\}, \qquad iH(T) = \{x : \sigma(x) = -x\},
$$

and $H(T)$ is the **fixed subtriple**, a Jordan triple over the fixed field $F$.

*Proof.* For the closure, $\sigma\{x,y,z\} = \{\sigma x,\sigma y,\sigma z\} = \{x,y,z\}$ when the three arguments are self-adjoint. The decomposition is the one of *Jordan Algebras with an Involution*: $h_1 = \tfrac12(x+\sigma x)$ and $h_2 = \tfrac{1}{2i}(x-\sigma x)$ are self-adjoint and $x = h_1+ih_2$. The ternary product of the fixed field is the restriction. $\square$

**Corollary.** The fixed subtriple $H(T)$ is the set of the self-adjoint elements and is a Jordan triple over the fixed field; the map $x\mapsto \sigma(x)$ is the identity on $H(T)$ and the negation on the skew part, and it is the semilinear extension of the identity of $H(T)$.

## The Case of a Jordan Algebra

### The Binary-to-Ternary Involution

**Theorem.** Let $J$ be a Jordan algebra with a $\varsigma$-semilinear involution $\sigma$ in the sense of *Jordan Algebras with an Involution*, and let $T = J$ be the associated Jordan triple. Then $\sigma$ is a $\varsigma$-semilinear involution of $T$, and the fixed subtriple of $T$ is the triple of the self-adjoint part:

$$
H(T) = H(J), \qquad \{x,y,z\} = (x\bullet y)\bullet z+(z\bullet y)\bullet x-(x\bullet z)\bullet y \ \text{ on } \ H(J) .
$$

*Proof.* The preservation of the ternary product follows from the preservation of the binary product: $\sigma\{x,y,z\} = (\sigma x\bullet\sigma y)\bullet\sigma z+\cdots = \{\sigma x,\sigma y,\sigma z\}$; the fixed sites coincide by definition. $\square$

**Corollary.** The involution of a Jordan triple restricts to the involution of any Jordan subalgebra that it preserves, and the fixed subtriple of the triple of $J$ is the Jordan triple of the fixed subalgebra; in particular the theory of the involutions of a Jordan triple contains that of the involutions of a Jordan algebra.

### The Descent

**Theorem (descent).** Let $T$ be a $K$-Jordan triple with a conjugate-linear involution $\sigma$ over a quadratic extension $K/F$. Then the fixed subtriple is an $F$-Jordan triple and $T = H(T)\otimes_F K$ as $K$-triples with the involution $\mathrm{id}\otimes\varsigma$; a $\sigma$-equivariant $K$-linear morphism of triples is the scalar extension of its restriction to $H(T)$.

*Proof.* The scalar extension of $H(T)$ by $K$ is $H(T)\oplus iH(T) = T$; the tensor product of triples is taken componentwise and the ternary product is $K$-trilinear; a $\sigma$-equivariant map preserves $H(T)$ and is $K$-linear, hence determined by its restriction. $\square$

**Corollary.** The fixed subtriple is the **real form** of the triple, and the passing to the fixed subtriple is the ternary analogue of the descent of *Real Forms and the Descent of an Algebra*.

## Examples

**Example (the rectangular matrix triple).** Let $T = M_{p,q}(\mathbb{C})$ with the triple $\{x,y,z\} = xy^*z+zy^*x$, where $y^* = \bar y^{\mathsf{T}}$ is the conjugate transpose. This is a Jordan triple, and the map $\sigma(x) = x^*$ is a conjugate-linear involution of $T$: $\sigma\{x,y,z\} = (xy^*z+zy^*x)^* = z^*yx^*+x^*yz^* = \{z^*,y^*,x^*\}$, which is $\{x^*,y^*,z^*\}$ by the outer symmetry. The fixed subtriple $H(T) = \{x : x^* = x\}$ is the space of the Hermitian matrices, nonzero only when $p = q$.

**Example (the Hermitian matrices).** For $p = q = n$ the fixed subtriple $H(T)$ is the space of the Hermitian $n\times n$ matrices, and the ternary product $\{x,y,z\} = xy z+z y x$ restricts to it; this is the triple of the formally real Jordan algebra $H_n(\mathbb{C})$, and its positive structure is the one of *Formally Real Algebras and the Sum of Squares*.

**Example (the binary reduction).** For a Jordan algebra $J$ with involution and the trivial ternary involution the fixed subtriple is $J$ itself; for the involution $\sigma = \mathrm{id}$ the whole triple is fixed, and for the triple of a formally real algebra the fixed subtriple is the ordered object of Part IV.

## Summary

A **Jordan triple system** is a module with a trilinear product symmetric in the outer variables and satisfying the Jordan triple identity; a Jordan algebra yields such a triple by $\{x,y,z\} = (x\bullet y)\bullet z+(z\bullet y)\bullet x-(x\bullet z)\bullet y$, with $\{x,y,x\} = 2U_x(y)$. A $\varsigma$-semilinear **involution** of the triple preserves the ternary product and is of order two; its fixed set, the **self-adjoint part** $H(T)$, is a sub-triple, and over a quadratic extension $K/F$ the triple splits as $T = H(T)\oplus iH(T)$, so the fixed subtriple is a **real form** of $T$ and the structure descends to it. The triple of a Jordan algebra with involution inherits the involution, and its fixed subtriple is the triple of the self-adjoint part, so the triple theory contains the binary theory. The rectangular matrix triple with the conjugate transpose is the standard example, its fixed subtriple being the Hermitian matrices. No form, norm, distance or order occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T$ | Jordan triple system over $R$ |
| $\{x,y,z\}$ | Ternary product |
| $\{x,y,z\}=\{z,y,x\}$ | Outer symmetry |
| $\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\}-\{u,\{y,x,v\},w\}+\{u,v,\{x,y,w\}\}$ | Jordan triple identity |
| $\{x,y,z\}=(x\bullet y)\bullet z+(z\bullet y)\bullet x-(x\bullet z)\bullet y$ | Triple of a Jordan algebra |
| $\sigma$ | $\varsigma$-semilinear involution of $T$ |
| $H(T)$ | Self-adjoint part, the fixed subtriple |
| $T = H(T)\oplus iH(T)$ | Decomposition over a quadratic extension |
| $H(T) = H(J)$ | Fixed subtriple of the triple of $J$ |
| $M_{p,q}(\mathbb{C})$, $\{x,y,z\}=xy^*z+zy^*x$ | Rectangular matrix example |

## Further Reading

- Ottmar Loos, *Jordan Pairs* (Springer Lecture Notes in Mathematics 460, 1975), for Jordan triple systems, their identities and their structure.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the binary-to-ternary transition and the involutions.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan triple of an algebra and the quadratic representation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions, the descent and the real forms.
- Erhard Neher, *Jordan Triple Systems by the Grid Approach* (Springer Lecture Notes in Mathematics 1280, 1987), for the rectangular triples and the classification of the Jordan triples.
